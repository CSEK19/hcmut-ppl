import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_101(self):
        self.assertTrue(TestLexer.test("Val","Val,<EOF>",101))

    def test_102(self):
        self.assertTrue(TestLexer.test(""" "TrueFalseTrueFalseTrueFalseTrueFalse' " """, """"TrueFalseTrueFalseTrueFalseTrueFalse' ",<EOF>""", 102))

    def test_103(self):
        self.assertTrue(TestLexer.test(""" "abc\\" """, """Illegal Escape In String: abc\\\"""", 103))

    def test_104(self):
        self.assertTrue(TestLexer.test("000_x123789", "00,0,_x123789,<EOF>", 104))

    def test_105(self):
        self.assertTrue(TestLexer.test("""He asked me: 'Where is John?'""", "He,asked,me,:,Error Token '", 105))

    def test_106(self):
        self.assertTrue(TestLexer.test("1_234.567_789e246_357", "1234.567,_789e246_357,<EOF>", 106))

    def test_107(self):
        self.assertTrue(TestLexer.test("Something \ ", """Something,Error Token \\""", 107))

    def test_108(self):
        self.assertTrue(TestLexer.test(""" abc" """, """abc,Unclosed String:  """, 108))

    def test_109(self):
        self.assertTrue(TestLexer.test(""" "'abc """, """Unclosed String: 'abc """, 109))

    def test_110(self):
        self.assertTrue(TestLexer.test(""" 1234.1e2000 0X1F """, """1234.1e2000,0X1F,<EOF>""", 110))

    def test_111(self):
        self.assertTrue(TestLexer.test(""" "abc\n\abc\" """, """Unclosed String: abc""", 111))

    def test_112(self):
        self.assertTrue(TestLexer.test(""" $123asd """, """$123asd,<EOF>""", 112))

    def test_113(self):
        self.assertTrue(TestLexer.test(""" 12_3_32__32_E1_323_1 """, """12332,__32_E1_323_1,<EOF>""", 113))

    def test_114(self):
        self.assertTrue(TestLexer.test(""" 0.123_3 """, """0,.,1233,<EOF>""", 114))

    def test_115(self):
        self.assertTrue(TestLexer.test(""" .3213 """, """.,3213,<EOF>""", 115))








