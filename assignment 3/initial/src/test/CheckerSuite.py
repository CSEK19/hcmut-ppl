import unittest
from TestUtils import TestChecker
from AST import *

class CheckerSuite(unittest.TestCase):
    def test_400(self):
        input = """
        Class A{foo(){}}
        ClassB:A{foo(x: Int){}}
        Class Program{$main(){}}
        """
        expect = "Redeclared Attribute: a"
        self.assertTrue(TestChecker.test(input,expect,400))
