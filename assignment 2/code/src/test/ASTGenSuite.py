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
   def test_317(self):
       input = """
       Class A {
           foo(){}
       }
       """
       expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([],[]))])])'
       self.assertTrue(TestAST.test(input, expect, 317))
   def test_318(self):
       input = """
       Class A {
           foo(a,b:Int;c:Float){}
       }
       """
       expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),FloatType)],Block([],[]))])])'
       self.assertTrue(TestAST.test(input, expect, 318))
   def test_319(self):
       input = """
       Class A {
           foo(a:Int;b:Boolean;c:String){}
       }
       """
       expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[param(Id(a),IntType),param(Id(b),BoolType),param(Id(c),StringType)],Block([],[]))])])'
       self.assertTrue(TestAST.test(input, expect, 319))
   def test_320(self):
       input = """
       Class A {
           foo(){
               Var a:Int;
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),IntType)],[]))])])'
       self.assertTrue(TestAST.test(input, expect, 320))
   def test_321(self):
       input = """
       Class A {
           foo(){
               Var a:Int = 1;
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),IntType,IntLit(1))],[]))])])'
       self.assertTrue(TestAST.test(input, expect, 321))
   def test_322(self):
       input = """
       Class A {
           foo(){
               Var a:Int = 1;
               Var b:Float = 1.0;
               Val c:Boolean = True;
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),IntType,IntLit(1)),VarDecl(Id(b),FloatType,FloatLit(1.0)),ConstDecl(Id(c),BoolType,BooleanLit(True))],[]))])])'
       self.assertTrue(TestAST.test(input, expect, 322))
   def test_323(self):
       input = """
       Class A {
           Var $b:Int = 1;
           foo(){
               Var a:Int = 1;
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Static,VarDecl(Id($b),IntType,IntLit(1))),MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),IntType,IntLit(1))],[]))])])'
       self.assertTrue(TestAST.test(input, expect, 323))
   def test_324(self):
       input = """
       Class A {
           foo(a,b,c,d,e:Int){
               Var f:Int = 1+2*3;
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(d),IntType),param(Id(e),IntType)],Block([VarDecl(Id(f),IntType,BinaryOp(+,IntLit(1),BinaryOp(*,IntLit(2),IntLit(3))))],[]))])])'
       self.assertTrue(TestAST.test(input, expect, 324))
   def test_325(self):
       input = """
       Class A {
           $foo(){
               Var a:Int = 2/3;
               a=1;
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id($foo),Static,[],Block([VarDecl(Id(a),IntType,BinaryOp(/,IntLit(2),IntLit(3)))],[AssignStmt(Id(a),IntLit(1))]))])])'
       self.assertTrue(TestAST.test(input, expect, 325))
   def test_326(self):
       input = """
       Class A {
           $foo(){
               a[1][3+4]=1;
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id($foo),Static,[],Block([],[AssignStmt(ArrayCell(Id(a),[IntLit(1),BinaryOp(+,IntLit(3),IntLit(4))]),IntLit(1))]))])])'
       self.assertTrue(TestAST.test(input, expect, 326))
   def test_327(self):
       input = """
       Class A {
           foo(){
               a[1][b[3]]="abc";
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([],[AssignStmt(ArrayCell(Id(a),[IntLit(1),ArrayCell(Id(b),[IntLit(3)])]),StringLit(abc))]))])])'
       self.assertTrue(TestAST.test(input, expect, 327))
   def test_328(self):
       input = """
       Class A {
           foo(){
               a.b.c="abc";
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([],[AssignStmt(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),StringLit(abc))]))])])'
       self.assertTrue(TestAST.test(input, expect, 328))
   def test_329(self):
       input = """
       Class A {
           foo(){
               a.b.c[1]=d.e.f(1,2+3);
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([],[AssignStmt(ArrayCell(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),[IntLit(1)]),CallExpr(FieldAccess(Id(d),Id(e)),Id(f),[IntLit(1),BinaryOp(+,IntLit(2),IntLit(3))]))]))])])'
       self.assertTrue(TestAST.test(input, expect, 329))
   def test_330(self):
       input = """
       Class A {
           foo(){
               Var a:A = d.e.f(1,2+3) + 2;
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),ClassType(Id(A)),BinaryOp(+,CallExpr(FieldAccess(Id(d),Id(e)),Id(f),[IntLit(1),BinaryOp(+,IntLit(2),IntLit(3))]),IntLit(2)))],[]))])])'
       self.assertTrue(TestAST.test(input, expect, 330))
   def test_331(self):
       input = """
       Class A {
           foo(){
               Var a:Array[Array[Int,5],5];
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),ArrayType(5,ArrayType(5,IntType)))],[]))])])'
       self.assertTrue(TestAST.test(input, expect, 331))
   def test_332(self):
       input = """
       Class A {
           foo(){
               Break;
               Continue;
               Return a==.!b;
               {}
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([],[Break,Continue,Return(BinaryOp(==.,Id(a),UnaryOp(!,Id(b)))),Block([],[])]))])])'
       self.assertTrue(TestAST.test(input, expect, 332))
   def test_333(self):
       input = """
       Class A:B{
           foo(){
               a = New a(1+2*3/4).b.c();
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(foo),Instance,[],Block([],[AssignStmt(Id(a),CallExpr(FieldAccess(NewExpr(Id(a),[BinaryOp(+,IntLit(1),BinaryOp(/,BinaryOp(*,IntLit(2),IntLit(3)),IntLit(4)))]),Id(b)),Id(c),[]))]))])])'
       self.assertTrue(TestAST.test(input, expect, 333))
   def test_334(self):
       input = """
       Class A:B{
           foo(){
               a = New a(1+2*3/4).b.c();
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(foo),Instance,[],Block([],[AssignStmt(Id(a),CallExpr(FieldAccess(NewExpr(Id(a),[BinaryOp(+,IntLit(1),BinaryOp(/,BinaryOp(*,IntLit(2),IntLit(3)),IntLit(4)))]),Id(b)),Id(c),[]))]))])])'
       self.assertTrue(TestAST.test(input, expect, 334))
   def test_335(self):
       input = """
       Class A:B{
           foo(){
               a = (1+2)*3;
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(foo),Instance,[],Block([],[AssignStmt(Id(a),BinaryOp(*,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(3)))]))])])'
       self.assertTrue(TestAST.test(input, expect, 335))
   def test_336(self):
       input = """
       Class A:B{
           foo(){
               Return Self.foo();
           }
           Constructor (a,b:J){}
           Destructor (){}
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(foo),Instance,[],Block([],[Return(CallExpr(Self(),Id(foo),[]))])),MethodDecl(Id(Constructor),Instance,[param(Id(a),ClassType(Id(J))),param(Id(b),ClassType(Id(J)))],Block([],[])),MethodDecl(Id(Destructor),Instance,[],Block([],[]))])])'
       self.assertTrue(TestAST.test(input, expect, 336))
   def test_337(self):
       input = """
       Class A:B{
           Var a,$b:Int;
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Static,VarDecl(Id($b),IntType))])])'
       self.assertTrue(TestAST.test(input, expect, 337))
   def test_338(self):
       input = """
       Class A:B{
           Var a,$b:Int = 1,2;
           Val $c,d:Boolean = True, Null;
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(1))),AttributeDecl(Static,VarDecl(Id($b),IntType,IntLit(2))),AttributeDecl(Static,ConstDecl(Id($c),BoolType,BooleanLit(True))),AttributeDecl(Instance,ConstDecl(Id(d),BoolType,NullLiteral()))])])'
       self.assertTrue(TestAST.test(input, expect, 338))
   def test_339(self):
       input = """
       Class A:B{
           Var a, b, c:Int;
           Foo(){
               Var a, b, c:Int;
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Instance,VarDecl(Id(a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),IntType)),AttributeDecl(Instance,VarDecl(Id(c),IntType)),MethodDecl(Id(Foo),Instance,[],Block([VarDecl(Id(a),IntType),VarDecl(Id(b),IntType),VarDecl(Id(c),IntType)],[]))])])'
       self.assertTrue(TestAST.test(input, expect, 339))
   def test_340(self):
       input = """
       Class A:B{
           Foo(){
               Val a, b, c:Int = 1,2,3;
               Var d:Boolean = True;
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([ConstDecl(Id(a),IntType,IntLit(1)),ConstDecl(Id(b),IntType,IntLit(2)),ConstDecl(Id(c),IntType,IntLit(3)),VarDecl(Id(d),BoolType,BooleanLit(True))],[]))])])'
       self.assertTrue(TestAST.test(input, expect, 340))
   def test_341(self):
       input = """
       Class A:B{
           Var $a:Array[Int,3] = Array(1,1,1);
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Static,VarDecl(Id($a),ArrayType(3,IntType),[IntLit(1),IntLit(1),IntLit(1)]))])])'
       self.assertTrue(TestAST.test(input, expect, 341))
   def test_342(self):
       input = """
       Class A:B{
           Var $a:Array[Array[Int,1],3] = Array(Array(1),Array(1),Array(1));
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Static,VarDecl(Id($a),ArrayType(3,ArrayType(1,IntType)),[[IntLit(1)],[IntLit(1)],[IntLit(1)]]))])])'
       self.assertTrue(TestAST.test(input, expect, 342))
   def test_343(self):
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
       self.assertTrue(TestAST.test(input, expect, 343))
   def test_344(self):
       input = """
       Class A:B{
           Var $0,a,$1,b,$2,c:Int = 5,4,3,2,1,0;
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Static,VarDecl(Id($0),IntType,IntLit(5))),AttributeDecl(Instance,VarDecl(Id(a),IntType,IntLit(4))),AttributeDecl(Static,VarDecl(Id($1),IntType,IntLit(3))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(2))),AttributeDecl(Static,VarDecl(Id($2),IntType,IntLit(1))),AttributeDecl(Instance,VarDecl(Id(c),IntType,IntLit(0)))])])'
       self.assertTrue(TestAST.test(input, expect, 344))
   def test_345(self):
       input = """
       Class A:B{
           Foo(){
               If(1){}
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([],[If(IntLit(1),Block([],[]))]))])])'
       self.assertTrue(TestAST.test(input, expect, 345))
   def test_346(self):
       input = """
       Class A:B{
           Foo(){
               If(1){}
               If(2){}Else{}
               If(3){}Elseif(4){}Else{a=1;}
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([],[If(IntLit(1),Block([],[])),If(IntLit(2),Block([],[]),Block([],[])),If(IntLit(3),Block([],[]),If(IntLit(4),Block([],[]),Block([],[AssignStmt(Id(a),IntLit(1))])))]))])])'
       self.assertTrue(TestAST.test(input, expect, 346))
   def test_347(self):
       input = """
       Class A:B{
           Foo(){
               If(3){}Elseif(4){}Elseif(5){}Else{a=1;}
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([],[If(IntLit(3),Block([],[]),If(IntLit(4),Block([],[]),If(IntLit(5),Block([],[]),Block([],[AssignStmt(Id(a),IntLit(1))]))))]))])])'
       self.assertTrue(TestAST.test(input, expect, 347))
   def test_348(self):
       input = """
       Class A:B{
           Foo(){
               a.b(1+2,3*4-5.5);
               If(1)
                   {}
               Elseif(2)
                   {}
               Elseif(3)
                   {}
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([],[Call(Id(a),Id(b),[BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(-,BinaryOp(*,IntLit(3),IntLit(4)),FloatLit(5.5))]),If(IntLit(1),Block([],[]),If(IntLit(2),Block([],[]),If(IntLit(3),Block([],[]))))]))])])'
       self.assertTrue(TestAST.test(input, expect, 348))
   def test_349(self):
       input = """
       Class A: B
       {
           Foo()
           {
               If(3)
                   {Val a: Int = 0X1234;}
               Elseif(4)
                   {{}}
               Elseif(5)
                   {Return Self;}
               Else
                   {a = 1;}
           }
       }
       """
       expect = 'Program([ClassDecl(Id(A),Id(B),[MethodDecl(Id(Foo),Instance,[],Block([],[If(IntLit(3),Block([ConstDecl(Id(a),IntType,IntLit(4660))],[]),If(IntLit(4),Block([],[Block([],[])]),If(IntLit(5),Block([],[Return(Self())]),Block([],[AssignStmt(Id(a),IntLit(1))]))))]))])])'
       self.assertTrue(TestAST.test(input, expect, 349))





