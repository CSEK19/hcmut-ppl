"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from StaticError import *


class CType:
    pass


class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype


class Symbol:
    def __init__(self, name, mtype, value=None, kind=None, scope=None, class_member=None,
                 parent_class_name=None, is_constant=False, is_stmt=None):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.kind = kind
        self.scope = scope
        self.class_member = class_member
        self.parent_class_name = parent_class_name
        self.is_constant = is_constant
        self.is_stmt = is_stmt


c_program = []
return_type_stack = []
is_constant_stack = []


class StaticChecker(BaseVisitor):

    global_envi = [
        Symbol("getInt", MType([], IntType())),
        Symbol("putIntLn", MType([IntType()], VoidType()))
    ]

    array_flag = True

    def __init__(self,ast):
        self.ast = ast

    def check(self):
        global c_program
        global return_type_stack
        global is_constant_stack

        c_program = []
        return_type_stack = []
        is_constant_stack = []

        self.visit(self.ast, c_program)

        flag = checkNoEntryPoint(c_program)
        if not flag:
            raise NoEntryPoint()

        return

    def visitProgram(self, ast:Program, c):
        global c_program

        for class_decl in ast.decl:
            self.visit(class_decl, c)
        c_program = c.copy()

        return

    def visitClassDecl(self, ast:ClassDecl, c):
        for class_name in c:
            if type(class_name.mtype) is CType:
                self.visit(ast.classname, ([class_name], Class()))

        parent_class_name = None
        if ast.parentname:
            parent_class_name = self.visit(ast.parentname, (c, 'CHECK_UNDECLARED_CLASS', Class(), ast.parentname.name))

        c.append(Symbol(ast.classname.name, CType(), None, parent_class_name=parent_class_name))
        lower_scope = len(c)

        for mem in ast.memlist:
            self.visit(mem, (c, lower_scope))
        new_class = []
        for element in c:
            if element.name == ast.classname.name:
                new_class = element
                break
        new_class.scope = (lower_scope, len(c))

        return

    def visitId(self, ast:Id, c):
        if not isinstance(c, tuple):
            obj = []
            for element in reversed(c):
                if element.name == ast.name:
                    obj = element
                    break
                elif isinstance(element.mtype, (CType, MType)):
                    raise Undeclared(Identifier(), ast.name)
            if obj:
                return obj.mtype
            else:
                raise Undeclared(Variable(), ast.name)

        inst = c[1]
        if inst == 'CHECK_UNDECLARED_IDENTIFIER':
            for element in reversed(c[0]):
                if element.name == ast.name:
                    return ast.name
                elif isinstance(element.mtype, (CType, MType)):
                    raise Undeclared(Identifier(), ast.name)

        elif inst == 'CHECK_UNDECLARED_CLASS':
            lst_class = []
            for class_name in c[0]:
                if type(class_name.mtype) is CType:
                    lst_class.append(class_name.name)
            if c[3] not in lst_class:
                raise Undeclared(c[2], ast.name)

        elif inst == 'CHECK_UNDECLARED_ATTRIBUTE':
            obj = []
            for element in c[0]:
                if element.name == c[3] and type(element.mtype) != MType:
                    obj = element
                    break

            if not obj:
                raise Undeclared(c[2], ast.name)

            obj_class = []
            if type(obj.mtype) == ClassType:
                for element in c[0]:
                    if type(element.mtype) is CType and element.name == obj.mtype.classname.name:
                        obj_class = element
                        break

                if not obj_class:
                    raise Undeclared(c[2], ast.name)
            else:
                obj_class = obj

            lst_class_member = getAllMemberClassID(c, obj_class.name, is_attribute=True)

            if ast.name not in lst_class_member:
                raise Undeclared(c[2], ast.name)

        elif inst == 'CHECK_UNDECLARED_METHOD':
            obj = []
            for element in c[0]:
                if element.name == c[3] and type(element.mtype) != MType:
                    obj = element
                    break

            if not obj:
                raise Undeclared(c[2], ast.name)

            obj_class = []
            for class_name in c[0]:
                if type(class_name.mtype) is CType and class_name.name == obj.mtype.classname.name:
                    obj_class = class_name
                    break

            lst_class_member = getAllMemberClassID(c, obj_class.name, is_attribute=False)

            if ast.name not in lst_class_member:
                raise Undeclared(c[2], ast.name)

        elif inst == 'CHECK_CONSTANT_ASSIGN':
            lst_obj = []
            for element in c[0]:
                lst_obj.append(element)
            obj = lst_obj[-1]

            if obj.is_constant:
                raise CannotAssignToConstant(c[2])

        elif inst == 'CHECK_ILLEGAL_MEMBER_ACCESS':
            for element in reversed(c[0]):
                if element.name == ast.name and type(element.mtype) == ClassType:
                    return 'VAR'
                elif isinstance(element.mtype, CType) or element.is_stmt == 'BLOCK':
                    for class_name in c[0]:
                        if ast.name == class_name.name and isinstance(class_name.mtype, CType):
                            return 'CLASS'
            raise Undeclared(Identifier(), ast.name)

        elif inst == 'CHECK_RETURN_IDENTIFIER':
            obj = []
            for element in reversed(c[0]):
                if element.name == ast.name:
                    obj = element
                    break
                elif isinstance(element.mtype, (CType, MType)):
                    raise Undeclared(Identifier(), ast.name)
            if obj:
                return obj.is_constant, obj.mtype
            else:
                raise Undeclared(Variable(), ast.name)

        elif inst == 'CHECK_CONSTRUCTOR_PARAM':
            obj = []
            for element in reversed(c[0]):
                if element.name == ast.name:
                    obj = element
                    break
                elif isinstance(element.mtype, (CType, MType)):
                    raise Undeclared(Identifier(), ast.name)
            if obj:
                return obj.mtype
            else:
                raise Undeclared(Variable(), ast.name)

        elif inst == 'CHECK_REDECLARED_METHOD':
            for element in c[0]:
                if element.name == ast.name and type(element.mtype) == MType:
                    raise Redeclared(c[2], ast.name)

        else:
            for element in c[0]:
                if element.name == ast.name:
                    raise Redeclared(c[1], ast.name)

        return ast.name

    def visitMethodDecl(self, ast:MethodDecl, c_scope):
        global return_type_stack
        global is_constant_stack

        c, lower_scope = c_scope
        m_name = self.visit(ast.name, (c[lower_scope:], 'CHECK_REDECLARED_METHOD', Method()))
        m_type = MType([], None)
        c.append(Symbol(m_name, m_type, kind=ast.kind, class_member=True))

        lower_scope = len(c)
        for param in ast.param:
            self.visit(param, (c, lower_scope, 'PARAM_DECL'))

        self.visit(ast.body, (c, lower_scope))

        new_method = []
        for element in c:
            if type(element.mtype) == MType and element.name == ast.name.name:
                new_method = element

        new_method.scope = (lower_scope, len(c))
        for element in ast.param:
            new_method.mtype.partype.append(element.varType)

        if return_type_stack:
            new_method.mtype.rettype = return_type_stack.pop()
            new_method.is_constant = is_constant_stack.pop()
        else:
            new_method.mtype.rettype = VoidType()
            new_method.is_constant = False

        return_type_stack = []
        is_constant_stack = []

        return

    def visitAttributeDecl(self, ast, c_scope):
        c, lower_scope = c_scope
        if type(ast.decl) is VarDecl:
            attr_name = self.visit(ast.decl.variable, (c[lower_scope:], Attribute()))
            attr_type = ast.decl.varType
            attr_value = ast.decl.varInit
        else:
            attr_name = self.visit(ast.decl.constant, (c[lower_scope:], Attribute()))
            attr_type = ast.decl.constType
            attr_value = ast.decl.value
            flag = checkIllegalConstantExpression(attr_value, c)
            if not flag:
                raise IllegalConstantExpression(attr_value)
        attr_kind = ast.kind

        if type(attr_type) is ClassType:
            inst = "CHECK_UNDECLARED_CLASS"
            self.visit(attr_type.classname, (c, inst, Class(), attr_type.classname.name))

        if not ((attr_value is None) or (isinstance(attr_value, NullLiteral))):
            if type(attr_type) is ArrayType:
                self.array_flag = True
            rhs_type = self.visit(attr_value, c)

            if type(attr_type) is ArrayType and not self.array_flag:
                raise IllegalArrayLiteral(attr_value)

            flag_type = checkType(attr_type, rhs_type, c)
            flag_id = checkIdentifierAttributeDecl(attr_value, c)

            if type(ast.decl) == VarDecl:
                if not (flag_id and flag_type):
                    raise TypeMismatchInStatement(ast.decl)
                if type(attr_type) == ArrayType:
                    if not checkArrayType(attr_type, rhs_type, c):
                        raise TypeMismatchInStatement(ast.decl)
            elif type(ast.decl) == ConstDecl:
                if not (flag_id and flag_type):
                    raise TypeMismatchInConstant(ast.decl)
                if type(attr_type) == ArrayType:
                    if not checkArrayType(attr_type, rhs_type, c):
                        raise TypeMismatchInConstant(ast.decl)

            if type(rhs_type) == ClassType:
                last_class = list(filter(lambda x: x.name == rhs_type.classname.name, c))[-1]
                if last_class.parent_class_name == attr_type.classname.name and\
                        rhs_type.classname.name == last_class.name:
                    if type(ast.decl) == VarDecl:
                        raise TypeMismatchInStatement(ast.decl)
                    else:
                        raise TypeMismatchInConstant(ast.decl)

        if type(ast.decl) is VarDecl:
            c.append(Symbol(attr_name, attr_type, attr_value, attr_kind, class_member=True))
        else:
            c.append(Symbol(attr_name, attr_type, attr_value, attr_kind, class_member=True, is_constant=True))

        return

    def visitVarDecl(self, ast:VarDecl, c_scope_inst):
        c, lower_scope, inst = c_scope_inst
        var_type = ast.varType
        var_value = ast.varInit
        var_kind = Instance()

        if type(var_type) is ClassType:
            inst = "CHECK_UNDECLARED_CLASS"
            self.visit(ast.varType.classname, (c, inst, Class(), var_type.classname.name))

        if not ((var_value is None) or (isinstance(var_value, NullLiteral))):
            if type(var_type) is ArrayType:
                self.array_flag = True

            rhs_type = self.visit(var_value, c)

            if type(var_type) is ArrayType and not self.array_flag:
                raise IllegalArrayLiteral(var_value)

            flag = checkType(ast.varType, rhs_type, c)
            if not flag:
                raise TypeMismatchInStatement(ast)

            if type(rhs_type) == ArrayType:
                flag_array = checkArrayType(ast.varType, rhs_type, c)
                if not flag_array:
                    raise TypeMismatchInStatement(ast)

        if inst == 'PARAM_DECL':
            var_name = self.visit(ast.variable, (c[lower_scope:], Parameter()))
        else:
            var_name = self.visit(ast.variable, (c[lower_scope:], Variable()))

        c.append(Symbol(var_name, var_type, var_value, var_kind, is_constant=False))

        return

    def visitConstDecl(self, ast:ConstDecl, c_scope_inst):
        c, lower_scope, inst = c_scope_inst
        var_name = self.visit(ast.constant, (c[lower_scope:], Constant()))
        var_type = ast.constType
        var_value = ast.value
        var_kind = Instance()

        if not var_value:
            raise IllegalConstantExpression(None)
        rhs_type = self.visit(var_value, c)

        if type(var_type) is ArrayType and not self.array_flag:
            raise IllegalArrayLiteral(var_value)

        flag_const = checkIllegalConstantExpression(var_value, c)
        if not flag_const:
            raise IllegalConstantExpression(var_value)

        if not ((var_value is None) or (isinstance(var_value, NullLiteral))):
            flag = checkType(var_type, rhs_type, c)
            if not flag:
                raise TypeMismatchInConstant(ast)

        c.append(Symbol(var_name, var_type, var_value, var_kind, is_constant=True))
        return

    def visitBlock(self, ast:Block, c_scope):
        c, lower_scope = c_scope
        new_block = Symbol('STMT_BLOCK', mtype=None, is_stmt='BLOCK')
        c.append(new_block)
        upper_scope = len(c)

        for instructor in ast.inst:
            if type(instructor) in [VarDecl, ConstDecl]:
                self.visit(instructor, (c, lower_scope, 'DECL'))
            elif type(instructor) in [Block]:
                self.visit(instructor, (c, len(c)))
            elif type(instructor) in [Assign]:
                self.visit(instructor, (c, lower_scope))
            elif type(instructor) in [CallStmt]:
                self.visit(instructor, (c, lower_scope))
            elif type(instructor) in [If]:
                self.visit(instructor, c)
            elif type(instructor) in [For]:
                self.visit(instructor, c)
            elif type(instructor) in [Break]:
                self.visit(instructor, c)
            elif type(instructor) in [Continue]:
                self.visit(instructor, c)
            elif type(instructor) in [Return]:
                self.visit(instructor, c)

        new_block.scope = (upper_scope, len(c))
        return

    def visitAssign(self, ast:Assign, c_scope):
        c, lower_scope = c_scope
        this_obj = []
        obj_class = []

        lhs_type = None
        rhs_type = None

        if type(ast.lhs) == FieldAccess:
            if type(ast.lhs.obj) == Id:
                self.visit(ast.lhs.fieldname, (c, 'CHECK_UNDECLARED_ATTRIBUTE', Attribute(), ast.lhs.obj.name))
                lhs_type = self.visit(ast.lhs, c)
                obj_type = []
                for element in c:
                    if element.name == ast.lhs.obj.name and isinstance(element.mtype, (CType, ClassType)):
                        obj_type = element
                if type(obj_type) == ClassType:
                    for element in c:
                        if element.name == obj_type.mtype.classname.name and type(element.mtype) == CType:
                            obj_class = element
                            break
                else:
                    obj_class = obj_type

                if obj_class.scope:
                    upper_scope, lower_scope = obj_class.scope
                    for element in c[upper_scope:lower_scope]:
                        if element.name == ast.lhs.fieldname.name and element.class_member:
                            this_obj = element
                            break
                else:
                    upper_scope = c.index(obj_class) + 1
                    for element in c[upper_scope:]:
                        if element.name == ast.lhs.fieldname.name and element.class_member:
                            this_obj = element
                            break

            elif type(ast.lhs.obj) == SelfLiteral:
                if not checkSelfStaticMethod(ast.lhs, c):
                    raise IllegalMemberAccess(ast.lhs)

                obj_class = []
                for element in c:
                    if type(element.mtype) == CType:
                        obj_class = element
                upper_scope = c.index(obj_class) + 1
                for element in c[upper_scope:]:
                    if element.name == ast.lhs.fieldname.name and element.class_member:
                        this_obj = element
                        lhs_type = this_obj.mtype
                        break
                rhs_type = self.visit(ast.exp, (c, 'CHECK_CONSTRUCTOR_PARAM'))

        elif type(ast.lhs) == ArrayCell:
            if type(ast.lhs.arr) == Id:
                for element in c:
                    if element.name == ast.lhs.arr.name:
                        if type(element.mtype) != ArrayType:
                            raise TypeMismatchInExpression(ast.lhs)
                        else:
                            break

                for idx in ast.lhs.idx:
                    if not(isinstance(idx, IntLiteral)):
                        if isinstance(idx, Id):
                            self.visit(idx, (c, 'CHECK_UNDECLARED_IDENTIFIER', Identifier()))
                        else:
                            raise TypeMismatchInExpression(ast.lhs)

                for element in c:
                    if element.name == ast.lhs.arr.name:
                        lhs_type = element.mtype.eleType
                        this_obj = element

        elif type(ast.lhs) == Id:
            rhs_type = self.visit(ast.exp, c)

            self.visit(ast.lhs, (c, 'CHECK_UNDECLARED_IDENTIFIER', Identifier()))
            self.visit(ast.lhs, (c, 'CHECK_CONSTANT_ASSIGN', ast))
            for element in c:
                if element.name == ast.lhs.name:
                    this_obj = element
                    lhs_type = element.mtype

        if not rhs_type:
            rhs_type = self.visit(ast.exp, c)

        if type(ast.exp) == NewExpr:
            for element in c:
                if element.name == this_obj.mtype.classname.name and type(element.mtype) == CType:
                    obj_class = element
                    break
            for element in c:
                if element.name == rhs_type.classname.name and type(element.mtype) == CType and \
                        element.parent_class_name == obj_class.name:
                    raise TypeMismatchInStatement(ast)

        if this_obj:
            if this_obj.is_constant:
                raise CannotAssignToConstant(ast)

            if type(ast.lhs) == ArrayCell:
                str_mtype = str(this_obj.mtype)
                array_dimension = str_mtype.count('Array')
                if array_dimension < len(ast.lhs.idx):
                    raise TypeMismatchInExpression(ast.lhs)

            if type(this_obj.mtype) == ArrayType and type(ast.exp) == ArrayLiteral:
                if this_obj.mtype.size != len(ast.exp.value):
                    raise TypeMismatchInStatement(ast)

                if not rhs_type:
                    raise IllegalArrayLiteral(ast.exp)

                flag_array = checkArrayType(this_obj.mtype, rhs_type, c)
                if not flag_array:
                    raise TypeMismatchInStatement(ast)

        flag = checkType(lhs_type, rhs_type, c)
        if not flag and type(ast.lhs) is not ArrayCell:
            raise TypeMismatchInStatement(ast)

        return

    def visitUnaryOp(self, ast:UnaryOp, c):
        op = ast.op
        exp = self.visit(ast.body, c)

        if op in ['-']:
            if isinstance(exp, (IntType, FloatType)) is False:
                raise TypeMismatchInExpression(ast)
            return IntType() if isinstance(exp, IntType) else FloatType()

        if op in ['!']:
            if isinstance(exp, BoolType) is False:
                raise TypeMismatchInExpression(ast)
            return BoolType()

    def visitBinaryOp(self, ast:BinaryOp, c):
        op = ast.op
        left = self.visit(ast.left, c)
        right = self.visit(ast.right, c)

        if op in ['+', '-', '*', '/']:
            if isinstance(left, (IntType, FloatType)) is False or isinstance(right, (IntType, FloatType)) is False:
                raise TypeMismatchInExpression(ast)
            if isinstance(left, FloatType) or isinstance(right, FloatType):
                return FloatType()
            return IntType()

        elif op in ['==.', '+.']:
            if isinstance(left, StringType) is False or isinstance(right, StringType) is False:
                raise TypeMismatchInExpression(ast)
            if op == '==.':
                return BoolType()
            return StringType()

        elif op in ['||', '&&']:
            if isinstance(left, BoolType) is False or isinstance(right, BoolType) is False:
                raise TypeMismatchInExpression(ast)
            return BoolType()

        elif op in ['==', '!=']:
            if (isinstance(left, IntType) and isinstance(right, IntType)) or \
                    (isinstance(left, BoolType) and isinstance(right, BoolType)):
                return BoolType()
            else:
                raise TypeMismatchInExpression(ast)

        elif op in ['<', '>', '<=', '>=']:
            if isinstance(left, (IntType, FloatType)) is False or isinstance(right, (IntType, FloatType)) is False:
                raise TypeMismatchInExpression(ast)
            return BoolType()

        elif op in ['%']:
            if isinstance(left, IntType) is False or isinstance(right, IntType) is False:
                raise TypeMismatchInExpression(ast)
            return IntType()

        return

    def visitCallStmt(self, ast:CallStmt, c_scope):
        c, lower_scope = c_scope
        obj = []
        obj_method = []
        obj_class = []

        if ast.method.name[0] == '$':
            self.visit(ast.obj, (c, 'CHECK_UNDECLARED_CLASS', Class(), ast.obj.name))

        if type(ast.obj) == Id:
            obj_type = self.visit(ast.obj, (c, 'CHECK_ILLEGAL_MEMBER_ACCESS', ast))

            if obj_type == 'VAR':
                if ast.method.name[0] == '$':
                    raise IllegalMemberAccess(ast)
                self.visit(ast.method, (c, 'CHECK_UNDECLARED_METHOD', Method(), ast.obj.name))
                for element in c:
                    if element.name == ast.obj.name and type(element.mtype) != MType:
                        obj = element
                if type(obj.mtype) != ClassType:
                    raise TypeMismatchInStatement(ast)
                for element in c:
                    if element.name == obj.mtype.classname.name and type(element.mtype) == CType:
                        obj_class = element
                        break

            elif obj_type == 'CLASS':
                if ast.method.name[0] != '$':
                    raise IllegalMemberAccess(ast)
                for element in c:
                    if element.name == ast.obj.name and type(element.mtype) == CType:
                        obj_class = element
                        break

            lst_obj_class_method = getAllMemberClass(c, obj_class.name, is_attribute=False)
            for element in lst_obj_class_method:
                if element.name == ast.method.name:
                    obj_method = element

        elif type(ast.obj) == SelfLiteral:
            if not checkSelfStaticMethod(ast, c):
                raise IllegalMemberAccess(ast)

            for element in reversed(c):
                if element.name == ast.method.name and type(element.mtype) == MType and element.class_member:
                    obj_method = element
                    break
                elif type(element.mtype) == CType:
                    break

        elif type(ast.obj) in (CallExpr, FieldAccess):
            obj_type = self.visit(ast.obj, c)
            for element in c:
                if element.name == obj_type.classname.name and isinstance(element.mtype, CType):
                    obj_class = element
                    break
            upper_scope, lower_scope = obj_class.scope
            for element in c[upper_scope:lower_scope]:
                if element.name == ast.method.name and isinstance(element.mtype, MType):
                    obj_method = element
                    break

        if not obj_method:
            raise Undeclared(Method(), ast.method.name)

        if type(obj_method.mtype.rettype) is not VoidType:
            raise TypeMismatchInStatement(ast)

        lst_expr_param = []
        for element in ast.param:
            lst_expr_param.append(type(self.visit(element, c)))

        lst_obj_param = []
        for element in obj_method.mtype.partype:
            lst_obj_param.append(type(element))

        flag = checkParamEqual(lst_expr_param, lst_obj_param)
        if not flag:
            raise TypeMismatchInStatement(ast)
        return obj_method.mtype.rettype

    def visitCallExpr(self, ast:CallExpr, c):
        obj = []
        obj_method = []
        obj_class = []

        if ast.method.name[0] == '$':
            self.visit(ast.obj, (c, 'CHECK_UNDECLARED_CLASS', Class(), ast.obj.name))

        if type(ast.obj) == Id:
            obj_type = self.visit(ast.obj, (c, 'CHECK_ILLEGAL_MEMBER_ACCESS', ast))
            if obj_type == 'VAR':
                if ast.method.name[0] == '$':
                    raise IllegalMemberAccess(ast)
                for element in c:
                    if element.name == ast.obj.name:
                        obj = element
                if type(obj.mtype) != ClassType:
                    raise TypeMismatchInExpression(ast)
                for element in c:
                    if type(element.mtype) == CType and element.name == obj.mtype.classname.name:
                        obj_class = element
                        break
            elif obj_type == 'CLASS':
                if ast.method.name[0] != '$':
                    raise IllegalMemberAccess(ast)
                for element in c:
                    if element.name == ast.obj.name and type(element.mtype) == CType:
                        obj_class = element
                        break

        elif type(ast.obj) == SelfLiteral:
            if not checkSelfStaticMethod(ast, c):
                raise IllegalMemberAccess(ast)

            for element in c:
                if type(element.mtype) == CType:
                    obj_class.append(element)
            obj_class = obj_class[-1]

        elif type(ast.obj) in (FieldAccess, CallExpr):
            obj_class_type = self.visit(ast.obj, c)
            for element in c:
                if element.name == obj_class_type.classname.name and isinstance(element.mtype, CType):
                    obj_class = element
                    break

        if obj_class.scope:
            upper_scope, lower_scope = obj_class.scope
            for element in c[upper_scope:lower_scope]:
                if element.class_member and element.name == ast.method.name and type(element.mtype) == MType:
                    obj_method = element
                    break
        else:
            upper_scope = c.index(obj_class) + 1
            for element in c[upper_scope:]:
                if element.class_member and element.name == ast.method.name and type(element.mtype) == MType:
                    obj_method = element

        if not obj_method:
            raise Undeclared(Method(), ast.method.name)

        if type(obj_method.mtype.rettype) is VoidType:
            raise TypeMismatchInExpression(ast)

        lst_expr_param = []
        for element in ast.param:
            lst_expr_param.append(type(self.visit(element, c)))

        lst_obj_param = []
        for element in obj_method.mtype.partype:
            lst_obj_param.append(type(element))

        flag = checkParamEqual(lst_expr_param, lst_obj_param)
        if not flag:
            raise TypeMismatchInExpression(ast)

        return obj_method.mtype.rettype

    def visitReturn(self, ast:Return, c):
        global return_type_stack
        global is_constant_stack

        nearest_method = list(filter(lambda x:isinstance(x.mtype,MType), c))[-1]
        nearest_class = list(filter(lambda x: isinstance(x.mtype, CType), c))[-1]

        if nearest_method.name == 'Constructor':
            if ast.expr:
                raise TypeMismatchInStatement(ast)
        elif nearest_method.name == 'Destructor':
            if ast:
                raise TypeMismatchInStatement(ast)
        elif nearest_class.name == 'Program' and nearest_method.name == 'main':
            if ast:
                raise TypeMismatchInStatement(ast)

        if not ast.expr:
            return

        is_constant = False
        if type(ast.expr) == Id:
            is_constant, new_return_type = self.visit(ast.expr, (c, 'CHECK_RETURN_IDENTIFIER'))
        else:
            new_return_type = self.visit(ast.expr, c)

        if return_type_stack:
            if type(new_return_type) != type(return_type_stack[0]):
                raise TypeMismatchInStatement(ast)

        return_type_stack.append(new_return_type)
        is_constant_stack.append(is_constant)

        return

    def visitFieldAccess(self, ast:FieldAccess, c):
        obj = []
        obj_class = []

        if ast.fieldname.name[0] == '$':
            self.visit(ast.obj, (c, 'CHECK_UNDECLARED_CLASS', Class(), ast.obj.name))

        if type(ast.obj) == Id:
            obj_type = self.visit(ast.obj, (c, 'CHECK_ILLEGAL_MEMBER_ACCESS', ast))

            if obj_type == 'VAR':
                if ast.fieldname.name[0] == '$':
                    raise IllegalMemberAccess(ast)
                for element in c:
                    if ast.obj.name == element.name and type(element.mtype) != MType:
                        obj = element

                if type(obj.mtype) != ClassType:
                    raise TypeMismatchInExpression(ast)

                for element in c:
                    if element.name == obj.mtype.classname.name and type(element.mtype) == CType:
                        obj_class = element
                        break

            elif obj_type == 'CLASS':
                if ast.fieldname.name[0] != '$':
                    raise IllegalMemberAccess(ast)

                for element in c:
                    if element.name == ast.obj.name and type(element.mtype) == CType:
                        obj_class = element
                        break

            lst_class_member = getAllMemberClass(c, obj_class.name, is_attribute=True)
            lst_same_name_obj = []
            for element in lst_class_member:
                if ast.fieldname.name == element.name:
                    lst_same_name_obj.append(element)
            if len(lst_same_name_obj) == 0:
                raise Undeclared(Attribute(), ast.fieldname.name)

            return lst_same_name_obj[-1].mtype

        elif type(ast.obj) == SelfLiteral:
            obj_method_inside = []
            for element in reversed(c):
                if type(element.mtype) == MType:
                    obj_method_inside = element
                    break
                elif type(element.mtype) == CType:
                    break

            if obj_method_inside and isinstance(obj_method_inside.kind, Static):
                raise IllegalMemberAccess(ast)

            for element in c:
                if type(element.mtype) == CType:
                    obj_class.append(element)

            obj_class = obj_class[-1]
            upper_scope = c.index(obj_class) + 1
            lst_attr = []
            for element in c[upper_scope:]:
                if element.class_member and type(element.mtype) != MType:
                    lst_attr.append(element)

            flag = False
            obj = []
            for attr in lst_attr:
                if attr.name == ast.fieldname.name:
                    obj = attr
                    flag = True
            if flag:
                return obj.mtype
            else:
                raise Undeclared(Attribute(), ast.fieldname.name)

        elif type(ast.obj) in (CallExpr, FieldAccess, NewExpr):
            obj_type = self.visit(ast.obj, c)

            if isinstance(obj_type, ClassType):
                for element in c:
                    if element.name == obj_type.classname.name and type(element.mtype) == CType:
                        obj_class = element

            lst_class_member = getAllMemberClass(c, obj_class.name, is_attribute=True)
            lst_same_name_obj = []
            for element in lst_class_member:
                if ast.fieldname.name == element.name:
                    lst_same_name_obj.append(element)
            if len(lst_same_name_obj) == 0:
                raise Undeclared(Attribute(), ast.fieldname.name)

            return lst_same_name_obj[-1].mtype

    def visitFor(self, ast:For, c):
        new_for = Symbol('STMT_FOR', mtype=None, is_stmt='FOR')
        c.append(new_for)
        self.visit(ast.id, (c, 'CHECK_UNDECLARED_IDENTIFIER', Identifier()))

        obj = []
        for element in reversed(c):
            if element.name == ast.id.name and not isinstance(element.mtype, (CType, MType)):
                obj = element
            elif isinstance(element.mtype, (CType, MType)):
                break

        if obj.is_constant:
            raise CannotAssignToConstant(Assign(ast.id, ast.expr1))
        expr1 = self.visit(ast.expr1, c)
        expr2 = self.visit(ast.expr2, c)
        upper_scope = len(c)
        if not (checkType(expr1, IntType(), c) and checkType(expr2, IntType(), c)):
            raise TypeMismatchInStatement(ast)
        expr3 = None
        if ast.expr3 is not None:
            expr3 = self.visit(ast.expr3, c)
        self.visit(ast.loop, (c, upper_scope))
        new_for.scope = (upper_scope, len(c))

        return

    def visitBreak(self, ast:Break, c):
        for element in reversed(c):
            if element.is_stmt == 'FOR':
                if element.scope is None:
                    break
            if isinstance(element.mtype, (CType, MType)):
                raise MustInLoop(ast)

        return

    def visitIf(self, ast:If, c):
        new_if = Symbol('STMT_IF', mtype=None, is_stmt='IF')
        c.append(new_if)
        upper_scope = len(c)
        self.visit(ast.expr, c)
        self.visit(ast.thenStmt, (c, upper_scope))
        if ast.elseStmt is not None and not isinstance(ast.elseStmt, If):
            upper_scope = len(c)
            self.visit(ast.elseStmt, (c,upper_scope))
        elif ast.elseStmt is not None and isinstance(ast.elseStmt, If):
            self.visit(ast.elseStmt, c)
        new_if.scope = (upper_scope, len(c))

        return

    def visitContinue(self, ast: Continue, c):
        for element in reversed(c):
            if element.is_stmt == 'FOR':
                if element.scope is None:
                    break
            if isinstance(element.mtype, (CType, MType)):
                raise MustInLoop(ast)

        return

    def visitIntLiteral(self, ast:IntLiteral, c):
        return IntType()

    def visitFloatLiteral(self, ast:FloatLiteral, c):
        return FloatType()

    def visitBooleanLiteral(self, ast:BooleanLiteral, c):
        return BoolType()

    def visitStringLiteral(self, ast:StringLiteral, c):
        return StringType()

    def visitNullLiteral(self, ast:NullLiteral, c):
        return NullLiteral()

    def visitNewExpr(self, ast:NewExpr, c):
        obj_class = []
        obj_constructor = []
        for element in c:
            if element.name == ast.classname.name and isinstance(element.mtype, CType):
                obj_class = element
                break

        if not obj_class:
            raise Undeclared('Class', ast.classname.name)

        if obj_class.scope:
            upper_scope, lower_scope = obj_class.scope
            for element in c[upper_scope:lower_scope]:
                if element.name == 'Constructor' and isinstance(element.mtype, MType):
                    obj_constructor = element
                    break
        else:
            upper_scope = c.index(obj_class) + 1
            for element in c[upper_scope:]:
                if element.name == 'Constructor' and isinstance(element.mtype, MType):
                    obj_constructor = element

        if not obj_constructor and not ast.param:
            return ClassType(Id(ast.classname.name))
        if not obj_constructor and ast.param:
            raise TypeMismatchInExpression(ast)

        if type(obj_constructor.mtype.rettype) is not VoidType:
            raise TypeMismatchInExpression(ast)

        lst_expr_param = []
        for element in ast.param:
            lst_expr_param.append(type(self.visit(element, c)))

        lst_obj_param = []
        for element in obj_constructor.mtype.partype:
            lst_obj_param.append(type(element))

        flag = checkParamEqual(lst_expr_param, lst_obj_param)
        if not flag:
            raise TypeMismatchInExpression(ast)

        return ClassType(Id(ast.classname.name))

    def visitArrayLiteral(self, ast:ArrayLiteral, c):
        if len(ast.value) == 0:
            return ArrayType()

        first_element_type = self.visit(ast.value[0], c)
        for element in ast.value[1:]:
            if type(self.visit(element, c)) is not type(first_element_type):
                self.array_flag = False
                return

        if type(ast.value[0]) == ArrayLiteral:
            max_ele = len(ast.value[0].value)
            for element in ast.value[1:]:
                if len(element.value) != max_ele:
                    self.array_flag = False
                    return

        return ArrayType(len(ast.value), first_element_type)

    def visitArrayCell(self, ast:ArrayCell, c):
        type_arr = self.visit(ast.arr, c)
        if not isinstance(type_arr, ArrayType):
            raise TypeMismatchInExpression(ast)

        for idx in ast.idx:
            if not isinstance(self.visit(idx, c), IntType):
                raise TypeMismatchInExpression(ast)
            if 'eleType' not in dir(type_arr):
                raise TypeMismatchInExpression(ast)
            type_arr = type_arr.eleType

        return type_arr


# ------------------------------- HELPER FUNCTION ------------------------------- #

# Use only for visitId
def getAllMemberClassID(c, class_name, is_attribute):
    obj_class = []
    for class_element in c[0]:
        if type(class_element.mtype) is CType and class_element.name == class_name:
            obj_class = class_element
            break

    lst_member = []
    if obj_class.scope:
        upper_scope, lower_scope = obj_class.scope
        if is_attribute:
            for element in c[0][upper_scope:lower_scope]:
                if element.class_member and type(element.mtype) != MType:
                    lst_member.append(element.name)
        else:
            for element in c[0][upper_scope:lower_scope]:
                if element.class_member and type(element.mtype) == MType:
                    lst_member.append(element.name)

    else:
        upper_scope = c[0].index(obj_class) + 1
        if is_attribute:
            for element in c[0][upper_scope:]:
                if element.class_member and type(element.mtype) != MType:
                    lst_member.append(element.name)
        else:
            for element in c[0][upper_scope:]:
                if element.class_member and type(element.mtype) == MType:
                    lst_member.append(element.name)

    return lst_member


# Use for program
def getAllMemberClass(c, class_name, is_attribute):
    obj_class = []
    for class_element in c:
        if type(class_element.mtype) is CType and class_element.name == class_name:
            obj_class = class_element
            break

    lst_member = []
    if obj_class.scope:
        upper_scope, lower_scope = obj_class.scope
        if is_attribute:
            for element in c[upper_scope:lower_scope]:
                if element.class_member and type(element.mtype) != MType:
                    lst_member.append(element)
        else:
            for element in c[upper_scope:lower_scope]:
                if element.class_member and type(element.mtype) == MType:
                    lst_member.append(element)

    else:
        upper_scope = c.index(obj_class) + 1
        if is_attribute:
            for element in c[upper_scope:]:
                if element.class_member and type(element.mtype) != MType:
                    lst_member.append(element)
        else:
            for element in c[upper_scope:]:
                if element.class_member and type(element.mtype) == MType:
                    lst_member.append(element)

    return lst_member


def checkType(lhs_type, rhs_type, c):
    if type(lhs_type) is FloatType:
        if type(rhs_type) in [IntType, FloatType]:
            return True

    elif isinstance(lhs_type, ClassType) and isinstance(rhs_type, ClassType):
        if lhs_type.classname.name == rhs_type.classname.name:
            return True

        rhs_class = []
        for element in c:
            if element.name == rhs_type.classname.name and type(element.mtype) == CType:
                rhs_class = element
                break

        if rhs_class.parent_class_name:
            return checkType(lhs_type, ClassType(Id(rhs_class.parent_class_name)), c)
        else:
            return False

    if type(lhs_type) == type(rhs_type):
        return True
    else:
        return False


def checkArrayType(lhs_type, rhs_type, c):
    if type(lhs_type) is not ArrayType or type(rhs_type) is not ArrayType:
        return False
    else:
        if type(lhs_type.eleType) is ArrayType and type(rhs_type.eleType) is ArrayType:
            return checkArrayType(lhs_type.eleType, rhs_type.eleType, c)
        else:
            if type(lhs_type.eleType) is ArrayType and type(rhs_type.eleType) is not ArrayType:
                return checkArrayType(lhs_type.eleType, rhs_type, c)
            if type(lhs_type.eleType) == type(rhs_type.eleType):
                return lhs_type.size == rhs_type.size
            else:
                return False


def checkIllegalConstantExpression(ast:Expr, c):
    if type(ast) in [BinaryOp, UnaryOp]:
        if type(ast) is BinaryOp:
            return checkIllegalConstantExpression(ast.left, c) and checkIllegalConstantExpression(ast.right, c)
        else:
            return checkIllegalConstantExpression(ast.body, c)

    elif type(ast) is ArrayCell:
        for idx in ast.idx:
            flag = checkIllegalConstantExpression(idx, c)
            if not flag:
                raise IllegalConstantExpression(ast)

        if type(ast.arr) is not Id:
            return checkIllegalConstantExpression(ast.arr, c)
        obj_arr = []

        for element in reversed(c):
            if element.name == ast.arr.name and type(element.mtype) == ArrayType:
                obj_arr = element

        if not obj_arr:
            return False

        if len(ast.idx) == 1:
            obj_arr_value = obj_arr.value.value
            if type(ast.idx[0]) == Id:
                return True

            obj_type = obj_arr_value[ast.idx[0].value]
            obj = []
            if type(obj_type) in [IntLiteral, FloatLiteral, StringLiteral, BooleanLiteral, ArrayLiteral, NewExpr,
                                  SelfLiteral]:
                return True
            else:
                for element in reversed(c):
                    if element.name == obj_type.name:
                        obj = element

            if obj.is_constant:
                return True
            else:
                raise IllegalConstantExpression(ast)

    elif type(ast) in [CallExpr]:
        if type(ast.obj) == SelfLiteral:
            nearest_class = list(filter(lambda x: isinstance(x.mtype, CType),c))[-1]
            obj_method = []
            upper_scope = c.index(nearest_class) + 1
            for element in c[upper_scope:]:
                if element.name == ast.method.name and isinstance(element.mtype, MType):
                    obj_method = element
                    break
            if not obj_method.is_constant:
                return False
            else:
                return True
        return checkIllegalConstantExpression(ast.obj, c)

    elif type(ast) in [Id]:
        obj = []
        for element in c:
            if element.name == ast.name:
                obj = element

        if not obj:
            return False

        if not obj.is_constant:
            return False
        else:
            return True

    elif type(ast) is FieldAccess:
        obj_class = []
        obj_class_name = []

        if type(ast.obj) == SelfLiteral:
            for element in c:
                if type(element.mtype) == CType:
                    obj_class = element
            upper_scoper = c.index(obj_class) + 1
            for element in c[upper_scoper:]:
                if element.name == ast.fieldname.name:
                    if not element.is_constant:
                        return False
                    else:
                        return True

        elif type(ast.obj) == FieldAccess:
            flag_obj = checkIllegalConstantExpression(ast.obj, c)
            if not flag_obj:
                return False

            for element in c:
                if element.name == ast.obj.fieldname.name and isinstance(element.mtype, ClassType):
                    obj_class_name = element.mtype.classname.name
                    if not element.is_constant:
                        return False
                    break

            for element in c:
                if element.name == obj_class_name and isinstance(element.mtype, CType):
                    obj_class = element
                    break

            upper_scope = c.index(obj_class) + 1
            for element in c[upper_scope:]:
                if element.name == ast.fieldname.name and not isinstance(element.mtype, (CType, MType)):
                    if not element.is_constant:
                        return False
                    else:
                        return True

        else:
            if ast.fieldname.name[0] == '$':
                for element in c:
                    if element.name == ast.obj.name and isinstance(element.mtype, CType):
                        obj_class = element
                        break

                if not obj_class:
                    return False

                upper_scope = c.index(obj_class) + 1
                for element in c[upper_scope:]:
                    if element.name == ast.fieldname.name and not isinstance(element.mtype, (CType, MType)):
                        if not element.is_constant:
                            return False
                        else:
                            return True

    elif type(ast) in [IntLiteral, FloatLiteral, StringLiteral, BooleanLiteral, ArrayLiteral, NewExpr, SelfLiteral]:
        return True
    elif type(ast) is None:
        return False
    return False


# Attribute in class must have keyword 'Self' to access
def checkIdentifierAttributeDecl(ast:Expr, c):
    if type(ast) in [BinaryOp, UnaryOp]:
        if type(ast) is BinaryOp:
            return checkIdentifierAttributeDecl(ast.left, c) and checkIdentifierAttributeDecl(ast.right, c)
        else:
            return checkIdentifierAttributeDecl(ast.body, c)

    elif type(ast) is ArrayCell:
        return True

    elif type(ast) in [Id]:
        raise Undeclared(Identifier(), ast.name)

    elif type(ast) is FieldAccess:
        obj_class = []

        if type(ast.obj) == SelfLiteral:
            for element in c:
                if type(element.mtype) == CType:
                    obj_class = element
            upper_scoper = c.index(obj_class) + 1
            for element in c[upper_scoper:]:
                if element.name == ast.fieldname.name:
                    return True

        elif ast.fieldname.name[0] == '$':
            for element in c:
                if element.name == ast.obj.name and isinstance(element.mtype, CType):
                    obj_class = element
                    break

            if not obj_class:
                return False

            upper_scope = c.index(obj_class) + 1
            for element in c[upper_scope:]:
                if element.name == ast.fieldname.name and not isinstance(element.mtype, (CType, MType)):
                    if not element.is_constant:
                        return False
                    else:
                        return True

    elif type(ast) in [IntLiteral, FloatLiteral, StringLiteral, BooleanLiteral, ArrayLiteral, NewExpr, SelfLiteral]:
        return True
    elif type(ast) is None:
        return False
    return False


def checkParamEqual(lst_expr_param, lst_obj_param):
    if len(lst_expr_param) != len(lst_obj_param):
        return False

    for (expr_param, method_param) in zip(lst_expr_param, lst_obj_param):
        if method_param is FloatType:
            if expr_param not in [IntType, FloatType]:
                return False
        else:
            if method_param != expr_param:
                return False

    return True


def checkNoEntryPoint(c_global):
    class_program = []
    for element in c_global:
        if element.name == 'Program' and isinstance(element.mtype, CType):
            class_program = element
            break

    if not class_program:
        return False

    upper_scope, lower_scope = class_program.scope
    class_program_method = []
    for element in c_global[upper_scope:lower_scope]:
        if isinstance(element.mtype, MType) and element.class_member is True:
            class_program_method.append(element)

    if not class_program_method:
        return False

    main_method = []
    for element in class_program_method:
        if element.name == 'main':
            main_method = element
            break

    if not main_method:
        return False
    if len(main_method.mtype.partype) != 0:
        return False
    if not isinstance(main_method.mtype.rettype, VoidType):
        return False
    if isinstance(main_method.kind, Instance):
        return False

    return True


def checkSelfStaticMethod(ast, c):
    obj_method_inside = []
    for element in reversed(c):
        if type(element.mtype) == MType:
            obj_method_inside = element
            break
        elif type(element.mtype) == CType:
            break

    if obj_method_inside and isinstance(obj_method_inside.kind, Static):
        return False

    return True
