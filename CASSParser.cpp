
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
      "forBlockStatement", "forSingleStatement", "forInit", "forUpdate", 
      "whileBlockStatement", "whileSingleStatement", "ifBlockStatement", 
      "ifSingleStatement", "functionCall", "argumentList", "returnStatement", 
      "expressionStatement", "parameterList", "parameter", "typeSpec", "expression", 
      "assignmentExpression", "unaryExpression", "primaryExpression", "assignmentOperator", 
      "logicalOrExpression", "logicalAndExpression", "equalityExpression", 
      "relationalExpression", "additiveExpression", "multiplicativeExpression", 
      "operationExpression"
    },
    std::vector<std::string>{
      "", "'('", "')'", "'{'", "'}'", "'='", "';'", "'for'", "'while'", 
      "'if'", "'else'", "','", "'return'", "'int'", "'float'", "'double'", 
      "'++'", "'--'", "'+='", "'-='", "'*='", "'/='", "'||'", "'&&'", "'=='", 
      "'!='", "'<'", "'>'", "'<='", "'>='", "'+'", "'-'", "'*'", "'/'"
    },
    std::vector<std::string>{
      "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 
      "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 
      "SL_COMMENT", "ML_COMMENT", "ID", "INT", "FLOAT", "CHAR", "STRING", 
      "WS"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,41,326,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,
  	14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,7,20,2,21,7,
  	21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,2,27,7,27,2,28,7,
  	28,2,29,7,29,2,30,7,30,2,31,7,31,1,0,4,0,66,8,0,11,0,12,0,67,1,0,1,0,
  	1,1,1,1,1,1,1,1,3,1,76,8,1,1,1,1,1,1,1,1,2,1,2,5,2,83,8,2,10,2,12,2,86,
  	9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,100,8,3,1,4,1,
  	4,1,4,1,4,3,4,106,8,4,1,4,1,4,1,5,1,5,1,5,3,5,113,8,5,1,5,1,5,3,5,117,
  	8,5,1,5,1,5,3,5,121,8,5,1,5,1,5,1,5,5,5,126,8,5,10,5,12,5,129,9,5,1,5,
  	1,5,1,6,1,6,1,6,3,6,136,8,6,1,6,1,6,3,6,140,8,6,1,6,1,6,3,6,144,8,6,1,
  	6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,162,
  	8,9,10,9,12,9,165,9,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,
  	1,11,1,11,1,11,1,11,5,11,181,8,11,10,11,12,11,184,9,11,1,11,1,11,1,11,
  	1,11,5,11,190,8,11,10,11,12,11,193,9,11,1,11,3,11,196,8,11,1,12,1,12,
  	1,12,1,12,1,12,1,12,1,12,3,12,205,8,12,1,13,1,13,1,13,3,13,210,8,13,1,
  	13,1,13,1,14,1,14,1,14,5,14,217,8,14,10,14,12,14,220,9,14,1,15,1,15,3,
  	15,224,8,15,1,15,1,15,1,16,1,16,1,16,1,17,1,17,1,17,5,17,234,8,17,10,
  	17,12,17,237,9,17,1,18,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,21,1,
  	21,1,21,3,21,251,8,21,1,22,1,22,1,22,1,22,1,22,3,22,258,8,22,1,23,1,23,
  	1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,270,8,23,1,24,1,24,1,25,
  	1,25,1,25,5,25,277,8,25,10,25,12,25,280,9,25,1,26,1,26,1,26,5,26,285,
  	8,26,10,26,12,26,288,9,26,1,27,1,27,1,27,5,27,293,8,27,10,27,12,27,296,
  	9,27,1,28,1,28,1,28,5,28,301,8,28,10,28,12,28,304,9,28,1,29,1,29,1,29,
  	5,29,309,8,29,10,29,12,29,312,9,29,1,30,1,30,1,30,5,30,317,8,30,10,30,
  	12,30,320,9,30,1,31,1,31,3,31,324,8,31,1,31,0,0,32,0,2,4,6,8,10,12,14,
  	16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,
  	62,0,6,1,0,13,15,2,0,5,5,18,21,1,0,24,25,1,0,26,29,1,0,30,31,1,0,32,33,
  	338,0,65,1,0,0,0,2,71,1,0,0,0,4,80,1,0,0,0,6,99,1,0,0,0,8,101,1,0,0,0,
  	10,109,1,0,0,0,12,132,1,0,0,0,14,148,1,0,0,0,16,153,1,0,0,0,18,155,1,
  	0,0,0,20,168,1,0,0,0,22,174,1,0,0,0,24,197,1,0,0,0,26,206,1,0,0,0,28,
  	213,1,0,0,0,30,221,1,0,0,0,32,227,1,0,0,0,34,230,1,0,0,0,36,238,1,0,0,
  	0,38,241,1,0,0,0,40,243,1,0,0,0,42,250,1,0,0,0,44,257,1,0,0,0,46,269,
  	1,0,0,0,48,271,1,0,0,0,50,273,1,0,0,0,52,281,1,0,0,0,54,289,1,0,0,0,56,
  	297,1,0,0,0,58,305,1,0,0,0,60,313,1,0,0,0,62,323,1,0,0,0,64,66,3,6,3,
  	0,65,64,1,0,0,0,66,67,1,0,0,0,67,65,1,0,0,0,67,68,1,0,0,0,68,69,1,0,0,
  	0,69,70,5,0,0,1,70,1,1,0,0,0,71,72,3,38,19,0,72,73,5,36,0,0,73,75,5,1,
  	0,0,74,76,3,34,17,0,75,74,1,0,0,0,75,76,1,0,0,0,76,77,1,0,0,0,77,78,5,
  	2,0,0,78,79,3,4,2,0,79,3,1,0,0,0,80,84,5,3,0,0,81,83,3,6,3,0,82,81,1,
  	0,0,0,83,86,1,0,0,0,84,82,1,0,0,0,84,85,1,0,0,0,85,87,1,0,0,0,86,84,1,
  	0,0,0,87,88,5,4,0,0,88,5,1,0,0,0,89,100,3,8,4,0,90,100,3,10,5,0,91,100,
  	3,12,6,0,92,100,3,18,9,0,93,100,3,20,10,0,94,100,3,22,11,0,95,100,3,24,
  	12,0,96,100,3,30,15,0,97,100,3,32,16,0,98,100,3,2,1,0,99,89,1,0,0,0,99,
  	90,1,0,0,0,99,91,1,0,0,0,99,92,1,0,0,0,99,93,1,0,0,0,99,94,1,0,0,0,99,
  	95,1,0,0,0,99,96,1,0,0,0,99,97,1,0,0,0,99,98,1,0,0,0,100,7,1,0,0,0,101,
  	102,3,38,19,0,102,105,5,36,0,0,103,104,5,5,0,0,104,106,3,40,20,0,105,
  	103,1,0,0,0,105,106,1,0,0,0,106,107,1,0,0,0,107,108,5,6,0,0,108,9,1,0,
  	0,0,109,110,5,7,0,0,110,112,5,1,0,0,111,113,3,14,7,0,112,111,1,0,0,0,
  	112,113,1,0,0,0,113,114,1,0,0,0,114,116,5,6,0,0,115,117,3,40,20,0,116,
  	115,1,0,0,0,116,117,1,0,0,0,117,118,1,0,0,0,118,120,5,6,0,0,119,121,3,
  	16,8,0,120,119,1,0,0,0,120,121,1,0,0,0,121,122,1,0,0,0,122,123,5,2,0,
  	0,123,127,5,3,0,0,124,126,3,6,3,0,125,124,1,0,0,0,126,129,1,0,0,0,127,
  	125,1,0,0,0,127,128,1,0,0,0,128,130,1,0,0,0,129,127,1,0,0,0,130,131,5,
  	4,0,0,131,11,1,0,0,0,132,133,5,7,0,0,133,135,5,1,0,0,134,136,3,14,7,0,
  	135,134,1,0,0,0,135,136,1,0,0,0,136,137,1,0,0,0,137,139,5,6,0,0,138,140,
  	3,40,20,0,139,138,1,0,0,0,139,140,1,0,0,0,140,141,1,0,0,0,141,143,5,6,
  	0,0,142,144,3,16,8,0,143,142,1,0,0,0,143,144,1,0,0,0,144,145,1,0,0,0,
  	145,146,5,2,0,0,146,147,3,6,3,0,147,13,1,0,0,0,148,149,3,38,19,0,149,
  	150,5,36,0,0,150,151,5,5,0,0,151,152,3,40,20,0,152,15,1,0,0,0,153,154,
  	3,44,22,0,154,17,1,0,0,0,155,156,5,8,0,0,156,157,5,1,0,0,157,158,3,40,
  	20,0,158,159,5,2,0,0,159,163,5,3,0,0,160,162,3,6,3,0,161,160,1,0,0,0,
  	162,165,1,0,0,0,163,161,1,0,0,0,163,164,1,0,0,0,164,166,1,0,0,0,165,163,
  	1,0,0,0,166,167,5,4,0,0,167,19,1,0,0,0,168,169,5,8,0,0,169,170,5,1,0,
  	0,170,171,3,40,20,0,171,172,5,2,0,0,172,173,3,6,3,0,173,21,1,0,0,0,174,
  	175,5,9,0,0,175,176,5,1,0,0,176,177,3,40,20,0,177,178,5,2,0,0,178,182,
  	5,3,0,0,179,181,3,6,3,0,180,179,1,0,0,0,181,184,1,0,0,0,182,180,1,0,0,
  	0,182,183,1,0,0,0,183,185,1,0,0,0,184,182,1,0,0,0,185,195,5,4,0,0,186,
  	187,5,10,0,0,187,191,5,3,0,0,188,190,3,6,3,0,189,188,1,0,0,0,190,193,
  	1,0,0,0,191,189,1,0,0,0,191,192,1,0,0,0,192,194,1,0,0,0,193,191,1,0,0,
  	0,194,196,5,4,0,0,195,186,1,0,0,0,195,196,1,0,0,0,196,23,1,0,0,0,197,
  	198,5,9,0,0,198,199,5,1,0,0,199,200,3,40,20,0,200,201,5,2,0,0,201,204,
  	3,6,3,0,202,203,5,10,0,0,203,205,3,6,3,0,204,202,1,0,0,0,204,205,1,0,
  	0,0,205,25,1,0,0,0,206,207,5,36,0,0,207,209,5,1,0,0,208,210,3,28,14,0,
  	209,208,1,0,0,0,209,210,1,0,0,0,210,211,1,0,0,0,211,212,5,2,0,0,212,27,
  	1,0,0,0,213,218,3,40,20,0,214,215,5,11,0,0,215,217,3,40,20,0,216,214,
  	1,0,0,0,217,220,1,0,0,0,218,216,1,0,0,0,218,219,1,0,0,0,219,29,1,0,0,
  	0,220,218,1,0,0,0,221,223,5,12,0,0,222,224,3,40,20,0,223,222,1,0,0,0,
  	223,224,1,0,0,0,224,225,1,0,0,0,225,226,5,6,0,0,226,31,1,0,0,0,227,228,
  	3,40,20,0,228,229,5,6,0,0,229,33,1,0,0,0,230,235,3,36,18,0,231,232,5,
  	11,0,0,232,234,3,36,18,0,233,231,1,0,0,0,234,237,1,0,0,0,235,233,1,0,
  	0,0,235,236,1,0,0,0,236,35,1,0,0,0,237,235,1,0,0,0,238,239,3,38,19,0,
  	239,240,5,36,0,0,240,37,1,0,0,0,241,242,7,0,0,0,242,39,1,0,0,0,243,244,
  	3,42,21,0,244,41,1,0,0,0,245,246,3,44,22,0,246,247,3,48,24,0,247,248,
  	3,42,21,0,248,251,1,0,0,0,249,251,3,50,25,0,250,245,1,0,0,0,250,249,1,
  	0,0,0,251,43,1,0,0,0,252,253,5,16,0,0,253,258,3,44,22,0,254,255,5,17,
  	0,0,255,258,3,44,22,0,256,258,3,46,23,0,257,252,1,0,0,0,257,254,1,0,0,
  	0,257,256,1,0,0,0,258,45,1,0,0,0,259,270,5,36,0,0,260,270,5,37,0,0,261,
  	270,5,38,0,0,262,270,5,39,0,0,263,270,5,40,0,0,264,270,3,26,13,0,265,
  	266,5,1,0,0,266,267,3,40,20,0,267,268,5,2,0,0,268,270,1,0,0,0,269,259,
  	1,0,0,0,269,260,1,0,0,0,269,261,1,0,0,0,269,262,1,0,0,0,269,263,1,0,0,
  	0,269,264,1,0,0,0,269,265,1,0,0,0,270,47,1,0,0,0,271,272,7,1,0,0,272,
  	49,1,0,0,0,273,278,3,52,26,0,274,275,5,22,0,0,275,277,3,52,26,0,276,274,
  	1,0,0,0,277,280,1,0,0,0,278,276,1,0,0,0,278,279,1,0,0,0,279,51,1,0,0,
  	0,280,278,1,0,0,0,281,286,3,54,27,0,282,283,5,23,0,0,283,285,3,54,27,
  	0,284,282,1,0,0,0,285,288,1,0,0,0,286,284,1,0,0,0,286,287,1,0,0,0,287,
  	53,1,0,0,0,288,286,1,0,0,0,289,294,3,56,28,0,290,291,7,2,0,0,291,293,
  	3,56,28,0,292,290,1,0,0,0,293,296,1,0,0,0,294,292,1,0,0,0,294,295,1,0,
  	0,0,295,55,1,0,0,0,296,294,1,0,0,0,297,302,3,58,29,0,298,299,7,3,0,0,
  	299,301,3,58,29,0,300,298,1,0,0,0,301,304,1,0,0,0,302,300,1,0,0,0,302,
  	303,1,0,0,0,303,57,1,0,0,0,304,302,1,0,0,0,305,310,3,60,30,0,306,307,
  	7,4,0,0,307,309,3,60,30,0,308,306,1,0,0,0,309,312,1,0,0,0,310,308,1,0,
  	0,0,310,311,1,0,0,0,311,59,1,0,0,0,312,310,1,0,0,0,313,318,3,44,22,0,
  	314,315,7,5,0,0,315,317,3,44,22,0,316,314,1,0,0,0,317,320,1,0,0,0,318,
  	316,1,0,0,0,318,319,1,0,0,0,319,61,1,0,0,0,320,318,1,0,0,0,321,324,3,
  	58,29,0,322,324,3,60,30,0,323,321,1,0,0,0,323,322,1,0,0,0,324,63,1,0,
  	0,0,31,67,75,84,99,105,112,116,120,127,135,139,143,163,182,191,195,204,
  	209,218,223,235,250,257,269,278,286,294,302,310,318,323
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

std::vector<CASSParser::StatementContext *> CASSParser::ProgContext::statement() {
  return getRuleContexts<CASSParser::StatementContext>();
}

CASSParser::StatementContext* CASSParser::ProgContext::statement(size_t i) {
  return getRuleContext<CASSParser::StatementContext>(i);
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
    setState(65); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(64);
      statement();
      setState(67); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 2130304037762) != 0));
    setState(69);
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
    setState(71);
    typeSpec();
    setState(72);
    match(CASSParser::ID);
    setState(73);
    match(CASSParser::T__0);
    setState(75);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 57344) != 0)) {
      setState(74);
      parameterList();
    }
    setState(77);
    match(CASSParser::T__1);
    setState(78);
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
    setState(80);
    match(CASSParser::T__2);
    setState(84);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 2130304037762) != 0)) {
      setState(81);
      statement();
      setState(86);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(87);
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

CASSParser::ForBlockStatementContext* CASSParser::StatementContext::forBlockStatement() {
  return getRuleContext<CASSParser::ForBlockStatementContext>(0);
}

CASSParser::ForSingleStatementContext* CASSParser::StatementContext::forSingleStatement() {
  return getRuleContext<CASSParser::ForSingleStatementContext>(0);
}

CASSParser::WhileBlockStatementContext* CASSParser::StatementContext::whileBlockStatement() {
  return getRuleContext<CASSParser::WhileBlockStatementContext>(0);
}

CASSParser::WhileSingleStatementContext* CASSParser::StatementContext::whileSingleStatement() {
  return getRuleContext<CASSParser::WhileSingleStatementContext>(0);
}

CASSParser::IfBlockStatementContext* CASSParser::StatementContext::ifBlockStatement() {
  return getRuleContext<CASSParser::IfBlockStatementContext>(0);
}

CASSParser::IfSingleStatementContext* CASSParser::StatementContext::ifSingleStatement() {
  return getRuleContext<CASSParser::IfSingleStatementContext>(0);
}

CASSParser::ReturnStatementContext* CASSParser::StatementContext::returnStatement() {
  return getRuleContext<CASSParser::ReturnStatementContext>(0);
}

CASSParser::ExpressionStatementContext* CASSParser::StatementContext::expressionStatement() {
  return getRuleContext<CASSParser::ExpressionStatementContext>(0);
}

CASSParser::FunctionDefinitionContext* CASSParser::StatementContext::functionDefinition() {
  return getRuleContext<CASSParser::FunctionDefinitionContext>(0);
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
    setState(99);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 3, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(89);
      declarationStatement();
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(90);
      forBlockStatement();
      break;
    }

    case 3: {
      enterOuterAlt(_localctx, 3);
      setState(91);
      forSingleStatement();
      break;
    }

    case 4: {
      enterOuterAlt(_localctx, 4);
      setState(92);
      whileBlockStatement();
      break;
    }

    case 5: {
      enterOuterAlt(_localctx, 5);
      setState(93);
      whileSingleStatement();
      break;
    }

    case 6: {
      enterOuterAlt(_localctx, 6);
      setState(94);
      ifBlockStatement();
      break;
    }

    case 7: {
      enterOuterAlt(_localctx, 7);
      setState(95);
      ifSingleStatement();
      break;
    }

    case 8: {
      enterOuterAlt(_localctx, 8);
      setState(96);
      returnStatement();
      break;
    }

    case 9: {
      enterOuterAlt(_localctx, 9);
      setState(97);
      expressionStatement();
      break;
    }

    case 10: {
      enterOuterAlt(_localctx, 10);
      setState(98);
      functionDefinition();
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
    setState(101);
    typeSpec();
    setState(102);
    match(CASSParser::ID);
    setState(105);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CASSParser::T__4) {
      setState(103);
      match(CASSParser::T__4);
      setState(104);
      expression();
    }
    setState(107);
    match(CASSParser::T__5);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ForBlockStatementContext ------------------------------------------------------------------

CASSParser::ForBlockStatementContext::ForBlockStatementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CASSParser::ForInitContext* CASSParser::ForBlockStatementContext::forInit() {
  return getRuleContext<CASSParser::ForInitContext>(0);
}

CASSParser::ExpressionContext* CASSParser::ForBlockStatementContext::expression() {
  return getRuleContext<CASSParser::ExpressionContext>(0);
}

CASSParser::ForUpdateContext* CASSParser::ForBlockStatementContext::forUpdate() {
  return getRuleContext<CASSParser::ForUpdateContext>(0);
}

std::vector<CASSParser::StatementContext *> CASSParser::ForBlockStatementContext::statement() {
  return getRuleContexts<CASSParser::StatementContext>();
}

CASSParser::StatementContext* CASSParser::ForBlockStatementContext::statement(size_t i) {
  return getRuleContext<CASSParser::StatementContext>(i);
}


size_t CASSParser::ForBlockStatementContext::getRuleIndex() const {
  return CASSParser::RuleForBlockStatement;
}

void CASSParser::ForBlockStatementContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterForBlockStatement(this);
}

void CASSParser::ForBlockStatementContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitForBlockStatement(this);
}

CASSParser::ForBlockStatementContext* CASSParser::forBlockStatement() {
  ForBlockStatementContext *_localctx = _tracker.createInstance<ForBlockStatementContext>(_ctx, getState());
  enterRule(_localctx, 10, CASSParser::RuleForBlockStatement);
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
    setState(109);
    match(CASSParser::T__6);
    setState(110);
    match(CASSParser::T__0);
    setState(112);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 57344) != 0)) {
      setState(111);
      forInit();
    }
    setState(114);
    match(CASSParser::T__5);
    setState(116);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 2130303975426) != 0)) {
      setState(115);
      expression();
    }
    setState(118);
    match(CASSParser::T__5);
    setState(120);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 2130303975426) != 0)) {
      setState(119);
      forUpdate();
    }
    setState(122);
    match(CASSParser::T__1);
    setState(123);
    match(CASSParser::T__2);
    setState(127);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 2130304037762) != 0)) {
      setState(124);
      statement();
      setState(129);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(130);
    match(CASSParser::T__3);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ForSingleStatementContext ------------------------------------------------------------------

CASSParser::ForSingleStatementContext::ForSingleStatementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CASSParser::StatementContext* CASSParser::ForSingleStatementContext::statement() {
  return getRuleContext<CASSParser::StatementContext>(0);
}

CASSParser::ForInitContext* CASSParser::ForSingleStatementContext::forInit() {
  return getRuleContext<CASSParser::ForInitContext>(0);
}

CASSParser::ExpressionContext* CASSParser::ForSingleStatementContext::expression() {
  return getRuleContext<CASSParser::ExpressionContext>(0);
}

CASSParser::ForUpdateContext* CASSParser::ForSingleStatementContext::forUpdate() {
  return getRuleContext<CASSParser::ForUpdateContext>(0);
}


size_t CASSParser::ForSingleStatementContext::getRuleIndex() const {
  return CASSParser::RuleForSingleStatement;
}

void CASSParser::ForSingleStatementContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterForSingleStatement(this);
}

void CASSParser::ForSingleStatementContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitForSingleStatement(this);
}

CASSParser::ForSingleStatementContext* CASSParser::forSingleStatement() {
  ForSingleStatementContext *_localctx = _tracker.createInstance<ForSingleStatementContext>(_ctx, getState());
  enterRule(_localctx, 12, CASSParser::RuleForSingleStatement);
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
    setState(132);
    match(CASSParser::T__6);
    setState(133);
    match(CASSParser::T__0);
    setState(135);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 57344) != 0)) {
      setState(134);
      forInit();
    }
    setState(137);
    match(CASSParser::T__5);
    setState(139);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 2130303975426) != 0)) {
      setState(138);
      expression();
    }
    setState(141);
    match(CASSParser::T__5);
    setState(143);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 2130303975426) != 0)) {
      setState(142);
      forUpdate();
    }
    setState(145);
    match(CASSParser::T__1);
    setState(146);
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
  enterRule(_localctx, 14, CASSParser::RuleForInit);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(148);
    typeSpec();
    setState(149);
    match(CASSParser::ID);
    setState(150);
    match(CASSParser::T__4);
    setState(151);
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
  enterRule(_localctx, 16, CASSParser::RuleForUpdate);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(153);
    unaryExpression();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- WhileBlockStatementContext ------------------------------------------------------------------

CASSParser::WhileBlockStatementContext::WhileBlockStatementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CASSParser::ExpressionContext* CASSParser::WhileBlockStatementContext::expression() {
  return getRuleContext<CASSParser::ExpressionContext>(0);
}

std::vector<CASSParser::StatementContext *> CASSParser::WhileBlockStatementContext::statement() {
  return getRuleContexts<CASSParser::StatementContext>();
}

CASSParser::StatementContext* CASSParser::WhileBlockStatementContext::statement(size_t i) {
  return getRuleContext<CASSParser::StatementContext>(i);
}


size_t CASSParser::WhileBlockStatementContext::getRuleIndex() const {
  return CASSParser::RuleWhileBlockStatement;
}

void CASSParser::WhileBlockStatementContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterWhileBlockStatement(this);
}

void CASSParser::WhileBlockStatementContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitWhileBlockStatement(this);
}

CASSParser::WhileBlockStatementContext* CASSParser::whileBlockStatement() {
  WhileBlockStatementContext *_localctx = _tracker.createInstance<WhileBlockStatementContext>(_ctx, getState());
  enterRule(_localctx, 18, CASSParser::RuleWhileBlockStatement);
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
    setState(155);
    match(CASSParser::T__7);
    setState(156);
    match(CASSParser::T__0);
    setState(157);
    expression();
    setState(158);
    match(CASSParser::T__1);
    setState(159);
    match(CASSParser::T__2);
    setState(163);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 2130304037762) != 0)) {
      setState(160);
      statement();
      setState(165);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(166);
    match(CASSParser::T__3);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- WhileSingleStatementContext ------------------------------------------------------------------

CASSParser::WhileSingleStatementContext::WhileSingleStatementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CASSParser::ExpressionContext* CASSParser::WhileSingleStatementContext::expression() {
  return getRuleContext<CASSParser::ExpressionContext>(0);
}

CASSParser::StatementContext* CASSParser::WhileSingleStatementContext::statement() {
  return getRuleContext<CASSParser::StatementContext>(0);
}


size_t CASSParser::WhileSingleStatementContext::getRuleIndex() const {
  return CASSParser::RuleWhileSingleStatement;
}

void CASSParser::WhileSingleStatementContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterWhileSingleStatement(this);
}

void CASSParser::WhileSingleStatementContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitWhileSingleStatement(this);
}

CASSParser::WhileSingleStatementContext* CASSParser::whileSingleStatement() {
  WhileSingleStatementContext *_localctx = _tracker.createInstance<WhileSingleStatementContext>(_ctx, getState());
  enterRule(_localctx, 20, CASSParser::RuleWhileSingleStatement);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(168);
    match(CASSParser::T__7);
    setState(169);
    match(CASSParser::T__0);
    setState(170);
    expression();
    setState(171);
    match(CASSParser::T__1);
    setState(172);
    statement();
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- IfBlockStatementContext ------------------------------------------------------------------

CASSParser::IfBlockStatementContext::IfBlockStatementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CASSParser::ExpressionContext* CASSParser::IfBlockStatementContext::expression() {
  return getRuleContext<CASSParser::ExpressionContext>(0);
}

std::vector<CASSParser::StatementContext *> CASSParser::IfBlockStatementContext::statement() {
  return getRuleContexts<CASSParser::StatementContext>();
}

CASSParser::StatementContext* CASSParser::IfBlockStatementContext::statement(size_t i) {
  return getRuleContext<CASSParser::StatementContext>(i);
}


size_t CASSParser::IfBlockStatementContext::getRuleIndex() const {
  return CASSParser::RuleIfBlockStatement;
}

void CASSParser::IfBlockStatementContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterIfBlockStatement(this);
}

void CASSParser::IfBlockStatementContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitIfBlockStatement(this);
}

CASSParser::IfBlockStatementContext* CASSParser::ifBlockStatement() {
  IfBlockStatementContext *_localctx = _tracker.createInstance<IfBlockStatementContext>(_ctx, getState());
  enterRule(_localctx, 22, CASSParser::RuleIfBlockStatement);
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
    match(CASSParser::T__8);
    setState(175);
    match(CASSParser::T__0);
    setState(176);
    expression();
    setState(177);
    match(CASSParser::T__1);
    setState(178);
    match(CASSParser::T__2);
    setState(182);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 2130304037762) != 0)) {
      setState(179);
      statement();
      setState(184);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(185);
    match(CASSParser::T__3);
    setState(195);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 15, _ctx)) {
    case 1: {
      setState(186);
      match(CASSParser::T__9);
      setState(187);
      match(CASSParser::T__2);
      setState(191);
      _errHandler->sync(this);
      _la = _input->LA(1);
      while ((((_la & ~ 0x3fULL) == 0) &&
        ((1ULL << _la) & 2130304037762) != 0)) {
        setState(188);
        statement();
        setState(193);
        _errHandler->sync(this);
        _la = _input->LA(1);
      }
      setState(194);
      match(CASSParser::T__3);
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

//----------------- IfSingleStatementContext ------------------------------------------------------------------

CASSParser::IfSingleStatementContext::IfSingleStatementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CASSParser::ExpressionContext* CASSParser::IfSingleStatementContext::expression() {
  return getRuleContext<CASSParser::ExpressionContext>(0);
}

std::vector<CASSParser::StatementContext *> CASSParser::IfSingleStatementContext::statement() {
  return getRuleContexts<CASSParser::StatementContext>();
}

CASSParser::StatementContext* CASSParser::IfSingleStatementContext::statement(size_t i) {
  return getRuleContext<CASSParser::StatementContext>(i);
}


size_t CASSParser::IfSingleStatementContext::getRuleIndex() const {
  return CASSParser::RuleIfSingleStatement;
}

void CASSParser::IfSingleStatementContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterIfSingleStatement(this);
}

void CASSParser::IfSingleStatementContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitIfSingleStatement(this);
}

CASSParser::IfSingleStatementContext* CASSParser::ifSingleStatement() {
  IfSingleStatementContext *_localctx = _tracker.createInstance<IfSingleStatementContext>(_ctx, getState());
  enterRule(_localctx, 24, CASSParser::RuleIfSingleStatement);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(197);
    match(CASSParser::T__8);
    setState(198);
    match(CASSParser::T__0);
    setState(199);
    expression();
    setState(200);
    match(CASSParser::T__1);
    setState(201);
    statement();
    setState(204);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 16, _ctx)) {
    case 1: {
      setState(202);
      match(CASSParser::T__9);
      setState(203);
      statement();
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

//----------------- FunctionCallContext ------------------------------------------------------------------

CASSParser::FunctionCallContext::FunctionCallContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CASSParser::FunctionCallContext::ID() {
  return getToken(CASSParser::ID, 0);
}

CASSParser::ArgumentListContext* CASSParser::FunctionCallContext::argumentList() {
  return getRuleContext<CASSParser::ArgumentListContext>(0);
}


size_t CASSParser::FunctionCallContext::getRuleIndex() const {
  return CASSParser::RuleFunctionCall;
}

void CASSParser::FunctionCallContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterFunctionCall(this);
}

void CASSParser::FunctionCallContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitFunctionCall(this);
}

CASSParser::FunctionCallContext* CASSParser::functionCall() {
  FunctionCallContext *_localctx = _tracker.createInstance<FunctionCallContext>(_ctx, getState());
  enterRule(_localctx, 26, CASSParser::RuleFunctionCall);
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
    setState(206);
    match(CASSParser::ID);
    setState(207);
    match(CASSParser::T__0);
    setState(209);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 2130303975426) != 0)) {
      setState(208);
      argumentList();
    }
    setState(211);
    match(CASSParser::T__1);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- ArgumentListContext ------------------------------------------------------------------

CASSParser::ArgumentListContext::ArgumentListContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

std::vector<CASSParser::ExpressionContext *> CASSParser::ArgumentListContext::expression() {
  return getRuleContexts<CASSParser::ExpressionContext>();
}

CASSParser::ExpressionContext* CASSParser::ArgumentListContext::expression(size_t i) {
  return getRuleContext<CASSParser::ExpressionContext>(i);
}


size_t CASSParser::ArgumentListContext::getRuleIndex() const {
  return CASSParser::RuleArgumentList;
}

void CASSParser::ArgumentListContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterArgumentList(this);
}

void CASSParser::ArgumentListContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitArgumentList(this);
}

CASSParser::ArgumentListContext* CASSParser::argumentList() {
  ArgumentListContext *_localctx = _tracker.createInstance<ArgumentListContext>(_ctx, getState());
  enterRule(_localctx, 28, CASSParser::RuleArgumentList);
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
    setState(213);
    expression();
    setState(218);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CASSParser::T__10) {
      setState(214);
      match(CASSParser::T__10);
      setState(215);
      expression();
      setState(220);
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
  enterRule(_localctx, 30, CASSParser::RuleReturnStatement);
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
    setState(221);
    match(CASSParser::T__11);
    setState(223);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 2130303975426) != 0)) {
      setState(222);
      expression();
    }
    setState(225);
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
  enterRule(_localctx, 32, CASSParser::RuleExpressionStatement);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(227);
    expression();
    setState(228);
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
  enterRule(_localctx, 34, CASSParser::RuleParameterList);
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
    setState(230);
    parameter();
    setState(235);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CASSParser::T__10) {
      setState(231);
      match(CASSParser::T__10);
      setState(232);
      parameter();
      setState(237);
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
  enterRule(_localctx, 36, CASSParser::RuleParameter);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(238);
    typeSpec();
    setState(239);
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
  enterRule(_localctx, 38, CASSParser::RuleTypeSpec);
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
    setState(241);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 57344) != 0))) {
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
  enterRule(_localctx, 40, CASSParser::RuleExpression);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(243);
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
  enterRule(_localctx, 42, CASSParser::RuleAssignmentExpression);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(250);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 21, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(245);
      unaryExpression();
      setState(246);
      assignmentOperator();
      setState(247);
      assignmentExpression();
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(249);
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
  enterRule(_localctx, 44, CASSParser::RuleUnaryExpression);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(257);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CASSParser::T__15: {
        enterOuterAlt(_localctx, 1);
        setState(252);
        match(CASSParser::T__15);
        setState(253);
        unaryExpression();
        break;
      }

      case CASSParser::T__16: {
        enterOuterAlt(_localctx, 2);
        setState(254);
        match(CASSParser::T__16);
        setState(255);
        unaryExpression();
        break;
      }

      case CASSParser::T__0:
      case CASSParser::ID:
      case CASSParser::INT:
      case CASSParser::FLOAT:
      case CASSParser::CHAR:
      case CASSParser::STRING: {
        enterOuterAlt(_localctx, 3);
        setState(256);
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

tree::TerminalNode* CASSParser::PrimaryExpressionContext::FLOAT() {
  return getToken(CASSParser::FLOAT, 0);
}

tree::TerminalNode* CASSParser::PrimaryExpressionContext::CHAR() {
  return getToken(CASSParser::CHAR, 0);
}

tree::TerminalNode* CASSParser::PrimaryExpressionContext::STRING() {
  return getToken(CASSParser::STRING, 0);
}

CASSParser::FunctionCallContext* CASSParser::PrimaryExpressionContext::functionCall() {
  return getRuleContext<CASSParser::FunctionCallContext>(0);
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
  enterRule(_localctx, 46, CASSParser::RulePrimaryExpression);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(269);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 23, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(259);
      match(CASSParser::ID);
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(260);
      match(CASSParser::INT);
      break;
    }

    case 3: {
      enterOuterAlt(_localctx, 3);
      setState(261);
      match(CASSParser::FLOAT);
      break;
    }

    case 4: {
      enterOuterAlt(_localctx, 4);
      setState(262);
      match(CASSParser::CHAR);
      break;
    }

    case 5: {
      enterOuterAlt(_localctx, 5);
      setState(263);
      match(CASSParser::STRING);
      break;
    }

    case 6: {
      enterOuterAlt(_localctx, 6);
      setState(264);
      functionCall();
      break;
    }

    case 7: {
      enterOuterAlt(_localctx, 7);
      setState(265);
      match(CASSParser::T__0);
      setState(266);
      expression();
      setState(267);
      match(CASSParser::T__1);
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
  enterRule(_localctx, 48, CASSParser::RuleAssignmentOperator);
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
    setState(271);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 3932192) != 0))) {
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
  enterRule(_localctx, 50, CASSParser::RuleLogicalOrExpression);
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
    setState(273);
    logicalAndExpression();
    setState(278);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CASSParser::T__21) {
      setState(274);
      match(CASSParser::T__21);
      setState(275);
      logicalAndExpression();
      setState(280);
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
  enterRule(_localctx, 52, CASSParser::RuleLogicalAndExpression);
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
    setState(281);
    equalityExpression();
    setState(286);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CASSParser::T__22) {
      setState(282);
      match(CASSParser::T__22);
      setState(283);
      equalityExpression();
      setState(288);
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
  enterRule(_localctx, 54, CASSParser::RuleEqualityExpression);
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
    setState(289);
    relationalExpression();
    setState(294);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CASSParser::T__23

    || _la == CASSParser::T__24) {
      setState(290);
      _la = _input->LA(1);
      if (!(_la == CASSParser::T__23

      || _la == CASSParser::T__24)) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
      setState(291);
      relationalExpression();
      setState(296);
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
  enterRule(_localctx, 56, CASSParser::RuleRelationalExpression);
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
    setState(297);
    additiveExpression();
    setState(302);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 1006632960) != 0)) {
      setState(298);
      _la = _input->LA(1);
      if (!((((_la & ~ 0x3fULL) == 0) &&
        ((1ULL << _la) & 1006632960) != 0))) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
      setState(299);
      additiveExpression();
      setState(304);
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
  enterRule(_localctx, 58, CASSParser::RuleAdditiveExpression);
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
    setState(305);
    multiplicativeExpression();
    setState(310);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CASSParser::T__29

    || _la == CASSParser::T__30) {
      setState(306);
      _la = _input->LA(1);
      if (!(_la == CASSParser::T__29

      || _la == CASSParser::T__30)) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
      setState(307);
      multiplicativeExpression();
      setState(312);
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
  enterRule(_localctx, 60, CASSParser::RuleMultiplicativeExpression);
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
    setState(313);
    unaryExpression();
    setState(318);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CASSParser::T__31

    || _la == CASSParser::T__32) {
      setState(314);
      _la = _input->LA(1);
      if (!(_la == CASSParser::T__31

      || _la == CASSParser::T__32)) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
      setState(315);
      unaryExpression();
      setState(320);
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

//----------------- OperationExpressionContext ------------------------------------------------------------------

CASSParser::OperationExpressionContext::OperationExpressionContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

CASSParser::AdditiveExpressionContext* CASSParser::OperationExpressionContext::additiveExpression() {
  return getRuleContext<CASSParser::AdditiveExpressionContext>(0);
}

CASSParser::MultiplicativeExpressionContext* CASSParser::OperationExpressionContext::multiplicativeExpression() {
  return getRuleContext<CASSParser::MultiplicativeExpressionContext>(0);
}


size_t CASSParser::OperationExpressionContext::getRuleIndex() const {
  return CASSParser::RuleOperationExpression;
}

void CASSParser::OperationExpressionContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterOperationExpression(this);
}

void CASSParser::OperationExpressionContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitOperationExpression(this);
}

CASSParser::OperationExpressionContext* CASSParser::operationExpression() {
  OperationExpressionContext *_localctx = _tracker.createInstance<OperationExpressionContext>(_ctx, getState());
  enterRule(_localctx, 62, CASSParser::RuleOperationExpression);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(323);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 30, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(321);
      additiveExpression();
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(322);
      multiplicativeExpression();
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

void CASSParser::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  cassParserInitialize();
#else
  ::antlr4::internal::call_once(cassParserOnceFlag, cassParserInitialize);
#endif
}
