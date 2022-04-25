import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_simple_program(self):
        """Simple program: int main() {} """
        input = """int main() {}"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([],[]))]))
        self.assertTrue(TestAST.test(input,expect,300))

    def test_more_complex_program(self):
        """More complex program"""
        input = """int main () {
            putIntLn(4);
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([],[CallExpr(Id("putIntLn"),[IntLiteral(4)])]))]))
        self.assertTrue(TestAST.test(input,expect,301))
    
    def test_call_without_parameter(self):
        """More complex program"""
        input = """int main () {
            getIntLn();
        }"""
        expect = str(Program([FuncDecl(Id("main"),[],IntType(),Block([],[CallExpr(Id("getIntLn"),[])]))]))
        self.assertTrue(TestAST.test(input,expect,302))

    def test_303(self):
        input = """Class a{
                    b(){
                        Var a:int = 1;
                        {
                            Var a:int = 1;
                            Var b:int = 1;
                            Var b:int = 1;
                        }
                    }
                    }
        """
        expect = ""
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_304(self):
        input = """Class Program{
        main(){}
            Var myVar:String = "Hello World";
            Var myVar:Int;
        
        }
        """
        expect = ""
        self.assertTrue(TestAST.test(input, expect, 304))
   