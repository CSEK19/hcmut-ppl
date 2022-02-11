from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *


class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        list_class = []
        for class_decl in ctx.stmt_ClassDeclaration():
            list_class = list_class + [self.visit(class_decl)]
        return Program(list_class)

    def visitStmt_ClassDeclaration(self, ctx:D96Parser.Stmt_ClassDeclarationContext):
        class_name = Id(ctx.ID()[0].getText())
        parent_name = None
        if len(ctx.ID()) == 2:
            parent_name = Id(ctx.ID()[1].getText())
        mem_list = self.visit(ctx.stmt_ClassBody())
        return ClassDecl(class_name, mem_list, parent_name)

    def visitStmt_ClassBody(self, ctx:D96Parser.Stmt_ClassBodyContext):
        class_body = []
        if ctx.getChildCount() != 2:
            for stmtClass in range(1, ctx.getChildCount() - 1):
                class_body = class_body + self.visit(ctx.getChild(stmtClass))
        return class_body

    def visitStmt_AttributeDeclaration(self, ctx:D96Parser.Stmt_AttributeDeclarationContext):
        kind, attr_name, attr_type, attr_value = self.visit(ctx.list_Attribute())
        tuple_seq_attr = zip(kind, attr_name, attr_value)
        list_attr_decl = []

        for kind_, attr_name_, attr_value_ in tuple_seq_attr:
            if ctx.VAR():
                list_attr_decl = list_attr_decl + [AttributeDecl(kind_, VarDecl(attr_name_, attr_type, attr_value_))]
            if ctx.VAL():
                list_attr_decl = list_attr_decl + [AttributeDecl(kind_, ConstDecl(attr_name_, attr_type, attr_value_))]

        return list_attr_decl

    def visitList_Attribute(self, ctx:D96Parser.List_AttributeContext):
        if ctx.list_AttributeTerm():
            kind, attr_list, attr_value = [], [], []
            for attr in ctx.getChildren():
                if attr in (ctx.ID() + ctx.STATIC_ID()):
                    attr_list = attr_list + [Id(attr.getText())]
                    if attr in ctx.ID():
                        kind = kind + [Instance()]
                    else:
                        kind = kind + [Static()]

            attr_value = [self.visit(ctx.expr())]
            kind_, attr_list_, attr_type, attr_value_ = self.visit(ctx.list_AttributeTerm())

            kind = kind + kind_
            attr_list = attr_list + attr_list_
            atr_value = attr_value + attr_value_

            atr_value.reverse()
            return kind, attr_list, attr_type, attr_value

        else:
            kind, attr_list, attr_value = [], [], []
            for attr in ctx.getChildren():
                if attr in (ctx.ID() + ctx.STATIC_ID()):
                    attr_list = attr_list + [Id(attr.getText())]
                    if attr in ctx.ID():
                        kind = kind + [Instance()]
                    else:
                        kind = kind + [Static()]
                    attr_value = attr_value + [None]

            attr_type = self.visit(ctx.type_Data())
            return kind, attr_list, attr_type, attr_value

    def visitList_AttributeTerm(self, ctx:D96Parser.List_AttributeTermContext):
        if ctx.type_Data():
            return [], [], self.visit(ctx.type_Data()), []
        else:
            kind, attr_list, attr_value = [], [], []
            for attr in ctx.getChildren():
                if attr in (ctx.ID() + ctx.STATIC_ID()):
                    attr_list = attr_list + [Id(attr.getText())]
                    if attr in ctx.ID():
                        kind = kind + [Instance()]
                    else:
                        kind = kind + [Static()]
                    attr_value = attr_value + [None]

            attr_value = [self.visit(ctx.expr())]
            kind_, attr_list_, attr_type, attr_value_ = self.visit(ctx.list_AttributeTerm())

            kind = kind + kind_
            attr_list = attr_list + attr_list_
            attr_value = attr_value + attr_value_

            return kind, attr_list, attr_type, attr_value

    def visitType_Data(self, ctx:D96Parser.Type_DataContext):
        if ctx.ID():
            return ClassType(classname=Id(ctx.ID().getText()))
        if ctx.INT():
            return IntType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.BOOLEAN():
            return BoolType()
        if ctx.STRING():
            return StringType()
        return self.visit(ctx.array_Type())

    def visitArray_Type(self, ctx:D96Parser.Array_TypeContext):
        size = int(ctx.INTLIT().getText())
        element_type = self.visit(ctx.type_DataArray())
        return ArrayType(size, element_type)

    def visitType_DataArray(self, ctx:D96Parser.Type_DataArrayContext):
        if ctx.INT():
            return IntType()
        if ctx.FLOAT():
            return FloatType()
        if ctx.BOOLEAN():
            return BoolType()
        if ctx.STRING():
            return StringType()
        return self.visit(ctx.array_Type())

    def visitExpr(self, ctx:D96Parser.ExprContext):
        return self.visit(ctx.exp_0())

    def visitExp_0(self, ctx:D96Parser.Exp_0Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp_1()[0])
        else:
            op = ctx.SADD().getText() if ctx.SADD() else ctx.SEQ().getText()
            left = self.visit(ctx.exp_1()[0])
            right = self.visit(ctx.exp_1()[1])
            return BinaryOp(op, left, right)

    def visitExp_1(self, ctx:D96Parser.Exp_1Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp_2()[0])
        else:
            op = ctx.exp_RelationalOperand().getText()
            left = self.visit(ctx.exp_2()[0])
            right = self .visit(ctx.exp_2()[1])
            return BinaryOp(op, left, right)

    def visitExp_2(self, ctx:D96Parser.Exp_2Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp_3())
        else:
            op = ctx.AND().getText() if ctx.AND() else ctx.OR().getText()
            left = self.visit(ctx.exp_2())
            right = self.visit(ctx.exp_3())
            return BinaryOp(op, left, right)

    def visitExp_3(self, ctx:D96Parser.Exp_3Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp_4())
        else:
            op = ctx.ADD().getText() if ctx.ADD() else ctx.SUB().getText()
            left = self.visit(ctx.exp_3())
            right = self.visit(ctx.exp_4())
            return BinaryOp(op, left, right)

    def visitExp_4(self, ctx:D96Parser.Exp_4Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp_5())
        else:
            op = ctx.MUL().getText()
            if ctx.DIV():
                op = ctx.DIV().getText()
            if ctx.MOD():
                op = ctx.MOD().getText()
            left = self.visit(ctx.exp_4())
            right = self.visit(ctx.exp_5())
            return BinaryOp(op, left, right)

    def visitExp_5(self, ctx:D96Parser.Exp_5Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp_6())
        else:
            op = ctx.NOT().getText()
            body = self.visit(ctx.exp_5())
            return UnaryOp(op, body)

    def visitExp_6(self, ctx:D96Parser.Exp_6Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp_7())
        else:
            op = ctx.SUB().getText()
            body = self.visit(ctx.exp_6())
            return UnaryOp(op, body)

    def visitExp_7(self, ctx:D96Parser.Exp_7Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp_8())
        else:
            # TODO?
            idx = []
            for exp_idx in range(len(ctx.expr())):
                idx = idx + [self.visit(ctx.expr(exp_idx))]
            arr = self.visit(ctx.exp_7())
            return ArrayCell(arr, idx)

    def visitExp_8(self, ctx:D96Parser.Exp_8Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp_9())
        else:
            obj = self.visit(ctx.exp_8())
            if ctx.list_Expr():
                method = Id(ctx.ID().getText())
                param = self.visit(ctx.list_Expr())
                return CallExpr(obj, method , param)
            else:
                fieldname = Id(ctx.ID().getText())
                return FieldAccess(obj, fieldname)

    def visitExp_9(self, ctx:D96Parser.Exp_9Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp_10())
        else:
            pass

    def visitExp_10(self, ctx:D96Parser.Exp_10Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp_11())
        else:
            classname = self.visit(ctx.exp_10())
            param = self.visit(ctx.list_Expr())
            return NewExpr(classname, param)

    def visitExp_11(self, ctx:D96Parser.Exp_11Context):
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.SELF():
            return SelfLiteral()
        if ctx.NULL():
            return NullLiteral()
        if ctx.lit_Data():
            return self.visit(ctx.lit_Data())
        if ctx.expr():
            return self.visit(ctx.expr())

    def visitList_Expr(self, ctx:D96Parser.List_ExprContext):
        list_expr = []
        for expr_temp in range(len(ctx.expr())):
            list_expr = list_expr + [self.visit(ctx.expr(expr_temp))]
        return list_expr

    ### TODO STATEMENT ##

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
            return BooleanLiteral(bool(ctx.BOOLLIT().getText() == 'True'))
        elif ctx.STRLIT():
            return StringLiteral(str(ctx.STRLIT().getText()))
        else:
            return ArrayLiteral(self.visit(ctx.lit_Array()))




