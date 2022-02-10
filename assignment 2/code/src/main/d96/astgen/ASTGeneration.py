from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *


class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        #program: stmt_ClassDeclaration+ EOF;
        classList = []
        for classDecl in ctx.stmt_ClassDeclaration():
            classList.append(self.visit(classDecl))
        return Program(classList)

    def visitStmt_ClassDeclaration(self, ctx:D96Parser.Stmt_ClassDeclarationContext):
        className = Id(ctx.ID()[0].getText())
        memList = []
        parentName = None
        if len(ctx.ID()) == 2:
            parentName = Id(ctx.ID()[1].getText())
        return ClassDecl(className, memList, parentName)


    # def visitMptype(self, ctx: D96Parser.MptypeContext):
    #     if ctx.INTTYPE():
    #         return IntType()
    #     else:
    #         return VoidType()
    #
    # def visitBody(self, ctx: D96Parser.BodyContext):
    #     return self.visit(ctx.funcall())
    #
    # def visitFuncall(self, ctx: D96Parser.FuncallContext):
    #     return CallExpr(Id(ctx.ID().getText()), [self.visit(ctx.exp())] if ctx.exp() else [])
    #
    # def visitExp(self, ctx: D96Parser.ExpContext):
    #     if (ctx.funcall()):
    #         return self.visit(ctx.funcall())
    #     else:
    #         return IntLiteral(int(ctx.INTLIT().getText()))

####################################################################################
################                        TODO                        ################
####################################################################################

    def visitLit_Data(self, ctx:D96Parser.Lit_DataContext):
        if ctx.INTLIT():
            try:
                return IntLiteral(int(ctx.INTLIT().getText()), 2)
            except:
                try:
                    return IntLiteral(int(ctx.INTLIT().getText(), 8))
                except:
                    try:
                        return IntLiteral(int(ctx.INTLIT().getText(), 10))
                    except:
                        return IntLiteral(int(ctx.INTLIT().getText(), 16))
        elif ctx.ZERO():
            return IntLiteral(int(ctx.ZERO().getText()))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOLLIT():
            return BooleanLiteral(bool(ctx.BOOLLIT().getText()) == 'True')
        elif ctx.STRLIT():
            return StringLiteral(str(ctx.STRLIT().getText()))
        else:
            return ArrayLiteral(self.visit(ctx.lit_Array()))




