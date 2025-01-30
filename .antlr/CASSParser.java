// Generated from /Users/deryaerman/Desktop/School/Uni/DIA/DIA-System-DS-Plagiarism-Checker-GIT/CASS.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class CASSParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, T__10=11, T__11=12, T__12=13, T__13=14, T__14=15, T__15=16, T__16=17, 
		T__17=18, T__18=19, T__19=20, T__20=21, T__21=22, T__22=23, T__23=24, 
		T__24=25, T__25=26, T__26=27, T__27=28, T__28=29, T__29=30, T__30=31, 
		T__31=32, T__32=33, T__33=34, T__34=35, T__35=36, T__36=37, T__37=38, 
		T__38=39, T__39=40, T__40=41, T__41=42, T__42=43, T__43=44, SL_COMMENT=45, 
		ML_COMMENT=46, ID=47, INT=48, BOOL=49, FLOAT=50, CHAR=51, POINTER=52, 
		STRING=53, WS=54;
	public static final int
		RULE_prog = 0, RULE_functionDefinition = 1, RULE_compoundStatement = 2, 
		RULE_statement = 3, RULE_declarationStatement = 4, RULE_forBlockStatement = 5, 
		RULE_forSingleStatement = 6, RULE_conditionClause = 7, RULE_whileBlockStatement = 8, 
		RULE_whileSingleStatement = 9, RULE_ifBlockStatement = 10, RULE_ifSingleStatement = 11, 
		RULE_elseClause = 12, RULE_switchStatement = 13, RULE_caseStatement = 14, 
		RULE_functionCall = 15, RULE_arrayDeclarator = 16, RULE_listInitializer = 17, 
		RULE_emptyInitializer = 18, RULE_nullptr = 19, RULE_argumentList = 20, 
		RULE_returnStatement = 21, RULE_expressionStatement = 22, RULE_includeStatement = 23, 
		RULE_parameterList = 24, RULE_parameter = 25, RULE_typeSpec = 26, RULE_expression = 27, 
		RULE_defaultExpression = 28, RULE_breakExpression = 29, RULE_assignmentExpression = 30, 
		RULE_unaryExpression = 31, RULE_comparingExpression = 32, RULE_primaryExpression = 33, 
		RULE_pointerExpression = 34, RULE_assignmentOperator = 35, RULE_logicalOrExpression = 36, 
		RULE_logicalAndExpression = 37, RULE_equalityExpression = 38, RULE_relationalExpression = 39, 
		RULE_additiveExpression = 40, RULE_multiplicativeExpression = 41, RULE_operationExpression = 42;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "functionDefinition", "compoundStatement", "statement", "declarationStatement", 
			"forBlockStatement", "forSingleStatement", "conditionClause", "whileBlockStatement", 
			"whileSingleStatement", "ifBlockStatement", "ifSingleStatement", "elseClause", 
			"switchStatement", "caseStatement", "functionCall", "arrayDeclarator", 
			"listInitializer", "emptyInitializer", "nullptr", "argumentList", "returnStatement", 
			"expressionStatement", "includeStatement", "parameterList", "parameter", 
			"typeSpec", "expression", "defaultExpression", "breakExpression", "assignmentExpression", 
			"unaryExpression", "comparingExpression", "primaryExpression", "pointerExpression", 
			"assignmentOperator", "logicalOrExpression", "logicalAndExpression", 
			"equalityExpression", "relationalExpression", "additiveExpression", "multiplicativeExpression", 
			"operationExpression"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'{'", "'}'", "'='", "';'", "'for'", "'while'", "'if'", 
			"'else'", "'switch'", "'case'", "':'", "'['", "']'", "','", "'nullptr'", 
			"'return'", "'include'", "'int'", "'float'", "'double'", "'void'", "'default'", 
			"'break'", "'++'", "'--'", "'>'", "'<'", "'<='", "'>='", "'&'", "'+='", 
			"'-='", "'*='", "'/='", "'||'", "'&&'", "'=='", "'!='", "'+'", "'-'", 
			"'/'", "'%'", null, null, null, null, null, null, null, "'*'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, "SL_COMMENT", "ML_COMMENT", 
			"ID", "INT", "BOOL", "FLOAT", "CHAR", "POINTER", "STRING", "WS"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "CASS.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public CASSParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ProgContext extends ParserRuleContext {
		public TerminalNode EOF() { return getToken(CASSParser.EOF, 0); }
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public ProgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_prog; }
	}

	public final ProgContext prog() throws RecognitionException {
		ProgContext _localctx = new ProgContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_prog);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(87); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(86);
				statement();
				}
				}
				setState(89); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 17873665550719882L) != 0) );
			setState(91);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionDefinitionContext extends ParserRuleContext {
		public TypeSpecContext typeSpec() {
			return getRuleContext(TypeSpecContext.class,0);
		}
		public PrimaryExpressionContext primaryExpression() {
			return getRuleContext(PrimaryExpressionContext.class,0);
		}
		public CompoundStatementContext compoundStatement() {
			return getRuleContext(CompoundStatementContext.class,0);
		}
		public ParameterListContext parameterList() {
			return getRuleContext(ParameterListContext.class,0);
		}
		public FunctionDefinitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionDefinition; }
	}

	public final FunctionDefinitionContext functionDefinition() throws RecognitionException {
		FunctionDefinitionContext _localctx = new FunctionDefinitionContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_functionDefinition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(93);
			typeSpec();
			setState(94);
			primaryExpression();
			setState(95);
			match(T__0);
			setState(97);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 15728640L) != 0)) {
				{
				setState(96);
				parameterList();
				}
			}

			setState(99);
			match(T__1);
			setState(100);
			compoundStatement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CompoundStatementContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public CompoundStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_compoundStatement; }
	}

	public final CompoundStatementContext compoundStatement() throws RecognitionException {
		CompoundStatementContext _localctx = new CompoundStatementContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_compoundStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(102);
			match(T__2);
			setState(106);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 17873665550719882L) != 0)) {
				{
				{
				setState(103);
				statement();
				}
				}
				setState(108);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(109);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class StatementContext extends ParserRuleContext {
		public DeclarationStatementContext declarationStatement() {
			return getRuleContext(DeclarationStatementContext.class,0);
		}
		public ForBlockStatementContext forBlockStatement() {
			return getRuleContext(ForBlockStatementContext.class,0);
		}
		public ForSingleStatementContext forSingleStatement() {
			return getRuleContext(ForSingleStatementContext.class,0);
		}
		public WhileBlockStatementContext whileBlockStatement() {
			return getRuleContext(WhileBlockStatementContext.class,0);
		}
		public WhileSingleStatementContext whileSingleStatement() {
			return getRuleContext(WhileSingleStatementContext.class,0);
		}
		public IfBlockStatementContext ifBlockStatement() {
			return getRuleContext(IfBlockStatementContext.class,0);
		}
		public IfSingleStatementContext ifSingleStatement() {
			return getRuleContext(IfSingleStatementContext.class,0);
		}
		public ReturnStatementContext returnStatement() {
			return getRuleContext(ReturnStatementContext.class,0);
		}
		public SwitchStatementContext switchStatement() {
			return getRuleContext(SwitchStatementContext.class,0);
		}
		public CaseStatementContext caseStatement() {
			return getRuleContext(CaseStatementContext.class,0);
		}
		public ExpressionStatementContext expressionStatement() {
			return getRuleContext(ExpressionStatementContext.class,0);
		}
		public FunctionDefinitionContext functionDefinition() {
			return getRuleContext(FunctionDefinitionContext.class,0);
		}
		public IncludeStatementContext includeStatement() {
			return getRuleContext(IncludeStatementContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_statement);
		try {
			setState(124);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(111);
				declarationStatement();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(112);
				forBlockStatement();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(113);
				forSingleStatement();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(114);
				whileBlockStatement();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(115);
				whileSingleStatement();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(116);
				ifBlockStatement();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(117);
				ifSingleStatement();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(118);
				returnStatement();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(119);
				switchStatement();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(120);
				caseStatement();
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(121);
				expressionStatement();
				}
				break;
			case 12:
				enterOuterAlt(_localctx, 12);
				{
				setState(122);
				functionDefinition();
				}
				break;
			case 13:
				enterOuterAlt(_localctx, 13);
				{
				setState(123);
				includeStatement();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DeclarationStatementContext extends ParserRuleContext {
		public TypeSpecContext typeSpec() {
			return getRuleContext(TypeSpecContext.class,0);
		}
		public PrimaryExpressionContext primaryExpression() {
			return getRuleContext(PrimaryExpressionContext.class,0);
		}
		public ArrayDeclaratorContext arrayDeclarator() {
			return getRuleContext(ArrayDeclaratorContext.class,0);
		}
		public List<TerminalNode> POINTER() { return getTokens(CASSParser.POINTER); }
		public TerminalNode POINTER(int i) {
			return getToken(CASSParser.POINTER, i);
		}
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public NullptrContext nullptr() {
			return getRuleContext(NullptrContext.class,0);
		}
		public EmptyInitializerContext emptyInitializer() {
			return getRuleContext(EmptyInitializerContext.class,0);
		}
		public DeclarationStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declarationStatement; }
	}

	public final DeclarationStatementContext declarationStatement() throws RecognitionException {
		DeclarationStatementContext _localctx = new DeclarationStatementContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_declarationStatement);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(126);
			typeSpec();
			setState(130);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(127);
					match(POINTER);
					}
					} 
				}
				setState(132);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			}
			setState(136);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				{
				setState(133);
				primaryExpression();
				}
				break;
			case 2:
				{
				}
				break;
			case 3:
				{
				setState(135);
				arrayDeclarator();
				}
				break;
			}
			setState(148);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__4) {
				{
				setState(138);
				match(T__4);
				setState(146);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
				case 1:
					{
					setState(139);
					statement();
					}
					break;
				case 2:
					{
					setState(140);
					nullptr();
					setState(141);
					match(T__5);
					}
					break;
				case 3:
					{
					setState(143);
					emptyInitializer();
					setState(144);
					match(T__5);
					}
					break;
				}
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForBlockStatementContext extends ParserRuleContext {
		public CompoundStatementContext compoundStatement() {
			return getRuleContext(CompoundStatementContext.class,0);
		}
		public LogicalOrExpressionContext logicalOrExpression() {
			return getRuleContext(LogicalOrExpressionContext.class,0);
		}
		public UnaryExpressionContext unaryExpression() {
			return getRuleContext(UnaryExpressionContext.class,0);
		}
		public DeclarationStatementContext declarationStatement() {
			return getRuleContext(DeclarationStatementContext.class,0);
		}
		public AssignmentExpressionContext assignmentExpression() {
			return getRuleContext(AssignmentExpressionContext.class,0);
		}
		public ForBlockStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forBlockStatement; }
	}

	public final ForBlockStatementContext forBlockStatement() throws RecognitionException {
		ForBlockStatementContext _localctx = new ForBlockStatementContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_forBlockStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(150);
			match(T__6);
			setState(151);
			match(T__0);
			setState(159);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,10,_ctx) ) {
			case 1:
				{
				setState(153);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 15728640L) != 0)) {
					{
					setState(152);
					declarationStatement();
					}
				}

				}
				break;
			case 2:
				{
				}
				break;
			case 3:
				{
				setState(157);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 17873665517420554L) != 0)) {
					{
					setState(156);
					assignmentExpression();
					}
				}

				}
				break;
			}
			setState(161);
			match(T__5);
			setState(163);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 17873665517420554L) != 0)) {
				{
				setState(162);
				logicalOrExpression();
				}
			}

			setState(165);
			match(T__5);
			setState(167);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 17873665517420554L) != 0)) {
				{
				setState(166);
				unaryExpression(0);
				}
			}

			setState(169);
			match(T__1);
			setState(170);
			compoundStatement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ForSingleStatementContext extends ParserRuleContext {
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public LogicalOrExpressionContext logicalOrExpression() {
			return getRuleContext(LogicalOrExpressionContext.class,0);
		}
		public UnaryExpressionContext unaryExpression() {
			return getRuleContext(UnaryExpressionContext.class,0);
		}
		public DeclarationStatementContext declarationStatement() {
			return getRuleContext(DeclarationStatementContext.class,0);
		}
		public AssignmentExpressionContext assignmentExpression() {
			return getRuleContext(AssignmentExpressionContext.class,0);
		}
		public ForSingleStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_forSingleStatement; }
	}

	public final ForSingleStatementContext forSingleStatement() throws RecognitionException {
		ForSingleStatementContext _localctx = new ForSingleStatementContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_forSingleStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(172);
			match(T__6);
			setState(173);
			match(T__0);
			setState(181);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,15,_ctx) ) {
			case 1:
				{
				setState(175);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 15728640L) != 0)) {
					{
					setState(174);
					declarationStatement();
					}
				}

				}
				break;
			case 2:
				{
				}
				break;
			case 3:
				{
				setState(179);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 17873665517420554L) != 0)) {
					{
					setState(178);
					assignmentExpression();
					}
				}

				}
				break;
			}
			setState(183);
			match(T__5);
			setState(185);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 17873665517420554L) != 0)) {
				{
				setState(184);
				logicalOrExpression();
				}
			}

			setState(187);
			match(T__5);
			setState(189);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 17873665517420554L) != 0)) {
				{
				setState(188);
				unaryExpression(0);
				}
			}

			setState(191);
			match(T__1);
			setState(192);
			statement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ConditionClauseContext extends ParserRuleContext {
		public LogicalOrExpressionContext logicalOrExpression() {
			return getRuleContext(LogicalOrExpressionContext.class,0);
		}
		public ConditionClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_conditionClause; }
	}

	public final ConditionClauseContext conditionClause() throws RecognitionException {
		ConditionClauseContext _localctx = new ConditionClauseContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_conditionClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(194);
			logicalOrExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhileBlockStatementContext extends ParserRuleContext {
		public ConditionClauseContext conditionClause() {
			return getRuleContext(ConditionClauseContext.class,0);
		}
		public CompoundStatementContext compoundStatement() {
			return getRuleContext(CompoundStatementContext.class,0);
		}
		public WhileBlockStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileBlockStatement; }
	}

	public final WhileBlockStatementContext whileBlockStatement() throws RecognitionException {
		WhileBlockStatementContext _localctx = new WhileBlockStatementContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_whileBlockStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(196);
			match(T__7);
			setState(197);
			match(T__0);
			setState(198);
			conditionClause();
			setState(199);
			match(T__1);
			setState(200);
			compoundStatement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class WhileSingleStatementContext extends ParserRuleContext {
		public ConditionClauseContext conditionClause() {
			return getRuleContext(ConditionClauseContext.class,0);
		}
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public WhileSingleStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_whileSingleStatement; }
	}

	public final WhileSingleStatementContext whileSingleStatement() throws RecognitionException {
		WhileSingleStatementContext _localctx = new WhileSingleStatementContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_whileSingleStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(202);
			match(T__7);
			setState(203);
			match(T__0);
			setState(204);
			conditionClause();
			setState(205);
			match(T__1);
			setState(206);
			statement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfBlockStatementContext extends ParserRuleContext {
		public ConditionClauseContext conditionClause() {
			return getRuleContext(ConditionClauseContext.class,0);
		}
		public CompoundStatementContext compoundStatement() {
			return getRuleContext(CompoundStatementContext.class,0);
		}
		public ElseClauseContext elseClause() {
			return getRuleContext(ElseClauseContext.class,0);
		}
		public IfBlockStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifBlockStatement; }
	}

	public final IfBlockStatementContext ifBlockStatement() throws RecognitionException {
		IfBlockStatementContext _localctx = new IfBlockStatementContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_ifBlockStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(208);
			match(T__8);
			setState(209);
			match(T__0);
			setState(210);
			conditionClause();
			setState(211);
			match(T__1);
			setState(212);
			compoundStatement();
			setState(214);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,18,_ctx) ) {
			case 1:
				{
				setState(213);
				elseClause();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IfSingleStatementContext extends ParserRuleContext {
		public ConditionClauseContext conditionClause() {
			return getRuleContext(ConditionClauseContext.class,0);
		}
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public ElseClauseContext elseClause() {
			return getRuleContext(ElseClauseContext.class,0);
		}
		public IfSingleStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_ifSingleStatement; }
	}

	public final IfSingleStatementContext ifSingleStatement() throws RecognitionException {
		IfSingleStatementContext _localctx = new IfSingleStatementContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_ifSingleStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(216);
			match(T__8);
			setState(217);
			match(T__0);
			setState(218);
			conditionClause();
			setState(219);
			match(T__1);
			setState(220);
			statement();
			setState(222);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				{
				setState(221);
				elseClause();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ElseClauseContext extends ParserRuleContext {
		public CompoundStatementContext compoundStatement() {
			return getRuleContext(CompoundStatementContext.class,0);
		}
		public IfBlockStatementContext ifBlockStatement() {
			return getRuleContext(IfBlockStatementContext.class,0);
		}
		public StatementContext statement() {
			return getRuleContext(StatementContext.class,0);
		}
		public ElseClauseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_elseClause; }
	}

	public final ElseClauseContext elseClause() throws RecognitionException {
		ElseClauseContext _localctx = new ElseClauseContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_elseClause);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(224);
			match(T__9);
			setState(228);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				{
				setState(225);
				compoundStatement();
				}
				break;
			case 2:
				{
				setState(226);
				ifBlockStatement();
				}
				break;
			case 3:
				{
				setState(227);
				statement();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class SwitchStatementContext extends ParserRuleContext {
		public ConditionClauseContext conditionClause() {
			return getRuleContext(ConditionClauseContext.class,0);
		}
		public CompoundStatementContext compoundStatement() {
			return getRuleContext(CompoundStatementContext.class,0);
		}
		public SwitchStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_switchStatement; }
	}

	public final SwitchStatementContext switchStatement() throws RecognitionException {
		SwitchStatementContext _localctx = new SwitchStatementContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_switchStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(230);
			match(T__10);
			setState(231);
			match(T__0);
			setState(232);
			conditionClause();
			setState(233);
			match(T__1);
			setState(234);
			compoundStatement();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class CaseStatementContext extends ParserRuleContext {
		public DefaultExpressionContext defaultExpression() {
			return getRuleContext(DefaultExpressionContext.class,0);
		}
		public PrimaryExpressionContext primaryExpression() {
			return getRuleContext(PrimaryExpressionContext.class,0);
		}
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BreakExpressionContext breakExpression() {
			return getRuleContext(BreakExpressionContext.class,0);
		}
		public CaseStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_caseStatement; }
	}

	public final CaseStatementContext caseStatement() throws RecognitionException {
		CaseStatementContext _localctx = new CaseStatementContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_caseStatement);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(238);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__11:
				{
				setState(236);
				match(T__11);
				}
				break;
			case T__23:
				{
				setState(237);
				defaultExpression();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(241);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 13370061393756162L) != 0)) {
				{
				setState(240);
				primaryExpression();
				}
			}

			setState(243);
			match(T__12);
			setState(247);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(244);
					statement();
					}
					} 
				}
				setState(249);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,23,_ctx);
			}
			setState(251);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,24,_ctx) ) {
			case 1:
				{
				setState(250);
				breakExpression();
				}
				break;
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class FunctionCallContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(CASSParser.ID, 0); }
		public ArgumentListContext argumentList() {
			return getRuleContext(ArgumentListContext.class,0);
		}
		public FunctionCallContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_functionCall; }
	}

	public final FunctionCallContext functionCall() throws RecognitionException {
		FunctionCallContext _localctx = new FunctionCallContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_functionCall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(253);
			match(ID);
			setState(254);
			match(T__0);
			setState(256);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 17873665517420554L) != 0)) {
				{
				setState(255);
				argumentList();
				}
			}

			setState(258);
			match(T__1);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArrayDeclaratorContext extends ParserRuleContext {
		public List<PrimaryExpressionContext> primaryExpression() {
			return getRuleContexts(PrimaryExpressionContext.class);
		}
		public PrimaryExpressionContext primaryExpression(int i) {
			return getRuleContext(PrimaryExpressionContext.class,i);
		}
		public ArrayDeclaratorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arrayDeclarator; }
	}

	public final ArrayDeclaratorContext arrayDeclarator() throws RecognitionException {
		ArrayDeclaratorContext _localctx = new ArrayDeclaratorContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_arrayDeclarator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(260);
			primaryExpression();
			setState(261);
			match(T__13);
			setState(263);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 13370061393756162L) != 0)) {
				{
				setState(262);
				primaryExpression();
				}
			}

			setState(265);
			match(T__14);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ListInitializerContext extends ParserRuleContext {
		public List<PrimaryExpressionContext> primaryExpression() {
			return getRuleContexts(PrimaryExpressionContext.class);
		}
		public PrimaryExpressionContext primaryExpression(int i) {
			return getRuleContext(PrimaryExpressionContext.class,i);
		}
		public ListInitializerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_listInitializer; }
	}

	public final ListInitializerContext listInitializer() throws RecognitionException {
		ListInitializerContext _localctx = new ListInitializerContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_listInitializer);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(267);
			match(T__2);
			setState(268);
			primaryExpression();
			setState(273);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__15) {
				{
				{
				setState(269);
				match(T__15);
				setState(270);
				primaryExpression();
				}
				}
				setState(275);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(276);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EmptyInitializerContext extends ParserRuleContext {
		public EmptyInitializerContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_emptyInitializer; }
	}

	public final EmptyInitializerContext emptyInitializer() throws RecognitionException {
		EmptyInitializerContext _localctx = new EmptyInitializerContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_emptyInitializer);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(278);
			match(T__2);
			setState(279);
			match(T__3);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class NullptrContext extends ParserRuleContext {
		public NullptrContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_nullptr; }
	}

	public final NullptrContext nullptr() throws RecognitionException {
		NullptrContext _localctx = new NullptrContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_nullptr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(281);
			match(T__16);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ArgumentListContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public ArgumentListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_argumentList; }
	}

	public final ArgumentListContext argumentList() throws RecognitionException {
		ArgumentListContext _localctx = new ArgumentListContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_argumentList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(283);
			expression();
			setState(288);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__15) {
				{
				{
				setState(284);
				match(T__15);
				setState(285);
				expression();
				}
				}
				setState(290);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ReturnStatementContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ReturnStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_returnStatement; }
	}

	public final ReturnStatementContext returnStatement() throws RecognitionException {
		ReturnStatementContext _localctx = new ReturnStatementContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_returnStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(291);
			match(T__17);
			setState(293);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 17873665517420554L) != 0)) {
				{
				setState(292);
				expression();
				}
			}

			setState(295);
			match(T__5);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionStatementContext extends ParserRuleContext {
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public ExpressionStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expressionStatement; }
	}

	public final ExpressionStatementContext expressionStatement() throws RecognitionException {
		ExpressionStatementContext _localctx = new ExpressionStatementContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_expressionStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(297);
			expression();
			setState(298);
			match(T__5);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class IncludeStatementContext extends ParserRuleContext {
		public TerminalNode STRING() { return getToken(CASSParser.STRING, 0); }
		public IncludeStatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_includeStatement; }
	}

	public final IncludeStatementContext includeStatement() throws RecognitionException {
		IncludeStatementContext _localctx = new IncludeStatementContext(_ctx, getState());
		enterRule(_localctx, 46, RULE_includeStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(300);
			match(T__18);
			setState(301);
			match(STRING);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParameterListContext extends ParserRuleContext {
		public List<ParameterContext> parameter() {
			return getRuleContexts(ParameterContext.class);
		}
		public ParameterContext parameter(int i) {
			return getRuleContext(ParameterContext.class,i);
		}
		public ParameterListContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameterList; }
	}

	public final ParameterListContext parameterList() throws RecognitionException {
		ParameterListContext _localctx = new ParameterListContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_parameterList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(303);
			parameter();
			setState(308);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__15) {
				{
				{
				setState(304);
				match(T__15);
				setState(305);
				parameter();
				}
				}
				setState(310);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ParameterContext extends ParserRuleContext {
		public TypeSpecContext typeSpec() {
			return getRuleContext(TypeSpecContext.class,0);
		}
		public PrimaryExpressionContext primaryExpression() {
			return getRuleContext(PrimaryExpressionContext.class,0);
		}
		public ParameterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_parameter; }
	}

	public final ParameterContext parameter() throws RecognitionException {
		ParameterContext _localctx = new ParameterContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_parameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(311);
			typeSpec();
			setState(312);
			primaryExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class TypeSpecContext extends ParserRuleContext {
		public TypeSpecContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_typeSpec; }
	}

	public final TypeSpecContext typeSpec() throws RecognitionException {
		TypeSpecContext _localctx = new TypeSpecContext(_ctx, getState());
		enterRule(_localctx, 52, RULE_typeSpec);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(314);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 15728640L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ExpressionContext extends ParserRuleContext {
		public AssignmentExpressionContext assignmentExpression() {
			return getRuleContext(AssignmentExpressionContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 54, RULE_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(316);
			assignmentExpression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class DefaultExpressionContext extends ParserRuleContext {
		public DefaultExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_defaultExpression; }
	}

	public final DefaultExpressionContext defaultExpression() throws RecognitionException {
		DefaultExpressionContext _localctx = new DefaultExpressionContext(_ctx, getState());
		enterRule(_localctx, 56, RULE_defaultExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(318);
			match(T__23);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class BreakExpressionContext extends ParserRuleContext {
		public BreakExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_breakExpression; }
	}

	public final BreakExpressionContext breakExpression() throws RecognitionException {
		BreakExpressionContext _localctx = new BreakExpressionContext(_ctx, getState());
		enterRule(_localctx, 58, RULE_breakExpression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(320);
			match(T__24);
			setState(321);
			match(T__5);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentExpressionContext extends ParserRuleContext {
		public UnaryExpressionContext unaryExpression() {
			return getRuleContext(UnaryExpressionContext.class,0);
		}
		public AssignmentOperatorContext assignmentOperator() {
			return getRuleContext(AssignmentOperatorContext.class,0);
		}
		public AssignmentExpressionContext assignmentExpression() {
			return getRuleContext(AssignmentExpressionContext.class,0);
		}
		public NullptrContext nullptr() {
			return getRuleContext(NullptrContext.class,0);
		}
		public EmptyInitializerContext emptyInitializer() {
			return getRuleContext(EmptyInitializerContext.class,0);
		}
		public LogicalOrExpressionContext logicalOrExpression() {
			return getRuleContext(LogicalOrExpressionContext.class,0);
		}
		public AssignmentExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignmentExpression; }
	}

	public final AssignmentExpressionContext assignmentExpression() throws RecognitionException {
		AssignmentExpressionContext _localctx = new AssignmentExpressionContext(_ctx, getState());
		enterRule(_localctx, 60, RULE_assignmentExpression);
		try {
			setState(333);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,33,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(323);
				unaryExpression(0);
				setState(324);
				assignmentOperator();
				setState(325);
				assignmentExpression();
				setState(327);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,31,_ctx) ) {
				case 1:
					{
					setState(326);
					nullptr();
					}
					break;
				}
				setState(330);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,32,_ctx) ) {
				case 1:
					{
					setState(329);
					emptyInitializer();
					}
					break;
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(332);
				logicalOrExpression();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class UnaryExpressionContext extends ParserRuleContext {
		public UnaryExpressionContext unaryExpression() {
			return getRuleContext(UnaryExpressionContext.class,0);
		}
		public PointerExpressionContext pointerExpression() {
			return getRuleContext(PointerExpressionContext.class,0);
		}
		public PrimaryExpressionContext primaryExpression() {
			return getRuleContext(PrimaryExpressionContext.class,0);
		}
		public ListInitializerContext listInitializer() {
			return getRuleContext(ListInitializerContext.class,0);
		}
		public UnaryExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_unaryExpression; }
	}

	public final UnaryExpressionContext unaryExpression() throws RecognitionException {
		return unaryExpression(0);
	}

	private UnaryExpressionContext unaryExpression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		UnaryExpressionContext _localctx = new UnaryExpressionContext(_ctx, _parentState);
		UnaryExpressionContext _prevctx = _localctx;
		int _startState = 62;
		enterRecursionRule(_localctx, 62, RULE_unaryExpression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(341);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__25:
			case T__26:
				{
				setState(336);
				_la = _input.LA(1);
				if ( !(_la==T__25 || _la==T__26) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(337);
				unaryExpression(5);
				}
				break;
			case T__31:
			case POINTER:
				{
				setState(338);
				pointerExpression();
				}
				break;
			case T__0:
			case ID:
			case INT:
			case BOOL:
			case FLOAT:
			case CHAR:
			case STRING:
				{
				setState(339);
				primaryExpression();
				}
				break;
			case T__2:
				{
				setState(340);
				listInitializer();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(347);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,35,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new UnaryExpressionContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_unaryExpression);
					setState(343);
					if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
					setState(344);
					_la = _input.LA(1);
					if ( !(_la==T__25 || _la==T__26) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					}
					} 
				}
				setState(349);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,35,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class ComparingExpressionContext extends ParserRuleContext {
		public ComparingExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparingExpression; }
	}

	public final ComparingExpressionContext comparingExpression() throws RecognitionException {
		ComparingExpressionContext _localctx = new ComparingExpressionContext(_ctx, getState());
		enterRule(_localctx, 64, RULE_comparingExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(350);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 4026531840L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PrimaryExpressionContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(CASSParser.ID, 0); }
		public TerminalNode INT() { return getToken(CASSParser.INT, 0); }
		public TerminalNode FLOAT() { return getToken(CASSParser.FLOAT, 0); }
		public TerminalNode CHAR() { return getToken(CASSParser.CHAR, 0); }
		public TerminalNode STRING() { return getToken(CASSParser.STRING, 0); }
		public TerminalNode BOOL() { return getToken(CASSParser.BOOL, 0); }
		public FunctionCallContext functionCall() {
			return getRuleContext(FunctionCallContext.class,0);
		}
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public PrimaryExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_primaryExpression; }
	}

	public final PrimaryExpressionContext primaryExpression() throws RecognitionException {
		PrimaryExpressionContext _localctx = new PrimaryExpressionContext(_ctx, getState());
		enterRule(_localctx, 66, RULE_primaryExpression);
		try {
			setState(363);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,36,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(352);
				match(ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(353);
				match(INT);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(354);
				match(FLOAT);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(355);
				match(CHAR);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(356);
				match(STRING);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(357);
				match(BOOL);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(358);
				functionCall();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(359);
				match(T__0);
				setState(360);
				expression();
				setState(361);
				match(T__1);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class PointerExpressionContext extends ParserRuleContext {
		public PrimaryExpressionContext primaryExpression() {
			return getRuleContext(PrimaryExpressionContext.class,0);
		}
		public TerminalNode POINTER() { return getToken(CASSParser.POINTER, 0); }
		public PointerExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_pointerExpression; }
	}

	public final PointerExpressionContext pointerExpression() throws RecognitionException {
		PointerExpressionContext _localctx = new PointerExpressionContext(_ctx, getState());
		enterRule(_localctx, 68, RULE_pointerExpression);
		try {
			setState(369);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__31:
				enterOuterAlt(_localctx, 1);
				{
				setState(365);
				match(T__31);
				setState(366);
				primaryExpression();
				}
				break;
			case POINTER:
				enterOuterAlt(_localctx, 2);
				{
				setState(367);
				match(POINTER);
				setState(368);
				primaryExpression();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AssignmentOperatorContext extends ParserRuleContext {
		public AssignmentOperatorContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignmentOperator; }
	}

	public final AssignmentOperatorContext assignmentOperator() throws RecognitionException {
		AssignmentOperatorContext _localctx = new AssignmentOperatorContext(_ctx, getState());
		enterRule(_localctx, 70, RULE_assignmentOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(371);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 128849018912L) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LogicalOrExpressionContext extends ParserRuleContext {
		public List<LogicalAndExpressionContext> logicalAndExpression() {
			return getRuleContexts(LogicalAndExpressionContext.class);
		}
		public LogicalAndExpressionContext logicalAndExpression(int i) {
			return getRuleContext(LogicalAndExpressionContext.class,i);
		}
		public LogicalOrExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logicalOrExpression; }
	}

	public final LogicalOrExpressionContext logicalOrExpression() throws RecognitionException {
		LogicalOrExpressionContext _localctx = new LogicalOrExpressionContext(_ctx, getState());
		enterRule(_localctx, 72, RULE_logicalOrExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(373);
			logicalAndExpression();
			setState(378);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__36) {
				{
				{
				setState(374);
				match(T__36);
				setState(375);
				logicalAndExpression();
				}
				}
				setState(380);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class LogicalAndExpressionContext extends ParserRuleContext {
		public List<EqualityExpressionContext> equalityExpression() {
			return getRuleContexts(EqualityExpressionContext.class);
		}
		public EqualityExpressionContext equalityExpression(int i) {
			return getRuleContext(EqualityExpressionContext.class,i);
		}
		public LogicalAndExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_logicalAndExpression; }
	}

	public final LogicalAndExpressionContext logicalAndExpression() throws RecognitionException {
		LogicalAndExpressionContext _localctx = new LogicalAndExpressionContext(_ctx, getState());
		enterRule(_localctx, 74, RULE_logicalAndExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(381);
			equalityExpression();
			setState(386);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__37) {
				{
				{
				setState(382);
				match(T__37);
				setState(383);
				equalityExpression();
				}
				}
				setState(388);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class EqualityExpressionContext extends ParserRuleContext {
		public List<RelationalExpressionContext> relationalExpression() {
			return getRuleContexts(RelationalExpressionContext.class);
		}
		public RelationalExpressionContext relationalExpression(int i) {
			return getRuleContext(RelationalExpressionContext.class,i);
		}
		public EqualityExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_equalityExpression; }
	}

	public final EqualityExpressionContext equalityExpression() throws RecognitionException {
		EqualityExpressionContext _localctx = new EqualityExpressionContext(_ctx, getState());
		enterRule(_localctx, 76, RULE_equalityExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(389);
			relationalExpression();
			setState(394);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__38 || _la==T__39) {
				{
				{
				setState(390);
				_la = _input.LA(1);
				if ( !(_la==T__38 || _la==T__39) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(391);
				relationalExpression();
				}
				}
				setState(396);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class RelationalExpressionContext extends ParserRuleContext {
		public List<AdditiveExpressionContext> additiveExpression() {
			return getRuleContexts(AdditiveExpressionContext.class);
		}
		public AdditiveExpressionContext additiveExpression(int i) {
			return getRuleContext(AdditiveExpressionContext.class,i);
		}
		public RelationalExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_relationalExpression; }
	}

	public final RelationalExpressionContext relationalExpression() throws RecognitionException {
		RelationalExpressionContext _localctx = new RelationalExpressionContext(_ctx, getState());
		enterRule(_localctx, 78, RULE_relationalExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(397);
			additiveExpression();
			setState(402);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4026531840L) != 0)) {
				{
				{
				setState(398);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 4026531840L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(399);
				additiveExpression();
				}
				}
				setState(404);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class AdditiveExpressionContext extends ParserRuleContext {
		public List<MultiplicativeExpressionContext> multiplicativeExpression() {
			return getRuleContexts(MultiplicativeExpressionContext.class);
		}
		public MultiplicativeExpressionContext multiplicativeExpression(int i) {
			return getRuleContext(MultiplicativeExpressionContext.class,i);
		}
		public AdditiveExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_additiveExpression; }
	}

	public final AdditiveExpressionContext additiveExpression() throws RecognitionException {
		AdditiveExpressionContext _localctx = new AdditiveExpressionContext(_ctx, getState());
		enterRule(_localctx, 80, RULE_additiveExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(405);
			multiplicativeExpression();
			setState(410);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__40 || _la==T__41) {
				{
				{
				setState(406);
				_la = _input.LA(1);
				if ( !(_la==T__40 || _la==T__41) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(407);
				multiplicativeExpression();
				}
				}
				setState(412);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class MultiplicativeExpressionContext extends ParserRuleContext {
		public List<UnaryExpressionContext> unaryExpression() {
			return getRuleContexts(UnaryExpressionContext.class);
		}
		public UnaryExpressionContext unaryExpression(int i) {
			return getRuleContext(UnaryExpressionContext.class,i);
		}
		public List<TerminalNode> POINTER() { return getTokens(CASSParser.POINTER); }
		public TerminalNode POINTER(int i) {
			return getToken(CASSParser.POINTER, i);
		}
		public MultiplicativeExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_multiplicativeExpression; }
	}

	public final MultiplicativeExpressionContext multiplicativeExpression() throws RecognitionException {
		MultiplicativeExpressionContext _localctx = new MultiplicativeExpressionContext(_ctx, getState());
		enterRule(_localctx, 82, RULE_multiplicativeExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(413);
			unaryExpression(0);
			setState(418);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 4529987906437120L) != 0)) {
				{
				{
				setState(414);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 4529987906437120L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(415);
				unaryExpression(0);
				}
				}
				setState(420);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	@SuppressWarnings("CheckReturnValue")
	public static class OperationExpressionContext extends ParserRuleContext {
		public AdditiveExpressionContext additiveExpression() {
			return getRuleContext(AdditiveExpressionContext.class,0);
		}
		public MultiplicativeExpressionContext multiplicativeExpression() {
			return getRuleContext(MultiplicativeExpressionContext.class,0);
		}
		public OperationExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_operationExpression; }
	}

	public final OperationExpressionContext operationExpression() throws RecognitionException {
		OperationExpressionContext _localctx = new OperationExpressionContext(_ctx, getState());
		enterRule(_localctx, 84, RULE_operationExpression);
		try {
			setState(423);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,44,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(421);
				additiveExpression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(422);
				multiplicativeExpression();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 31:
			return unaryExpression_sempred((UnaryExpressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean unaryExpression_sempred(UnaryExpressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 4);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u00016\u01aa\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007\u0002"+
		"\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b\u0002"+
		"\f\u0007\f\u0002\r\u0007\r\u0002\u000e\u0007\u000e\u0002\u000f\u0007\u000f"+
		"\u0002\u0010\u0007\u0010\u0002\u0011\u0007\u0011\u0002\u0012\u0007\u0012"+
		"\u0002\u0013\u0007\u0013\u0002\u0014\u0007\u0014\u0002\u0015\u0007\u0015"+
		"\u0002\u0016\u0007\u0016\u0002\u0017\u0007\u0017\u0002\u0018\u0007\u0018"+
		"\u0002\u0019\u0007\u0019\u0002\u001a\u0007\u001a\u0002\u001b\u0007\u001b"+
		"\u0002\u001c\u0007\u001c\u0002\u001d\u0007\u001d\u0002\u001e\u0007\u001e"+
		"\u0002\u001f\u0007\u001f\u0002 \u0007 \u0002!\u0007!\u0002\"\u0007\"\u0002"+
		"#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007&\u0002\'\u0007\'\u0002"+
		"(\u0007(\u0002)\u0007)\u0002*\u0007*\u0001\u0000\u0004\u0000X\b\u0000"+
		"\u000b\u0000\f\u0000Y\u0001\u0000\u0001\u0000\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0003\u0001b\b\u0001\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0002\u0001\u0002\u0005\u0002i\b\u0002\n\u0002\f\u0002"+
		"l\t\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0003\u0003}\b\u0003"+
		"\u0001\u0004\u0001\u0004\u0005\u0004\u0081\b\u0004\n\u0004\f\u0004\u0084"+
		"\t\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0003\u0004\u0089\b\u0004"+
		"\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0004"+
		"\u0001\u0004\u0001\u0004\u0003\u0004\u0093\b\u0004\u0003\u0004\u0095\b"+
		"\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0003\u0005\u009a\b\u0005\u0001"+
		"\u0005\u0001\u0005\u0003\u0005\u009e\b\u0005\u0003\u0005\u00a0\b\u0005"+
		"\u0001\u0005\u0001\u0005\u0003\u0005\u00a4\b\u0005\u0001\u0005\u0001\u0005"+
		"\u0003\u0005\u00a8\b\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0003\u0006\u00b0\b\u0006\u0001\u0006\u0001\u0006"+
		"\u0003\u0006\u00b4\b\u0006\u0003\u0006\u00b6\b\u0006\u0001\u0006\u0001"+
		"\u0006\u0003\u0006\u00ba\b\u0006\u0001\u0006\u0001\u0006\u0003\u0006\u00be"+
		"\b\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\t\u0001\t\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0001\n\u0003"+
		"\n\u00d7\b\n\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b"+
		"\u0001\u000b\u0003\u000b\u00df\b\u000b\u0001\f\u0001\f\u0001\f\u0001\f"+
		"\u0003\f\u00e5\b\f\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001\r\u0001"+
		"\u000e\u0001\u000e\u0003\u000e\u00ef\b\u000e\u0001\u000e\u0003\u000e\u00f2"+
		"\b\u000e\u0001\u000e\u0001\u000e\u0005\u000e\u00f6\b\u000e\n\u000e\f\u000e"+
		"\u00f9\t\u000e\u0001\u000e\u0003\u000e\u00fc\b\u000e\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0003\u000f\u0101\b\u000f\u0001\u000f\u0001\u000f\u0001"+
		"\u0010\u0001\u0010\u0001\u0010\u0003\u0010\u0108\b\u0010\u0001\u0010\u0001"+
		"\u0010\u0001\u0011\u0001\u0011\u0001\u0011\u0001\u0011\u0005\u0011\u0110"+
		"\b\u0011\n\u0011\f\u0011\u0113\t\u0011\u0001\u0011\u0001\u0011\u0001\u0012"+
		"\u0001\u0012\u0001\u0012\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014"+
		"\u0001\u0014\u0005\u0014\u011f\b\u0014\n\u0014\f\u0014\u0122\t\u0014\u0001"+
		"\u0015\u0001\u0015\u0003\u0015\u0126\b\u0015\u0001\u0015\u0001\u0015\u0001"+
		"\u0016\u0001\u0016\u0001\u0016\u0001\u0017\u0001\u0017\u0001\u0017\u0001"+
		"\u0018\u0001\u0018\u0001\u0018\u0005\u0018\u0133\b\u0018\n\u0018\f\u0018"+
		"\u0136\t\u0018\u0001\u0019\u0001\u0019\u0001\u0019\u0001\u001a\u0001\u001a"+
		"\u0001\u001b\u0001\u001b\u0001\u001c\u0001\u001c\u0001\u001d\u0001\u001d"+
		"\u0001\u001d\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0003\u001e"+
		"\u0148\b\u001e\u0001\u001e\u0003\u001e\u014b\b\u001e\u0001\u001e\u0003"+
		"\u001e\u014e\b\u001e\u0001\u001f\u0001\u001f\u0001\u001f\u0001\u001f\u0001"+
		"\u001f\u0001\u001f\u0003\u001f\u0156\b\u001f\u0001\u001f\u0001\u001f\u0005"+
		"\u001f\u015a\b\u001f\n\u001f\f\u001f\u015d\t\u001f\u0001 \u0001 \u0001"+
		"!\u0001!\u0001!\u0001!\u0001!\u0001!\u0001!\u0001!\u0001!\u0001!\u0001"+
		"!\u0003!\u016c\b!\u0001\"\u0001\"\u0001\"\u0001\"\u0003\"\u0172\b\"\u0001"+
		"#\u0001#\u0001$\u0001$\u0001$\u0005$\u0179\b$\n$\f$\u017c\t$\u0001%\u0001"+
		"%\u0001%\u0005%\u0181\b%\n%\f%\u0184\t%\u0001&\u0001&\u0001&\u0005&\u0189"+
		"\b&\n&\f&\u018c\t&\u0001\'\u0001\'\u0001\'\u0005\'\u0191\b\'\n\'\f\'\u0194"+
		"\t\'\u0001(\u0001(\u0001(\u0005(\u0199\b(\n(\f(\u019c\t(\u0001)\u0001"+
		")\u0001)\u0005)\u01a1\b)\n)\f)\u01a4\t)\u0001*\u0001*\u0003*\u01a8\b*"+
		"\u0001*\u0000\u0001>+\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012"+
		"\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,.02468:<>@BDFHJLNPRT\u0000"+
		"\u0007\u0001\u0000\u0014\u0017\u0001\u0000\u001a\u001b\u0001\u0000\u001c"+
		"\u001f\u0002\u0000\u0005\u0005!$\u0001\u0000\'(\u0001\u0000)*\u0002\u0000"+
		"+,44\u01c3\u0000W\u0001\u0000\u0000\u0000\u0002]\u0001\u0000\u0000\u0000"+
		"\u0004f\u0001\u0000\u0000\u0000\u0006|\u0001\u0000\u0000\u0000\b~\u0001"+
		"\u0000\u0000\u0000\n\u0096\u0001\u0000\u0000\u0000\f\u00ac\u0001\u0000"+
		"\u0000\u0000\u000e\u00c2\u0001\u0000\u0000\u0000\u0010\u00c4\u0001\u0000"+
		"\u0000\u0000\u0012\u00ca\u0001\u0000\u0000\u0000\u0014\u00d0\u0001\u0000"+
		"\u0000\u0000\u0016\u00d8\u0001\u0000\u0000\u0000\u0018\u00e0\u0001\u0000"+
		"\u0000\u0000\u001a\u00e6\u0001\u0000\u0000\u0000\u001c\u00ee\u0001\u0000"+
		"\u0000\u0000\u001e\u00fd\u0001\u0000\u0000\u0000 \u0104\u0001\u0000\u0000"+
		"\u0000\"\u010b\u0001\u0000\u0000\u0000$\u0116\u0001\u0000\u0000\u0000"+
		"&\u0119\u0001\u0000\u0000\u0000(\u011b\u0001\u0000\u0000\u0000*\u0123"+
		"\u0001\u0000\u0000\u0000,\u0129\u0001\u0000\u0000\u0000.\u012c\u0001\u0000"+
		"\u0000\u00000\u012f\u0001\u0000\u0000\u00002\u0137\u0001\u0000\u0000\u0000"+
		"4\u013a\u0001\u0000\u0000\u00006\u013c\u0001\u0000\u0000\u00008\u013e"+
		"\u0001\u0000\u0000\u0000:\u0140\u0001\u0000\u0000\u0000<\u014d\u0001\u0000"+
		"\u0000\u0000>\u0155\u0001\u0000\u0000\u0000@\u015e\u0001\u0000\u0000\u0000"+
		"B\u016b\u0001\u0000\u0000\u0000D\u0171\u0001\u0000\u0000\u0000F\u0173"+
		"\u0001\u0000\u0000\u0000H\u0175\u0001\u0000\u0000\u0000J\u017d\u0001\u0000"+
		"\u0000\u0000L\u0185\u0001\u0000\u0000\u0000N\u018d\u0001\u0000\u0000\u0000"+
		"P\u0195\u0001\u0000\u0000\u0000R\u019d\u0001\u0000\u0000\u0000T\u01a7"+
		"\u0001\u0000\u0000\u0000VX\u0003\u0006\u0003\u0000WV\u0001\u0000\u0000"+
		"\u0000XY\u0001\u0000\u0000\u0000YW\u0001\u0000\u0000\u0000YZ\u0001\u0000"+
		"\u0000\u0000Z[\u0001\u0000\u0000\u0000[\\\u0005\u0000\u0000\u0001\\\u0001"+
		"\u0001\u0000\u0000\u0000]^\u00034\u001a\u0000^_\u0003B!\u0000_a\u0005"+
		"\u0001\u0000\u0000`b\u00030\u0018\u0000a`\u0001\u0000\u0000\u0000ab\u0001"+
		"\u0000\u0000\u0000bc\u0001\u0000\u0000\u0000cd\u0005\u0002\u0000\u0000"+
		"de\u0003\u0004\u0002\u0000e\u0003\u0001\u0000\u0000\u0000fj\u0005\u0003"+
		"\u0000\u0000gi\u0003\u0006\u0003\u0000hg\u0001\u0000\u0000\u0000il\u0001"+
		"\u0000\u0000\u0000jh\u0001\u0000\u0000\u0000jk\u0001\u0000\u0000\u0000"+
		"km\u0001\u0000\u0000\u0000lj\u0001\u0000\u0000\u0000mn\u0005\u0004\u0000"+
		"\u0000n\u0005\u0001\u0000\u0000\u0000o}\u0003\b\u0004\u0000p}\u0003\n"+
		"\u0005\u0000q}\u0003\f\u0006\u0000r}\u0003\u0010\b\u0000s}\u0003\u0012"+
		"\t\u0000t}\u0003\u0014\n\u0000u}\u0003\u0016\u000b\u0000v}\u0003*\u0015"+
		"\u0000w}\u0003\u001a\r\u0000x}\u0003\u001c\u000e\u0000y}\u0003,\u0016"+
		"\u0000z}\u0003\u0002\u0001\u0000{}\u0003.\u0017\u0000|o\u0001\u0000\u0000"+
		"\u0000|p\u0001\u0000\u0000\u0000|q\u0001\u0000\u0000\u0000|r\u0001\u0000"+
		"\u0000\u0000|s\u0001\u0000\u0000\u0000|t\u0001\u0000\u0000\u0000|u\u0001"+
		"\u0000\u0000\u0000|v\u0001\u0000\u0000\u0000|w\u0001\u0000\u0000\u0000"+
		"|x\u0001\u0000\u0000\u0000|y\u0001\u0000\u0000\u0000|z\u0001\u0000\u0000"+
		"\u0000|{\u0001\u0000\u0000\u0000}\u0007\u0001\u0000\u0000\u0000~\u0082"+
		"\u00034\u001a\u0000\u007f\u0081\u00054\u0000\u0000\u0080\u007f\u0001\u0000"+
		"\u0000\u0000\u0081\u0084\u0001\u0000\u0000\u0000\u0082\u0080\u0001\u0000"+
		"\u0000\u0000\u0082\u0083\u0001\u0000\u0000\u0000\u0083\u0088\u0001\u0000"+
		"\u0000\u0000\u0084\u0082\u0001\u0000\u0000\u0000\u0085\u0089\u0003B!\u0000"+
		"\u0086\u0089\u0001\u0000\u0000\u0000\u0087\u0089\u0003 \u0010\u0000\u0088"+
		"\u0085\u0001\u0000\u0000\u0000\u0088\u0086\u0001\u0000\u0000\u0000\u0088"+
		"\u0087\u0001\u0000\u0000\u0000\u0089\u0094\u0001\u0000\u0000\u0000\u008a"+
		"\u0092\u0005\u0005\u0000\u0000\u008b\u0093\u0003\u0006\u0003\u0000\u008c"+
		"\u008d\u0003&\u0013\u0000\u008d\u008e\u0005\u0006\u0000\u0000\u008e\u0093"+
		"\u0001\u0000\u0000\u0000\u008f\u0090\u0003$\u0012\u0000\u0090\u0091\u0005"+
		"\u0006\u0000\u0000\u0091\u0093\u0001\u0000\u0000\u0000\u0092\u008b\u0001"+
		"\u0000\u0000\u0000\u0092\u008c\u0001\u0000\u0000\u0000\u0092\u008f\u0001"+
		"\u0000\u0000\u0000\u0093\u0095\u0001\u0000\u0000\u0000\u0094\u008a\u0001"+
		"\u0000\u0000\u0000\u0094\u0095\u0001\u0000\u0000\u0000\u0095\t\u0001\u0000"+
		"\u0000\u0000\u0096\u0097\u0005\u0007\u0000\u0000\u0097\u009f\u0005\u0001"+
		"\u0000\u0000\u0098\u009a\u0003\b\u0004\u0000\u0099\u0098\u0001\u0000\u0000"+
		"\u0000\u0099\u009a\u0001\u0000\u0000\u0000\u009a\u00a0\u0001\u0000\u0000"+
		"\u0000\u009b\u00a0\u0001\u0000\u0000\u0000\u009c\u009e\u0003<\u001e\u0000"+
		"\u009d\u009c\u0001\u0000\u0000\u0000\u009d\u009e\u0001\u0000\u0000\u0000"+
		"\u009e\u00a0\u0001\u0000\u0000\u0000\u009f\u0099\u0001\u0000\u0000\u0000"+
		"\u009f\u009b\u0001\u0000\u0000\u0000\u009f\u009d\u0001\u0000\u0000\u0000"+
		"\u00a0\u00a1\u0001\u0000\u0000\u0000\u00a1\u00a3\u0005\u0006\u0000\u0000"+
		"\u00a2\u00a4\u0003H$\u0000\u00a3\u00a2\u0001\u0000\u0000\u0000\u00a3\u00a4"+
		"\u0001\u0000\u0000\u0000\u00a4\u00a5\u0001\u0000\u0000\u0000\u00a5\u00a7"+
		"\u0005\u0006\u0000\u0000\u00a6\u00a8\u0003>\u001f\u0000\u00a7\u00a6\u0001"+
		"\u0000\u0000\u0000\u00a7\u00a8\u0001\u0000\u0000\u0000\u00a8\u00a9\u0001"+
		"\u0000\u0000\u0000\u00a9\u00aa\u0005\u0002\u0000\u0000\u00aa\u00ab\u0003"+
		"\u0004\u0002\u0000\u00ab\u000b\u0001\u0000\u0000\u0000\u00ac\u00ad\u0005"+
		"\u0007\u0000\u0000\u00ad\u00b5\u0005\u0001\u0000\u0000\u00ae\u00b0\u0003"+
		"\b\u0004\u0000\u00af\u00ae\u0001\u0000\u0000\u0000\u00af\u00b0\u0001\u0000"+
		"\u0000\u0000\u00b0\u00b6\u0001\u0000\u0000\u0000\u00b1\u00b6\u0001\u0000"+
		"\u0000\u0000\u00b2\u00b4\u0003<\u001e\u0000\u00b3\u00b2\u0001\u0000\u0000"+
		"\u0000\u00b3\u00b4\u0001\u0000\u0000\u0000\u00b4\u00b6\u0001\u0000\u0000"+
		"\u0000\u00b5\u00af\u0001\u0000\u0000\u0000\u00b5\u00b1\u0001\u0000\u0000"+
		"\u0000\u00b5\u00b3\u0001\u0000\u0000\u0000\u00b6\u00b7\u0001\u0000\u0000"+
		"\u0000\u00b7\u00b9\u0005\u0006\u0000\u0000\u00b8\u00ba\u0003H$\u0000\u00b9"+
		"\u00b8\u0001\u0000\u0000\u0000\u00b9\u00ba\u0001\u0000\u0000\u0000\u00ba"+
		"\u00bb\u0001\u0000\u0000\u0000\u00bb\u00bd\u0005\u0006\u0000\u0000\u00bc"+
		"\u00be\u0003>\u001f\u0000\u00bd\u00bc\u0001\u0000\u0000\u0000\u00bd\u00be"+
		"\u0001\u0000\u0000\u0000\u00be\u00bf\u0001\u0000\u0000\u0000\u00bf\u00c0"+
		"\u0005\u0002\u0000\u0000\u00c0\u00c1\u0003\u0006\u0003\u0000\u00c1\r\u0001"+
		"\u0000\u0000\u0000\u00c2\u00c3\u0003H$\u0000\u00c3\u000f\u0001\u0000\u0000"+
		"\u0000\u00c4\u00c5\u0005\b\u0000\u0000\u00c5\u00c6\u0005\u0001\u0000\u0000"+
		"\u00c6\u00c7\u0003\u000e\u0007\u0000\u00c7\u00c8\u0005\u0002\u0000\u0000"+
		"\u00c8\u00c9\u0003\u0004\u0002\u0000\u00c9\u0011\u0001\u0000\u0000\u0000"+
		"\u00ca\u00cb\u0005\b\u0000\u0000\u00cb\u00cc\u0005\u0001\u0000\u0000\u00cc"+
		"\u00cd\u0003\u000e\u0007\u0000\u00cd\u00ce\u0005\u0002\u0000\u0000\u00ce"+
		"\u00cf\u0003\u0006\u0003\u0000\u00cf\u0013\u0001\u0000\u0000\u0000\u00d0"+
		"\u00d1\u0005\t\u0000\u0000\u00d1\u00d2\u0005\u0001\u0000\u0000\u00d2\u00d3"+
		"\u0003\u000e\u0007\u0000\u00d3\u00d4\u0005\u0002\u0000\u0000\u00d4\u00d6"+
		"\u0003\u0004\u0002\u0000\u00d5\u00d7\u0003\u0018\f\u0000\u00d6\u00d5\u0001"+
		"\u0000\u0000\u0000\u00d6\u00d7\u0001\u0000\u0000\u0000\u00d7\u0015\u0001"+
		"\u0000\u0000\u0000\u00d8\u00d9\u0005\t\u0000\u0000\u00d9\u00da\u0005\u0001"+
		"\u0000\u0000\u00da\u00db\u0003\u000e\u0007\u0000\u00db\u00dc\u0005\u0002"+
		"\u0000\u0000\u00dc\u00de\u0003\u0006\u0003\u0000\u00dd\u00df\u0003\u0018"+
		"\f\u0000\u00de\u00dd\u0001\u0000\u0000\u0000\u00de\u00df\u0001\u0000\u0000"+
		"\u0000\u00df\u0017\u0001\u0000\u0000\u0000\u00e0\u00e4\u0005\n\u0000\u0000"+
		"\u00e1\u00e5\u0003\u0004\u0002\u0000\u00e2\u00e5\u0003\u0014\n\u0000\u00e3"+
		"\u00e5\u0003\u0006\u0003\u0000\u00e4\u00e1\u0001\u0000\u0000\u0000\u00e4"+
		"\u00e2\u0001\u0000\u0000\u0000\u00e4\u00e3\u0001\u0000\u0000\u0000\u00e5"+
		"\u0019\u0001\u0000\u0000\u0000\u00e6\u00e7\u0005\u000b\u0000\u0000\u00e7"+
		"\u00e8\u0005\u0001\u0000\u0000\u00e8\u00e9\u0003\u000e\u0007\u0000\u00e9"+
		"\u00ea\u0005\u0002\u0000\u0000\u00ea\u00eb\u0003\u0004\u0002\u0000\u00eb"+
		"\u001b\u0001\u0000\u0000\u0000\u00ec\u00ef\u0005\f\u0000\u0000\u00ed\u00ef"+
		"\u00038\u001c\u0000\u00ee\u00ec\u0001\u0000\u0000\u0000\u00ee\u00ed\u0001"+
		"\u0000\u0000\u0000\u00ef\u00f1\u0001\u0000\u0000\u0000\u00f0\u00f2\u0003"+
		"B!\u0000\u00f1\u00f0\u0001\u0000\u0000\u0000\u00f1\u00f2\u0001\u0000\u0000"+
		"\u0000\u00f2\u00f3\u0001\u0000\u0000\u0000\u00f3\u00f7\u0005\r\u0000\u0000"+
		"\u00f4\u00f6\u0003\u0006\u0003\u0000\u00f5\u00f4\u0001\u0000\u0000\u0000"+
		"\u00f6\u00f9\u0001\u0000\u0000\u0000\u00f7\u00f5\u0001\u0000\u0000\u0000"+
		"\u00f7\u00f8\u0001\u0000\u0000\u0000\u00f8\u00fb\u0001\u0000\u0000\u0000"+
		"\u00f9\u00f7\u0001\u0000\u0000\u0000\u00fa\u00fc\u0003:\u001d\u0000\u00fb"+
		"\u00fa\u0001\u0000\u0000\u0000\u00fb\u00fc\u0001\u0000\u0000\u0000\u00fc"+
		"\u001d\u0001\u0000\u0000\u0000\u00fd\u00fe\u0005/\u0000\u0000\u00fe\u0100"+
		"\u0005\u0001\u0000\u0000\u00ff\u0101\u0003(\u0014\u0000\u0100\u00ff\u0001"+
		"\u0000\u0000\u0000\u0100\u0101\u0001\u0000\u0000\u0000\u0101\u0102\u0001"+
		"\u0000\u0000\u0000\u0102\u0103\u0005\u0002\u0000\u0000\u0103\u001f\u0001"+
		"\u0000\u0000\u0000\u0104\u0105\u0003B!\u0000\u0105\u0107\u0005\u000e\u0000"+
		"\u0000\u0106\u0108\u0003B!\u0000\u0107\u0106\u0001\u0000\u0000\u0000\u0107"+
		"\u0108\u0001\u0000\u0000\u0000\u0108\u0109\u0001\u0000\u0000\u0000\u0109"+
		"\u010a\u0005\u000f\u0000\u0000\u010a!\u0001\u0000\u0000\u0000\u010b\u010c"+
		"\u0005\u0003\u0000\u0000\u010c\u0111\u0003B!\u0000\u010d\u010e\u0005\u0010"+
		"\u0000\u0000\u010e\u0110\u0003B!\u0000\u010f\u010d\u0001\u0000\u0000\u0000"+
		"\u0110\u0113\u0001\u0000\u0000\u0000\u0111\u010f\u0001\u0000\u0000\u0000"+
		"\u0111\u0112\u0001\u0000\u0000\u0000\u0112\u0114\u0001\u0000\u0000\u0000"+
		"\u0113\u0111\u0001\u0000\u0000\u0000\u0114\u0115\u0005\u0004\u0000\u0000"+
		"\u0115#\u0001\u0000\u0000\u0000\u0116\u0117\u0005\u0003\u0000\u0000\u0117"+
		"\u0118\u0005\u0004\u0000\u0000\u0118%\u0001\u0000\u0000\u0000\u0119\u011a"+
		"\u0005\u0011\u0000\u0000\u011a\'\u0001\u0000\u0000\u0000\u011b\u0120\u0003"+
		"6\u001b\u0000\u011c\u011d\u0005\u0010\u0000\u0000\u011d\u011f\u00036\u001b"+
		"\u0000\u011e\u011c\u0001\u0000\u0000\u0000\u011f\u0122\u0001\u0000\u0000"+
		"\u0000\u0120\u011e\u0001\u0000\u0000\u0000\u0120\u0121\u0001\u0000\u0000"+
		"\u0000\u0121)\u0001\u0000\u0000\u0000\u0122\u0120\u0001\u0000\u0000\u0000"+
		"\u0123\u0125\u0005\u0012\u0000\u0000\u0124\u0126\u00036\u001b\u0000\u0125"+
		"\u0124\u0001\u0000\u0000\u0000\u0125\u0126\u0001\u0000\u0000\u0000\u0126"+
		"\u0127\u0001\u0000\u0000\u0000\u0127\u0128\u0005\u0006\u0000\u0000\u0128"+
		"+\u0001\u0000\u0000\u0000\u0129\u012a\u00036\u001b\u0000\u012a\u012b\u0005"+
		"\u0006\u0000\u0000\u012b-\u0001\u0000\u0000\u0000\u012c\u012d\u0005\u0013"+
		"\u0000\u0000\u012d\u012e\u00055\u0000\u0000\u012e/\u0001\u0000\u0000\u0000"+
		"\u012f\u0134\u00032\u0019\u0000\u0130\u0131\u0005\u0010\u0000\u0000\u0131"+
		"\u0133\u00032\u0019\u0000\u0132\u0130\u0001\u0000\u0000\u0000\u0133\u0136"+
		"\u0001\u0000\u0000\u0000\u0134\u0132\u0001\u0000\u0000\u0000\u0134\u0135"+
		"\u0001\u0000\u0000\u0000\u01351\u0001\u0000\u0000\u0000\u0136\u0134\u0001"+
		"\u0000\u0000\u0000\u0137\u0138\u00034\u001a\u0000\u0138\u0139\u0003B!"+
		"\u0000\u01393\u0001\u0000\u0000\u0000\u013a\u013b\u0007\u0000\u0000\u0000"+
		"\u013b5\u0001\u0000\u0000\u0000\u013c\u013d\u0003<\u001e\u0000\u013d7"+
		"\u0001\u0000\u0000\u0000\u013e\u013f\u0005\u0018\u0000\u0000\u013f9\u0001"+
		"\u0000\u0000\u0000\u0140\u0141\u0005\u0019\u0000\u0000\u0141\u0142\u0005"+
		"\u0006\u0000\u0000\u0142;\u0001\u0000\u0000\u0000\u0143\u0144\u0003>\u001f"+
		"\u0000\u0144\u0145\u0003F#\u0000\u0145\u0147\u0003<\u001e\u0000\u0146"+
		"\u0148\u0003&\u0013\u0000\u0147\u0146\u0001\u0000\u0000\u0000\u0147\u0148"+
		"\u0001\u0000\u0000\u0000\u0148\u014a\u0001\u0000\u0000\u0000\u0149\u014b"+
		"\u0003$\u0012\u0000\u014a\u0149\u0001\u0000\u0000\u0000\u014a\u014b\u0001"+
		"\u0000\u0000\u0000\u014b\u014e\u0001\u0000\u0000\u0000\u014c\u014e\u0003"+
		"H$\u0000\u014d\u0143\u0001\u0000\u0000\u0000\u014d\u014c\u0001\u0000\u0000"+
		"\u0000\u014e=\u0001\u0000\u0000\u0000\u014f\u0150\u0006\u001f\uffff\uffff"+
		"\u0000\u0150\u0151\u0007\u0001\u0000\u0000\u0151\u0156\u0003>\u001f\u0005"+
		"\u0152\u0156\u0003D\"\u0000\u0153\u0156\u0003B!\u0000\u0154\u0156\u0003"+
		"\"\u0011\u0000\u0155\u014f\u0001\u0000\u0000\u0000\u0155\u0152\u0001\u0000"+
		"\u0000\u0000\u0155\u0153\u0001\u0000\u0000\u0000\u0155\u0154\u0001\u0000"+
		"\u0000\u0000\u0156\u015b\u0001\u0000\u0000\u0000\u0157\u0158\n\u0004\u0000"+
		"\u0000\u0158\u015a\u0007\u0001\u0000\u0000\u0159\u0157\u0001\u0000\u0000"+
		"\u0000\u015a\u015d\u0001\u0000\u0000\u0000\u015b\u0159\u0001\u0000\u0000"+
		"\u0000\u015b\u015c\u0001\u0000\u0000\u0000\u015c?\u0001\u0000\u0000\u0000"+
		"\u015d\u015b\u0001\u0000\u0000\u0000\u015e\u015f\u0007\u0002\u0000\u0000"+
		"\u015fA\u0001\u0000\u0000\u0000\u0160\u016c\u0005/\u0000\u0000\u0161\u016c"+
		"\u00050\u0000\u0000\u0162\u016c\u00052\u0000\u0000\u0163\u016c\u00053"+
		"\u0000\u0000\u0164\u016c\u00055\u0000\u0000\u0165\u016c\u00051\u0000\u0000"+
		"\u0166\u016c\u0003\u001e\u000f\u0000\u0167\u0168\u0005\u0001\u0000\u0000"+
		"\u0168\u0169\u00036\u001b\u0000\u0169\u016a\u0005\u0002\u0000\u0000\u016a"+
		"\u016c\u0001\u0000\u0000\u0000\u016b\u0160\u0001\u0000\u0000\u0000\u016b"+
		"\u0161\u0001\u0000\u0000\u0000\u016b\u0162\u0001\u0000\u0000\u0000\u016b"+
		"\u0163\u0001\u0000\u0000\u0000\u016b\u0164\u0001\u0000\u0000\u0000\u016b"+
		"\u0165\u0001\u0000\u0000\u0000\u016b\u0166\u0001\u0000\u0000\u0000\u016b"+
		"\u0167\u0001\u0000\u0000\u0000\u016cC\u0001\u0000\u0000\u0000\u016d\u016e"+
		"\u0005 \u0000\u0000\u016e\u0172\u0003B!\u0000\u016f\u0170\u00054\u0000"+
		"\u0000\u0170\u0172\u0003B!\u0000\u0171\u016d\u0001\u0000\u0000\u0000\u0171"+
		"\u016f\u0001\u0000\u0000\u0000\u0172E\u0001\u0000\u0000\u0000\u0173\u0174"+
		"\u0007\u0003\u0000\u0000\u0174G\u0001\u0000\u0000\u0000\u0175\u017a\u0003"+
		"J%\u0000\u0176\u0177\u0005%\u0000\u0000\u0177\u0179\u0003J%\u0000\u0178"+
		"\u0176\u0001\u0000\u0000\u0000\u0179\u017c\u0001\u0000\u0000\u0000\u017a"+
		"\u0178\u0001\u0000\u0000\u0000\u017a\u017b\u0001\u0000\u0000\u0000\u017b"+
		"I\u0001\u0000\u0000\u0000\u017c\u017a\u0001\u0000\u0000\u0000\u017d\u0182"+
		"\u0003L&\u0000\u017e\u017f\u0005&\u0000\u0000\u017f\u0181\u0003L&\u0000"+
		"\u0180\u017e\u0001\u0000\u0000\u0000\u0181\u0184\u0001\u0000\u0000\u0000"+
		"\u0182\u0180\u0001\u0000\u0000\u0000\u0182\u0183\u0001\u0000\u0000\u0000"+
		"\u0183K\u0001\u0000\u0000\u0000\u0184\u0182\u0001\u0000\u0000\u0000\u0185"+
		"\u018a\u0003N\'\u0000\u0186\u0187\u0007\u0004\u0000\u0000\u0187\u0189"+
		"\u0003N\'\u0000\u0188\u0186\u0001\u0000\u0000\u0000\u0189\u018c\u0001"+
		"\u0000\u0000\u0000\u018a\u0188\u0001\u0000\u0000\u0000\u018a\u018b\u0001"+
		"\u0000\u0000\u0000\u018bM\u0001\u0000\u0000\u0000\u018c\u018a\u0001\u0000"+
		"\u0000\u0000\u018d\u0192\u0003P(\u0000\u018e\u018f\u0007\u0002\u0000\u0000"+
		"\u018f\u0191\u0003P(\u0000\u0190\u018e\u0001\u0000\u0000\u0000\u0191\u0194"+
		"\u0001\u0000\u0000\u0000\u0192\u0190\u0001\u0000\u0000\u0000\u0192\u0193"+
		"\u0001\u0000\u0000\u0000\u0193O\u0001\u0000\u0000\u0000\u0194\u0192\u0001"+
		"\u0000\u0000\u0000\u0195\u019a\u0003R)\u0000\u0196\u0197\u0007\u0005\u0000"+
		"\u0000\u0197\u0199\u0003R)\u0000\u0198\u0196\u0001\u0000\u0000\u0000\u0199"+
		"\u019c\u0001\u0000\u0000\u0000\u019a\u0198\u0001\u0000\u0000\u0000\u019a"+
		"\u019b\u0001\u0000\u0000\u0000\u019bQ\u0001\u0000\u0000\u0000\u019c\u019a"+
		"\u0001\u0000\u0000\u0000\u019d\u01a2\u0003>\u001f\u0000\u019e\u019f\u0007"+
		"\u0006\u0000\u0000\u019f\u01a1\u0003>\u001f\u0000\u01a0\u019e\u0001\u0000"+
		"\u0000\u0000\u01a1\u01a4\u0001\u0000\u0000\u0000\u01a2\u01a0\u0001\u0000"+
		"\u0000\u0000\u01a2\u01a3\u0001\u0000\u0000\u0000\u01a3S\u0001\u0000\u0000"+
		"\u0000\u01a4\u01a2\u0001\u0000\u0000\u0000\u01a5\u01a8\u0003P(\u0000\u01a6"+
		"\u01a8\u0003R)\u0000\u01a7\u01a5\u0001\u0000\u0000\u0000\u01a7\u01a6\u0001"+
		"\u0000\u0000\u0000\u01a8U\u0001\u0000\u0000\u0000-Yaj|\u0082\u0088\u0092"+
		"\u0094\u0099\u009d\u009f\u00a3\u00a7\u00af\u00b3\u00b5\u00b9\u00bd\u00d6"+
		"\u00de\u00e4\u00ee\u00f1\u00f7\u00fb\u0100\u0107\u0111\u0120\u0125\u0134"+
		"\u0147\u014a\u014d\u0155\u015b\u016b\u0171\u017a\u0182\u018a\u0192\u019a"+
		"\u01a2\u01a7";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}