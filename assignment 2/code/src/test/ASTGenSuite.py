import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):

    def test_316(self):
        """Simple program: int main() {} """
        input = """
       Class A {
           Var $b:Float=6.9;
       }
       """
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Static,VarDecl(Id($b),FloatType,FloatLit(6.9)))])])'
        self.assertTrue(TestAST.test(input, expect, 316))

