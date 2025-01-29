# Generated from CASS.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,45,321,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        4,0,68,8,0,11,0,12,0,69,1,0,1,0,1,1,1,1,1,1,1,1,3,1,78,8,1,1,1,1,
        1,1,1,1,2,1,2,5,2,85,8,2,10,2,12,2,88,9,2,1,2,1,2,1,3,1,3,1,3,1,
        3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,103,8,3,1,4,1,4,1,4,1,4,3,4,109,
        8,4,1,4,3,4,112,8,4,1,5,1,5,1,5,3,5,117,8,5,1,5,1,5,3,5,121,8,5,
        3,5,123,8,5,1,5,1,5,3,5,127,8,5,1,5,1,5,3,5,131,8,5,1,5,1,5,1,5,
        1,6,1,6,1,6,3,6,139,8,6,1,6,1,6,3,6,143,8,6,3,6,145,8,6,1,6,1,6,
        3,6,149,8,6,1,6,1,6,3,6,153,8,6,1,6,1,6,1,6,1,7,1,7,1,8,1,8,1,8,
        1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,
        1,10,3,10,179,8,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,3,11,188,8,
        11,1,12,1,12,1,12,3,12,193,8,12,1,12,1,12,1,13,1,13,1,13,5,13,200,
        8,13,10,13,12,13,203,9,13,1,14,1,14,3,14,207,8,14,1,14,1,14,1,15,
        1,15,1,15,1,16,1,16,1,16,1,17,1,17,1,17,5,17,220,8,17,10,17,12,17,
        223,9,17,1,18,1,18,1,18,1,19,1,19,1,20,1,20,1,21,1,21,1,21,1,21,
        1,21,3,21,237,8,21,1,22,1,22,1,22,1,22,3,22,243,8,22,1,22,1,22,5,
        22,247,8,22,10,22,12,22,250,9,22,1,23,1,23,1,24,1,24,1,24,1,24,1,
        24,1,24,1,24,1,24,1,24,1,24,1,24,3,24,265,8,24,1,25,1,25,1,26,1,
        26,1,26,5,26,272,8,26,10,26,12,26,275,9,26,1,27,1,27,1,27,5,27,280,
        8,27,10,27,12,27,283,9,27,1,28,1,28,1,28,5,28,288,8,28,10,28,12,
        28,291,9,28,1,29,1,29,1,29,5,29,296,8,29,10,29,12,29,299,9,29,1,
        30,1,30,1,30,5,30,304,8,30,10,30,12,30,307,9,30,1,31,1,31,1,31,5,
        31,312,8,31,10,31,12,31,315,9,31,1,32,1,32,3,32,319,8,32,1,32,0,
        1,44,33,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,
        42,44,46,48,50,52,54,56,58,60,62,64,0,7,1,0,14,17,1,0,18,19,1,0,
        20,23,2,0,5,5,24,27,1,0,30,31,1,0,32,33,1,0,34,36,337,0,67,1,0,0,
        0,2,73,1,0,0,0,4,82,1,0,0,0,6,102,1,0,0,0,8,104,1,0,0,0,10,113,1,
        0,0,0,12,135,1,0,0,0,14,157,1,0,0,0,16,159,1,0,0,0,18,165,1,0,0,
        0,20,171,1,0,0,0,22,180,1,0,0,0,24,189,1,0,0,0,26,196,1,0,0,0,28,
        204,1,0,0,0,30,210,1,0,0,0,32,213,1,0,0,0,34,216,1,0,0,0,36,224,
        1,0,0,0,38,227,1,0,0,0,40,229,1,0,0,0,42,236,1,0,0,0,44,242,1,0,
        0,0,46,251,1,0,0,0,48,264,1,0,0,0,50,266,1,0,0,0,52,268,1,0,0,0,
        54,276,1,0,0,0,56,284,1,0,0,0,58,292,1,0,0,0,60,300,1,0,0,0,62,308,
        1,0,0,0,64,318,1,0,0,0,66,68,3,6,3,0,67,66,1,0,0,0,68,69,1,0,0,0,
        69,67,1,0,0,0,69,70,1,0,0,0,70,71,1,0,0,0,71,72,5,0,0,1,72,1,1,0,
        0,0,73,74,3,38,19,0,74,75,3,48,24,0,75,77,5,1,0,0,76,78,3,34,17,
        0,77,76,1,0,0,0,77,78,1,0,0,0,78,79,1,0,0,0,79,80,5,2,0,0,80,81,
        3,4,2,0,81,3,1,0,0,0,82,86,5,3,0,0,83,85,3,6,3,0,84,83,1,0,0,0,85,
        88,1,0,0,0,86,84,1,0,0,0,86,87,1,0,0,0,87,89,1,0,0,0,88,86,1,0,0,
        0,89,90,5,4,0,0,90,5,1,0,0,0,91,103,3,8,4,0,92,103,3,10,5,0,93,103,
        3,12,6,0,94,103,3,16,8,0,95,103,3,18,9,0,96,103,3,20,10,0,97,103,
        3,22,11,0,98,103,3,28,14,0,99,103,3,30,15,0,100,103,3,2,1,0,101,
        103,3,32,16,0,102,91,1,0,0,0,102,92,1,0,0,0,102,93,1,0,0,0,102,94,
        1,0,0,0,102,95,1,0,0,0,102,96,1,0,0,0,102,97,1,0,0,0,102,98,1,0,
        0,0,102,99,1,0,0,0,102,100,1,0,0,0,102,101,1,0,0,0,103,7,1,0,0,0,
        104,105,3,38,19,0,105,108,3,48,24,0,106,107,5,5,0,0,107,109,3,40,
        20,0,108,106,1,0,0,0,108,109,1,0,0,0,109,111,1,0,0,0,110,112,5,6,
        0,0,111,110,1,0,0,0,111,112,1,0,0,0,112,9,1,0,0,0,113,114,5,7,0,
        0,114,122,5,1,0,0,115,117,3,8,4,0,116,115,1,0,0,0,116,117,1,0,0,
        0,117,123,1,0,0,0,118,123,1,0,0,0,119,121,3,42,21,0,120,119,1,0,
        0,0,120,121,1,0,0,0,121,123,1,0,0,0,122,116,1,0,0,0,122,118,1,0,
        0,0,122,120,1,0,0,0,123,124,1,0,0,0,124,126,5,6,0,0,125,127,3,52,
        26,0,126,125,1,0,0,0,126,127,1,0,0,0,127,128,1,0,0,0,128,130,5,6,
        0,0,129,131,3,44,22,0,130,129,1,0,0,0,130,131,1,0,0,0,131,132,1,
        0,0,0,132,133,5,2,0,0,133,134,3,4,2,0,134,11,1,0,0,0,135,136,5,7,
        0,0,136,144,5,1,0,0,137,139,3,8,4,0,138,137,1,0,0,0,138,139,1,0,
        0,0,139,145,1,0,0,0,140,145,1,0,0,0,141,143,3,42,21,0,142,141,1,
        0,0,0,142,143,1,0,0,0,143,145,1,0,0,0,144,138,1,0,0,0,144,140,1,
        0,0,0,144,142,1,0,0,0,145,146,1,0,0,0,146,148,5,6,0,0,147,149,3,
        52,26,0,148,147,1,0,0,0,148,149,1,0,0,0,149,150,1,0,0,0,150,152,
        5,6,0,0,151,153,3,44,22,0,152,151,1,0,0,0,152,153,1,0,0,0,153,154,
        1,0,0,0,154,155,5,2,0,0,155,156,3,6,3,0,156,13,1,0,0,0,157,158,3,
        52,26,0,158,15,1,0,0,0,159,160,5,8,0,0,160,161,5,1,0,0,161,162,3,
        14,7,0,162,163,5,2,0,0,163,164,3,4,2,0,164,17,1,0,0,0,165,166,5,
        8,0,0,166,167,5,1,0,0,167,168,3,14,7,0,168,169,5,2,0,0,169,170,3,
        6,3,0,170,19,1,0,0,0,171,172,5,9,0,0,172,173,5,1,0,0,173,174,3,14,
        7,0,174,175,5,2,0,0,175,178,3,4,2,0,176,177,5,10,0,0,177,179,3,4,
        2,0,178,176,1,0,0,0,178,179,1,0,0,0,179,21,1,0,0,0,180,181,5,9,0,
        0,181,182,5,1,0,0,182,183,3,14,7,0,183,184,5,2,0,0,184,187,3,6,3,
        0,185,186,5,10,0,0,186,188,3,6,3,0,187,185,1,0,0,0,187,188,1,0,0,
        0,188,23,1,0,0,0,189,190,5,39,0,0,190,192,5,1,0,0,191,193,3,26,13,
        0,192,191,1,0,0,0,192,193,1,0,0,0,193,194,1,0,0,0,194,195,5,2,0,
        0,195,25,1,0,0,0,196,201,3,40,20,0,197,198,5,11,0,0,198,200,3,40,
        20,0,199,197,1,0,0,0,200,203,1,0,0,0,201,199,1,0,0,0,201,202,1,0,
        0,0,202,27,1,0,0,0,203,201,1,0,0,0,204,206,5,12,0,0,205,207,3,40,
        20,0,206,205,1,0,0,0,206,207,1,0,0,0,207,208,1,0,0,0,208,209,5,6,
        0,0,209,29,1,0,0,0,210,211,3,40,20,0,211,212,5,6,0,0,212,31,1,0,
        0,0,213,214,5,13,0,0,214,215,5,44,0,0,215,33,1,0,0,0,216,221,3,36,
        18,0,217,218,5,11,0,0,218,220,3,36,18,0,219,217,1,0,0,0,220,223,
        1,0,0,0,221,219,1,0,0,0,221,222,1,0,0,0,222,35,1,0,0,0,223,221,1,
        0,0,0,224,225,3,38,19,0,225,226,3,48,24,0,226,37,1,0,0,0,227,228,
        7,0,0,0,228,39,1,0,0,0,229,230,3,42,21,0,230,41,1,0,0,0,231,232,
        3,44,22,0,232,233,3,50,25,0,233,234,3,42,21,0,234,237,1,0,0,0,235,
        237,3,52,26,0,236,231,1,0,0,0,236,235,1,0,0,0,237,43,1,0,0,0,238,
        239,6,22,-1,0,239,240,7,1,0,0,240,243,3,44,22,3,241,243,3,48,24,
        0,242,238,1,0,0,0,242,241,1,0,0,0,243,248,1,0,0,0,244,245,10,2,0,
        0,245,247,7,1,0,0,246,244,1,0,0,0,247,250,1,0,0,0,248,246,1,0,0,
        0,248,249,1,0,0,0,249,45,1,0,0,0,250,248,1,0,0,0,251,252,7,2,0,0,
        252,47,1,0,0,0,253,265,5,39,0,0,254,265,5,40,0,0,255,265,5,42,0,
        0,256,265,5,43,0,0,257,265,5,44,0,0,258,265,5,41,0,0,259,265,3,24,
        12,0,260,261,5,1,0,0,261,262,3,40,20,0,262,263,5,2,0,0,263,265,1,
        0,0,0,264,253,1,0,0,0,264,254,1,0,0,0,264,255,1,0,0,0,264,256,1,
        0,0,0,264,257,1,0,0,0,264,258,1,0,0,0,264,259,1,0,0,0,264,260,1,
        0,0,0,265,49,1,0,0,0,266,267,7,3,0,0,267,51,1,0,0,0,268,273,3,54,
        27,0,269,270,5,28,0,0,270,272,3,54,27,0,271,269,1,0,0,0,272,275,
        1,0,0,0,273,271,1,0,0,0,273,274,1,0,0,0,274,53,1,0,0,0,275,273,1,
        0,0,0,276,281,3,56,28,0,277,278,5,29,0,0,278,280,3,56,28,0,279,277,
        1,0,0,0,280,283,1,0,0,0,281,279,1,0,0,0,281,282,1,0,0,0,282,55,1,
        0,0,0,283,281,1,0,0,0,284,289,3,58,29,0,285,286,7,4,0,0,286,288,
        3,58,29,0,287,285,1,0,0,0,288,291,1,0,0,0,289,287,1,0,0,0,289,290,
        1,0,0,0,290,57,1,0,0,0,291,289,1,0,0,0,292,297,3,60,30,0,293,294,
        7,2,0,0,294,296,3,60,30,0,295,293,1,0,0,0,296,299,1,0,0,0,297,295,
        1,0,0,0,297,298,1,0,0,0,298,59,1,0,0,0,299,297,1,0,0,0,300,305,3,
        62,31,0,301,302,7,5,0,0,302,304,3,62,31,0,303,301,1,0,0,0,304,307,
        1,0,0,0,305,303,1,0,0,0,305,306,1,0,0,0,306,61,1,0,0,0,307,305,1,
        0,0,0,308,313,3,44,22,0,309,310,7,6,0,0,310,312,3,44,22,0,311,309,
        1,0,0,0,312,315,1,0,0,0,313,311,1,0,0,0,313,314,1,0,0,0,314,63,1,
        0,0,0,315,313,1,0,0,0,316,319,3,60,30,0,317,319,3,62,31,0,318,316,
        1,0,0,0,318,317,1,0,0,0,319,65,1,0,0,0,33,69,77,86,102,108,111,116,
        120,122,126,130,138,142,144,148,152,178,187,192,201,206,221,236,
        242,248,264,273,281,289,297,305,313,318
    ]

class CASSParser ( Parser ):

    grammarFileName = "CASS.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "'='", "';'", 
                     "'for'", "'while'", "'if'", "'else'", "','", "'return'", 
                     "'include'", "'int'", "'float'", "'double'", "'void'", 
                     "'++'", "'--'", "'>'", "'<'", "'<='", "'>='", "'+='", 
                     "'-='", "'*='", "'/='", "'||'", "'&&'", "'=='", "'!='", 
                     "'+'", "'-'", "'*'", "'/'", "'%'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "SL_COMMENT", "ML_COMMENT", "ID", "INT", 
                      "BOOL", "FLOAT", "CHAR", "STRING", "WS" ]

    RULE_prog = 0
    RULE_functionDefinition = 1
    RULE_compoundStatement = 2
    RULE_statement = 3
    RULE_declarationStatement = 4
    RULE_forBlockStatement = 5
    RULE_forSingleStatement = 6
    RULE_conditionClause = 7
    RULE_whileBlockStatement = 8
    RULE_whileSingleStatement = 9
    RULE_ifBlockStatement = 10
    RULE_ifSingleStatement = 11
    RULE_functionCall = 12
    RULE_argumentList = 13
    RULE_returnStatement = 14
    RULE_expressionStatement = 15
    RULE_includeStatement = 16
    RULE_parameterList = 17
    RULE_parameter = 18
    RULE_typeSpec = 19
    RULE_expression = 20
    RULE_assignmentExpression = 21
    RULE_unaryExpression = 22
    RULE_comparingExpression = 23
    RULE_primaryExpression = 24
    RULE_assignmentOperator = 25
    RULE_logicalOrExpression = 26
    RULE_logicalAndExpression = 27
    RULE_equalityExpression = 28
    RULE_relationalExpression = 29
    RULE_additiveExpression = 30
    RULE_multiplicativeExpression = 31
    RULE_operationExpression = 32

    ruleNames =  [ "prog", "functionDefinition", "compoundStatement", "statement", 
                   "declarationStatement", "forBlockStatement", "forSingleStatement", 
                   "conditionClause", "whileBlockStatement", "whileSingleStatement", 
                   "ifBlockStatement", "ifSingleStatement", "functionCall", 
                   "argumentList", "returnStatement", "expressionStatement", 
                   "includeStatement", "parameterList", "parameter", "typeSpec", 
                   "expression", "assignmentExpression", "unaryExpression", 
                   "comparingExpression", "primaryExpression", "assignmentOperator", 
                   "logicalOrExpression", "logicalAndExpression", "equalityExpression", 
                   "relationalExpression", "additiveExpression", "multiplicativeExpression", 
                   "operationExpression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    T__25=26
    T__26=27
    T__27=28
    T__28=29
    T__29=30
    T__30=31
    T__31=32
    T__32=33
    T__33=34
    T__34=35
    T__35=36
    SL_COMMENT=37
    ML_COMMENT=38
    ID=39
    INT=40
    BOOL=41
    FLOAT=42
    CHAR=43
    STRING=44
    WS=45

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CASSParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CASSParser.StatementContext)
            else:
                return self.getTypedRuleContext(CASSParser.StatementContext,i)


        def getRuleIndex(self):
            return CASSParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProg" ):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = CASSParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 66
                self.statement()
                self.state = 69 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 34634617320322) != 0)):
                    break

            self.state = 71
            self.match(CASSParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpec(self):
            return self.getTypedRuleContext(CASSParser.TypeSpecContext,0)


        def primaryExpression(self):
            return self.getTypedRuleContext(CASSParser.PrimaryExpressionContext,0)


        def compoundStatement(self):
            return self.getTypedRuleContext(CASSParser.CompoundStatementContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(CASSParser.ParameterListContext,0)


        def getRuleIndex(self):
            return CASSParser.RULE_functionDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDefinition" ):
                listener.enterFunctionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDefinition" ):
                listener.exitFunctionDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDefinition" ):
                return visitor.visitFunctionDefinition(self)
            else:
                return visitor.visitChildren(self)




    def functionDefinition(self):

        localctx = CASSParser.FunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 73
            self.typeSpec()
            self.state = 74
            self.primaryExpression()
            self.state = 75
            self.match(CASSParser.T__0)
            self.state = 77
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 245760) != 0):
                self.state = 76
                self.parameterList()


            self.state = 79
            self.match(CASSParser.T__1)
            self.state = 80
            self.compoundStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompoundStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CASSParser.StatementContext)
            else:
                return self.getTypedRuleContext(CASSParser.StatementContext,i)


        def getRuleIndex(self):
            return CASSParser.RULE_compoundStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompoundStatement" ):
                listener.enterCompoundStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompoundStatement" ):
                listener.exitCompoundStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompoundStatement" ):
                return visitor.visitCompoundStatement(self)
            else:
                return visitor.visitChildren(self)




    def compoundStatement(self):

        localctx = CASSParser.CompoundStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_compoundStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(CASSParser.T__2)
            self.state = 86
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 34634617320322) != 0):
                self.state = 83
                self.statement()
                self.state = 88
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 89
            self.match(CASSParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declarationStatement(self):
            return self.getTypedRuleContext(CASSParser.DeclarationStatementContext,0)


        def forBlockStatement(self):
            return self.getTypedRuleContext(CASSParser.ForBlockStatementContext,0)


        def forSingleStatement(self):
            return self.getTypedRuleContext(CASSParser.ForSingleStatementContext,0)


        def whileBlockStatement(self):
            return self.getTypedRuleContext(CASSParser.WhileBlockStatementContext,0)


        def whileSingleStatement(self):
            return self.getTypedRuleContext(CASSParser.WhileSingleStatementContext,0)


        def ifBlockStatement(self):
            return self.getTypedRuleContext(CASSParser.IfBlockStatementContext,0)


        def ifSingleStatement(self):
            return self.getTypedRuleContext(CASSParser.IfSingleStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(CASSParser.ReturnStatementContext,0)


        def expressionStatement(self):
            return self.getTypedRuleContext(CASSParser.ExpressionStatementContext,0)


        def functionDefinition(self):
            return self.getTypedRuleContext(CASSParser.FunctionDefinitionContext,0)


        def includeStatement(self):
            return self.getTypedRuleContext(CASSParser.IncludeStatementContext,0)


        def getRuleIndex(self):
            return CASSParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = CASSParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_statement)
        try:
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 91
                self.declarationStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 92
                self.forBlockStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 93
                self.forSingleStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 94
                self.whileBlockStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 95
                self.whileSingleStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 96
                self.ifBlockStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 97
                self.ifSingleStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 98
                self.returnStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 99
                self.expressionStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 100
                self.functionDefinition()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 101
                self.includeStatement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclarationStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpec(self):
            return self.getTypedRuleContext(CASSParser.TypeSpecContext,0)


        def primaryExpression(self):
            return self.getTypedRuleContext(CASSParser.PrimaryExpressionContext,0)


        def expression(self):
            return self.getTypedRuleContext(CASSParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CASSParser.RULE_declarationStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclarationStatement" ):
                listener.enterDeclarationStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclarationStatement" ):
                listener.exitDeclarationStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclarationStatement" ):
                return visitor.visitDeclarationStatement(self)
            else:
                return visitor.visitChildren(self)




    def declarationStatement(self):

        localctx = CASSParser.DeclarationStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_declarationStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.typeSpec()
            self.state = 105
            self.primaryExpression()
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 106
                self.match(CASSParser.T__4)
                self.state = 107
                self.expression()


            self.state = 111
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 110
                self.match(CASSParser.T__5)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForBlockStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def compoundStatement(self):
            return self.getTypedRuleContext(CASSParser.CompoundStatementContext,0)


        def logicalOrExpression(self):
            return self.getTypedRuleContext(CASSParser.LogicalOrExpressionContext,0)


        def unaryExpression(self):
            return self.getTypedRuleContext(CASSParser.UnaryExpressionContext,0)


        def declarationStatement(self):
            return self.getTypedRuleContext(CASSParser.DeclarationStatementContext,0)


        def assignmentExpression(self):
            return self.getTypedRuleContext(CASSParser.AssignmentExpressionContext,0)


        def getRuleIndex(self):
            return CASSParser.RULE_forBlockStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForBlockStatement" ):
                listener.enterForBlockStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForBlockStatement" ):
                listener.exitForBlockStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForBlockStatement" ):
                return visitor.visitForBlockStatement(self)
            else:
                return visitor.visitChildren(self)




    def forBlockStatement(self):

        localctx = CASSParser.ForBlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_forBlockStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(CASSParser.T__6)
            self.state = 114
            self.match(CASSParser.T__0)
            self.state = 122
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 116
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 245760) != 0):
                    self.state = 115
                    self.declarationStatement()


                pass

            elif la_ == 2:
                pass

            elif la_ == 3:
                self.state = 120
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 34634617061378) != 0):
                    self.state = 119
                    self.assignmentExpression()


                pass


            self.state = 124
            self.match(CASSParser.T__5)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 34634617061378) != 0):
                self.state = 125
                self.logicalOrExpression()


            self.state = 128
            self.match(CASSParser.T__5)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 34634617061378) != 0):
                self.state = 129
                self.unaryExpression(0)


            self.state = 132
            self.match(CASSParser.T__1)
            self.state = 133
            self.compoundStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForSingleStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(CASSParser.StatementContext,0)


        def logicalOrExpression(self):
            return self.getTypedRuleContext(CASSParser.LogicalOrExpressionContext,0)


        def unaryExpression(self):
            return self.getTypedRuleContext(CASSParser.UnaryExpressionContext,0)


        def declarationStatement(self):
            return self.getTypedRuleContext(CASSParser.DeclarationStatementContext,0)


        def assignmentExpression(self):
            return self.getTypedRuleContext(CASSParser.AssignmentExpressionContext,0)


        def getRuleIndex(self):
            return CASSParser.RULE_forSingleStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForSingleStatement" ):
                listener.enterForSingleStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForSingleStatement" ):
                listener.exitForSingleStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForSingleStatement" ):
                return visitor.visitForSingleStatement(self)
            else:
                return visitor.visitChildren(self)




    def forSingleStatement(self):

        localctx = CASSParser.ForSingleStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_forSingleStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(CASSParser.T__6)
            self.state = 136
            self.match(CASSParser.T__0)
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 245760) != 0):
                    self.state = 137
                    self.declarationStatement()


                pass

            elif la_ == 2:
                pass

            elif la_ == 3:
                self.state = 142
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & 34634617061378) != 0):
                    self.state = 141
                    self.assignmentExpression()


                pass


            self.state = 146
            self.match(CASSParser.T__5)
            self.state = 148
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 34634617061378) != 0):
                self.state = 147
                self.logicalOrExpression()


            self.state = 150
            self.match(CASSParser.T__5)
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 34634617061378) != 0):
                self.state = 151
                self.unaryExpression(0)


            self.state = 154
            self.match(CASSParser.T__1)
            self.state = 155
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalOrExpression(self):
            return self.getTypedRuleContext(CASSParser.LogicalOrExpressionContext,0)


        def getRuleIndex(self):
            return CASSParser.RULE_conditionClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditionClause" ):
                listener.enterConditionClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditionClause" ):
                listener.exitConditionClause(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditionClause" ):
                return visitor.visitConditionClause(self)
            else:
                return visitor.visitChildren(self)




    def conditionClause(self):

        localctx = CASSParser.ConditionClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_conditionClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.logicalOrExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileBlockStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionClause(self):
            return self.getTypedRuleContext(CASSParser.ConditionClauseContext,0)


        def compoundStatement(self):
            return self.getTypedRuleContext(CASSParser.CompoundStatementContext,0)


        def getRuleIndex(self):
            return CASSParser.RULE_whileBlockStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileBlockStatement" ):
                listener.enterWhileBlockStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileBlockStatement" ):
                listener.exitWhileBlockStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileBlockStatement" ):
                return visitor.visitWhileBlockStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileBlockStatement(self):

        localctx = CASSParser.WhileBlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_whileBlockStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self.match(CASSParser.T__7)
            self.state = 160
            self.match(CASSParser.T__0)
            self.state = 161
            self.conditionClause()
            self.state = 162
            self.match(CASSParser.T__1)
            self.state = 163
            self.compoundStatement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileSingleStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionClause(self):
            return self.getTypedRuleContext(CASSParser.ConditionClauseContext,0)


        def statement(self):
            return self.getTypedRuleContext(CASSParser.StatementContext,0)


        def getRuleIndex(self):
            return CASSParser.RULE_whileSingleStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileSingleStatement" ):
                listener.enterWhileSingleStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileSingleStatement" ):
                listener.exitWhileSingleStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileSingleStatement" ):
                return visitor.visitWhileSingleStatement(self)
            else:
                return visitor.visitChildren(self)




    def whileSingleStatement(self):

        localctx = CASSParser.WhileSingleStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_whileSingleStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.match(CASSParser.T__7)
            self.state = 166
            self.match(CASSParser.T__0)
            self.state = 167
            self.conditionClause()
            self.state = 168
            self.match(CASSParser.T__1)
            self.state = 169
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfBlockStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionClause(self):
            return self.getTypedRuleContext(CASSParser.ConditionClauseContext,0)


        def compoundStatement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CASSParser.CompoundStatementContext)
            else:
                return self.getTypedRuleContext(CASSParser.CompoundStatementContext,i)


        def getRuleIndex(self):
            return CASSParser.RULE_ifBlockStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfBlockStatement" ):
                listener.enterIfBlockStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfBlockStatement" ):
                listener.exitIfBlockStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfBlockStatement" ):
                return visitor.visitIfBlockStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifBlockStatement(self):

        localctx = CASSParser.IfBlockStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_ifBlockStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(CASSParser.T__8)
            self.state = 172
            self.match(CASSParser.T__0)
            self.state = 173
            self.conditionClause()
            self.state = 174
            self.match(CASSParser.T__1)
            self.state = 175
            self.compoundStatement()
            self.state = 178
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 176
                self.match(CASSParser.T__9)
                self.state = 177
                self.compoundStatement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfSingleStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditionClause(self):
            return self.getTypedRuleContext(CASSParser.ConditionClauseContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CASSParser.StatementContext)
            else:
                return self.getTypedRuleContext(CASSParser.StatementContext,i)


        def getRuleIndex(self):
            return CASSParser.RULE_ifSingleStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfSingleStatement" ):
                listener.enterIfSingleStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfSingleStatement" ):
                listener.exitIfSingleStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfSingleStatement" ):
                return visitor.visitIfSingleStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifSingleStatement(self):

        localctx = CASSParser.IfSingleStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_ifSingleStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.match(CASSParser.T__8)
            self.state = 181
            self.match(CASSParser.T__0)
            self.state = 182
            self.conditionClause()
            self.state = 183
            self.match(CASSParser.T__1)
            self.state = 184
            self.statement()
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.state = 185
                self.match(CASSParser.T__9)
                self.state = 186
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CASSParser.ID, 0)

        def argumentList(self):
            return self.getTypedRuleContext(CASSParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return CASSParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = CASSParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(CASSParser.ID)
            self.state = 190
            self.match(CASSParser.T__0)
            self.state = 192
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 34634617061378) != 0):
                self.state = 191
                self.argumentList()


            self.state = 194
            self.match(CASSParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CASSParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CASSParser.ExpressionContext,i)


        def getRuleIndex(self):
            return CASSParser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = CASSParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.expression()
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 197
                self.match(CASSParser.T__10)
                self.state = 198
                self.expression()
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CASSParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CASSParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = CASSParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(CASSParser.T__11)
            self.state = 206
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 34634617061378) != 0):
                self.state = 205
                self.expression()


            self.state = 208
            self.match(CASSParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CASSParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CASSParser.RULE_expressionStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpressionStatement" ):
                listener.enterExpressionStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpressionStatement" ):
                listener.exitExpressionStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpressionStatement" ):
                return visitor.visitExpressionStatement(self)
            else:
                return visitor.visitChildren(self)




    def expressionStatement(self):

        localctx = CASSParser.ExpressionStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.expression()
            self.state = 211
            self.match(CASSParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncludeStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(CASSParser.STRING, 0)

        def getRuleIndex(self):
            return CASSParser.RULE_includeStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncludeStatement" ):
                listener.enterIncludeStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncludeStatement" ):
                listener.exitIncludeStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncludeStatement" ):
                return visitor.visitIncludeStatement(self)
            else:
                return visitor.visitChildren(self)




    def includeStatement(self):

        localctx = CASSParser.IncludeStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_includeStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.match(CASSParser.T__12)
            self.state = 214
            self.match(CASSParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CASSParser.ParameterContext)
            else:
                return self.getTypedRuleContext(CASSParser.ParameterContext,i)


        def getRuleIndex(self):
            return CASSParser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterList" ):
                return visitor.visitParameterList(self)
            else:
                return visitor.visitChildren(self)




    def parameterList(self):

        localctx = CASSParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.parameter()
            self.state = 221
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==11:
                self.state = 217
                self.match(CASSParser.T__10)
                self.state = 218
                self.parameter()
                self.state = 223
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpec(self):
            return self.getTypedRuleContext(CASSParser.TypeSpecContext,0)


        def primaryExpression(self):
            return self.getTypedRuleContext(CASSParser.PrimaryExpressionContext,0)


        def getRuleIndex(self):
            return CASSParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = CASSParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
            self.typeSpec()
            self.state = 225
            self.primaryExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSpecContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CASSParser.RULE_typeSpec

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSpec" ):
                listener.enterTypeSpec(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSpec" ):
                listener.exitTypeSpec(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeSpec" ):
                return visitor.visitTypeSpec(self)
            else:
                return visitor.visitChildren(self)




    def typeSpec(self):

        localctx = CASSParser.TypeSpecContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_typeSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 245760) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignmentExpression(self):
            return self.getTypedRuleContext(CASSParser.AssignmentExpressionContext,0)


        def getRuleIndex(self):
            return CASSParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = CASSParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.assignmentExpression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self):
            return self.getTypedRuleContext(CASSParser.UnaryExpressionContext,0)


        def assignmentOperator(self):
            return self.getTypedRuleContext(CASSParser.AssignmentOperatorContext,0)


        def assignmentExpression(self):
            return self.getTypedRuleContext(CASSParser.AssignmentExpressionContext,0)


        def logicalOrExpression(self):
            return self.getTypedRuleContext(CASSParser.LogicalOrExpressionContext,0)


        def getRuleIndex(self):
            return CASSParser.RULE_assignmentExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentExpression" ):
                listener.enterAssignmentExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentExpression" ):
                listener.exitAssignmentExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentExpression" ):
                return visitor.visitAssignmentExpression(self)
            else:
                return visitor.visitChildren(self)




    def assignmentExpression(self):

        localctx = CASSParser.AssignmentExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_assignmentExpression)
        try:
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.unaryExpression(0)
                self.state = 232
                self.assignmentOperator()
                self.state = 233
                self.assignmentExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.logicalOrExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UnaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self):
            return self.getTypedRuleContext(CASSParser.UnaryExpressionContext,0)


        def primaryExpression(self):
            return self.getTypedRuleContext(CASSParser.PrimaryExpressionContext,0)


        def getRuleIndex(self):
            return CASSParser.RULE_unaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryExpression" ):
                listener.enterUnaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryExpression" ):
                listener.exitUnaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUnaryExpression" ):
                return visitor.visitUnaryExpression(self)
            else:
                return visitor.visitChildren(self)



    def unaryExpression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CASSParser.UnaryExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_unaryExpression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [18, 19]:
                self.state = 239
                _la = self._input.LA(1)
                if not(_la==18 or _la==19):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 240
                self.unaryExpression(3)
                pass
            elif token in [1, 39, 40, 41, 42, 43, 44]:
                self.state = 241
                self.primaryExpression()
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 248
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CASSParser.UnaryExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_unaryExpression)
                    self.state = 244
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 245
                    _la = self._input.LA(1)
                    if not(_la==18 or _la==19):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume() 
                self.state = 250
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ComparingExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CASSParser.RULE_comparingExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparingExpression" ):
                listener.enterComparingExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparingExpression" ):
                listener.exitComparingExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparingExpression" ):
                return visitor.visitComparingExpression(self)
            else:
                return visitor.visitChildren(self)




    def comparingExpression(self):

        localctx = CASSParser.ComparingExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_comparingExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15728640) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PrimaryExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CASSParser.ID, 0)

        def INT(self):
            return self.getToken(CASSParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CASSParser.FLOAT, 0)

        def CHAR(self):
            return self.getToken(CASSParser.CHAR, 0)

        def STRING(self):
            return self.getToken(CASSParser.STRING, 0)

        def BOOL(self):
            return self.getToken(CASSParser.BOOL, 0)

        def functionCall(self):
            return self.getTypedRuleContext(CASSParser.FunctionCallContext,0)


        def expression(self):
            return self.getTypedRuleContext(CASSParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CASSParser.RULE_primaryExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimaryExpression" ):
                listener.enterPrimaryExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimaryExpression" ):
                listener.exitPrimaryExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimaryExpression" ):
                return visitor.visitPrimaryExpression(self)
            else:
                return visitor.visitChildren(self)




    def primaryExpression(self):

        localctx = CASSParser.PrimaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_primaryExpression)
        try:
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.match(CASSParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.match(CASSParser.INT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 255
                self.match(CASSParser.FLOAT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 256
                self.match(CASSParser.CHAR)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 257
                self.match(CASSParser.STRING)
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 258
                self.match(CASSParser.BOOL)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 259
                self.functionCall()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 260
                self.match(CASSParser.T__0)
                self.state = 261
                self.expression()
                self.state = 262
                self.match(CASSParser.T__1)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return CASSParser.RULE_assignmentOperator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignmentOperator" ):
                listener.enterAssignmentOperator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignmentOperator" ):
                listener.exitAssignmentOperator(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignmentOperator" ):
                return visitor.visitAssignmentOperator(self)
            else:
                return visitor.visitChildren(self)




    def assignmentOperator(self):

        localctx = CASSParser.AssignmentOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 251658272) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalOrExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalAndExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CASSParser.LogicalAndExpressionContext)
            else:
                return self.getTypedRuleContext(CASSParser.LogicalAndExpressionContext,i)


        def getRuleIndex(self):
            return CASSParser.RULE_logicalOrExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalOrExpression" ):
                listener.enterLogicalOrExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalOrExpression" ):
                listener.exitLogicalOrExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalOrExpression" ):
                return visitor.visitLogicalOrExpression(self)
            else:
                return visitor.visitChildren(self)




    def logicalOrExpression(self):

        localctx = CASSParser.LogicalOrExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_logicalOrExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 268
            self.logicalAndExpression()
            self.state = 273
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 269
                self.match(CASSParser.T__27)
                self.state = 270
                self.logicalAndExpression()
                self.state = 275
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalAndExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def equalityExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CASSParser.EqualityExpressionContext)
            else:
                return self.getTypedRuleContext(CASSParser.EqualityExpressionContext,i)


        def getRuleIndex(self):
            return CASSParser.RULE_logicalAndExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalAndExpression" ):
                listener.enterLogicalAndExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalAndExpression" ):
                listener.exitLogicalAndExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogicalAndExpression" ):
                return visitor.visitLogicalAndExpression(self)
            else:
                return visitor.visitChildren(self)




    def logicalAndExpression(self):

        localctx = CASSParser.LogicalAndExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_logicalAndExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.equalityExpression()
            self.state = 281
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 277
                self.match(CASSParser.T__28)
                self.state = 278
                self.equalityExpression()
                self.state = 283
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EqualityExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def relationalExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CASSParser.RelationalExpressionContext)
            else:
                return self.getTypedRuleContext(CASSParser.RelationalExpressionContext,i)


        def getRuleIndex(self):
            return CASSParser.RULE_equalityExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpression" ):
                listener.enterEqualityExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpression" ):
                listener.exitEqualityExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEqualityExpression" ):
                return visitor.visitEqualityExpression(self)
            else:
                return visitor.visitChildren(self)




    def equalityExpression(self):

        localctx = CASSParser.EqualityExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_equalityExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.relationalExpression()
            self.state = 289
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30 or _la==31:
                self.state = 285
                _la = self._input.LA(1)
                if not(_la==30 or _la==31):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 286
                self.relationalExpression()
                self.state = 291
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelationalExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CASSParser.AdditiveExpressionContext)
            else:
                return self.getTypedRuleContext(CASSParser.AdditiveExpressionContext,i)


        def getRuleIndex(self):
            return CASSParser.RULE_relationalExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpression" ):
                listener.enterRelationalExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpression" ):
                listener.exitRelationalExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelationalExpression" ):
                return visitor.visitRelationalExpression(self)
            else:
                return visitor.visitChildren(self)




    def relationalExpression(self):

        localctx = CASSParser.RelationalExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_relationalExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.additiveExpression()
            self.state = 297
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 15728640) != 0):
                self.state = 293
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15728640) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 294
                self.additiveExpression()
                self.state = 299
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AdditiveExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def multiplicativeExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CASSParser.MultiplicativeExpressionContext)
            else:
                return self.getTypedRuleContext(CASSParser.MultiplicativeExpressionContext,i)


        def getRuleIndex(self):
            return CASSParser.RULE_additiveExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)




    def additiveExpression(self):

        localctx = CASSParser.AdditiveExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.multiplicativeExpression()
            self.state = 305
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32 or _la==33:
                self.state = 301
                _la = self._input.LA(1)
                if not(_la==32 or _la==33):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 302
                self.multiplicativeExpression()
                self.state = 307
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MultiplicativeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CASSParser.UnaryExpressionContext)
            else:
                return self.getTypedRuleContext(CASSParser.UnaryExpressionContext,i)


        def getRuleIndex(self):
            return CASSParser.RULE_multiplicativeExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)




    def multiplicativeExpression(self):

        localctx = CASSParser.MultiplicativeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 308
            self.unaryExpression(0)
            self.state = 313
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 120259084288) != 0):
                self.state = 309
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 120259084288) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 310
                self.unaryExpression(0)
                self.state = 315
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def additiveExpression(self):
            return self.getTypedRuleContext(CASSParser.AdditiveExpressionContext,0)


        def multiplicativeExpression(self):
            return self.getTypedRuleContext(CASSParser.MultiplicativeExpressionContext,0)


        def getRuleIndex(self):
            return CASSParser.RULE_operationExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperationExpression" ):
                listener.enterOperationExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperationExpression" ):
                listener.exitOperationExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperationExpression" ):
                return visitor.visitOperationExpression(self)
            else:
                return visitor.visitChildren(self)




    def operationExpression(self):

        localctx = CASSParser.OperationExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_operationExpression)
        try:
            self.state = 318
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 316
                self.additiveExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 317
                self.multiplicativeExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[22] = self.unaryExpression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def unaryExpression_sempred(self, localctx:UnaryExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         




