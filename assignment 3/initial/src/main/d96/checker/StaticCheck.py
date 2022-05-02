
"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *


class CType:
    # Type ID of class
    pass

class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self, name, mtype, value=None, kind=None, scope=None, class_member=None,
                 parent_class_name=None, is_constant=None, is_stmt=None):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.kind = kind
        self.scope = scope
        self.class_member = class_member
        self.parent_class_name = parent_class_name
        self.is_constant = is_constant
        self.is_stmt = is_stmt

class StaticChecker(BaseVisitor,Utils):

    global_envi = [
    Symbol("getInt",MType([],IntType())),
    Symbol("putIntLn",MType([IntType()],VoidType()))
    ]

    return_type_stack = []


    def __init__(self,ast):
        self.ast = ast



    def check(self):
        #return self.visit(self.ast,StaticChecker.global_envi)
        return self.visit(self.ast, [])


    def visitProgram(self, ast:Program, c):
        for class_decl in ast.decl:
            self.visit(class_decl, c)
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
                elif isinstance(element.mtype, (CType, MType)) or element.is_stmt == 'BLOCK':
                    raise Undeclared(Variable(), ast.name)

            if obj:
                return obj.mtype
            else:
                raise Undeclared(Variable(), ast.name)

        inst = c[1]
        if inst == 'CHECK_UNDECLARED_IDENTIFIER':
            lst_class = []
            for id_name in c[0]:
                if type(id_name.mtype) is CType:
                    lst_class.append(id_name)
            obj_class = lst_class[-1]

            lower_scope = c[0].index(obj_class) + 1
            lst_ids = c[0][lower_scope:]
            lst_ids_name = []
            for element in lst_ids:
                lst_ids_name.append(element.name)

            if ast.name not in lst_ids_name:
                raise Undeclared(c[2], ast.name)

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

            obj_class = []
            for class_name in c[0]:
                if type(class_name.mtype) is CType and class_name.name == obj.mtype.classname.name:
                    obj_class = class_name
                    break

            lst_class_member = getAllMemberClassID(c, obj_class.name, is_attribute=True)
            if ast.name not in lst_class_member:
                raise Undeclared(c[2], ast.name)

        elif inst == 'CHECK_UNDECLARED_METHOD':
            obj = []
            for element in c[0]:
                if element.name == c[3] and type(element.mtype) != MType:
                    obj = element
                    break

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

        else:
            for element in c[0]:
                if element.name == ast.name:
                    raise Redeclared(c[1], ast.name)

        return ast.name

    def visitMethodDecl(self, ast:MethodDecl, c_scope):
        c, lower_scope = c_scope
        m_name = self.visit(ast.name, (c[lower_scope:], Method()))
        m_type = MType([], None)
        c.append(Symbol(m_name, m_type, class_member=True))

        lower_scope = len(c)
        for param in ast.param:
            self.visit(param, (c, lower_scope, 'PARAM_DECL'))

        self.visit(ast.body, (c, lower_scope))

        new_method = []
        for element in c:
            if type(element.mtype) == MType and element.name == ast.name.name:
                new_method = element
                break

        new_method.scope = (lower_scope, len(c))
        for element in ast.param:
            new_method.mtype.partype.append(element.varType)
        if self.return_type_stack:
            new_method.mtype.rettype = self.return_type_stack.pop()
        else:
            new_method.mtype.rettype = VoidType()
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
        attr_kind = ast.kind

        c.append(Symbol(attr_name, attr_type, attr_value, attr_kind, class_member=True))
        return

    def visitVarDecl(self, ast:VarDecl, c_scope_inst):
        c, lower_scope, inst = c_scope_inst
        if inst == 'PARAM_DECL':
            var_name = self.visit(ast.variable, (c[lower_scope:], Parameter()))
        else:
            var_name = self.visit(ast.variable, (c[lower_scope:], Variable()))
        var_type = ast.varType
        var_value = ast.varInit
        var_kind = Instance()

        if type(var_type) is ClassType:
            inst = "CHECK_UNDECLARED_CLASS"
            self.visit(ast.varType.classname, (c, inst, Class(), var_type.classname.name))

        if not ((var_value is None) or (isinstance(var_value, NullLiteral))):
            rhs_type = self.visit(ast.varInit, c)
            flag = checkType(ast.varType, rhs_type, c)
            if not flag:
                raise TypeMismatchInStatement(ast)


        c.append(Symbol(var_name, var_type, var_value, var_kind, is_constant=False))

        return

    def visitConstDecl(self, ast:ConstDecl, c_scope_inst):
        c, lower_scope, inst = c_scope_inst
        var_name = self.visit(ast.constant, (c[lower_scope:], Constant()))
        var_type = ast.constType
        var_value = ast.value
        var_kind = Instance()

        if not ((var_value is None) or (isinstance(var_value, NullLiteral))):
            rhs_type = self.visit(var_value, c)
            flag = checkType(ast.constType, rhs_type, c)
            if not flag:
                raise TypeMismatchInConstant(ast)

        flag = checkIllegalConstantExpression(var_value, c)
        if not flag:
            raise IllegalConstantExpression(var_value)

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
        lhs_type = None
        if type(ast.lhs) == Id:
            self.visit(ast.lhs, (c, 'CHECK_UNDECLARED_IDENTIFIER', Identifier()))
            self.visit(ast.lhs, (c, 'CHECK_CONSTANT_ASSIGN', ast))
            for element in c:
                if element.name == ast.lhs.name:
                    lhs_type = element.mtype

        elif type(ast.lhs) == FieldAccess:
            if type(ast.lhs.obj) == Id:
                self.visit(ast.lhs.fieldname, (c, 'CHECK_UNDECLARED_ATTRIBUTE', Attribute(), ast.lhs.obj.name))
                lhs_type = self.visit(ast.lhs, c)

        elif type(ast.lhs) == ArrayCell:
            if type(ast.lhs.arr) == Id:
                for element in c:
                    if element.name == ast.lhs.arr.name and type(element.mtype) != ArrayType:
                        raise TypeMismatchInExpression(ast.lhs)
                for idx in ast.lhs.idx:
                    if not(isinstance(idx, IntLiteral)):
                        raise TypeMismatchInExpression(ast.lhs)
                    for element in c:
                        if element.name == ast.lhs.arr.name:
                            lhs_type = element.mtype.eleType

        rhs_type = self.visit(ast.exp, c)
        flag = checkType(lhs_type, rhs_type, c)
        if not flag:
            raise TypeMismatchInStatement(ast)


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
            if isinstance(left, (IntType, BoolType)) is False or isinstance(right, (IntType, BoolType)) is False:
                raise TypeMismatchInExpression(ast)
            return BoolType()

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
        if type(ast.obj) == Id:
            self.visit(ast.method, (c, 'CHECK_UNDECLARED_METHOD', Method(), ast.obj.name))

            obj = []
            for element in c:
                if element.name == ast.obj.name and type(element.mtype) != MType:
                    obj = element
                    break

            if type(obj.mtype) != ClassType:
                raise TypeMismatchInStatement(ast)

            obj_class = []
            for element in c:
                if element.name == obj.mtype.classname.name and type(element.mtype) == CType:
                    obj_class = element
                    break

            lst_obj_class_method = getAllMemberClass(c, obj_class.name, is_attribute=False)
            obj_method = []
            for element in lst_obj_class_method:
                if element.name == ast.method.name:
                    obj_method = element

            if type(obj_method.mtype.rettype) is not VoidType:
                raise TypeMismatchInStatement(ast)

            lst_param_type_call = []
            for element in ast.param:
                lst_param_type_call.append(type(self.visit(element, c)))

            lst_obj_method_param_type = []
            for element in obj_method.mtype.partype:
                lst_obj_method_param_type.append(type(element))

            if len(lst_param_type_call) != len(lst_obj_method_param_type):
                raise TypeMismatchInStatement(ast)

            for (param_type_call, param_type_method) in zip(lst_param_type_call, lst_obj_method_param_type):
                if param_type_method is FloatType:
                    if param_type_call not in [IntType, FloatType]:
                        raise TypeMismatchInStatement(ast)
                else:
                    if param_type_call != param_type_method:
                        raise TypeMismatchInStatement(ast)

            return obj_method.mtype.rettype

    def visitCallExpr(self, ast:CallExpr, c):
        if type(ast.obj) == Id:
            obj = []
            for element in c:
                if element.name == ast.obj.name:
                    obj = element
                    break

            if type(obj.mtype) != ClassType:
                raise TypeMismatchInExpression(ast)

            obj_class = []
            for element in c:
                if type(element.mtype) == CType and element.name == obj.mtype.classname.name:
                    obj_class = element
                    break

            upper_scope, lower_scope = obj_class.scope
            obj_method = []
            for element in c[upper_scope:lower_scope]:
                if element.name == ast.method.name and type(element.mtype) == MType:
                    obj_method = element
                    break

            if type(obj_method.mtype.rettype) is VoidType:
                raise TypeMismatchInExpression(ast)

            lst_param_type_call = []
            for element in ast.param:
                lst_param_type_call.append(type(self.visit(element, c)))

            lst_obj_method_param_type = []
            for element in obj_method.mtype.partype:
                lst_obj_method_param_type.append(type(element))

            if len(lst_param_type_call) != len(lst_obj_method_param_type):
                raise TypeMismatchInExpression(ast)

            for (param_type_call, param_type_method) in zip(lst_param_type_call, lst_obj_method_param_type):
                if param_type_method is FloatType:
                    if param_type_call not in [IntType, FloatType]:
                        raise TypeMismatchInExpression(ast)
                else:
                    if param_type_call != param_type_method:
                        raise TypeMismatchInExpression(ast)

            return obj_method.mtype.rettype

    def visitReturn(self, ast:Return, c):
        new_return_type = self.visit(ast.expr, c)
        self.return_type_stack.append(new_return_type)

        return

    def visitFieldAccess(self, ast:FieldAccess, c):
        if type(ast.obj) == Id:
            obj = []
            for element in c:
                if ast.obj.name == element.name and type(element.mtype) != MType:
                    obj = element
                    break

            if type(obj.mtype) != ClassType:
                raise TypeMismatchInExpression(ast)

            obj_class = []
            for element in c:
                if element.name == obj.mtype.classname.name and type(element.mtype) == CType:
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
            obj_class = []
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

    def visitFor(self, ast:For, c):
        new_for = Symbol('STMT_FOR', mtype=None, is_stmt='FOR')
        c.append(new_for)
        expr1 = self.visit(ast.expr1, c)
        expr2 = self.visit(ast.expr2, c)
        upper_scope = len(c)
        if not (checkType(expr1, IntType(), c) and checkType(expr2, IntType(), c)):
            raise TypeMismatchInStatement(ast)
        expr3 = self.visit(ast.expr3, c) if ast.expr3 is not None else None
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

    # TODO!
    def visitIf(self, ast:If, c):
        if isinstance(c, tuple):
            c, scope = c
        new_if = Symbol('STMT_IF', mtype=None, is_stmt='IF')
        c.append(new_if)
        upper_scope = len(c)
        self.visit(ast.expr, c)
        self.visit(ast.thenStmt, (c, upper_scope))
        self.visit(ast.elseStmt, (c, upper_scope)) if ast.elseStmt is not None else None
        new_if.scope = (upper_scope, len(c))

    def visitContinue(self, ast: Continue, c):
        for element in reversed(c):
            if element.is_stmt == 'FOR':
                if element.scope is None:
                    break
            if isinstance(element.mtype, (CType, MType)):
                raise MustInLoop(ast)

    # def visitFuncDecl(self, ast, c):
    #     return list(map(lambda x: self.visit(x,(c,True)),ast.body.stmt))
    #
    #
    #
    # def visitCallExpr(self, ast, c):
    #     at = [self.visit(x,(c[0],False)) for x in ast.param]
    #
    #     res = self.lookup(ast.method.name,c[0],lambda x: x.name)
    #     if res is None or not type(res.mtype) is MType:
    #         raise Undeclared(Function(),ast.method.name)
    #     elif len(res.mtype.partype) != len(at):
    #         if c[1]:
    #             raise TypeMismatchInStatement(ast)
    #         else:
    #             raise TypeMismatchInExpression(ast)
    #     else:
    #         return res.mtype.rettype
    #
    # def visitIntLiteral(self,ast, c):
    #     return IntType()


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
        return ClassType(Id(ast.classname.name))


# ------------------------------- SUPPORT FUNCTION ------------------------------- #

# Use only for visitId
def getAllMemberClassID(c, class_name, is_attribute):
    obj_class = []
    for class_element in c[0]:
        if type(class_element.mtype) is CType and class_element.name == class_name:
            obj_class = class_element
            break

    lst_member = []
    upper_scope, lower_scope = obj_class.scope
    if is_attribute:
        for element in c[0][upper_scope:lower_scope]:
            if element.class_member and type(element.mtype) != MType:
                lst_member.append(element.name)
    else:
        for element in c[0][upper_scope:lower_scope]:
            if element.class_member and type(element.mtype) == MType:
                lst_member.append(element.name)

    if obj_class.parent_class_name:
        return lst_member + getAllMemberClassID(c, obj_class.parent_class_name, is_attribute)
    else:
        return lst_member

# Use for program
def getAllMemberClass(c, class_name, is_attribute):
    obj_class = []
    for class_element in c:
        if type(class_element.mtype) is CType and class_element.name == class_name:
            obj_class = class_element
            break

    lst_member = []
    upper_scope, lower_scope = obj_class.scope
    if is_attribute:
        for element in c[upper_scope:lower_scope]:
            if element.class_member and type(element.mtype) != MType:
                lst_member.append(element)
    else:
        for element in c[upper_scope:lower_scope]:
            if element.class_member and type(element.mtype) == MType:
                lst_member.append(element)

    if obj_class.parent_class_name:
        return lst_member + getAllMemberClass(c, obj_class.parent_class_name, is_attribute)
    else:
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



def checkIllegalConstantExpression(ast:Expr, c):
    if type(ast) in [BinaryOp, UnaryOp]:
        if type(ast) is BinaryOp:
            return checkIllegalConstantExpression(ast.left, c) and checkIllegalConstantExpression(ast.right, c)
        else:
            return checkIllegalConstantExpression(ast.body, c)
    elif type(ast) in [CallExpr, FieldAccess]:
        return checkIllegalConstantExpression(ast.obj, c)
    elif type(ast) in [Id]:
        obj = []
        for element in c:
            if element.name == ast.name:
                obj = element
        if not obj.is_constant:
            return False
        else:
            return True
    elif type(ast) in [IntLiteral, FloatLiteral, StringLiteral, BooleanLiteral, ArrayLiteral, NewExpr, SelfLiteral]:
        return True
    elif type(ast) is None:
        return False
    return False





