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
   