import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_484(self):
        """Simple program: int main() {} """
        input = """     
        Class Program{main(){}}
                        Class A {
                           Var a:Int = 1;
                           $fooExp1(x:Float; y:String){
                                Return Self.a;
                           } 
                           $fooExp2(x:Float; y:String){
                                Return x;
                           }  
                           $fooExp3(x:Float; y:String){
                                Return y;
                           }               
                        }                        
                        Class BB{
                            foo2(){
                                Var e:Float = (New A()).a - 7;
                                e = A::$fooExp1(1, "a") +2 - -----5;
                                e = A::$fooExp2(1, "a") + 1;
                                Var f:String = A::$fooExp3(1, "a") +. "abc";
                                Var g:String = A::$fooExp3(1, "a") + 1;
                            }
                        }"""
        expect = "Type Mismatch In Expression: BinaryOp(+,CallExpr(Id(A),Id($fooExp3),[IntLit(1),StringLit(a)]),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 484))
