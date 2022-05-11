import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_423(self):
        input = """
                        Class C{
                            e(){
                                Return;
                            }
                        }"""
        expect = "Type Mismatch In Expression: BinaryOp(||,StringLit(abc),IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 423))