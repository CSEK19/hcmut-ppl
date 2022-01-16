import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_lowercase_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",101))
    def test_lower_upper_id(self):
        self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",102))
    '''
    def test_mixed_id(self):
        self.assertTrue(TestLexer.test("aAsVN3","aAsVN,3,<EOF>",103))
    def test_integer(self):
        """test integers"""
        self.assertTrue(TestLexer.test("123a123","123,a,123,<EOF>",104))'''
    def test_BK_2(self):
        self.assertTrue(TestLexer.test("Break","Break,<EOF>",105))
    def test_BK_3(self):
        self.assertTrue(TestLexer.test("ab?svn","ab,Error Token ?",106))
    def test_BK_4(self):
        self.assertTrue(TestLexer.test("Return x;","Return,x,;,<EOF>",107))
    def test_BK_5(self):
        self.assertTrue(TestLexer.test(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",108))
    def test_BK_6(self):
        self.assertTrue(TestLexer.test(""" "abc def  ""","""Unclosed String: abc def  """,109))
