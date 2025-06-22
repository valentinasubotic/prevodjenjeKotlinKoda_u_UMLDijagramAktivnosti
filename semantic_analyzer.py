from antlr4 import *
from antlr_gen.KotlinParserListener import KotlinParserListener
from antlr_gen.KotlinParser import KotlinParser

class SemanticAnalyzer(KotlinParserListener):
    def __init__(self):
        self.symbol_table = {}  # parametri i promjenljive
        self.errors = []
        self.reserved_literals = {"true", "false", "null"}
        self.builtin_identifiers = {"println", "print", "arrayOf"}
        self.builtin_properties = {"message", "stackTrace", "cause"}

    
    def analyze(self, tree):
        walker = ParseTreeWalker()
        walker.walk(self, tree)
        return self.errors

    def _is_ignored(self, ident):
        return (
            ident in self.symbol_table
        or ident in self.reserved_literals
        or ident in self.builtin_identifiers
        or ident in self.builtin_properties
        or ident.isdigit()
         )   


    def _extract_identifiers(self, expr_text):
        import re
        expr_text = re.sub(r'"[^"]*"', '', expr_text)    # ukloni string literal
        expr_text = re.sub(r"\'[^\']*\'", '', expr_text)  # ukloni char literal
        return re.findall(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b', expr_text)
    
    def enterExpression(self, ctx: KotlinParser.ExpressionContext):
    # npr. a + b
        if ctx.getChildCount() == 3:
            left = ctx.expression(0)
            right = ctx.expression(1)
            op = ctx.getChild(1).getText()

            if op == "+":
                left_name = left.getText()
                right_name = right.getText()

                left_type = self.symbol_table.get(left_name)
                right_type = self.symbol_table.get(right_name)

                if left_type and right_type and left_type != right_type:
                    self.errors.append(
                        f"[SEMANTIČKA GREŠKA] Operator '+' nije dozvoljen za tipove {left_type} i {right_type}"
                )

    def check_expression_variables(self, expr_text, kontekst="izrazu"):
        for ident in self._extract_identifiers(expr_text):
            if not self._is_ignored(ident):
                self.errors.append(f"[SEMANTIČKA GREŠKA] Nedefinisana promenljiva u {kontekst}: '{ident}'")
        self._check_binary_expr_types(expr_text)
    
    def _check_binary_expr_types(self, expr_text):
        import re
        if '+' in expr_text:
            # Uzimamo tipove samo iz tabele (ako su dostupni)
            # Ispitujemo samo najjednostavnije izraze oblika "a + b"
            parts = expr_text.split('+')
            if len(parts) == 2:
                levo = parts[0].strip()
                desno = parts[1].strip()
                tip_levo = self.symbol_table.get(levo, None)
                tip_desno = self.symbol_table.get(desno, None)
                if tip_levo and tip_desno and tip_levo != tip_desno:
                    self.errors.append(f"[SEMANTIČKA GREŠKA] Operator '+' nije dozvoljen za tipove {tip_levo} i {tip_desno}")


    def enterVarDecl(self, ctx: KotlinParser.VarDeclContext):
        var_name = ctx.ID().getText()
        if var_name in self.symbol_table:
            self.errors.append(f"[SEMANTIČKA GREŠKA] Promenljiva '{var_name}' je već definisana")
        type_ = ctx.type_().getText() if ctx.type_() else "unknown"
        self.symbol_table[var_name] = type_

        if ctx.expression():
            expr_text = ctx.expression().getText()
            for ident in self._extract_identifiers(expr_text):
                if not self._is_ignored(ident):
                    self.errors.append(f"[SEMANTIČKA GREŠKA] Nedefinisana promenljiva u izrazu: '{ident}'")

    def enterValDecl(self, ctx: KotlinParser.ValDeclContext):
        var_name = ctx.ID().getText()

        if var_name in self.symbol_table:
            self.errors.append(f"[SEMANTIČKA GREŠKA] Promenljiva '{var_name}' je već definisana")
        type_ = ctx.type_().getText() if ctx.type_() else "unknown"
        self.symbol_table[var_name] = type_

        if ctx.expression():
            expr_text = ctx.expression().getText()
            for ident in self._extract_identifiers(expr_text):
                if not self._is_ignored(ident):
                    self.errors.append(f"[SEMANTIČKA GREŠKA] Nedefinisana promenljiva u izrazu: '{ident}'")


    def enterExpressionStatement(self, ctx: KotlinParser.exprStatement):
        if ctx.expression():
            expr = ctx.expression().getText()
            for ident in self._extract_identifiers(expr):
                if not self._is_ignored(ident):
                    self.errors.append(f"[SEMANTIČKA GREŠKA] Nedefinisana promenljiva u izrazu: '{ident}'")



    def enterFunctionDecl(self, ctx: KotlinParser.FunctionDeclContext):
        self.symbol_table.clear()
        if ctx.parameterList():
            for param in ctx.parameterList().parameter():
                name = param.ID().getText()
                type_ = param.type_().getText()
                self.symbol_table[name] = type_

    def enterReturnStatement(self, ctx: KotlinParser.ReturnStatementContext):
        if ctx.expression():
            expr = ctx.expression().getText()
            self.check_expression_variables(expr, "return")

    def enterIfStatement(self, ctx: KotlinParser.IfStatementContext):
        if ctx.expression():
            expr = ctx.expression().getText()
            self.check_expression_variables(expr, "if uslovu")

    def enterWhileStatement(self, ctx: KotlinParser.WhileStatementContext):
        if ctx.expression():
            expr = ctx.expression().getText()
            self.check_expression_variables(expr, "while uslovu")

    def enterDoWhileStatement(self, ctx: KotlinParser.DoWhileStatementContext):
        if ctx.expression():
            expr = ctx.expression().getText()
            self.check_expression_variables(expr, "do-while uslovu")

    def enterForStatement(self, ctx: KotlinParser.ForStatementContext):
        if ctx.expression():
            expr = ctx.expression().getText()
            self.check_expression_variables(expr, "for opsegu")
        var_name = ctx.ID().getText()
        self.symbol_table[var_name] = "unknown"

    def enterWhenStatement(self, ctx: KotlinParser.WhenStatementContext):
        if ctx.expression():
            expr = ctx.expression().getText()
            self.check_expression_variables(expr, "when izrazu")

    def enterExprStatement(self, ctx: KotlinParser.ExprStatementContext):
        if ctx.expression():
            expr = ctx.expression().getText()
            self.check_expression_variables(expr, "izrazu")

    def enterCatchClause(self, ctx: KotlinParser.CatchClauseContext):
        if ctx.ID():
            var_name = ctx.ID().getText()
            self.symbol_table[var_name] = "Exception"  # ili bilo koja vrednost

