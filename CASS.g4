grammar CASS;

// --------------------------
// 1) Top-Level Structure
// --------------------------

// Parse one or more function definitions.
prog
    : functionDefinition+ EOF
    ;

functionDefinition
    : typeSpec ID '(' parameterList? ')' compoundStatement
    ;

// A block of statements in braces
compoundStatement
    : '{' statement* '}'
    ;

// --------------------------
// 2) Declarations & Statements
// --------------------------

statement
    // e.g.  int sum = 0;
    : declarationStatement
    // e.g.  for (int i = start_val; i <= end_val; ++i) sum += i;
    | forBlockStatement          // For loop with { }
    | forSingleStatement         // For loop without { }

    | whileBlockStatement       // While loop with { }
    | whileSingleStatement
    | ifBlockStatement           // If with { }
    | ifSingleStatement          // If without { }

    // e.g.  return sum;
    | returnStatement
    // e.g.  sum += i;
    | expressionStatement
    ;

// A simple variable declaration with initialization, e.g. "int sum = 0;"
declarationStatement
    : typeSpec ID ('=' expression)? ';'
    ;

// For loop in a slightly simplified form
forBlockStatement
    : 'for' '(' forInit? ';' expression? ';' forUpdate? ')' '{' statement* '}'
    ;

forSingleStatement
    : 'for' '(' forInit? ';' expression? ';' forUpdate? ')' statement 
    ;

// Optional initialization part of the for loop, e.g. "int i = start_val"
forInit
    : typeSpec ID '=' expression
    ;

// Optional update part, e.g. "++i" or "i++" or "i += 2"
forUpdate
    : unaryExpression
    ;

whileBlockStatement
    : 'while' '(' expression ')' '{' statement* '}'
    ;

whileSingleStatement
    : 'while' '(' expression ')' statement
    ;

ifBlockStatement
    : 'if' '(' expression ')' '{' statement* '}' ('else' '{' statement* '}')?
    ;

ifSingleStatement
    : 'if' '(' expression ')' statement ('else' statement)?
    ;


returnStatement
    : 'return' expression? ';'
    ;

expressionStatement
    : expression ';'
    ;

// --------------------------
// 3) Parameters & Types
// --------------------------

parameterList
    : parameter (',' parameter)*
    ;

parameter
    : typeSpec ID
    ;

// Very simple type spec to catch "int" (you can expand as needed)
typeSpec
    : 'int' 
    | 'float'
    | 'double'
    | 'char'
    ;

// --------------------------
// 4) Expressions
// --------------------------

// For simplicity, we let "expression" wrap typical C operator precedences.

expression
    : assignmentExpression
    ;

assignmentExpression
    // e.g. "sum += i" or "i = i + 1"
    : unaryExpression assignmentOperator assignmentExpression
    | logicalOrExpression
    ;

// e.g. ++i, --i, i++, i--
unaryExpression
    : '++' unaryExpression
    | '--' unaryExpression
    | primaryExpression
    ;

primaryExpression
    : ID
    | INT
    | FLOAT
    | '(' expression ')'
    ;

// Compound assignment ops
assignmentOperator
    : '='
    | '+='
    | '-='
    | '*='
    | '/='
    ;

// A minimal boolean-expr chain
logicalOrExpression
    : logicalAndExpression ('||' logicalAndExpression)*
    ;

logicalAndExpression
    : equalityExpression ('&&' equalityExpression)*
    ;

equalityExpression
    : relationalExpression (( '==' | '!=' ) relationalExpression)*
    ;

relationalExpression
    : additiveExpression (( '<' | '>' | '<=' | '>=' ) additiveExpression)*
    ;

additiveExpression
    : multiplicativeExpression (( '+' | '-' ) multiplicativeExpression)*
    ;

multiplicativeExpression
    : unaryExpression (( '*' | '/' ) unaryExpression)*
    ;

// --------------------------
// 5) Lexer Rules
// --------------------------

SL_COMMENT
    : '//' ~[\r\n]* -> skip
    ;

ML_COMMENT
    : '/*' .*? '*/' -> skip
    ;

ID
    : [a-zA-Z_] [a-zA-Z0-9_]*
    ;

INT
    : [0-9]+
    ;

FLOAT
    : [0-9]+ '.' [0-9]+ ([eE] [+-]? [0-9]+)?
    | '.' [0-9]+ ([eE] [+-]? [0-9]+)?
    | [0-9]+ ([eE] [+-]? [0-9]+)
    ;


// Skip whitespace and newlines
WS
    : [ \t\r\n]+ -> skip
    ;
