
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
      "expressionStatement", "includeStatement", "parameterList", "parameter", 
      "typeSpec", "expression", "assignmentExpression", "unaryExpression", 
      "primaryExpression", "assignmentOperator", "logicalOrExpression", 
      "logicalAndExpression", "equalityExpression", "relationalExpression", 
      "additiveExpression", "multiplicativeExpression", "operationExpression"
    },
    std::vector<std::string>{
      "", "'('", "')'", "'{'", "'}'", "'='", "';'", "'for'", "'while'", 
      "'if'", "'else'", "','", "'return'", "'include'", "'int'", "'float'", 
      "'double'", "'++'", "'--'", "'+='", "'-='", "'*='", "'/='", "'||'", 
      "'&&'", "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'+'", "'-'", 
      "'*'", "'/'", "'%'"
    },
    std::vector<std::string>{
      "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 
      "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", 
      "", "", "SL_COMMENT", "ML_COMMENT", "ID", "INT", "FLOAT", "CHAR", 
      "STRING", "WS"
    }
  );
  static const int32_t serializedATNSegment[] = {
  	4,1,43,332,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,6,2,
  	7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,7,
  	14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,7,20,2,21,7,
  	21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,2,27,7,27,2,28,7,
  	28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,4,0,68,8,0,11,0,12,0,69,
  	1,0,1,0,1,1,1,1,1,1,1,1,3,1,78,8,1,1,1,1,1,1,1,1,2,1,2,5,2,85,8,2,10,
  	2,12,2,88,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,
  	103,8,3,1,4,1,4,1,4,1,4,3,4,109,8,4,1,4,1,4,1,5,1,5,1,5,3,5,116,8,5,1,
  	5,1,5,3,5,120,8,5,1,5,1,5,3,5,124,8,5,1,5,1,5,1,5,5,5,129,8,5,10,5,12,
  	5,132,9,5,1,5,1,5,1,6,1,6,1,6,3,6,139,8,6,1,6,1,6,3,6,143,8,6,1,6,1,6,
  	3,6,147,8,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,9,1,
  	9,1,9,5,9,165,8,9,10,9,12,9,168,9,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,
  	1,10,1,11,1,11,1,11,1,11,1,11,1,11,5,11,184,8,11,10,11,12,11,187,9,11,
  	1,11,1,11,1,11,1,11,5,11,193,8,11,10,11,12,11,196,9,11,1,11,3,11,199,
  	8,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,3,12,208,8,12,1,13,1,13,1,13,
  	3,13,213,8,13,1,13,1,13,1,14,1,14,1,14,5,14,220,8,14,10,14,12,14,223,
  	9,14,1,15,1,15,3,15,227,8,15,1,15,1,15,1,16,1,16,1,16,1,17,1,17,1,17,
  	1,18,1,18,1,18,5,18,240,8,18,10,18,12,18,243,9,18,1,19,1,19,1,19,1,20,
  	1,20,1,21,1,21,1,22,1,22,1,22,1,22,1,22,3,22,257,8,22,1,23,1,23,1,23,
  	1,23,1,23,3,23,264,8,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
  	1,24,3,24,276,8,24,1,25,1,25,1,26,1,26,1,26,5,26,283,8,26,10,26,12,26,
  	286,9,26,1,27,1,27,1,27,5,27,291,8,27,10,27,12,27,294,9,27,1,28,1,28,
  	1,28,5,28,299,8,28,10,28,12,28,302,9,28,1,29,1,29,1,29,5,29,307,8,29,
  	10,29,12,29,310,9,29,1,30,1,30,1,30,5,30,315,8,30,10,30,12,30,318,9,30,
  	1,31,1,31,1,31,5,31,323,8,31,10,31,12,31,326,9,31,1,32,1,32,3,32,330,
  	8,32,1,32,0,0,33,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,
  	38,40,42,44,46,48,50,52,54,56,58,60,62,64,0,6,1,0,14,16,2,0,5,5,19,22,
  	1,0,25,26,1,0,27,30,1,0,31,32,1,0,33,35,344,0,67,1,0,0,0,2,73,1,0,0,0,
  	4,82,1,0,0,0,6,102,1,0,0,0,8,104,1,0,0,0,10,112,1,0,0,0,12,135,1,0,0,
  	0,14,151,1,0,0,0,16,156,1,0,0,0,18,158,1,0,0,0,20,171,1,0,0,0,22,177,
  	1,0,0,0,24,200,1,0,0,0,26,209,1,0,0,0,28,216,1,0,0,0,30,224,1,0,0,0,32,
  	230,1,0,0,0,34,233,1,0,0,0,36,236,1,0,0,0,38,244,1,0,0,0,40,247,1,0,0,
  	0,42,249,1,0,0,0,44,256,1,0,0,0,46,263,1,0,0,0,48,275,1,0,0,0,50,277,
  	1,0,0,0,52,279,1,0,0,0,54,287,1,0,0,0,56,295,1,0,0,0,58,303,1,0,0,0,60,
  	311,1,0,0,0,62,319,1,0,0,0,64,329,1,0,0,0,66,68,3,6,3,0,67,66,1,0,0,0,
  	68,69,1,0,0,0,69,67,1,0,0,0,69,70,1,0,0,0,70,71,1,0,0,0,71,72,5,0,0,1,
  	72,1,1,0,0,0,73,74,3,40,20,0,74,75,5,38,0,0,75,77,5,1,0,0,76,78,3,36,
  	18,0,77,76,1,0,0,0,77,78,1,0,0,0,78,79,1,0,0,0,79,80,5,2,0,0,80,81,3,
  	4,2,0,81,3,1,0,0,0,82,86,5,3,0,0,83,85,3,6,3,0,84,83,1,0,0,0,85,88,1,
  	0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,89,1,0,0,0,88,86,1,0,0,0,89,90,5,
  	4,0,0,90,5,1,0,0,0,91,103,3,8,4,0,92,103,3,10,5,0,93,103,3,12,6,0,94,
  	103,3,18,9,0,95,103,3,20,10,0,96,103,3,22,11,0,97,103,3,24,12,0,98,103,
  	3,30,15,0,99,103,3,32,16,0,100,103,3,2,1,0,101,103,3,34,17,0,102,91,1,
  	0,0,0,102,92,1,0,0,0,102,93,1,0,0,0,102,94,1,0,0,0,102,95,1,0,0,0,102,
  	96,1,0,0,0,102,97,1,0,0,0,102,98,1,0,0,0,102,99,1,0,0,0,102,100,1,0,0,
  	0,102,101,1,0,0,0,103,7,1,0,0,0,104,105,3,40,20,0,105,108,5,38,0,0,106,
  	107,5,5,0,0,107,109,3,42,21,0,108,106,1,0,0,0,108,109,1,0,0,0,109,110,
  	1,0,0,0,110,111,5,6,0,0,111,9,1,0,0,0,112,113,5,7,0,0,113,115,5,1,0,0,
  	114,116,3,14,7,0,115,114,1,0,0,0,115,116,1,0,0,0,116,117,1,0,0,0,117,
  	119,5,6,0,0,118,120,3,42,21,0,119,118,1,0,0,0,119,120,1,0,0,0,120,121,
  	1,0,0,0,121,123,5,6,0,0,122,124,3,16,8,0,123,122,1,0,0,0,123,124,1,0,
  	0,0,124,125,1,0,0,0,125,126,5,2,0,0,126,130,5,3,0,0,127,129,3,6,3,0,128,
  	127,1,0,0,0,129,132,1,0,0,0,130,128,1,0,0,0,130,131,1,0,0,0,131,133,1,
  	0,0,0,132,130,1,0,0,0,133,134,5,4,0,0,134,11,1,0,0,0,135,136,5,7,0,0,
  	136,138,5,1,0,0,137,139,3,14,7,0,138,137,1,0,0,0,138,139,1,0,0,0,139,
  	140,1,0,0,0,140,142,5,6,0,0,141,143,3,42,21,0,142,141,1,0,0,0,142,143,
  	1,0,0,0,143,144,1,0,0,0,144,146,5,6,0,0,145,147,3,16,8,0,146,145,1,0,
  	0,0,146,147,1,0,0,0,147,148,1,0,0,0,148,149,5,2,0,0,149,150,3,6,3,0,150,
  	13,1,0,0,0,151,152,3,40,20,0,152,153,5,38,0,0,153,154,5,5,0,0,154,155,
  	3,42,21,0,155,15,1,0,0,0,156,157,3,46,23,0,157,17,1,0,0,0,158,159,5,8,
  	0,0,159,160,5,1,0,0,160,161,3,42,21,0,161,162,5,2,0,0,162,166,5,3,0,0,
  	163,165,3,6,3,0,164,163,1,0,0,0,165,168,1,0,0,0,166,164,1,0,0,0,166,167,
  	1,0,0,0,167,169,1,0,0,0,168,166,1,0,0,0,169,170,5,4,0,0,170,19,1,0,0,
  	0,171,172,5,8,0,0,172,173,5,1,0,0,173,174,3,42,21,0,174,175,5,2,0,0,175,
  	176,3,6,3,0,176,21,1,0,0,0,177,178,5,9,0,0,178,179,5,1,0,0,179,180,3,
  	42,21,0,180,181,5,2,0,0,181,185,5,3,0,0,182,184,3,6,3,0,183,182,1,0,0,
  	0,184,187,1,0,0,0,185,183,1,0,0,0,185,186,1,0,0,0,186,188,1,0,0,0,187,
  	185,1,0,0,0,188,198,5,4,0,0,189,190,5,10,0,0,190,194,5,3,0,0,191,193,
  	3,6,3,0,192,191,1,0,0,0,193,196,1,0,0,0,194,192,1,0,0,0,194,195,1,0,0,
  	0,195,197,1,0,0,0,196,194,1,0,0,0,197,199,5,4,0,0,198,189,1,0,0,0,198,
  	199,1,0,0,0,199,23,1,0,0,0,200,201,5,9,0,0,201,202,5,1,0,0,202,203,3,
  	42,21,0,203,204,5,2,0,0,204,207,3,6,3,0,205,206,5,10,0,0,206,208,3,6,
  	3,0,207,205,1,0,0,0,207,208,1,0,0,0,208,25,1,0,0,0,209,210,5,38,0,0,210,
  	212,5,1,0,0,211,213,3,28,14,0,212,211,1,0,0,0,212,213,1,0,0,0,213,214,
  	1,0,0,0,214,215,5,2,0,0,215,27,1,0,0,0,216,221,3,42,21,0,217,218,5,11,
  	0,0,218,220,3,42,21,0,219,217,1,0,0,0,220,223,1,0,0,0,221,219,1,0,0,0,
  	221,222,1,0,0,0,222,29,1,0,0,0,223,221,1,0,0,0,224,226,5,12,0,0,225,227,
  	3,42,21,0,226,225,1,0,0,0,226,227,1,0,0,0,227,228,1,0,0,0,228,229,5,6,
  	0,0,229,31,1,0,0,0,230,231,3,42,21,0,231,232,5,6,0,0,232,33,1,0,0,0,233,
  	234,5,13,0,0,234,235,5,42,0,0,235,35,1,0,0,0,236,241,3,38,19,0,237,238,
  	5,11,0,0,238,240,3,38,19,0,239,237,1,0,0,0,240,243,1,0,0,0,241,239,1,
  	0,0,0,241,242,1,0,0,0,242,37,1,0,0,0,243,241,1,0,0,0,244,245,3,40,20,
  	0,245,246,5,38,0,0,246,39,1,0,0,0,247,248,7,0,0,0,248,41,1,0,0,0,249,
  	250,3,44,22,0,250,43,1,0,0,0,251,252,3,46,23,0,252,253,3,50,25,0,253,
  	254,3,44,22,0,254,257,1,0,0,0,255,257,3,52,26,0,256,251,1,0,0,0,256,255,
  	1,0,0,0,257,45,1,0,0,0,258,259,5,17,0,0,259,264,3,46,23,0,260,261,5,18,
  	0,0,261,264,3,46,23,0,262,264,3,48,24,0,263,258,1,0,0,0,263,260,1,0,0,
  	0,263,262,1,0,0,0,264,47,1,0,0,0,265,276,5,38,0,0,266,276,5,39,0,0,267,
  	276,5,40,0,0,268,276,5,41,0,0,269,276,5,42,0,0,270,276,3,26,13,0,271,
  	272,5,1,0,0,272,273,3,42,21,0,273,274,5,2,0,0,274,276,1,0,0,0,275,265,
  	1,0,0,0,275,266,1,0,0,0,275,267,1,0,0,0,275,268,1,0,0,0,275,269,1,0,0,
  	0,275,270,1,0,0,0,275,271,1,0,0,0,276,49,1,0,0,0,277,278,7,1,0,0,278,
  	51,1,0,0,0,279,284,3,54,27,0,280,281,5,23,0,0,281,283,3,54,27,0,282,280,
  	1,0,0,0,283,286,1,0,0,0,284,282,1,0,0,0,284,285,1,0,0,0,285,53,1,0,0,
  	0,286,284,1,0,0,0,287,292,3,56,28,0,288,289,5,24,0,0,289,291,3,56,28,
  	0,290,288,1,0,0,0,291,294,1,0,0,0,292,290,1,0,0,0,292,293,1,0,0,0,293,
  	55,1,0,0,0,294,292,1,0,0,0,295,300,3,58,29,0,296,297,7,2,0,0,297,299,
  	3,58,29,0,298,296,1,0,0,0,299,302,1,0,0,0,300,298,1,0,0,0,300,301,1,0,
  	0,0,301,57,1,0,0,0,302,300,1,0,0,0,303,308,3,60,30,0,304,305,7,3,0,0,
  	305,307,3,60,30,0,306,304,1,0,0,0,307,310,1,0,0,0,308,306,1,0,0,0,308,
  	309,1,0,0,0,309,59,1,0,0,0,310,308,1,0,0,0,311,316,3,62,31,0,312,313,
  	7,4,0,0,313,315,3,62,31,0,314,312,1,0,0,0,315,318,1,0,0,0,316,314,1,0,
  	0,0,316,317,1,0,0,0,317,61,1,0,0,0,318,316,1,0,0,0,319,324,3,46,23,0,
  	320,321,7,5,0,0,321,323,3,46,23,0,322,320,1,0,0,0,323,326,1,0,0,0,324,
  	322,1,0,0,0,324,325,1,0,0,0,325,63,1,0,0,0,326,324,1,0,0,0,327,330,3,
  	60,30,0,328,330,3,62,31,0,329,327,1,0,0,0,329,328,1,0,0,0,330,65,1,0,
  	0,0,31,69,77,86,102,108,115,119,123,130,138,142,146,166,185,194,198,207,
  	212,221,226,241,256,263,275,284,292,300,308,316,324,329
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
    setState(67); 
    _errHandler->sync(this);
    _la = _input->LA(1);
    do {
      setState(66);
      statement();
      setState(69); 
      _errHandler->sync(this);
      _la = _input->LA(1);
    } while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 8521215636354) != 0));
    setState(71);
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
    setState(73);
    typeSpec();
    setState(74);
    match(CASSParser::ID);
    setState(75);
    match(CASSParser::T__0);
    setState(77);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 114688) != 0)) {
      setState(76);
      parameterList();
    }
    setState(79);
    match(CASSParser::T__1);
    setState(80);
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
    setState(82);
    match(CASSParser::T__2);
    setState(86);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 8521215636354) != 0)) {
      setState(83);
      statement();
      setState(88);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(89);
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

CASSParser::IncludeStatementContext* CASSParser::StatementContext::includeStatement() {
  return getRuleContext<CASSParser::IncludeStatementContext>(0);
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
    setState(102);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 3, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(91);
      declarationStatement();
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(92);
      forBlockStatement();
      break;
    }

    case 3: {
      enterOuterAlt(_localctx, 3);
      setState(93);
      forSingleStatement();
      break;
    }

    case 4: {
      enterOuterAlt(_localctx, 4);
      setState(94);
      whileBlockStatement();
      break;
    }

    case 5: {
      enterOuterAlt(_localctx, 5);
      setState(95);
      whileSingleStatement();
      break;
    }

    case 6: {
      enterOuterAlt(_localctx, 6);
      setState(96);
      ifBlockStatement();
      break;
    }

    case 7: {
      enterOuterAlt(_localctx, 7);
      setState(97);
      ifSingleStatement();
      break;
    }

    case 8: {
      enterOuterAlt(_localctx, 8);
      setState(98);
      returnStatement();
      break;
    }

    case 9: {
      enterOuterAlt(_localctx, 9);
      setState(99);
      expressionStatement();
      break;
    }

    case 10: {
      enterOuterAlt(_localctx, 10);
      setState(100);
      functionDefinition();
      break;
    }

    case 11: {
      enterOuterAlt(_localctx, 11);
      setState(101);
      includeStatement();
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
    setState(104);
    typeSpec();
    setState(105);
    match(CASSParser::ID);
    setState(108);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if (_la == CASSParser::T__4) {
      setState(106);
      match(CASSParser::T__4);
      setState(107);
      expression();
    }
    setState(110);
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
    setState(112);
    match(CASSParser::T__6);
    setState(113);
    match(CASSParser::T__0);
    setState(115);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 114688) != 0)) {
      setState(114);
      forInit();
    }
    setState(117);
    match(CASSParser::T__5);
    setState(119);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 8521215508482) != 0)) {
      setState(118);
      expression();
    }
    setState(121);
    match(CASSParser::T__5);
    setState(123);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 8521215508482) != 0)) {
      setState(122);
      forUpdate();
    }
    setState(125);
    match(CASSParser::T__1);
    setState(126);
    match(CASSParser::T__2);
    setState(130);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 8521215636354) != 0)) {
      setState(127);
      statement();
      setState(132);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(133);
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
    setState(135);
    match(CASSParser::T__6);
    setState(136);
    match(CASSParser::T__0);
    setState(138);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 114688) != 0)) {
      setState(137);
      forInit();
    }
    setState(140);
    match(CASSParser::T__5);
    setState(142);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 8521215508482) != 0)) {
      setState(141);
      expression();
    }
    setState(144);
    match(CASSParser::T__5);
    setState(146);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 8521215508482) != 0)) {
      setState(145);
      forUpdate();
    }
    setState(148);
    match(CASSParser::T__1);
    setState(149);
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
    setState(151);
    typeSpec();
    setState(152);
    match(CASSParser::ID);
    setState(153);
    match(CASSParser::T__4);
    setState(154);
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
    setState(156);
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
    setState(158);
    match(CASSParser::T__7);
    setState(159);
    match(CASSParser::T__0);
    setState(160);
    expression();
    setState(161);
    match(CASSParser::T__1);
    setState(162);
    match(CASSParser::T__2);
    setState(166);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 8521215636354) != 0)) {
      setState(163);
      statement();
      setState(168);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(169);
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
    setState(171);
    match(CASSParser::T__7);
    setState(172);
    match(CASSParser::T__0);
    setState(173);
    expression();
    setState(174);
    match(CASSParser::T__1);
    setState(175);
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
    setState(177);
    match(CASSParser::T__8);
    setState(178);
    match(CASSParser::T__0);
    setState(179);
    expression();
    setState(180);
    match(CASSParser::T__1);
    setState(181);
    match(CASSParser::T__2);
    setState(185);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 8521215636354) != 0)) {
      setState(182);
      statement();
      setState(187);
      _errHandler->sync(this);
      _la = _input->LA(1);
    }
    setState(188);
    match(CASSParser::T__3);
    setState(198);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 15, _ctx)) {
    case 1: {
      setState(189);
      match(CASSParser::T__9);
      setState(190);
      match(CASSParser::T__2);
      setState(194);
      _errHandler->sync(this);
      _la = _input->LA(1);
      while ((((_la & ~ 0x3fULL) == 0) &&
        ((1ULL << _la) & 8521215636354) != 0)) {
        setState(191);
        statement();
        setState(196);
        _errHandler->sync(this);
        _la = _input->LA(1);
      }
      setState(197);
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
    setState(200);
    match(CASSParser::T__8);
    setState(201);
    match(CASSParser::T__0);
    setState(202);
    expression();
    setState(203);
    match(CASSParser::T__1);
    setState(204);
    statement();
    setState(207);
    _errHandler->sync(this);

    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 16, _ctx)) {
    case 1: {
      setState(205);
      match(CASSParser::T__9);
      setState(206);
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
    setState(209);
    match(CASSParser::ID);
    setState(210);
    match(CASSParser::T__0);
    setState(212);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 8521215508482) != 0)) {
      setState(211);
      argumentList();
    }
    setState(214);
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
    setState(216);
    expression();
    setState(221);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CASSParser::T__10) {
      setState(217);
      match(CASSParser::T__10);
      setState(218);
      expression();
      setState(223);
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
    setState(224);
    match(CASSParser::T__11);
    setState(226);
    _errHandler->sync(this);

    _la = _input->LA(1);
    if ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 8521215508482) != 0)) {
      setState(225);
      expression();
    }
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
    setState(230);
    expression();
    setState(231);
    match(CASSParser::T__5);
   
  }
  catch (RecognitionException &e) {
    _errHandler->reportError(this, e);
    _localctx->exception = std::current_exception();
    _errHandler->recover(this, _localctx->exception);
  }

  return _localctx;
}

//----------------- IncludeStatementContext ------------------------------------------------------------------

CASSParser::IncludeStatementContext::IncludeStatementContext(ParserRuleContext *parent, size_t invokingState)
  : ParserRuleContext(parent, invokingState) {
}

tree::TerminalNode* CASSParser::IncludeStatementContext::STRING() {
  return getToken(CASSParser::STRING, 0);
}


size_t CASSParser::IncludeStatementContext::getRuleIndex() const {
  return CASSParser::RuleIncludeStatement;
}

void CASSParser::IncludeStatementContext::enterRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->enterIncludeStatement(this);
}

void CASSParser::IncludeStatementContext::exitRule(tree::ParseTreeListener *listener) {
  auto parserListener = dynamic_cast<CASSListener *>(listener);
  if (parserListener != nullptr)
    parserListener->exitIncludeStatement(this);
}

CASSParser::IncludeStatementContext* CASSParser::includeStatement() {
  IncludeStatementContext *_localctx = _tracker.createInstance<IncludeStatementContext>(_ctx, getState());
  enterRule(_localctx, 34, CASSParser::RuleIncludeStatement);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(233);
    match(CASSParser::T__12);
    setState(234);
    match(CASSParser::STRING);
   
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
  enterRule(_localctx, 36, CASSParser::RuleParameterList);
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
    setState(236);
    parameter();
    setState(241);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CASSParser::T__10) {
      setState(237);
      match(CASSParser::T__10);
      setState(238);
      parameter();
      setState(243);
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
  enterRule(_localctx, 38, CASSParser::RuleParameter);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(244);
    typeSpec();
    setState(245);
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
  enterRule(_localctx, 40, CASSParser::RuleTypeSpec);
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
    setState(247);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 114688) != 0))) {
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
  enterRule(_localctx, 42, CASSParser::RuleExpression);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    enterOuterAlt(_localctx, 1);
    setState(249);
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
  enterRule(_localctx, 44, CASSParser::RuleAssignmentExpression);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(256);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 21, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(251);
      unaryExpression();
      setState(252);
      assignmentOperator();
      setState(253);
      assignmentExpression();
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(255);
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
  enterRule(_localctx, 46, CASSParser::RuleUnaryExpression);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(263);
    _errHandler->sync(this);
    switch (_input->LA(1)) {
      case CASSParser::T__16: {
        enterOuterAlt(_localctx, 1);
        setState(258);
        match(CASSParser::T__16);
        setState(259);
        unaryExpression();
        break;
      }

      case CASSParser::T__17: {
        enterOuterAlt(_localctx, 2);
        setState(260);
        match(CASSParser::T__17);
        setState(261);
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
        setState(262);
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
  enterRule(_localctx, 48, CASSParser::RulePrimaryExpression);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(275);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 23, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(265);
      match(CASSParser::ID);
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(266);
      match(CASSParser::INT);
      break;
    }

    case 3: {
      enterOuterAlt(_localctx, 3);
      setState(267);
      match(CASSParser::FLOAT);
      break;
    }

    case 4: {
      enterOuterAlt(_localctx, 4);
      setState(268);
      match(CASSParser::CHAR);
      break;
    }

    case 5: {
      enterOuterAlt(_localctx, 5);
      setState(269);
      match(CASSParser::STRING);
      break;
    }

    case 6: {
      enterOuterAlt(_localctx, 6);
      setState(270);
      functionCall();
      break;
    }

    case 7: {
      enterOuterAlt(_localctx, 7);
      setState(271);
      match(CASSParser::T__0);
      setState(272);
      expression();
      setState(273);
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
  enterRule(_localctx, 50, CASSParser::RuleAssignmentOperator);
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
    setState(277);
    _la = _input->LA(1);
    if (!((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 7864352) != 0))) {
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
  enterRule(_localctx, 52, CASSParser::RuleLogicalOrExpression);
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
    setState(279);
    logicalAndExpression();
    setState(284);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CASSParser::T__22) {
      setState(280);
      match(CASSParser::T__22);
      setState(281);
      logicalAndExpression();
      setState(286);
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
  enterRule(_localctx, 54, CASSParser::RuleLogicalAndExpression);
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
    setState(287);
    equalityExpression();
    setState(292);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CASSParser::T__23) {
      setState(288);
      match(CASSParser::T__23);
      setState(289);
      equalityExpression();
      setState(294);
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
  enterRule(_localctx, 56, CASSParser::RuleEqualityExpression);
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
    setState(295);
    relationalExpression();
    setState(300);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CASSParser::T__24

    || _la == CASSParser::T__25) {
      setState(296);
      _la = _input->LA(1);
      if (!(_la == CASSParser::T__24

      || _la == CASSParser::T__25)) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
      setState(297);
      relationalExpression();
      setState(302);
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
  enterRule(_localctx, 58, CASSParser::RuleRelationalExpression);
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
    setState(303);
    additiveExpression();
    setState(308);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 2013265920) != 0)) {
      setState(304);
      _la = _input->LA(1);
      if (!((((_la & ~ 0x3fULL) == 0) &&
        ((1ULL << _la) & 2013265920) != 0))) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
      setState(305);
      additiveExpression();
      setState(310);
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
  enterRule(_localctx, 60, CASSParser::RuleAdditiveExpression);
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
    setState(311);
    multiplicativeExpression();
    setState(316);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while (_la == CASSParser::T__30

    || _la == CASSParser::T__31) {
      setState(312);
      _la = _input->LA(1);
      if (!(_la == CASSParser::T__30

      || _la == CASSParser::T__31)) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
      setState(313);
      multiplicativeExpression();
      setState(318);
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
  enterRule(_localctx, 62, CASSParser::RuleMultiplicativeExpression);
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
    setState(319);
    unaryExpression();
    setState(324);
    _errHandler->sync(this);
    _la = _input->LA(1);
    while ((((_la & ~ 0x3fULL) == 0) &&
      ((1ULL << _la) & 60129542144) != 0)) {
      setState(320);
      _la = _input->LA(1);
      if (!((((_la & ~ 0x3fULL) == 0) &&
        ((1ULL << _la) & 60129542144) != 0))) {
      _errHandler->recoverInline(this);
      }
      else {
        _errHandler->reportMatch(this);
        consume();
      }
      setState(321);
      unaryExpression();
      setState(326);
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
  enterRule(_localctx, 64, CASSParser::RuleOperationExpression);

#if __cplusplus > 201703L
  auto onExit = finally([=, this] {
#else
  auto onExit = finally([=] {
#endif
    exitRule();
  });
  try {
    setState(329);
    _errHandler->sync(this);
    switch (getInterpreter<atn::ParserATNSimulator>()->adaptivePredict(_input, 30, _ctx)) {
    case 1: {
      enterOuterAlt(_localctx, 1);
      setState(327);
      additiveExpression();
      break;
    }

    case 2: {
      enterOuterAlt(_localctx, 2);
      setState(328);
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
