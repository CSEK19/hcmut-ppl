
"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *


class CType:
    # Type Class ID
    pass

class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self, name, mtype, value=None, kind=None, scope=None, class_member=None,
                 parent_class_name=None, is_constant=None):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.kind = kind
        self.scope = scope
        self.class_member = class_member
        self.parent_class_name = parent_class_name
        self.is_constant = is_constant

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

            lst_class_member = getAllMemberClass(c, obj_class.name, is_attribute=True)
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

            lst_class_member = getAllMemberClass(c, obj_class.name, is_attribute=False)

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
            if type(ast.varType) is FloatType:
                if type(rhs_type) not in [IntType, FloatType]:
                    raise TypeMismatchInStatement(ast)
            else:
                if type(ast.varType) != type(rhs_type):
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
            rhs_type = self.visit(ast.value, c)
            if type(ast.constType) is FloatType:
                if type(rhs_type) not in [IntType, FloatType]:
                    raise TypeMismatchInConstant(ast)
            else:
                if type(ast.constType) != type(rhs_type):
                    raise TypeMismatchInConstant(ast)

        c.append(Symbol(var_name, var_type, var_value, var_kind, is_constant=True))
        return

    def visitBlock(self, ast:Block, c_scope):
        c, lower_scope = c_scope
        for instructor in ast.inst:
            if type(instructor) in [VarDecl, ConstDecl]:
                self.visit(instructor, (c, lower_scope, 'INST'))
            elif type(instructor) in [Block]:
                self.visit(instructor, (c, len(c)))
            elif type(instructor) in [Assign]:
                self.visit(instructor, (c, lower_scope))
            elif type(instructor) in [CallStmt]:
                self.visit(instructor, (c, lower_scope))
            elif type(instructor) in [Return]:
                self.visit(instructor, c)
        return

    def visitAssign(self, ast:Assign, c_scope):
        c, lower_scope = c_scope
        if type(ast.lhs) == Id:
            self.visit(ast.lhs, (c, 'CHECK_UNDECLARED_IDENTIFIER', Identifier()))
            self.visit(ast.lhs, (c, 'CHECK_CONSTANT_ASSIGN', ast))

        elif type(ast.lhs) == FieldAccess:
            if type(ast.lhs.obj) == Id:
                self.visit(ast.lhs.fieldname, (c, 'CHECK_UNDECLARED_ATTRIBUTE', Attribute(), ast.lhs.obj.name))

        elif type(ast.lhs) == ArrayCell:
            if type(ast.lhs.arr) == Id:
                for element in c:
                    if element.name == ast.lhs.arr.name and type(element.mtype) != ArrayType:
                        raise TypeMismatchInExpression(ast.lhs)
                for idx in ast.lhs.idx:
                    if not(isinstance(idx, IntLiteral)):
                        raise TypeMismatchInExpression(ast.lhs)


        rhs_type = self.visit(ast.exp, c)

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

    def visitCallStmt(self, ast:CallStmt, c_scope):
        c, lower_scope = c_scope
        if type(ast.obj) == Id:
            self.visit(ast.method, (c, 'CHECK_UNDECLARED_METHOD', Method(), ast.obj.name))

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

            if obj_method.mtype.rettype is None:
                raise TypeMismatchInExpression(ast)

            lst_param_type = []
            for element in ast.param:
                lst_param_type.append(type(self.visit(element, c)))

            lst_obj_method_param_type = []
            for element in obj_method.mtype.partype:
                lst_obj_method_param_type.append(type(element))

            if len(lst_param_type) != len(lst_obj_method_param_type):
                raise TypeMismatchInExpression(ast)

            for (param_type, param_type_method) in zip(lst_param_type, lst_obj_method_param_type):
                if param_type_method is FloatType:
                    if param_type not in [IntType, FloatType]:
                        raise TypeMismatchInExpression(ast)
                else:
                    if param_type != param_type_method:
                        raise TypeMismatchInExpression(ast)

            return obj_method.mtype.rettype

    def visitReturn(self, ast:Return, c):
        return_type = self.visit(ast.expr, c)
        self.return_type_stack.append(return_type)

    def visitFieldAccess(self, ast:FieldAccess, c):
        if type(ast.obj) == Id:
            obj = []
            for element in c:
                if ast.obj.name == element.name:
                    obj = element
                    break

            if type(obj.mtype) != ClassType:
                raise TypeMismatchInExpression(ast)

            obj_class = []
            for element in c:
                if element.name == obj.mtype.classname.name and type(element.mtype) == CType:
                    obj_class = element
                    break

            lst_class_member = getAllAttributeMemberClass(c, obj_class.name)
            lst_same_name_object = []
            for element in lst_class_member:
                if ast.fieldname.name == element.name:
                    lst_same_name_object.append(element)
            if len(lst_same_name_object) == 0:
                raise Undeclared(Attribute(), ast.fieldname.name)

            return lst_same_name_object[-1].mtype






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


# ------------------------------- SUPPORT FUNCTION ------------------------------- #

def getAllMemberClass(c, class_name, is_attribute):
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
        return lst_member + getAllMemberClass(c, obj_class.parent_class_name, is_attribute)
    else:
        return lst_member


def getAllAttributeMemberClass(c, class_name):
    obj_class = []
    for class_element in c:
        if type(class_element.mtype) is CType and class_element.name == class_name:
            obj_class = class_element
            break

    lst_member = []
    upper_scope, lower_scope = obj_class.scope
    for element in c[upper_scope:lower_scope]:
        if element.class_member and type(element.mtype) != MType:
            lst_member.append(element)

    if obj_class.parent_class_name:
        return lst_member + getAllMemberClass(c, obj_class.parent_class_name)
    else:
        return lst_member







