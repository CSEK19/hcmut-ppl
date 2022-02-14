import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):

    def test_101(self):
        self.assertTrue(TestLexer.test("Val","Val,<EOF>",101))

    def test_102(self):
        self.assertTrue(TestLexer.test(""" "TrueFalseTrueFalseTrueFalseTrueFalse' " """, """TrueFalseTrueFalseTrueFalseTrueFalse' ,<EOF>""", 102))

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
        self.assertTrue(TestLexer.test(""" 0.123_3 """, """0.123,_3,<EOF>""", 114))

    def test_115(self):
        self.assertTrue(TestLexer.test(""" .3213 """, """.,3213,<EOF>""", 115))

    def test_116(self):
        self.assertTrue(TestLexer.test(""" "## This is a comment ##" """, """## This is a comment ##,<EOF>""", 116))

    def test_117(self):
        self.assertTrue(TestLexer.test(""" "TrueFalseTrueFalseTrueFalseTrueFalse'" """, """Unclosed String: TrueFalseTrueFalseTrueFalseTrueFalse'" """, 117))

    def test_118(self):
        self.assertTrue(TestLexer.test(""" 0 00 0x0 0X0 0b0 0B0 """, """0,00,0x0,0X0,0b0,0B0,<EOF>""", 118))

    def test_119(self):
        self.assertTrue(TestLexer.test(""" 0000x00X00b00B0 """, """00,00,x00X00b00B0,<EOF>""", 119))

    def test_120(self):
        self.assertTrue(TestLexer.test(""" 0000x00X00b00B0 """, """00,00,x00X00b00B0,<EOF>""", 120))

    def test_121(self):
        self.assertTrue(TestLexer.test(""" 0000x00X00b00B0 """, """00,00,x00X00b00B0,<EOF>""", 121))

    def test_122(self):
        self.assertTrue(TestLexer.test(""" 0e123 .0e123 """, """0e123,.0e123,<EOF>""", 122))

    def test_123(self):
        self.assertTrue(TestLexer.test(""" 0b0e123 """, """0b0,e123,<EOF>""", 123))

    def test_124(self):
        self.assertTrue(TestLexer.test(""" 128397128937_32112312_31242121094582149012_312123123__12389123721 """, """1283971289373211231231242121094582149012312123123,__12389123721,<EOF>""", 124))

    def test_125(self):
        self.assertTrue(TestLexer.test(""" 4587.E00000 6754.e-00000 4530.0000e3 """, """4587.E00000,6754.e-00000,4530.0000e3,<EOF>""", 125))

    def test_126(self):
        self.assertTrue(TestLexer.test(""" 456789.0e0 0.0e0 12345.E-0 """, """456789.0e0,0.0e0,12345.E-0,<EOF>""", 126))

    def test_127(self):
        self.assertTrue(TestLexer.test(""" _123412 __218374 """, """_123412,__218374,<EOF>""", 127))

    def test_128(self):
        self.assertTrue(TestLexer.test(""" 12341234_ 987435__ """, """12341234,_,987435,__,<EOF>""", 128))

    def test_129(self):
        self.assertTrue(TestLexer.test(""" 0_x123128721 """, """0,_x123128721,<EOF>""", 129))

    def test_130(self):
        self.assertTrue(TestLexer.test(""" 1___2341 1__2_34 """, """1,___2341,1,__2_34,<EOF>""", 130))

    def test_131(self):
        self.assertTrue(TestLexer.test(""" -123456789 """, """-,123456789,<EOF>""", 131))

    def test_132(self):
        self.assertTrue(TestLexer.test(""" -132_3_3321321312232E1_32412412123_1312312312 """, """-,13233321321312232E1,_32412412123_1312312312,<EOF>""", 132))

    def test_133(self):
        self.assertTrue(TestLexer.test(""" 312412_353252E1 _32312E-1123123;412312e-24312124 """, """312412353252E1,_32312E,-,1123123,;,412312e-24312124,<EOF>""", 133))

    def test_134(self):
        self.assertTrue(TestLexer.test(""" 23124121E-2-33124124,5512213412 """, """23124121E-2,-,33124124,,,5512213412,<EOF>""", 134))

    def test_135(self):
        self.assertTrue(TestLexer.test(""" 151241.321312312312323F3234124122 """, """151241.321312312312323,F3234124122,<EOF>""", 135))

    def test_136(self):
        self.assertTrue(TestLexer.test(""" 123121.d132124124122 """, """123121.,d132124124122,<EOF>""", 136))

    def test_137(self):
        self.assertTrue(TestLexer.test(""" 05121_324123.e-41_2233_34 """, """05121324123,.e-41,_2233_34,<EOF>""", 137))

    def test_138(self):
        self.assertTrue(TestLexer.test(""" .23412abdcesdf """, """.,23412,abdcesdf,<EOF>""", 138))

    def test_139(self):
        self.assertTrue(TestLexer.test(""" 0x12AF34e12GHJKLMN """, """0x12AF34,e12GHJKLMN,<EOF>""", 139))

    def test_140(self):
        self.assertTrue(TestLexer.test(""" 0x0123123124124e1312412 """, """0x0,123123124124e1312412,<EOF>""", 140))

    def test_141(self):
        self.assertTrue(TestLexer.test(""" 00412e122 """, """00,412e122,<EOF>""", 141))

    def test_142(self):
        self.assertTrue(TestLexer.test(""" 0127BCA334e102 """, """0127,BCA334e102,<EOF>""", 142))

    def test_143(self):
        self.assertTrue(TestLexer.test(""" 0x8902F3DG_345,332412e-12 """, """0x8902F3D,G_345,,,332412e-12,<EOF>""", 143))

    def test_144(self):
        self.assertTrue(TestLexer.test(""" 0x0123123124124e1312412 """, """0x0,123123124124e1312412,<EOF>""", 144))

    def test_145(self):
        self.assertTrue(TestLexer.test(""" falsefalseTruetrueTruefalsefalseFalse FalseTrue True """, """falsefalseTruetrueTruefalsefalseFalse,FalseTrue,True,<EOF>""", 145))

    def test_146(self):
        self.assertTrue(TestLexer.test(""" Array(1, 5, 20, -1) """, """Array,(,1,,,5,,,20,,,-,1,),<EOF>""", 146))

    def test_147(self):
        self.assertTrue(TestLexer.test(""" Array(Array(1,2), Array(1,2)) """, """Array,(,Array,(,1,,,2,),,,Array,(,1,,,2,),),<EOF>""", 147))

    def test_148(self):
        self.assertTrue(TestLexer.test(""" Array("Hello", "World") """, """Array,(,Hello,,,World,),<EOF>""", 148))

    def test_149(self):
        self.assertTrue(TestLexer.test(""" abb = 13122!||!231233 """, """abb,=,13122,!,||,!,231233,<EOF>""", 149))

    def test_150(self):
        self.assertTrue(TestLexer.test(""" dddb != 4124214||&&&&dawdqaw - 35234! """, """dddb,!=,4124214,||,&&,&&,dawdqaw,-,35234,!,<EOF>""", 150))

    def test_151(self):
        self.assertTrue(TestLexer.test(""" Array("abc \\h") """, """Array,(,Illegal Escape In String: abc \h""", 151))

    def test_152(self):
        self.assertTrue(TestLexer.test(""" "abch def" """, """abch def,<EOF>""", 152))

    def test_153(self):
        self.assertTrue(TestLexer.test(""" "PPL \'\" """, """Unclosed String: PPL '" """, 153))

    def test_154(self):
        self.assertTrue(TestLexer.test(""" "ppl \'\" """, """Unclosed String: ppl '" """, 154))

    def test_155(self):
        self.assertTrue(TestLexer.test(""" New line\nin string """, """New,line,in,string,<EOF>""", 155))

    def test_156(self):
        self.assertTrue(TestLexer.test(""" "He asked me: '"Where is John? '"" """, """He asked me: '"Where is John? '",<EOF>""", 156))

    def test_157(self):
        self.assertTrue(TestLexer.test(""" "\"String with ##Comment## inside\"" """, """,String,with,inside,,<EOF>""", 157))

    def test_158(self):
        self.assertTrue(TestLexer.test(""" "\"String with single quote \'this is good\'\"" """, """,String,with,single,quote,Error Token '""", 158))

    def test_159(self):
        self.assertTrue(TestLexer.test(""" "'dadada\\dadadaad" """, """Illegal Escape In String: 'dadada\d""", 159))

    def test_160(self):
        self.assertTrue(TestLexer.test(""" abc"adadadvc \\m abv "abc """, """abc,Illegal Escape In String: adadadvc \m""", 160))

    def test_161(self):
        self.assertTrue(TestLexer.test(""" "Hello \' there"  """, """Hello ' there,<EOF>""", 161))

    def test_162(self):
        self.assertTrue(TestLexer.test(""" "++.--.* *.\\\\.<<.>>.<=<=.>=>=.===/="  """, """++.--.* *.\\\\.<<.>>.<=<=.>=>=.===/=,<EOF>""", 162))

    def test_163(self):
        self.assertTrue(TestLexer.test(""" 1+2+3+4  """, """1,+,2,+,3,+,4,<EOF>""", 163))

    def test_164(self):
        self.assertTrue(TestLexer.test(""" (2*3)/(4/4)  """, """(,2,*,3,),/,(,4,/,4,),<EOF>""", 164))

    def test_165(self):
        self.assertTrue(TestLexer.test(""" x < 2 && x > 10  """, """x,<,2,&&,x,>,10,<EOF>""", 165))

    def test_166(self):
        self.assertTrue(TestLexer.test(""" (abc)(def)[123,abc](TRUE && False)  """, """(,abc,),(,def,),[,123,,,abc,],(,TRUE,&&,False,),<EOF>""", 166))

    def test_167(self):
        self.assertTrue(TestLexer.test(""" Class A(){Val a : Int = 1;}  """, """Class,A,(,),{,Val,a,:,Int,=,1,;,},<EOF>""", 167))

    def test_168(self):
        self.assertTrue(TestLexer.test(""" Var $A: Array[Int,10];  """, """Var,$A,:,Array,[,Int,,,10,],;,<EOF>""", 168))

    def test_169(self):
        self.assertTrue(TestLexer.test(""" $getNumOfShape() {Return a::$numOfShape;}  """, """$getNumOfShape,(,),{,Return,a,::,$numOfShape,;,},<EOF>""", 169))

    def test_170(self):
        self.assertTrue(TestLexer.test(""" Val My1stCons, My2ndCons: Int = 1 + 5, 2; """, """Val,My1stCons,,,My2ndCons,:,Int,=,1,+,5,,,2,;,<EOF>""", 170))

    def test_171(self):
        self.assertTrue(TestLexer.test(""" "abc\\h def"  """, """Illegal Escape In String: abc\h""", 171))

    def test_172(self):
        self.assertTrue(TestLexer.test(""" "abc\\a def"  """, """Illegal Escape In String: abc\\a""", 172))

    def test_173(self):
        self.assertTrue(TestLexer.test(""" \"abc\\\\ def\" \"  """, """abc\\\\ def,Unclosed String:   """, 173))

    def test_174(self):
        self.assertTrue(TestLexer.test(""" "\\b \\f \\r \\n \\t \\' \\\\ '" "  """, """\\b \\f \\r \\n \\t \\' \\\\ '" ,<EOF>""", 174))

    def test_175(self):
        self.assertTrue(TestLexer.test(""" "Hello World\\" """, """Illegal Escape In String: Hello World\\\"""", 175))

    def test_176(self):
        self.assertTrue(TestLexer.test(""" "HCMUT = Ho Chi Minh University of Technology"  """, """HCMUT = Ho Chi Minh University of Technology,<EOF>""", 176))

    def test_177(self):
        self.assertTrue(TestLexer.test(""" a.foo()  """, """a,.,foo,(,),<EOF>""", 177))

    def test_178(self):
        self.assertTrue(TestLexer.test(""" Foreach(1.. 100 By 2)  """, """Foreach,(,1.,.,100,By,2,),<EOF>""", 178))

    def test_179(self):
        self.assertTrue(TestLexer.test(""" Array("abc \\\\h")  """, """Array,(,abc \\\\h,),<EOF>""", 179))

    def test_180(self):
        self.assertTrue(TestLexer.test(""" ##Comment##  """, """<EOF>""", 180))

    def test_181(self):
        self.assertTrue(TestLexer.test(""" ##Comment## ## """, """Error Token #""", 181))

    def test_182(self):
        self.assertTrue(TestLexer.test(""" $123321 """, """$123321,<EOF>""", 182))

    def test_183(self):
        self.assertTrue(TestLexer.test(""" $ """, """Error Token $""", 183))

    def test_184(self):
        self.assertTrue(TestLexer.test(""" 03123124710131231241243120788xooox124123123 """, """031231247101312312412431207,88,xooox124123123,<EOF>""", 184))

    def test_185(self):
        self.assertTrue(TestLexer.test(""" 0_71__010_7__8_8 """, """0,_71__010_7__8_8,<EOF>""", 185))

    def test_186(self):
        self.assertTrue(TestLexer.test(""" 1+++++1---1***1 """, """1,+,+,+,+,+,1,-,-,-,1,*,*,*,1,<EOF>""", 186))

    def test_187(self):
        self.assertTrue(TestLexer.test(""" Var r, s: Int; """, """Var,r,,,s,:,Int,;,<EOF>""", 187))

    def test_188(self):
        self.assertTrue(TestLexer.test(""" r = 2.0; """, """r,=,2.0,;,<EOF>""", 188))

    def test_189(self):
        self.assertTrue(TestLexer.test(""" Var a, b: Array[Int, 5]; """, """Var,a,,,b,:,Array,[,Int,,,5,],;,<EOF>""", 189))

    def test_190(self):
        self.assertTrue(TestLexer.test(""" s = r * r * Self.myPI; """, """s,=,r,*,r,*,Self,.,myPI,;,<EOF>""", 190))

    def test_191(self):
        self.assertTrue(TestLexer.test(""" a[0] = s; """, """a,[,0,],=,s,;,<EOF>""", 191))

    def test_192(self):
        self.assertTrue(TestLexer.test(""" getArea() {Return Self.length * Self.width;} """, """getArea,(,),{,Return,Self,.,length,*,Self,.,width,;,},<EOF>""", 192))

    def test_193(self):
        self.assertTrue(TestLexer.test(""" Class Program {main() {Out.printInt(Shape::$numOfShape);}} """, """Class,Program,{,main,(,),{,Out,.,printInt,(,Shape,::,$numOfShape,),;,},},<EOF>""", 193))

    def test_194(self):
        self.assertTrue(TestLexer.test(""" H_C_M_U_T_NO_1 """, """H_C_M_U_T_NO_1,<EOF>""", 194))

    def test_195(self):
        self.assertTrue(TestLexer.test(""" "This is a normal string" """, """This is a normal string,<EOF>""", 195))

    def test_196(self):
        self.assertTrue(TestLexer.test(""" "Testcase 196" + 196 """, """Testcase 196,+,196,<EOF>""", 196))

    def test_197(self):
        self.assertTrue(TestLexer.test(""" "\\197" 197_e3120421-4.0123124 """, """Illegal Escape In String: \\1""", 197))

    def test_198(self):
        self.assertTrue(TestLexer.test(""" "'"198\\\\'"'" 198.e+312412412_31241240000  """, """Unclosed String: '"198\\\\'"'" 198.e+312412412_31241240000  """, 198))

    def test_199(self):
        self.assertTrue(TestLexer.test(""" "STRING" + "string" == 199 """, """STRING,+,string,==,199,<EOF>""", 199))

    def test_200(self):
        self.assertTrue(TestLexer.test(""" End_of_Lexer_test """, """End_of_Lexer_test,<EOF>""", 200))












