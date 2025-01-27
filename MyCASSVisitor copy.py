from CASSVisitor import CASSVisitor
from CASSParser import CASSParser
from CASSNode import CassNode  # or define CassNode inline here if you prefer

class MyCassVisitor(CASSVisitor):

    def visitProg(self, ctx: CASSParser.ProgContext):
        # 'prog' might be your top-level rule
        root = CassNode("root")
        for statement in ctx.statement():
            n = self.visit(statement)
            root.add_child(n)
        return root

    def visitFunctionDefinition(self, ctx: CASSParser.FunctionDefinitionContext):
        func_type = 1 if ctx.typeSpec().getText() != 'void' else 0
        params_num = len(ctx.parameterList().parameter()) if ctx.parameterList() else 0
        if params_num > 2:
            paramsnum = 2

        node = CassNode(f"S#FS#{func_type}{params_num}")
        # Gather parameters
        if ctx.parameterList():
            params_node = self.visit(ctx.parameterList())
            node.add_child(params_node)
        # Visit the compoundStatement
        block_node = self.visit(ctx.compoundStatement())
        node.add_child(block_node)
        return node

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
        # Count the number of direct statements (children) in the compound statement
        num_children = len(ctx.statement())
        dollar_placeholders = "$" * num_children  # Create the correct number of $ placeholders
        block_node = CassNode(f"#compound_statement#{{{dollar_placeholders}}}")

        # Add each statement as a direct child
        for st in ctx.statement():
            stmt_node = self.visit(st)
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
    
    def visitAdditiveExpression(self, ctx: CASSParser.AdditiveExpressionContext):
        # If there's only one child, pass it up the chain (e.g., "a")
        if len(ctx.children) == 1:
            return self.visit(ctx.multiplicativeExpression(0))

        # If there are multiple operands, create a node for each operator and operand
        operands = ctx.multiplicativeExpression()
        result = self.visit(operands[0])  # Start with the first operand

        for i in range(1, len(operands)):
            operator = ctx.getChild(2 * i - 1).getText()  # Get "+" or "-"
            next_operand = self.visit(operands[i])
            operator_node = CassNode(f"${operator}$")
            operator_node.add_child(result)
            operator_node.add_child(next_operand)
            result = operator_node  # Update the result to the new operator node

        return result
    
    def visitMultiplicativeExpression(self, ctx: CASSParser.MultiplicativeExpressionContext):
        # If there's only one child, pass it up the chain (e.g., "a")
        if len(ctx.children) == 1:
            return self.visit(ctx.unaryExpression(0))

        # If there are multiple operands, create a node for each operator and operand
        operands = ctx.unaryExpression()
        result = self.visit(operands[0])  # Start with the first operand

        for i in range(1, len(operands)):
            operator = ctx.getChild(2 * i - 1).getText()  # Get "*" or "/"
            next_operand = self.visit(operands[i])
            operator_node = CassNode(f"${operator}$")
            operator_node.add_child(result)
            operator_node.add_child(next_operand)
            result = operator_node  # Update the result to the new operator node

        return result






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
        if ctx.assignmentExpression():
            return self.visit(ctx.assignmentExpression())
        return None


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
        # Case 1: It's an identifier
        if ctx.ID():
            var_text = ctx.ID().getText()
            return CassNode(f"#VAR:{var_text}")
        
        # Case 2: It's an integer literal
        elif ctx.INT():
            lit_text = ctx.INT().getText()
            return CassNode(f"#LIT:{lit_text}")
        
        # Case 3: It's a float literal
        elif ctx.FLOAT():
            lit_text = ctx.FLOAT().getText()
            return CassNode(f"#LIT:{lit_text}")
        
        # Case 4: It's parentheses => ( expression )
        elif ctx.expression():
            # 1) Visit the sub-expression
            subexpr_node = self.visit(ctx.expression())

            # 2) Check if subexpr_node is an additive expression
            #    For example, if your additive visitor produces "$+$" or "$-$" as the label:
            if subexpr_node and subexpr_node.label in {"$+$", "$-$", "$*$", "$/$", "$%$"}:
                # Create a paren node
                paren_node = CassNode("#paren_op_exp#($)")
                paren_node.add_child(subexpr_node)
                return paren_node
            else:
                # If not additive, just return the inner expression without special wrapping
                return subexpr_node
        
        # Fallback if something unexpected
        else:
            return CassNode("???")

##addddd modulo digggaaqaa