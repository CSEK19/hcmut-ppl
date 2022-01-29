import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):
    # Test 1: Simple program
    def test_201(self):
        input = """Class Program {
            main() {
                Out.printInt();
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))
    
    # Test 2: Example program
    def test_202(self):
        input = """Class Shape { 
            Val $numOfShape: Int = 0; 
            Val immutableAttribute: Int = 0; 
            Var length, width: Int; 
            $getNumOfShape() { 
                Return $numOfShape; 
            } 
        }
        Class Rectangle: Shape { 
            getArea() { 
                Return Self.length * Self.width; 
            } 
        } 
        Class Program { 
            main() { 
                Out.printInt(Shape::$numOfShape); 
        } 
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))
    
    # Test 3:  Test If statement
    def test_203(self):
        input = """Class Program {
            main() { 
                Var x: Int = 8;
                    If(){
                        Out.printInt(x);
                }
                Else{
                    Out.printInt(0);
                }
            } 
        }"""
        expect = "Error on line 4 col 23: )"
        self.assertTrue(TestParser.test(input, expect, 203))

    # Test 4:  Test If statement
    def test_204(self):
        input = """Class Program {
            main() { 
                Var x: Int = 8;
                If(x>4){
                    Return x;
                }
                Elseif(x<4 && x>2){
                    Return x+2;
                }
                Elseif(x>0 && x<2){
                    Return x+4;
                }
                Else{
                    Return 0;
                }
            } 
        }
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,204))

    # Test 5:  Continue & For statement
    def test_205(self):
        input = """Class Program {
            main() { 
                Foreach (i In 1 .. 100 By 2) { 
                    If(x%2 == 0){
                        Out.printInt(i); 
                    }
                }
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 205))

    # Test 6:  Statement in class
    def test_206(self):
        input = """Class B{
            Var a: Int = 0;
            a = 111;
        }"""
        expect = "Error on line 3 col 14: ="
        self.assertTrue(TestParser.test(input, expect, 206))

    # Test 7:  Constructor & Destructor
    def test_207(self):
        input = """Class A{
            Constructor(a, b: String; c, d: Int){
               Self.a = a;
               Self.b = b;
               Self.sum = c + d;
            }
            Destructor(){}
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    # Test 8:  Constructor & Destructor
    def test_208(self):
        input = """Class A{
            Constructor(){
               Self.a = 0;
               Self.b = 0;
            }
            Destructor(x: Int){}
        }"""
        expect = "Error on line 6 col 23: x"
        self.assertTrue(TestParser.test(input, expect, 208))

    # Test 9:  Parameter
    def test_209(self):
        input = """Class A{
            B(a: Int;){
               x = C::$Neg(a);
            }
        }
        Class C{
            Negative(m){
                Return -m;
            }
        }"""
        expect = "Error on line 2 col 21: )"
        self.assertTrue(TestParser.test(input, expect, 209))

    # Test 10:  Parameter 2
    def test_210(self):
        input = """Class A{
            $B(a: Int; b,: Boolean){
               This.x = a+b;
               This.y = (a*b)/(a+b);
            }
        }"""
        expect = "Error on line 2 col 25: :"
        self.assertTrue(TestParser.test(input, expect, 210))

    # Test 11:  Parameter 3
    def test_211(self):
        input = """Class A{
            $B(a: Int = 10){
               This.x = a+b;
               This.y = (a*b)/(a+b);
            }
        }"""
        expect = "Error on line 2 col 22: ="
        self.assertTrue(TestParser.test(input, expect, 211))

    # Test 12: Attribute declaration
    def test_212(self):
        input = """Class A{
            Val My1stCons, My2ndCons: Int = 1 + 5, 2;
            Var $x, $y : Int = 0, 0;
            $B(a,b: Boolean){
                Out.printInt(a-b==x-y);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 212))

    # Test 13: Attribute declaration
    def test_213(self):
        input = """Class A{
            Val My1stCons, My2ndCons: Int = 1 + 5, 2;
            Var $x, $y : Int = 0, 0;
            $B(a,b: Boolean){
                Out.printInt(a-b==x-y);
            }
        }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    # Test 14: Attribute declaration
    def test_214(self):
        input = """Class A{
            Val $a, b: Int = 8;
            }
        }"""
        expect = "Error on line 2 col 30: ;"
        self.assertTrue(TestParser.test(input, expect, 214))

    # Test 15: Attribute declaration
    def test_215(self):
        input = """Class A{
            Val $a, b: Int = 8;
            }
        }"""
        expect = "Error on line 2 col 30: ;"
        self.assertTrue(TestParser.test(input, expect, 215))

    # Test 16: Array declaration
    def test_216(self):
        input = """Class A{
               Var a: Array[Int,12];
           }"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 216))

    # Test 17: Array declaration
    def test_217(self):
        input = """Class A{
               Val $a: Array[Array,12];
           }"""
        expect = "Error on line 2 col 33: ,"
        self.assertTrue(TestParser.test(input, expect, 217))

    # Test 18: Test Class available
    def test_218(self):
        input = """Val $a: Array[Array,12];"""
        expect = "Error on line 1 col 0: Val"
        self.assertTrue(TestParser.test(input, expect, 218))

    # Test 18: Test Class available
    def test_219(self):
        input = """Val $a: Array[Array,12];"""
        expect = "Error on line 1 col 0: Val"
        self.assertTrue(TestParser.test(input, expect, 218))