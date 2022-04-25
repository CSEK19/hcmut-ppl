
"""
 * @author nhphung
"""
from AST import *
from Visitor import *
from Utils import Utils
from StaticError import *

class CType:
    pass

class MType:
    def __init__(self, partype, rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self, name, mtype, value=None, kind=None, scope=None, class_member=None):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.kind = kind
        self.scope = scope
        self.class_member = class_member

class StaticChecker(BaseVisitor,Utils):

    global_envi = [
    Symbol("getInt",MType([],IntType())),
    Symbol("putIntLn",MType([IntType()],VoidType()))
    ]


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
        c.append(Symbol(ast.classname.name, CType(), None))
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
            last_class = lst_class[-1]

            lower_scope = c[0].index(last_class) + 1
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
            lst_obj = []
            for element in c[0]:
                lst_obj.append(element)
            obj = lst_obj[-1]

            lst_class = []
            obj_class = []
            for class_name in c[0]:
                if type(class_name.mtype) is CType and class_name.name == obj.mtype.classname.name:
                    obj_class = class_name
                    break
            upper_scope, lower_scope = obj_class.scope
            lst_class_member = []
            for element in c[0][upper_scope:lower_scope]:
                if element.class_member and type(element.mtype) != MType:
                    lst_class_member.append(element.name)

            if ast.name not in lst_class_member:
                raise Undeclared(c[2], ast.name)

        elif inst == 'CHECK_UNDECLARED_METHOD':
            lst_obj = []
            for element in c[0]:
                lst_obj.append(element)
            obj = lst_obj[-1]

            lst_class = []
            obj_class = []

            for class_name in c[0]:
                if type(class_name.mtype) is CType and class_name.name == obj.mtype.classname.name:
                    obj_class = class_name
                    break

            upper_scope, lower_scope = obj_class.scope
            lst_class_method = []
            for element in c[0][upper_scope:lower_scope]:
                if element.class_member and type(element.mtype) == MType:
                    lst_class_method.append(element.name)

            if ast.name not in lst_class_method:
                raise Undeclared(c[2], ast.name)

        else:
            for element in c[0]:
                if element.name == ast.name:
                    raise Redeclared(c[1], ast.name)

        return ast.name


    def visitMethodDecl(self, ast:MethodDecl, c_scope):
        c, lower_scope = c_scope
        m_name = self.visit(ast.name, (c[lower_scope:], Method()))
        m_type = MType(None, None)
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

        c.append(Symbol(var_name, var_type, var_value, var_kind))

        return

    def visitConstDecl(self, ast:ConstDecl, c_scope_inst):
        c, lower_scope, inst = c_scope_inst
        var_name = self.visit(ast.constant, (c[lower_scope:], Constant()))
        var_type = ast.constType
        var_value = ast.value
        var_kind = Instance()
        c.append(Symbol(var_name, var_type, var_value, var_kind))
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
        return

    def visitAssign(self, ast:Assign, c_scope):
        c, lower_scope = c_scope
        if type(ast.lhs) == Id:
            self.visit(ast.lhs, (c, 'CHECK_UNDECLARED_IDENTIFIER', Identifier()))
        elif type(ast.lhs) == FieldAccess:
            if type(ast.lhs.obj) == Id:
                self.visit(ast.lhs.fieldname, (c, 'CHECK_UNDECLARED_ATTRIBUTE', Attribute(), ast.lhs.obj.name))

    def visitCallStmt(self, ast:CallStmt, c_scope):
        c, lower_scope = c_scope
        if type(ast.obj) == Id:
            self.visit(ast.method, (c, 'CHECK_UNDECLARED_METHOD', Method(), ast.obj.name))

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


