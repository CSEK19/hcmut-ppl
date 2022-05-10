import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):

    def test_414(self):
        input = """
            Class Program {
               Var a: Int = 5;
               Var b: Int = a + 1;
               main(){}
            }
        """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 414))

    def test_415(self):
        input = """
            Class Program {
               main(){
                    Var a:Array[Int,2];

                    a = Array(1,2,3);
               }
            }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),[IntLit(1),IntLit(2),IntLit(3)])"
        self.assertTrue(TestChecker.test(input, expect, 415))

    def test_416(self):
        input = """
            Class Program {
               main(){
                    Var a:Array[Int,2];

                    a = Array("a","b");
               }
            }
        """
        expect = "Type Mismatch In Statement: AssignStmt(Id(a),[StringLit(a),StringLit(b)])"
        self.assertTrue(TestChecker.test(input, expect, 416))

    def test_417(self):
        input = """
            Class A {

                goo(){Return 1;}

                foo(){

                    Var x : Int = Self.goo; 
                }
            }
        """
        expect = "Undeclared Attribute: goo"
        self.assertTrue(TestChecker.test(input, expect, 417))

    def test_418(self):
        input = """
            Class A {

                Var goo : Int = 1;

                foo(){

                    Var x : Int = Self.goo(); 
                }
            }
        """
        expect = "Undeclared Method: goo"
        self.assertTrue(TestChecker.test(input, expect, 418))

    def test_419(self):
        input = """
            Class A {

                Var A : Array[String, 5] = Array("Hello");

            }
        """
        expect = "Type Mismatch In Statement: VarDecl(Id(A),ArrayType(5,StringType),[StringLit(Hello)])"
        self.assertTrue(TestChecker.test(input, expect, 419))


    def test_420(self):
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
        self.assertTrue(TestChecker.test(input, expect, 420))

    def test_421(self):
        input = """
                Class A {

                    foo() {
                        Var a: Array[Int, 3] = Array(1,2,3);
                        a[4] = 5; ## Index out of bound ##
                        a[1][2] = 4; ## Error with dimension##
                    }
                }
            """
        expect = "Type Mismatch In Expression: ArrayCell(Id(a),[IntLit(1),IntLit(2)])"
        self.assertTrue(TestChecker.test(input, expect, 421))

    def test_422(self):
        # NOTE: This case check for param compatiblity of Constructor
        input = """
                        Class Student
                        {
                            Var name: String;
                            Var ID: Int;
                            Constructor(newName: String; newID : Int)
                            {
                                Self.name = newName;
                                Self.ID = newID;
                            }
                        }
                        Class Program
                        {
                            main()
                            {
                                Var myStudent: Student = New Student ();
                            }
                        }
            """

        expect = "Type Mismatch In Expression: NewExpr(Id(Student),[])"
        self.assertTrue(TestChecker.test(input, expect, 422))

    def test_423(self):
        input = """
                        Class A
                        {
                        }
                        Class B:A
                        {
                            Var a: A = New C();
                        }
            """

        expect = "Undeclared Class: C"
        self.assertTrue(TestChecker.test(input, expect, 423))

    def test_424(self):
        # NOTE: This case check for param compatiblity of Constructor
        input = """
                        Class A
                        {
                        }
                        Class B:A
                        {
                            Var a: A = New B();
                        }
            """

        expect = "Type Mismatch In Statement: VarDecl(Id(a),ClassType(Id(A)),NewExpr(Id(B),[]))"
        self.assertTrue(TestChecker.test(input, expect, 424))

    def test_425(self):
        input = """
                        Class Program{

                            Val $someStatic : Int = 10;

                            foo() {

                                Var Program : Float = 1.0;

                                Var x : Int = Program::$someStatic;

                           }

                        }
            """

        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 425))

    def test_426(self):
        input = """
                Class A {
                      Var foo: Int = 1;
                      foo() {
                      }
                }
            """

        expect = "No Entry Point"
        self.assertTrue(TestChecker.test(input, expect, 426))