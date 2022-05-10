import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):

    def test_414(self):
        input = """
              Class Program {
                 Var a: Int = 5;
                 Var b: Int = a + 1;
                 $main(){}
              }
          """
        expect = "Undeclared Identifier: a"
        self.assertTrue(TestChecker.test(input, expect, 414))