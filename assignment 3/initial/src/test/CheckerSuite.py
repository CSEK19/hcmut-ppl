import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_400(self):
        input = """
        Class Test{
            Var x:Int;
            Var z:Int;
            Var x:Int;
        }
        """
        expect = "Redeclared Attribute: x"
        self.assertTrue(TestChecker.test(input,expect,400))

    def test_401(self):
        input = """
        Class x{}
        Class x:y{}
        Class y{}
        """
        expect = "Redeclared Class: x"
        self.assertTrue(TestChecker.test(input,expect,401))

    def test_402(self):
        input = """
        Class x{
            foo(xyz:Int; xyz:String){}
            }
        """
        expect = "Redeclared Parameter: xyz"
        self.assertTrue(TestChecker.test(input,expect,402))

    def test_403(self):
        input = """
        Class x{
                Var y:Int;
                y(){}
            }
        """
        expect = "Redeclared Method: y"
        self.assertTrue(TestChecker.test(input,expect,403))

    def test_404(self):
        input = """
        Class x{
            y(){
                Var z:Boolean;
                Var z:Boolean;
            }
        }
        """
        expect = "Redeclared Variable: z"
        self.assertTrue(TestChecker.test(input,expect,404))

    def test_405(self):
        input = """
        Class x{
            func(){
                Val yz:Int = 1;
                Val yz:Int = 1;
            }
        }
        """
        expect = "Redeclared Constant: yz"
        self.assertTrue(TestChecker.test(input,expect,405))

    def test_406(self):
        input = """
        Class x{
            func(x:String){
                Val x:Boolean = True;
            }
        }
        """
        expect = "Redeclared Constant: x"
        self.assertTrue(TestChecker.test(input,expect,406))

    def test_407(self):
        input = """
        Class x{
            func(y:Int){
                Var y:String = "Hello World";
            }
        }
        """
        expect = "Redeclared Variable: y"
        self.assertTrue(TestChecker.test(input,expect,407))

    def test_408(self):
        input = """
        Class x{
            func(){
                Var y:Int = 0b1;
                {
                    Var y:Int = 0x1;
                    Var x:Int = 1;
                    Var x:Int = 1;
                }
            }
            }
        """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input,expect,408))

    def test_409(self):
        input = """
        Class x{
            func(){
                Var y:Int = 0b1;
                {
                    Var y:Int = 0x1;
                    Var x:Int = 0x123;
                    Val x:Int = 1;
                }
            }
        }
        """
        expect = "Redeclared Constant: x"
        self.assertTrue(TestChecker.test(input,expect,409))

    def test_410(self):
        input = """
        Class x{
            func(){
                Var y:Int = 1;
                h = 1;
            }
        }
        """
        expect = "Undeclared Identifier: h"
        self.assertTrue(TestChecker.test(input,expect,410))

    def test_411(self):
        input = """
        Class X{}
        Class Y:Z{}
        """
        expect = "Undeclared Class: Z"
        self.assertTrue(TestChecker.test(input,expect,411))

    def test_412(self):
        input = """
        Class X{
            Var x:Int = 1;
        }
        Class Y{
            x(){
                Var y:Int = 1;
                Var z:X;
                z.x = 1;
                z.z = 1;
            }
        }
        """
        expect = "Undeclared Attribute: z"
        self.assertTrue(TestChecker.test(input,expect,412))

    def test_413(self):
        input = """
        Class X{
            Var x:Int = 1;
            z(){}
        }
        Class Y{
            x(){
                Var y:Int = 1;
                Var z:X;
                z.x = 1;
                z.z = 1;
            }
        }
        """
        expect = "Undeclared Attribute: z"
        self.assertTrue(TestChecker.test(input, expect, 413))

    def test_414(self):
        input = """
        Class X{
            Var x:Int = 1;
            z(){}
        }
        Class Y{
            x(){
                Var y:Int = 1;
                Var z:X;
                z.x = 1;
                z.z();
                z.func();
            }
        }
        """
        expect = "Undeclared Method: func"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_415(self):
        input = """
        Class X{
            Var x:Int = 1;
            z(){}
        }
        Class Y:X{}
        Class Z:SIGMA{}
        """
        expect = "Undeclared Class: SIGMA"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_416(self):
        input = """
        Class X{
            Var x:Int = 1;
            z(){}
        }
        Class Y:X{}
        Class D{
            func(){
                Var y:X;
                Var a:Int;
                y.x = 2;
                y.z();
                y.func = 2;
            }
        }
        """
        expect = "Undeclared Attribute: func"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_417(self):
        input = """ 
        Class X{
            Var x:Int = 1;
            z(){}
        }
        Class Y:X{}
        Class Z{
            m(){
                Var y:Y;
                Var a:Int;
                y.x= 2;
                y.z();
                y.m();
            }
        }
        """
        expect = "Undeclared Method: m"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_418(self):
        input = """
        Class Z{
            m(){
                Val const:Int = 4124122;
                const = 12312;
            }
        }
        """
        expect = "Cannot Assign To Constant: AssignStmt(Id(const),IntLit(12312))"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_419(self):
        input = """
                        Class Z{
                            m(){
                                Var y:Int = 2;
                                Var x:Array[Int,5];
                                x[1]=1;
                                y[1]=1;
                            }
                        }"""
        expect = "Type Mismatch In Expression: ArrayCell(Id(y),[IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 419))

    def test_420(self):
        input = """
        Class Z{
            m(){
                Var y:Int = 2;
                Var x:Array[Int,5];
                x[1.2]=1;
            }
        }
        """
        expect = "Type Mismatch In Expression: ArrayCell(Id(x),[FloatLit(1.2)])"
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_421(self):
        input = """
        Class Z{
            m(){
                Var y:Int = 0x123+2+3;
                Var x:Float = 1+2.2+3.5;
                Var z:Float = 0+True;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,IntLit(0),BooleanLit(True))"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_422(self):
        input = """
        Class Z{
            m(){
                Var z:String = "xyz" +. "abc";
                Var d:Boolean = ("xyz" +. "abc") ==. "def";
                Var m:String = ("xyz" ==. "abc") +. "def";
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+.,BinaryOp(==.,StringLit(xyz),StringLit(abc)),StringLit(def))"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_423(self):
        """Simple program: int main() {} """
        input = """
                        Class Z{
                            m(){
                                Var z:Float = 1.22;
                                Var d:Boolean = (("abc" +. "def") ==. "ghi") || False;
                                Var m:Boolean = 0==False;
                                Var f:Boolean = "abc"||1;
                            }
                        }"""
        expect = "Type Mismatch In Expression: BinaryOp(||,StringLit(abc),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_424(self):
        """Simple program: int main() {} """
        input = """
                        Class Z{
                            m(){
                                Var z:Float = --------1.22;
                                Var d:Boolean = !((("abc" +. "def") ==. "ghi") || False);
                                Var m:Float = !!!!--1.22;
                            }
                        }"""
        expect = "Type Mismatch In Expression: UnaryOp(!,UnaryOp(-,UnaryOp(-,FloatLit(1.22))))"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_425(self):
        """Simple program: int main() {} """
        input = """
                        Class X{
                            Var x:Int = 1;
                            z(g:Int; h:Float){
                                Return 1;
                            }
                            d(){}
                        }
                        Class Z{
                            m(){
                                Var y:X;
                                Var d:Int = y.z(1,2);
                                Var m:Int = y.z(1,"abc");
                            }
                        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(y),Id(z),[IntLit(1),StringLit(abc)])"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_426(self):
        """Simple program: int main() {} """
        input = """
                        Class X{
                            Var x:Int = 1;
                            z(g:Int; h:Float){
                                Return 1;
                            }
                            d(){}
                        }
                        Class Z{
                            m(){
                                Var y:X;
                                Var d:Float = y.z(1,2);
                                Var m:String = y.z(1.1,2);
                            }
                        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(y),Id(z),[FloatLit(1.1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 426))

    def test_427(self):
        """Simple program: int main() {} """
        input = """
                        Class X{
                            Var x:Int = 1;
                            z(g:Int; h:Float){
                                Return 1;
                            }
                            d(){}
                        }
                        Class Z{
                            m(){
                                Var y:X;
                                Var d:Float = y.z(1,2);
                                Var m:String = y.z(1.1,2);
                            }
                        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(y),Id(z),[FloatLit(1.1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_428(self):
        """Simple program: int main() {} """
        input = """
                        Class X{
                            Var x:Int = 1;
                            z(g:Int; h:Float){
                                Return 1;
                            }
                            d(){}
                        }
                        Class Z{
                            m(){
                                Var y:X;
                                Var d:Float = y.z(1,2);
                                Var m:String = y.z(1,2);
                            }
                        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(m),StringType,CallExpr(Id(y),Id(z),[IntLit(1),IntLit(2)]))"
        self.assertTrue(TestChecker.test(input, expect, 428))

    def test_429(self):
        """Simple program: int main() {} """
        input = """
                        Class X{
                            Var x:Int = 1;
                            z(g:Int; h:Float){
                                Return 1;
                            }
                            d(){}
                        }
                        Class Z{
                            m(){
                                Var y:X;
                                Var d:Float = y.z(1,2);
                                y.d();
                                Var m:String = y.d();
                            }
                        }"""
        expect = "Type Mismatch In Expression: CallExpr(Id(y),Id(d),[])"
        self.assertTrue(TestChecker.test(input, expect, 429))

    def test_430(self):
        """Simple program: int main() {} """
        input = """
                        Class X{
                            Var x:Int = 1;
                            z(g:Int; h:Float){
                                Return 1;
                            }
                            d(){}
                        }
                        Class Z{
                            m(){
                                Var y:X;
                                Var d:Float = y.z(1,2);
                                y.d();
                                Var m:Float = y.x;
                                Var f:Float = y.d;
                            }
                        }"""
        expect = "Undeclared Attribute: d"
        self.assertTrue(TestChecker.test(input, expect, 430))

    def test_431(self):
        """Simple program: int main() {} """
        input = """
                        Class X{
                            Var x:Int = 1;
                            z(g:Int; h:Float){
                                Return 1;
                            }
                            d(){}
                        }
                        Class Z{
                            m(){
                                Var y:X;
                                Var d:Float = y.z(1,2);
                                y.d();
                                Var m:Float = y.x;
                                Var f:String = y.x;
                            }
                        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(f),StringType,FieldAccess(Id(y),Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 431))

    def test_432(self):
        """Simple program: int main() {} """
        input = """
                        Class X{
                            Var x:Int = 1;
                            z(g:Int; h:Float){
                                Return 1;
                            }
                            d(){}
                        }
                        Class Z{
                            m(){
                                Val y:X = New X();
                                Val d:Float = y.z(1,2);
                                Val m:String = y.z(1,2);
                            }
                        }"""
        expect = "Illegal Constant Expression: CallExpr(Id(y),Id(z),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 432))
    def test_433(self):
        """Simple program: int main() {} """
        input = """
                        Class Z{
                            m(){
                                Val y : Int = 1.2;
                            }
                        }"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(y),IntType,FloatLit(1.2))"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_434(self):
        """Simple program: int main() {} """
        input = """
                        Class Z{
                            m(){
                                Val y : Float = -(1.2 +1);
                                Val x : Float = -(1 + 1);
                                Val z : Boolean = !!((1>2)&&(True || ("abc"==."cef")));
                                Val d :String = ("abc" +. "def")+."ghi";
                                Val m :String = True==1;
                            }
                        }"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(m),StringType,BinaryOp(==,BooleanLit(True),IntLit(1)))"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_435(self):
        """Simple program: int main() {} """
        input = """
                        Class X{
                            Var x:Int = 1;
                            z(g:Int; h:Float){
                                Return 1;
                            }
                            d(){}
                        }
                        Class Z{
                            m(){
                                Val y:X = New X();
                                Val d:Float = y.z(1,2);
                                Val m:String = y.d(1,2);
                            }
                        }"""
        expect = "Illegal Constant Expression: CallExpr(Id(y),Id(z),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_436(self):
        """Simple program: int main() {} """
        input = """
                        Class X{
                            Var x:Int = 1;
                            z(g:Int; h:Float){
                                Return 1;
                            }
                            d(x:Int; y:Float; z:String){}
                        }
                        Class Z{
                            m(){
                                Val y:X = New X();
                                Val d:Float = y.z(1,2);
                                y.d(1,2,"y");
                                y.d(1,2,3);
                            }
                        }"""
        expect = "Illegal Constant Expression: CallExpr(Id(y),Id(z),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_437(self):
        """Simple program: int main() {} """
        input = """
                        Class X{
                            Var x:Int = 1;
                            z(g:Int; h:Float){
                                Return 1;
                            }
                            d(x:Int; y:Float; z:String){}
                        }
                        Class Z{
                            m(){
                                Val y:X = New X();
                                Val d:Float = y.z(1,2);
                                y.d(1+2,2--2.0,"y"+."bcd");
                                y.z(1,2);
                            }
                        }"""
        expect = "Illegal Constant Expression: CallExpr(Id(y),Id(z),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_438(self):
        """Simple program: int main() {} """
        input = """
                        Class X{
                            Var x:Int = 1;
                            z(g:Int; h:Float){
                                Return 1;
                            }
                            d(x:Int; y:Float; z:String){}
                        }
                        Class Z{
                            m(){
                                Val y:X = New X();
                                Val d:Float = y.z(1,2);
                                y.d(1+2,2--2.0,"y"==."bcd");
                            }
                        }"""
        expect = "Illegal Constant Expression: CallExpr(Id(y),Id(z),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_439(self):
        """Simple program: int main() {} """
        input = """
                        Class X{
                            Var x:Int = 1;
                            z(g:Int; h:Float){
                                Return 1;
                            }
                            d(x:Int; y:Float; z:String){}
                        }
                        Class Z{
                            m(){
                                Val y:X = New X();
                                Val d:Float = y.z(1,2);
                                y.d(1+2,2--2.0,("y"==."bcd")+1);
                            }
                        }"""
        expect = "Illegal Constant Expression: CallExpr(Id(y),Id(z),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_440(self):
        """Simple program: int main() {} """
        input = """
                        Class X{
                            Var x:Int = 1;
                            z(g:Int; h:Float){
                                Return 1;
                            }
                            d(x:Int; y:Float; z:String){}
                        }
                        Class Y{}
                        Class Z{
                            m(){
                                Var y:X = New X();
                                y = New Y();
                            }
                        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(y),NewExpr(Id(Y),[]))"
        self.assertTrue(TestChecker.test(input, expect, 440))

    def test_441(self):
        """Simple program: int main() {} """
        input = """
                        Class X{
                            Var x:Int = 1;
                            z(g:Int; h:Float){
                                Return 1;
                            }
                            d(x:Int; y:Float; z:String){}
                        }
                        Class Y:X{}
                        Class Z{
                            m(){
                                Var x:X = New X();
                                x = New Y();
                                Var y:Y = New Y();
                                y = New X();
                            }
                        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(y),NewExpr(Id(X),[]))"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_442(self):
        """Simple program: int main() {} """
        input = """
                        Class Z{
                            m(){
                                Val y:Int = 1;
                                Val x:Float = 1;
                                Val z:Float = y+x;
                                Val d:Int = y+x;
                            }
                        }"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(d),IntType,BinaryOp(+,Id(y),Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 442))

    def test_443(self):
        """Simple program: int main() {} """
        input = """
                        Class Z{
                            m(){
                                Var y:Int = 1;
                                Var x:Float = 1;
                                Var z:Float = y+x;
                                Var d:Int = y+x;
                            }
                        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(d),IntType,BinaryOp(+,Id(y),Id(x)))"
        self.assertTrue(TestChecker.test(input, expect, 443))

    def test_444(self):
        """Simple program: int main() {} """
        input = """
                        Class Z{
                            m(){
                                Var y:Int = 1;
                                Var x:Int = 1;
                                If (True){
                                    Var y:Int = 2;
                                }
                                Elseif(True){
                                    Var y:Int = 2;
                                }
                                Else{
                                    Var y:Int = 2;
                                }
                                Var x:Int = 2 ;
                            }
                        }"""
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_445(self):
        """Simple program: int main() {} """
        input = """
                        Class Z{
                            m(){
                                Var y:Int = 1;
                                Var x:Int = 1;
                                Var i:Int = 0;
                                Foreach(i In 1 .. 10 By 1){
                                    Var y:Int = 1;
                                    Break;
                                    If (True){
                                        Var y:Int = 1;
                                        Continue;
                                    }
                                }
                                Var x:Int = 2 ;
                            }
                        }"""
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 445))

    def test_446(self):
        """Simple program: int main() {} """
        input = """
                        Class Z{
                            m(){
                                Var i:Int = 0;
                                Foreach(i In 1 .. 10 By 1){
                                    Var y:Int = 1;
                                    Break;
                                    If (True){
                                        Var y:Int = 1;
                                        Continue;
                                    }
                                }
                                Break;
                            }
                        }"""
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 446))

    def test_447(self):
        """Simple program: int main() {} """
        input = """
                        Class Z{
                            m(){
                                Var i:Int = 0;
                                Foreach(i In 1 .. 10 By 1){
                                    Var y:Int = 1;
                                    Break;
                                    If (True){
                                        Var y:Int = 1;
                                        Continue;
                                    }
                                }
                                Continue;
                            }
                        }"""
        expect = "Continue Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 447))

    def test_448(self):
        """Simple program: int main() {} """
        input = """
                        Class Z{
                            m(){
                                Var y:Int = 0;
                                Val x:Int = 1;
                                Val z:Float = x+1;
                                Val d:Float = y+1;
                            }
                        }"""
        expect = "Illegal Constant Expression: BinaryOp(+,Id(y),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_449(self):
        """Simple program: int main() {} """
        input = """
                        Class Z{
                            m(){
                                Var y:Int = 0;
                                Val x:Int = 1;
                                Val z:Float = x+1;
                                Val d:Float = y + "abc";
                            }
                        }"""
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(y),StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_450(self):
        """Simple program: int main() {} """
        input = """
                        Class Z{
                            m(){
                                Var y:Int = 0;
                                Val x:Int = 1;
                                Val z:Float = x+1;
                                Val d:Float = y + "abc";
                            }
                        }"""
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(y),StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_451(self):
        """Simple program: int main() {} """
        input = """
                        Class Z{
                            m(){
                                Var y:Int = 0;
                                Val x:Int = 1;
                                Val z:Float = x+1;
                            }
                        }
                         Class Car {

                            Var y : Int = 10;
                            foo() {
                                Var x : Int = Self.y;
                                Var y : Int = y;
                            }
                        }"""
        expect = "Undeclared Identifier: y"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_452(self):
        """Simple program: int main() {} """
        input = """
                         Class Car {
                            foo() {
                                Var y:Array[Int,2];
                                y = Array(1,2);
                                y = Array(1,2.3);
                            }
                        }"""
        expect = "Illegal Array Literal: [IntLit(1),FloatLit(2.3)]"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_453(self):
        """Simple program: int main() {} """
        input = """         
                        Class X{
                        func(){
                            count.foo();
                        }
                        }"""
        expect = "Undeclared Identifier: count"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_454(self):
        """Simple program: int main() {} """
        input = """
                        Class Y{
                            Var $y:Int = 5;
                            Var x:Int = 4;
                        }         
                        Class X{
                        func(){
                            Var x:Int = Y::$y;
                            x = count.foo();
                        }
                        }"""
        expect = "Undeclared Identifier: count"
        self.assertTrue(TestChecker.test(input, expect, 454))

    def test_455(self):
        """Simple program: int main() {} """
        input = """         
                        Class Y{
                            Var $y:Int = 5;
                            Var x:Int = 4;
                        }         
                        Class X{
                        func(){
                            Var x:Int = Y::$y;
                            x = Y.x;
                        }
                        }"""
        expect = "Illegal Member Access: FieldAccess(Id(Y),Id(x))"
        self.assertTrue(TestChecker.test(input, expect, 455))

    def test_456(self):
        """Simple program: int main() {} """
        input = """         
                        Class Y{
                            Var $y:Int = 5;
                            Var x:Int = 4;
                        }         
                        Class X{
                        func(){
                            Var x:Y = New Y();
                            Var z:Int = x.x;
                            Var d:Int = x::$y;
                        }
                        }"""
        expect = "Illegal Member Access: FieldAccess(Id(x),Id($y))"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_457(self):
        """Simple program: int main() {} """
        input = """         
                        Class Y{
                            $y(){}
                            x(){}
                        }         
                        Class X{
                        func(){
                            Y::$y();
                            Var x:Y = New Y();
                            x.x();
                            x::$y();
                        }
                        }"""
        expect = "Illegal Member Access: Call(Id(x),Id($y),[])"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_458(self):
        """Simple program: int main() {} """
        input = """         
                        Class Y{
                            $y(){}
                            x(){}
                        }         
                        Class X{
                        func(){
                            Y::$y();
                            Var x:Y = New Y();
                            x.x();
                            Y.x();
                        }
                        }"""
        expect = "Illegal Member Access: Call(Id(Y),Id(x),[])"
        self.assertTrue(TestChecker.test(input, expect, 458))

    def test_459(self):
        """Simple program: int main() {} """
        input = """         
                        Class Y{
                            $y(){
                                Return 1;
                            }
                            x(){
                                Return 1;
                            }
                        }         
                        Class X{
                        func(){
                            Var x:Y = New Y();
                            Var z:Int = Y::$y();
                            z = x.x();
                            z = Y.x();
                        }
                        }"""
        expect = "Illegal Member Access: CallExpr(Id(Y),Id(x),[])"
        self.assertTrue(TestChecker.test(input, expect, 459))

    def test_460(self):
        """Simple program: int main() {} """
        input = """         
                        Class Y{
                            $y(){
                                Return 1;
                            }
                            x(){
                                Return 1;
                            }
                        }         
                        Class X{
                        func(){
                            Var x:Y = New Y();
                            Var z:Int = Y::$y();
                            z = x.x();
                            z = x::$y();
                        }
                        }"""
        expect = "Illegal Member Access: CallExpr(Id(x),Id($y),[])"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_461(self):
        """Simple program: int main() {} """
        input = """         
                        Class Y{
                            $y(){
                                Return 1;
                            }
                            x(){
                                Return 1;
                            }
                        } """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 461))

    def test_462(self):
        """Simple program: int main() {} """
        input = """         
                        Class Y{
                            $y(){
                                Return 1;
                            }
                            x(){
                                Return 1;
                            }
                        } 
                        Class Program{
                            z(){
                                Return 1;
                            }
                        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 462))

    def test_463(self):
        """Simple program: int main() {} """
        input = """         
                        Class Y{
                            $y(){
                                Return 1;
                            }
                            x(){
                                Return 1;
                            }
                        } 
                        Class Program{
                            $main(){
                                Return 1;
                            }
                        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 463))

    def test_464(self):
        """Simple program: int main() {} """
        input = """         
                        Class Y{
                            $y(){
                                Return 1;
                            }
                            x(){
                                Return 1;
                            }
                        } 
                        Class Program{
                            $main(y:Int){
                            }
                        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 464))

    def test_465(self):
        """Simple program: int main() {} """
        input = """         
                        Class Y{
                            $y(){
                                Return 1;
                            }
                            x(){
                                Return 1;
                            }
                        } 
                        Class Program{
                            main(){}
                        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_466(self):
        """Simple program: int main() {} """
        input = """         
                        Class Y{
                            Var y:Int = 1;
                            foo(){
                                Var x:Int = Self.y;
                                Var z:Int = y;
                            }
                        } """
        expect = "Undeclared Identifier: y"
        self.assertTrue(TestChecker.test(input, expect, 466))

    def test_467(self):
        """Simple program: int main() {} """
        input = """         
                        Class Y{
                        Val y:Int=10;
                        }
                        Class X{
                        Var x:Y;
                        func (){
                            Val z:Int=Self.x.y;
                        }
                        } """
        expect = "Illegal Constant Expression: FieldAccess(FieldAccess(Self(),Id(x)),Id(y))"
        self.assertTrue(TestChecker.test(input, expect, 467))

    def test_468(self):
        """Simple program: int main() {} """
        input = """     
                        Class X{
                        Var x:Int = 1;
                        foo(){
                            Return 1;
                        }
                        func (){
                            Var y:Int = Self.x;
                            y = Self.foo();
                            Var x:String = Self.foo();
                        }
                        } """
        expect = "Type Mismatch In Statement: VarDecl(Id(x),StringType,CallExpr(Self(),Id(foo),[]))"
        self.assertTrue(TestChecker.test(input, expect, 468))

    def test_469(self):
        """Simple program: int main() {} """
        input = """     
                        Class X{
                        Var x:Int = 1;
                        foo(){
                            Return 1;
                        }
                        func (){
                            Var y:Int = Self.x;
                            y = Self.foo();
                            Var x:String = Self.foofoo();
                        }
                        } """
        expect = "Undeclared Method: foofoo"
        self.assertTrue(TestChecker.test(input, expect, 469))

    def test_470(self):
        """Simple program: int main() {} """
        input = """     
                        Class E {
                           func() {                        
                           }                        
                        }                        
                        Class Test{                        
                          test() {                        
                                Var m: E = New E();                        
                                Return m.func;                       
                          }                        
                        } """
        expect = "Undeclared Attribute: func"
        self.assertTrue(TestChecker.test(input, expect, 470))

    def test_471(self):
        """Simple program: int main() {} """
        input = """     
                        Class E {
                           func() {                        
                           } 
                           Constructor(y:Int){
                           }                       
                        }                        
                        Class Test{                        
                          Var m: E = New E(1);              
                          Var x: E = New E();                                
                        } """
        expect = "Type Mismatch In Expression: NewExpr(Id(E),[])"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_472(self):
        """Simple program: int main() {} """
        input = """     
                        Class E {
                           func() {                        
                           } 
                           Constructor(y:Int){
                           }                       
                        }                        
                        Class Test{                        
                          Var m: E = New E(1);              
                          Val x: String = New E(1);                                
                        } """
        expect = "Type Mismatch In Statement: AttributeDecl(Instance,ConstDecl(Id(x),StringType,NewExpr(Id(E),[IntLit(1)])))"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_473(self):
        """Simple program: int main() {} """
        input = """     
                        Class E {
                           $func() {                        
                           } 
                           Constructor(y:Int){
                           }                       
                        }                        
                        Class Test{ 
                            cak(){                     
                                E::$func();   
                                E::$foo();                             
                            }
                        }"""
        expect = "Undeclared Method: $foo"
        self.assertTrue(TestChecker.test(input, expect, 473))

    def test_474(self):
        """Simple program: int main() {} """
        input = """     
                        Class E {
                           $func() { 
                                Return 1;                       
                           } 
                           Constructor(y:Int){
                           }                       
                        }                        
                        Class Test{ 
                            cak(){                     
                                Var y:Int = E::$func();   
                                Var x:Int = E::$foo();                             
                            }
                        }"""
        expect = "Undeclared Method: $foo"
        self.assertTrue(TestChecker.test(input, expect, 474))

    def test_475(self):
        """Simple program: int main() {} """
        input = """     
                        Class Y {
                           Var y:Int = 1;                      
                        }                        
                        Class X{ 
                            Var x:Y = New Y(); 
                        }
                        Class Z{
                            foo(){
                                Var z:X = New X();
                                Var m:Int = z.x.y;
                                Var f:Int = z.x.g;
                            }
                        }"""
        expect = "Undeclared Attribute: g"
        self.assertTrue(TestChecker.test(input, expect, 475))

    def test_476(self):
        """Simple program: int main() {} """
        input = """     
                        Class Y {
                           Var y:Int = 1;                      
                        }                        
                        Class X{ 
                            Var x:Y = New Y(); 
                        }
                        Class Z{
                            foo(){
                                Var z:X = New X();
                                Var m:Int = z.x.y;
                                Var f:Int = z.g.y;
                            }
                        }"""
        expect = "Undeclared Attribute: g"
        self.assertTrue(TestChecker.test(input, expect, 476))

    def test_477(self):
        """Simple program: int main() {} """
        input = """     
                        Class Y {
                           Var y:Int = 1;                      
                        }                        
                        Class X{ 
                            Var $x:Y = New Y(); 
                        }
                        Class Z{
                            foo(){
                                Var z:X = New X();
                                Var m:Int = X::$x.y;
                                Var f:Int = X::$x.g;
                            }
                        }"""
        expect = "Undeclared Attribute: g"
        self.assertTrue(TestChecker.test(input, expect, 477))

    def test_478(self):
        input = """     
                        Class Y {
                           Var y:Int = 1;                      
                        }                        
                        Class X{ 
                            Var $x:Y = New Y(); 
                        }
                        Class Z{
                            foo(){
                                Var z:X = New X();
                                Var m:Int = X::$x.y;
                                Var f:Int = X::$g.y;
                            }
                        }"""
        expect = "Undeclared Attribute: $g"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_479(self):
        """Simple program: int main() {} """
        input = """     
                        Class Y {
                           Var y:Int = 1;
                           foo(){
                                Return 1;
                           }                      
                        }                        
                        Class X{ 
                            Var x:Y = New Y();
                            foo(){
                                Return New Y();
                            }
                        }
                        Class Z{
                            foo(){
                                Var z:X = New X();
                                Var m:Int = z.x.y;
                                m = z.x.foo();
                                m = z.foo().y;
                                m = z.foo().foo();
                                Var f:Int = z.foo();
                            }
                        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(f),IntType,CallExpr(Id(z),Id(foo),[]))"
        self.assertTrue(TestChecker.test(input, expect, 478))

    def test_480(self):
        """Simple program: int main() {} """
        input = """     
                        Class Y {
                           Var y:Int = 1;
                           foo(x:Float; y:String){
                           }                      
                        }                        
                        Class X{ 
                            Var x:Y = New Y();
                            foo(){
                                Return New Y();
                            }
                        }
                        Class Z{
                            foo(){
                                Var z:X = New X();
                                z.foo().foo(1,"y");
                                z.x.foo(1.2,"y");
                                z.x.foo(1,1.2);
                            }
                        }"""
        expect = "Type Mismatch In Statement: Call(FieldAccess(Id(z),Id(x)),Id(foo),[IntLit(1),FloatLit(1.2)])"
        self.assertTrue(TestChecker.test(input, expect, 480))

    def test_481(self):
        """Simple program: int main() {} """
        input = """     
                        Class Y {
                           Var y:Int = 1;
                           fooExp(x:Float; y:String){
                                Return 1;
                           }  
                           fooCall(x:Float; y:String){}                    
                        }                        
                        Class X{ 
                            Var x:Y = New Y();
                            foo(){
                                Return New Y();
                            }
                            foo2(){
                                Var m:Int = Self.x.y;
                                m = Self.x.fooExp(1, "y");
                                m = Self.foo().y;
                                m = Self.foo().fooExp(1, "y");
                                Self.x.fooCall(1, "y");
                                Self.foo().fooCall(1, "y");
                                Self.g().fooCall(1, "y");
                            }
                        }"""
        expect = "Undeclared Method: g"
        self.assertTrue(TestChecker.test(input, expect, 481))

    def test_482(self):
        """Simple program: int main() {} """
        input = """     
                        Class Y {
                           Var y:Int = 1;
                           fooExp(x:Float; y:String){
                                Return 1;
                           }  
                           fooCall(x:Float; y:String){}                    
                        }                        
                        Class X{ 
                            Var x:Y = New Y();
                            foo(){
                                Return New Y();
                            }
                            foo2(){
                                Var m:Int = Self.x.y;
                                m = Self.x.fooExp(1, "y");
                                m = Self.foo().y;
                                m = Self.foo().fooExp(1, "y");
                                Self.x.fooCall(1, "y");
                                Self.foo().fooCall(1, "y");
                                Self.g().fooCall(1, "y");
                            }
                        }"""
        expect = "Undeclared Method: g"
        self.assertTrue(TestChecker.test(input, expect, 482))

    def test_483(self):
        input = """     
        Class X{
           Var x:Int = 1;
           $foo1(a:Float; b:String){
                Return Self.x;
           } 
           $foo2(x:Float; y:String){
                Return x;
           }  
           $foo3(x:Float; y:String){
                Return y;
           }               
        }                        
        Class Y{
            foo2(){
                Var e:Float = (New X()).x;
                e = X::$foo1(1, "a");
                e = X::$foo2(1, "a");
                Var h:String = X::$foo3(1, "a");
                Var j:Float = X::$foo3(1, "a");
            }
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(j),FloatType,CallExpr(Id(X),Id($foo3),[IntLit(1),StringLit(a)]))"
        self.assertTrue(TestChecker.test(input, expect, 483))

    def test_484(self):
        input = """     
        Class X{
           Var x:Int = 1;
           $foo1(a:Float; b:String){
                Return Self.x;
           } 
           $foo2(x:Float; y:String){
                Return x;
           }  
           $foo3(x:Float; y:String){
                Return y;
           }               
        }                        
        Class Y{
            foo2(){
                Var e:Float = (New X()).x;
                e = X::$foo1(1, "a");
                e = X::$foo2(1, "a");
                Var h:String = X::$foo3(1, "a");
                Var j:Float = X::$foo3(1, "a") + 1;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(+,CallExpr(Id(X),Id($foo3),[IntLit(1),StringLit(a)]),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 484))

    def test_485(self):
        input = """     
        Class Y {
           funcMethod1(x:Float; y:String){
                Var a:Array[Int, 2] = Array(1,1);
                a = Array(1,1,1);
           }               
        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),[IntLit(1),IntLit(1),IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 485))

    def test_486(self):
        input = """     
        Class Y {
           funcMethod1(x:Float; y:String){
                Var a:Array[Int, 2] = Array(1,1);
                a = Array("DSA", "PPL");
           }               
        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),[StringLit(DSA),StringLit(PPL)])"
        self.assertTrue(TestChecker.test(input, expect, 486))

    def test_487(self):
        input = """     
                        Class Y {
                           funcMethod1(x:Float; y:String){
                                Var a: Array[Array[Int, 2],2] = Array(Array(1,1),Array(1,1));
                                Var b: Array[Array[Int, 2],2] = Array(Array(1,1),Array(1));
                           }               
                        }"""
        expect = "Illegal Array Literal: [[IntLit(1),IntLit(1)],[IntLit(1)]]"
        self.assertTrue(TestChecker.test(input, expect, 487))

    def test_488(self):
        input = """     
                        Class Y {
                           funcMethod1(x:Float; y:String){
                                Var a: Array[Array[Int, 2],2] = Array(Array(1,1),Array(1,1));
                                Var b: Array[Array[Int, 2],2] = Array(Array("CS","CE"),Array("DSA","CA"));
                           }               
                        }"""
        expect = "Type Mismatch In Statement: VarDecl(Id(b),ArrayType(2,ArrayType(2,IntType)),[[StringLit(CS),StringLit(CE)],[StringLit(DSA),StringLit(CA)]])"
        self.assertTrue(TestChecker.test(input, expect, 488))

    def test_489(self):
        input = """     
                        Class Y{
                           funcMethod1(x:Float; y:String){
                                Var a: Array[Array[Int, 2],2] = Array(Array(1,1),Array(1,1,"Hello World"));
                           }               
                        }"""
        expect = "Illegal Array Literal: [IntLit(1),IntLit(1),StringLit(Hello World)]"
        self.assertTrue(TestChecker.test(input, expect, 489))

    def test_490(self):
        input = """     
                        Class Y {
                           funcMethod1(){
                                Var y: Array[Array[Int, 2],2] = Array(Array(1,1),Array(1,1));
                                y[1] = Array(1,1);
                                y[1][1] = 1;
                                y = 1;
                           }               
                        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(y),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 490))

    def test_491(self):
        input = """     
                        Class Y {
                           funcMethod1(){
                                Val y: Array[Array[Int, 2],2] = Array(Array(1,1),Array(1,1));
                                y[1] = Array(1,1);
                           }               
                        }"""
        expect = "Cannot Assign To Constant: AssignStmt(ArrayCell(Id(y),[IntLit(1)]),[IntLit(1),IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 491))

    def test_492(self):
        input = """     
                        Class Y {
                        Val y:Int = 2;
                           funcMethod1(){
                                Self.y = "abc";
                           }               
                        }"""
        expect = "Cannot Assign To Constant: AssignStmt(FieldAccess(Self(),Id(y)),StringLit(abc))"
        self.assertTrue(TestChecker.test(input, expect, 492))



