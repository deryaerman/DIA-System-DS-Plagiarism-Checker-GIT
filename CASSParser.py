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
        4,1,39,303,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,1,0,4,0,62,8,0,11,0,12,0,63,1,0,1,
        0,1,1,1,1,1,1,1,1,3,1,72,8,1,1,1,1,1,1,1,1,2,1,2,5,2,79,8,2,10,2,
        12,2,82,9,2,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,95,8,
        3,1,4,1,4,1,4,1,4,3,4,101,8,4,1,4,1,4,1,5,1,5,1,5,3,5,108,8,5,1,
        5,1,5,3,5,112,8,5,1,5,1,5,3,5,116,8,5,1,5,1,5,1,5,5,5,121,8,5,10,
        5,12,5,124,9,5,1,5,1,5,1,6,1,6,1,6,3,6,131,8,6,1,6,1,6,3,6,135,8,
        6,1,6,1,6,3,6,139,8,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,8,1,8,1,
        9,1,9,1,9,1,9,1,9,1,9,5,9,157,8,9,10,9,12,9,160,9,9,1,9,1,9,1,10,
        1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,11,5,11,176,
        8,11,10,11,12,11,179,9,11,1,11,1,11,1,11,1,11,5,11,185,8,11,10,11,
        12,11,188,9,11,1,11,3,11,191,8,11,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,3,12,200,8,12,1,13,1,13,3,13,204,8,13,1,13,1,13,1,14,1,14,1,
        14,1,15,1,15,1,15,5,15,214,8,15,10,15,12,15,217,9,15,1,16,1,16,1,
        16,1,17,1,17,1,18,1,18,1,19,1,19,1,19,1,19,1,19,3,19,231,8,19,1,
        20,1,20,1,20,1,20,1,20,3,20,238,8,20,1,21,1,21,1,21,1,21,1,21,1,
        21,1,21,3,21,247,8,21,1,22,1,22,1,23,1,23,1,23,5,23,254,8,23,10,
        23,12,23,257,9,23,1,24,1,24,1,24,5,24,262,8,24,10,24,12,24,265,9,
        24,1,25,1,25,1,25,5,25,270,8,25,10,25,12,25,273,9,25,1,26,1,26,1,
        26,5,26,278,8,26,10,26,12,26,281,9,26,1,27,1,27,1,27,5,27,286,8,
        27,10,27,12,27,289,9,27,1,28,1,28,1,28,5,28,294,8,28,10,28,12,28,
        297,9,28,1,29,1,29,3,29,301,8,29,1,29,0,0,30,0,2,4,6,8,10,12,14,
        16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,
        0,6,1,0,13,15,2,0,5,5,18,21,1,0,24,25,1,0,26,29,1,0,30,31,1,0,32,
        33,311,0,61,1,0,0,0,2,67,1,0,0,0,4,76,1,0,0,0,6,94,1,0,0,0,8,96,
        1,0,0,0,10,104,1,0,0,0,12,127,1,0,0,0,14,143,1,0,0,0,16,148,1,0,
        0,0,18,150,1,0,0,0,20,163,1,0,0,0,22,169,1,0,0,0,24,192,1,0,0,0,
        26,201,1,0,0,0,28,207,1,0,0,0,30,210,1,0,0,0,32,218,1,0,0,0,34,221,
        1,0,0,0,36,223,1,0,0,0,38,230,1,0,0,0,40,237,1,0,0,0,42,246,1,0,
        0,0,44,248,1,0,0,0,46,250,1,0,0,0,48,258,1,0,0,0,50,266,1,0,0,0,
        52,274,1,0,0,0,54,282,1,0,0,0,56,290,1,0,0,0,58,300,1,0,0,0,60,62,
        3,2,1,0,61,60,1,0,0,0,62,63,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,
        64,65,1,0,0,0,65,66,5,0,0,1,66,1,1,0,0,0,67,68,3,34,17,0,68,69,5,
        36,0,0,69,71,5,1,0,0,70,72,3,30,15,0,71,70,1,0,0,0,71,72,1,0,0,0,
        72,73,1,0,0,0,73,74,5,2,0,0,74,75,3,4,2,0,75,3,1,0,0,0,76,80,5,3,
        0,0,77,79,3,6,3,0,78,77,1,0,0,0,79,82,1,0,0,0,80,78,1,0,0,0,80,81,
        1,0,0,0,81,83,1,0,0,0,82,80,1,0,0,0,83,84,5,4,0,0,84,5,1,0,0,0,85,
        95,3,8,4,0,86,95,3,10,5,0,87,95,3,12,6,0,88,95,3,18,9,0,89,95,3,
        20,10,0,90,95,3,22,11,0,91,95,3,24,12,0,92,95,3,26,13,0,93,95,3,
        28,14,0,94,85,1,0,0,0,94,86,1,0,0,0,94,87,1,0,0,0,94,88,1,0,0,0,
        94,89,1,0,0,0,94,90,1,0,0,0,94,91,1,0,0,0,94,92,1,0,0,0,94,93,1,
        0,0,0,95,7,1,0,0,0,96,97,3,34,17,0,97,100,5,36,0,0,98,99,5,5,0,0,
        99,101,3,36,18,0,100,98,1,0,0,0,100,101,1,0,0,0,101,102,1,0,0,0,
        102,103,5,6,0,0,103,9,1,0,0,0,104,105,5,7,0,0,105,107,5,1,0,0,106,
        108,3,14,7,0,107,106,1,0,0,0,107,108,1,0,0,0,108,109,1,0,0,0,109,
        111,5,6,0,0,110,112,3,36,18,0,111,110,1,0,0,0,111,112,1,0,0,0,112,
        113,1,0,0,0,113,115,5,6,0,0,114,116,3,16,8,0,115,114,1,0,0,0,115,
        116,1,0,0,0,116,117,1,0,0,0,117,118,5,2,0,0,118,122,5,3,0,0,119,
        121,3,6,3,0,120,119,1,0,0,0,121,124,1,0,0,0,122,120,1,0,0,0,122,
        123,1,0,0,0,123,125,1,0,0,0,124,122,1,0,0,0,125,126,5,4,0,0,126,
        11,1,0,0,0,127,128,5,7,0,0,128,130,5,1,0,0,129,131,3,14,7,0,130,
        129,1,0,0,0,130,131,1,0,0,0,131,132,1,0,0,0,132,134,5,6,0,0,133,
        135,3,36,18,0,134,133,1,0,0,0,134,135,1,0,0,0,135,136,1,0,0,0,136,
        138,5,6,0,0,137,139,3,16,8,0,138,137,1,0,0,0,138,139,1,0,0,0,139,
        140,1,0,0,0,140,141,5,2,0,0,141,142,3,6,3,0,142,13,1,0,0,0,143,144,
        3,34,17,0,144,145,5,36,0,0,145,146,5,5,0,0,146,147,3,36,18,0,147,
        15,1,0,0,0,148,149,3,40,20,0,149,17,1,0,0,0,150,151,5,8,0,0,151,
        152,5,1,0,0,152,153,3,36,18,0,153,154,5,2,0,0,154,158,5,3,0,0,155,
        157,3,6,3,0,156,155,1,0,0,0,157,160,1,0,0,0,158,156,1,0,0,0,158,
        159,1,0,0,0,159,161,1,0,0,0,160,158,1,0,0,0,161,162,5,4,0,0,162,
        19,1,0,0,0,163,164,5,8,0,0,164,165,5,1,0,0,165,166,3,36,18,0,166,
        167,5,2,0,0,167,168,3,6,3,0,168,21,1,0,0,0,169,170,5,9,0,0,170,171,
        5,1,0,0,171,172,3,36,18,0,172,173,5,2,0,0,173,177,5,3,0,0,174,176,
        3,6,3,0,175,174,1,0,0,0,176,179,1,0,0,0,177,175,1,0,0,0,177,178,
        1,0,0,0,178,180,1,0,0,0,179,177,1,0,0,0,180,190,5,4,0,0,181,182,
        5,10,0,0,182,186,5,3,0,0,183,185,3,6,3,0,184,183,1,0,0,0,185,188,
        1,0,0,0,186,184,1,0,0,0,186,187,1,0,0,0,187,189,1,0,0,0,188,186,
        1,0,0,0,189,191,5,4,0,0,190,181,1,0,0,0,190,191,1,0,0,0,191,23,1,
        0,0,0,192,193,5,9,0,0,193,194,5,1,0,0,194,195,3,36,18,0,195,196,
        5,2,0,0,196,199,3,6,3,0,197,198,5,10,0,0,198,200,3,6,3,0,199,197,
        1,0,0,0,199,200,1,0,0,0,200,25,1,0,0,0,201,203,5,11,0,0,202,204,
        3,36,18,0,203,202,1,0,0,0,203,204,1,0,0,0,204,205,1,0,0,0,205,206,
        5,6,0,0,206,27,1,0,0,0,207,208,3,36,18,0,208,209,5,6,0,0,209,29,
        1,0,0,0,210,215,3,32,16,0,211,212,5,12,0,0,212,214,3,32,16,0,213,
        211,1,0,0,0,214,217,1,0,0,0,215,213,1,0,0,0,215,216,1,0,0,0,216,
        31,1,0,0,0,217,215,1,0,0,0,218,219,3,34,17,0,219,220,5,36,0,0,220,
        33,1,0,0,0,221,222,7,0,0,0,222,35,1,0,0,0,223,224,3,38,19,0,224,
        37,1,0,0,0,225,226,3,40,20,0,226,227,3,44,22,0,227,228,3,38,19,0,
        228,231,1,0,0,0,229,231,3,46,23,0,230,225,1,0,0,0,230,229,1,0,0,
        0,231,39,1,0,0,0,232,233,5,16,0,0,233,238,3,40,20,0,234,235,5,17,
        0,0,235,238,3,40,20,0,236,238,3,42,21,0,237,232,1,0,0,0,237,234,
        1,0,0,0,237,236,1,0,0,0,238,41,1,0,0,0,239,247,5,36,0,0,240,247,
        5,37,0,0,241,247,5,38,0,0,242,243,5,1,0,0,243,244,3,36,18,0,244,
        245,5,2,0,0,245,247,1,0,0,0,246,239,1,0,0,0,246,240,1,0,0,0,246,
        241,1,0,0,0,246,242,1,0,0,0,247,43,1,0,0,0,248,249,7,1,0,0,249,45,
        1,0,0,0,250,255,3,48,24,0,251,252,5,22,0,0,252,254,3,48,24,0,253,
        251,1,0,0,0,254,257,1,0,0,0,255,253,1,0,0,0,255,256,1,0,0,0,256,
        47,1,0,0,0,257,255,1,0,0,0,258,263,3,50,25,0,259,260,5,23,0,0,260,
        262,3,50,25,0,261,259,1,0,0,0,262,265,1,0,0,0,263,261,1,0,0,0,263,
        264,1,0,0,0,264,49,1,0,0,0,265,263,1,0,0,0,266,271,3,52,26,0,267,
        268,7,2,0,0,268,270,3,52,26,0,269,267,1,0,0,0,270,273,1,0,0,0,271,
        269,1,0,0,0,271,272,1,0,0,0,272,51,1,0,0,0,273,271,1,0,0,0,274,279,
        3,54,27,0,275,276,7,3,0,0,276,278,3,54,27,0,277,275,1,0,0,0,278,
        281,1,0,0,0,279,277,1,0,0,0,279,280,1,0,0,0,280,53,1,0,0,0,281,279,
        1,0,0,0,282,287,3,56,28,0,283,284,7,4,0,0,284,286,3,56,28,0,285,
        283,1,0,0,0,286,289,1,0,0,0,287,285,1,0,0,0,287,288,1,0,0,0,288,
        55,1,0,0,0,289,287,1,0,0,0,290,295,3,40,20,0,291,292,7,5,0,0,292,
        294,3,40,20,0,293,291,1,0,0,0,294,297,1,0,0,0,295,293,1,0,0,0,295,
        296,1,0,0,0,296,57,1,0,0,0,297,295,1,0,0,0,298,301,3,54,27,0,299,
        301,3,56,28,0,300,298,1,0,0,0,300,299,1,0,0,0,301,59,1,0,0,0,29,
        63,71,80,94,100,107,111,115,122,130,134,138,158,177,186,190,199,
        203,215,230,237,246,255,263,271,279,287,295,300
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
                      "ID", "INT", "FLOAT", "WS" ]

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
    WS=39

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

        def functionDefinition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CASSParser.FunctionDefinitionContext)
            else:
                return self.getTypedRuleContext(CASSParser.FunctionDefinitionContext,i)


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
                self.functionDefinition()
                self.state = 63 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 57344) != 0)):
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
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 481036594050) != 0):
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
            self.state = 94
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
            self.state = 96
            self.typeSpec()
            self.state = 97
            self.match(CASSParser.ID)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 98
                self.match(CASSParser.T__4)
                self.state = 99
                self.expression()


            self.state = 102
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
            self.state = 104
            self.match(CASSParser.T__6)
            self.state = 105
            self.match(CASSParser.T__0)
            self.state = 107
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 57344) != 0):
                self.state = 106
                self.forInit()


            self.state = 109
            self.match(CASSParser.T__5)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 481036533762) != 0):
                self.state = 110
                self.expression()


            self.state = 113
            self.match(CASSParser.T__5)
            self.state = 115
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 481036533762) != 0):
                self.state = 114
                self.forUpdate()


            self.state = 117
            self.match(CASSParser.T__1)
            self.state = 118
            self.match(CASSParser.T__2)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 481036594050) != 0):
                self.state = 119
                self.statement()
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 125
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
            self.state = 127
            self.match(CASSParser.T__6)
            self.state = 128
            self.match(CASSParser.T__0)
            self.state = 130
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 57344) != 0):
                self.state = 129
                self.forInit()


            self.state = 132
            self.match(CASSParser.T__5)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 481036533762) != 0):
                self.state = 133
                self.expression()


            self.state = 136
            self.match(CASSParser.T__5)
            self.state = 138
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 481036533762) != 0):
                self.state = 137
                self.forUpdate()


            self.state = 140
            self.match(CASSParser.T__1)
            self.state = 141
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
            self.state = 143
            self.typeSpec()
            self.state = 144
            self.match(CASSParser.ID)
            self.state = 145
            self.match(CASSParser.T__4)
            self.state = 146
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
            self.state = 148
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
            self.state = 150
            self.match(CASSParser.T__7)
            self.state = 151
            self.match(CASSParser.T__0)
            self.state = 152
            self.expression()
            self.state = 153
            self.match(CASSParser.T__1)
            self.state = 154
            self.match(CASSParser.T__2)
            self.state = 158
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 481036594050) != 0):
                self.state = 155
                self.statement()
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 161
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
            self.state = 163
            self.match(CASSParser.T__7)
            self.state = 164
            self.match(CASSParser.T__0)
            self.state = 165
            self.expression()
            self.state = 166
            self.match(CASSParser.T__1)
            self.state = 167
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
            self.state = 169
            self.match(CASSParser.T__8)
            self.state = 170
            self.match(CASSParser.T__0)
            self.state = 171
            self.expression()
            self.state = 172
            self.match(CASSParser.T__1)
            self.state = 173
            self.match(CASSParser.T__2)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 481036594050) != 0):
                self.state = 174
                self.statement()
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 180
            self.match(CASSParser.T__3)
            self.state = 190
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 181
                self.match(CASSParser.T__9)
                self.state = 182
                self.match(CASSParser.T__2)
                self.state = 186
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & 481036594050) != 0):
                    self.state = 183
                    self.statement()
                    self.state = 188
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 189
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
            self.state = 192
            self.match(CASSParser.T__8)
            self.state = 193
            self.match(CASSParser.T__0)
            self.state = 194
            self.expression()
            self.state = 195
            self.match(CASSParser.T__1)
            self.state = 196
            self.statement()
            self.state = 199
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 197
                self.match(CASSParser.T__9)
                self.state = 198
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
            self.state = 201
            self.match(CASSParser.T__10)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 481036533762) != 0):
                self.state = 202
                self.expression()


            self.state = 205
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
            self.state = 207
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
            self.state = 210
            self.parameter()
            self.state = 215
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==12:
                self.state = 211
                self.match(CASSParser.T__11)
                self.state = 212
                self.parameter()
                self.state = 217
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
            self.state = 218
            self.typeSpec()
            self.state = 219
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
            self.state = 221
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
            self.state = 223
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
            self.state = 230
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 225
                self.unaryExpression()
                self.state = 226
                self.assignmentOperator()
                self.state = 227
                self.assignmentExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 229
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
            self.state = 237
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.match(CASSParser.T__15)
                self.state = 233
                self.unaryExpression()
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 234
                self.match(CASSParser.T__16)
                self.state = 235
                self.unaryExpression()
                pass
            elif token in [1, 36, 37, 38]:
                self.enterOuterAlt(localctx, 3)
                self.state = 236
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
            self.state = 246
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [36]:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.match(CASSParser.ID)
                pass
            elif token in [37]:
                self.enterOuterAlt(localctx, 2)
                self.state = 240
                self.match(CASSParser.INT)
                pass
            elif token in [38]:
                self.enterOuterAlt(localctx, 3)
                self.state = 241
                self.match(CASSParser.FLOAT)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 4)
                self.state = 242
                self.match(CASSParser.T__0)
                self.state = 243
                self.expression()
                self.state = 244
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
            self.state = 248
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
            self.state = 250
            self.logicalAndExpression()
            self.state = 255
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==22:
                self.state = 251
                self.match(CASSParser.T__21)
                self.state = 252
                self.logicalAndExpression()
                self.state = 257
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
            self.state = 258
            self.equalityExpression()
            self.state = 263
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==23:
                self.state = 259
                self.match(CASSParser.T__22)
                self.state = 260
                self.equalityExpression()
                self.state = 265
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
            self.state = 266
            self.relationalExpression()
            self.state = 271
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==24 or _la==25:
                self.state = 267
                _la = self._input.LA(1)
                if not(_la==24 or _la==25):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 268
                self.relationalExpression()
                self.state = 273
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
            self.state = 274
            self.additiveExpression()
            self.state = 279
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 1006632960) != 0):
                self.state = 275
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1006632960) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 276
                self.additiveExpression()
                self.state = 281
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
            self.state = 282
            self.multiplicativeExpression()
            self.state = 287
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30 or _la==31:
                self.state = 283
                _la = self._input.LA(1)
                if not(_la==30 or _la==31):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 284
                self.multiplicativeExpression()
                self.state = 289
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
            self.state = 290
            self.unaryExpression()
            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==32 or _la==33:
                self.state = 291
                _la = self._input.LA(1)
                if not(_la==32 or _la==33):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 292
                self.unaryExpression()
                self.state = 297
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
            self.state = 300
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.additiveExpression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
                self.multiplicativeExpression()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





