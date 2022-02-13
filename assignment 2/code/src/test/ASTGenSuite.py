import unittest
from TestUtils import TestAST
from AST import *

class ASTGenSuite(unittest.TestCase):
   def test_300(self):
        input = """
          Class A{
              foo(){
                If(1){}
                Elseif(2){}
              }
          }
          """
        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(foo),Instance,[],Block([],[If(IntLit(1),Block([],[]),If(IntLit(2),Block([],[])))]))])])'
        self.assertTrue(TestAST.test(input,expect,300))


