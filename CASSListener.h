
// Generated from CASS.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "CASSParser.h"


/**
 * This interface defines an abstract listener for a parse tree produced by CASSParser.
 */
class  CASSListener : public antlr4::tree::ParseTreeListener {
public:

  virtual void enterProg(CASSParser::ProgContext *ctx) = 0;
  virtual void exitProg(CASSParser::ProgContext *ctx) = 0;

  virtual void enterFunctionDefinition(CASSParser::FunctionDefinitionContext *ctx) = 0;
  virtual void exitFunctionDefinition(CASSParser::FunctionDefinitionContext *ctx) = 0;

  virtual void enterCompoundStatement(CASSParser::CompoundStatementContext *ctx) = 0;
  virtual void exitCompoundStatement(CASSParser::CompoundStatementContext *ctx) = 0;

  virtual void enterStatement(CASSParser::StatementContext *ctx) = 0;
  virtual void exitStatement(CASSParser::StatementContext *ctx) = 0;

  virtual void enterDeclarationStatement(CASSParser::DeclarationStatementContext *ctx) = 0;
  virtual void exitDeclarationStatement(CASSParser::DeclarationStatementContext *ctx) = 0;

  virtual void enterForStatement(CASSParser::ForStatementContext *ctx) = 0;
  virtual void exitForStatement(CASSParser::ForStatementContext *ctx) = 0;

  virtual void enterForInit(CASSParser::ForInitContext *ctx) = 0;
  virtual void exitForInit(CASSParser::ForInitContext *ctx) = 0;

  virtual void enterForUpdate(CASSParser::ForUpdateContext *ctx) = 0;
  virtual void exitForUpdate(CASSParser::ForUpdateContext *ctx) = 0;

  virtual void enterReturnStatement(CASSParser::ReturnStatementContext *ctx) = 0;
  virtual void exitReturnStatement(CASSParser::ReturnStatementContext *ctx) = 0;

  virtual void enterExpressionStatement(CASSParser::ExpressionStatementContext *ctx) = 0;
  virtual void exitExpressionStatement(CASSParser::ExpressionStatementContext *ctx) = 0;

  virtual void enterParameterList(CASSParser::ParameterListContext *ctx) = 0;
  virtual void exitParameterList(CASSParser::ParameterListContext *ctx) = 0;

  virtual void enterParameter(CASSParser::ParameterContext *ctx) = 0;
  virtual void exitParameter(CASSParser::ParameterContext *ctx) = 0;

  virtual void enterTypeSpec(CASSParser::TypeSpecContext *ctx) = 0;
  virtual void exitTypeSpec(CASSParser::TypeSpecContext *ctx) = 0;

  virtual void enterExpression(CASSParser::ExpressionContext *ctx) = 0;
  virtual void exitExpression(CASSParser::ExpressionContext *ctx) = 0;

  virtual void enterAssignmentExpression(CASSParser::AssignmentExpressionContext *ctx) = 0;
  virtual void exitAssignmentExpression(CASSParser::AssignmentExpressionContext *ctx) = 0;

  virtual void enterUnaryExpression(CASSParser::UnaryExpressionContext *ctx) = 0;
  virtual void exitUnaryExpression(CASSParser::UnaryExpressionContext *ctx) = 0;

  virtual void enterPrimaryExpression(CASSParser::PrimaryExpressionContext *ctx) = 0;
  virtual void exitPrimaryExpression(CASSParser::PrimaryExpressionContext *ctx) = 0;

  virtual void enterAssignmentOperator(CASSParser::AssignmentOperatorContext *ctx) = 0;
  virtual void exitAssignmentOperator(CASSParser::AssignmentOperatorContext *ctx) = 0;

  virtual void enterLogicalOrExpression(CASSParser::LogicalOrExpressionContext *ctx) = 0;
  virtual void exitLogicalOrExpression(CASSParser::LogicalOrExpressionContext *ctx) = 0;

  virtual void enterLogicalAndExpression(CASSParser::LogicalAndExpressionContext *ctx) = 0;
  virtual void exitLogicalAndExpression(CASSParser::LogicalAndExpressionContext *ctx) = 0;

  virtual void enterEqualityExpression(CASSParser::EqualityExpressionContext *ctx) = 0;
  virtual void exitEqualityExpression(CASSParser::EqualityExpressionContext *ctx) = 0;

  virtual void enterRelationalExpression(CASSParser::RelationalExpressionContext *ctx) = 0;
  virtual void exitRelationalExpression(CASSParser::RelationalExpressionContext *ctx) = 0;

  virtual void enterAdditiveExpression(CASSParser::AdditiveExpressionContext *ctx) = 0;
  virtual void exitAdditiveExpression(CASSParser::AdditiveExpressionContext *ctx) = 0;

  virtual void enterMultiplicativeExpression(CASSParser::MultiplicativeExpressionContext *ctx) = 0;
  virtual void exitMultiplicativeExpression(CASSParser::MultiplicativeExpressionContext *ctx) = 0;


};

