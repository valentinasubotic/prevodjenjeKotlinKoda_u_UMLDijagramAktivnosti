lexer grammar KotlinLexer;

// KLJUČNE RIJEČI
FUN     : 'fun';
IF      : 'if';
ELSE    : 'else';
FOR     : 'for';
WHILE   : 'while';
DO : 'do';
IN      : 'in';
RETURN  : 'return';
VAL     : 'val';
VAR     : 'var';
TRUE    : 'true';
FALSE   : 'false';
AS : 'as';
BREAK : 'break';
CLASS : 'class';
CONTINUE : 'continue';
IS : 'is';
OBJECT : 'object';
PACKAGE : 'package';
THIS : 'this';
THROW : 'throw';
TYPEALIAS : 'typealias';
TYPEOF : 'typeof';
ARRAYOF : 'arrayOf';
WHEN : 'when';
INTERFACE : 'interface';
TRY     : 'try';
CATCH   : 'catch';
FINALLY : 'finally';
NULL    : 'null';

ARROW       : '->';

// TIPOVI
INT_TYPE    : 'Int';
STRING_TYPE : 'String';
BOOLEAN_TYPE: 'Boolean';
FLOAT_TYPE  : 'Float';
DOUBLE_TYPE : 'Double';
CHAR_TYPE : 'Char';
ARRAY_TYPE : 'Array';
INTARRAY_TYPE     : 'IntArray';
CHARARRAY_TYPE    : 'CharArray';
BOOLEANARRAY_TYPE : 'BooleanArray';


// SIMBOLI
LPAREN      : '(';
RPAREN      : ')';
LBRACE      : '{';
RBRACE      : '}';
LBRACK      : '[';
RBRACK      : ']';
SEMI        : ';';
COLON       : ':';
COMMA       : ',';
RANGE       : '..';
DOT         : '.';



// OPERACIJE
PLUS        : '+';
MINUS       : '-';
MUL         : '*';
DIV         : '/';
MOD         : '%';
INC         : '++';
DEC         : '--';
PLUSEQ      : '+=';
MINUSEQ     : '-=';
MULEQ       : '*=';
DIVEQ       : '/=';
MODEQ       : '%=';



EQ          : '==';
NEQ         : '!=';
LT          : '<';
GT          : '>';
LEQ         : '<=';
GEQ         : '>=';


ASSIGN      : '=';

AND     : '&&';
OR      : '||';
NOT     : '!';




// IDENTIFIKATORI I LITERALNE VRIJEDNOSTI
ID      : [a-zA-Z_][a-zA-Z0-9_]*;
INT_LITERAL : [0-9]+;
FLOAT_LITERAL : [0-9]+ '.' [0-9]* [fF]? | '.' [0-9]+ [fF]? ;
STRING  : '"' ( ~["\\] | '\\' . )* '"';
CHAR : '\'' ( ~['\\] | '\\' . ) '\'' ;

// KOMENTARI I PRAZNINE
LINE_COMMENT : '//' ~[\r\n]* -> skip;
BLOCK_COMMENT: '/*' .*? '*/' -> skip;
WS           : [ \t\r\n]+ -> skip;
