// Generated from CASS.g4 by ANTLR 4.13.2
import org.antlr.v4.runtime.tree.ParseTreeVisitor;

/**
 * This interface defines a complete generic visitor for a parse tree produced
 * by {@link CASSParser}.
 *
 * @param <T> The return type of the visit operation. Use {@link Void} for
 * operations with no return type.
 */
public interface CASSVisitor<T> extends ParseTreeVisitor<T> {
	/**
	 * Visit a parse tree produced by {@link CASSParser#prog}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitProg(CASSParser.ProgContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#functionDefinition}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunctionDefinition(CASSParser.FunctionDefinitionContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#compoundStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitCompoundStatement(CASSParser.CompoundStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#statement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitStatement(CASSParser.StatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#declarationStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitDeclarationStatement(CASSParser.DeclarationStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#forBlockStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitForBlockStatement(CASSParser.ForBlockStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#forSingleStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitForSingleStatement(CASSParser.ForSingleStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#forInit}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitForInit(CASSParser.ForInitContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#forUpdate}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitForUpdate(CASSParser.ForUpdateContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#whileBlockStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWhileBlockStatement(CASSParser.WhileBlockStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#whileSingleStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitWhileSingleStatement(CASSParser.WhileSingleStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#ifBlockStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIfBlockStatement(CASSParser.IfBlockStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#ifSingleStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIfSingleStatement(CASSParser.IfSingleStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#functionCall}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitFunctionCall(CASSParser.FunctionCallContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#argumentList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitArgumentList(CASSParser.ArgumentListContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#returnStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitReturnStatement(CASSParser.ReturnStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#expressionStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpressionStatement(CASSParser.ExpressionStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#includeStatement}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitIncludeStatement(CASSParser.IncludeStatementContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#parameterList}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParameterList(CASSParser.ParameterListContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#parameter}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitParameter(CASSParser.ParameterContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#typeSpec}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitTypeSpec(CASSParser.TypeSpecContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#expression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitExpression(CASSParser.ExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#assignmentExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssignmentExpression(CASSParser.AssignmentExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#unaryExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitUnaryExpression(CASSParser.UnaryExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#primaryExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitPrimaryExpression(CASSParser.PrimaryExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#assignmentOperator}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAssignmentOperator(CASSParser.AssignmentOperatorContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#logicalOrExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLogicalOrExpression(CASSParser.LogicalOrExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#logicalAndExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitLogicalAndExpression(CASSParser.LogicalAndExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#equalityExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitEqualityExpression(CASSParser.EqualityExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#relationalExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitRelationalExpression(CASSParser.RelationalExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#additiveExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitAdditiveExpression(CASSParser.AdditiveExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#multiplicativeExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitMultiplicativeExpression(CASSParser.MultiplicativeExpressionContext ctx);
	/**
	 * Visit a parse tree produced by {@link CASSParser#operationExpression}.
	 * @param ctx the parse tree
	 * @return the visitor result
	 */
	T visitOperationExpression(CASSParser.OperationExpressionContext ctx);
}