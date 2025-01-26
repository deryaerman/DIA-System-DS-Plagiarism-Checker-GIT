# Generated from CASS.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .CASSParser import CASSParser
else:
    from CASSParser import CASSParser

# This class defines a complete generic visitor for a parse tree produced by CASSParser.

class CASSVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CASSParser#prog.
    def visitProg(self, ctx:CASSParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CASSParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:CASSParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CASSParser#compoundStatement.
    def visitCompoundStatement(self, ctx:CASSParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CASSParser#statement.
    def visitStatement(self, ctx:CASSParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CASSParser#declarationStatement.
    def visitDeclarationStatement(self, ctx:CASSParser.DeclarationStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CASSParser#forBlockStatement.
    def visitForBlockStatement(self, ctx:CASSParser.ForBlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CASSParser#forSingleStatement.
    def visitForSingleStatement(self, ctx:CASSParser.ForSingleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CASSParser#forInit.
    def visitForInit(self, ctx:CASSParser.ForInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CASSParser#forUpdate.
    def visitForUpdate(self, ctx:CASSParser.ForUpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CASSParser#whileBlockStatement.
    def visitWhileBlockStatement(self, ctx:CASSParser.WhileBlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CASSParser#whileSingleStatement.
    def visitWhileSingleStatement(self, ctx:CASSParser.WhileSingleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CASSParser#ifBlockStatement.
    def visitIfBlockStatement(self, ctx:CASSParser.IfBlockStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CASSParser#ifSingleStatement.
    def visitIfSingleStatement(self, ctx:CASSParser.IfSingleStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CASSParser#returnStatement.
    def visitReturnStatement(self, ctx:CASSParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CASSParser#expressionStatement.
    def visitExpressionStatement(self, ctx:CASSParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CASSParser#parameterList.
    def visitParameterList(self, ctx:CASSParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CASSParser#parameter.
    def visitParameter(self, ctx:CASSParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CASSParser#typeSpec.
    def visitTypeSpec(self, ctx:CASSParser.TypeSpecContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CASSParser#expression.
    def visitExpression(self, ctx:CASSParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CASSParser#assignmentExpression.
    def visitAssignmentExpression(self, ctx:CASSParser.AssignmentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CASSParser#unaryExpression.
    def visitUnaryExpression(self, ctx:CASSParser.UnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CASSParser#primaryExpression.
    def visitPrimaryExpression(self, ctx:CASSParser.PrimaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CASSParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:CASSParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CASSParser#logicalOrExpression.
    def visitLogicalOrExpression(self, ctx:CASSParser.LogicalOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CASSParser#logicalAndExpression.
    def visitLogicalAndExpression(self, ctx:CASSParser.LogicalAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CASSParser#equalityExpression.
    def visitEqualityExpression(self, ctx:CASSParser.EqualityExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CASSParser#relationalExpression.
    def visitRelationalExpression(self, ctx:CASSParser.RelationalExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CASSParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:CASSParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CASSParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:CASSParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)



del CASSParser