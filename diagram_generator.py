from antlr_gen.KotlinParserListener import KotlinParserListener
from antlr_gen.KotlinParser import KotlinParser

class KotlinActivityListenerImpl(KotlinParserListener):
    def __init__(self):
        self.uml_lines = []
        self.label_count = 0
        self.indent = ""
        self.inside_function = False

    def get_plantuml(self):
        return "\n".join(self.uml_lines)

    def new_label(self):
        self.label_count += 1
        return f"L{self.label_count}"

    def enterFunctionDecl(self, ctx: KotlinParser.FunctionDeclContext):
        self.uml_lines.append("start")
        self.inside_function = True

    def exitFunctionDecl(self, ctx: KotlinParser.FunctionDeclContext):
        self.uml_lines.append("stop") 
        self.inside_function = False

    def enterReturnStatement(self, ctx: KotlinParser.ReturnStatementContext):
        if ctx.expression():
            expr_text = ctx.expression().getText()
            self.uml_lines.append(f":return {expr_text};")
        else:
            self.uml_lines.append(f":return;")

    def enterIfStatement(self, ctx: KotlinParser.IfStatementContext):
        condition = ctx.expression().getText()
        self.uml_lines.append(f"if ({condition}) then (yes)")

    def exitIfStatement(self, ctx: KotlinParser.IfStatementContext):
        if ctx.ELSE():
            self.uml_lines.insert(-1, "else (no)")  
        self.uml_lines.append("endif")

    def enterForStatement(self, ctx: KotlinParser.ForStatementContext):
        var_name = ctx.ID().getText()
        range_expr = ctx.expression().getText()
        self.uml_lines.append(f"group for {var_name} in {range_expr}")

    def exitForStatement(self, ctx: KotlinParser.ForStatementContext):
        self.uml_lines.append("end group")

    
    def enterWhileStatement(self, ctx: KotlinParser.WhileStatementContext):
        condition = ctx.expression().getText()
        self.uml_lines.append(f"while ({condition}) is (true)")

    def exitWhileStatement(self, ctx: KotlinParser.WhileStatementContext):
        self.uml_lines.append("endwhile")

    
    def enterDoWhileStatement(self, ctx: KotlinParser.DoWhileStatementContext):
        self.uml_lines.append("repeat")

    def exitDoWhileStatement(self, ctx: KotlinParser.DoWhileStatementContext):
        condition = ctx.expression().getText()
        self.uml_lines.append(f"repeat while ({condition})")

    def enterExprStatement(self, ctx: KotlinParser.ExprStatementContext):
        expr_text = ctx.expression().getText()

    # Prepoznavanje i transformacija += izraza 
        if "+=" in expr_text:
            var, value = expr_text.split("+=")
            var = var.strip()
            value = value.strip()
            expr_text = f"{var} = {var} + {value}"

        self.uml_lines.append(f":{expr_text};")


    def enterWhenStatement(self, ctx: KotlinParser.WhenStatementContext):
        condition = ctx.expression().getText()
        self.uml_lines.append(f"switch ({condition})")

    def enterWhenEntry(self, ctx: KotlinParser.WhenEntryContext):
        expr = ctx.expression()
        label = expr.getText() if expr else "else"
        self.uml_lines.append(f"case ({label})")

    def enterValDecl(self, ctx: KotlinParser.ValDeclContext):
        var_name = ctx.ID().getText()
        if ctx.expression():
            value = ctx.expression().getText()
            self.uml_lines.append(f":{var_name} = {value};")
    
    
    def enterVarDecl(self, ctx: KotlinParser.ValDeclContext):
        var_name = ctx.ID().getText()
        if ctx.expression():
            value = ctx.expression().getText()
            self.uml_lines.append(f":{var_name} = {value};")



    def exitWhenStatement(self, ctx: KotlinParser.WhenStatementContext):
        self.uml_lines.append("endswitch")

    def enterTryStatement(self, ctx: KotlinParser.TryStatementContext):
        self.uml_lines.append("group try")

    def enterCatchClause(self, ctx: KotlinParser.CatchClauseContext):
        var_name = ctx.ID().getText()
        self.uml_lines.append(f"group catch ({var_name})")

    def exitCatchClause(self, ctx: KotlinParser.CatchClauseContext):
        self.uml_lines.append("end group")

    def enterFinallyClause(self, ctx: KotlinParser.FinallyClauseContext):
        self.uml_lines.append("group finally")

    def exitFinallyClause(self, ctx: KotlinParser.FinallyClauseContext):
        self.uml_lines.append("end group")

    def exitTryStatement(self, ctx: KotlinParser.TryStatementContext):
        self.uml_lines.append("end group")

    def enterBreakStatement(self, ctx: KotlinParser.BreakStatementContext):
        self.uml_lines.append(":break;")

    def enterContinueStatement(self, ctx: KotlinParser.ContinueStatementContext):
        self.uml_lines.append(":continue;")

    def enterThrowStatement(self, ctx: KotlinParser.ThrowStatementContext):
        expr = ctx.expression().getText()
        self.uml_lines.append(f":throw {expr};")

    









