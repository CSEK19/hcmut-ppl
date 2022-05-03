import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_444(self):
        """Simple program: int main() {} """
        input = """
                         Class C{
                             e(){
                                 Var a:Int = 1;
                                 Var b:Int = 1;
                                 If (True){
                                     Var a:Int = 2;
                                 }
                                 Elseif(True){
                                     Var a:Int = 2;
                                 }
                                 Else{
                                     Var a:Int = 2;
                                 }
                                 Var c:Int = 2 ;
                             }
                         }
                         Class DADADAD{}
                         Class XYZ{
                            Var x :Int;
                            Var x: Int;
                         }"""
        expect = "Redeclared Variable: b"
        self.assertTrue(TestChecker.test(input, expect, 444))