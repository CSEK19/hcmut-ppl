import unittest
from TestUtils import TestChecker
from AST import *


class CheckerSuite(unittest.TestCase):
    def test_429(self):
        input = """
                Class ProgramA {
                    main(){
                        Return 1;
                        Return 2;
                        Return 3;
                    }
                }
            """

        expect = "Type Mismatch In Statement: Return(IntLit(1))"
        self.assertTrue(TestChecker.test(input, expect, 429))

