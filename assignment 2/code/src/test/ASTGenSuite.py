import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
   def test_300(self):
       input = """
       Class A:B{
           Var $0:Int;
           $foo(i:Array [Boolean ,0105]){
               a=0105;
               b.c(Self,Null,Array(1)).d=0x12DEF;
               d[e][f[g]]=0B1010111011101;
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Static,VarDecl(Id($0),IntType)),MethodDecl(Id($foo),Static,[param(Id(i),ArrayType(69,BoolType))],Block([],[AssignStmt(Id(a),IntLit(69)),AssignStmt(FieldAccess(CallExpr(Id(b),Id(c),[Self(),NullLiteral(),[IntLit(1)]]),Id(d)),IntLit(77295)),AssignStmt(ArrayCell(Id(d),[Id(e),ArrayCell(Id(f),[Id(g)])]),IntLit(5597))]))])])'
       self.assertTrue(TestAST.test(input,expect,300))


