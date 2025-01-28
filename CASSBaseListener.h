
// Generated from CASS.g4 by ANTLR 4.13.2

#pragma once


#include "antlr4-runtime.h"
#include "CASSListener.h"


/**
 * This class provides an empty implementation of CASSListener,
 * which can be extended to create a listener which only needs to handle a subset
 * of the available methods.
 */
class  CASSBaseListener : public CASSListener {
public:

  virtual void enterProg(CASSParser::ProgContext * /*ctx*/) override { }
  virtual void exitProg(CASSParser::ProgContext * /*ctx*/) override { }

  virtual void enterFunctionDefinition(CASSParser::FunctionDefinitionContext * /*ctx*/) override { }
  virtual void exitFunctionDefinition(CASSParser::FunctionDefinitionContext * /*ctx*/) override { }

  virtual void enterCompoundStatement(CASSParser::CompoundStatementContext * /*ctx*/) override { }
  virtual void exitCompoundStatement(CASSParser::CompoundStatementContext * /*ctx*/) override { }

  virtual void enterStatement(CASSParser::StatementContext * /*ctx*/) override { }
  virtual void exitStatement(CASSParser::StatementContext * /*ctx*/) override { }

  virtual void enterDeclarationStatement(CASSParser::DeclarationStatementContext * /*ctx*/) override { }
  virtual void exitDeclarationStatement(CASSParser::DeclarationStatementContext * /*ctx*/) override { }

  virtual void enterForBlockStatement(CASSParser::ForBlockStatementContext * /*ctx*/) override { }
  virtual void exitForBlockStatement(CASSParser::ForBlockStatementContext * /*ctx*/) override { }

  virtual void enterForSingleStatement(CASSParser::ForSingleStatementContext * /*ctx*/) override { }
  virtual void exitForSingleStatement(CASSParser::ForSingleStatementContext * /*ctx*/) override { }

  virtual void enterForInit(CASSParser::ForInitContext * /*ctx*/) override { }
  virtual void exitForInit(CASSParser::ForInitContext * /*ctx*/) override { }

  virtual void enterForUpdate(CASSParser::ForUpdateContext * /*ctx*/) override { }
  virtual void exitForUpdate(CASSParser::ForUpdateContext * /*ctx*/) override { }

  virtual void enterWhileBlockStatement(CASSParser::WhileBlockStatementContext * /*ctx*/) override { }
  virtual void exitWhileBlockStatement(CASSParser::WhileBlockStatementContext * /*ctx*/) override { }

  virtual void enterWhileSingleStatement(CASSParser::WhileSingleStatementContext * /*ctx*/) override { }
  virtual void exitWhileSingleStatement(CASSParser::WhileSingleStatementContext * /*ctx*/) override { }

  virtual void enterIfBlockStatement(CASSParser::IfBlockStatementContext * /*ctx*/) override { }
  virtual void exitIfBlockStatement(CASSParser::IfBlockStatementContext * /*ctx*/) override { }

  virtual void enterIfSingleStatement(CASSParser::IfSingleStatementContext * /*ctx*/) override { }
  virtual void exitIfSingleStatement(CASSParser::IfSingleStatementContext * /*ctx*/) override { }

  virtual void enterFunctionCall(CASSParser::FunctionCallContext * /*ctx*/) override { }
  virtual void exitFunctionCall(CASSParser::FunctionCallContext * /*ctx*/) override { }

  virtual void enterArgumentList(CASSParser::ArgumentListContext * /*ctx*/) override { }
  virtual void exitArgumentList(CASSParser::ArgumentListContext * /*ctx*/) override { }

  virtual void enterReturnStatement(CASSParser::ReturnStatementContext * /*ctx*/) override { }
  virtual void exitReturnStatement(CASSParser::ReturnStatementContext * /*ctx*/) override { }

  virtual void enterExpressionStatement(CASSParser::ExpressionStatementContext * /*ctx*/) override { }
  virtual void exitExpressionStatement(CASSParser::ExpressionStatementContext * /*ctx*/) override { }

  virtual void enterIncludeStatement(CASSParser::IncludeStatementContext * /*ctx*/) override { }
  virtual void exitIncludeStatement(CASSParser::IncludeStatementContext * /*ctx*/) override { }

  virtual void enterParameterList(CASSParser::ParameterListContext * /*ctx*/) override { }
  virtual void exitParameterList(CASSParser::ParameterListContext * /*ctx*/) override { }

  virtual void enterParameter(CASSParser::ParameterContext * /*ctx*/) override { }
  virtual void exitParameter(CASSParser::ParameterContext * /*ctx*/) override { }

  virtual void enterTypeSpec(CASSParser::TypeSpecContext * /*ctx*/) override { }
  virtual void exitTypeSpec(CASSParser::TypeSpecContext * /*ctx*/) override { }

  virtual void enterExpression(CASSParser::ExpressionContext * /*ctx*/) override { }
  virtual void exitExpression(CASSParser::ExpressionContext * /*ctx*/) override { }

  virtual void enterAssignmentExpression(CASSParser::AssignmentExpressionContext * /*ctx*/) override { }
  virtual void exitAssignmentExpression(CASSParser::AssignmentExpressionContext * /*ctx*/) override { }

  virtual void enterUnaryExpression(CASSParser::UnaryExpressionContext * /*ctx*/) override { }
  virtual void exitUnaryExpression(CASSParser::UnaryExpressionContext * /*ctx*/) override { }

  virtual void enterPrimaryExpression(CASSParser::PrimaryExpressionContext * /*ctx*/) override { }
  virtual void exitPrimaryExpression(CASSParser::PrimaryExpressionContext * /*ctx*/) override { }

  virtual void enterAssignmentOperator(CASSParser::AssignmentOperatorContext * /*ctx*/) override { }
  virtual void exitAssignmentOperator(CASSParser::AssignmentOperatorContext * /*ctx*/) override { }

  virtual void enterLogicalOrExpression(CASSParser::LogicalOrExpressionContext * /*ctx*/) override { }
  virtual void exitLogicalOrExpression(CASSParser::LogicalOrExpressionContext * /*ctx*/) override { }

  virtual void enterLogicalAndExpression(CASSParser::LogicalAndExpressionContext * /*ctx*/) override { }
  virtual void exitLogicalAndExpression(CASSParser::LogicalAndExpressionContext * /*ctx*/) override { }

  virtual void enterEqualityExpression(CASSParser::EqualityExpressionContext * /*ctx*/) override { }
  virtual void exitEqualityExpression(CASSParser::EqualityExpressionContext * /*ctx*/) override { }

  virtual void enterRelationalExpression(CASSParser::RelationalExpressionContext * /*ctx*/) override { }
  virtual void exitRelationalExpression(CASSParser::RelationalExpressionContext * /*ctx*/) override { }

  virtual void enterAdditiveExpression(CASSParser::AdditiveExpressionContext * /*ctx*/) override { }
  virtual void exitAdditiveExpression(CASSParser::AdditiveExpressionContext * /*ctx*/) override { }

  virtual void enterMultiplicativeExpression(CASSParser::MultiplicativeExpressionContext * /*ctx*/) override { }
  virtual void exitMultiplicativeExpression(CASSParser::MultiplicativeExpressionContext * /*ctx*/) override { }

  virtual void enterOperationExpression(CASSParser::OperationExpressionContext * /*ctx*/) override { }
  virtual void exitOperationExpression(CASSParser::OperationExpressionContext * /*ctx*/) override { }


  virtual void enterEveryRule(antlr4::ParserRuleContext * /*ctx*/) override { }
  virtual void exitEveryRule(antlr4::ParserRuleContext * /*ctx*/) override { }
  virtual void visitTerminal(antlr4::tree::TerminalNode * /*node*/) override { }
  virtual void visitErrorNode(antlr4::tree::ErrorNode * /*node*/) override { }

};

