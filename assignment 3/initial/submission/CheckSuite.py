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
        expect = "No Entry Point"
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
            }
        }
        """
        expect = "No Entry Point"
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
        input = """
                        Class Z{
                            m(){
                                Var z:Float = 1.22;
                                Var d:Boolean = (("abc" +. "def") ==. "ghi") || False;
                                Var m:Boolean = 0==False;
                                Var f:Boolean = "abc"||1;
                            }
                        }"""
        expect = "Type Mismatch In Expression: BinaryOp(==,IntLit(0),BooleanLit(False))"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_424(self):
        input = """
                        Class Z{
                            m(){
                                Var z:Float = --------1.22;
                                Var d:Boolean = !((("abc" +. "def") ==. "ghi") || False);
                                Var m:Float = !!!!--1.22;
                            }
                        }"""
        expect = "Type Mismatch In Expression: UnaryOp(!,UnaryOp(-,UnaryOp(-,FloatLit(1.22))))"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_425(self):
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
        input = """
        Class X{
            Val a:Int = 24;
            z(){Return 2.4;}
        }
        Class Y{
            Var x: X = New X();
            Var y: Y = New Y();
            Var z: X = New Y();
        }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(z),ClassType(Id(X)),NewExpr(Id(Y),[]))"
        self.assertTrue(TestChecker.test(input, expect, 427))

    def test_428(self):
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
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(m),StringType,CallExpr(Id(y),Id(z),[IntLit(1),IntLit(2)]))"
        self.assertTrue(TestChecker.test(input, expect, 432))
    def test_433(self):
        input = """
                        Class Z{
                            m(){
                                Val y : Int = 22.4;
                            }
                        }"""
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(y),IntType,FloatLit(22.4))"
        self.assertTrue(TestChecker.test(input, expect, 433))

    def test_434(self):
        input = """
        Class Z{
            m(){
                Val x : Float = -(1 + 1);
                Val y : Float = -(2.4 +1);
                Val z : Boolean = !!((1>2)&&(True || ("abc"==."cef")));
                Val d :String = ("abc" +. "def")+."ghi";
                Val m :String = True==1;
            }
        }
        """
        expect = "Type Mismatch In Expression: BinaryOp(==,BooleanLit(True),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 434))

    def test_435(self):
        input = """
        Class X{
            Var x:Int = 1;
            Var y: String = "Hello World";
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
        }
        """
        expect = "Type Mismatch In Expression: CallExpr(Id(y),Id(d),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 435))

    def test_436(self):
        input = """
            Class B {
                Var y: String = "Hello World";
                Var b: Int = 213123122.2123123;
            }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(b),IntType,FloatLit(213123122.2123123))"
        self.assertTrue(TestChecker.test(input, expect, 436))

    def test_437(self):
        input = """
        Class X {
            Var x: Int;
            Val y: Int = 1;
            z()
            {
                Val h: Int = Self.x - 1;
                Val j: Int = Self.y - 1;
            }
        }
        """
        expect = "Illegal Constant Expression: BinaryOp(-,FieldAccess(Self(),Id(x)),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 437))

    def test_438(self):
        input = """
        Class Program {
                    Var x: Int;
                    Val y: Int = 0;
                    Var z: Int;
                    Val arr: Array[Int,2] = Array(1, Self.x);
                    Val test3: Int = Self.arr[Self.y];
                    Val test4: Int = Self.arr[Self.z];
                }"""
        expect = "Illegal Constant Expression: ArrayCell(FieldAccess(Self(),Id(arr)),[FieldAccess(Self(),Id(z))])"
        self.assertTrue(TestChecker.test(input, expect, 438))

    def test_439(self):
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
            }
        }"""
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 439))

    def test_440(self):
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
        input = """
        Class A {
        Val a:Int = 2;
           $fooExp1(){
                Self.a = "abc";
           }
        }
        """
        expect = "Illegal Member Access: FieldAccess(Self(),Id(a))"
        self.assertTrue(TestChecker.test(input, expect, 441))

    def test_442(self):
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
        input = """
                        Class Z{
                            m(){
                                Var y:String = "1";
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
                                Var x:Int = 2022 ;
                            }
                        }
                        """
        expect = "Redeclared Variable: x"
        self.assertTrue(TestChecker.test(input, expect, 444))

    def test_445(self):
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
        input = """
                        Class Z{
                            m(){
                                Var y:Int = 0;
                                Val x:Int = 1;
                                Val z:Float = x+2;
                                Val d:Float = y+3;
                            }
                        }"""
        expect = "Illegal Constant Expression: BinaryOp(+,Id(y),IntLit(3))"
        self.assertTrue(TestChecker.test(input, expect, 448))

    def test_449(self):
        input = """
                        Class Z{
                            m(){
                                Var y:Int = 0;
                                Val x:Int = 1;
                                Val z:Float = x+1;
                                Val d:Float = y + "PPL";
                            }
                        }"""
        expect = "Type Mismatch In Expression: BinaryOp(+,Id(y),StringLit(PPL))"
        self.assertTrue(TestChecker.test(input, expect, 449))

    def test_450(self):
        input = """
                        Class Z{
                            m(){
                                Var xyz: Array[Array[Int, 2],2] = Array(Array(0,0),Array(1,1));
                                xyz[1] = Array(0,1);
                                xyz[1][1] = 1;
                                xyz = 1;
                            }
                        }"""
        expect = "Type Mismatch In Statement: AssignStmt(Id(xyz),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 450))

    def test_451(self):
        input = """
                        Class Z{
                            m(){
                                Var y:Int = 0;
                                Val x:Int = 1;
                                Val z:Float = x+1;
                            }
                        }
                         Class Vehicle {

                            Var y : Int = 10;
                            foo() {
                                Var x : Int = Self.y;
                                Var y : Int = y;
                            }
                        }"""
        expect = "Undeclared Identifier: y"
        self.assertTrue(TestChecker.test(input, expect, 451))

    def test_452(self):
        input = """
                         Class Vehicle {
                            run() {
                                Var y:Array[Int,2];
                                y = Array(1,2);
                                y = Array(1,2.3);
                            }
                        }"""
        expect = "Illegal Array Literal: [IntLit(1),FloatLit(2.3)]"
        self.assertTrue(TestChecker.test(input, expect, 452))

    def test_453(self):
        input = """         
                        Class Clock{
                        func(){
                            counter.run();
                        }
                        }"""
        expect = "Undeclared Identifier: counter"
        self.assertTrue(TestChecker.test(input, expect, 453))

    def test_454(self):
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
        input = """
        Class X{
           $foo(){
                Val x: Array[Array[Int, 2],2] = Array(Array(1,1),Array(1,1));
                x[1] = Array(1,1);
           }
        }"""
        expect = "Cannot Assign To Constant: AssignStmt(ArrayCell(Id(x),[IntLit(1)]),[IntLit(1),IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 456))

    def test_457(self):
        input = """         
        Class Program {
            main(){
                Return 1;
            }
        }
        """
        expect = "Type Mismatch In Statement: Return(IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 457))

    def test_458(self):
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
        expect = "Undeclared Class: x"
        self.assertTrue(TestChecker.test(input, expect, 460))

    def test_461(self):
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
        input = """         
        Class Y{
            $y(){
                Return 1;
            }
        } 
        Class Program{
            abc(){}
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 465))

    def test_466(self):
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
        input = """     
        Class E {
           func() {                        
           } 
           Constructor(y:Int){
           }                       
        }                        
        Class Test{  
            Var y: String = "Hello World";                  
            Var m: E = New E(1);              
            Var x: E = New E();                                
        } """
        expect = "Type Mismatch In Expression: NewExpr(Id(E),[])"
        self.assertTrue(TestChecker.test(input, expect, 471))

    def test_472(self):
        input = """     
        Class E {
        Var test:String = "test_472";
           func() {                        
           } 
           Constructor(y:Int){
           }                       
        }                        
        Class Test{                        
          Var m: E = New E(1);              
          Val x: String = New E(1);                                
        } """
        expect = "Type Mismatch In Constant Declaration: ConstDecl(Id(x),StringType,NewExpr(Id(E),[IntLit(1)]))"
        self.assertTrue(TestChecker.test(input, expect, 472))

    def test_473(self):
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
        self.assertTrue(TestChecker.test(input, expect, 479))

    def test_480(self):
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
        expect = "Illegal Member Access: FieldAccess(Self(),Id(x))"
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
        expect = "Illegal Member Access: FieldAccess(Self(),Id(x))"
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
        expect = "Illegal Array Literal: [[IntLit(1),IntLit(1)],[IntLit(1),IntLit(1),StringLit(Hello World)]]"
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



    def test_493(self):
        input = """
                Class A {
                    Var $myArray: Array[Array[Array[Int,4],2],2] = Array(
                        Array(
                            Array(1,2,3,4),
                            Array(5,6,7,8)
                        ),
                        Array(
                            Array(-1,-2,-3,-4),
                            Array(-5,-6,-7, False)
                        )
                    );
                }
            """
        expect = "Illegal Array Literal: [[[IntLit(1),IntLit(2),IntLit(3),IntLit(4)],[IntLit(5),IntLit(6),IntLit(7),IntLit(8)]],[[UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(2)),UnaryOp(-,IntLit(3)),UnaryOp(-,IntLit(4))],[UnaryOp(-,IntLit(5)),UnaryOp(-,IntLit(6)),UnaryOp(-,IntLit(7)),BooleanLit(False)]]]"
        self.assertTrue(TestChecker.test(input, expect, 493))

    def test_494(self):
        input = """
        Class A{}
        Class B{Var a : A = New A(1,2,3);}     
            """
        expect = "Type Mismatch In Expression: NewExpr(Id(A),[IntLit(1),IntLit(2),IntLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 494))

    def test_495(self):
        input = """
        Class A{}
        Class B{Var a : A = New A();}
        Class C{
            Var a: Int;
            Val b: Int = 0;
            Var c: Int;
            Var arr: Array[Int,2] = Array(1, a);
            Val test1: Int = arr[0];
            Val test2: Int = arr[1];
        }
            """
        expect = "Illegal Constant Expression: ArrayCell(Id(arr),[IntLit(1)])"
        self.assertTrue(TestChecker.test(input, expect, 495))

    def test_496(self):
        input = """
        Class B{
            Var x, y: Int;
            foo(str: String){
                Break;
                Return "PPL";
            }
        }
        Class Program{
            main(){
            }
        }
            """
        expect = "Break Not In Loop"
        self.assertTrue(TestChecker.test(input, expect, 496))

    def test_497(self):
            input = """
            Class B{
                Var x, y: Int;
                foo(str: String){
                    Return "PPL";
                }
            }
            Class Programmer{
                main(){
                }
            }
                """
            expect = "No Entry Point"
            self.assertTrue(TestChecker.test(input, expect, 497))

    def test_498(self):
        input = """
        Class X {
            Var x: Int;
            Val y: Int = 1;
            foo()
            {
                Val z: Int = Self.x - 1;
            }
        }
        """
        expect = "Illegal Constant Expression: BinaryOp(-,FieldAccess(Self(),Id(x)),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 498))

    def test_499(self):
        input = """
        Class Program
        {
            Val $ABC : Int = 10;
            foo() {
                Var Program : Float = 1.0;
                Var x : Int = Program::$ABC;
           }
        }
        """
        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 499))
