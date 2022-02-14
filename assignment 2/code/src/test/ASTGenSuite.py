import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
    def test_300(self):
        input = """
 Class A:B{
            Var $a,b,c,$d : Int = 0,0b0,0x0,00;
        }
        """
        expect = 'Program([ClassDecl(Id(A),Id(B),[AttributeDecl(Static,VarDecl(Id($a),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(b),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(c),IntType,IntLit(0))),AttributeDecl(Static,VarDecl(Id($d),IntType,IntLit(0)))])])'
        self.assertTrue(TestAST.test(input, expect, 300))
