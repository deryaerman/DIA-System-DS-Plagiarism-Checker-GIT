
// Generated from CASS.g4 by ANTLR 4.13.2


#include "CASSLexer.h"


using namespace antlr4;



using namespace antlr4;

namespace {

struct CASSLexerStaticData final {
  CASSLexerStaticData(std::vector<std::string> ruleNames,
                          std::vector<std::string> channelNames,
                          std::vector<std::string> modeNames,
                          std::vector<std::string> literalNames,
                          std::vector<std::string> symbolicNames)
      : ruleNames(std::move(ruleNames)), channelNames(std::move(channelNames)),
        modeNames(std::move(modeNames)), literalNames(std::move(literalNames)),
        symbolicNames(std::move(symbolicNames)),
        vocabulary(this->literalNames, this->symbolicNames) {}

  CASSLexerStaticData(const CASSLexerStaticData&) = delete;
  CASSLexerStaticData(CASSLexerStaticData&&) = delete;
  CASSLexerStaticData& operator=(const CASSLexerStaticData&) = delete;
  CASSLexerStaticData& operator=(CASSLexerStaticData&&) = delete;

  std::vector<antlr4::dfa::DFA> decisionToDFA;
  antlr4::atn::PredictionContextCache sharedContextCache;
  const std::vector<std::string> ruleNames;
  const std::vector<std::string> channelNames;
  const std::vector<std::string> modeNames;
  const std::vector<std::string> literalNames;
  const std::vector<std::string> symbolicNames;
  const antlr4::dfa::Vocabulary vocabulary;
  antlr4::atn::SerializedATNView serializedATN;
  std::unique_ptr<antlr4::atn::ATN> atn;
};

::antlr4::internal::OnceFlag casslexerLexerOnceFlag;
#if ANTLR4_USE_THREAD_LOCAL_CACHE
static thread_local
#endif
std::unique_ptr<CASSLexerStaticData> casslexerLexerStaticData = nullptr;

void casslexerLexerInitialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  if (casslexerLexerStaticData != nullptr) {
    return;
  }
#else
  assert(casslexerLexerStaticData == nullptr);
#endif
  auto staticData = std::make_unique<CASSLexerStaticData>(
    std::vector<std::string>{
      "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", "T__7", "T__8", 
      "T__9", "T__10", "T__11", "T__12", "T__13", "T__14", "T__15", "T__16", 
      "T__17", "T__18", "T__19", "T__20", "T__21", "T__22", "T__23", "T__24", 
      "T__25", "T__26", "T__27", "ID", "INT", "WS"
    },
    std::vector<std::string>{
      "DEFAULT_TOKEN_CHANNEL", "HIDDEN"
    },
    std::vector<std::string>{
      "DEFAULT_MODE"
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
  	4,0,31,159,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
  	6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,2,14,
  	7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,7,20,2,21,
  	7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,2,27,7,27,2,28,
  	7,28,2,29,7,29,2,30,7,30,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,
  	1,5,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,
  	9,1,10,1,10,1,10,1,11,1,11,1,11,1,12,1,12,1,12,1,13,1,13,1,13,1,14,1,
  	14,1,14,1,15,1,15,1,15,1,16,1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,18,1,
  	19,1,19,1,19,1,20,1,20,1,21,1,21,1,22,1,22,1,22,1,23,1,23,1,23,1,24,1,
  	24,1,25,1,25,1,26,1,26,1,27,1,27,1,28,1,28,5,28,143,8,28,10,28,12,28,
  	146,9,28,1,29,4,29,149,8,29,11,29,12,29,150,1,30,4,30,154,8,30,11,30,
  	12,30,155,1,30,1,30,0,0,31,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,
  	10,21,11,23,12,25,13,27,14,29,15,31,16,33,17,35,18,37,19,39,20,41,21,
  	43,22,45,23,47,24,49,25,51,26,53,27,55,28,57,29,59,30,61,31,1,0,4,3,0,
  	65,90,95,95,97,122,4,0,48,57,65,90,95,95,97,122,1,0,48,57,3,0,9,10,13,
  	13,32,32,161,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,
  	0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,
  	0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,
  	1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,
  	0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,
  	0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,1,63,
  	1,0,0,0,3,65,1,0,0,0,5,67,1,0,0,0,7,69,1,0,0,0,9,71,1,0,0,0,11,73,1,0,
  	0,0,13,75,1,0,0,0,15,79,1,0,0,0,17,86,1,0,0,0,19,88,1,0,0,0,21,92,1,0,
  	0,0,23,95,1,0,0,0,25,98,1,0,0,0,27,101,1,0,0,0,29,104,1,0,0,0,31,107,
  	1,0,0,0,33,110,1,0,0,0,35,113,1,0,0,0,37,116,1,0,0,0,39,119,1,0,0,0,41,
  	122,1,0,0,0,43,124,1,0,0,0,45,126,1,0,0,0,47,129,1,0,0,0,49,132,1,0,0,
  	0,51,134,1,0,0,0,53,136,1,0,0,0,55,138,1,0,0,0,57,140,1,0,0,0,59,148,
  	1,0,0,0,61,153,1,0,0,0,63,64,5,40,0,0,64,2,1,0,0,0,65,66,5,41,0,0,66,
  	4,1,0,0,0,67,68,5,123,0,0,68,6,1,0,0,0,69,70,5,125,0,0,70,8,1,0,0,0,71,
  	72,5,61,0,0,72,10,1,0,0,0,73,74,5,59,0,0,74,12,1,0,0,0,75,76,5,102,0,
  	0,76,77,5,111,0,0,77,78,5,114,0,0,78,14,1,0,0,0,79,80,5,114,0,0,80,81,
  	5,101,0,0,81,82,5,116,0,0,82,83,5,117,0,0,83,84,5,114,0,0,84,85,5,110,
  	0,0,85,16,1,0,0,0,86,87,5,44,0,0,87,18,1,0,0,0,88,89,5,105,0,0,89,90,
  	5,110,0,0,90,91,5,116,0,0,91,20,1,0,0,0,92,93,5,43,0,0,93,94,5,43,0,0,
  	94,22,1,0,0,0,95,96,5,45,0,0,96,97,5,45,0,0,97,24,1,0,0,0,98,99,5,43,
  	0,0,99,100,5,61,0,0,100,26,1,0,0,0,101,102,5,45,0,0,102,103,5,61,0,0,
  	103,28,1,0,0,0,104,105,5,42,0,0,105,106,5,61,0,0,106,30,1,0,0,0,107,108,
  	5,47,0,0,108,109,5,61,0,0,109,32,1,0,0,0,110,111,5,124,0,0,111,112,5,
  	124,0,0,112,34,1,0,0,0,113,114,5,38,0,0,114,115,5,38,0,0,115,36,1,0,0,
  	0,116,117,5,61,0,0,117,118,5,61,0,0,118,38,1,0,0,0,119,120,5,33,0,0,120,
  	121,5,61,0,0,121,40,1,0,0,0,122,123,5,60,0,0,123,42,1,0,0,0,124,125,5,
  	62,0,0,125,44,1,0,0,0,126,127,5,60,0,0,127,128,5,61,0,0,128,46,1,0,0,
  	0,129,130,5,62,0,0,130,131,5,61,0,0,131,48,1,0,0,0,132,133,5,43,0,0,133,
  	50,1,0,0,0,134,135,5,45,0,0,135,52,1,0,0,0,136,137,5,42,0,0,137,54,1,
  	0,0,0,138,139,5,47,0,0,139,56,1,0,0,0,140,144,7,0,0,0,141,143,7,1,0,0,
  	142,141,1,0,0,0,143,146,1,0,0,0,144,142,1,0,0,0,144,145,1,0,0,0,145,58,
  	1,0,0,0,146,144,1,0,0,0,147,149,7,2,0,0,148,147,1,0,0,0,149,150,1,0,0,
  	0,150,148,1,0,0,0,150,151,1,0,0,0,151,60,1,0,0,0,152,154,7,3,0,0,153,
  	152,1,0,0,0,154,155,1,0,0,0,155,153,1,0,0,0,155,156,1,0,0,0,156,157,1,
  	0,0,0,157,158,6,30,0,0,158,62,1,0,0,0,4,0,144,150,155,1,6,0,0
  };
  staticData->serializedATN = antlr4::atn::SerializedATNView(serializedATNSegment, sizeof(serializedATNSegment) / sizeof(serializedATNSegment[0]));

  antlr4::atn::ATNDeserializer deserializer;
  staticData->atn = deserializer.deserialize(staticData->serializedATN);

  const size_t count = staticData->atn->getNumberOfDecisions();
  staticData->decisionToDFA.reserve(count);
  for (size_t i = 0; i < count; i++) { 
    staticData->decisionToDFA.emplace_back(staticData->atn->getDecisionState(i), i);
  }
  casslexerLexerStaticData = std::move(staticData);
}

}

CASSLexer::CASSLexer(CharStream *input) : Lexer(input) {
  CASSLexer::initialize();
  _interpreter = new atn::LexerATNSimulator(this, *casslexerLexerStaticData->atn, casslexerLexerStaticData->decisionToDFA, casslexerLexerStaticData->sharedContextCache);
}

CASSLexer::~CASSLexer() {
  delete _interpreter;
}

std::string CASSLexer::getGrammarFileName() const {
  return "CASS.g4";
}

const std::vector<std::string>& CASSLexer::getRuleNames() const {
  return casslexerLexerStaticData->ruleNames;
}

const std::vector<std::string>& CASSLexer::getChannelNames() const {
  return casslexerLexerStaticData->channelNames;
}

const std::vector<std::string>& CASSLexer::getModeNames() const {
  return casslexerLexerStaticData->modeNames;
}

const dfa::Vocabulary& CASSLexer::getVocabulary() const {
  return casslexerLexerStaticData->vocabulary;
}

antlr4::atn::SerializedATNView CASSLexer::getSerializedATN() const {
  return casslexerLexerStaticData->serializedATN;
}

const atn::ATN& CASSLexer::getATN() const {
  return *casslexerLexerStaticData->atn;
}




void CASSLexer::initialize() {
#if ANTLR4_USE_THREAD_LOCAL_CACHE
  casslexerLexerInitialize();
#else
  ::antlr4::internal::call_once(casslexerLexerOnceFlag, casslexerLexerInitialize);
#endif
}
