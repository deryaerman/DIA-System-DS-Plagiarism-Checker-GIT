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
        4,1,41,306,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,1,0,4,0,62,8,0,11,0,12,0,63,1,0,1,
        0,1,1,1,1,1,1,1,1,3,1,72,8,1,1,1,1,1,1,1,1,2,1,2,5,2,79,8,2,10,2,
        12,2,82,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,
        96,8,3,1,4,1,4,1,4,1,4,3,4,102,8,4,1,4,1,4,1,5,1,5,1,5,3,5,109,8,
        5,1,5,1,5,3,5,113,8,5,1,5,1,5,3,5,117,8,5,1,5,1,5,1,5,5,5,122,8,
        5,10,5,12,5,125,9,5,1,5,1,5,1,6,1,6,1,6,3,6,132,8,6,1,6,1,6,3,6,
        136,8,6,1,6,1,6,3,6,140,8,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,
        1,8,1,9,1,9,1,9,1,9,1,9,1,9,5,9,158,8,9,10,9,12,9,161,9,9,1,9,1,
        9,1,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,5,
        11,177,8,11,10,11,12,11,180,9,11,1,11,1,11,1,11,1,11,5,11,186,8,
        11,10,11,12,11,189,9,11,1,11,3,11,192,8,11,1,12,1,12,1,12,1,12,1,
        12,1,12,1,12,3,12,201,8,12,1,13,1,13,3,13,205,8,13,1,13,1,13,1,14,
        1,14,1,14,1,15,1,15,1,15,5,15,215,8,15,10,15,12,15,218,9,15,1,16,
        1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,19,1,19,1,19,3,19,232,
        8,19,1,20,1,20,1,20,1,20,1,20,3,20,239,8,20,1,21,1,21,1,21,1,21,
        1,21,1,21,1,21,1,21,1,21,3,21,250,8,21,1,22,1,22,1,23,1,23,1,23,
        5,23,257,8,23,10,23,12,23,260,9,23,1,24,1,24,1,24,5,24,265,8,24,
        10,24,12,24,268,9,24,1,25,1,25,1,25,5,25,273,8,25,10,25,12,25,276,
        9,25,1,26,1,26,1,26,5,26,281,8,26,10,26,12,26,284,9,26,1,27,1,27,
        1,27,5,27,289,8,27,10,27,12,27,292,9,27,1,28,1,28,1,28,5,28,297,
        8,28,10,28,12,28,300,9,28,1,29,1,29,3,29,304,8,29,1,29,0,0,30,0,
        2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,
        48,50,52,54,56,58,0,6,1,0,13,15,2,0,5,5,18,21,1,0,24,25,1,0,26,29,
        1,0,30,31,1,0,32,33,317,0,61,1,0,0,0,2,67,1,0,0,0,4,76,1,0,0,0,6,
        95,1,0,0,0,8,97,1,0,0,0,10,105,1,0,0,0,12,128,1,0,0,0,14,144,1,0,
        0,0,16,149,1,0,0,0,18,151,1,0,0,0,20,164,1,0,0,0,22,170,1,0,0,0,
        24,193,1,0,0,0,26,202,1,0,0,0,28,208,1,0,0,0,30,211,1,0,0,0,32,219,
        1,0,0,0,34,222,1,0,0,0,36,224,1,0,0,0,38,231,1,0,0,0,40,238,1,0,
        0,0,42,249,1,0,0,0,44,251,1,0,0,0,46,253,1,0,0,0,48,261,1,0,0,0,
        50,269,1,0,0,0,52,277,1,0,0,0,54,285,1,0,0,0,56,293,1,0,0,0,58,303,
        1,0,0,0,60,62,3,6,3,0,61,60,1,0,0,0,62,63,1,0,0,0,63,61,1,0,0,0,
        63,64,1,0,0,0,64,65,1,0,0,0,65,66,5,0,0,1,66,1,1,0,0,0,67,68,3,34,
        17,0,68,69,5,36,0,0,69,71,5,1,0,0,70,72,3,30,15,0,71,70,1,0,0,0,
        71,72,1,0,0,0,72,73,1,0,0,0,73,74,5,2,0,0,74,75,3,4,2,0,75,3,1,0,
        0,0,76,80,5,3,0,0,77,79,3,6,3,0,78,77,1,0,0,0,79,82,1,0,0,0,80,78,
        1,0,0,0,80,81,1,0,0,0,81,83,1,0,0,0,82,80,1,0,0,0,83,84,5,4,0,0,
        84,5,1,0,0,0,85,96,3,8,4,0,86,96,3,10,5,0,87,96,3,12,6,0,88,96,3,
        18,9,0,89,96,3,20,10,0,90,96,3,22,11,0,91,96,3,24,12,0,92,96,3,26,
        13,0,93,96,3,28,14,0,94,96,3,2,1,0,95,85,1,0,0,0,95,86,1,0,0,0,95,
        87,1,0,0,0,95,88,1,0,0,0,95,89,1,0,0,0,95,90,1,0,0,0,95,91,1,0,0,
        0,95,92,1,0,0,0,95,93,1,0,0,0,95,94,1,0,0,0,96,7,1,0,0,0,97,98,3,
        34,17,0,98,101,5,36,0,0,99,100,5,5,0,0,100,102,3,36,18,0,101,99,
        1,0,0,0,101,102,1,0,0,0,102,103,1,0,0,0,103,104,5,6,0,0,104,9,1,
        0,0,0,105,106,5,7,0,0,106,108,5,1,0,0,107,109,3,14,7,0,108,107,1,
        0,0,0,108,109,1,0,0,0,109,110,1,0,0,0,110,112,5,6,0,0,111,113,3,
        36,18,0,112,111,1,0,0,0,112,113,1,0,0,0,113,114,1,0,0,0,114,116,
        5,6,0,0,115,117,3,16,8,0,116,115,1,0,0,0,116,117,1,0,0,0,117,118,
        1,0,0,0,118,119,5,2,0,0,119,123,5,3,0,0,120,122,3,6,3,0,121,120,
        1,0,0,0,122,125,1,0,0,0,123,121,1,0,0,0,123,124,1,0,0,0,124,126,
        1,0,0,0,125,123,1,0,0,0,126,127,5,4,0,0,127,11,1,0,0,0,128,129,5,
        7,0,0,129,131,5,1,0,0,130,132,3,14,7,0,131,130,1,0,0,0,131,132,1,
        0,0,0,132,133,1,0,0,0,133,135,5,6,0,0,134,136,3,36,18,0,135,134,
        1,0,0,0,135,136,1,0,0,0,136,137,1,0,0,0,137,139,5,6,0,0,138,140,
        3,16,8,0,139,138,1,0,0,0,139,140,1,0,0,0,140,141,1,0,0,0,141,142,
        5,2,0,0,142,143,3,6,3,0,143,13,1,0,0,0,144,145,3,34,17,0,145,146,
        5,36,0,0,146,147,5,5,0,0,147,148,3,36,18,0,148,15,1,0,0,0,149,150,
        3,40,20,0,150,17,1,0,0,0,151,152,5,8,0,0,152,153,5,1,0,0,153,154,
        3,36,18,0,154,155,5,2,0,0,155,159,5,3,0,0,156,158,3,6,3,0,157,156,
        1,0,0,0,158,161,1,0,0,0,159,157,1,0,0,0,159,160,1,0,0,0,160,162,
        1,0,0,0,161,159,1,0,0,0,162,163,5,4,0,0,163,19,1,0,0,0,164,165,5,
        8,0,0,165,166,5,1,0,0,166,167,3,36,18,0,167,168,5,2,0,0,168,169,
        3,6,3,0,169,21,1,0,0,0,170,171,5,9,0,0,171,172,5,1,0,0,172,173,3,
        36,18,0,173,174,5,2,0,0,174,178,5,3,0,0,175,177,3,6,3,0,176,175,
        1,0,0,0,177,180,1,0,0,0,178,176,1,0,0,0,178,179,1,0,0,0,179,181,
        1,0,0,0,180,178,1,0,0,0,181,191,5,4,0,0,182,183,5,10,0,0,183,187,
        5,3,0,0,184,186,3,6,3,0,185,184,1,0,0,0,186,189,1,0,0,0,187,185,
        1,0,0,0,187,188,1,0,0,0,188,190,1,0,0,0,189,187,1,0,0,0,190,192,
        5,4,0,0,191,182,1,0,0,0,191,192,1,0,0,0,192,23,1,0,0,0,193,194,5,
        9,0,0,194,195,5,1,0,0,195,196,3,36,18,0,196,197,5,2,0,0,197,200,
        3,6,3,0,198,199,5,10,0,0,199,201,3,6,3,0,200,198,1,0,0,0,200,201,
        1,0,0,0,201,25,1,0,0,0,202,204,5,11,0,0,203,205,3,36,18,0,204,203,
        1,0,0,0,204,205,1,0,0,0,205,206,1,0,0,0,206,207,5,6,0,0,207,27,1,
        0,0,0,208,209,3,36,18,0,209,210,5,6,0,0,210,29,1,0,0,0,211,216,3,
        32,16,0,212,213,5,12,0,0,213,215,3,32,16,0,214,212,1,0,0,0,215,218,
        1,0,0,0,216,214,1,0,0,0,216,217,1,0,0,0,217,31,1,0,0,0,218,216,1,
        0,0,0,219,220,3,34,17,0,220,221,5,36,0,0,221,33,1,0,0,0,222,223,
        7,0,0,0,223,35,1,0,0,0,224,225,3,38,19,0,225,37,1,0,0,0,226,227,
        3,40,20,0,227,228,3,44,22,0,228,229,3,38,19,0,229,232,1,0,0,0,230,
        232,3,46,23,0,231,226,1,0,0,0,231,230,1,0,0,0,232,39,1,0,0,0,233,
        234,5,16,0,0,234,239,3,40,20,0,235,236,5,17,0,0,236,239,3,40,20,
        0,237,239,3,42,21,0,238,233,1,0,0,0,238,235,1,0,0,0,238,237,1,0,
        0,0,239,41,1,0,0,0,240,250,5,36,0,0,241,250,5,37,0,0,242,250,5,38,
        0,0,243,250,5,39,0,0,244,250,5,40,0,0,245,246,5,1,0,0,246,247,3,
        36,18,0,247,248,5,2,0,0,248,250,1,0,0,0,249,240,1,0,0,0,249,241,
        1,0,0,0,249,242,1,0,0,0,249,243,1,0,0,0,249,244,1,0,0,0,249,245,
        1,0,0,0,250,43,1,0,0,0,251,252,7,1,0,0,252,45,1,0,0,0,253,258,3,
        48,24,0,254,255,5,22,0,0,255,257,3,48,24,0,256,254,1,0,0,0,257,260,
        1,0,0,0,258,256,1,0,0,0,258,259,1,0,0,0,259,47,1,0,0,0,260,258,1,
        0,0,0,261,266,3,50,25,0,262,263,5,23,0,0,263,265,3,50,25,0,264,262,
        1,0,0,0,265,268,1,0,0,0,266,264,1,0,0,0,266,267,1,0,0,0,267,49,1,
        0,0,0,268,266,1,0,0,0,269,274,3,52,26,0,270,271,7,2,0,0,271,273,
        3,52,26,0,272,270,1,0,0,0,273,276,1,0,0,0,274,272,1,0,0,0,274,275,
        1,0,0,0,275,51,1,0,0,0,276,274,1,0,0,0,277,282,3,54,27,0,278,279,
        7,3,0,0,279,281,3,54,27,0,280,278,1,0,0,0,281,284,1,0,0,0,282,280,
        1,0,0,0,282,283,1,0,0,0,283,53,1,0,0,0,284,282,1,0,0,0,285,290,3,
        56,28,0,286,287,7,4,0,0,287,289,3,56,28,0,288,286,1,0,0,0,289,292,
        1,0,0,0,290,288,1,0,0,0,290,291,1,0,0,0,291,55,1,0,0,0,292,290,1,
        0,0,0,293,298,3,40,20,0,294,295,7,5,0,0,295,297,3,40,20,0,296,294,
        1,0,0,0,297,300,1,0,0,0,298,296,1,0,0,0,298,299,1,0,0,0,299,57,1,
        0,0,0,300,298,1,0,0,0,301,304,3,54,27,0,302,304,3,56,28,0,303,301,
        1,0,0,0,303,302,1,0,0,0,304,59,1,0,0,0,29,63,71,80,95,101,108,112,
        116,123,131,135,139,159,178,187,191,200,204,216,231,238,249,258,
        266,274,282,290,298,303
    ]

class CASSParser ( Parser ):

    grammarFileName = "CASS.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'{'", "'}'", "'='", "';'", 
                     "'for'", "'while'", "'if'", "'else'", "'return'", "','", 
                     "'int'", "'float'", "'double'", "'++'", "'--'", "'+='", 
                     "'-='", "'*='", "'/='", "'||'", "'&&'", "'=='", "'!='", 
                     "'<'", "'>'", "'<='", "'>='", "'+'", "'-'", "'*'", 
                     "'/'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "SL_COMMENT", "ML_COMMENT", 
                      "ID", "INT", "FLOAT", "CHAR", "STRING", "WS" ]

    RULE_prog = 0
    RULE_functionDefinition = 1
    RULE_compoundStatement = 2
    RULE_statement = 3
    RULE_declarationStatement = 4
    RULE_forBlockStatement = 5
    RULE_forSingleStatement = 6
    RULE_forInit = 7
    RULE_forUpdate = 8
    RULE_whileBlockStatement = 9
    RULE_whileSingleStatement = 10
    RULE_ifBlockStatement = 11
    RULE_ifSingleStatement = 12
    RULE_returnStatement = 13
    RULE_expressionStatement = 14
    RULE_parameterList = 15
    RULE_parameter = 16
    RULE_typeSpec = 17
    RULE_expression = 18
    RULE_assignmentExpression = 19
    RULE_unaryExpression = 20
    RULE_primaryExpression = 21
    RULE_assignmentOperator = 22
    RULE_logicalOrExpression = 23
    RULE_logicalAndExpression = 24
    RULE_equalityExpression = 25
    RULE_relationalExpression = 26
    RULE_additiveExpression = 27
    RULE_multiplicativeExpression = 28
    RULE_operationExpression = 29

    ruleNames =  [ "prog", "functionDefinition", "compoundStatement", "statement", 
                   "declarationStatement", "forBlockStatement", "forSingleStatement", 
                   "forInit", "forUpdate", "whileBlockStatement", "whileSingleStatement", 
                   "ifBlockStatement", "ifSingleStatement", "returnStatement", 
                   "expressionStatement", "parameterList", "parameter", 
                   "typeSpec", "expression", "assignmentExpression", "unaryExpression", 
                   "primaryExpression", "assignmentOperator", "logicalOrExpression", 
                   "logicalAndExpression", "equalityExpression", "relationalExpression", 
                   "additiveExpression", "multiplicativeExpression", "operationExpression" ]

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
    SL_COMMENT=34
    ML_COMMENT=35
    ID=36
    INT=37
    FLOAT=38
    CHAR=39
    STRING=40
    WS=41

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
            self.state = 61 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 60
                self.statement()
                self.state = 63 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 2130304035714) != 0)):
                    break

            self.state = 65
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


        def ID(self):
            return self.getToken(CASSParser.ID, 0)

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
            self.state = 67
            self.typeSpec()
            self.state = 68
            self.match(CASSParser.ID)
            self.state = 69
            self.match(CASSParser.T__0)
            self.state = 71
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 57344) != 0):
                self.state = 70
                self.parameterList()


            self.state = 73
            self.match(CASSParser.T__1)
            self.state = 74
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
            self.state = 76
            self.match(CASSParser.T__2)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2130304035714) != 0):
                self.state = 77
                self.statement()
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 83
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
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.declarationStatement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
                self.forBlockStatement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 87
                self.forSingleStatement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 88
                self.whileBlockStatement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 89
                self.whileSingleStatement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 90
                self.ifBlockStatement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 91
                self.ifSingleStatement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 92
                self.returnStatement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 93
                self.expressionStatement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 94
                self.functionDefinition()
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


        def ID(self):
            return self.getToken(CASSParser.ID, 0)

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
            self.state = 97
            self.typeSpec()
            self.state = 98
            self.match(CASSParser.ID)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 99
                self.match(CASSParser.T__4)
                self.state = 100
                self.expression()


            self.state = 103
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

        def forInit(self):
            return self.getTypedRuleContext(CASSParser.ForInitContext,0)


        def expression(self):
            return self.getTypedRuleContext(CASSParser.ExpressionContext,0)


        def forUpdate(self):
            return self.getTypedRuleContext(CASSParser.ForUpdateContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CASSParser.StatementContext)
            else:
                return self.getTypedRuleContext(CASSParser.StatementContext,i)


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
            self.state = 105
            self.match(CASSParser.T__6)
            self.state = 106
            self.match(CASSParser.T__0)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 57344) != 0):
                self.state = 107
                self.forInit()


            self.state = 110
            self.match(CASSParser.T__5)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2130303975426) != 0):
                self.state = 111
                self.expression()


            self.state = 114
            self.match(CASSParser.T__5)
            self.state = 116
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2130303975426) != 0):
                self.state = 115
                self.forUpdate()


            self.state = 118
            self.match(CASSParser.T__1)
            self.state = 119
            self.match(CASSParser.T__2)
            self.state = 123
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2130304035714) != 0):
                self.state = 120
                self.statement()
                self.state = 125
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 126
            self.match(CASSParser.T__3)
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


        def forInit(self):
            return self.getTypedRuleContext(CASSParser.ForInitContext,0)


        def expression(self):
            return self.getTypedRuleContext(CASSParser.ExpressionContext,0)


        def forUpdate(self):
            return self.getTypedRuleContext(CASSParser.ForUpdateContext,0)


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
            self.state = 128
            self.match(CASSParser.T__6)
            self.state = 129
            self.match(CASSParser.T__0)
            self.state = 131
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 57344) != 0):
                self.state = 130
                self.forInit()


            self.state = 133
            self.match(CASSParser.T__5)
            self.state = 135
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2130303975426) != 0):
                self.state = 134
                self.expression()


            self.state = 137
            self.match(CASSParser.T__5)
            self.state = 139
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2130303975426) != 0):
                self.state = 138
                self.forUpdate()


            self.state = 141
            self.match(CASSParser.T__1)
            self.state = 142
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def typeSpec(self):
            return self.getTypedRuleContext(CASSParser.TypeSpecContext,0)


        def ID(self):
            return self.getToken(CASSParser.ID, 0)

        def expression(self):
            return self.getTypedRuleContext(CASSParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CASSParser.RULE_forInit

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForInit" ):
                listener.enterForInit(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForInit" ):
                listener.exitForInit(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInit" ):
                return visitor.visitForInit(self)
            else:
                return visitor.visitChildren(self)




    def forInit(self):

        localctx = CASSParser.ForInitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_forInit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.typeSpec()
            self.state = 145
            self.match(CASSParser.ID)
            self.state = 146
            self.match(CASSParser.T__4)
            self.state = 147
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForUpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unaryExpression(self):
            return self.getTypedRuleContext(CASSParser.UnaryExpressionContext,0)


        def getRuleIndex(self):
            return CASSParser.RULE_forUpdate

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForUpdate" ):
                listener.enterForUpdate(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForUpdate" ):
                listener.exitForUpdate(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForUpdate" ):
                return visitor.visitForUpdate(self)
            else:
                return visitor.visitChildren(self)




    def forUpdate(self):

        localctx = CASSParser.ForUpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_forUpdate)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 149
            self.unaryExpression()
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

        def expression(self):
            return self.getTypedRuleContext(CASSParser.ExpressionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CASSParser.StatementContext)
            else:
                return self.getTypedRuleContext(CASSParser.StatementContext,i)


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
        self.enterRule(localctx, 18, self.RULE_whileBlockStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self.match(CASSParser.T__7)
            self.state = 152
            self.match(CASSParser.T__0)
            self.state = 153
            self.expression()
            self.state = 154
            self.match(CASSParser.T__1)
            self.state = 155
            self.match(CASSParser.T__2)
            self.state = 159
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2130304035714) != 0):
                self.state = 156
                self.statement()
                self.state = 161
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 162
            self.match(CASSParser.T__3)
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

        def expression(self):
            return self.getTypedRuleContext(CASSParser.ExpressionContext,0)


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
        self.enterRule(localctx, 20, self.RULE_whileSingleStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.match(CASSParser.T__7)
            self.state = 165
            self.match(CASSParser.T__0)
            self.state = 166
            self.expression()
            self.state = 167
            self.match(CASSParser.T__1)
            self.state = 168
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

        def expression(self):
            return self.getTypedRuleContext(CASSParser.ExpressionContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CASSParser.StatementContext)
            else:
                return self.getTypedRuleContext(CASSParser.StatementContext,i)


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
        self.enterRule(localctx, 22, self.RULE_ifBlockStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
            self.match(CASSParser.T__8)
            self.state = 171
            self.match(CASSParser.T__0)
            self.state = 172
            self.expression()
            self.state = 173
            self.match(CASSParser.T__1)
            self.state = 174
            self.match(CASSParser.T__2)
            self.state = 178
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2130304035714) != 0):
                self.state = 175
                self.statement()
                self.state = 180
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 181
            self.match(CASSParser.T__3)
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 182
                self.match(CASSParser.T__9)
                self.state = 183
                self.match(CASSParser.T__2)
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2130304035714) != 0):
                    self.state = 184
                    self.statement()
                    self.state = 189
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 190
                self.match(CASSParser.T__3)


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

        def expression(self):
            return self.getTypedRuleContext(CASSParser.ExpressionContext,0)


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
        self.enterRule(localctx, 24, self.RULE_ifSingleStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(CASSParser.T__8)
            self.state = 194
            self.match(CASSParser.T__0)
            self.state = 195
            self.expression()
            self.state = 196
            self.match(CASSParser.T__1)
            self.state = 197
            self.statement()
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 198
                self.match(CASSParser.T__9)
                self.state = 199
                self.statement()


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
        self.enterRule(localctx, 26, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(CASSParser.T__10)
            self.state = 204
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2130303975426) != 0):
                self.state = 203
                self.expression()


            self.state = 206
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
        self.enterRule(localctx, 28, self.RULE_expressionStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.expression()
            self.state = 209
            self.match(CASSParser.T__5)
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
        self.enterRule(localctx, 30, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 211
            self.parameter()
            self.state = 216
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 212
                self.match(CASSParser.T__11)
                self.state = 213
                self.parameter()
                self.state = 218
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


        def ID(self):
            return self.getToken(CASSParser.ID, 0)

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
        self.enterRule(localctx, 32, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.typeSpec()
            self.state = 220
            self.match(CASSParser.ID)
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
        self.enterRule(localctx, 34, self.RULE_typeSpec)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 57344) != 0)):
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
        self.enterRule(localctx, 36, self.RULE_expression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 224
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
        self.enterRule(localctx, 38, self.RULE_assignmentExpression)
        try:
            self.state = 231
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.unaryExpression()
                self.state = 227
                self.assignmentOperator()
                self.state = 228
                self.assignmentExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 230
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




    def unaryExpression(self):

        localctx = CASSParser.UnaryExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_unaryExpression)
        try:
            self.state = 238
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.match(CASSParser.T__15)
                self.state = 234
                self.unaryExpression()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.match(CASSParser.T__16)
                self.state = 236
                self.unaryExpression()
                pass
            elif token in [1, 36, 37, 38, 39, 40]:
                self.enterOuterAlt(localctx, 3)
                self.state = 237
                self.primaryExpression()
                pass
            else:
                raise NoViableAltException(self)

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
        self.enterRule(localctx, 42, self.RULE_primaryExpression)
        try:
            self.state = 249
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.match(CASSParser.ID)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 241
                self.match(CASSParser.INT)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 3)
                self.state = 242
                self.match(CASSParser.FLOAT)
                pass
            elif token in [39]:
                self.enterOuterAlt(localctx, 4)
                self.state = 243
                self.match(CASSParser.CHAR)
                pass
            elif token in [40]:
                self.enterOuterAlt(localctx, 5)
                self.state = 244
                self.match(CASSParser.STRING)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 6)
                self.state = 245
                self.match(CASSParser.T__0)
                self.state = 246
                self.expression()
                self.state = 247
                self.match(CASSParser.T__1)
                pass
            else:
                raise NoViableAltException(self)

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
        self.enterRule(localctx, 44, self.RULE_assignmentOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 3932192) != 0)):
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
        self.enterRule(localctx, 46, self.RULE_logicalOrExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.logicalAndExpression()
            self.state = 258
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 254
                self.match(CASSParser.T__21)
                self.state = 255
                self.logicalAndExpression()
                self.state = 260
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
        self.enterRule(localctx, 48, self.RULE_logicalAndExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.equalityExpression()
            self.state = 266
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 262
                self.match(CASSParser.T__22)
                self.state = 263
                self.equalityExpression()
                self.state = 268
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
        self.enterRule(localctx, 50, self.RULE_equalityExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.relationalExpression()
            self.state = 274
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24 or _la==25:
                self.state = 270
                _la = self._input.LA(1)
                if not(_la==24 or _la==25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 271
                self.relationalExpression()
                self.state = 276
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
        self.enterRule(localctx, 52, self.RULE_relationalExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.additiveExpression()
            self.state = 282
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1006632960) != 0):
                self.state = 278
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1006632960) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 279
                self.additiveExpression()
                self.state = 284
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
        self.enterRule(localctx, 54, self.RULE_additiveExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.multiplicativeExpression()
            self.state = 290
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30 or _la==31:
                self.state = 286
                _la = self._input.LA(1)
                if not(_la==30 or _la==31):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 287
                self.multiplicativeExpression()
                self.state = 292
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
        self.enterRule(localctx, 56, self.RULE_multiplicativeExpression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 293
            self.unaryExpression()
            self.state = 298
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32 or _la==33:
                self.state = 294
                _la = self._input.LA(1)
                if not(_la==32 or _la==33):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 295
                self.unaryExpression()
                self.state = 300
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
        self.enterRule(localctx, 58, self.RULE_operationExpression)
        try:
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self.additiveExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 302
                self.multiplicativeExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





