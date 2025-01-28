from CASSVisitor import CASSVisitor
from CASSParser import CASSParser
from CASSNode import CassNode  # or define CassNode inline here if you prefer

class MyCassVisitor(CASSVisitor):

    def __init__(self):
        super().__init__()
        self.scopes = []  # stack of sets, each set contains declared variable names

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
    
        option = 1
        
        if option == 1:
            
            if params_num > 2:
                params_num = 2
            
            node = CassNode(f"S#FS#{func_type}_{params_num}")
        
        else:
  
            node = CassNode(f"I#function_definition#{func_type}$$") #always 2 children: funct declarator and comp stmt
            node.add_child(CassNode("2"))
            
            if params_num == 0:
                x = "$()"
                num = 1
            else :
                x = "$$"
                num = 2
            node.add_child("I#function_declarator#" + f"{x}")
            node.add_child(CassNode(f"{num}"))
            node.add_child(CassNode(f"v{ctx.ID().getText()}"))
            node.add_child("-1") # never used before
            node.add_child("-1") # will never be used as a variable
            # Gather parameters
            if ctx.parameterList():
                params_node = self.visit(ctx.parameterList())
                node.add_child(params_node)        

    
        # Visit the compoundStatement
        block_node = self.visit(ctx.compoundStatement())
        node.add_child(block_node)

        self.parentNode = node.label

        return node

    def visitParameterList(self, ctx: CASSParser.ParameterListContext):
        #I#parameter_list#($)\t1\tI#parameter_declaration#int$\t1\tvc\t-1\t24\tI#compound_statement#
        num_params = len(ctx.parameter())
        dollar_signs = "$" * num_params
        node = CassNode(f'I#parameter_list#({dollar_signs})')
        node.add_child(CassNode(f"{num_params}"))
        for p in ctx.parameter():
            node.add_child(self.visit(p))
        return node

    def visitParameter(self, ctx: CASSParser.ParameterContext):
        # e.g. "int start_val"
        param_type = ctx.typeSpec().getText()
        param_name = ctx.ID().getText()
        node = CassNode(f"I#parameter_declaration#{param_type}$")
        node.add_child(CassNode("1"))
        node.add_child(CassNode(f"v{param_name}"))
        node.add_child(CassNode("-1"))
        node.add_child(CassNode("-1"))
        
        return CassNode(f"v:{param_name}")

    def visitCompoundStatement(self, ctx: CASSParser.CompoundStatementContext):
        # 1) Push a new empty set for local declarations in this block
        self.scopes.append(set())

        # Count the number of direct statements (children) in the compound statement
        num_children = len(ctx.statement())
        dollar_signs = "$" * num_children  # Create the correct number of $ placeholders
        block_node = CassNode(f"I#compound_statement#{{{dollar_signs}}}")
        block_node.add_child(CassNode(F"{num_children}"))
        block_node.is_in_comp_stmt = True

        # Add each statement as a direct child
        for st in ctx.statement():
            stmt_node = self.visit(st)
            #stmt_node.is_in_comp_stmt = True
            block_node.add_child(stmt_node)

        # 4) Pop the scope after leaving this block    
        self.scopes.pop()
        return block_node
    
    def visitIncludeStatement(self, ctx: CASSParser.IncludeStatementContext):
        return CassNode('removed')

    def visitDeclarationStatement(self, ctx: CASSParser.DeclarationStatementContext):

        # Mark this variable as local in the top scope
        var_name = ctx.ID().getText()
        if len(self.scopes) > 0:
            self.scopes[-1].add(var_name)
        
        type_label = ctx.typeSpec().getText()   # e.g. "int"
        decl_node = CassNode(f"I#declaration#{type_label}$;") ##intermediate nodes

        # e.g. "int sum = 0;"
        var_name = ctx.ID().getText()
        if ctx.expression():
            assign_node = CassNode("I#init_declarator#$=$")
            assign_node.add_child(CassNode(f"v{var_name}"))
            assign_node.prevUse = -1 # -> initial declaration so the node has not been used
            #assign_node.nextUse()

            # Visit the expression to see if it's #VAR or #LIT or something else
            value_node = self.visit(ctx.expression())
            assign_node.add_child(value_node)

            # Add `$=$` as the child of the `int$;` node
            decl_node.add_child(assign_node)
        else:
            # no initializer, just add #VAR as a child
            decl_node.add_child(CassNode(f"v{var_name}"))

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
        var_node = CassNode(f"v{var_name}")
        assign_node.add_child(var_node)

        # 4) The right side is the expression
        expr_node = self.visit(ctx.expression())  # this might yield #VAR:start_val, #LIT:0, etc.
        assign_node.add_child(expr_node)

        # Link everything: "int$;" -> "$=$"
        init_node.add_child(assign_node)

        return init_node



    def visitForBlockStatement(self, ctx: CASSParser.ForBlockStatementContext):
        num_children = len(ctx.statement())
        dollar_signs = "$" * num_children
        for_node = CassNode(f"#for_statement#for($$;$){dollar_signs}")
        for_node.add_child(CassNode(f"{num_children+3}"))

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
        for_node = CassNode("I#for_statement#for($$;$)$")
        for_node.add_child(CassNode("4"))

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
        while_node = CassNode("I#while_statement#while($;$)")

        # Condition
        cond_node = self.visit(ctx.expression())
        while_node.add_child(cond_node)

        # Body (multiple statements)
        for stmt_ctx in ctx.statement():
            stmt_node = self.visit(stmt_ctx)
            while_node.add_child(stmt_node)

        return while_node
    
    def visitWhileSingleStatement(self, ctx: CASSParser.WhileSingleStatementContext):
        while_node = CassNode("I#while_statement#while($;$)")

        # Condition
        cond_node = self.visit(ctx.expression())
        while_node.add_child(cond_node)

        # Single body statement
        body_node = self.visit(ctx.statement())
        while_node.add_child(body_node)

        return while_node
    
    def visitIfBlockStatement(self, ctx: CASSParser.IfBlockStatementContext):
        # Create a node for the "if" statement
        if_node = CassNode("I#if_statement#if($;$)")

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
        if_node = CassNode("I#if_statement#if($;$)")

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
            operator_node = CassNode(f"I#binary_expression#${operator}$")
            operator_node.add_child(CassNode("2"))
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
            operator_node = CassNode(f"I#binary_expression#${operator}$")
            operator_node.add_child(CassNode("2"))
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
    
    def visitFunctionCall(self, ctx: CASSParser.FunctionCallContext):
       
        # 1) The function name is the ID
        func_name = ctx.ID().getText()  # e.g. "init"

        # call_expression always has 2 children: name and parameter list
        call_node = CassNode("#call_expression#$$")

        # 3) First child = "F<funcName>", e.g. Finit
        func_node = CassNode(f"F{func_name}")
        call_node.add_child(func_node)

        # 4) Second child = the argument list (which might be empty)
        if ctx.argumentList():
            arg_list_node = self.visit(ctx.argumentList())
            call_node.add_child(arg_list_node)
        else:
            # No arguments => #argument_list#() with zero placeholders
            empty_args = CassNode("#argument_list#()")
            call_node.add_child(empty_args)

        return call_node


    def visitArgumentList(self, ctx: CASSParser.ArgumentListContext):
        """
        Grammar snippet:
            argumentList
                : expression (',' expression)*  # ArgumentList
                ;
        """
        # Count how many arguments we have
        num_args = len(ctx.expression())

        # Create a label like #argument_list#($$$...) with as many $ as arguments
        placeholders = ",".join(["$"] * num_args)  # Join $ with commas if more than one
        arg_list_node = CassNode(f"#argument_list#({placeholders})")
        arg_list_node.add_child(CassNode(f"{num_args}"))

        # For each expression argument, visit it and add as a child
        for expr_ctx in ctx.expression():
            arg_node = self.visit(expr_ctx)
            arg_list_node.add_child(arg_node)

        return arg_list_node
    

    def visitReturnStatement(self, ctx: CASSParser.ReturnStatementContext):
        # e.g. "return sum;"
        node = CassNode("#return_statement#return$;")
        if ctx.expression():
            expr_node = self.visit(ctx.expression())
            node.add_child(expr_node)
        return node

    def visitExpressionStatement(self, ctx: CASSParser.ExpressionStatementContext):

        statement_node = CassNode('#expression_statement#$')

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
        # Distinguish between:
        #   unaryExpression assignmentOperator assignmentExpression
        # vs
        #   logicalOrExpression

        if ctx.assignmentOperator():
            # e.g. b = b + 1
            op_text = ctx.assignmentOperator().getText()  # '=' or '+=' or ...
            
            # Use a node labeled #assignment_expression#$<op_text>
            # For a simple '=' you might produce '#assignment_expression#$=$'
            # For '+=' maybe '#assignment_expression#$+=$', etc.
            node = CassNode(f"#assignment_expression#$" + op_text + "$")

            lhs = self.visit(ctx.unaryExpression())  # e.g. b
            rhs = self.visit(ctx.assignmentExpression())  # e.g. b + 1

            node.add_child(lhs)
            node.add_child(rhs)
            return node
        else:
            # No assignment operator => just pass logicalOrExpression up
            return self.visit(ctx.logicalOrExpression())


    def visitUnaryExpression(self, ctx: CASSParser.UnaryExpressionContext):
        # e.g. ++i, primaryExpression, etc.
        text = ctx.getText()
        # If it's prefix like ++i
        if ctx.unaryExpression():
            # e.g. '++' unaryExpression
            # We'll produce a node for e.g. '++ #VAR'
            op = text[:2]  + "$" # '++' or '--'
            node = CassNode(f"#update_statement#{op}")
            var_text = ctx.unaryExpression().getText()
            node.add_child(CassNode(f"v{var_text}"))
            node.add_child("-1")
            node.add_child("-1")
            return node
        else:
            # We might have a primary expression
            return self.visit(ctx.primaryExpression())
        
    def isLocal(self, var_name: str) -> bool:
        # Search from the top of the stack downward
        for scope_set in reversed(self.scopes):
            if var_name in scope_set:
                return True
        return False

    def visitPrimaryExpression(self, ctx: CASSParser.PrimaryExpressionContext):
        # Case 1: It's an identifier
        if ctx.ID():
            var_text = ctx.ID().getText()

            # Check if var_text is declared in the current or any parent scope
            if self.isLocal(var_text):
                return CassNode(f"v{var_text}")
            else:
                # If not found in any scope, treat as global
                return CassNode(f"V{var_text}")

        
        # Case 2: It's an integer literal
        elif ctx.INT():
            lit_text = ctx.INT().getText()
            return CassNode(f"N{lit_text}")
        
        # Case 3: It's a float literal
        elif ctx.FLOAT():
            lit_text = ctx.FLOAT().getText()
            return CassNode(f"N{lit_text}")
        
        elif ctx.CHAR():
            lit_text = ctx.CHAR().getText()
            return CassNode(f"C{lit_text}")
        elif ctx.STRING():
            str_text = ctx.STRING().getText()
            return CassNode(f"S{str_text}")
        
        # Case 4: It's parentheses => ( expression )
        elif ctx.expression():
            # 1) Visit the sub-expression
            subexpr_node = self.visit(ctx.expression())

            # 2) Check if subexpr_node is an additive expression
            #    For example, if your additive visitor produces "$+$" or "$-$" as the label:
            if subexpr_node and subexpr_node.label in {"#binary_expression#$+$", "#binary_expression#$-$", "#binary_expression#$*$", "#binary_expression#$/$", "#binary_expression#$%$"}:
                # Create a paren node
                paren_node = CassNode("#parenthesized_expression#($)")
                paren_node.add_child(subexpr_node)
                return paren_node
            else:
                # If not additive, just return the inner expression without special wrapping
                return subexpr_node
            
        elif ctx.functionCall():
            return self.visit(ctx.functionCall())
        
        # Fallback if something unexpected
        else:
            return CassNode("???")

##addddd modulo digggaaqaa