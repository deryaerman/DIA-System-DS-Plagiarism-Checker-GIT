
// Generated from CASS.g4 by ANTLR 4.13.2


#include "CASSListener.h"

#include "CASSParser.h"


using namespace antlrcpp;

using namespace antlr4;

namespace {

struct CASSParserStaticData final {
  CASSParserStaticData(std::vector<std::string> ruleNames,
                        std::vector<std::string> literalNames,
                        std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  CASSParserStaticData(const CASSParserStaticData&) = delete;
  CASSParserStaticData(CASSParserStaticData&&) = delete;
  CASSParserStaticData& operator=(const CASSParserStaticData&) = delete;
  CASSParserStaticData& operator=(CASSParserStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag cassParserOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
std::unique_ptr<CASSParserStaticData> cassParserStaticData = nullptr;

void cassParserInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (cassParserStaticData != nullptr) {
    return;
  }
#else
  assert(cassParserStaticData == nullptr);
#endif
  auto staticData = std::make_unique<CASSParserStaticData>(
    std::vector<std::string>{
      "prog", "functionDefinition", "compoundStatement", "statement", "declarationStatement", 
      "forStatement", "forInit", "forUpdate", "returnStatement", "expressionStatement", 
      "parameterList", "parameter", "typeSpec", "expression", "assignmentExpression", 
      "unaryExpression", "primaryExpression", "assignmentOperator", "logicalOrExpression", 
      "logicalAndExpression", "equalityExpression", "relationalExpression", 
      "additiveExpression", "multiplicativeExpression"
    },
    std::vector<std::string>{
      "", "'('", "')'", "'{'", "'}'", "'='", "';'", "'for'", "'return'", 
      "','", "'int'", "'++'", "'--'", "'+='", "'-='", "'*='", "'/='", "'||'", 
      "'&&'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'+'", "'-'", 
      "'*'", "'/'"
    },
    std::vector<std::string>{
      "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 
      "", "", "", "", "", "", "", "", "", "", "", "", "ID", "INT", "WS"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,31,207,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,
  	14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,7,20,2,21,7,
  	21,2,22,7,22,2,23,7,23,1,0,4,0,50,8,0,11,0,12,0,51,1,0,1,0,1,1,1,1,1,
  	1,1,1,3,1,60,8,1,1,1,1,1,1,1,1,2,1,2,5,2,67,8,2,10,2,12,2,70,9,2,1,2,
  	1,2,1,3,1,3,1,3,1,3,3,3,78,8,3,1,4,1,4,1,4,1,4,3,4,84,8,4,1,4,1,4,1,5,
  	1,5,1,5,3,5,91,8,5,1,5,1,5,3,5,95,8,5,1,5,1,5,3,5,99,8,5,1,5,1,5,1,5,
  	1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,3,8,113,8,8,1,8,1,8,1,9,1,9,1,9,1,
  	10,1,10,1,10,5,10,123,8,10,10,10,12,10,126,9,10,1,11,1,11,1,11,1,12,1,
  	12,1,13,1,13,1,14,1,14,1,14,1,14,1,14,3,14,140,8,14,1,15,1,15,1,15,1,
  	15,1,15,3,15,147,8,15,1,16,1,16,1,16,1,16,1,16,1,16,3,16,155,8,16,1,17,
  	1,17,1,18,1,18,1,18,5,18,162,8,18,10,18,12,18,165,9,18,1,19,1,19,1,19,
  	5,19,170,8,19,10,19,12,19,173,9,19,1,20,1,20,1,20,5,20,178,8,20,10,20,
  	12,20,181,9,20,1,21,1,21,1,21,5,21,186,8,21,10,21,12,21,189,9,21,1,22,
  	1,22,1,22,5,22,194,8,22,10,22,12,22,197,9,22,1,23,1,23,1,23,5,23,202,
  	8,23,10,23,12,23,205,9,23,1,23,0,0,24,0,2,4,6,8,10,12,14,16,18,20,22,
  	24,26,28,30,32,34,36,38,40,42,44,46,0,5,2,0,5,5,13,16,1,0,19,20,1,0,21,
  	24,1,0,25,26,1,0,27,28,205,0,49,1,0,0,0,2,55,1,0,0,0,4,64,1,0,0,0,6,77,
  	1,0,0,0,8,79,1,0,0,0,10,87,1,0,0,0,12,103,1,0,0,0,14,108,1,0,0,0,16,110,
  	1,0,0,0,18,116,1,0,0,0,20,119,1,0,0,0,22,127,1,0,0,0,24,130,1,0,0,0,26,
  	132,1,0,0,0,28,139,1,0,0,0,30,146,1,0,0,0,32,154,1,0,0,0,34,156,1,0,0,
  	0,36,158,1,0,0,0,38,166,1,0,0,0,40,174,1,0,0,0,42,182,1,0,0,0,44,190,
  	1,0,0,0,46,198,1,0,0,0,48,50,3,2,1,0,49,48,1,0,0,0,50,51,1,0,0,0,51,49,
  	1,0,0,0,51,52,1,0,0,0,52,53,1,0,0,0,53,54,5,0,0,1,54,1,1,0,0,0,55,56,
  	3,24,12,0,56,57,5,29,0,0,57,59,5,1,0,0,58,60,3,20,10,0,59,58,1,0,0,0,
  	59,60,1,0,0,0,60,61,1,0,0,0,61,62,5,2,0,0,62,63,3,4,2,0,63,3,1,0,0,0,
  	64,68,5,3,0,0,65,67,3,6,3,0,66,65,1,0,0,0,67,70,1,0,0,0,68,66,1,0,0,0,
  	68,69,1,0,0,0,69,71,1,0,0,0,70,68,1,0,0,0,71,72,5,4,0,0,72,5,1,0,0,0,
  	73,78,3,8,4,0,74,78,3,10,5,0,75,78,3,16,8,0,76,78,3,18,9,0,77,73,1,0,
  	0,0,77,74,1,0,0,0,77,75,1,0,0,0,77,76,1,0,0,0,78,7,1,0,0,0,79,80,3,24,
  	12,0,80,83,5,29,0,0,81,82,5,5,0,0,82,84,3,26,13,0,83,81,1,0,0,0,83,84,
  	1,0,0,0,84,85,1,0,0,0,85,86,5,6,0,0,86,9,1,0,0,0,87,88,5,7,0,0,88,90,
  	5,1,0,0,89,91,3,12,6,0,90,89,1,0,0,0,90,91,1,0,0,0,91,92,1,0,0,0,92,94,
  	5,6,0,0,93,95,3,26,13,0,94,93,1,0,0,0,94,95,1,0,0,0,95,96,1,0,0,0,96,
  	98,5,6,0,0,97,99,3,14,7,0,98,97,1,0,0,0,98,99,1,0,0,0,99,100,1,0,0,0,
  	100,101,5,2,0,0,101,102,3,6,3,0,102,11,1,0,0,0,103,104,3,24,12,0,104,
  	105,5,29,0,0,105,106,5,5,0,0,106,107,3,26,13,0,107,13,1,0,0,0,108,109,
  	3,30,15,0,109,15,1,0,0,0,110,112,5,8,0,0,111,113,3,26,13,0,112,111,1,
  	0,0,0,112,113,1,0,0,0,113,114,1,0,0,0,114,115,5,6,0,0,115,17,1,0,0,0,
  	116,117,3,26,13,0,117,118,5,6,0,0,118,19,1,0,0,0,119,124,3,22,11,0,120,
  	121,5,9,0,0,121,123,3,22,11,0,122,120,1,0,0,0,123,126,1,0,0,0,124,122,
  	1,0,0,0,124,125,1,0,0,0,125,21,1,0,0,0,126,124,1,0,0,0,127,128,3,24,12,
  	0,128,129,5,29,0,0,129,23,1,0,0,0,130,131,5,10,0,0,131,25,1,0,0,0,132,
  	133,3,28,14,0,133,27,1,0,0,0,134,135,3,30,15,0,135,136,3,34,17,0,136,
  	137,3,28,14,0,137,140,1,0,0,0,138,140,3,36,18,0,139,134,1,0,0,0,139,138,
  	1,0,0,0,140,29,1,0,0,0,141,142,5,11,0,0,142,147,3,30,15,0,143,144,5,12,
  	0,0,144,147,3,30,15,0,145,147,3,32,16,0,146,141,1,0,0,0,146,143,1,0,0,
  	0,146,145,1,0,0,0,147,31,1,0,0,0,148,155,5,29,0,0,149,155,5,30,0,0,150,
  	151,5,1,0,0,151,152,3,26,13,0,152,153,5,2,0,0,153,155,1,0,0,0,154,148,
  	1,0,0,0,154,149,1,0,0,0,154,150,1,0,0,0,155,33,1,0,0,0,156,157,7,0,0,
  	0,157,35,1,0,0,0,158,163,3,38,19,0,159,160,5,17,0,0,160,162,3,38,19,0,
  	161,159,1,0,0,0,162,165,1,0,0,0,163,161,1,0,0,0,163,164,1,0,0,0,164,37,
  	1,0,0,0,165,163,1,0,0,0,166,171,3,40,20,0,167,168,5,18,0,0,168,170,3,
  	40,20,0,169,167,1,0,0,0,170,173,1,0,0,0,171,169,1,0,0,0,171,172,1,0,0,
  	0,172,39,1,0,0,0,173,171,1,0,0,0,174,179,3,42,21,0,175,176,7,1,0,0,176,
  	178,3,42,21,0,177,175,1,0,0,0,178,181,1,0,0,0,179,177,1,0,0,0,179,180,
  	1,0,0,0,180,41,1,0,0,0,181,179,1,0,0,0,182,187,3,44,22,0,183,184,7,2,
  	0,0,184,186,3,44,22,0,185,183,1,0,0,0,186,189,1,0,0,0,187,185,1,0,0,0,
  	187,188,1,0,0,0,188,43,1,0,0,0,189,187,1,0,0,0,190,195,3,46,23,0,191,
  	192,7,3,0,0,192,194,3,46,23,0,193,191,1,0,0,0,194,197,1,0,0,0,195,193,
  	1,0,0,0,195,196,1,0,0,0,196,45,1,0,0,0,197,195,1,0,0,0,198,203,3,30,15,
  	0,199,200,7,4,0,0,200,202,3,30,15,0,201,199,1,0,0,0,202,205,1,0,0,0,203,
  	201,1,0,0,0,203,204,1,0,0,0,204,47,1,0,0,0,205,203,1,0,0,0,19,51,59,68,
  	77,83,90,94,98,112,124,139,146,154,163,171,179,187,195,203
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  cassParserStaticData = std::move(staticData);
}

}

CASSParser::CASSParser(TokenStream *input) : CASSParser(input, antlr4::atn::ParserATNSimulatorOptions()) {}

CASSParser::CASSParser(TokenStream *input, const antlr4::atn::ParserATNSimulatorOptions &options) : Parser(input) {
  CASSParser::initialize();
  _interpreter = new atn::ParserATNSimulator(this, *cassParserStaticData->atn, cassParserStaticData->decisionToDFA, cassParserStaticData->sharedContextCache, options);
}

CASSParser::~CASSParser() {
  delete _interpreter;
}

const atn::ATN& CASSParser::getATN() const {
  return *cassParserStaticData->atn;
}

std::string CASSParser::getGrammarFileName() const {
  return "CASS.g4";
}

const std::vector<std::string>& CASSParser::getRuleNames() const {
  return cassParserStaticData->ruleNames;
}

const dfa::Vocabulary& CASSParser::getVocabulary() const {
  return cassParserStaticData->vocabulary;
}

antlr4::atn::SerializedATNView CASSParser::getSerializedATN() const {
  return cassParserStaticData->serializedATN;
}


//----------------- ProgContext ------------------------------------------------------------------

CASSParser::ProgContext::ProgContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CASSParser::ProgContext::EOF() {
  return getToken(CASSParser::EOF, 0);
}

std::vector<CASSParser::FunctionDefinitionContext *> CASSParser::ProgContext::functionDefinition() {
  return getRuleContexts<CASSParser::FunctionDefinitionContext>();
}

CASSParser::FunctionDefinitionContext* CASSParser::ProgContext::functionDefinition(size_t i) {
  return getRuleContext<CASSParser::FunctionDefinitionContext>(i);
}


size_t CASSParser::ProgContext::getRuleIndex() const {
  return CASSParser::RuleProg;
}

void CASSParser::ProgContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterProg(this);
}

void CASSParser::ProgContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitProg(this);
}

CASSParser::ProgContext* CASSParser::prog() {
  ProgContext *_localctx = _tracker.createInstance<ProgContext>(_ctx, getState());
  enterRule(_localctx, 0, CASSParser::RuleProg);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(49); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(48);
      functionDefinition();
      setState(51); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while (_la == CASSParser::T__9);
    setState(53);
    match(CASSParser::EOF);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- FunctionDefinitionContext ------------------------------------------------------------------

CASSParser::FunctionDefinitionContext::FunctionDefinitionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CASSParser::TypeSpecContext* CASSParser::FunctionDefinitionContext::typeSpec() {
  return getRuleContext<CASSParser::TypeSpecContext>(0);
}

tree::TerminalNode* CASSParser::FunctionDefinitionContext::ID() {
  return getToken(CASSParser::ID, 0);
}

CASSParser::CompoundStatementContext* CASSParser::FunctionDefinitionContext::compoundStatement() {
  return getRuleContext<CASSParser::CompoundStatementContext>(0);
}

CASSParser::ParameterListContext* CASSParser::FunctionDefinitionContext::parameterList() {
  return getRuleContext<CASSParser::ParameterListContext>(0);
}


size_t CASSParser::FunctionDefinitionContext::getRuleIndex() const {
  return CASSParser::RuleFunctionDefinition;
}

void CASSParser::FunctionDefinitionContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterFunctionDefinition(this);
}

void CASSParser::FunctionDefinitionContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitFunctionDefinition(this);
}

CASSParser::FunctionDefinitionContext* CASSParser::functionDefinition() {
  FunctionDefinitionContext *_localctx = _tracker.createInstance<FunctionDefinitionContext>(_ctx, getState());
  enterRule(_localctx, 2, CASSParser::RuleFunctionDefinition);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(55);
    typeSpec();
    setState(56);
    match(CASSParser::ID);
    setState(57);
    match(CASSParser::T__0);
    setState(59);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CASSParser::T__9) {
      setState(58);
      parameterList();
    }
    setState(61);
    match(CASSParser::T__1);
    setState(62);
    compoundStatement();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- CompoundStatementContext ------------------------------------------------------------------

CASSParser::CompoundStatementContext::CompoundStatementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CASSParser::StatementContext *> CASSParser::CompoundStatementContext::statement() {
  return getRuleContexts<CASSParser::StatementContext>();
}

CASSParser::StatementContext* CASSParser::CompoundStatementContext::statement(size_t i) {
  return getRuleContext<CASSParser::StatementContext>(i);
}


size_t CASSParser::CompoundStatementContext::getRuleIndex() const {
  return CASSParser::RuleCompoundStatement;
}

void CASSParser::CompoundStatementContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterCompoundStatement(this);
}

void CASSParser::CompoundStatementContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitCompoundStatement(this);
}

CASSParser::CompoundStatementContext* CASSParser::compoundStatement() {
  CompoundStatementContext *_localctx = _tracker.createInstance<CompoundStatementContext>(_ctx, getState());
  enterRule(_localctx, 4, CASSParser::RuleCompoundStatement);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(64);
    match(CASSParser::T__2);
    setState(68);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 1610620290) != 0)) {
      setState(65);
      statement();
      setState(70);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(71);
    match(CASSParser::T__3);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- StatementContext ------------------------------------------------------------------

CASSParser::StatementContext::StatementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CASSParser::DeclarationStatementContext* CASSParser::StatementContext::declarationStatement() {
  return getRuleContext<CASSParser::DeclarationStatementContext>(0);
}

CASSParser::ForStatementContext* CASSParser::StatementContext::forStatement() {
  return getRuleContext<CASSParser::ForStatementContext>(0);
}

CASSParser::ReturnStatementContext* CASSParser::StatementContext::returnStatement() {
  return getRuleContext<CASSParser::ReturnStatementContext>(0);
}

CASSParser::ExpressionStatementContext* CASSParser::StatementContext::expressionStatement() {
  return getRuleContext<CASSParser::ExpressionStatementContext>(0);
}


size_t CASSParser::StatementContext::getRuleIndex() const {
  return CASSParser::RuleStatement;
}

void CASSParser::StatementContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterStatement(this);
}

void CASSParser::StatementContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitStatement(this);
}

CASSParser::StatementContext* CASSParser::statement() {
  StatementContext *_localctx = _tracker.createInstance<StatementContext>(_ctx, getState());
  enterRule(_localctx, 6, CASSParser::RuleStatement);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(77);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CASSParser::T__9: {
        enterOuterAlt(_localctx, 1);
        setState(73);
        declarationStatement();
        break;
      }

      case CASSParser::T__6: {
        enterOuterAlt(_localctx, 2);
        setState(74);
        forStatement();
        break;
      }

      case CASSParser::T__7: {
        enterOuterAlt(_localctx, 3);
        setState(75);
        returnStatement();
        break;
      }

      case CASSParser::T__0:
      case CASSParser::T__10:
      case CASSParser::T__11:
      case CASSParser::ID:
      case CASSParser::INT: {
        enterOuterAlt(_localctx, 4);
        setState(76);
        expressionStatement();
        break;
      }

    default:
      throw NoViableAltException(this);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- DeclarationStatementContext ------------------------------------------------------------------

CASSParser::DeclarationStatementContext::DeclarationStatementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CASSParser::TypeSpecContext* CASSParser::DeclarationStatementContext::typeSpec() {
  return getRuleContext<CASSParser::TypeSpecContext>(0);
}

tree::TerminalNode* CASSParser::DeclarationStatementContext::ID() {
  return getToken(CASSParser::ID, 0);
}

CASSParser::ExpressionContext* CASSParser::DeclarationStatementContext::expression() {
  return getRuleContext<CASSParser::ExpressionContext>(0);
}


size_t CASSParser::DeclarationStatementContext::getRuleIndex() const {
  return CASSParser::RuleDeclarationStatement;
}

void CASSParser::DeclarationStatementContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterDeclarationStatement(this);
}

void CASSParser::DeclarationStatementContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitDeclarationStatement(this);
}

CASSParser::DeclarationStatementContext* CASSParser::declarationStatement() {
  DeclarationStatementContext *_localctx = _tracker.createInstance<DeclarationStatementContext>(_ctx, getState());
  enterRule(_localctx, 8, CASSParser::RuleDeclarationStatement);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(79);
    typeSpec();
    setState(80);
    match(CASSParser::ID);
    setState(83);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CASSParser::T__4) {
      setState(81);
      match(CASSParser::T__4);
      setState(82);
      expression();
    }
    setState(85);
    match(CASSParser::T__5);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ForStatementContext ------------------------------------------------------------------

CASSParser::ForStatementContext::ForStatementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CASSParser::StatementContext* CASSParser::ForStatementContext::statement() {
  return getRuleContext<CASSParser::StatementContext>(0);
}

CASSParser::ForInitContext* CASSParser::ForStatementContext::forInit() {
  return getRuleContext<CASSParser::ForInitContext>(0);
}

CASSParser::ExpressionContext* CASSParser::ForStatementContext::expression() {
  return getRuleContext<CASSParser::ExpressionContext>(0);
}

CASSParser::ForUpdateContext* CASSParser::ForStatementContext::forUpdate() {
  return getRuleContext<CASSParser::ForUpdateContext>(0);
}


size_t CASSParser::ForStatementContext::getRuleIndex() const {
  return CASSParser::RuleForStatement;
}

void CASSParser::ForStatementContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterForStatement(this);
}

void CASSParser::ForStatementContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitForStatement(this);
}

CASSParser::ForStatementContext* CASSParser::forStatement() {
  ForStatementContext *_localctx = _tracker.createInstance<ForStatementContext>(_ctx, getState());
  enterRule(_localctx, 10, CASSParser::RuleForStatement);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(87);
    match(CASSParser::T__6);
    setState(88);
    match(CASSParser::T__0);
    setState(90);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CASSParser::T__9) {
      setState(89);
      forInit();
    }
    setState(92);
    match(CASSParser::T__5);
    setState(94);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 1610618882) != 0)) {
      setState(93);
      expression();
    }
    setState(96);
    match(CASSParser::T__5);
    setState(98);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 1610618882) != 0)) {
      setState(97);
      forUpdate();
    }
    setState(100);
    match(CASSParser::T__1);
    setState(101);
    statement();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ForInitContext ------------------------------------------------------------------

CASSParser::ForInitContext::ForInitContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CASSParser::TypeSpecContext* CASSParser::ForInitContext::typeSpec() {
  return getRuleContext<CASSParser::TypeSpecContext>(0);
}

tree::TerminalNode* CASSParser::ForInitContext::ID() {
  return getToken(CASSParser::ID, 0);
}

CASSParser::ExpressionContext* CASSParser::ForInitContext::expression() {
  return getRuleContext<CASSParser::ExpressionContext>(0);
}


size_t CASSParser::ForInitContext::getRuleIndex() const {
  return CASSParser::RuleForInit;
}

void CASSParser::ForInitContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterForInit(this);
}

void CASSParser::ForInitContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitForInit(this);
}

CASSParser::ForInitContext* CASSParser::forInit() {
  ForInitContext *_localctx = _tracker.createInstance<ForInitContext>(_ctx, getState());
  enterRule(_localctx, 12, CASSParser::RuleForInit);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(103);
    typeSpec();
    setState(104);
    match(CASSParser::ID);
    setState(105);
    match(CASSParser::T__4);
    setState(106);
    expression();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ForUpdateContext ------------------------------------------------------------------

CASSParser::ForUpdateContext::ForUpdateContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CASSParser::UnaryExpressionContext* CASSParser::ForUpdateContext::unaryExpression() {
  return getRuleContext<CASSParser::UnaryExpressionContext>(0);
}


size_t CASSParser::ForUpdateContext::getRuleIndex() const {
  return CASSParser::RuleForUpdate;
}

void CASSParser::ForUpdateContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterForUpdate(this);
}

void CASSParser::ForUpdateContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitForUpdate(this);
}

CASSParser::ForUpdateContext* CASSParser::forUpdate() {
  ForUpdateContext *_localctx = _tracker.createInstance<ForUpdateContext>(_ctx, getState());
  enterRule(_localctx, 14, CASSParser::RuleForUpdate);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(108);
    unaryExpression();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ReturnStatementContext ------------------------------------------------------------------

CASSParser::ReturnStatementContext::ReturnStatementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CASSParser::ExpressionContext* CASSParser::ReturnStatementContext::expression() {
  return getRuleContext<CASSParser::ExpressionContext>(0);
}


size_t CASSParser::ReturnStatementContext::getRuleIndex() const {
  return CASSParser::RuleReturnStatement;
}

void CASSParser::ReturnStatementContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterReturnStatement(this);
}

void CASSParser::ReturnStatementContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitReturnStatement(this);
}

CASSParser::ReturnStatementContext* CASSParser::returnStatement() {
  ReturnStatementContext *_localctx = _tracker.createInstance<ReturnStatementContext>(_ctx, getState());
  enterRule(_localctx, 16, CASSParser::RuleReturnStatement);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(110);
    match(CASSParser::T__7);
    setState(112);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 1610618882) != 0)) {
      setState(111);
      expression();
    }
    setState(114);
    match(CASSParser::T__5);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ExpressionStatementContext ------------------------------------------------------------------

CASSParser::ExpressionStatementContext::ExpressionStatementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CASSParser::ExpressionContext* CASSParser::ExpressionStatementContext::expression() {
  return getRuleContext<CASSParser::ExpressionContext>(0);
}


size_t CASSParser::ExpressionStatementContext::getRuleIndex() const {
  return CASSParser::RuleExpressionStatement;
}

void CASSParser::ExpressionStatementContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterExpressionStatement(this);
}

void CASSParser::ExpressionStatementContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitExpressionStatement(this);
}

CASSParser::ExpressionStatementContext* CASSParser::expressionStatement() {
  ExpressionStatementContext *_localctx = _tracker.createInstance<ExpressionStatementContext>(_ctx, getState());
  enterRule(_localctx, 18, CASSParser::RuleExpressionStatement);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(116);
    expression();
    setState(117);
    match(CASSParser::T__5);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ParameterListContext ------------------------------------------------------------------

CASSParser::ParameterListContext::ParameterListContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CASSParser::ParameterContext *> CASSParser::ParameterListContext::parameter() {
  return getRuleContexts<CASSParser::ParameterContext>();
}

CASSParser::ParameterContext* CASSParser::ParameterListContext::parameter(size_t i) {
  return getRuleContext<CASSParser::ParameterContext>(i);
}


size_t CASSParser::ParameterListContext::getRuleIndex() const {
  return CASSParser::RuleParameterList;
}

void CASSParser::ParameterListContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterParameterList(this);
}

void CASSParser::ParameterListContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitParameterList(this);
}

CASSParser::ParameterListContext* CASSParser::parameterList() {
  ParameterListContext *_localctx = _tracker.createInstance<ParameterListContext>(_ctx, getState());
  enterRule(_localctx, 20, CASSParser::RuleParameterList);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(119);
    parameter();
    setState(124);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CASSParser::T__8) {
      setState(120);
      match(CASSParser::T__8);
      setState(121);
      parameter();
      setState(126);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ParameterContext ------------------------------------------------------------------

CASSParser::ParameterContext::ParameterContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CASSParser::TypeSpecContext* CASSParser::ParameterContext::typeSpec() {
  return getRuleContext<CASSParser::TypeSpecContext>(0);
}

tree::TerminalNode* CASSParser::ParameterContext::ID() {
  return getToken(CASSParser::ID, 0);
}


size_t CASSParser::ParameterContext::getRuleIndex() const {
  return CASSParser::RuleParameter;
}

void CASSParser::ParameterContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterParameter(this);
}

void CASSParser::ParameterContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitParameter(this);
}

CASSParser::ParameterContext* CASSParser::parameter() {
  ParameterContext *_localctx = _tracker.createInstance<ParameterContext>(_ctx, getState());
  enterRule(_localctx, 22, CASSParser::RuleParameter);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(127);
    typeSpec();
    setState(128);
    match(CASSParser::ID);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- TypeSpecContext ------------------------------------------------------------------

CASSParser::TypeSpecContext::TypeSpecContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}


size_t CASSParser::TypeSpecContext::getRuleIndex() const {
  return CASSParser::RuleTypeSpec;
}

void CASSParser::TypeSpecContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterTypeSpec(this);
}

void CASSParser::TypeSpecContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitTypeSpec(this);
}

CASSParser::TypeSpecContext* CASSParser::typeSpec() {
  TypeSpecContext *_localctx = _tracker.createInstance<TypeSpecContext>(_ctx, getState());
  enterRule(_localctx, 24, CASSParser::RuleTypeSpec);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(130);
    match(CASSParser::T__9);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ExpressionContext ------------------------------------------------------------------

CASSParser::ExpressionContext::ExpressionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CASSParser::AssignmentExpressionContext* CASSParser::ExpressionContext::assignmentExpression() {
  return getRuleContext<CASSParser::AssignmentExpressionContext>(0);
}


size_t CASSParser::ExpressionContext::getRuleIndex() const {
  return CASSParser::RuleExpression;
}

void CASSParser::ExpressionContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterExpression(this);
}

void CASSParser::ExpressionContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitExpression(this);
}

CASSParser::ExpressionContext* CASSParser::expression() {
  ExpressionContext *_localctx = _tracker.createInstance<ExpressionContext>(_ctx, getState());
  enterRule(_localctx, 26, CASSParser::RuleExpression);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(132);
    assignmentExpression();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- AssignmentExpressionContext ------------------------------------------------------------------

CASSParser::AssignmentExpressionContext::AssignmentExpressionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CASSParser::UnaryExpressionContext* CASSParser::AssignmentExpressionContext::unaryExpression() {
  return getRuleContext<CASSParser::UnaryExpressionContext>(0);
}

CASSParser::AssignmentOperatorContext* CASSParser::AssignmentExpressionContext::assignmentOperator() {
  return getRuleContext<CASSParser::AssignmentOperatorContext>(0);
}

CASSParser::AssignmentExpressionContext* CASSParser::AssignmentExpressionContext::assignmentExpression() {
  return getRuleContext<CASSParser::AssignmentExpressionContext>(0);
}

CASSParser::LogicalOrExpressionContext* CASSParser::AssignmentExpressionContext::logicalOrExpression() {
  return getRuleContext<CASSParser::LogicalOrExpressionContext>(0);
}


size_t CASSParser::AssignmentExpressionContext::getRuleIndex() const {
  return CASSParser::RuleAssignmentExpression;
}

void CASSParser::AssignmentExpressionContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterAssignmentExpression(this);
}

void CASSParser::AssignmentExpressionContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitAssignmentExpression(this);
}

CASSParser::AssignmentExpressionContext* CASSParser::assignmentExpression() {
  AssignmentExpressionContext *_localctx = _tracker.createInstance<AssignmentExpressionContext>(_ctx, getState());
  enterRule(_localctx, 28, CASSParser::RuleAssignmentExpression);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(139);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 10, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(134);
      unaryExpression();
      setState(135);
      assignmentOperator();
      setState(136);
      assignmentExpression();
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(138);
      logicalOrExpression();
      break;
    }

    default:
      break;
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- UnaryExpressionContext ------------------------------------------------------------------

CASSParser::UnaryExpressionContext::UnaryExpressionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CASSParser::UnaryExpressionContext* CASSParser::UnaryExpressionContext::unaryExpression() {
  return getRuleContext<CASSParser::UnaryExpressionContext>(0);
}

CASSParser::PrimaryExpressionContext* CASSParser::UnaryExpressionContext::primaryExpression() {
  return getRuleContext<CASSParser::PrimaryExpressionContext>(0);
}


size_t CASSParser::UnaryExpressionContext::getRuleIndex() const {
  return CASSParser::RuleUnaryExpression;
}

void CASSParser::UnaryExpressionContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterUnaryExpression(this);
}

void CASSParser::UnaryExpressionContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitUnaryExpression(this);
}

CASSParser::UnaryExpressionContext* CASSParser::unaryExpression() {
  UnaryExpressionContext *_localctx = _tracker.createInstance<UnaryExpressionContext>(_ctx, getState());
  enterRule(_localctx, 30, CASSParser::RuleUnaryExpression);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(146);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CASSParser::T__10: {
        enterOuterAlt(_localctx, 1);
        setState(141);
        match(CASSParser::T__10);
        setState(142);
        unaryExpression();
        break;
      }

      case CASSParser::T__11: {
        enterOuterAlt(_localctx, 2);
        setState(143);
        match(CASSParser::T__11);
        setState(144);
        unaryExpression();
        break;
      }

      case CASSParser::T__0:
      case CASSParser::ID:
      case CASSParser::INT: {
        enterOuterAlt(_localctx, 3);
        setState(145);
        primaryExpression();
        break;
      }

    default:
      throw NoViableAltException(this);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- PrimaryExpressionContext ------------------------------------------------------------------

CASSParser::PrimaryExpressionContext::PrimaryExpressionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CASSParser::PrimaryExpressionContext::ID() {
  return getToken(CASSParser::ID, 0);
}

tree::TerminalNode* CASSParser::PrimaryExpressionContext::INT() {
  return getToken(CASSParser::INT, 0);
}

CASSParser::ExpressionContext* CASSParser::PrimaryExpressionContext::expression() {
  return getRuleContext<CASSParser::ExpressionContext>(0);
}


size_t CASSParser::PrimaryExpressionContext::getRuleIndex() const {
  return CASSParser::RulePrimaryExpression;
}

void CASSParser::PrimaryExpressionContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterPrimaryExpression(this);
}

void CASSParser::PrimaryExpressionContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitPrimaryExpression(this);
}

CASSParser::PrimaryExpressionContext* CASSParser::primaryExpression() {
  PrimaryExpressionContext *_localctx = _tracker.createInstance<PrimaryExpressionContext>(_ctx, getState());
  enterRule(_localctx, 32, CASSParser::RulePrimaryExpression);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(154);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CASSParser::ID: {
        enterOuterAlt(_localctx, 1);
        setState(148);
        match(CASSParser::ID);
        break;
      }

      case CASSParser::INT: {
        enterOuterAlt(_localctx, 2);
        setState(149);
        match(CASSParser::INT);
        break;
      }

      case CASSParser::T__0: {
        enterOuterAlt(_localctx, 3);
        setState(150);
        match(CASSParser::T__0);
        setState(151);
        expression();
        setState(152);
        match(CASSParser::T__1);
        break;
      }

    default:
      throw NoViableAltException(this);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- AssignmentOperatorContext ------------------------------------------------------------------

CASSParser::AssignmentOperatorContext::AssignmentOperatorContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}


size_t CASSParser::AssignmentOperatorContext::getRuleIndex() const {
  return CASSParser::RuleAssignmentOperator;
}

void CASSParser::AssignmentOperatorContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterAssignmentOperator(this);
}

void CASSParser::AssignmentOperatorContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitAssignmentOperator(this);
}

CASSParser::AssignmentOperatorContext* CASSParser::assignmentOperator() {
  AssignmentOperatorContext *_localctx = _tracker.createInstance<AssignmentOperatorContext>(_ctx, getState());
  enterRule(_localctx, 34, CASSParser::RuleAssignmentOperator);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(156);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 122912) != 0))) {
    _errHandler->recoverInline(this);
    }
    else {
      _errHandler->reportMatch(this);
      consume();
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- LogicalOrExpressionContext ------------------------------------------------------------------

CASSParser::LogicalOrExpressionContext::LogicalOrExpressionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CASSParser::LogicalAndExpressionContext *> CASSParser::LogicalOrExpressionContext::logicalAndExpression() {
  return getRuleContexts<CASSParser::LogicalAndExpressionContext>();
}

CASSParser::LogicalAndExpressionContext* CASSParser::LogicalOrExpressionContext::logicalAndExpression(size_t i) {
  return getRuleContext<CASSParser::LogicalAndExpressionContext>(i);
}


size_t CASSParser::LogicalOrExpressionContext::getRuleIndex() const {
  return CASSParser::RuleLogicalOrExpression;
}

void CASSParser::LogicalOrExpressionContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterLogicalOrExpression(this);
}

void CASSParser::LogicalOrExpressionContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitLogicalOrExpression(this);
}

CASSParser::LogicalOrExpressionContext* CASSParser::logicalOrExpression() {
  LogicalOrExpressionContext *_localctx = _tracker.createInstance<LogicalOrExpressionContext>(_ctx, getState());
  enterRule(_localctx, 36, CASSParser::RuleLogicalOrExpression);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(158);
    logicalAndExpression();
    setState(163);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CASSParser::T__16) {
      setState(159);
      match(CASSParser::T__16);
      setState(160);
      logicalAndExpression();
      setState(165);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- LogicalAndExpressionContext ------------------------------------------------------------------

CASSParser::LogicalAndExpressionContext::LogicalAndExpressionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CASSParser::EqualityExpressionContext *> CASSParser::LogicalAndExpressionContext::equalityExpression() {
  return getRuleContexts<CASSParser::EqualityExpressionContext>();
}

CASSParser::EqualityExpressionContext* CASSParser::LogicalAndExpressionContext::equalityExpression(size_t i) {
  return getRuleContext<CASSParser::EqualityExpressionContext>(i);
}


size_t CASSParser::LogicalAndExpressionContext::getRuleIndex() const {
  return CASSParser::RuleLogicalAndExpression;
}

void CASSParser::LogicalAndExpressionContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterLogicalAndExpression(this);
}

void CASSParser::LogicalAndExpressionContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitLogicalAndExpression(this);
}

CASSParser::LogicalAndExpressionContext* CASSParser::logicalAndExpression() {
  LogicalAndExpressionContext *_localctx = _tracker.createInstance<LogicalAndExpressionContext>(_ctx, getState());
  enterRule(_localctx, 38, CASSParser::RuleLogicalAndExpression);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(166);
    equalityExpression();
    setState(171);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CASSParser::T__17) {
      setState(167);
      match(CASSParser::T__17);
      setState(168);
      equalityExpression();
      setState(173);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- EqualityExpressionContext ------------------------------------------------------------------

CASSParser::EqualityExpressionContext::EqualityExpressionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CASSParser::RelationalExpressionContext *> CASSParser::EqualityExpressionContext::relationalExpression() {
  return getRuleContexts<CASSParser::RelationalExpressionContext>();
}

CASSParser::RelationalExpressionContext* CASSParser::EqualityExpressionContext::relationalExpression(size_t i) {
  return getRuleContext<CASSParser::RelationalExpressionContext>(i);
}


size_t CASSParser::EqualityExpressionContext::getRuleIndex() const {
  return CASSParser::RuleEqualityExpression;
}

void CASSParser::EqualityExpressionContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterEqualityExpression(this);
}

void CASSParser::EqualityExpressionContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitEqualityExpression(this);
}

CASSParser::EqualityExpressionContext* CASSParser::equalityExpression() {
  EqualityExpressionContext *_localctx = _tracker.createInstance<EqualityExpressionContext>(_ctx, getState());
  enterRule(_localctx, 40, CASSParser::RuleEqualityExpression);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(174);
    relationalExpression();
    setState(179);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CASSParser::T__18

    || _la == CASSParser::T__19) {
      setState(175);
      _la = _input->LA(1);
      if (!(_la == CASSParser::T__18

      || _la == CASSParser::T__19)) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
      setState(176);
      relationalExpression();
      setState(181);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- RelationalExpressionContext ------------------------------------------------------------------

CASSParser::RelationalExpressionContext::RelationalExpressionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CASSParser::AdditiveExpressionContext *> CASSParser::RelationalExpressionContext::additiveExpression() {
  return getRuleContexts<CASSParser::AdditiveExpressionContext>();
}

CASSParser::AdditiveExpressionContext* CASSParser::RelationalExpressionContext::additiveExpression(size_t i) {
  return getRuleContext<CASSParser::AdditiveExpressionContext>(i);
}


size_t CASSParser::RelationalExpressionContext::getRuleIndex() const {
  return CASSParser::RuleRelationalExpression;
}

void CASSParser::RelationalExpressionContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterRelationalExpression(this);
}

void CASSParser::RelationalExpressionContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitRelationalExpression(this);
}

CASSParser::RelationalExpressionContext* CASSParser::relationalExpression() {
  RelationalExpressionContext *_localctx = _tracker.createInstance<RelationalExpressionContext>(_ctx, getState());
  enterRule(_localctx, 42, CASSParser::RuleRelationalExpression);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(182);
    additiveExpression();
    setState(187);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 31457280) != 0)) {
      setState(183);
      _la = _input->LA(1);
      if (!((((_la & ~ 0x3fULL) == 0) &&
        ((1ULL << _la) & 31457280) != 0))) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
      setState(184);
      additiveExpression();
      setState(189);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- AdditiveExpressionContext ------------------------------------------------------------------

CASSParser::AdditiveExpressionContext::AdditiveExpressionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CASSParser::MultiplicativeExpressionContext *> CASSParser::AdditiveExpressionContext::multiplicativeExpression() {
  return getRuleContexts<CASSParser::MultiplicativeExpressionContext>();
}

CASSParser::MultiplicativeExpressionContext* CASSParser::AdditiveExpressionContext::multiplicativeExpression(size_t i) {
  return getRuleContext<CASSParser::MultiplicativeExpressionContext>(i);
}


size_t CASSParser::AdditiveExpressionContext::getRuleIndex() const {
  return CASSParser::RuleAdditiveExpression;
}

void CASSParser::AdditiveExpressionContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterAdditiveExpression(this);
}

void CASSParser::AdditiveExpressionContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitAdditiveExpression(this);
}

CASSParser::AdditiveExpressionContext* CASSParser::additiveExpression() {
  AdditiveExpressionContext *_localctx = _tracker.createInstance<AdditiveExpressionContext>(_ctx, getState());
  enterRule(_localctx, 44, CASSParser::RuleAdditiveExpression);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(190);
    multiplicativeExpression();
    setState(195);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CASSParser::T__24

    || _la == CASSParser::T__25) {
      setState(191);
      _la = _input->LA(1);
      if (!(_la == CASSParser::T__24

      || _la == CASSParser::T__25)) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
      setState(192);
      multiplicativeExpression();
      setState(197);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- MultiplicativeExpressionContext ------------------------------------------------------------------

CASSParser::MultiplicativeExpressionContext::MultiplicativeExpressionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CASSParser::UnaryExpressionContext *> CASSParser::MultiplicativeExpressionContext::unaryExpression() {
  return getRuleContexts<CASSParser::UnaryExpressionContext>();
}

CASSParser::UnaryExpressionContext* CASSParser::MultiplicativeExpressionContext::unaryExpression(size_t i) {
  return getRuleContext<CASSParser::UnaryExpressionContext>(i);
}


size_t CASSParser::MultiplicativeExpressionContext::getRuleIndex() const {
  return CASSParser::RuleMultiplicativeExpression;
}

void CASSParser::MultiplicativeExpressionContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterMultiplicativeExpression(this);
}

void CASSParser::MultiplicativeExpressionContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitMultiplicativeExpression(this);
}

CASSParser::MultiplicativeExpressionContext* CASSParser::multiplicativeExpression() {
  MultiplicativeExpressionContext *_localctx = _tracker.createInstance<MultiplicativeExpressionContext>(_ctx, getState());
  enterRule(_localctx, 46, CASSParser::RuleMultiplicativeExpression);
  size_t _la = 0;

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(198);
    unaryExpression();
    setState(203);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CASSParser::T__26

    || _la == CASSParser::T__27) {
      setState(199);
      _la = _input->LA(1);
      if (!(_la == CASSParser::T__26

      || _la == CASSParser::T__27)) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
      setState(200);
      unaryExpression();
      setState(205);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

void CASSParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  cassParserInitialize();
#else
  ::antlr4::internal::call_once(cassParserOnceFlag, cassParserInitialize);
#endif
}
