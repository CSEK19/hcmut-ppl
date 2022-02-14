import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_300(self):
        """Simple program: int main() {} """
        input = """
        Class Program {
        foo(){
            Foreach (i In 1 .. 100 By 2) { Out.printInt(i); }
        }
        }
        """
        expect = 'Program([ClassDecl(Id(Program),[])])'
        self.assertTrue(TestAST.test(input, expect, 300))
