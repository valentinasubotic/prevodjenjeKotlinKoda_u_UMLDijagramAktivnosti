# Generated from grammar/KotlinParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .KotlinParser import KotlinParser
else:
    from KotlinParser import KotlinParser

# This class defines a complete listener for a parse tree produced by KotlinParser.
class KotlinParserListener(ParseTreeListener):

    # Enter a parse tree produced by KotlinParser#program.
    def enterProgram(self, ctx:KotlinParser.ProgramContext):
        pass

    # Exit a parse tree produced by KotlinParser#program.
    def exitProgram(self, ctx:KotlinParser.ProgramContext):
        pass


    # Enter a parse tree produced by KotlinParser#statement.
    def enterStatement(self, ctx:KotlinParser.StatementContext):
        pass

    # Exit a parse tree produced by KotlinParser#statement.
    def exitStatement(self, ctx:KotlinParser.StatementContext):
        pass


    # Enter a parse tree produced by KotlinParser#functionDecl.
    def enterFunctionDecl(self, ctx:KotlinParser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by KotlinParser#functionDecl.
    def exitFunctionDecl(self, ctx:KotlinParser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by KotlinParser#parameterList.
    def enterParameterList(self, ctx:KotlinParser.ParameterListContext):
        pass

    # Exit a parse tree produced by KotlinParser#parameterList.
    def exitParameterList(self, ctx:KotlinParser.ParameterListContext):
        pass


    # Enter a parse tree produced by KotlinParser#parameter.
    def enterParameter(self, ctx:KotlinParser.ParameterContext):
        pass

    # Exit a parse tree produced by KotlinParser#parameter.
    def exitParameter(self, ctx:KotlinParser.ParameterContext):
        pass


    # Enter a parse tree produced by KotlinParser#type.
    def enterType(self, ctx:KotlinParser.TypeContext):
        pass

    # Exit a parse tree produced by KotlinParser#type.
    def exitType(self, ctx:KotlinParser.TypeContext):
        pass


    # Enter a parse tree produced by KotlinParser#ifStatement.
    def enterIfStatement(self, ctx:KotlinParser.IfStatementContext):
        pass

    # Exit a parse tree produced by KotlinParser#ifStatement.
    def exitIfStatement(self, ctx:KotlinParser.IfStatementContext):
        pass


    # Enter a parse tree produced by KotlinParser#whenStatement.
    def enterWhenStatement(self, ctx:KotlinParser.WhenStatementContext):
        pass

    # Exit a parse tree produced by KotlinParser#whenStatement.
    def exitWhenStatement(self, ctx:KotlinParser.WhenStatementContext):
        pass


    # Enter a parse tree produced by KotlinParser#whenEntry.
    def enterWhenEntry(self, ctx:KotlinParser.WhenEntryContext):
        pass

    # Exit a parse tree produced by KotlinParser#whenEntry.
    def exitWhenEntry(self, ctx:KotlinParser.WhenEntryContext):
        pass


    # Enter a parse tree produced by KotlinParser#whileStatement.
    def enterWhileStatement(self, ctx:KotlinParser.WhileStatementContext):
        pass

    # Exit a parse tree produced by KotlinParser#whileStatement.
    def exitWhileStatement(self, ctx:KotlinParser.WhileStatementContext):
        pass


    # Enter a parse tree produced by KotlinParser#doWhileStatement.
    def enterDoWhileStatement(self, ctx:KotlinParser.DoWhileStatementContext):
        pass

    # Exit a parse tree produced by KotlinParser#doWhileStatement.
    def exitDoWhileStatement(self, ctx:KotlinParser.DoWhileStatementContext):
        pass


    # Enter a parse tree produced by KotlinParser#forStatement.
    def enterForStatement(self, ctx:KotlinParser.ForStatementContext):
        pass

    # Exit a parse tree produced by KotlinParser#forStatement.
    def exitForStatement(self, ctx:KotlinParser.ForStatementContext):
        pass


    # Enter a parse tree produced by KotlinParser#tryStatement.
    def enterTryStatement(self, ctx:KotlinParser.TryStatementContext):
        pass

    # Exit a parse tree produced by KotlinParser#tryStatement.
    def exitTryStatement(self, ctx:KotlinParser.TryStatementContext):
        pass


    # Enter a parse tree produced by KotlinParser#catchClause.
    def enterCatchClause(self, ctx:KotlinParser.CatchClauseContext):
        pass

    # Exit a parse tree produced by KotlinParser#catchClause.
    def exitCatchClause(self, ctx:KotlinParser.CatchClauseContext):
        pass


    # Enter a parse tree produced by KotlinParser#finallyClause.
    def enterFinallyClause(self, ctx:KotlinParser.FinallyClauseContext):
        pass

    # Exit a parse tree produced by KotlinParser#finallyClause.
    def exitFinallyClause(self, ctx:KotlinParser.FinallyClauseContext):
        pass


    # Enter a parse tree produced by KotlinParser#returnStatement.
    def enterReturnStatement(self, ctx:KotlinParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by KotlinParser#returnStatement.
    def exitReturnStatement(self, ctx:KotlinParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by KotlinParser#valDecl.
    def enterValDecl(self, ctx:KotlinParser.ValDeclContext):
        pass

    # Exit a parse tree produced by KotlinParser#valDecl.
    def exitValDecl(self, ctx:KotlinParser.ValDeclContext):
        pass


    # Enter a parse tree produced by KotlinParser#varDecl.
    def enterVarDecl(self, ctx:KotlinParser.VarDeclContext):
        pass

    # Exit a parse tree produced by KotlinParser#varDecl.
    def exitVarDecl(self, ctx:KotlinParser.VarDeclContext):
        pass


    # Enter a parse tree produced by KotlinParser#exprStatement.
    def enterExprStatement(self, ctx:KotlinParser.ExprStatementContext):
        pass

    # Exit a parse tree produced by KotlinParser#exprStatement.
    def exitExprStatement(self, ctx:KotlinParser.ExprStatementContext):
        pass


    # Enter a parse tree produced by KotlinParser#block.
    def enterBlock(self, ctx:KotlinParser.BlockContext):
        pass

    # Exit a parse tree produced by KotlinParser#block.
    def exitBlock(self, ctx:KotlinParser.BlockContext):
        pass


    # Enter a parse tree produced by KotlinParser#breakStatement.
    def enterBreakStatement(self, ctx:KotlinParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by KotlinParser#breakStatement.
    def exitBreakStatement(self, ctx:KotlinParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by KotlinParser#continueStatement.
    def enterContinueStatement(self, ctx:KotlinParser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by KotlinParser#continueStatement.
    def exitContinueStatement(self, ctx:KotlinParser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by KotlinParser#throwStatement.
    def enterThrowStatement(self, ctx:KotlinParser.ThrowStatementContext):
        pass

    # Exit a parse tree produced by KotlinParser#throwStatement.
    def exitThrowStatement(self, ctx:KotlinParser.ThrowStatementContext):
        pass


    # Enter a parse tree produced by KotlinParser#expression.
    def enterExpression(self, ctx:KotlinParser.ExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#expression.
    def exitExpression(self, ctx:KotlinParser.ExpressionContext):
        pass


    # Enter a parse tree produced by KotlinParser#arrayCreation.
    def enterArrayCreation(self, ctx:KotlinParser.ArrayCreationContext):
        pass

    # Exit a parse tree produced by KotlinParser#arrayCreation.
    def exitArrayCreation(self, ctx:KotlinParser.ArrayCreationContext):
        pass


    # Enter a parse tree produced by KotlinParser#literal.
    def enterLiteral(self, ctx:KotlinParser.LiteralContext):
        pass

    # Exit a parse tree produced by KotlinParser#literal.
    def exitLiteral(self, ctx:KotlinParser.LiteralContext):
        pass


    # Enter a parse tree produced by KotlinParser#binaryOp.
    def enterBinaryOp(self, ctx:KotlinParser.BinaryOpContext):
        pass

    # Exit a parse tree produced by KotlinParser#binaryOp.
    def exitBinaryOp(self, ctx:KotlinParser.BinaryOpContext):
        pass


    # Enter a parse tree produced by KotlinParser#unaryOp.
    def enterUnaryOp(self, ctx:KotlinParser.UnaryOpContext):
        pass

    # Exit a parse tree produced by KotlinParser#unaryOp.
    def exitUnaryOp(self, ctx:KotlinParser.UnaryOpContext):
        pass


    # Enter a parse tree produced by KotlinParser#unaryPostfixOp.
    def enterUnaryPostfixOp(self, ctx:KotlinParser.UnaryPostfixOpContext):
        pass

    # Exit a parse tree produced by KotlinParser#unaryPostfixOp.
    def exitUnaryPostfixOp(self, ctx:KotlinParser.UnaryPostfixOpContext):
        pass


    # Enter a parse tree produced by KotlinParser#rangeExpression.
    def enterRangeExpression(self, ctx:KotlinParser.RangeExpressionContext):
        pass

    # Exit a parse tree produced by KotlinParser#rangeExpression.
    def exitRangeExpression(self, ctx:KotlinParser.RangeExpressionContext):
        pass



del KotlinParser