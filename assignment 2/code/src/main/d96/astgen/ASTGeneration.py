from D96Visitor import D96Visitor
from D96Parser import D96Parser
from AST import *


class ASTGeneration(D96Visitor):
    def visitProgram(self, ctx: D96Parser.ProgramContext):
        list_class = []
        for class_decl in ctx.stmt_ClassDeclaration():
            list_class = list_class + self.visit(class_decl)
        return Program(list_class)

    def visitStmt_ClassDeclaration(self, ctx:D96Parser.Stmt_ClassDeclarationContext):
        class_name = Id(ctx.ID()[0].getText())
        parent_name = None
        if len(ctx.ID()) == 2:
            parent_name = Id(ctx.ID()[1].getText())
        mem_list = self.visit(ctx.stmt_ClassBody())
        return [ClassDecl(class_name, mem_list, parent_name)]

    def visitStmt_ClassBody(self, ctx:D96Parser.Stmt_ClassBodyContext):
        class_body = []
        for element in ctx.getChildren():
            if element not in ([ctx.LCB()] + [ctx.RCB()]):
                class_body = class_body + self.visit(element)
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
            attr_value = attr_value + attr_value_

            attr_value.reverse()
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
                if attr in ([ctx.ID()] + [ctx.STATIC_ID()]):
                    attr_list = attr_list + [Id(attr.getText())]
                    if attr in [ctx.ID()]:
                        kind = kind + [Instance()]
                    if attr in [ctx.STATIC_ID()]:
                        kind = kind + [Static()]

            attr_value = [self.visit(ctx.expr())]
            kind_, attr_list_, attr_type, attr_value_ = self.visit(ctx.list_AttributeTerm())

            kind = kind + kind_
            attr_list = attr_list + attr_list_
            attr_value = attr_value + attr_value_

            return kind, attr_list, attr_type, attr_value

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
            op = None
            if ctx.MUL():
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
                return CallExpr(obj, method, param)
            else:
                fieldname = Id(ctx.ID().getText())
                return FieldAccess(obj, fieldname)

    def visitExp_9(self, ctx:D96Parser.Exp_9Context):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp_10())
        else:
            obj = Id(ctx.ID().getText())
            if ctx.list_Expr():
                method = Id(ctx.STATIC_ID().getText())
                param = self.visit(ctx.list_Expr())
                return CallExpr(obj, method, param)
            else:
                fieldname = Id(ctx.STATIC_ID().getText())
                return FieldAccess(obj, fieldname)

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

    def visitList_Parameters(self, ctx:D96Parser.List_ParametersContext):
        list_param = []
        for element in range(len(ctx.seq_Parameters())):
            list_param = list_param + self.visit(ctx.seq_Parameters(element))
        return list_param

    def visitSeq_Parameters(self, ctx:D96Parser.Seq_ParametersContext):
        attr_type = self.visit(ctx.type_Data())
        list_attr = self.visit(ctx.seq_IDParameters())
        list_parameter = []
        for idx in range(len(list_attr)):
            list_parameter = list_parameter + [VarDecl(Id(list_attr[idx]), attr_type)]
        return list_parameter

    def visitSeq_IDParameters(self, ctx:D96Parser.Seq_IDParametersContext):
        list_id = []
        for attr in ctx.getChildren():
            if attr in ctx.ID():
                list_id = list_id + [attr.getText()]
        return list_id

    def visitStmt_ClassMethod(self, ctx:D96Parser.Stmt_ClassMethodContext):
        if ctx.stmt_ClassConstruction():
            return self.visit(ctx.stmt_ClassConstruction())
        if ctx.stmt_ClassDestruction():
            return self.visit(ctx.stmt_ClassDestruction())

    def visitStmt_ClassConstruction(self, ctx:D96Parser.Stmt_ClassConstructionContext):
        name = '"Constructor"'
        param = self.visit(ctx.list_Parameters())
        body = self.visit(ctx.stmt_Block())
        return [MethodDecl(Instance(), Id(name), param, body)]

    def visitStmt_ClassDestruction(self, ctx:D96Parser.Stmt_ClassDestructionContext):
        name = '"Destructor"'
        param = []
        body = self.visit(ctx.stmt_Block())
        return [MethodDecl(Instance(), Id(name), param, body)]

    def visitStmt(self, ctx:D96Parser.StmtContext):
        if ctx.stmt_Assign():
            return [self.visit(ctx.stmt_Assign())]
        if ctx.stmt_Block():
            return [self.visit(ctx.stmt_Block())]
        if ctx.stmt_Break():
            return [self.visit(ctx.stmt_Break())]
        if ctx.stmt_Continue():
            return [self.visit(ctx.stmt_Continue())]
        if ctx.stmt_ForIn():
            return [self.visit(ctx.stmt_ForIn())]
        if ctx.stmt_If():
            return [self.visit(ctx.stmt_If())]
        if ctx.stmt_MethodInvocation():
            return [self.visit(ctx.stmt_MethodInvocation())]
        if ctx.stmt_Return():
            return [self.visit(ctx.stmt_Return())]

    def visitList_Stmt(self, ctx:D96Parser.List_StmtContext):
        inst = []
        for element in ctx.getChildren():
            inst = inst + self.visit(element)
        return inst

    def visitStmt_Assign(self, ctx:D96Parser.Stmt_AssignContext):
        lhs = self.visit(ctx.lhs())
        exp = self.visit(ctx.expr())
        return Assign(lhs, exp)

    def visitStmt_Block(self, ctx:D96Parser.Stmt_BlockContext):
        inst = []
        if ctx.list_Stmt():
                inst = inst + self.visit(ctx.list_Stmt())
        return Block(inst)

    def visitStmt_Break(self, ctx:D96Parser.Stmt_BreakContext):
        return Break()

    def visitStmt_Continue(self, ctx:D96Parser.Stmt_ContinueContext):
        return Continue()

    def visitStmt_Return(self, ctx:D96Parser.Stmt_ReturnContext):
        expr = None
        if ctx.expr():
            expr = self.visit(ctx.expr())
        return Return(expr)

    def visitStmt_ForIn(self, ctx:D96Parser.Stmt_ForInContext):
        expr3 = None

        id = Id(ctx.ID().getText())
        expr1 = self.visit(ctx.expr()[0])
        expr2 = self.visit(ctx.expr()[1])
        loop = self.visit(ctx.stmt_Block())
        if len(ctx.expr()) > 2:
            expr3 = self.visit(ctx.expr()[2])

        return For(id, expr1, expr2, loop, expr3)

    def visitStmt_If(self, ctx:D96Parser.Stmt_IfContext):
        expr = None
        then_stmt = None
        else_stmt = None

        if not ctx.ELSE():
            idx_stmt = range(len(ctx.stmt_Block()))
            for i in reversed(idx_stmt):
                expr = self.visit(ctx.expr()[i])
                then_stmt = self.visit(ctx.stmt_Block()[i])
                else_stmt = If(expr, then_stmt, else_stmt)

            return else_stmt

        if ctx.ELSE():
            expr = self.visit(ctx.expr()[0])
            then_stmt = self.visit(ctx.stmt_Block()[0])

            if len(ctx.stmt_Block()) == 2:
                else_stmt = self.visit(ctx.stmt_Block()[1])

            if len(ctx.stmt_Block()) > 2:
                idx_stmt = range(len(ctx.stmt_Block()))
                expr_ = None
                then_stmt_ = None
                else_stmt_ = None

                for i in reversed(idx_stmt):
                    if i == 1:
                        break
                    if i == max(idx_stmt):
                        else_stmt_ = self.visit(ctx.stmt_Block()[i])
                    expr_ = self.visit(ctx.expr()[i - 1])
                    then_stmt_ = self.visit(ctx.stmt_Block()[i - 1])
                    else_stmt_ = If(expr_, then_stmt_, else_stmt_)

                else_stmt = else_stmt_
        return If(expr, then_stmt, else_stmt)

    def visitExp_8_MethodInvocation(self, ctx:D96Parser.Exp_8_MethodInvocationContext):
        if ctx.getChildCount() == 1:
            return self.visit(ctx.exp_9())
        else:
            obj = self.visit(ctx.exp_8_MethodInvocation())
            if ctx.list_Expr():
                method = Id(ctx.ID().getText())
                param = self.visit(ctx.list_Expr())
                return CallExpr(obj, method, param)
            else:
                fieldname = Id(ctx.ID().getText())
                return FieldAccess(obj, fieldname)

    def visitStmt_MethodInvocation(self, ctx:D96Parser.Stmt_MethodInvocationContext):
        obj = []
        method = []
        param = []

        if ctx.exp_8_MethodInvocation():
            obj = self.visit(ctx.exp_8_MethodInvocation())
            method = Id(ctx.ID().getText())
            param = self.visit(ctx.list_Expr())

        if ctx.exp_9():
            obj = self.visit(ctx.exp_9())
            method = Id(ctx.ID().getText())
            param = self.visit(ctx.list_Expr())

        if ctx.exp_10():
            obj = self.visit(ctx.exp_10())
            method = Id(ctx.STATIC_ID().getText())
            param = self.visit(ctx.list_Expr())

        return CallStmt(obj, method, param)

    def visitStmt_MethodVarDeclaration(self, ctx:D96Parser.Stmt_MethodVarDeclarationContext):
        attr, attr_type, attr_value = self.visit(ctx.list_AttributeMethod())
        tuple_list_attr = zip(attr, attr_value)
        list_attr = []
        if ctx.VAR():
            for (attr_, attr_value_) in tuple_list_attr:
                list_attr = list_attr + [VarDecl(attr_, attr_type, attr_value_)]
        if ctx.VAL():
            for (attr_, attr_value_) in tuple_list_attr:
                list_attr = list_attr + [ConstDecl(attr_, attr_type, attr_value_)]
        return list_attr

    def visitList_AttributeMethod(self, ctx:D96Parser.List_AttributeMethodContext):
        attr, attr_type, attr_value = [], [], []

        if ctx.list_AttributeMethodTerm():
            for element in ctx.getChildren():
                if element in ctx.ID():
                    attr = attr + [Id(element.getText())]
            attr_value = [self.visit(ctx.expr())]

            attr_, attr_type, attr_value_ = self.visit(ctx.list_AttributeMethodTerm())

            attr = attr + attr_
            attr_value = attr_value + attr_value_

            attr_value.reverse()
            return attr, attr_type, attr_value
        else:
            attr_type = self.visit(ctx.type_Data())
            for element in ctx.ID():
                attr = attr + [Id(element.getText())]
                attr_value = attr_value + [None]
            return attr, attr_type, attr_value

    def visitList_AttributeMethodTerm(self, ctx:D96Parser.List_AttributeMethodTermContext):
        if ctx.type_Data():
            return [], self.visit(ctx.type_Data()), []
        else:
            attr, attr_type, attr_value = [], [], []
            for element in ctx.getChildren():
                if element in [ctx.ID()]:
                    attr = attr + [Id(element.getText())]

            attr_value = [self.visit(ctx.expr())]

            attr_, attr_type, attr_value_ = self.visit(ctx.list_AttributeMethodTerm())

            attr = attr + attr_
            attr_value = attr_value + attr_value_

            return attr, attr_type, attr_value

    def visitStmt_MethodDeclaration(self, ctx:D96Parser.Stmt_MethodDeclarationContext):
        kind = None
        name = None
        param = []
        body = self.visit(ctx.stmt_Block())

        if ctx.list_Parameters():
            param = self.visit(ctx.list_Parameters())

        if not ctx.STATIC_ID() and ctx.ID().getText() == 'main':
            class_body = ctx.parentCtx
            class_decl = class_body.parentCtx
            class_name = class_decl.ID()[0].getText()

            if class_name == 'Program':
                if not param:
                    kind = Static()
                    name = Id(ctx.ID().getText())
                    return [MethodDecl(kind, name, param, body)]

        if ctx.ID():
            kind = Instance()
            name = Id(ctx.ID().getText())
        if ctx.STATIC_ID():
            kind = Static()
            name = Id(ctx.STATIC_ID().getText())

        return [MethodDecl(kind, name, param, body)]

    def visitLhs(self, ctx:D96Parser.LhsContext):
        if ctx.ID():
            return Id(ctx.ID().getText())
        if ctx.exp_7():
            return self.visit(ctx.exp_7())

    def visitType_Data(self, ctx:D96Parser.Type_DataContext):
        if ctx.ID():
            return ClassType(Id(ctx.ID().getText()))
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
        size = None
        if ctx.INTLIT():
            if ctx.INTLIT().getText()[0] == '0':
                if ctx.INTLIT().getText()[1] in ['b', 'B']:
                    size = (int(ctx.INTLIT().getText(), 2))
                elif ctx.INTLIT().getText()[1] in ['x', 'X']:
                    size = (int(ctx.INTLIT().getText(), 16))
                else:
                    size = (int(ctx.INTLIT().getText(), 8))
            else:
                size = (int(ctx.INTLIT().getText(), 10))
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

    def visitLit_Array(self, ctx:D96Parser.Lit_ArrayContext):
        value = []
        if ctx.list_Expr():
            value = value + self.visit(ctx.list_Expr())
        return ArrayLiteral(value)

    def visitLit_Data(self, ctx:D96Parser.Lit_DataContext):
        if ctx.INTLIT():
            if ctx.getText()[0] == '0':
                if ctx.getText()[1] in ['b', 'B']:
                    return IntLiteral(int(ctx.INTLIT().getText(), 2))
                if ctx.getText()[1] in ['x', 'X']:
                    return IntLiteral(int(ctx.INTLIT().getText(), 16))
                else:
                    return IntLiteral(int(ctx.INTLIT().getText(), 8))
            else:
                return IntLiteral(int(ctx.INTLIT().getText(), 10))
        elif ctx.ZERO():
            if len(ctx.getText()) == 1:
                return IntLiteral(int(ctx.ZERO().getText(), 10))
            else:
                if ctx.getText()[1] in ['b', 'B']:
                    return IntLiteral(int(ctx.ZERO().getText(), 2))
                if ctx.getText()[1] in ['x', 'X']:
                    return IntLiteral(int(ctx.ZERO().getText(), 16))
                else:
                    return IntLiteral(int(ctx.ZERO().getText(), 8))
        elif ctx.FLOATLIT():
            return FloatLiteral(float(ctx.FLOATLIT().getText()))
        elif ctx.BOOLLIT():
            return BooleanLiteral(bool(ctx.BOOLLIT().getText() == 'True'))
        elif ctx.STRLIT():
            return StringLiteral(str(ctx.STRLIT().getText()))
        else:
            return self.visit(ctx.lit_Array())
