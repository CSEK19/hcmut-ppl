import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_201(self):
        """Simple program: int main() {} """
        input = """Class main{}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_202(self):
        """More complex program"""
        input = """Class Rectangle: Shape {
        getArea() {
        Return self.length * self.width;
    }
}"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_203(self):
        """More complex program"""
        input = """Var a: Array[Array[Int,5],5];"""
        expect = "Error on line 1 col 0: Var"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_204(self):
        """More complex program"""
        input = """1 + 1 + a.foo()"""
        expect = "Error on line 1 col 0: 1"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_205(self):
        """More complex program"""
        input = """
    Class Shape {
        $getNumOfShape( {
            Return self.length * self.width;
        }
    }
"""
        expect = "Error on line 3 col 24: {"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_206(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            a[b[1]][c][foo()] = 1;
        }
        Var e,f : Int = 1 + 1, 1 - 2;
    }
"""
        expect = "Error on line 4 col 26: ("
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_207(self):
        """More complex program"""
        input = """
Class Shape2 {
    $getNumOfShape() {
        If (a == (1+1) ){
            Var b,c:Boolean = True, False;
        }
        Foreach (i In 1 .. 100 By 2) {
             Var a:Boolean = True;
        }
    }
}
"""
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_208(self):
        """More complex program"""
        input = """
    Class Shape {
        sum(a,b:Int; c,d:Float){}
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_209(self):
        """More complex program"""
        input = """
    Class Shape {
        Var a :Array[Array[Int,2],2] = Array(Array(1,1),Array(1,1));
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_210(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            Var a: Boolean = !!True;
        }
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 210))

    def test_211(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            foo2(1+1,"a"+."b","a"==."b");
        }
    }
    """
        expect = "Error on line 4 col 16: ("
        self.assertTrue(TestParser.test(input, expect, 211))

    def test_212(self):
        """More complex program"""
        input = """
    Class Shape {
        Val $numOfShape: Int = 0;
        Val immutableAttribute: Int = 0;
        Var length, width: Int;
        $getNumOfShape() {
            Return $numOfShape;
        }
    }
    Class Rectangle: Shape {
        getArea() {
            Return self.length * self.width;
        }
    }
    Class Program {
        main() {
            Out.printInt(Shape::$numOfShape);
        }
    }
    """
        expect = "Error on line 7 col 19: $numOfShape"
        self.assertTrue(TestParser.test(input, expect, 212))

    def test_213(self):
        """More complex program"""
        input = """
    Class Shape {
        Constructor(width, height : Int; name:String){
            Self.Area=Self.width*Self.height;
            Self.name="shape"+.name;
        } 
        Destructor(){} 
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 213))

    def test_214(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            a=1------1+1--1;
        } 
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 214))

    def test_215(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            a=New X().Y();
        } 
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 215))

    def test_216(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            a();
        } 
    }
    """
        expect = "Error on line 4 col 13: ("
        self.assertTrue(TestParser.test(input, expect, 216))

    def test_217(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            Var a();
        } 
    }
    """
        expect = "Error on line 4 col 17: ("
        self.assertTrue(TestParser.test(input, expect, 217))

    def test_218(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            Var r, s: Int;
            r = 2.0;
            Var a, b: Array[Int, 5];
            s = r * r * Self.myPI;
            a[0] = s;
        } 
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_218(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            a.b();
        } 
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 218))

    def test_219(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            a=b.c.d.e;
        } 
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 219))

    def test_220(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            Foreach (i In (1+2) .. (100*2-3) By (16-14)) {
                Out.printInt(i);
            }
        } 
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 220))

    def test_221(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            ;
        } 
    }
    """
        expect = "Error on line 4 col 12: ;"
        self.assertTrue(TestParser.test(input, expect, 221))

    def test_222(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            Foreach (i In a[1] .. foo() By _123()) {}
        } 
    }
    """
        expect = "Error on line 4 col 37: ("
        self.assertTrue(TestParser.test(input, expect, 222))

    def test_223(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            a = !!!!!!!!!!!!True;
            b = ------------5;
        } 
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 223))

    def test_224(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            a = !!!!!!!!!!!!True;
            b = ------------5;
            c=d.d.d.d.d.d.d.d;
            e=f[1][1][1][1];
        } 
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 224))

    def test_225(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            a = (b==c) == True;
        } 
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 225))

    def test_226(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            a = b == c  == True;
        } 
    }
    """
        expect = "Error on line 4 col 24: =="
        self.assertTrue(TestParser.test(input, expect, 226))

    def test_227(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            a = (b < c)  == True;
        } 
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 227))

    def test_228(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            a = (b < c) < True;
        } 
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_228(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            a = b < c < True;
        } 
    }
    """
        expect = "Error on line 4 col 22: <"
        self.assertTrue(TestParser.test(input, expect, 228))

    def test_229(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            a = ("a"+."b")+."b";
            c = ("a"==."a")==True;
        } 
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 229))

    def test_230(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            a = "a"+."b"+."b";
        } 
    }
    """
        expect = "Error on line 4 col 24: +."
        self.assertTrue(TestParser.test(input, expect, 230))

    def test_231(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            a = "a"==."b"==."b";
        } 
    }
    """
        expect = "Error on line 4 col 25: ==."
        self.assertTrue(TestParser.test(input, expect, 231))

    def test_232(self):
        """More complex program"""
        input = """
    Class Shape:a:b{}
    """
        expect = "Error on line 2 col 17: :"
        self.assertTrue(TestParser.test(input, expect, 232))

    def test_233(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            a::$b=2;
            a::$e();
            a::$c::$d=2;
        } 
    }
    """
        expect = "Error on line 6 col 17: ::"
        self.assertTrue(TestParser.test(input, expect, 233))

    def test_234(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            a::$b=2;
            a::$e();
            a::$c()::$d=2;
        } 
    }
    """
        expect = "Error on line 6 col 19: ::"
        self.assertTrue(TestParser.test(input, expect, 234))

    def test_235(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
        a+=1;
        } 
    }
    """
        expect = "Error on line 4 col 9: +"
        self.assertTrue(TestParser.test(input, expect, 235))

    def test_236(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
        a=+1;
        } 
    }
    """
        expect = "Error on line 4 col 10: +"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_237(self):
        input = """
            Class Shape {
                foo(){
                a=-1+1;
                b=1+-1;
                } 
            }
            """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 236))

    def test_238(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
            a=-1+1;
            b=1+-1--1+-1---1;
        } 
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 238))

    def test_239(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
        b=1+-1--1+-1-+-1;
        } 
    }
    """
        expect = "Error on line 4 col 21: +"
        self.assertTrue(TestParser.test(input, expect, 239))

    def test_240(self):
        """More complex program"""
        input = """
    Class Shape {
        foo(){
        Var a :Int = $1-----5;
        } 
    }
    """
        expect = "Error on line 4 col 21: $1"
        self.assertTrue(TestParser.test(input, expect, 240))

    def test_241(self):
        input = """
                Class Shape{
                    foo(){
                        a = New X().Y();
                        Var a: Array[Int, 0];
                    }
                }

            """
        output = """Error on line 5 col 42: 0"""
        self.assertTrue(TestParser.test(input, output, 241))

    def test_242(self):
        input = """
                Class Shape{
                    foo(){
                        b::$f=1;
                    }
                    a = 1;
                }

            """
        output = """Error on line 6 col 22: ="""
        self.assertTrue(TestParser.test(input, output, 242))

    def test_243(self):
        input = """
                Class Shape{
                    foo(){
                        a=1;
                    }
                    Foreach (x In 1 .. 100 by 2){}
                }

            """
        output = """Error on line 6 col 20: Foreach"""
        self.assertTrue(TestParser.test(input, output, 243))

    def test_244(self):
        input = """
                Class Shape{
                    foo(){}
                    Class LamTestMetVaiLoz{}
                }

            """
        output = """Error on line 4 col 20: Class"""
        self.assertTrue(TestParser.test(input, output, 244))

    def test_245(self):
        input = """
                Class Shape{
                    foo(){
                        Class LamTestMetVaiLoz{}
                    }
                }

            """
        output = """Error on line 4 col 24: Class"""
        self.assertTrue(TestParser.test(input, output, 245))

    def test_246(self):
        input = """
                Class Shape{
                    foo(){
                        Var a: Array[Int, 01];
                        Var a: Array[Int, 0x1];
                        Var a: Array[Int, 0X1];
                        Var a: Array[Int, 0b1];
                        Var a: Array[Int, 0B1];
                        Var a: Array[Int, 1];
                        Var a: Array[Int, 00];
                    }
                }

            """
        output = """Error on line 10 col 42: 00"""
        self.assertTrue(TestParser.test(input, output, 246))

    def test_247(self):
        input = """
                Class Shape{
                    foo(){
                        Var a: Array[Int, 0b0];
                    }
                }

            """
        output = """Error on line 4 col 42: 0b0"""
        self.assertTrue(TestParser.test(input, output, 247))

    def test_248(self):
        input = """
                Class Shape{
                    foo(){
                        Var a: Array[Int, 0x0];
                    }
                }

            """
        output = """Error on line 4 col 42: 0x0"""
        self.assertTrue(TestParser.test(input, output, 248))

    def test_249(self):
        input = """
                Class Shape{
                    foo(){
                        Var a: Array[Int, 1_23.456e+7];
                    }
                }

            """
        output = """Error on line 4 col 42: 123.456e+7"""
        self.assertTrue(TestParser.test(input, output, 249))

    def test_250(self):
        input = """
                Class Shape{
                    foo(){
                        Var a: Array[Int, b::$c.foo()];
                    }
                }

            """
        output = """Error on line 4 col 42: b"""
        self.assertTrue(TestParser.test(input, output, 250))

    def test_251(self):
        input = """
                Class Shape{
                    Var a,b:Int=5,6,7;
                }

            """
        output = """Error on line 3 col 35: ,"""
        self.assertTrue(TestParser.test(input, output, 251))

    def test_252(self):
        input = """
                Class Shape{
                    Var a,b,c:Int=5,6;
                }

            """
        output = """Error on line 3 col 37: ;"""
        self.assertTrue(TestParser.test(input, output, 252))

    def test_253(self):
        input = """
                Class Shape{
                    Var a,b:Int=5,6;
                }

            """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 253))

    def test_254(self):
        input = """
                Class Shape{
                    Var $a,b:Int=5,6;
                    foo(){
                        Var $c,d:Int=5,6;
                    }
                }

            """
        output = """Error on line 5 col 28: $c"""
        self.assertTrue(TestParser.test(input, output, 254))

    def test_255(self):
        input = """
                Class Shape{
                    foo(){
                        Return a::$TAloz;
                    }
                }

            """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 255))

    def test_256(self):
        input = """
                Class Shape{
                    Return a::$TAloz*a::$TAloz---------a::$TAloz;
                }

            """
        output = """Error on line 3 col 20: Return"""
        self.assertTrue(TestParser.test(input, output, 256))

    def test_257(self):
        input = """
                Class Shape{
                    foo(){
                        Return a::$TAloz*a::$TAloz---------a::$TAloz;
                    }
                }
            """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 257))

    def test_258(self):
        input = """
                Class Shape{
                    foo(){
                        Foreach (x In 1+1 .. 100+100 By a.foo()){}
                    }
                }
            """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 258))

    def test_259(self):
        input = """
                Class Shape{
                    foo(){
                        Foreach (x In a::$b() .. a.c.c.c By a::$foo){
                            Class Shape{}
                        }
                    }
                }
            """
        output = """Error on line 5 col 28: Class"""
        self.assertTrue(TestParser.test(input, output, 259))

    def test_260(self):
        input = """
                Class Shape{
                    foo(){
                        Foreach (x In a::$b() .. a.c.c.c By a::$foo){
                            Var $a:Int;
                        }
                }
                """
        output = """Error on line 5 col 32: $a"""
        self.assertTrue(TestParser.test(input, output, 260))

    def test_261(self):
        input = """
                Class Shape{
                    foo(){
                        Foreach (x In a::$b() .. a.c.c.c By a::$foo){
                            Foreach (x In a::$b() .. a.c.c.c By a::$foo){}
                        }
                    }
                }   
                """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 261))

    def test_262(self):
        input = """
                Class Shape{
                    foo(){
                        a[b[c[d[e[f::$g]]]]][h::$i][j.k()][Lzzzzz::$m()]=0;
                    }
                }   
                """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 262))

    def test_263(self):
        input = """
                Class Shape{
                    foo(){
                        If ( a == -1--1){
                            If(b==True){}
                        }
                    }
                }   
                """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 263))

    def test_264(self):
        input = """
                Class Shape{
                    foo(){
                        If ( a == -1--1){
                            If(b == "c"+."c"){}
                        }
                    }
                }   
                """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 264))

    def test_265(self):
        input = """
                Class Shape{
                    foo(){
                        If ( a == -1--1){
                            If(b == "c"+."c"){}
                            Elseif( a == b ==. c){}
                        }
                    }
                }   
                """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 265))

    def test_266(self):
        input = """
                Class Shape{
                    foo(){
                        If ( a == -1--1){
                            If(b == "c"+."c"){}
                            Elseif( a == b ==. c){}
                            Else(1=2){}
                        }
                    }
                } 
                """
        output = """Error on line 7 col 32: ("""
        self.assertTrue(TestParser.test(input, output, 266))

    def test_267(self):
        input = """
                Class Shape{
                    foo(){
                        If ( a == -1--1){
                            Foreach(x In 1 .. 100 By 2){
                                If ( a == -1--1){
                                    Foreach(x In 1 .. 100 By 2){

                                    }
                                }
                            }
                        }
                    }
                }   
                """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 267))

    def test_268(self):
        input = """
                Class Shape{
                Var $a: Int;
                Var b:int;
                Val c:Int;
                Val $d:Int;
                }   
                """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 268))

    def test_269(self):
        input = """
                Class Shape{
                    $a(){
                        Break;
                        Continue;
                        Return;
                    }
                }   
                """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 269))

    def test_270(self):
        input = """
                Class Shape{
                    Break;
                }   
                """
        output = """Error on line 3 col 20: Break"""
        self.assertTrue(TestParser.test(input, output, 270))

    def test_271(self):
        input = """
                Class Shape{
                    Continue;
                }   
                """
        output = """Error on line 3 col 20: Continue"""
        self.assertTrue(TestParser.test(input, output, 271))
    def test_272(self):
        input = """
                Class Shape{
                    foo(){
                        True=a;
                    }
                }   
                """
        output = """Error on line 4 col 24: True"""
        self.assertTrue(TestParser.test(input, output, 272))
    def test_273(self):
        input = """
                Class Shape{
                    foo(){
                        a=b==c==d;
                    }
                }   
                """
        output = """Error on line 4 col 30: =="""
        self.assertTrue(TestParser.test(input, output, 273))
    def test_274(self):
        input = """
                Class Shape{
                    foo(){
                        a=b<=c>=d;
                    }
                }   
                """
        output = """Error on line 4 col 30: >="""
        self.assertTrue(TestParser.test(input, output, 274))
    def test_275(self):
        input = """
                Class Shape{
                    foo(){
                        a=b==c<d;
                    }
                }   
                """
        output = """Error on line 4 col 30: <"""
        self.assertTrue(TestParser.test(input, output, 275))
    def test_276(self):
        input = """
                Class Shape{
                    Foreach(i In 1 . . 100 by 2 ){}
                }   
                """
        output = """Error on line 3 col 20: Foreach"""
        self.assertTrue(TestParser.test(input, output, 276))
    def test_277(self):
        input = """
                Class Shape{
                    Var a: Array[Array[Array[1,1_12],1],1];
                }   
                """
        output = """Error on line 3 col 45: 1"""
        self.assertTrue(TestParser.test(input, output, 277))
    def test_278(self):
        input = """
                Class Shape{
                    Var a: Array[Array[Array[d,1_12],1],1];
                }   
                """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 278))
    def test_279(self):
        input = """
                Class Shape{
                    Var a: Array[Array[Array[d,_1_12],1],1];
                }   
                """
        output = """Error on line 3 col 47: _1_12"""
        self.assertTrue(TestParser.test(input, output, 279))
    def test_280(self):
        input = """
                Class Shape{
                    Var a: Array[b,Array[c,Array[d,1]]];
                }   
                """
        output = """Error on line 3 col 35: Array"""
        self.assertTrue(TestParser.test(input, output, 280))

    def test_281(self):
        input = '''Class _:r{}Class _:R{Var _,__0,j_:Array[Array[Array[Float,04],2],0B1];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_282(self):
        input = '''Class d:q{}Class G{}Class _{}Class _:G{}Class _{Destructor(){} }Class N8_40IWV:B__{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_283(self):
        input = '''Class c:_{Destructor(){} }Class __:y_161{Destructor(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_284(self):
        input = '''Class a:tW_{$_8(){}Var $_:Float;_(){} }Class D:_{}Class _3M:o_8__l{Constructor(_:W8){Break;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_285(self):
        input = '''Class ATE2:__0{}Class A5:_u1gP{}Class _{Val _,$5_,$__R_3v,Q,_,$_H,$9zV_4s_,J_,A6,_:String;}Class __:_v42{}Class F{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_286(self):
        input = '''Class __:___b_{}Class e{Var $H6:Float;Val $e_,$_9_:Boolean;Var $_,G,$0143:__1W_;}Class s:_{t(l8:Array[Array[Array[Int,0114],4],0X45];P_:Boolean){} }Class U{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_287(self):
        input = '''Class _60{}Class __:_{}Class _4B:_{}Class z:jA{}Class _1{}Class x{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_288(self):
        input = '''Class _{$2_1(){} }Class _t:_0{}Class A_:gO6{$S(_:_;X,_3,_,_:Int){Return;Return!!!!!!New _().X61();{}Continue;} }Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 288))

    def test_289(self):
        input = '''Class _{Constructor(){}Constructor(_O_,b_,i:_;LB,H,_j,___:String;_x10__,O1:Float;X,H:_T;T:Array[Array[Array[Boolean,0b1_0],0126],06]){} }Class q95{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 289))

    def test_290(self):
        input = '''Class _:N_L{Destructor(){Break;}y8(o_d_8,_,w,_1:J6){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 290))

    def test_291(self):
        input = '''Class _{}Class l__5{Val $_:Float;}Class F6_{Val $P_X_,$_,$91:String;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 291))

    def test_292(self):
        input = '''Class _{Constructor(U0d,W2,__mMlKE,_Jl11:String;b_C,E:String){} }Class _:Pm4{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 292))

    def test_293(self):
        input = '''Class _{}Class ot{$_(){} }Class g__1mU{Constructor(){Var __12:String;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 293))

    def test_294(self):
        input = '''Class b{}Class _445{Constructor(_:String;K:Array[String,0b1];r_4N:k3h;_,Y_48g__:_;_,_:e_;b:B_;O:_3){}Var $7_:Array[Array[Array[Boolean,03],50],0XE_62];}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 294))

    def test_295(self):
        input = '''Class _:__uDj{Constructor(_5:Array[Boolean,0b1001110];_,_,_v,_,T:Array[Array[Float,0X8_9_D],070];_,_9:Array[Int,0B100101];v,nu:Array[Boolean,05_2]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 295))

    def test_296(self):
        input = '''Class _:y{}Class s:S{Val $3,_,_x_c3_93k,C1:V;}Class _:n7{}Class __1:_{}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 296))

    def test_297(self):
        input = '''Class dp:_{Constructor(_8v_,M:Int;_,_N_:Array[Array[Int,0x50],45];B4cl38,_:_8){}Destructor(){}$0(T:Float){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 297))

    def test_298(self):
        input = '''Class p:_o{Constructor(u,_90,V:J__;_4:c){}Constructor(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 298))

    def test_299(self):
        input = '''Class Lzzzzz{Destructor(){Return;_9::$g3k.m();} }Class classA1provip123:z{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_300(self):
        input = '''
Class Lzzzzz{Destructor(){Return;_9::$g3k.m();} }Class classA1provip123:z{}
        Class a{
            foo(){
                a = "Tao noi cho lam cai test case nay met vai loz luon";
            }
        }
        foo(){
                a = "26 am roi, vay ma chang duoc 
                     Sam mua do tet
                     ma chi co
                     sap mat lam test
                     :<<"
            }'''
        expect = 'Error on line 8 col 8: foo'
        self.assertTrue(TestParser.test(input, expect, 300))





