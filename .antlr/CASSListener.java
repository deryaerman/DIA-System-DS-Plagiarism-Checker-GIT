// Generated from c:/Users/Maria/Downloads/DIA-System-DS-Plagiarism-Checker-GIT/CASS.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link CASSParser}.
 */
public interface CASSListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link CASSParser#prog}.
	 * @param ctx the parse tree
	 */
	void enterProg(CASSParser.ProgContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#prog}.
	 * @param ctx the parse tree
	 */
	void exitProg(CASSParser.ProgContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#functionDefinition}.
	 * @param ctx the parse tree
	 */
	void enterFunctionDefinition(CASSParser.FunctionDefinitionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#functionDefinition}.
	 * @param ctx the parse tree
	 */
	void exitFunctionDefinition(CASSParser.FunctionDefinitionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#compoundStatement}.
	 * @param ctx the parse tree
	 */
	void enterCompoundStatement(CASSParser.CompoundStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#compoundStatement}.
	 * @param ctx the parse tree
	 */
	void exitCompoundStatement(CASSParser.CompoundStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(CASSParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(CASSParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#declarationStatement}.
	 * @param ctx the parse tree
	 */
	void enterDeclarationStatement(CASSParser.DeclarationStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#declarationStatement}.
	 * @param ctx the parse tree
	 */
	void exitDeclarationStatement(CASSParser.DeclarationStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#forBlockStatement}.
	 * @param ctx the parse tree
	 */
	void enterForBlockStatement(CASSParser.ForBlockStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#forBlockStatement}.
	 * @param ctx the parse tree
	 */
	void exitForBlockStatement(CASSParser.ForBlockStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#forSingleStatement}.
	 * @param ctx the parse tree
	 */
	void enterForSingleStatement(CASSParser.ForSingleStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#forSingleStatement}.
	 * @param ctx the parse tree
	 */
	void exitForSingleStatement(CASSParser.ForSingleStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#conditionClause}.
	 * @param ctx the parse tree
	 */
	void enterConditionClause(CASSParser.ConditionClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#conditionClause}.
	 * @param ctx the parse tree
	 */
	void exitConditionClause(CASSParser.ConditionClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#whileBlockStatement}.
	 * @param ctx the parse tree
	 */
	void enterWhileBlockStatement(CASSParser.WhileBlockStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#whileBlockStatement}.
	 * @param ctx the parse tree
	 */
	void exitWhileBlockStatement(CASSParser.WhileBlockStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#whileSingleStatement}.
	 * @param ctx the parse tree
	 */
	void enterWhileSingleStatement(CASSParser.WhileSingleStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#whileSingleStatement}.
	 * @param ctx the parse tree
	 */
	void exitWhileSingleStatement(CASSParser.WhileSingleStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#ifBlockStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfBlockStatement(CASSParser.IfBlockStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#ifBlockStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfBlockStatement(CASSParser.IfBlockStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#ifSingleStatement}.
	 * @param ctx the parse tree
	 */
	void enterIfSingleStatement(CASSParser.IfSingleStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#ifSingleStatement}.
	 * @param ctx the parse tree
	 */
	void exitIfSingleStatement(CASSParser.IfSingleStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void enterFunctionCall(CASSParser.FunctionCallContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#functionCall}.
	 * @param ctx the parse tree
	 */
	void exitFunctionCall(CASSParser.FunctionCallContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#argumentList}.
	 * @param ctx the parse tree
	 */
	void enterArgumentList(CASSParser.ArgumentListContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#argumentList}.
	 * @param ctx the parse tree
	 */
	void exitArgumentList(CASSParser.ArgumentListContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void enterReturnStatement(CASSParser.ReturnStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#returnStatement}.
	 * @param ctx the parse tree
	 */
	void exitReturnStatement(CASSParser.ReturnStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#expressionStatement}.
	 * @param ctx the parse tree
	 */
	void enterExpressionStatement(CASSParser.ExpressionStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#expressionStatement}.
	 * @param ctx the parse tree
	 */
	void exitExpressionStatement(CASSParser.ExpressionStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#includeStatement}.
	 * @param ctx the parse tree
	 */
	void enterIncludeStatement(CASSParser.IncludeStatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#includeStatement}.
	 * @param ctx the parse tree
	 */
	void exitIncludeStatement(CASSParser.IncludeStatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#parameterList}.
	 * @param ctx the parse tree
	 */
	void enterParameterList(CASSParser.ParameterListContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#parameterList}.
	 * @param ctx the parse tree
	 */
	void exitParameterList(CASSParser.ParameterListContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#parameter}.
	 * @param ctx the parse tree
	 */
	void enterParameter(CASSParser.ParameterContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#parameter}.
	 * @param ctx the parse tree
	 */
	void exitParameter(CASSParser.ParameterContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#typeSpec}.
	 * @param ctx the parse tree
	 */
	void enterTypeSpec(CASSParser.TypeSpecContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#typeSpec}.
	 * @param ctx the parse tree
	 */
	void exitTypeSpec(CASSParser.TypeSpecContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#expression}.
	 * @param ctx the parse tree
	 */
	void enterExpression(CASSParser.ExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#expression}.
	 * @param ctx the parse tree
	 */
	void exitExpression(CASSParser.ExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#assignmentExpression}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentExpression(CASSParser.AssignmentExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#assignmentExpression}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentExpression(CASSParser.AssignmentExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#unaryExpression}.
	 * @param ctx the parse tree
	 */
	void enterUnaryExpression(CASSParser.UnaryExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#unaryExpression}.
	 * @param ctx the parse tree
	 */
	void exitUnaryExpression(CASSParser.UnaryExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#comparingExpression}.
	 * @param ctx the parse tree
	 */
	void enterComparingExpression(CASSParser.ComparingExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#comparingExpression}.
	 * @param ctx the parse tree
	 */
	void exitComparingExpression(CASSParser.ComparingExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#primaryExpression}.
	 * @param ctx the parse tree
	 */
	void enterPrimaryExpression(CASSParser.PrimaryExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#primaryExpression}.
	 * @param ctx the parse tree
	 */
	void exitPrimaryExpression(CASSParser.PrimaryExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#assignmentOperator}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentOperator(CASSParser.AssignmentOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#assignmentOperator}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentOperator(CASSParser.AssignmentOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#logicalOrExpression}.
	 * @param ctx the parse tree
	 */
	void enterLogicalOrExpression(CASSParser.LogicalOrExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#logicalOrExpression}.
	 * @param ctx the parse tree
	 */
	void exitLogicalOrExpression(CASSParser.LogicalOrExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#logicalAndExpression}.
	 * @param ctx the parse tree
	 */
	void enterLogicalAndExpression(CASSParser.LogicalAndExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#logicalAndExpression}.
	 * @param ctx the parse tree
	 */
	void exitLogicalAndExpression(CASSParser.LogicalAndExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#equalityExpression}.
	 * @param ctx the parse tree
	 */
	void enterEqualityExpression(CASSParser.EqualityExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#equalityExpression}.
	 * @param ctx the parse tree
	 */
	void exitEqualityExpression(CASSParser.EqualityExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#relationalExpression}.
	 * @param ctx the parse tree
	 */
	void enterRelationalExpression(CASSParser.RelationalExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#relationalExpression}.
	 * @param ctx the parse tree
	 */
	void exitRelationalExpression(CASSParser.RelationalExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#additiveExpression}.
	 * @param ctx the parse tree
	 */
	void enterAdditiveExpression(CASSParser.AdditiveExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#additiveExpression}.
	 * @param ctx the parse tree
	 */
	void exitAdditiveExpression(CASSParser.AdditiveExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#multiplicativeExpression}.
	 * @param ctx the parse tree
	 */
	void enterMultiplicativeExpression(CASSParser.MultiplicativeExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#multiplicativeExpression}.
	 * @param ctx the parse tree
	 */
	void exitMultiplicativeExpression(CASSParser.MultiplicativeExpressionContext ctx);
	/**
	 * Enter a parse tree produced by {@link CASSParser#operationExpression}.
	 * @param ctx the parse tree
	 */
	void enterOperationExpression(CASSParser.OperationExpressionContext ctx);
	/**
	 * Exit a parse tree produced by {@link CASSParser#operationExpression}.
	 * @param ctx the parse tree
	 */
	void exitOperationExpression(CASSParser.OperationExpressionContext ctx);
}