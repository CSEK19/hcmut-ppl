
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
    def __init__(self, name, mtype, value = None, kind = None, scope = None):
        self.name = name
        self.mtype = mtype
        self.value = value
        self.kind = kind
        self.scope = scope

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
        return

    def visitId(self, ast:Id, c):
        if c[1] == 'CHECK_UNDECLARED':
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

            if ast not in lst_ids_name:
                raise Undeclared(c[2], ast.name)

        for element in c[0]:
            if element.name == ast.name:
                if ast.name == 'ef':
                    print(ast.name)
                raise Redeclared(c[1], ast.name)

        return ast.name


    def visitMethodDecl(self, ast:MethodDecl, c_scope):
        c, lower_scope = c_scope
        m_name = self.visit(ast.name, (c[lower_scope:], Method()))
        m_type = MType(None, None)
        c.append(Symbol(m_name, m_type))

        lower_scope = len(c)
        for param in ast.param:
            self.visit(param, (c, lower_scope, 'PARAM'))

        self.visit(ast.body, (c, lower_scope))
        return

    def visitAttributeDecl(self, ast, c_scope):
        c, lower_scope = c_scope
        # attr_name, attr_type, attr_value, attr_kind = None

        if type(ast.decl) is VarDecl:
            attr_name = self.visit(ast.decl.variable, (c[lower_scope:], Attribute()))
            attr_type = ast.decl.varType
            attr_value = ast.decl.varInit
        else:
            attr_name = self.visit(ast.decl.constant, (c[lower_scope:], Attribute()))
            attr_type = ast.decl.constType
            attr_value = ast.decl.value
        attr_kind = ast.kind

        c.append(Symbol(attr_name, attr_type, attr_value, attr_kind))
        return



    def visitVarDecl(self, ast:VarDecl, c_scope_inst):
        c, lower_scope, inst = c_scope_inst
        # var_name, var_type, var_value, var_kind = None
        if inst == 'PARAM':
            var_name = self.visit(ast.variable, (c[lower_scope:], Parameter()))
        else:
            var_name = self.visit(ast.variable, (c[lower_scope:], Variable()))
        var_type = ast.varType
        var_value = ast.varInit
        var_kind = Instance()
        c.append(Symbol(var_name, var_type, var_value, var_kind))

        return



    def visitConstDecl(self,ast:ConstDecl, c_scope_inst):
        c, lower_scope, inst = c_scope_inst
        # var_name, var_type, var_value, var_kind = None
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
        return

    def visitAssign(self, ast: Assign, c_scope):
        c, lower_scope = c_scope
        if type(ast.lhs) == Id:
            self.visit(ast.lhs, (c, 'CHECK_UNDECLARED', Identifier()))






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


