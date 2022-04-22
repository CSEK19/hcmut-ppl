
"""
 * @author nhphung
"""
from AST import * 
from Visitor import *
from Utils import Utils
from StaticError import *

class MType:
    def __init__(self,partype,rettype):
        self.partype = partype
        self.rettype = rettype

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value

class StaticChecker(BaseVisitor,Utils):

    global_envi = [
    Symbol("getInt",MType([],IntType())),
    Symbol("putIntLn",MType([IntType()],VoidType()))
    ]
            
    
    def __init__(self,ast):
        self.ast = ast

 
    
    def check(self):
        return self.visit(self.ast,StaticChecker.global_envi)

    def visitProgram(self, ast:Program, c):
        program_context = {}
        c.append(program_context)
        a = c
        for decl in ast.decl:
            self.visit(decl, c)
        # return [self.visit(x,c) for x in ast.decl]

    def visitClassDecl(self, ast:ClassDecl, c):
        program_contex = c[-1]
        if ast.classname.name in program_contex.keys():
            raise Redeclared(Class(), ast.classname.name)
        else:
            program_contex[ast.classname.name] = {}
            for element in ast.memlist:
                self.visit(element, program_contex[ast.classname.name])

    def visitMethodDecl(self, ast:MethodDecl, c):
        class_context = c
        m_kind = ast.kind

        m_name = ast.name.name
        if m_name in class_context.keys():
            raise Redeclared(Method(), m_name)

        m_param = []
        for element in ast.param:
            m_param.append(self.visit(element,(m_param,'PARAMS')))

        m_body = self.visit(ast.body,(c, m_param))
        class_context[m_name] = [m_kind, m_name, m_param, m_body]


    def visitAttributeDecl(self, ast, c):
        class_context = c
        atr_kind = ast.kind

        if type(ast.decl) is VarDecl:
            atr_name = ast.decl.variable.name
            atr_type = ast.decl.varType
            atr_value = ast.decl.varInit
        else:
            atr_name = ast.decl.constant.name
            atr_type = ast.decl.constType
            atr_value = ast.decl.value

        if atr_name in class_context.keys():
            raise Redeclared(Attribute(), atr_name)
        else:
            class_context[atr_name] = [atr_type, atr_kind, atr_name, atr_value]

    def visitVarDecl(self, ast:VarDecl, c):
        if c[1] == 'PARAMS':
            for element in c[0]:
                if ast.variable.name in element[2]:
                    raise Redeclared(Parameter(), ast.variable.name)

            # if ast.variable.name in [x[2] for x in c[0]]:
            #     raise Redeclared(Parameter(), ast.variable.name)

            return [ast.varType, Instance(), ast.variable.name, ast.varInit]
        elif c[1] == 'INST':
            for element in c[2]:
                if ast.variable.name in element[2]:
                    raise Redeclared(Variable(), ast.variable.name)

            for element in c[3]:
                if ast.variable.name in element['information'][2]:
                    raise Redeclared(Variable(), ast.variable.name)

            # if ast.variable.name in [x[2] for x in c[2]] + [x['information'][2] for x in c[3]]:
            #     raise Redeclared(Variable(), ast.variable.name)
            return {'instruction_ast': ast, 'information': [ast.varType, Instance(), ast.variable.name, ast.varInit]}

    def visitConstDecl(self,ast:ConstDecl, c):
        if c[1] == 'INST':
            for element in c[2]:
                if ast.constant.name in element[2]:
                    raise Redeclared(Constant(), ast.constant.name)
            for element in c[3]:
                if ast.constant.name in element['information'][2]:
                    raise Redeclared(Constant(), ast.constant.name)
            # if ast.constant.name in [x[2] for x in c[2]] + [x['information'][2] for x in c[3]]:
            #     raise Redeclared(Constant(), ast.constant.name)
            return {'instruction_ast': ast, 'information': [ast.constType, Instance(), ast.constant.name, ast.value]}

    def visitBlock(self, ast:Block, c):
        b_param = c[1]
        b_body = []
        for inst in ast.inst:
            if isinstance(inst,(VarDecl, ConstDecl)):
                b_body = b_body + [self.visit(inst, (c,'INST',b_param, b_body))]
        return b_body



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


