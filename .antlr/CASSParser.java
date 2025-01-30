// Generated from c:/Users/Maria/Downloads/DIA-System-DS-Plagiarism-Checker-GIT/CASS.g4 by ANTLR 4.13.1
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
		T__38=39, SL_COMMENT=40, ML_COMMENT=41, ID=42, INT=43, BOOL=44, FLOAT=45, 
		CHAR=46, POINTER=47, STRING=48, WS=49;
	public static final int
		RULE_prog = 0, RULE_functionDefinition = 1, RULE_compoundStatement = 2, 
		RULE_statement = 3, RULE_declarationStatement = 4, RULE_forBlockStatement = 5, 
		RULE_forSingleStatement = 6, RULE_conditionClause = 7, RULE_whileBlockStatement = 8, 
		RULE_whileSingleStatement = 9, RULE_ifBlockStatement = 10, RULE_ifSingleStatement = 11, 
		RULE_elseClause = 12, RULE_functionCall = 13, RULE_arrayDeclarator = 14, 
		RULE_listInitializer = 15, RULE_emptyInitializer = 16, RULE_nullptr = 17, 
		RULE_argumentList = 18, RULE_returnStatement = 19, RULE_expressionStatement = 20, 
		RULE_includeStatement = 21, RULE_parameterList = 22, RULE_parameter = 23, 
		RULE_typeSpec = 24, RULE_expression = 25, RULE_assignmentExpression = 26, 
		RULE_unaryExpression = 27, RULE_comparingExpression = 28, RULE_primaryExpression = 29, 
		RULE_pointerExpression = 30, RULE_assignmentOperator = 31, RULE_logicalOrExpression = 32, 
		RULE_logicalAndExpression = 33, RULE_equalityExpression = 34, RULE_relationalExpression = 35, 
		RULE_additiveExpression = 36, RULE_multiplicativeExpression = 37, RULE_operationExpression = 38;
	private static String[] makeRuleNames() {
		return new String[] {
			"prog", "functionDefinition", "compoundStatement", "statement", "declarationStatement", 
			"forBlockStatement", "forSingleStatement", "conditionClause", "whileBlockStatement", 
			"whileSingleStatement", "ifBlockStatement", "ifSingleStatement", "elseClause", 
			"functionCall", "arrayDeclarator", "listInitializer", "emptyInitializer", 
			"nullptr", "argumentList", "returnStatement", "expressionStatement", 
			"includeStatement", "parameterList", "parameter", "typeSpec", "expression", 
			"assignmentExpression", "unaryExpression", "comparingExpression", "primaryExpression", 
			"pointerExpression", "assignmentOperator", "logicalOrExpression", "logicalAndExpression", 
			"equalityExpression", "relationalExpression", "additiveExpression", "multiplicativeExpression", 
			"operationExpression"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'('", "')'", "'{'", "'}'", "'='", "';'", "'for'", "'while'", "'if'", 
			"'else'", "'['", "']'", "','", "'nullptr'", "'return'", "'include'", 
			"'int'", "'float'", "'double'", "'void'", "'++'", "'--'", "'>'", "'<'", 
			"'<='", "'>='", "'&'", "'+='", "'-='", "'*='", "'/='", "'||'", "'&&'", 
			"'=='", "'!='", "'+'", "'-'", "'/'", "'%'", null, null, null, null, null, 
			null, null, "'*'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			null, null, null, null, "SL_COMMENT", "ML_COMMENT", "ID", "INT", "BOOL", 
			"FLOAT", "CHAR", "POINTER", "STRING", "WS"
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
			setState(79); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(78);
				statement();
				}
				}
				setState(81); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 558552049484682L) != 0) );
			setState(83);
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
			setState(85);
			typeSpec();
			setState(86);
			primaryExpression();
			setState(87);
			match(T__0);
			setState(89);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1966080L) != 0)) {
				{
				setState(88);
				parameterList();
				}
			}

			setState(91);
			match(T__1);
			setState(92);
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
			setState(94);
			match(T__2);
			setState(98);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 558552049484682L) != 0)) {
				{
				{
				setState(95);
				statement();
				}
				}
				setState(100);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(101);
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
			setState(114);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,3,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(103);
				declarationStatement();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(104);
				forBlockStatement();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(105);
				forSingleStatement();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(106);
				whileBlockStatement();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(107);
				whileSingleStatement();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(108);
				ifBlockStatement();
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(109);
				ifSingleStatement();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(110);
				returnStatement();
				}
				break;
			case 9:
				enterOuterAlt(_localctx, 9);
				{
				setState(111);
				expressionStatement();
				}
				break;
			case 10:
				enterOuterAlt(_localctx, 10);
				{
				setState(112);
				functionDefinition();
				}
				break;
			case 11:
				enterOuterAlt(_localctx, 11);
				{
				setState(113);
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
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
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
			setState(116);
			typeSpec();
			setState(120);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(117);
					match(POINTER);
					}
					} 
				}
				setState(122);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,4,_ctx);
			}
			setState(126);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				{
				setState(123);
				primaryExpression();
				}
				break;
			case 2:
				{
				}
				break;
			case 3:
				{
				setState(125);
				arrayDeclarator();
				}
				break;
			}
			setState(134);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==T__4) {
				{
				setState(128);
				match(T__4);
				setState(132);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
				case 1:
					{
					setState(129);
					expression();
					}
					break;
				case 2:
					{
					setState(130);
					nullptr();
					}
					break;
				case 3:
					{
					setState(131);
					emptyInitializer();
					}
					break;
				}
				}
			}

			setState(137);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,8,_ctx) ) {
			case 1:
				{
				setState(136);
				match(T__5);
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
			setState(139);
			match(T__6);
			setState(140);
			match(T__0);
			setState(148);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,11,_ctx) ) {
			case 1:
				{
				setState(142);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1966080L) != 0)) {
					{
					setState(141);
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
				setState(146);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 558552047419402L) != 0)) {
					{
					setState(145);
					assignmentExpression();
					}
				}

				}
				break;
			}
			setState(150);
			match(T__5);
			setState(152);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 558552047419402L) != 0)) {
				{
				setState(151);
				logicalOrExpression();
				}
			}

			setState(154);
			match(T__5);
			setState(156);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 558552047419402L) != 0)) {
				{
				setState(155);
				unaryExpression(0);
				}
			}

			setState(158);
			match(T__1);
			setState(159);
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
			setState(161);
			match(T__6);
			setState(162);
			match(T__0);
			setState(170);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,16,_ctx) ) {
			case 1:
				{
				setState(164);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 1966080L) != 0)) {
					{
					setState(163);
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
				setState(168);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 558552047419402L) != 0)) {
					{
					setState(167);
					assignmentExpression();
					}
				}

				}
				break;
			}
			setState(172);
			match(T__5);
			setState(174);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 558552047419402L) != 0)) {
				{
				setState(173);
				logicalOrExpression();
				}
			}

			setState(176);
			match(T__5);
			setState(178);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 558552047419402L) != 0)) {
				{
				setState(177);
				unaryExpression(0);
				}
			}

			setState(180);
			match(T__1);
			setState(181);
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
			setState(183);
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
			setState(185);
			match(T__7);
			setState(186);
			match(T__0);
			setState(187);
			conditionClause();
			setState(188);
			match(T__1);
			setState(189);
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
			setState(191);
			match(T__7);
			setState(192);
			match(T__0);
			setState(193);
			conditionClause();
			setState(194);
			match(T__1);
			setState(195);
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
			setState(197);
			match(T__8);
			setState(198);
			match(T__0);
			setState(199);
			conditionClause();
			setState(200);
			match(T__1);
			setState(201);
			compoundStatement();
			setState(203);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,19,_ctx) ) {
			case 1:
				{
				setState(202);
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
			setState(205);
			match(T__8);
			setState(206);
			match(T__0);
			setState(207);
			conditionClause();
			setState(208);
			match(T__1);
			setState(209);
			statement();
			setState(211);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,20,_ctx) ) {
			case 1:
				{
				setState(210);
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
			setState(213);
			match(T__9);
			setState(217);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,21,_ctx) ) {
			case 1:
				{
				setState(214);
				compoundStatement();
				}
				break;
			case 2:
				{
				setState(215);
				ifBlockStatement();
				}
				break;
			case 3:
				{
				setState(216);
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
		enterRule(_localctx, 26, RULE_functionCall);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(219);
			match(ID);
			setState(220);
			match(T__0);
			setState(222);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 558552047419402L) != 0)) {
				{
				setState(221);
				argumentList();
				}
			}

			setState(224);
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
		enterRule(_localctx, 28, RULE_arrayDeclarator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(226);
			primaryExpression();
			setState(227);
			match(T__10);
			setState(229);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 417814418554882L) != 0)) {
				{
				setState(228);
				primaryExpression();
				}
			}

			setState(231);
			match(T__11);
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
		enterRule(_localctx, 30, RULE_listInitializer);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(233);
			match(T__2);
			setState(234);
			primaryExpression();
			setState(239);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__12) {
				{
				{
				setState(235);
				match(T__12);
				setState(236);
				primaryExpression();
				}
				}
				setState(241);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(242);
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
		enterRule(_localctx, 32, RULE_emptyInitializer);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(244);
			match(T__2);
			setState(245);
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
		enterRule(_localctx, 34, RULE_nullptr);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(247);
			match(T__13);
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
		enterRule(_localctx, 36, RULE_argumentList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(249);
			expression();
			setState(254);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__12) {
				{
				{
				setState(250);
				match(T__12);
				setState(251);
				expression();
				}
				}
				setState(256);
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
		enterRule(_localctx, 38, RULE_returnStatement);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(257);
			match(T__14);
			setState(259);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & 558552047419402L) != 0)) {
				{
				setState(258);
				expression();
				}
			}

			setState(261);
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
		enterRule(_localctx, 40, RULE_expressionStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(263);
			expression();
			setState(264);
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
		enterRule(_localctx, 42, RULE_includeStatement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(266);
			match(T__15);
			setState(267);
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
		enterRule(_localctx, 44, RULE_parameterList);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(269);
			parameter();
			setState(274);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__12) {
				{
				{
				setState(270);
				match(T__12);
				setState(271);
				parameter();
				}
				}
				setState(276);
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
		enterRule(_localctx, 46, RULE_parameter);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(277);
			typeSpec();
			setState(278);
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
		enterRule(_localctx, 48, RULE_typeSpec);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(280);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 1966080L) != 0)) ) {
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
		enterRule(_localctx, 50, RULE_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(282);
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
		enterRule(_localctx, 52, RULE_assignmentExpression);
		try {
			setState(294);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,29,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(284);
				unaryExpression(0);
				setState(285);
				assignmentOperator();
				setState(291);
				_errHandler.sync(this);
				switch ( getInterpreter().adaptivePredict(_input,28,_ctx) ) {
				case 1:
					{
					setState(286);
					assignmentExpression();
					}
					break;
				case 2:
					{
					}
					break;
				case 3:
					{
					setState(288);
					nullptr();
					}
					break;
				case 4:
					{
					}
					break;
				case 5:
					{
					setState(290);
					emptyInitializer();
					}
					break;
				}
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(293);
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
		int _startState = 54;
		enterRecursionRule(_localctx, 54, RULE_unaryExpression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(302);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__20:
			case T__21:
				{
				setState(297);
				_la = _input.LA(1);
				if ( !(_la==T__20 || _la==T__21) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(298);
				unaryExpression(5);
				}
				break;
			case T__26:
			case POINTER:
				{
				setState(299);
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
				setState(300);
				primaryExpression();
				}
				break;
			case T__2:
				{
				setState(301);
				listInitializer();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			_ctx.stop = _input.LT(-1);
			setState(308);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,31,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					{
					_localctx = new UnaryExpressionContext(_parentctx, _parentState);
					pushNewRecursionContext(_localctx, _startState, RULE_unaryExpression);
					setState(304);
					if (!(precpred(_ctx, 4))) throw new FailedPredicateException(this, "precpred(_ctx, 4)");
					setState(305);
					_la = _input.LA(1);
					if ( !(_la==T__20 || _la==T__21) ) {
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
				setState(310);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,31,_ctx);
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
		enterRule(_localctx, 56, RULE_comparingExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(311);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 125829120L) != 0)) ) {
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
		enterRule(_localctx, 58, RULE_primaryExpression);
		try {
			setState(324);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,32,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(313);
				match(ID);
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(314);
				match(INT);
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(315);
				match(FLOAT);
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(316);
				match(CHAR);
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(317);
				match(STRING);
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(318);
				match(BOOL);
				}
				break;
			case 7:
				enterOuterAlt(_localctx, 7);
				{
				setState(319);
				functionCall();
				}
				break;
			case 8:
				enterOuterAlt(_localctx, 8);
				{
				setState(320);
				match(T__0);
				setState(321);
				expression();
				setState(322);
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
		enterRule(_localctx, 60, RULE_pointerExpression);
		try {
			setState(330);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case T__26:
				enterOuterAlt(_localctx, 1);
				{
				setState(326);
				match(T__26);
				setState(327);
				primaryExpression();
				}
				break;
			case POINTER:
				enterOuterAlt(_localctx, 2);
				{
				setState(328);
				match(POINTER);
				setState(329);
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
		enterRule(_localctx, 62, RULE_assignmentOperator);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(332);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 4026531872L) != 0)) ) {
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
		enterRule(_localctx, 64, RULE_logicalOrExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(334);
			logicalAndExpression();
			setState(339);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__31) {
				{
				{
				setState(335);
				match(T__31);
				setState(336);
				logicalAndExpression();
				}
				}
				setState(341);
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
		enterRule(_localctx, 66, RULE_logicalAndExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(342);
			equalityExpression();
			setState(347);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__32) {
				{
				{
				setState(343);
				match(T__32);
				setState(344);
				equalityExpression();
				}
				}
				setState(349);
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
		enterRule(_localctx, 68, RULE_equalityExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(350);
			relationalExpression();
			setState(355);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__33 || _la==T__34) {
				{
				{
				setState(351);
				_la = _input.LA(1);
				if ( !(_la==T__33 || _la==T__34) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(352);
				relationalExpression();
				}
				}
				setState(357);
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
		enterRule(_localctx, 70, RULE_relationalExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(358);
			additiveExpression();
			setState(363);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while ((((_la) & ~0x3f) == 0 && ((1L << _la) & 125829120L) != 0)) {
				{
				{
				setState(359);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 125829120L) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(360);
				additiveExpression();
				}
				}
				setState(365);
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
		enterRule(_localctx, 72, RULE_additiveExpression);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(366);
			multiplicativeExpression();
			setState(371);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==T__35 || _la==T__36) {
				{
				{
				setState(367);
				_la = _input.LA(1);
				if ( !(_la==T__35 || _la==T__36) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(368);
				multiplicativeExpression();
				}
				}
				setState(373);
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
		enterRule(_localctx, 74, RULE_multiplicativeExpression);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(374);
			unaryExpression(0);
			setState(379);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,39,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					{
					{
					setState(375);
					_la = _input.LA(1);
					if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & 141562122076160L) != 0)) ) {
					_errHandler.recoverInline(this);
					}
					else {
						if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
						_errHandler.reportMatch(this);
						consume();
					}
					setState(376);
					unaryExpression(0);
					}
					} 
				}
				setState(381);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,39,_ctx);
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
		enterRule(_localctx, 76, RULE_operationExpression);
		try {
			setState(384);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,40,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(382);
				additiveExpression();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(383);
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
		case 27:
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
		"\u0004\u00011\u0183\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
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
		"#\u0007#\u0002$\u0007$\u0002%\u0007%\u0002&\u0007&\u0001\u0000\u0004\u0000"+
		"P\b\u0000\u000b\u0000\f\u0000Q\u0001\u0000\u0001\u0000\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0003\u0001Z\b\u0001\u0001\u0001\u0001"+
		"\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0005\u0002a\b\u0002\n\u0002"+
		"\f\u0002d\t\u0002\u0001\u0002\u0001\u0002\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0003\u0003\u0003s\b\u0003\u0001\u0004\u0001"+
		"\u0004\u0005\u0004w\b\u0004\n\u0004\f\u0004z\t\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0003\u0004\u007f\b\u0004\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0003\u0004\u0085\b\u0004\u0003\u0004\u0087\b\u0004"+
		"\u0001\u0004\u0003\u0004\u008a\b\u0004\u0001\u0005\u0001\u0005\u0001\u0005"+
		"\u0003\u0005\u008f\b\u0005\u0001\u0005\u0001\u0005\u0003\u0005\u0093\b"+
		"\u0005\u0003\u0005\u0095\b\u0005\u0001\u0005\u0001\u0005\u0003\u0005\u0099"+
		"\b\u0005\u0001\u0005\u0001\u0005\u0003\u0005\u009d\b\u0005\u0001\u0005"+
		"\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006"+
		"\u00a5\b\u0006\u0001\u0006\u0001\u0006\u0003\u0006\u00a9\b\u0006\u0003"+
		"\u0006\u00ab\b\u0006\u0001\u0006\u0001\u0006\u0003\u0006\u00af\b\u0006"+
		"\u0001\u0006\u0001\u0006\u0003\u0006\u00b3\b\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001\n\u0001"+
		"\n\u0001\n\u0001\n\u0001\n\u0001\n\u0003\n\u00cc\b\n\u0001\u000b\u0001"+
		"\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0001\u000b\u0003\u000b\u00d4"+
		"\b\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0003\f\u00da\b\f\u0001\r\u0001"+
		"\r\u0001\r\u0003\r\u00df\b\r\u0001\r\u0001\r\u0001\u000e\u0001\u000e\u0001"+
		"\u000e\u0003\u000e\u00e6\b\u000e\u0001\u000e\u0001\u000e\u0001\u000f\u0001"+
		"\u000f\u0001\u000f\u0001\u000f\u0005\u000f\u00ee\b\u000f\n\u000f\f\u000f"+
		"\u00f1\t\u000f\u0001\u000f\u0001\u000f\u0001\u0010\u0001\u0010\u0001\u0010"+
		"\u0001\u0011\u0001\u0011\u0001\u0012\u0001\u0012\u0001\u0012\u0005\u0012"+
		"\u00fd\b\u0012\n\u0012\f\u0012\u0100\t\u0012\u0001\u0013\u0001\u0013\u0003"+
		"\u0013\u0104\b\u0013\u0001\u0013\u0001\u0013\u0001\u0014\u0001\u0014\u0001"+
		"\u0014\u0001\u0015\u0001\u0015\u0001\u0015\u0001\u0016\u0001\u0016\u0001"+
		"\u0016\u0005\u0016\u0111\b\u0016\n\u0016\f\u0016\u0114\t\u0016\u0001\u0017"+
		"\u0001\u0017\u0001\u0017\u0001\u0018\u0001\u0018\u0001\u0019\u0001\u0019"+
		"\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a\u0001\u001a"+
		"\u0001\u001a\u0003\u001a\u0124\b\u001a\u0001\u001a\u0003\u001a\u0127\b"+
		"\u001a\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001\u001b\u0001"+
		"\u001b\u0003\u001b\u012f\b\u001b\u0001\u001b\u0001\u001b\u0005\u001b\u0133"+
		"\b\u001b\n\u001b\f\u001b\u0136\t\u001b\u0001\u001c\u0001\u001c\u0001\u001d"+
		"\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d"+
		"\u0001\u001d\u0001\u001d\u0001\u001d\u0001\u001d\u0003\u001d\u0145\b\u001d"+
		"\u0001\u001e\u0001\u001e\u0001\u001e\u0001\u001e\u0003\u001e\u014b\b\u001e"+
		"\u0001\u001f\u0001\u001f\u0001 \u0001 \u0001 \u0005 \u0152\b \n \f \u0155"+
		"\t \u0001!\u0001!\u0001!\u0005!\u015a\b!\n!\f!\u015d\t!\u0001\"\u0001"+
		"\"\u0001\"\u0005\"\u0162\b\"\n\"\f\"\u0165\t\"\u0001#\u0001#\u0001#\u0005"+
		"#\u016a\b#\n#\f#\u016d\t#\u0001$\u0001$\u0001$\u0005$\u0172\b$\n$\f$\u0175"+
		"\t$\u0001%\u0001%\u0001%\u0005%\u017a\b%\n%\f%\u017d\t%\u0001&\u0001&"+
		"\u0003&\u0181\b&\u0001&\u0000\u00016\'\u0000\u0002\u0004\u0006\b\n\f\u000e"+
		"\u0010\u0012\u0014\u0016\u0018\u001a\u001c\u001e \"$&(*,.02468:<>@BDF"+
		"HJL\u0000\u0007\u0001\u0000\u0011\u0014\u0001\u0000\u0015\u0016\u0001"+
		"\u0000\u0017\u001a\u0002\u0000\u0005\u0005\u001c\u001f\u0001\u0000\"#"+
		"\u0001\u0000$%\u0002\u0000&\'//\u019d\u0000O\u0001\u0000\u0000\u0000\u0002"+
		"U\u0001\u0000\u0000\u0000\u0004^\u0001\u0000\u0000\u0000\u0006r\u0001"+
		"\u0000\u0000\u0000\bt\u0001\u0000\u0000\u0000\n\u008b\u0001\u0000\u0000"+
		"\u0000\f\u00a1\u0001\u0000\u0000\u0000\u000e\u00b7\u0001\u0000\u0000\u0000"+
		"\u0010\u00b9\u0001\u0000\u0000\u0000\u0012\u00bf\u0001\u0000\u0000\u0000"+
		"\u0014\u00c5\u0001\u0000\u0000\u0000\u0016\u00cd\u0001\u0000\u0000\u0000"+
		"\u0018\u00d5\u0001\u0000\u0000\u0000\u001a\u00db\u0001\u0000\u0000\u0000"+
		"\u001c\u00e2\u0001\u0000\u0000\u0000\u001e\u00e9\u0001\u0000\u0000\u0000"+
		" \u00f4\u0001\u0000\u0000\u0000\"\u00f7\u0001\u0000\u0000\u0000$\u00f9"+
		"\u0001\u0000\u0000\u0000&\u0101\u0001\u0000\u0000\u0000(\u0107\u0001\u0000"+
		"\u0000\u0000*\u010a\u0001\u0000\u0000\u0000,\u010d\u0001\u0000\u0000\u0000"+
		".\u0115\u0001\u0000\u0000\u00000\u0118\u0001\u0000\u0000\u00002\u011a"+
		"\u0001\u0000\u0000\u00004\u0126\u0001\u0000\u0000\u00006\u012e\u0001\u0000"+
		"\u0000\u00008\u0137\u0001\u0000\u0000\u0000:\u0144\u0001\u0000\u0000\u0000"+
		"<\u014a\u0001\u0000\u0000\u0000>\u014c\u0001\u0000\u0000\u0000@\u014e"+
		"\u0001\u0000\u0000\u0000B\u0156\u0001\u0000\u0000\u0000D\u015e\u0001\u0000"+
		"\u0000\u0000F\u0166\u0001\u0000\u0000\u0000H\u016e\u0001\u0000\u0000\u0000"+
		"J\u0176\u0001\u0000\u0000\u0000L\u0180\u0001\u0000\u0000\u0000NP\u0003"+
		"\u0006\u0003\u0000ON\u0001\u0000\u0000\u0000PQ\u0001\u0000\u0000\u0000"+
		"QO\u0001\u0000\u0000\u0000QR\u0001\u0000\u0000\u0000RS\u0001\u0000\u0000"+
		"\u0000ST\u0005\u0000\u0000\u0001T\u0001\u0001\u0000\u0000\u0000UV\u0003"+
		"0\u0018\u0000VW\u0003:\u001d\u0000WY\u0005\u0001\u0000\u0000XZ\u0003,"+
		"\u0016\u0000YX\u0001\u0000\u0000\u0000YZ\u0001\u0000\u0000\u0000Z[\u0001"+
		"\u0000\u0000\u0000[\\\u0005\u0002\u0000\u0000\\]\u0003\u0004\u0002\u0000"+
		"]\u0003\u0001\u0000\u0000\u0000^b\u0005\u0003\u0000\u0000_a\u0003\u0006"+
		"\u0003\u0000`_\u0001\u0000\u0000\u0000ad\u0001\u0000\u0000\u0000b`\u0001"+
		"\u0000\u0000\u0000bc\u0001\u0000\u0000\u0000ce\u0001\u0000\u0000\u0000"+
		"db\u0001\u0000\u0000\u0000ef\u0005\u0004\u0000\u0000f\u0005\u0001\u0000"+
		"\u0000\u0000gs\u0003\b\u0004\u0000hs\u0003\n\u0005\u0000is\u0003\f\u0006"+
		"\u0000js\u0003\u0010\b\u0000ks\u0003\u0012\t\u0000ls\u0003\u0014\n\u0000"+
		"ms\u0003\u0016\u000b\u0000ns\u0003&\u0013\u0000os\u0003(\u0014\u0000p"+
		"s\u0003\u0002\u0001\u0000qs\u0003*\u0015\u0000rg\u0001\u0000\u0000\u0000"+
		"rh\u0001\u0000\u0000\u0000ri\u0001\u0000\u0000\u0000rj\u0001\u0000\u0000"+
		"\u0000rk\u0001\u0000\u0000\u0000rl\u0001\u0000\u0000\u0000rm\u0001\u0000"+
		"\u0000\u0000rn\u0001\u0000\u0000\u0000ro\u0001\u0000\u0000\u0000rp\u0001"+
		"\u0000\u0000\u0000rq\u0001\u0000\u0000\u0000s\u0007\u0001\u0000\u0000"+
		"\u0000tx\u00030\u0018\u0000uw\u0005/\u0000\u0000vu\u0001\u0000\u0000\u0000"+
		"wz\u0001\u0000\u0000\u0000xv\u0001\u0000\u0000\u0000xy\u0001\u0000\u0000"+
		"\u0000y~\u0001\u0000\u0000\u0000zx\u0001\u0000\u0000\u0000{\u007f\u0003"+
		":\u001d\u0000|\u007f\u0001\u0000\u0000\u0000}\u007f\u0003\u001c\u000e"+
		"\u0000~{\u0001\u0000\u0000\u0000~|\u0001\u0000\u0000\u0000~}\u0001\u0000"+
		"\u0000\u0000\u007f\u0086\u0001\u0000\u0000\u0000\u0080\u0084\u0005\u0005"+
		"\u0000\u0000\u0081\u0085\u00032\u0019\u0000\u0082\u0085\u0003\"\u0011"+
		"\u0000\u0083\u0085\u0003 \u0010\u0000\u0084\u0081\u0001\u0000\u0000\u0000"+
		"\u0084\u0082\u0001\u0000\u0000\u0000\u0084\u0083\u0001\u0000\u0000\u0000"+
		"\u0085\u0087\u0001\u0000\u0000\u0000\u0086\u0080\u0001\u0000\u0000\u0000"+
		"\u0086\u0087\u0001\u0000\u0000\u0000\u0087\u0089\u0001\u0000\u0000\u0000"+
		"\u0088\u008a\u0005\u0006\u0000\u0000\u0089\u0088\u0001\u0000\u0000\u0000"+
		"\u0089\u008a\u0001\u0000\u0000\u0000\u008a\t\u0001\u0000\u0000\u0000\u008b"+
		"\u008c\u0005\u0007\u0000\u0000\u008c\u0094\u0005\u0001\u0000\u0000\u008d"+
		"\u008f\u0003\b\u0004\u0000\u008e\u008d\u0001\u0000\u0000\u0000\u008e\u008f"+
		"\u0001\u0000\u0000\u0000\u008f\u0095\u0001\u0000\u0000\u0000\u0090\u0095"+
		"\u0001\u0000\u0000\u0000\u0091\u0093\u00034\u001a\u0000\u0092\u0091\u0001"+
		"\u0000\u0000\u0000\u0092\u0093\u0001\u0000\u0000\u0000\u0093\u0095\u0001"+
		"\u0000\u0000\u0000\u0094\u008e\u0001\u0000\u0000\u0000\u0094\u0090\u0001"+
		"\u0000\u0000\u0000\u0094\u0092\u0001\u0000\u0000\u0000\u0095\u0096\u0001"+
		"\u0000\u0000\u0000\u0096\u0098\u0005\u0006\u0000\u0000\u0097\u0099\u0003"+
		"@ \u0000\u0098\u0097\u0001\u0000\u0000\u0000\u0098\u0099\u0001\u0000\u0000"+
		"\u0000\u0099\u009a\u0001\u0000\u0000\u0000\u009a\u009c\u0005\u0006\u0000"+
		"\u0000\u009b\u009d\u00036\u001b\u0000\u009c\u009b\u0001\u0000\u0000\u0000"+
		"\u009c\u009d\u0001\u0000\u0000\u0000\u009d\u009e\u0001\u0000\u0000\u0000"+
		"\u009e\u009f\u0005\u0002\u0000\u0000\u009f\u00a0\u0003\u0004\u0002\u0000"+
		"\u00a0\u000b\u0001\u0000\u0000\u0000\u00a1\u00a2\u0005\u0007\u0000\u0000"+
		"\u00a2\u00aa\u0005\u0001\u0000\u0000\u00a3\u00a5\u0003\b\u0004\u0000\u00a4"+
		"\u00a3\u0001\u0000\u0000\u0000\u00a4\u00a5\u0001\u0000\u0000\u0000\u00a5"+
		"\u00ab\u0001\u0000\u0000\u0000\u00a6\u00ab\u0001\u0000\u0000\u0000\u00a7"+
		"\u00a9\u00034\u001a\u0000\u00a8\u00a7\u0001\u0000\u0000\u0000\u00a8\u00a9"+
		"\u0001\u0000\u0000\u0000\u00a9\u00ab\u0001\u0000\u0000\u0000\u00aa\u00a4"+
		"\u0001\u0000\u0000\u0000\u00aa\u00a6\u0001\u0000\u0000\u0000\u00aa\u00a8"+
		"\u0001\u0000\u0000\u0000\u00ab\u00ac\u0001\u0000\u0000\u0000\u00ac\u00ae"+
		"\u0005\u0006\u0000\u0000\u00ad\u00af\u0003@ \u0000\u00ae\u00ad\u0001\u0000"+
		"\u0000\u0000\u00ae\u00af\u0001\u0000\u0000\u0000\u00af\u00b0\u0001\u0000"+
		"\u0000\u0000\u00b0\u00b2\u0005\u0006\u0000\u0000\u00b1\u00b3\u00036\u001b"+
		"\u0000\u00b2\u00b1\u0001\u0000\u0000\u0000\u00b2\u00b3\u0001\u0000\u0000"+
		"\u0000\u00b3\u00b4\u0001\u0000\u0000\u0000\u00b4\u00b5\u0005\u0002\u0000"+
		"\u0000\u00b5\u00b6\u0003\u0006\u0003\u0000\u00b6\r\u0001\u0000\u0000\u0000"+
		"\u00b7\u00b8\u0003@ \u0000\u00b8\u000f\u0001\u0000\u0000\u0000\u00b9\u00ba"+
		"\u0005\b\u0000\u0000\u00ba\u00bb\u0005\u0001\u0000\u0000\u00bb\u00bc\u0003"+
		"\u000e\u0007\u0000\u00bc\u00bd\u0005\u0002\u0000\u0000\u00bd\u00be\u0003"+
		"\u0004\u0002\u0000\u00be\u0011\u0001\u0000\u0000\u0000\u00bf\u00c0\u0005"+
		"\b\u0000\u0000\u00c0\u00c1\u0005\u0001\u0000\u0000\u00c1\u00c2\u0003\u000e"+
		"\u0007\u0000\u00c2\u00c3\u0005\u0002\u0000\u0000\u00c3\u00c4\u0003\u0006"+
		"\u0003\u0000\u00c4\u0013\u0001\u0000\u0000\u0000\u00c5\u00c6\u0005\t\u0000"+
		"\u0000\u00c6\u00c7\u0005\u0001\u0000\u0000\u00c7\u00c8\u0003\u000e\u0007"+
		"\u0000\u00c8\u00c9\u0005\u0002\u0000\u0000\u00c9\u00cb\u0003\u0004\u0002"+
		"\u0000\u00ca\u00cc\u0003\u0018\f\u0000\u00cb\u00ca\u0001\u0000\u0000\u0000"+
		"\u00cb\u00cc\u0001\u0000\u0000\u0000\u00cc\u0015\u0001\u0000\u0000\u0000"+
		"\u00cd\u00ce\u0005\t\u0000\u0000\u00ce\u00cf\u0005\u0001\u0000\u0000\u00cf"+
		"\u00d0\u0003\u000e\u0007\u0000\u00d0\u00d1\u0005\u0002\u0000\u0000\u00d1"+
		"\u00d3\u0003\u0006\u0003\u0000\u00d2\u00d4\u0003\u0018\f\u0000\u00d3\u00d2"+
		"\u0001\u0000\u0000\u0000\u00d3\u00d4\u0001\u0000\u0000\u0000\u00d4\u0017"+
		"\u0001\u0000\u0000\u0000\u00d5\u00d9\u0005\n\u0000\u0000\u00d6\u00da\u0003"+
		"\u0004\u0002\u0000\u00d7\u00da\u0003\u0014\n\u0000\u00d8\u00da\u0003\u0006"+
		"\u0003\u0000\u00d9\u00d6\u0001\u0000\u0000\u0000\u00d9\u00d7\u0001\u0000"+
		"\u0000\u0000\u00d9\u00d8\u0001\u0000\u0000\u0000\u00da\u0019\u0001\u0000"+
		"\u0000\u0000\u00db\u00dc\u0005*\u0000\u0000\u00dc\u00de\u0005\u0001\u0000"+
		"\u0000\u00dd\u00df\u0003$\u0012\u0000\u00de\u00dd\u0001\u0000\u0000\u0000"+
		"\u00de\u00df\u0001\u0000\u0000\u0000\u00df\u00e0\u0001\u0000\u0000\u0000"+
		"\u00e0\u00e1\u0005\u0002\u0000\u0000\u00e1\u001b\u0001\u0000\u0000\u0000"+
		"\u00e2\u00e3\u0003:\u001d\u0000\u00e3\u00e5\u0005\u000b\u0000\u0000\u00e4"+
		"\u00e6\u0003:\u001d\u0000\u00e5\u00e4\u0001\u0000\u0000\u0000\u00e5\u00e6"+
		"\u0001\u0000\u0000\u0000\u00e6\u00e7\u0001\u0000\u0000\u0000\u00e7\u00e8"+
		"\u0005\f\u0000\u0000\u00e8\u001d\u0001\u0000\u0000\u0000\u00e9\u00ea\u0005"+
		"\u0003\u0000\u0000\u00ea\u00ef\u0003:\u001d\u0000\u00eb\u00ec\u0005\r"+
		"\u0000\u0000\u00ec\u00ee\u0003:\u001d\u0000\u00ed\u00eb\u0001\u0000\u0000"+
		"\u0000\u00ee\u00f1\u0001\u0000\u0000\u0000\u00ef\u00ed\u0001\u0000\u0000"+
		"\u0000\u00ef\u00f0\u0001\u0000\u0000\u0000\u00f0\u00f2\u0001\u0000\u0000"+
		"\u0000\u00f1\u00ef\u0001\u0000\u0000\u0000\u00f2\u00f3\u0005\u0004\u0000"+
		"\u0000\u00f3\u001f\u0001\u0000\u0000\u0000\u00f4\u00f5\u0005\u0003\u0000"+
		"\u0000\u00f5\u00f6\u0005\u0004\u0000\u0000\u00f6!\u0001\u0000\u0000\u0000"+
		"\u00f7\u00f8\u0005\u000e\u0000\u0000\u00f8#\u0001\u0000\u0000\u0000\u00f9"+
		"\u00fe\u00032\u0019\u0000\u00fa\u00fb\u0005\r\u0000\u0000\u00fb\u00fd"+
		"\u00032\u0019\u0000\u00fc\u00fa\u0001\u0000\u0000\u0000\u00fd\u0100\u0001"+
		"\u0000\u0000\u0000\u00fe\u00fc\u0001\u0000\u0000\u0000\u00fe\u00ff\u0001"+
		"\u0000\u0000\u0000\u00ff%\u0001\u0000\u0000\u0000\u0100\u00fe\u0001\u0000"+
		"\u0000\u0000\u0101\u0103\u0005\u000f\u0000\u0000\u0102\u0104\u00032\u0019"+
		"\u0000\u0103\u0102\u0001\u0000\u0000\u0000\u0103\u0104\u0001\u0000\u0000"+
		"\u0000\u0104\u0105\u0001\u0000\u0000\u0000\u0105\u0106\u0005\u0006\u0000"+
		"\u0000\u0106\'\u0001\u0000\u0000\u0000\u0107\u0108\u00032\u0019\u0000"+
		"\u0108\u0109\u0005\u0006\u0000\u0000\u0109)\u0001\u0000\u0000\u0000\u010a"+
		"\u010b\u0005\u0010\u0000\u0000\u010b\u010c\u00050\u0000\u0000\u010c+\u0001"+
		"\u0000\u0000\u0000\u010d\u0112\u0003.\u0017\u0000\u010e\u010f\u0005\r"+
		"\u0000\u0000\u010f\u0111\u0003.\u0017\u0000\u0110\u010e\u0001\u0000\u0000"+
		"\u0000\u0111\u0114\u0001\u0000\u0000\u0000\u0112\u0110\u0001\u0000\u0000"+
		"\u0000\u0112\u0113\u0001\u0000\u0000\u0000\u0113-\u0001\u0000\u0000\u0000"+
		"\u0114\u0112\u0001\u0000\u0000\u0000\u0115\u0116\u00030\u0018\u0000\u0116"+
		"\u0117\u0003:\u001d\u0000\u0117/\u0001\u0000\u0000\u0000\u0118\u0119\u0007"+
		"\u0000\u0000\u0000\u01191\u0001\u0000\u0000\u0000\u011a\u011b\u00034\u001a"+
		"\u0000\u011b3\u0001\u0000\u0000\u0000\u011c\u011d\u00036\u001b\u0000\u011d"+
		"\u0123\u0003>\u001f\u0000\u011e\u0124\u00034\u001a\u0000\u011f\u0124\u0001"+
		"\u0000\u0000\u0000\u0120\u0124\u0003\"\u0011\u0000\u0121\u0124\u0001\u0000"+
		"\u0000\u0000\u0122\u0124\u0003 \u0010\u0000\u0123\u011e\u0001\u0000\u0000"+
		"\u0000\u0123\u011f\u0001\u0000\u0000\u0000\u0123\u0120\u0001\u0000\u0000"+
		"\u0000\u0123\u0121\u0001\u0000\u0000\u0000\u0123\u0122\u0001\u0000\u0000"+
		"\u0000\u0124\u0127\u0001\u0000\u0000\u0000\u0125\u0127\u0003@ \u0000\u0126"+
		"\u011c\u0001\u0000\u0000\u0000\u0126\u0125\u0001\u0000\u0000\u0000\u0127"+
		"5\u0001\u0000\u0000\u0000\u0128\u0129\u0006\u001b\uffff\uffff\u0000\u0129"+
		"\u012a\u0007\u0001\u0000\u0000\u012a\u012f\u00036\u001b\u0005\u012b\u012f"+
		"\u0003<\u001e\u0000\u012c\u012f\u0003:\u001d\u0000\u012d\u012f\u0003\u001e"+
		"\u000f\u0000\u012e\u0128\u0001\u0000\u0000\u0000\u012e\u012b\u0001\u0000"+
		"\u0000\u0000\u012e\u012c\u0001\u0000\u0000\u0000\u012e\u012d\u0001\u0000"+
		"\u0000\u0000\u012f\u0134\u0001\u0000\u0000\u0000\u0130\u0131\n\u0004\u0000"+
		"\u0000\u0131\u0133\u0007\u0001\u0000\u0000\u0132\u0130\u0001\u0000\u0000"+
		"\u0000\u0133\u0136\u0001\u0000\u0000\u0000\u0134\u0132\u0001\u0000\u0000"+
		"\u0000\u0134\u0135\u0001\u0000\u0000\u0000\u01357\u0001\u0000\u0000\u0000"+
		"\u0136\u0134\u0001\u0000\u0000\u0000\u0137\u0138\u0007\u0002\u0000\u0000"+
		"\u01389\u0001\u0000\u0000\u0000\u0139\u0145\u0005*\u0000\u0000\u013a\u0145"+
		"\u0005+\u0000\u0000\u013b\u0145\u0005-\u0000\u0000\u013c\u0145\u0005."+
		"\u0000\u0000\u013d\u0145\u00050\u0000\u0000\u013e\u0145\u0005,\u0000\u0000"+
		"\u013f\u0145\u0003\u001a\r\u0000\u0140\u0141\u0005\u0001\u0000\u0000\u0141"+
		"\u0142\u00032\u0019\u0000\u0142\u0143\u0005\u0002\u0000\u0000\u0143\u0145"+
		"\u0001\u0000\u0000\u0000\u0144\u0139\u0001\u0000\u0000\u0000\u0144\u013a"+
		"\u0001\u0000\u0000\u0000\u0144\u013b\u0001\u0000\u0000\u0000\u0144\u013c"+
		"\u0001\u0000\u0000\u0000\u0144\u013d\u0001\u0000\u0000\u0000\u0144\u013e"+
		"\u0001\u0000\u0000\u0000\u0144\u013f\u0001\u0000\u0000\u0000\u0144\u0140"+
		"\u0001\u0000\u0000\u0000\u0145;\u0001\u0000\u0000\u0000\u0146\u0147\u0005"+
		"\u001b\u0000\u0000\u0147\u014b\u0003:\u001d\u0000\u0148\u0149\u0005/\u0000"+
		"\u0000\u0149\u014b\u0003:\u001d\u0000\u014a\u0146\u0001\u0000\u0000\u0000"+
		"\u014a\u0148\u0001\u0000\u0000\u0000\u014b=\u0001\u0000\u0000\u0000\u014c"+
		"\u014d\u0007\u0003\u0000\u0000\u014d?\u0001\u0000\u0000\u0000\u014e\u0153"+
		"\u0003B!\u0000\u014f\u0150\u0005 \u0000\u0000\u0150\u0152\u0003B!\u0000"+
		"\u0151\u014f\u0001\u0000\u0000\u0000\u0152\u0155\u0001\u0000\u0000\u0000"+
		"\u0153\u0151\u0001\u0000\u0000\u0000\u0153\u0154\u0001\u0000\u0000\u0000"+
		"\u0154A\u0001\u0000\u0000\u0000\u0155\u0153\u0001\u0000\u0000\u0000\u0156"+
		"\u015b\u0003D\"\u0000\u0157\u0158\u0005!\u0000\u0000\u0158\u015a\u0003"+
		"D\"\u0000\u0159\u0157\u0001\u0000\u0000\u0000\u015a\u015d\u0001\u0000"+
		"\u0000\u0000\u015b\u0159\u0001\u0000\u0000\u0000\u015b\u015c\u0001\u0000"+
		"\u0000\u0000\u015cC\u0001\u0000\u0000\u0000\u015d\u015b\u0001\u0000\u0000"+
		"\u0000\u015e\u0163\u0003F#\u0000\u015f\u0160\u0007\u0004\u0000\u0000\u0160"+
		"\u0162\u0003F#\u0000\u0161\u015f\u0001\u0000\u0000\u0000\u0162\u0165\u0001"+
		"\u0000\u0000\u0000\u0163\u0161\u0001\u0000\u0000\u0000\u0163\u0164\u0001"+
		"\u0000\u0000\u0000\u0164E\u0001\u0000\u0000\u0000\u0165\u0163\u0001\u0000"+
		"\u0000\u0000\u0166\u016b\u0003H$\u0000\u0167\u0168\u0007\u0002\u0000\u0000"+
		"\u0168\u016a\u0003H$\u0000\u0169\u0167\u0001\u0000\u0000\u0000\u016a\u016d"+
		"\u0001\u0000\u0000\u0000\u016b\u0169\u0001\u0000\u0000\u0000\u016b\u016c"+
		"\u0001\u0000\u0000\u0000\u016cG\u0001\u0000\u0000\u0000\u016d\u016b\u0001"+
		"\u0000\u0000\u0000\u016e\u0173\u0003J%\u0000\u016f\u0170\u0007\u0005\u0000"+
		"\u0000\u0170\u0172\u0003J%\u0000\u0171\u016f\u0001\u0000\u0000\u0000\u0172"+
		"\u0175\u0001\u0000\u0000\u0000\u0173\u0171\u0001\u0000\u0000\u0000\u0173"+
		"\u0174\u0001\u0000\u0000\u0000\u0174I\u0001\u0000\u0000\u0000\u0175\u0173"+
		"\u0001\u0000\u0000\u0000\u0176\u017b\u00036\u001b\u0000\u0177\u0178\u0007"+
		"\u0006\u0000\u0000\u0178\u017a\u00036\u001b\u0000\u0179\u0177\u0001\u0000"+
		"\u0000\u0000\u017a\u017d\u0001\u0000\u0000\u0000\u017b\u0179\u0001\u0000"+
		"\u0000\u0000\u017b\u017c\u0001\u0000\u0000\u0000\u017cK\u0001\u0000\u0000"+
		"\u0000\u017d\u017b\u0001\u0000\u0000\u0000\u017e\u0181\u0003H$\u0000\u017f"+
		"\u0181\u0003J%\u0000\u0180\u017e\u0001\u0000\u0000\u0000\u0180\u017f\u0001"+
		"\u0000\u0000\u0000\u0181M\u0001\u0000\u0000\u0000)QYbrx~\u0084\u0086\u0089"+
		"\u008e\u0092\u0094\u0098\u009c\u00a4\u00a8\u00aa\u00ae\u00b2\u00cb\u00d3"+
		"\u00d9\u00de\u00e5\u00ef\u00fe\u0103\u0112\u0123\u0126\u012e\u0134\u0144"+
		"\u014a\u0153\u015b\u0163\u016b\u0173\u017b\u0180";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}