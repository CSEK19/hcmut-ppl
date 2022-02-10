import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
   def test_300(self):
       """Simple program: int main() {} """
       input = "Class Program {}"
       expect = 'Program([ClassDecl(Id(Program),[])])'
       self.assertTrue(TestAST.test(input,expect,300))

   def test_301(self):
       """Simple program: int main() {} """
       input = "Class A:B {}"
       expect = 'Program([ClassDecl(Id(A),Id(B),[])])'
       self.assertTrue(TestAST.test(input,expect,301))

   def test_302(self):
       """Simple program: int main() {} """
       input = "Class A {} Class B {} Class C {}"
       expect = 'Program([ClassDecl(Id(A),[]),ClassDecl(Id(B),[]),ClassDecl(Id(C),[])])'
       self.assertTrue(TestAST.test(input,expect,302))

   def test_303(self):
       """Simple program: int main() {} """
       input = """
       Class A {
           Var a:Int;
       }
       """
       expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType))])])'
       self.assertTrue(TestAST.test(input,expect,303))
   def test_304(self):
       """Simple program: int main() {} """
       input = """
       Class A {
           Var a:Int;
           Var b:Int;
       }
       """
       expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType))])])'
       self.assertTrue(TestAST.test(input,expect,304))
   def test_305(self):
       """Simple program: int main() {} """
       input = """
       Class A {
           Var a:Array[Int,5];
       }
       """
       expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),ArrayType(5,IntType)))])])'
       self.assertTrue(TestAST.test(input,expect,305))
   def test_306(self):
       """Simple program: int main() {} """
       input = """
       Class A {
           Var a:Int=1;
       }
       """
       expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(1)))])])'
       self.assertTrue(TestAST.test(input,expect,306))
   def test_307(self):
       """Simple program: int main() {} """
       input = """
       Class A {
           Var a:Int=1+1;
       }
       """
       expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,IntLit(1),IntLit(1))))])])'
       self.assertTrue(TestAST.test(input,expect,307))
   def test_308(self):
       """Simple program: int main() {} """
       input = """
       Class A {
           Var a:Int=1+1*2;
       }
       """
       expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(1),IntLit(2)))))])])'
       self.assertTrue(TestAST.test(input,expect,308))
   def test_309(self):
       """Simple program: int main() {} """
       input = """
       Class A {
           Var a:Int=\"abc\"+.1+2;
       }
       """
       expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(+.,StringLit(abc),BinaryOp(+,IntLit(1),IntLit(2)))))])])'
       self.assertTrue(TestAST.test(input,expect,309))
   def test_310(self):
       """Simple program: int main() {} """
       input = """
       Class A {
           Var a:Int=!!a---2*---3;
       }
       """
       expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType,BinaryOp(-,UnaryOp(!,UnaryOp(!,Id(a))),BinaryOp(*,UnaryOp(-,UnaryOp(-,IntLit(2))),UnaryOp(-,UnaryOp(-,UnaryOp(-,IntLit(3))))))))])])'
       self.assertTrue(TestAST.test(input,expect,310))
   def test_311(self):
       """Simple program: int main() {} """
       input = """
       Class A {
           Val a:Boolean=True;
       }
       """
       expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),BoolType,BooleanLit(True)))])])'
       self.assertTrue(TestAST.test(input,expect,311))
   def test_312(self):
       """Simple program: int main() {} """
       input = """
       Class A {
           Val a:String=b[1][1];
       }
       """
       expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(a),StringType,ArrayCell(Id(b),[IntLit(1),IntLit(1)])))])])'
       self.assertTrue(TestAST.test(input,expect,312))
   def test_313(self):
       """Simple program: int main() {} """
       input = """
       Class A {
           Var a:Int = New a();
       }
       """
       expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(a),IntType,NewExpr(Id(a),[])))])])'
       self.assertTrue(TestAST.test(input,expect,313))
   def test_314(self):
       """Simple program: int main() {} """
       input = """
       Class A {
           Val b:Int = Null;
       }
       """
       expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(b),IntType,NullLiteral()))])])'
       self.assertTrue(TestAST.test(input,expect,314))
   def test_315(self):
       """Simple program: int main() {} """
       input = """
       Class A {
           Val b:Int = New a(1+2,Null);
       }
       """
       expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,ConstDecl(Id(b),IntType,NewExpr(Id(a),[BinaryOp(+,IntLit(1),IntLit(2)),NullLiteral()])))])])'
       self.assertTrue(TestAST.test(input,expect,315))
   def test_316(self):
       """Simple program: int main() {} """
       input = """
       Class A {
           Var $b:Float=6.9;
       }
       """
       expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Static,VarDecl(Id($b),FloatType,FloatLit(6.9)))])])'
       self.assertTrue(TestAST.test(input,expect,316))




