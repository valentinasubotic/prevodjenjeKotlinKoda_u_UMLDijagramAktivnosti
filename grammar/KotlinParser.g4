parser grammar KotlinParser;

options { tokenVocab=KotlinLexer; }

// Početni simbol
program: statement* EOF;

// Svi tipovi naredbi 
statement
    : varDecl
    | valDecl
    | functionDecl
    | ifStatement
    | whenStatement
    | whileStatement
    | doWhileStatement
    | forStatement
    | tryStatement
    | returnStatement
    | exprStatement
    | block
    | breakStatement
    | continueStatement
    | throwStatement
    ;

// Definicija funkcije sa parametrima i opcionalnim tipom
functionDecl: FUN ID LPAREN parameterList? RPAREN (COLON type)? block;

parameterList: parameter (COMMA parameter)*;
parameter: ID COLON type;

// Tipovi podataka
type
    : INT_TYPE
    | STRING_TYPE
    | BOOLEAN_TYPE
    | FLOAT_TYPE
    | DOUBLE_TYPE
    | CHAR_TYPE
    | ARRAY_TYPE
    | INTARRAY_TYPE
    | CHARARRAY_TYPE
    | BOOLEANARRAY_TYPE
    | ID  // korisnički definisani tipovi
    ;

// If-else izraz
ifStatement: IF LPAREN expression RPAREN block (ELSE block)?;

// When izraz
whenStatement: WHEN LPAREN expression RPAREN LBRACE whenEntry* RBRACE;


whenEntry: expression ARROW statement+
         | ELSE ARROW statement+;


// While petlja
whileStatement: WHILE LPAREN expression RPAREN block;

// Do-while petlja
doWhileStatement: DO block WHILE LPAREN expression RPAREN;

// For petlja
forStatement: FOR LPAREN ID IN expression RPAREN block;

// Try-catch-finally blok
tryStatement: TRY block catchClause+ finallyClause?;
catchClause: CATCH LPAREN ID COLON type RPAREN block;
finallyClause: FINALLY block;

// Return naredba
returnStatement: RETURN expression? SEMI?;

valDecl: VAL ID (COLON type)? ASSIGN expression SEMI?;
varDecl: VAR ID (COLON type)? ASSIGN expression SEMI?;




// Obična naredba izraza
exprStatement: expression SEMI?;

// Blok koda
block: LBRACE statement* RBRACE;
breakStatement: BREAK SEMI?;
continueStatement: CONTINUE SEMI?;
throwStatement: THROW expression SEMI?;


// Izrazi
expression
    : literal
    | ID
    | ID ASSIGN expression                      // dodjela vrednosti
    | expression DOT ID                         // (e.message)
    | expression binaryOp expression            // binarni izrazi
    | unaryOp expression                        // prefiks unarni operator
    | expression unaryPostfixOp                 // postfiks unarni operator (++/--)
    | LPAREN expression RPAREN
    | expression LBRACK expression RBRACK       // pristup nizu
    | arrayCreation                             // arrayOf(...)
    | ID PLUSEQ expression  
    ;

// Kreiranje niza, npr. arrayOf(1, 2)
arrayCreation: ARRAYOF LPAREN (expression (COMMA expression)*)? RPAREN;

// Literali
literal
    : INT_LITERAL
    | FLOAT_LITERAL
    | STRING
    | CHAR
    | TRUE
    | FALSE
    | NULL
    ;

// Binarni operatori
binaryOp
    : PLUS | MINUS | MUL | DIV | MOD
    | EQ | NEQ | LT | GT | LEQ | GEQ
    | AND | OR
    ;

// Prefiks unarni operatori: -a...
unaryOp
    : PLUS | MINUS | NOT | INC | DEC
    ;

// Postfiks unarni operatori: a++..
unaryPostfixOp
    : INC | DEC
    ;

rangeExpression: expression RANGE expression;
