import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
      
    def test_101(self):
        """test identifiers"""
        self.assertTrue(TestLexer.test("abc","abc,<EOF>",101))
    def test_102(self):
        self.assertTrue(TestLexer.test("aCBbdc","aCBbdc,<EOF>",102))
    def test_103(self):
        self.assertTrue(TestLexer.test("Break","Break,<EOF>",103))
    def test_BK_3(self):
        self.assertTrue(TestLexer.test("ab?svn","ab,Error Token ?",104))
    def test_105(self):
        self.assertTrue(TestLexer.test("Return x;","Return,x,;,<EOF>",105))
    def test_106(self):
        self.assertTrue(TestLexer.test(""" "abc\\h def"  ""","""Illegal Escape In String: abc\\h""",106))
    def test_107(self):
        self.assertTrue(TestLexer.test(""" "abc def  ""","""Unclosed String: abc def  """,107))
    def test_108(self):
        self.assertTrue(TestLexer.test(""" "abc\\\\h def"  """,""""abc\\\\h def",<EOF>""",108))
    def test_109(self):
        self.assertTrue(TestLexer.test(""" "abc\\a def"  ""","""Illegal Escape In String: abc\\a""",109))
    def test_110(self):
        self.assertTrue(TestLexer.test(""" "abc\\' def"  """,""""abc\\' def",<EOF>""",110))
    def test_111(self):
        self.assertTrue(TestLexer.test(""" 12345  ""","""12345,<EOF>""",111))
    def test_112(self):
        self.assertTrue(TestLexer.test(""" "abc\\\\ def"  """,""""abc\\\\ def",<EOF>""",112))
    def test_113(self):
        self.assertTrue(TestLexer.test(""" "abc\\\\h def"  """,""""abc\\\\h def",<EOF>""",113))
    def test_114(self):
        self.assertTrue(TestLexer.test(""" 1.23e-15 ""","""1.23e-15,<EOF>""",114))
    def test_115(self):
        self.assertTrue(TestLexer.test(""" 1.23e15 ""","""1.23e15,<EOF>""",115))
    def test_115(self):
        self.assertTrue(TestLexer.test("""1_234_567""","""1234567,<EOF>""",115))
    def test_116(self):
        self.assertTrue(TestLexer.test("""1_234_567.123""","""1234567.123,<EOF>""",116))
    def test_117(self):
        self.assertTrue(TestLexer.test("""7E-10""","""7E-10,<EOF>""",117))
    def test_118(self):
        self.assertTrue(TestLexer.test("""7E-10""","""7E-10,<EOF>""",118))
    def test_119(self):
        self.assertTrue(TestLexer.test("""0b11111111""","""0b11111111,<EOF>""",119))
    def test_120(self):
        self.assertTrue(TestLexer.test(""" "\\b \\f \\r \\n \\t \\' \\\\ '" " """,""""\\b \\f \\r \\n \\t \\' \\\\ '" ",<EOF>""",120))
    def test_121(self):
        self.assertTrue(TestLexer.test(""" "This is a string containing tab \\t" """,""""This is a string containing tab \\t",<EOF>""",121))

    def test_122(self):
        self.assertTrue(TestLexer.test(""" "He asked me:'"Where is John?'"" """, """"He asked me:'"Where is John?'"",<EOF>""",122))

    def test_123(self):
        self.assertTrue(TestLexer.test(""" "abc \\n def" """, """"abc \\n def",<EOF>""", 123))

    def test_124(self):
        self.assertTrue(TestLexer.test("1323_a_321_1", "1323,_a_321_1,<EOF>", 124))

    def test_125(self):
        self.assertTrue(TestLexer.test("1_234.567_789e246_357", "1234.567,_789e246_357,<EOF>", 125))

    def test_126(self):
        self.assertTrue(TestLexer.test("0x13A2D_321_D_1", "0x13A2D321D1,<EOF>", 126))

    def test_127(self):
        self.assertTrue(TestLexer.test("0X12_AB_Aabc", "0X12ABA,abc,<EOF>", 127))

    def test_128(self):
        self.assertTrue(TestLexer.test("0X12_AB_Aabc123", "0X12ABA,abc123,<EOF>", 128))

    def test_129(self):
        self.assertTrue(TestLexer.test("0x12_AB_Aabc123", "0x12ABA,abc123,<EOF>", 129))

    def test_130(self):
        self.assertTrue(TestLexer.test("071010788", "0710107,88,<EOF>", 130))



