# Generated from grammar/KotlinParser.g4 by ANTLR 4.13.2
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
        4,1,82,312,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,1,0,5,0,62,8,0,10,0,12,0,65,9,0,1,
        0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,3,1,84,8,1,1,2,1,2,1,2,1,2,3,2,90,8,2,1,2,1,2,1,2,3,2,95,8,2,1,
        2,1,2,1,3,1,3,1,3,5,3,102,8,3,10,3,12,3,105,9,3,1,4,1,4,1,4,1,4,
        1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,120,8,6,1,7,1,7,1,7,1,7,
        1,7,1,7,5,7,128,8,7,10,7,12,7,131,9,7,1,7,1,7,1,8,1,8,1,8,4,8,138,
        8,8,11,8,12,8,139,1,8,1,8,1,8,4,8,145,8,8,11,8,12,8,146,3,8,149,
        8,8,1,9,1,9,1,9,1,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,4,12,175,8,
        12,11,12,12,12,176,1,12,3,12,180,8,12,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,14,1,14,1,14,1,15,1,15,3,15,195,8,15,1,15,3,15,198,
        8,15,1,16,1,16,1,16,1,16,3,16,204,8,16,1,16,1,16,1,16,3,16,209,8,
        16,1,17,1,17,1,17,1,17,3,17,215,8,17,1,17,1,17,1,17,3,17,220,8,17,
        1,18,1,18,3,18,224,8,18,1,19,1,19,5,19,228,8,19,10,19,12,19,231,
        9,19,1,19,1,19,1,20,1,20,3,20,237,8,20,1,21,1,21,3,21,241,8,21,1,
        22,1,22,1,22,3,22,246,8,22,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,
        23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,3,23,265,8,23,1,
        23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,23,1,
        23,5,23,281,8,23,10,23,12,23,284,9,23,1,24,1,24,1,24,1,24,1,24,5,
        24,291,8,24,10,24,12,24,294,9,24,3,24,296,8,24,1,24,1,24,1,25,1,
        25,1,26,1,26,1,27,1,27,1,28,1,28,1,29,1,29,1,29,1,29,1,29,0,1,46,
        30,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,
        44,46,48,50,52,54,56,58,0,5,2,0,32,41,75,75,3,0,11,12,30,30,76,79,
        3,0,53,57,65,70,72,73,3,0,53,54,58,59,74,74,1,0,58,59,329,0,63,1,
        0,0,0,2,83,1,0,0,0,4,85,1,0,0,0,6,98,1,0,0,0,8,106,1,0,0,0,10,110,
        1,0,0,0,12,112,1,0,0,0,14,121,1,0,0,0,16,148,1,0,0,0,18,150,1,0,
        0,0,20,156,1,0,0,0,22,163,1,0,0,0,24,171,1,0,0,0,26,181,1,0,0,0,
        28,189,1,0,0,0,30,192,1,0,0,0,32,199,1,0,0,0,34,210,1,0,0,0,36,221,
        1,0,0,0,38,225,1,0,0,0,40,234,1,0,0,0,42,238,1,0,0,0,44,242,1,0,
        0,0,46,264,1,0,0,0,48,285,1,0,0,0,50,299,1,0,0,0,52,301,1,0,0,0,
        54,303,1,0,0,0,56,305,1,0,0,0,58,307,1,0,0,0,60,62,3,2,1,0,61,60,
        1,0,0,0,62,65,1,0,0,0,63,61,1,0,0,0,63,64,1,0,0,0,64,66,1,0,0,0,
        65,63,1,0,0,0,66,67,5,0,0,1,67,1,1,0,0,0,68,84,3,34,17,0,69,84,3,
        32,16,0,70,84,3,4,2,0,71,84,3,12,6,0,72,84,3,14,7,0,73,84,3,18,9,
        0,74,84,3,20,10,0,75,84,3,22,11,0,76,84,3,24,12,0,77,84,3,30,15,
        0,78,84,3,36,18,0,79,84,3,38,19,0,80,84,3,40,20,0,81,84,3,42,21,
        0,82,84,3,44,22,0,83,68,1,0,0,0,83,69,1,0,0,0,83,70,1,0,0,0,83,71,
        1,0,0,0,83,72,1,0,0,0,83,73,1,0,0,0,83,74,1,0,0,0,83,75,1,0,0,0,
        83,76,1,0,0,0,83,77,1,0,0,0,83,78,1,0,0,0,83,79,1,0,0,0,83,80,1,
        0,0,0,83,81,1,0,0,0,83,82,1,0,0,0,84,3,1,0,0,0,85,86,5,1,0,0,86,
        87,5,75,0,0,87,89,5,42,0,0,88,90,3,6,3,0,89,88,1,0,0,0,89,90,1,0,
        0,0,90,91,1,0,0,0,91,94,5,43,0,0,92,93,5,49,0,0,93,95,3,10,5,0,94,
        92,1,0,0,0,94,95,1,0,0,0,95,96,1,0,0,0,96,97,3,38,19,0,97,5,1,0,
        0,0,98,103,3,8,4,0,99,100,5,50,0,0,100,102,3,8,4,0,101,99,1,0,0,
        0,102,105,1,0,0,0,103,101,1,0,0,0,103,104,1,0,0,0,104,7,1,0,0,0,
        105,103,1,0,0,0,106,107,5,75,0,0,107,108,5,49,0,0,108,109,3,10,5,
        0,109,9,1,0,0,0,110,111,7,0,0,0,111,11,1,0,0,0,112,113,5,2,0,0,113,
        114,5,42,0,0,114,115,3,46,23,0,115,116,5,43,0,0,116,119,3,38,19,
        0,117,118,5,3,0,0,118,120,3,38,19,0,119,117,1,0,0,0,119,120,1,0,
        0,0,120,13,1,0,0,0,121,122,5,25,0,0,122,123,5,42,0,0,123,124,3,46,
        23,0,124,125,5,43,0,0,125,129,5,44,0,0,126,128,3,16,8,0,127,126,
        1,0,0,0,128,131,1,0,0,0,129,127,1,0,0,0,129,130,1,0,0,0,130,132,
        1,0,0,0,131,129,1,0,0,0,132,133,5,45,0,0,133,15,1,0,0,0,134,135,
        3,46,23,0,135,137,5,31,0,0,136,138,3,2,1,0,137,136,1,0,0,0,138,139,
        1,0,0,0,139,137,1,0,0,0,139,140,1,0,0,0,140,149,1,0,0,0,141,142,
        5,3,0,0,142,144,5,31,0,0,143,145,3,2,1,0,144,143,1,0,0,0,145,146,
        1,0,0,0,146,144,1,0,0,0,146,147,1,0,0,0,147,149,1,0,0,0,148,134,
        1,0,0,0,148,141,1,0,0,0,149,17,1,0,0,0,150,151,5,5,0,0,151,152,5,
        42,0,0,152,153,3,46,23,0,153,154,5,43,0,0,154,155,3,38,19,0,155,
        19,1,0,0,0,156,157,5,6,0,0,157,158,3,38,19,0,158,159,5,5,0,0,159,
        160,5,42,0,0,160,161,3,46,23,0,161,162,5,43,0,0,162,21,1,0,0,0,163,
        164,5,4,0,0,164,165,5,42,0,0,165,166,5,75,0,0,166,167,5,7,0,0,167,
        168,3,46,23,0,168,169,5,43,0,0,169,170,3,38,19,0,170,23,1,0,0,0,
        171,172,5,27,0,0,172,174,3,38,19,0,173,175,3,26,13,0,174,173,1,0,
        0,0,175,176,1,0,0,0,176,174,1,0,0,0,176,177,1,0,0,0,177,179,1,0,
        0,0,178,180,3,28,14,0,179,178,1,0,0,0,179,180,1,0,0,0,180,25,1,0,
        0,0,181,182,5,28,0,0,182,183,5,42,0,0,183,184,5,75,0,0,184,185,5,
        49,0,0,185,186,3,10,5,0,186,187,5,43,0,0,187,188,3,38,19,0,188,27,
        1,0,0,0,189,190,5,29,0,0,190,191,3,38,19,0,191,29,1,0,0,0,192,194,
        5,8,0,0,193,195,3,46,23,0,194,193,1,0,0,0,194,195,1,0,0,0,195,197,
        1,0,0,0,196,198,5,48,0,0,197,196,1,0,0,0,197,198,1,0,0,0,198,31,
        1,0,0,0,199,200,5,9,0,0,200,203,5,75,0,0,201,202,5,49,0,0,202,204,
        3,10,5,0,203,201,1,0,0,0,203,204,1,0,0,0,204,205,1,0,0,0,205,206,
        5,71,0,0,206,208,3,46,23,0,207,209,5,48,0,0,208,207,1,0,0,0,208,
        209,1,0,0,0,209,33,1,0,0,0,210,211,5,10,0,0,211,214,5,75,0,0,212,
        213,5,49,0,0,213,215,3,10,5,0,214,212,1,0,0,0,214,215,1,0,0,0,215,
        216,1,0,0,0,216,217,5,71,0,0,217,219,3,46,23,0,218,220,5,48,0,0,
        219,218,1,0,0,0,219,220,1,0,0,0,220,35,1,0,0,0,221,223,3,46,23,0,
        222,224,5,48,0,0,223,222,1,0,0,0,223,224,1,0,0,0,224,37,1,0,0,0,
        225,229,5,44,0,0,226,228,3,2,1,0,227,226,1,0,0,0,228,231,1,0,0,0,
        229,227,1,0,0,0,229,230,1,0,0,0,230,232,1,0,0,0,231,229,1,0,0,0,
        232,233,5,45,0,0,233,39,1,0,0,0,234,236,5,14,0,0,235,237,5,48,0,
        0,236,235,1,0,0,0,236,237,1,0,0,0,237,41,1,0,0,0,238,240,5,16,0,
        0,239,241,5,48,0,0,240,239,1,0,0,0,240,241,1,0,0,0,241,43,1,0,0,
        0,242,243,5,21,0,0,243,245,3,46,23,0,244,246,5,48,0,0,245,244,1,
        0,0,0,245,246,1,0,0,0,246,45,1,0,0,0,247,248,6,23,-1,0,248,265,3,
        50,25,0,249,265,5,75,0,0,250,251,5,75,0,0,251,252,5,71,0,0,252,265,
        3,46,23,9,253,254,3,54,27,0,254,255,3,46,23,6,255,265,1,0,0,0,256,
        257,5,42,0,0,257,258,3,46,23,0,258,259,5,43,0,0,259,265,1,0,0,0,
        260,265,3,48,24,0,261,262,5,75,0,0,262,263,5,60,0,0,263,265,3,46,
        23,1,264,247,1,0,0,0,264,249,1,0,0,0,264,250,1,0,0,0,264,253,1,0,
        0,0,264,256,1,0,0,0,264,260,1,0,0,0,264,261,1,0,0,0,265,282,1,0,
        0,0,266,267,10,7,0,0,267,268,3,52,26,0,268,269,3,46,23,8,269,281,
        1,0,0,0,270,271,10,8,0,0,271,272,5,52,0,0,272,281,5,75,0,0,273,274,
        10,5,0,0,274,281,3,56,28,0,275,276,10,3,0,0,276,277,5,46,0,0,277,
        278,3,46,23,0,278,279,5,47,0,0,279,281,1,0,0,0,280,266,1,0,0,0,280,
        270,1,0,0,0,280,273,1,0,0,0,280,275,1,0,0,0,281,284,1,0,0,0,282,
        280,1,0,0,0,282,283,1,0,0,0,283,47,1,0,0,0,284,282,1,0,0,0,285,286,
        5,24,0,0,286,295,5,42,0,0,287,292,3,46,23,0,288,289,5,50,0,0,289,
        291,3,46,23,0,290,288,1,0,0,0,291,294,1,0,0,0,292,290,1,0,0,0,292,
        293,1,0,0,0,293,296,1,0,0,0,294,292,1,0,0,0,295,287,1,0,0,0,295,
        296,1,0,0,0,296,297,1,0,0,0,297,298,5,43,0,0,298,49,1,0,0,0,299,
        300,7,1,0,0,300,51,1,0,0,0,301,302,7,2,0,0,302,53,1,0,0,0,303,304,
        7,3,0,0,304,55,1,0,0,0,305,306,7,4,0,0,306,57,1,0,0,0,307,308,3,
        46,23,0,308,309,5,51,0,0,309,310,3,46,23,0,310,59,1,0,0,0,28,63,
        83,89,94,103,119,129,139,146,148,176,179,194,197,203,208,214,219,
        223,229,236,240,245,264,280,282,292,295
    ]

class KotlinParser ( Parser ):

    grammarFileName = "KotlinParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'fun'", "'if'", "'else'", "'for'", "'while'", 
                     "'do'", "'in'", "'return'", "'val'", "'var'", "'true'", 
                     "'false'", "'as'", "'break'", "'class'", "'continue'", 
                     "'is'", "'object'", "'package'", "'this'", "'throw'", 
                     "'typealias'", "'typeof'", "'arrayOf'", "'when'", "'interface'", 
                     "'try'", "'catch'", "'finally'", "'null'", "'->'", 
                     "'Int'", "'String'", "'Boolean'", "'Float'", "'Double'", 
                     "'Char'", "'Array'", "'IntArray'", "'CharArray'", "'BooleanArray'", 
                     "'('", "')'", "'{'", "'}'", "'['", "']'", "';'", "':'", 
                     "','", "'..'", "'.'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'++'", "'--'", "'+='", "'-='", "'*='", "'/='", "'%='", 
                     "'=='", "'!='", "'<'", "'>'", "'<='", "'>='", "'='", 
                     "'&&'", "'||'", "'!'" ]

    symbolicNames = [ "<INVALID>", "FUN", "IF", "ELSE", "FOR", "WHILE", 
                      "DO", "IN", "RETURN", "VAL", "VAR", "TRUE", "FALSE", 
                      "AS", "BREAK", "CLASS", "CONTINUE", "IS", "OBJECT", 
                      "PACKAGE", "THIS", "THROW", "TYPEALIAS", "TYPEOF", 
                      "ARRAYOF", "WHEN", "INTERFACE", "TRY", "CATCH", "FINALLY", 
                      "NULL", "ARROW", "INT_TYPE", "STRING_TYPE", "BOOLEAN_TYPE", 
                      "FLOAT_TYPE", "DOUBLE_TYPE", "CHAR_TYPE", "ARRAY_TYPE", 
                      "INTARRAY_TYPE", "CHARARRAY_TYPE", "BOOLEANARRAY_TYPE", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "LBRACK", 
                      "RBRACK", "SEMI", "COLON", "COMMA", "RANGE", "DOT", 
                      "PLUS", "MINUS", "MUL", "DIV", "MOD", "INC", "DEC", 
                      "PLUSEQ", "MINUSEQ", "MULEQ", "DIVEQ", "MODEQ", "EQ", 
                      "NEQ", "LT", "GT", "LEQ", "GEQ", "ASSIGN", "AND", 
                      "OR", "NOT", "ID", "INT_LITERAL", "FLOAT_LITERAL", 
                      "STRING", "CHAR", "LINE_COMMENT", "BLOCK_COMMENT", 
                      "WS" ]

    RULE_program = 0
    RULE_statement = 1
    RULE_functionDecl = 2
    RULE_parameterList = 3
    RULE_parameter = 4
    RULE_type = 5
    RULE_ifStatement = 6
    RULE_whenStatement = 7
    RULE_whenEntry = 8
    RULE_whileStatement = 9
    RULE_doWhileStatement = 10
    RULE_forStatement = 11
    RULE_tryStatement = 12
    RULE_catchClause = 13
    RULE_finallyClause = 14
    RULE_returnStatement = 15
    RULE_valDecl = 16
    RULE_varDecl = 17
    RULE_exprStatement = 18
    RULE_block = 19
    RULE_breakStatement = 20
    RULE_continueStatement = 21
    RULE_throwStatement = 22
    RULE_expression = 23
    RULE_arrayCreation = 24
    RULE_literal = 25
    RULE_binaryOp = 26
    RULE_unaryOp = 27
    RULE_unaryPostfixOp = 28
    RULE_rangeExpression = 29

    ruleNames =  [ "program", "statement", "functionDecl", "parameterList", 
                   "parameter", "type", "ifStatement", "whenStatement", 
                   "whenEntry", "whileStatement", "doWhileStatement", "forStatement", 
                   "tryStatement", "catchClause", "finallyClause", "returnStatement", 
                   "valDecl", "varDecl", "exprStatement", "block", "breakStatement", 
                   "continueStatement", "throwStatement", "expression", 
                   "arrayCreation", "literal", "binaryOp", "unaryOp", "unaryPostfixOp", 
                   "rangeExpression" ]

    EOF = Token.EOF
    FUN=1
    IF=2
    ELSE=3
    FOR=4
    WHILE=5
    DO=6
    IN=7
    RETURN=8
    VAL=9
    VAR=10
    TRUE=11
    FALSE=12
    AS=13
    BREAK=14
    CLASS=15
    CONTINUE=16
    IS=17
    OBJECT=18
    PACKAGE=19
    THIS=20
    THROW=21
    TYPEALIAS=22
    TYPEOF=23
    ARRAYOF=24
    WHEN=25
    INTERFACE=26
    TRY=27
    CATCH=28
    FINALLY=29
    NULL=30
    ARROW=31
    INT_TYPE=32
    STRING_TYPE=33
    BOOLEAN_TYPE=34
    FLOAT_TYPE=35
    DOUBLE_TYPE=36
    CHAR_TYPE=37
    ARRAY_TYPE=38
    INTARRAY_TYPE=39
    CHARARRAY_TYPE=40
    BOOLEANARRAY_TYPE=41
    LPAREN=42
    RPAREN=43
    LBRACE=44
    RBRACE=45
    LBRACK=46
    RBRACK=47
    SEMI=48
    COLON=49
    COMMA=50
    RANGE=51
    DOT=52
    PLUS=53
    MINUS=54
    MUL=55
    DIV=56
    MOD=57
    INC=58
    DEC=59
    PLUSEQ=60
    MINUSEQ=61
    MULEQ=62
    DIVEQ=63
    MODEQ=64
    EQ=65
    NEQ=66
    LT=67
    GT=68
    LEQ=69
    GEQ=70
    ASSIGN=71
    AND=72
    OR=73
    NOT=74
    ID=75
    INT_LITERAL=76
    FLOAT_LITERAL=77
    STRING=78
    CHAR=79
    LINE_COMMENT=80
    BLOCK_COMMENT=81
    WS=82

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(KotlinParser.EOF, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.StatementContext)
            else:
                return self.getTypedRuleContext(KotlinParser.StatementContext,i)


        def getRuleIndex(self):
            return KotlinParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = KotlinParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 891734717712392054) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & 63) != 0):
                self.state = 60
                self.statement()
                self.state = 65
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 66
            self.match(KotlinParser.EOF)
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

        def varDecl(self):
            return self.getTypedRuleContext(KotlinParser.VarDeclContext,0)


        def valDecl(self):
            return self.getTypedRuleContext(KotlinParser.ValDeclContext,0)


        def functionDecl(self):
            return self.getTypedRuleContext(KotlinParser.FunctionDeclContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(KotlinParser.IfStatementContext,0)


        def whenStatement(self):
            return self.getTypedRuleContext(KotlinParser.WhenStatementContext,0)


        def whileStatement(self):
            return self.getTypedRuleContext(KotlinParser.WhileStatementContext,0)


        def doWhileStatement(self):
            return self.getTypedRuleContext(KotlinParser.DoWhileStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(KotlinParser.ForStatementContext,0)


        def tryStatement(self):
            return self.getTypedRuleContext(KotlinParser.TryStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(KotlinParser.ReturnStatementContext,0)


        def exprStatement(self):
            return self.getTypedRuleContext(KotlinParser.ExprStatementContext,0)


        def block(self):
            return self.getTypedRuleContext(KotlinParser.BlockContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(KotlinParser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(KotlinParser.ContinueStatementContext,0)


        def throwStatement(self):
            return self.getTypedRuleContext(KotlinParser.ThrowStatementContext,0)


        def getRuleIndex(self):
            return KotlinParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)




    def statement(self):

        localctx = KotlinParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 83
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 68
                self.varDecl()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 69
                self.valDecl()
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 70
                self.functionDecl()
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 4)
                self.state = 71
                self.ifStatement()
                pass
            elif token in [25]:
                self.enterOuterAlt(localctx, 5)
                self.state = 72
                self.whenStatement()
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 6)
                self.state = 73
                self.whileStatement()
                pass
            elif token in [6]:
                self.enterOuterAlt(localctx, 7)
                self.state = 74
                self.doWhileStatement()
                pass
            elif token in [4]:
                self.enterOuterAlt(localctx, 8)
                self.state = 75
                self.forStatement()
                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 9)
                self.state = 76
                self.tryStatement()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 10)
                self.state = 77
                self.returnStatement()
                pass
            elif token in [11, 12, 24, 30, 42, 53, 54, 58, 59, 74, 75, 76, 77, 78, 79]:
                self.enterOuterAlt(localctx, 11)
                self.state = 78
                self.exprStatement()
                pass
            elif token in [44]:
                self.enterOuterAlt(localctx, 12)
                self.state = 79
                self.block()
                pass
            elif token in [14]:
                self.enterOuterAlt(localctx, 13)
                self.state = 80
                self.breakStatement()
                pass
            elif token in [16]:
                self.enterOuterAlt(localctx, 14)
                self.state = 81
                self.continueStatement()
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 15)
                self.state = 82
                self.throwStatement()
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


    class FunctionDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUN(self):
            return self.getToken(KotlinParser.FUN, 0)

        def ID(self):
            return self.getToken(KotlinParser.ID, 0)

        def LPAREN(self):
            return self.getToken(KotlinParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(KotlinParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(KotlinParser.BlockContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(KotlinParser.ParameterListContext,0)


        def COLON(self):
            return self.getToken(KotlinParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(KotlinParser.TypeContext,0)


        def getRuleIndex(self):
            return KotlinParser.RULE_functionDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDecl" ):
                listener.enterFunctionDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDecl" ):
                listener.exitFunctionDecl(self)




    def functionDecl(self):

        localctx = KotlinParser.FunctionDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_functionDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(KotlinParser.FUN)
            self.state = 86
            self.match(KotlinParser.ID)
            self.state = 87
            self.match(KotlinParser.LPAREN)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==75:
                self.state = 88
                self.parameterList()


            self.state = 91
            self.match(KotlinParser.RPAREN)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 92
                self.match(KotlinParser.COLON)
                self.state = 93
                self.type_()


            self.state = 96
            self.block()
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
                return self.getTypedRuleContexts(KotlinParser.ParameterContext)
            else:
                return self.getTypedRuleContext(KotlinParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(KotlinParser.COMMA)
            else:
                return self.getToken(KotlinParser.COMMA, i)

        def getRuleIndex(self):
            return KotlinParser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)




    def parameterList(self):

        localctx = KotlinParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.parameter()
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==50:
                self.state = 99
                self.match(KotlinParser.COMMA)
                self.state = 100
                self.parameter()
                self.state = 105
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

        def ID(self):
            return self.getToken(KotlinParser.ID, 0)

        def COLON(self):
            return self.getToken(KotlinParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(KotlinParser.TypeContext,0)


        def getRuleIndex(self):
            return KotlinParser.RULE_parameter

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameter" ):
                listener.enterParameter(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameter" ):
                listener.exitParameter(self)




    def parameter(self):

        localctx = KotlinParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.match(KotlinParser.ID)
            self.state = 107
            self.match(KotlinParser.COLON)
            self.state = 108
            self.type_()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_TYPE(self):
            return self.getToken(KotlinParser.INT_TYPE, 0)

        def STRING_TYPE(self):
            return self.getToken(KotlinParser.STRING_TYPE, 0)

        def BOOLEAN_TYPE(self):
            return self.getToken(KotlinParser.BOOLEAN_TYPE, 0)

        def FLOAT_TYPE(self):
            return self.getToken(KotlinParser.FLOAT_TYPE, 0)

        def DOUBLE_TYPE(self):
            return self.getToken(KotlinParser.DOUBLE_TYPE, 0)

        def CHAR_TYPE(self):
            return self.getToken(KotlinParser.CHAR_TYPE, 0)

        def ARRAY_TYPE(self):
            return self.getToken(KotlinParser.ARRAY_TYPE, 0)

        def INTARRAY_TYPE(self):
            return self.getToken(KotlinParser.INTARRAY_TYPE, 0)

        def CHARARRAY_TYPE(self):
            return self.getToken(KotlinParser.CHARARRAY_TYPE, 0)

        def BOOLEANARRAY_TYPE(self):
            return self.getToken(KotlinParser.BOOLEANARRAY_TYPE, 0)

        def ID(self):
            return self.getToken(KotlinParser.ID, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = KotlinParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            _la = self._input.LA(1)
            if not(((((_la - 32)) & ~0x3f) == 0 and ((1 << (_la - 32)) & 8796093023231) != 0)):
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


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(KotlinParser.IF, 0)

        def LPAREN(self):
            return self.getToken(KotlinParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(KotlinParser.RPAREN, 0)

        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.BlockContext)
            else:
                return self.getTypedRuleContext(KotlinParser.BlockContext,i)


        def ELSE(self):
            return self.getToken(KotlinParser.ELSE, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)




    def ifStatement(self):

        localctx = KotlinParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ifStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.match(KotlinParser.IF)
            self.state = 113
            self.match(KotlinParser.LPAREN)
            self.state = 114
            self.expression(0)
            self.state = 115
            self.match(KotlinParser.RPAREN)
            self.state = 116
            self.block()
            self.state = 119
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 117
                self.match(KotlinParser.ELSE)
                self.state = 118
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhenStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHEN(self):
            return self.getToken(KotlinParser.WHEN, 0)

        def LPAREN(self):
            return self.getToken(KotlinParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(KotlinParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(KotlinParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(KotlinParser.RBRACE, 0)

        def whenEntry(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.WhenEntryContext)
            else:
                return self.getTypedRuleContext(KotlinParser.WhenEntryContext,i)


        def getRuleIndex(self):
            return KotlinParser.RULE_whenStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhenStatement" ):
                listener.enterWhenStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhenStatement" ):
                listener.exitWhenStatement(self)




    def whenStatement(self):

        localctx = KotlinParser.WhenStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_whenStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            self.match(KotlinParser.WHEN)
            self.state = 122
            self.match(KotlinParser.LPAREN)
            self.state = 123
            self.expression(0)
            self.state = 124
            self.match(KotlinParser.RPAREN)
            self.state = 125
            self.match(KotlinParser.LBRACE)
            self.state = 129
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 891717125356394504) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & 63) != 0):
                self.state = 126
                self.whenEntry()
                self.state = 131
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 132
            self.match(KotlinParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhenEntryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


        def ARROW(self):
            return self.getToken(KotlinParser.ARROW, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.StatementContext)
            else:
                return self.getTypedRuleContext(KotlinParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(KotlinParser.ELSE, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_whenEntry

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhenEntry" ):
                listener.enterWhenEntry(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhenEntry" ):
                listener.exitWhenEntry(self)




    def whenEntry(self):

        localctx = KotlinParser.WhenEntryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_whenEntry)
        try:
            self.state = 148
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [11, 12, 24, 30, 42, 53, 54, 58, 59, 74, 75, 76, 77, 78, 79]:
                self.enterOuterAlt(localctx, 1)
                self.state = 134
                self.expression(0)
                self.state = 135
                self.match(KotlinParser.ARROW)
                self.state = 137 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 136
                        self.statement()

                    else:
                        raise NoViableAltException(self)
                    self.state = 139 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.match(KotlinParser.ELSE)
                self.state = 142
                self.match(KotlinParser.ARROW)
                self.state = 144 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 143
                        self.statement()

                    else:
                        raise NoViableAltException(self)
                    self.state = 146 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

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


    class WhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(KotlinParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(KotlinParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(KotlinParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(KotlinParser.BlockContext,0)


        def getRuleIndex(self):
            return KotlinParser.RULE_whileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStatement" ):
                listener.enterWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStatement" ):
                listener.exitWhileStatement(self)




    def whileStatement(self):

        localctx = KotlinParser.WhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_whileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 150
            self.match(KotlinParser.WHILE)
            self.state = 151
            self.match(KotlinParser.LPAREN)
            self.state = 152
            self.expression(0)
            self.state = 153
            self.match(KotlinParser.RPAREN)
            self.state = 154
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DoWhileStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DO(self):
            return self.getToken(KotlinParser.DO, 0)

        def block(self):
            return self.getTypedRuleContext(KotlinParser.BlockContext,0)


        def WHILE(self):
            return self.getToken(KotlinParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(KotlinParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(KotlinParser.RPAREN, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_doWhileStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDoWhileStatement" ):
                listener.enterDoWhileStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDoWhileStatement" ):
                listener.exitDoWhileStatement(self)




    def doWhileStatement(self):

        localctx = KotlinParser.DoWhileStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_doWhileStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 156
            self.match(KotlinParser.DO)
            self.state = 157
            self.block()
            self.state = 158
            self.match(KotlinParser.WHILE)
            self.state = 159
            self.match(KotlinParser.LPAREN)
            self.state = 160
            self.expression(0)
            self.state = 161
            self.match(KotlinParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(KotlinParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(KotlinParser.LPAREN, 0)

        def ID(self):
            return self.getToken(KotlinParser.ID, 0)

        def IN(self):
            return self.getToken(KotlinParser.IN, 0)

        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(KotlinParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(KotlinParser.BlockContext,0)


        def getRuleIndex(self):
            return KotlinParser.RULE_forStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStatement" ):
                listener.enterForStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStatement" ):
                listener.exitForStatement(self)




    def forStatement(self):

        localctx = KotlinParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_forStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(KotlinParser.FOR)
            self.state = 164
            self.match(KotlinParser.LPAREN)
            self.state = 165
            self.match(KotlinParser.ID)
            self.state = 166
            self.match(KotlinParser.IN)
            self.state = 167
            self.expression(0)
            self.state = 168
            self.match(KotlinParser.RPAREN)
            self.state = 169
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TryStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TRY(self):
            return self.getToken(KotlinParser.TRY, 0)

        def block(self):
            return self.getTypedRuleContext(KotlinParser.BlockContext,0)


        def catchClause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.CatchClauseContext)
            else:
                return self.getTypedRuleContext(KotlinParser.CatchClauseContext,i)


        def finallyClause(self):
            return self.getTypedRuleContext(KotlinParser.FinallyClauseContext,0)


        def getRuleIndex(self):
            return KotlinParser.RULE_tryStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTryStatement" ):
                listener.enterTryStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTryStatement" ):
                listener.exitTryStatement(self)




    def tryStatement(self):

        localctx = KotlinParser.TryStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_tryStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.match(KotlinParser.TRY)
            self.state = 172
            self.block()
            self.state = 174 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 173
                self.catchClause()
                self.state = 176 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==28):
                    break

            self.state = 179
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==29:
                self.state = 178
                self.finallyClause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CatchClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CATCH(self):
            return self.getToken(KotlinParser.CATCH, 0)

        def LPAREN(self):
            return self.getToken(KotlinParser.LPAREN, 0)

        def ID(self):
            return self.getToken(KotlinParser.ID, 0)

        def COLON(self):
            return self.getToken(KotlinParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(KotlinParser.TypeContext,0)


        def RPAREN(self):
            return self.getToken(KotlinParser.RPAREN, 0)

        def block(self):
            return self.getTypedRuleContext(KotlinParser.BlockContext,0)


        def getRuleIndex(self):
            return KotlinParser.RULE_catchClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCatchClause" ):
                listener.enterCatchClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCatchClause" ):
                listener.exitCatchClause(self)




    def catchClause(self):

        localctx = KotlinParser.CatchClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_catchClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.match(KotlinParser.CATCH)
            self.state = 182
            self.match(KotlinParser.LPAREN)
            self.state = 183
            self.match(KotlinParser.ID)
            self.state = 184
            self.match(KotlinParser.COLON)
            self.state = 185
            self.type_()
            self.state = 186
            self.match(KotlinParser.RPAREN)
            self.state = 187
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FinallyClauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FINALLY(self):
            return self.getToken(KotlinParser.FINALLY, 0)

        def block(self):
            return self.getTypedRuleContext(KotlinParser.BlockContext,0)


        def getRuleIndex(self):
            return KotlinParser.RULE_finallyClause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFinallyClause" ):
                listener.enterFinallyClause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFinallyClause" ):
                listener.exitFinallyClause(self)




    def finallyClause(self):

        localctx = KotlinParser.FinallyClauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_finallyClause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(KotlinParser.FINALLY)
            self.state = 190
            self.block()
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

        def RETURN(self):
            return self.getToken(KotlinParser.RETURN, 0)

        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(KotlinParser.SEMI, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)




    def returnStatement(self):

        localctx = KotlinParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 192
            self.match(KotlinParser.RETURN)
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 193
                self.expression(0)


            self.state = 197
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 196
                self.match(KotlinParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAL(self):
            return self.getToken(KotlinParser.VAL, 0)

        def ID(self):
            return self.getToken(KotlinParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(KotlinParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


        def COLON(self):
            return self.getToken(KotlinParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(KotlinParser.TypeContext,0)


        def SEMI(self):
            return self.getToken(KotlinParser.SEMI, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_valDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValDecl" ):
                listener.enterValDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValDecl" ):
                listener.exitValDecl(self)




    def valDecl(self):

        localctx = KotlinParser.ValDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_valDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            self.match(KotlinParser.VAL)
            self.state = 200
            self.match(KotlinParser.ID)
            self.state = 203
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 201
                self.match(KotlinParser.COLON)
                self.state = 202
                self.type_()


            self.state = 205
            self.match(KotlinParser.ASSIGN)
            self.state = 206
            self.expression(0)
            self.state = 208
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 207
                self.match(KotlinParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(KotlinParser.VAR, 0)

        def ID(self):
            return self.getToken(KotlinParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(KotlinParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


        def COLON(self):
            return self.getToken(KotlinParser.COLON, 0)

        def type_(self):
            return self.getTypedRuleContext(KotlinParser.TypeContext,0)


        def SEMI(self):
            return self.getToken(KotlinParser.SEMI, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_varDecl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarDecl" ):
                listener.enterVarDecl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarDecl" ):
                listener.exitVarDecl(self)




    def varDecl(self):

        localctx = KotlinParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_varDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(KotlinParser.VAR)
            self.state = 211
            self.match(KotlinParser.ID)
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==49:
                self.state = 212
                self.match(KotlinParser.COLON)
                self.state = 213
                self.type_()


            self.state = 216
            self.match(KotlinParser.ASSIGN)
            self.state = 217
            self.expression(0)
            self.state = 219
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 218
                self.match(KotlinParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(KotlinParser.SEMI, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_exprStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprStatement" ):
                listener.enterExprStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprStatement" ):
                listener.exitExprStatement(self)




    def exprStatement(self):

        localctx = KotlinParser.ExprStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_exprStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.expression(0)
            self.state = 223
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 222
                self.match(KotlinParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(KotlinParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(KotlinParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.StatementContext)
            else:
                return self.getTypedRuleContext(KotlinParser.StatementContext,i)


        def getRuleIndex(self):
            return KotlinParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = KotlinParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(KotlinParser.LBRACE)
            self.state = 229
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 891734717712392054) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & 63) != 0):
                self.state = 226
                self.statement()
                self.state = 231
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 232
            self.match(KotlinParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(KotlinParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(KotlinParser.SEMI, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_breakStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStatement" ):
                listener.enterBreakStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStatement" ):
                listener.exitBreakStatement(self)




    def breakStatement(self):

        localctx = KotlinParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_breakStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 234
            self.match(KotlinParser.BREAK)
            self.state = 236
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 235
                self.match(KotlinParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(KotlinParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(KotlinParser.SEMI, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_continueStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterContinueStatement" ):
                listener.enterContinueStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitContinueStatement" ):
                listener.exitContinueStatement(self)




    def continueStatement(self):

        localctx = KotlinParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_continueStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(KotlinParser.CONTINUE)
            self.state = 240
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 239
                self.match(KotlinParser.SEMI)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ThrowStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def THROW(self):
            return self.getToken(KotlinParser.THROW, 0)

        def expression(self):
            return self.getTypedRuleContext(KotlinParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(KotlinParser.SEMI, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_throwStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterThrowStatement" ):
                listener.enterThrowStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitThrowStatement" ):
                listener.exitThrowStatement(self)




    def throwStatement(self):

        localctx = KotlinParser.ThrowStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_throwStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(KotlinParser.THROW)
            self.state = 243
            self.expression(0)
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 244
                self.match(KotlinParser.SEMI)


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

        def literal(self):
            return self.getTypedRuleContext(KotlinParser.LiteralContext,0)


        def ID(self):
            return self.getToken(KotlinParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(KotlinParser.ASSIGN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(KotlinParser.ExpressionContext,i)


        def unaryOp(self):
            return self.getTypedRuleContext(KotlinParser.UnaryOpContext,0)


        def LPAREN(self):
            return self.getToken(KotlinParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(KotlinParser.RPAREN, 0)

        def arrayCreation(self):
            return self.getTypedRuleContext(KotlinParser.ArrayCreationContext,0)


        def PLUSEQ(self):
            return self.getToken(KotlinParser.PLUSEQ, 0)

        def binaryOp(self):
            return self.getTypedRuleContext(KotlinParser.BinaryOpContext,0)


        def DOT(self):
            return self.getToken(KotlinParser.DOT, 0)

        def unaryPostfixOp(self):
            return self.getTypedRuleContext(KotlinParser.UnaryPostfixOpContext,0)


        def LBRACK(self):
            return self.getToken(KotlinParser.LBRACK, 0)

        def RBRACK(self):
            return self.getToken(KotlinParser.RBRACK, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = KotlinParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 248
                self.literal()
                pass

            elif la_ == 2:
                self.state = 249
                self.match(KotlinParser.ID)
                pass

            elif la_ == 3:
                self.state = 250
                self.match(KotlinParser.ID)
                self.state = 251
                self.match(KotlinParser.ASSIGN)
                self.state = 252
                self.expression(9)
                pass

            elif la_ == 4:
                self.state = 253
                self.unaryOp()
                self.state = 254
                self.expression(6)
                pass

            elif la_ == 5:
                self.state = 256
                self.match(KotlinParser.LPAREN)
                self.state = 257
                self.expression(0)
                self.state = 258
                self.match(KotlinParser.RPAREN)
                pass

            elif la_ == 6:
                self.state = 260
                self.arrayCreation()
                pass

            elif la_ == 7:
                self.state = 261
                self.match(KotlinParser.ID)
                self.state = 262
                self.match(KotlinParser.PLUSEQ)
                self.state = 263
                self.expression(1)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 282
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 280
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        localctx = KotlinParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 266
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 267
                        self.binaryOp()
                        self.state = 268
                        self.expression(8)
                        pass

                    elif la_ == 2:
                        localctx = KotlinParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 270
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 271
                        self.match(KotlinParser.DOT)
                        self.state = 272
                        self.match(KotlinParser.ID)
                        pass

                    elif la_ == 3:
                        localctx = KotlinParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 273
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 274
                        self.unaryPostfixOp()
                        pass

                    elif la_ == 4:
                        localctx = KotlinParser.ExpressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 275
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 276
                        self.match(KotlinParser.LBRACK)
                        self.state = 277
                        self.expression(0)
                        self.state = 278
                        self.match(KotlinParser.RBRACK)
                        pass

             
                self.state = 284
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ArrayCreationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAYOF(self):
            return self.getToken(KotlinParser.ARRAYOF, 0)

        def LPAREN(self):
            return self.getToken(KotlinParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(KotlinParser.RPAREN, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(KotlinParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(KotlinParser.COMMA)
            else:
                return self.getToken(KotlinParser.COMMA, i)

        def getRuleIndex(self):
            return KotlinParser.RULE_arrayCreation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArrayCreation" ):
                listener.enterArrayCreation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArrayCreation" ):
                listener.exitArrayCreation(self)




    def arrayCreation(self):

        localctx = KotlinParser.ArrayCreationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_arrayCreation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 285
            self.match(KotlinParser.ARRAYOF)
            self.state = 286
            self.match(KotlinParser.LPAREN)
            self.state = 295
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 891717125356394496) != 0) or ((((_la - 74)) & ~0x3f) == 0 and ((1 << (_la - 74)) & 63) != 0):
                self.state = 287
                self.expression(0)
                self.state = 292
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==50:
                    self.state = 288
                    self.match(KotlinParser.COMMA)
                    self.state = 289
                    self.expression(0)
                    self.state = 294
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 297
            self.match(KotlinParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LITERAL(self):
            return self.getToken(KotlinParser.INT_LITERAL, 0)

        def FLOAT_LITERAL(self):
            return self.getToken(KotlinParser.FLOAT_LITERAL, 0)

        def STRING(self):
            return self.getToken(KotlinParser.STRING, 0)

        def CHAR(self):
            return self.getToken(KotlinParser.CHAR, 0)

        def TRUE(self):
            return self.getToken(KotlinParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(KotlinParser.FALSE, 0)

        def NULL(self):
            return self.getToken(KotlinParser.NULL, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_literal

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLiteral" ):
                listener.enterLiteral(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLiteral" ):
                listener.exitLiteral(self)




    def literal(self):

        localctx = KotlinParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 299
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1073747968) != 0) or ((((_la - 76)) & ~0x3f) == 0 and ((1 << (_la - 76)) & 15) != 0)):
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


    class BinaryOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(KotlinParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(KotlinParser.MINUS, 0)

        def MUL(self):
            return self.getToken(KotlinParser.MUL, 0)

        def DIV(self):
            return self.getToken(KotlinParser.DIV, 0)

        def MOD(self):
            return self.getToken(KotlinParser.MOD, 0)

        def EQ(self):
            return self.getToken(KotlinParser.EQ, 0)

        def NEQ(self):
            return self.getToken(KotlinParser.NEQ, 0)

        def LT(self):
            return self.getToken(KotlinParser.LT, 0)

        def GT(self):
            return self.getToken(KotlinParser.GT, 0)

        def LEQ(self):
            return self.getToken(KotlinParser.LEQ, 0)

        def GEQ(self):
            return self.getToken(KotlinParser.GEQ, 0)

        def AND(self):
            return self.getToken(KotlinParser.AND, 0)

        def OR(self):
            return self.getToken(KotlinParser.OR, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_binaryOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBinaryOp" ):
                listener.enterBinaryOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBinaryOp" ):
                listener.exitBinaryOp(self)




    def binaryOp(self):

        localctx = KotlinParser.BinaryOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_binaryOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            _la = self._input.LA(1)
            if not(((((_la - 53)) & ~0x3f) == 0 and ((1 << (_la - 53)) & 1830943) != 0)):
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


    class UnaryOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PLUS(self):
            return self.getToken(KotlinParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(KotlinParser.MINUS, 0)

        def NOT(self):
            return self.getToken(KotlinParser.NOT, 0)

        def INC(self):
            return self.getToken(KotlinParser.INC, 0)

        def DEC(self):
            return self.getToken(KotlinParser.DEC, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_unaryOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryOp" ):
                listener.enterUnaryOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryOp" ):
                listener.exitUnaryOp(self)




    def unaryOp(self):

        localctx = KotlinParser.UnaryOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_unaryOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            _la = self._input.LA(1)
            if not(((((_la - 53)) & ~0x3f) == 0 and ((1 << (_la - 53)) & 2097251) != 0)):
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


    class UnaryPostfixOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INC(self):
            return self.getToken(KotlinParser.INC, 0)

        def DEC(self):
            return self.getToken(KotlinParser.DEC, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_unaryPostfixOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryPostfixOp" ):
                listener.enterUnaryPostfixOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryPostfixOp" ):
                listener.exitUnaryPostfixOp(self)




    def unaryPostfixOp(self):

        localctx = KotlinParser.UnaryPostfixOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_unaryPostfixOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 305
            _la = self._input.LA(1)
            if not(_la==58 or _la==59):
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


    class RangeExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(KotlinParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(KotlinParser.ExpressionContext,i)


        def RANGE(self):
            return self.getToken(KotlinParser.RANGE, 0)

        def getRuleIndex(self):
            return KotlinParser.RULE_rangeExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRangeExpression" ):
                listener.enterRangeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRangeExpression" ):
                listener.exitRangeExpression(self)




    def rangeExpression(self):

        localctx = KotlinParser.RangeExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_rangeExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 307
            self.expression(0)
            self.state = 308
            self.match(KotlinParser.RANGE)
            self.state = 309
            self.expression(0)
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
        self._predicates[23] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 8)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 3)
         




