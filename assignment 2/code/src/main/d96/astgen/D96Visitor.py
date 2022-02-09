# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .D96Parser import D96Parser
else:
    from D96Parser import D96Parser

# This class defines a complete generic visitor for a parse tree produced by D96Parser.

class D96Visitor(ParseTreeVisitor):

    # Visit a parse tree produced by D96Parser#program.
    def visitProgram(self, ctx:D96Parser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#expr.
    def visitExpr(self, ctx:D96Parser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_0.
    def visitExp_0(self, ctx:D96Parser.Exp_0Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_1.
    def visitExp_1(self, ctx:D96Parser.Exp_1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_2.
    def visitExp_2(self, ctx:D96Parser.Exp_2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_3.
    def visitExp_3(self, ctx:D96Parser.Exp_3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_4.
    def visitExp_4(self, ctx:D96Parser.Exp_4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_5.
    def visitExp_5(self, ctx:D96Parser.Exp_5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_6.
    def visitExp_6(self, ctx:D96Parser.Exp_6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_7.
    def visitExp_7(self, ctx:D96Parser.Exp_7Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_8.
    def visitExp_8(self, ctx:D96Parser.Exp_8Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_9.
    def visitExp_9(self, ctx:D96Parser.Exp_9Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_10.
    def visitExp_10(self, ctx:D96Parser.Exp_10Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_11.
    def visitExp_11(self, ctx:D96Parser.Exp_11Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_RelationalOperand.
    def visitExp_RelationalOperand(self, ctx:D96Parser.Exp_RelationalOperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_Idx.
    def visitExp_Idx(self, ctx:D96Parser.Exp_IdxContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#idx_Operators.
    def visitIdx_Operators(self, ctx:D96Parser.Idx_OperatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_IdxMemberAccess.
    def visitExp_IdxMemberAccess(self, ctx:D96Parser.Exp_IdxMemberAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#idx_MemberAccessOperators.
    def visitIdx_MemberAccessOperators(self, ctx:D96Parser.Idx_MemberAccessOperatorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#scalar_Variable.
    def visitScalar_Variable(self, ctx:D96Parser.Scalar_VariableContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_InstanceAttributeAccess.
    def visitExp_InstanceAttributeAccess(self, ctx:D96Parser.Exp_InstanceAttributeAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_InstanceAttributeAccessTerm.
    def visitExp_InstanceAttributeAccessTerm(self, ctx:D96Parser.Exp_InstanceAttributeAccessTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_InstanceMethodInvocation.
    def visitExp_InstanceMethodInvocation(self, ctx:D96Parser.Exp_InstanceMethodInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_InstanceMethodInvocationTerm.
    def visitExp_InstanceMethodInvocationTerm(self, ctx:D96Parser.Exp_InstanceMethodInvocationTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_StaticAttributeAccess.
    def visitExp_StaticAttributeAccess(self, ctx:D96Parser.Exp_StaticAttributeAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_StaticMethodInvocation.
    def visitExp_StaticMethodInvocation(self, ctx:D96Parser.Exp_StaticMethodInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#exp_ObjCreation.
    def visitExp_ObjCreation(self, ctx:D96Parser.Exp_ObjCreationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_Expr.
    def visitList_Expr(self, ctx:D96Parser.List_ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#type_Data.
    def visitType_Data(self, ctx:D96Parser.Type_DataContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#type_DataArray.
    def visitType_DataArray(self, ctx:D96Parser.Type_DataArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#array_Type.
    def visitArray_Type(self, ctx:D96Parser.Array_TypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#seq_ID.
    def visitSeq_ID(self, ctx:D96Parser.Seq_IDContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_Attribute.
    def visitList_Attribute(self, ctx:D96Parser.List_AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_AttributeTerm.
    def visitList_AttributeTerm(self, ctx:D96Parser.List_AttributeTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_AttributeDeclaration.
    def visitStmt_AttributeDeclaration(self, ctx:D96Parser.Stmt_AttributeDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#lhs.
    def visitLhs(self, ctx:D96Parser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_Assign.
    def visitStmt_Assign(self, ctx:D96Parser.Stmt_AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_If.
    def visitStmt_If(self, ctx:D96Parser.Stmt_IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_ForIn.
    def visitStmt_ForIn(self, ctx:D96Parser.Stmt_ForInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_Block.
    def visitStmt_Block(self, ctx:D96Parser.Stmt_BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_MethodInvocation.
    def visitStmt_MethodInvocation(self, ctx:D96Parser.Stmt_MethodInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_Continue.
    def visitStmt_Continue(self, ctx:D96Parser.Stmt_ContinueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_Return.
    def visitStmt_Return(self, ctx:D96Parser.Stmt_ReturnContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_Break.
    def visitStmt_Break(self, ctx:D96Parser.Stmt_BreakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_AttributeMethod.
    def visitList_AttributeMethod(self, ctx:D96Parser.List_AttributeMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_AttributeMethodTerm.
    def visitList_AttributeMethodTerm(self, ctx:D96Parser.List_AttributeMethodTermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_MethodVarDeclaration.
    def visitStmt_MethodVarDeclaration(self, ctx:D96Parser.Stmt_MethodVarDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt.
    def visitStmt(self, ctx:D96Parser.StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_Stmt.
    def visitList_Stmt(self, ctx:D96Parser.List_StmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_ClassMethod.
    def visitStmt_ClassMethod(self, ctx:D96Parser.Stmt_ClassMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_ClassDeclaration.
    def visitStmt_ClassDeclaration(self, ctx:D96Parser.Stmt_ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#stmt_MethodDeclaration.
    def visitStmt_MethodDeclaration(self, ctx:D96Parser.Stmt_MethodDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_Construction.
    def visitClass_Construction(self, ctx:D96Parser.Class_ConstructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#class_Destruction.
    def visitClass_Destruction(self, ctx:D96Parser.Class_DestructionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#list_Parameters.
    def visitList_Parameters(self, ctx:D96Parser.List_ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#seq_Parameters.
    def visitSeq_Parameters(self, ctx:D96Parser.Seq_ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#seq_IDParameters.
    def visitSeq_IDParameters(self, ctx:D96Parser.Seq_IDParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#lit_Array.
    def visitLit_Array(self, ctx:D96Parser.Lit_ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by D96Parser#lit_Data.
    def visitLit_Data(self, ctx:D96Parser.Lit_DataContext):
        return self.visitChildren(ctx)



del D96Parser