from CASSVisitor import CASSVisitor
from CASSParser import CASSParser
from CASSNode import CassNode  # or define CassNode inline here if you prefer

class MyCassVisitor(CASSVisitor):

    def visitProg(self, ctx: CASSParser.ProgContext):
        # 'prog' might be your top-level rule
        root = CassNode("prog")
        for func_def_ctx in ctx.functionDefinition():
            func_node = self.visit(func_def_ctx)
            root.add_child(func_node)
        return root

    # def visitFunctionDefinition(self, ctx: CASSParser.FunctionDefinitionContext):
    #     # For example: "int summation(int start_val, int end_val) { ... }"
    #     # Instead of a deep AST, we create a simpler node
    #     func_name = ctx.ID().getText()  # e.g. "summation"
    #     node = CassNode(f"function:{func_name}")
    #     # Gather parameters
    #     if ctx.parameterList():
    #         params_node = self.visit(ctx.parameterList())
    #         node.add_child(params_node)
    #     # Visit the compoundStatement
    #     block_node = self.visit(ctx.compoundStatement())
    #     node.add_child(block_node)
    #     return node

    def visitParameterList(self, ctx: CASSParser.ParameterListContext):
        node = CassNode("params")
        for p in ctx.parameter():
            node.add_child(self.visit(p))
        return node

    def visitParameter(self, ctx: CASSParser.ParameterContext):
        # e.g. "int start_val"
        param_name = ctx.ID().getText()
        return CassNode(f"#VAR:{param_name}")

    def visitCompoundStatement(self, ctx: CASSParser.CompoundStatementContext):
        block_node = CassNode("#compound_statement#{$}")
        for st in ctx.statement():
            stmt_node = self.visit(st)   # e.g. $; => $+=$ => (#VAR:sum, #VAR:j)
            block_node.add_child(stmt_node)
        return block_node
    

    def visitDeclarationStatement(self, ctx: CASSParser.DeclarationStatementContext):
        
        type_label = ctx.typeSpec().getText()   # e.g. "int"
        decl_node = CassNode(f"{type_label}$;") ##intermediate nodes

        # e.g. "int sum = 0;"
        var_name = ctx.ID().getText()
        if ctx.expression():
            assign_node = CassNode("$=$")
            assign_node.add_child(CassNode(f"#VAR:{var_name}"))

            # Visit the expression to see if it's #VAR or #LIT or something else
            value_node = self.visit(ctx.expression())
            assign_node.add_child(value_node)

            # Add `$=$` as the child of the `int$;` node
            decl_node.add_child(assign_node)
        else:
            # no initializer, just add #VAR as a child
            decl_node.add_child(CassNode(f"#VAR:{var_name}"))

        return decl_node
    
    def visitForInit(self, ctx: CASSParser.ForInitContext):
        """
        Grammar rule: forInit : typeSpec ID '=' expression ;
        e.g. "int i = start_val"
        We want:
        (int$;)
            \
            ($=$)
            /   \
        (#VAR:i) (#VAR:start_val or #LIT:0 etc.)
        """

        # 1) Create the top-level node for the type, e.g. "int$;"
        type_text = ctx.typeSpec().getText()  # should be "int"
        init_node = CassNode(f"{type_text}$;")

        # 2) Create the "$=$" node
        assign_node = CassNode("$=$")

        # 3) The left side is the variable being declared
        var_name = ctx.ID().getText()  # e.g. "i"
        var_node = CassNode(f"#VAR:{var_name}")
        assign_node.add_child(var_node)

        # 4) The right side is the expression
        expr_node = self.visit(ctx.expression())  # this might yield #VAR:start_val, #LIT:0, etc.
        assign_node.add_child(expr_node)

        # Link everything: "int$;" -> "$=$"
        init_node.add_child(assign_node)

        return init_node



    def visitForBlockStatement(self, ctx: CASSParser.ForBlockStatementContext):
        for_node = CassNode("for($$;$)$")

        # Initialization (forInit)
        if ctx.forInit():
            init_node = self.visit(ctx.forInit())
            for_node.add_child(init_node)
        else:
            for_node.add_child(CassNode("EMPTY_INIT"))

        # Condition
        if ctx.expression():
            cond_node = self.visit(ctx.expression())
            for_node.add_child(cond_node)
        else:
            for_node.add_child(CassNode("EMPTY_COND"))

        # Update (forUpdate)
        if ctx.forUpdate():
            update_node = self.visit(ctx.forUpdate())
            for_node.add_child(update_node)
        else:
            for_node.add_child(CassNode("EMPTY_UPDATE"))

        # Body (multiple statements in the block)
        for stmt_ctx in ctx.statement():
            stmt_node = self.visit(stmt_ctx)
            for_node.add_child(stmt_node)

        return for_node
    
    def visitForSingleStatement(self, ctx: CASSParser.ForSingleStatementContext):
        for_node = CassNode("for($$;$)$")

        # Initialization (forInit)
        if ctx.forInit():
            init_node = self.visit(ctx.forInit())
            for_node.add_child(init_node)
        else:
            for_node.add_child(CassNode("EMPTY_INIT"))

        # Condition
        if ctx.expression():
            cond_node = self.visit(ctx.expression())
            for_node.add_child(cond_node)
        else:
            for_node.add_child(CassNode("EMPTY_COND"))

        # Update (forUpdate)
        if ctx.forUpdate():
            update_node = self.visit(ctx.forUpdate())
            for_node.add_child(update_node)
        else:
            for_node.add_child(CassNode("EMPTY_UPDATE"))

        # Body (single statement)
        body_node = self.visit(ctx.statement())
        for_node.add_child(body_node)


        return for_node


    
    def visitWhileBlockStatement(self, ctx: CASSParser.WhileBlockStatementContext):
        while_node = CassNode("while($;$)")

        # Condition
        cond_node = self.visit(ctx.expression())
        while_node.add_child(cond_node)

        # Body (multiple statements)
        for stmt_ctx in ctx.statement():
            stmt_node = self.visit(stmt_ctx)
            while_node.add_child(stmt_node)

        return while_node
    
    def visitWhileSingleStatement(self, ctx: CASSParser.WhileSingleStatementContext):
        while_node = CassNode("while($;$)")

        # Condition
        cond_node = self.visit(ctx.expression())
        while_node.add_child(cond_node)

        # Single body statement
        body_node = self.visit(ctx.statement())
        while_node.add_child(body_node)

        return while_node
    
    def visitIfBlockStatement(self, ctx: CASSParser.IfBlockStatementContext):
        # Create a node for the "if" statement
        if_node = CassNode("if($;$)")

        # Condition (the part in parentheses)
        cond_node = self.visit(ctx.expression())
        if_node.add_child(cond_node)

        # Separate "if" and "else" blocks
        if_block = []
        else_block = []

        # Iterate through statements to determine if they belong to "if" or "else"
        has_else = False
        for i, child in enumerate(ctx.children):
            if child.getText() == "else":
                has_else = True  # We found the "else"
            elif isinstance(child, CASSParser.StatementContext):
                # Add to "else" block if we're in the "else" part
                if has_else:
                    else_block.append(child)
                else:
                    if_block.append(child)

        # Process "if" block statements
        for stmt_ctx in if_block:
            stmt_node = self.visit(stmt_ctx)
            if_node.add_child(stmt_node)

        # Process "else" block statements, if any
        if has_else:
            else_node = CassNode("else")
            for stmt_ctx in else_block:
                stmt_node = self.visit(stmt_ctx)
                else_node.add_child(stmt_node)
            if_node.add_child(else_node)

        return if_node


    
    def visitIfSingleStatement(self, ctx: CASSParser.IfSingleStatementContext):
        # Create a node for the "if" statement
        if_node = CassNode("if($;$)")

        # Condition
        cond_node = self.visit(ctx.expression())
        if_node.add_child(cond_node)

        # Single "if" body statement
        if_body_node = self.visit(ctx.statement(0))
        if_node.add_child(if_body_node)

        # Optional "else"
        if ctx.statement(1):
            else_node = CassNode("else")
            else_body_node = self.visit(ctx.statement(1))
            else_node.add_child(else_body_node)
            if_node.add_child(else_node)

        return if_node



    def visitRelationalExpression(self, ctx: CASSParser.RelationalExpressionContext):
    # If there's only one child additiveExpression, just pass it up the chain
        if len(ctx.children) == 1:
            return self.visit(ctx.additiveExpression(0))

        # If there's an operator like "<=" or ">" ...
        left = self.visit(ctx.additiveExpression(0))
        op = ctx.getChild(1).getText()  # e.g. "<="
        right = self.visit(ctx.additiveExpression(1))

        # Create a node labeled "$<=$" (or "$>$" etc.)
        node = CassNode(f"${op}$")
        node.add_child(left)
        node.add_child(right)
        return node


    def visitReturnStatement(self, ctx: CASSParser.ReturnStatementContext):
        # e.g. "return sum;"
        node = CassNode("return$")
        if ctx.expression():
            expr_node = self.visit(ctx.expression())
            node.add_child(expr_node)
        return node

    def visitExpressionStatement(self, ctx: CASSParser.ExpressionStatementContext):

        statement_node = CassNode("$;")

        # 2) Visit the expression, which might yield something like "$+=$"
        expr_node = self.visit(ctx.expression())

        # 3) Add it as a child
        statement_node.add_child(expr_node)

        return statement_node


    # ---------------------
    # Expression Collapsing
    # ---------------------
    def visitExpression(self, ctx: CASSParser.ExpressionContext):
        # This might still be a nest of sub-rules:
        # assignmentExpression, unaryExpression, logicalAndExpression, etc.
        # Instead of recursing deeply, we can unify them:

        # We can just do:
        return self.visit(ctx.assignmentExpression())

    def visitAssignmentExpression(self, ctx: CASSParser.AssignmentExpressionContext):
        # We'll check if we have something like "sum += i"
        if ctx.assignmentOperator():
            # e.g. sum += i
            op = ctx.assignmentOperator().getText()  # '+='
            op = f"${op}$"
            lhs = self.visit(ctx.unaryExpression())
            rhs = self.visit(ctx.assignmentExpression())
            node = CassNode(op)
            node.add_child(lhs)
            node.add_child(rhs)
            return node
        else:
            # We presumably have logicalOrExpression
            return self.visit(ctx.logicalOrExpression())

    def visitUnaryExpression(self, ctx: CASSParser.UnaryExpressionContext):
        # e.g. ++i, primaryExpression, etc.
        text = ctx.getText()
        # If it's prefix like ++i
        if ctx.unaryExpression():
            # e.g. '++' unaryExpression
            # We'll produce a node for e.g. '++ #VAR'
            op = text[:2]  + "$" # '++' or '--'
            var_text = ctx.unaryExpression().getText()
            node = CassNode(op)
            node.add_child(CassNode(f"#VAR:{var_text}"))
            return node
        else:
            # We might have a primary expression
            return self.visit(ctx.primaryExpression())

    def visitPrimaryExpression(self, ctx: CASSParser.PrimaryExpressionContext):
        if ctx.ID():
            var_text = ctx.ID().getText()
            return CassNode(f"#VAR:{var_text}")
        elif ctx.INT():
            lit_text = ctx.INT().getText()
            return CassNode(f"#LIT:{lit_text}")
        elif ctx.expression():
            # ( expression )
            return self.visit(ctx.expression())
        else:
            return CassNode("???")  # Fallback
