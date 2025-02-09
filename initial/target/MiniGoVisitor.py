# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .MiniGoParser import MiniGoParser
else:
    from MiniGoParser import MiniGoParser

# This class defines a complete generic visitor for a parse tree produced by MiniGoParser.

class MiniGoVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by MiniGoParser#program.
    def visitProgram(self, ctx:MiniGoParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#decl.
    def visitDecl(self, ctx:MiniGoParser.DeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#typee.
    def visitTypee(self, ctx:MiniGoParser.TypeeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrType.
    def visitArrType(self, ctx:MiniGoParser.ArrTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#dimenList.
    def visitDimenList(self, ctx:MiniGoParser.DimenListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structDecl.
    def visitStructDecl(self, ctx:MiniGoParser.StructDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structBody.
    def visitStructBody(self, ctx:MiniGoParser.StructBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#listField.
    def visitListField(self, ctx:MiniGoParser.ListFieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#field.
    def visitField(self, ctx:MiniGoParser.FieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfaceDecl.
    def visitInterfaceDecl(self, ctx:MiniGoParser.InterfaceDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#interfaceBody.
    def visitInterfaceBody(self, ctx:MiniGoParser.InterfaceBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#listMethod.
    def visitListMethod(self, ctx:MiniGoParser.ListMethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#method.
    def visitMethod(self, ctx:MiniGoParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#paramList.
    def visitParamList(self, ctx:MiniGoParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#paramPrime.
    def visitParamPrime(self, ctx:MiniGoParser.ParamPrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#param.
    def visitParam(self, ctx:MiniGoParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#nameList.
    def visitNameList(self, ctx:MiniGoParser.NameListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#varDecl.
    def visitVarDecl(self, ctx:MiniGoParser.VarDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#constDecl.
    def visitConstDecl(self, ctx:MiniGoParser.ConstDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literalConst.
    def visitLiteralConst(self, ctx:MiniGoParser.LiteralConstContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcDecl.
    def visitFuncDecl(self, ctx:MiniGoParser.FuncDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcBody.
    def visitFuncBody(self, ctx:MiniGoParser.FuncBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodStructDecl.
    def visitMethodStructDecl(self, ctx:MiniGoParser.MethodStructDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrAccess.
    def visitArrAccess(self, ctx:MiniGoParser.ArrAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#positionList.
    def visitPositionList(self, ctx:MiniGoParser.PositionListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprA.
    def visitExprA(self, ctx:MiniGoParser.ExprAContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprA1.
    def visitExprA1(self, ctx:MiniGoParser.ExprA1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprA2.
    def visitExprA2(self, ctx:MiniGoParser.ExprA2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprA3.
    def visitExprA3(self, ctx:MiniGoParser.ExprA3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprA4.
    def visitExprA4(self, ctx:MiniGoParser.ExprA4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprA5.
    def visitExprA5(self, ctx:MiniGoParser.ExprA5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprA6.
    def visitExprA6(self, ctx:MiniGoParser.ExprA6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#operandA.
    def visitOperandA(self, ctx:MiniGoParser.OperandAContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structAccess.
    def visitStructAccess(self, ctx:MiniGoParser.StructAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#refList.
    def visitRefList(self, ctx:MiniGoParser.RefListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprS.
    def visitExprS(self, ctx:MiniGoParser.ExprSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprS1.
    def visitExprS1(self, ctx:MiniGoParser.ExprS1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprS2.
    def visitExprS2(self, ctx:MiniGoParser.ExprS2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprS3.
    def visitExprS3(self, ctx:MiniGoParser.ExprS3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprS4.
    def visitExprS4(self, ctx:MiniGoParser.ExprS4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprS5.
    def visitExprS5(self, ctx:MiniGoParser.ExprS5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprS6.
    def visitExprS6(self, ctx:MiniGoParser.ExprS6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#operandS.
    def visitOperandS(self, ctx:MiniGoParser.OperandSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrStructAccess.
    def visitArrStructAccess(self, ctx:MiniGoParser.ArrStructAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#accessList.
    def visitAccessList(self, ctx:MiniGoParser.AccessListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrLit.
    def visitArrLit(self, ctx:MiniGoParser.ArrLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#arrBody.
    def visitArrBody(self, ctx:MiniGoParser.ArrBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elementList.
    def visitElementList(self, ctx:MiniGoParser.ElementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#element.
    def visitElement(self, ctx:MiniGoParser.ElementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structLit.
    def visitStructLit(self, ctx:MiniGoParser.StructLitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structElList.
    def visitStructElList(self, ctx:MiniGoParser.StructElListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structELPrime.
    def visitStructELPrime(self, ctx:MiniGoParser.StructELPrimeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#structEL.
    def visitStructEL(self, ctx:MiniGoParser.StructELContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#funcCall.
    def visitFuncCall(self, ctx:MiniGoParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#argumentList.
    def visitArgumentList(self, ctx:MiniGoParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#methodCall.
    def visitMethodCall(self, ctx:MiniGoParser.MethodCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprM.
    def visitExprM(self, ctx:MiniGoParser.ExprMContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprM1.
    def visitExprM1(self, ctx:MiniGoParser.ExprM1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprM2.
    def visitExprM2(self, ctx:MiniGoParser.ExprM2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprM3.
    def visitExprM3(self, ctx:MiniGoParser.ExprM3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprM4.
    def visitExprM4(self, ctx:MiniGoParser.ExprM4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprM5.
    def visitExprM5(self, ctx:MiniGoParser.ExprM5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#exprM6.
    def visitExprM6(self, ctx:MiniGoParser.ExprM6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#operandM.
    def visitOperandM(self, ctx:MiniGoParser.OperandMContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr.
    def visitExpr(self, ctx:MiniGoParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr1.
    def visitExpr1(self, ctx:MiniGoParser.Expr1Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr2.
    def visitExpr2(self, ctx:MiniGoParser.Expr2Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr3.
    def visitExpr3(self, ctx:MiniGoParser.Expr3Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr4.
    def visitExpr4(self, ctx:MiniGoParser.Expr4Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr5.
    def visitExpr5(self, ctx:MiniGoParser.Expr5Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#expr6.
    def visitExpr6(self, ctx:MiniGoParser.Expr6Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#operand.
    def visitOperand(self, ctx:MiniGoParser.OperandContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#literal.
    def visitLiteral(self, ctx:MiniGoParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statement.
    def visitStatement(self, ctx:MiniGoParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#statementList.
    def visitStatementList(self, ctx:MiniGoParser.StatementListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#varDeclStatement.
    def visitVarDeclStatement(self, ctx:MiniGoParser.VarDeclStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#constDeclStatement.
    def visitConstDeclStatement(self, ctx:MiniGoParser.ConstDeclStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignment.
    def visitAssignment(self, ctx:MiniGoParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#lhs.
    def visitLhs(self, ctx:MiniGoParser.LhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignOperator.
    def visitAssignOperator(self, ctx:MiniGoParser.AssignOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#rhs.
    def visitRhs(self, ctx:MiniGoParser.RhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#ifStatement.
    def visitIfStatement(self, ctx:MiniGoParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#elifList.
    def visitElifList(self, ctx:MiniGoParser.ElifListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#eliff.
    def visitEliff(self, ctx:MiniGoParser.EliffContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forStatement.
    def visitForStatement(self, ctx:MiniGoParser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forBasic.
    def visitForBasic(self, ctx:MiniGoParser.ForBasicContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forInitial.
    def visitForInitial(self, ctx:MiniGoParser.ForInitialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#initialization.
    def visitInitialization(self, ctx:MiniGoParser.InitializationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#varDeclInitial.
    def visitVarDeclInitial(self, ctx:MiniGoParser.VarDeclInitialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#condition.
    def visitCondition(self, ctx:MiniGoParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#update.
    def visitUpdate(self, ctx:MiniGoParser.UpdateContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#assignScalar.
    def visitAssignScalar(self, ctx:MiniGoParser.AssignScalarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#forRange.
    def visitForRange(self, ctx:MiniGoParser.ForRangeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#breakStatement.
    def visitBreakStatement(self, ctx:MiniGoParser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#continueStatement.
    def visitContinueStatement(self, ctx:MiniGoParser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#callStatement.
    def visitCallStatement(self, ctx:MiniGoParser.CallStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by MiniGoParser#returnStatement.
    def visitReturnStatement(self, ctx:MiniGoParser.ReturnStatementContext):
        return self.visitChildren(ctx)



del MiniGoParser