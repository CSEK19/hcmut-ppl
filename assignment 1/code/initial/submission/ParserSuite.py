import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_201(self):
        input = """
        Class main{}
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 201))

    def test_202(self):
        input = """
        Class main{
        main(){}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 202))

    def test_203(self):
        input = """
        Class main{
        Val $a,b : Int = 0,0;
        main(){}
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 203))

    def test_204(self):
        input = """
        Class main{
        Val $a,b : Int = 0,0,1;
        main(){}
        }
        """
        expect = "Error on line 3 col 28: ,"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_205(self):
        input = """
        Class main{
        Val $a : Int = 0;
        main(){}

        """
        expect = "Error on line 6 col 8: <EOF>"
        self.assertTrue(TestParser.test(input, expect, 205))

    def test_206(self):
        input = """
        Class Something:Polygon{
        Val arr : Array[Proplayer, 4];
        foo(){
            Var a : Proplayer = New Student();
        }
        }
        """
        expect = "Error on line 3 col 24: Proplayer"
        self.assertTrue(TestParser.test(input, expect, 206))

    def test_207(self):
        input = """
        Class F{
            main(){
                Val a: Int = 0;
                Val b: Int = 0;
                Var c, d: Int;
            }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 207))

    def test_208(self):
        input = """
        Class AS{
                Val a: Int = 0;
                Var xyz, wfg: Int;
                main(){
                    Var $var1:String = "hhello world";
                }
                function(){{}}
        }
        """
        expect = "Error on line 6 col 24: $var1"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_209(self):
        input = """
         Class E{
            main(){
                Var dawiodjoawid1 : Int = "dawodjawoijdoawd";
            }
            abc();
        }
        """
        expect = "Error on line 6 col 17: ;"
        self.assertTrue(TestParser.test(input, expect, 209))

    def test_210(self):
        input = """
            Class D{
                main(){
                    Var var1:String = "str1";
                }
                foo(){
                        Return True;
                }
            }
            """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 210))


    def test_211(self):
        input = """
            Class C{
                function(){
                    a = b%c + Self.foo();
                    a = b*c*d + Self.foo();
                    Self.foo();
                    Return True;
                }
            }
            """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 211))


    def test_212(self):
        input = """
            Class A{
                main(){
                    Var aw:String = "awgawdfaw";
                }
                foo(){
                    DADAIUHADIUDH.dwaiofghwai9otghfawi(0wqrjoawif, fwafawfwaggwefwa);
                }
            }
            """
        output = "Error on line 7 col 56: wqrjoawif"
        self.assertTrue(TestParser.test(input, output, 212))


    def test_213(self):
        input = """
            Class B{
                main(){
                }
                foo(){
                    a = b%c + Self.foo();
                    Self.foo2(param1, param2);
                    a1 = Self.foo3(param1, param2);
                    Var $b = 1 >= 3;
                    Val val1 = True == False;
                    b = ! val1;
                }
            }
            """
        output = "Error on line 9 col 24: $b"
        self.assertTrue(TestParser.test(input, output, 213))


    def test_214(self):
        input = """
            Class HAHA{
                main(){
                    Var var1:String = "str1";
                }
                foo(){
                    a = b%c + Self.foo();
                    Self.foo2(param1, param2);
                    a1 = Self.foo3(param1, param2);
                    Var b: Boolean = 1 >= 3;
                    Val val1: Boolean = True == False;
                    b = ! val1;
                    Return True;
                }
            }
            """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 214))


    def test_215(self):
        input = """
            Class Program{
                Val a: Int = 0;
                Val b: Int = 0;
                Var c, d: Int;
                main(){
                    Var var1:String = "str1";
                }
                foo(){
                    a = b%c + Self.foo();
                    Self.foo2(param1, param2);
                    a1 = Self.foo3(param1, param2);
                    Var b: Boolean = 1 >= 3;
                    Val val1: Boolean = True == False;
                    b = ! val1;
                    Return True;
                }
            }
            Class Vehicle{
                run(){
                    Self.running = True;
                }
                stop(){
                    Self.running = False;
                }
            }
            """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 215))


    def test_216(self):
        input = """
            Class Vinfast{
                Var running: Boolean = True;
                run(){
                    Self.running = True;
                }
                stop(){
                    Self.running = False;
                }
            }
            """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 216))


    def test_217(self):
        input = """
            Class Vinfast{
                Var running: Boolean = True;
                Val speed: Int;
                Constructor(){
                    Self.speed = 10000000;
                }
                Constructor(speed: Int){
                    Self.speed = speed;
                }
                run(){
                    Self.running = True;
                }
                stop(){
                    Self.running = False;
                }
            }
            """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 217))


    def test_218(self):
        input = """
            Class Vinfast{
                Destructor(){}
            }
            """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 218))


    def test_219(self):
        input = """
            Class Vinfast{
                Constructor(speed: Float, name: String){
                    Self.speed = speed;
                    Self.name = name;
                }
                Destructor(){}
            }
            Class Car:Vinfast{}
            """
        output = "Error on line 3 col 40: ,"
        self.assertTrue(TestParser.test(input, output, 219))


    def test_220(self):
        input = """
            Class Vehicle{
                Var $numOfVehicle: Int;
                Constructor(speed: Float; model_name: String){
                Self.speed = speed;
                Self.name = name;
                }
                Constructor(){
                    Self.speed = 321321421421;
                }

                Destructor(){}
                run(){
                    Self.is_running = True;
                }
                stop(){
                    Self.is_running = False;
                }
            }
            Class Car:Vehicle{}
            """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 220))


    def test_220(self):
        input = """
            Class __AWFJIAWFHBAWIUF__ {
            Var a: Float = 13124122.e312312423;
            waiuhfiawuhawf() {
                Var $a,$b: String, Int;
            """
        output = "Error on line 5 col 20: $a"
        self.assertTrue(TestParser.test(input, output, 220))


    def test_221(self):
        input = """
            Class FOIWAHFIAHFDWAI {
            If (1 + 2 == 0) {
                OutScreen.println(3 * 2);
            }
            Elseif (1 + 2 == "3") {
                Sys32.terminate(41241211 - "4124124124");
            }
            Else {
                Break;
                Return;
            }
        }
            """
        output = "Error on line 3 col 12: If"
        self.assertTrue(TestParser.test(input, output, 221))


    def test_222(self):
        input = """
            Class DAWFAWDFAW {
            function() {
                If (1214125412 + 112312421412 == 0) {
                    Outscreen.print(1 / 2);
                }
                Elseif (1 + 2 == 43124124123) {
                    Sys32.sus(11 - "3222");
                }
                Else {
                    Break;
                    Return;
                }
            }
        }
            """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 222))


    def test_223(self):
        input = """
            Class Car:Vehicle{
                open(){
                    ## Open hood ##
                    If (Hood==False){
                        Hood = True;
                    }
                }
            }
            """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 223))


    def test_223(self):
        input = """
            Class Car:Vehicle{
                Val sunScreen: Boolean = False;
                open(){
                    ## Open hood ##
                    If (Hood==False){
                        Hood = True;
                        Return True
                    }
                    Else 
                        Return False;
                }
            }
            """
        output = "Error on line 9 col 20: }"
        self.assertTrue(TestParser.test(input, output, 223))


    def test_224(self):
        input = """
            Class Car : Vehicle{
                Val speed: String = 0;
                Val $model, tireNum: Float;
            }

            """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 224))


    def test_225(self):
        input = """
            Class Car : Vehicle{
                    Val speed: Float = 0;
                    Val $model, tireNum: Int = 1 * 3 + 4 + 5 + 4 - 4 / 100_000_0000;
                }

            """
        output = "Error on line 4 col 83: ;"
        self.assertTrue(TestParser.test(input, output, 225))


    def test_226(self):
        input = """
            Class Eval{
                getSpeedfromKm(hadhawd, gsiafhQIA, IUEHGFI_eQWEQW: Int; e, gggg: String){
                    Outscreen.get("The speed = " +.  "1000km/h");
                }
            }
            """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 226))


    def test_227(self):
        input = """
            Class HelloWorld : C{Return True;}
            """
        output = "Error on line 2 col 33: Return"
        self.assertTrue(TestParser.test(input, output, 227))


    def test_228(self):
        input = """
            Class Shape {
            foo(){
            a = (b < c < e < f) < True < False;
            } 
            }

            """
        output = "Error on line 4 col 23: <"
        self.assertTrue(TestParser.test(input, output, 228))


    def test_229(self):
        input = """
            Class Shape {
            foo(){
                a = ("a"+."b")+."b";
            } 
            }
            """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 229))


    def test_230(self):
        input = """
             Class Shape {
            foo(){
                c = ("a"==."a")==True;
            } 
            }
            """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 230))

    def test_231(self):
        input = """
         Class Shape {
            foo(){
                a = ("a"+."b")+."b";
                c = ("a"==."a")==True;
            } 
            }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 231))

    def test_232(self):
        input = """
        Class Shape:a:b{}
        """
        output = "Error on line 2 col 21: :"
        self.assertTrue(TestParser.test(input, output, 232))

    def test_233(self):
        input = """
        Class Polygon {
        function(){
            Dqwfgwa::$Dwqags=2312521412;
            Dqwafgw::$Dwqgasda();
            dwqfwa::$c::$Dwtgfwadwa=22341412;
        } 
        }
        """
        output = "Error on line 6 col 22: ::"
        self.assertTrue(TestParser.test(input, output, 233))

    def test_234(self):
        input = """
        Class DAFASCsafwaerwqe {
        dgsadf_iuefsdhiawshd(){
            fawfscawsdwqr::$b="";
            qweqwgsxdfcxzc::$e();
            dwafawf::$dwcscaas()::$dDwafawdasd=Dawgwadssazxc;
        } 
        }
        """
        output = "Error on line 6 col 32: ::"
        self.assertTrue(TestParser.test(input, output, 234))

    def test_235(self):
        input = """
        Class Loop {
        function(){
        i=+1;
        } 
        }
        """
        output = "Error on line 4 col 10: +"
        self.assertTrue(TestParser.test(input, output, 235))

    def test_236(self):
        input = """
        Class Loop {
        function(){
        i+=1;
        } 
        }
        """
        output = "Error on line 4 col 9: +"
        self.assertTrue(TestParser.test(input, output, 236))

    def test_237(self):
        input = """
        Class Loop {
        function(){
        i++;
        } 
        }
        """
        output = "Error on line 4 col 9: +"
        self.assertTrue(TestParser.test(input, output, 237))

    def test_238(self):
        input = """
        Class Loop {
        function(){
        i-=1;
        } 
        }
        """
        output = "Error on line 4 col 9: -"
        self.assertTrue(TestParser.test(input, output, 238))

    def test_239(self):
        input = """
       Class Loop {
        function(){
        i=-1;
        } 
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 239))

    def test_240(self):
        input = """
        Class Loop {
        function(){
        i--;
        } 
        }
        """
        output = "Error on line 4 col 9: -"
        self.assertTrue(TestParser.test(input, output, 240))

    def test_241(self):
        input = """
        Class Sharp{
                    foo(){
                        _ID = New X().Y().Z();
                        Var C : Array[Int, 0];
                    }
                }
        """
        output = "Error on line 5 col 43: 0"
        self.assertTrue(TestParser.test(input, output, 241))

    def test_242(self):
        input = """
         Class Sharp{
                    foo(){
                        _ID = New X().Y().Z();
                        Var C : Array[Int, 0b0];
                    }
                }
        """
        output = "Error on line 5 col 43: 0b0"
        self.assertTrue(TestParser.test(input, output, 242))

    def test_243(self):
        input = """
         Class Sharp{
                    foo(){
                        _ID = New X().Y().Z();
                        Var C : Array[Int, 0X0];
                    }
                }
        """
        output = "Error on line 5 col 43: 0X0"
        self.assertTrue(TestParser.test(input, output, 243))

    def test_244(self):
        input = """
        Class Sharp{
                    func(){
                        Val a:String ="abc";
                        D = 1;
                    }
                }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 244))

    def test_245(self):
        input = """
        Class Sharp{
                    func(){
                        Var a: Array[Int, 01];
                        Var a: Array[Int, 0x1];
                        Var a: Array[Int, 0X1];
                        Var a: Array[Int, 0b1];
                        Var a: Array[Int, 0B1];
                        Var a: Array[Int, 1];
                    }
                }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 245))

    def test_246(self):
        input = """
                Class Sharp{
                    func(){
                        Var a: Array[Int, 1_23.456e+7990];
                    }
                }

        """
        output = "Error on line 4 col 42: 123.456e+7990"
        self.assertTrue(TestParser.test(input, output, 246))

    def test_247(self):
        input = """
        Class Sharp{
                    func(){
                        Var 123: Array[Int, xyz::$ghz.func()];
                    }
                }

        """
        output = "Error on line 4 col 28: 123"
        self.assertTrue(TestParser.test(input, output, 247))

    def test_248(self):
        input = """
         Class Sharp{
                    Var a,b:Int=53,2631;
                }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 248))

    def test_249(self):
        input = """
                 Class Sharp{
                    Var a,b:Int=53,2631l,1242134;
                }
        """
        output = "Error on line 3 col 39: l"
        self.assertTrue(TestParser.test(input, output, 249))

    def test_250(self):
        input = """
                 Class Sharp{
                    Var a,b:Int=53,2631LDAWDAWFA;
                }
        """
        output = "Error on line 3 col 39: LDAWDAWFA"
        self.assertTrue(TestParser.test(input, output, 250))

    def test_251(self):
        input = """
                    Class Shape{
                        Var a,b:Int=1,2,3;
                    }{}

                """
        output = """Error on line 3 col 39: ,"""
        self.assertTrue(TestParser.test(input, output, 251))

    def test_252(self):
        input = """
                    Class Shape{
                        Var a,f,e: Int=1,2;

                    }

                """
        output = """Error on line 3 col 42: ;"""
        self.assertTrue(TestParser.test(input, output, 252))

    def test_253(self):
        input = """
                    Class Shape{
                        Var Ahhh,b:Int=5,6;{}
                    }

                """
        output = """Error on line 3 col 43: {"""
        self.assertTrue(TestParser.test(input, output, 253))

    def test_254(self):
        input = """
                    Class Shape{
                        Var $a,b:Int=5,6;
                        func_tion(){
                            Var $c,d:Int=5,6;
                        }
                    }

                """
        output = """Error on line 5 col 32: $c"""
        self.assertTrue(TestParser.test(input, output, 254))

    def test_255(self):
        input = """
                    Class Shape{
                        func_tion(){
                            ReturnAhhh::$TAloz;
                        }
                    }

                """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 255))

    def test_256(self):
        input = """
                    Class Shape{
                        ReturnAhhh::$TAloz*a::$TAloz---------a::$TAloz;
                    }

                """
        output = """Error on line 3 col 34: ::"""
        self.assertTrue(TestParser.test(input, output, 256))

    def test_257(self):
        input = """
                    Class Shape{
                        func_tion(){
                            ReturnAhhh::$TAloz*a::$TAloz---------a::$TAloz;
                        }
                    }
                """
        output = """Error on line 4 col 46: *"""
        self.assertTrue(TestParser.test(input, output, 257))

    def test_258(self):
        input = """
                    Class Shape{
                        func_tion(){
                            Foreach (Step In 1+1 .. 100+100 By D.func_tion()){}
                        }
                    }
                """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 258))

    def test_259(self):
        input = """
                    Class Shape{
                        func_tion(){
                            Foreach (Step In E::$b() ..312412_edasd32_3123.c.c.c F::$func_tion){
                                Class Shape{}
                            }
                        }
                    }
                """
        output = """Error on line 4 col 61: _edasd32_3123"""
        self.assertTrue(TestParser.test(input, output, 259))

    def test_260(self):
        input = """
                    Class Shape{
                        func_tion(){
                            Foreach (Step In Canon::$b() ..hawuid_3123.c.c.c By IN_D::$func_tion){
                                Var $a:Int;
                            }
                    }
                    """
        output = """Error on line 5 col 36: $a"""
        self.assertTrue(TestParser.test(input, output, 260))

    def test_261(self):
        input = """
                    Class Shape{
                        func_tion(){
                            Foreach (Step In Heck::$b() ..adsda_e.c.c.c By The::$func_tion){
                                Foreach (Step In What::$b() ..42HDASAO_D.c.c.c By ANGLE::$func_tion){}
                            }
                        }
                    }   
                    """
        output = """Error on line 5 col 64: HDASAO_D"""
        self.assertTrue(TestParser.test(input, output, 261))

    def test_262(self):
        input = """
                    Class Shape{
                        func_tion(){
                           ASDNAIWDQAW_312[b[c[d[e[f::$g]]]]][h::$i][j.k()][Lzzzzz::$m()]=0;
                        }
                    }   
                    """
        output = """successful"""
        self.assertTrue(TestParser.test(input, output, 262))

    def test_263(self):
        input = """
                    Class Shape{
                        func_tion(){
                            If (HKKKK == -1--1){
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
                        func_tion(){
                            If (DAOWSIDHAWI_1231239218 == -1--1){
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
                        func_tion(){
                            If (3123_321412_312321_DAWDAW == -1--1){
                                If(b == "c"+."c"){}
                                Elseif(SHAPE == b ==. c){}
                            }
                        }
                    }   
                    """
        output = """Error on line 4 col 50: _DAWDAW"""
        self.assertTrue(TestParser.test(input, output, 265))

    def test_266(self):
        input = """
                    Class DAWDAWFSC{
                        func_tion(){
                            If (AhhWASDAWDh == -1--1){
                                If(b == "c"+."c"){}
                                Elseif(AWSCXS == b ==. c){}
                                Else(1=2){}
                            }
                        }
                    } 
                    """
        output = """Error on line 7 col 36: ("""
        self.assertTrue(TestParser.test(input, output, 266))

    def test_267(self):
        input = """
                    Class Shape{
                        func_tion(){
                            If (DAWDZXCAWR == -1--1){
                                Foreach(Step In 1 .. 100 By 2){
                                    If (AhhEWAEWAEh == -1--1){
                                        Foreach(Step In 1 .. 100 By 2){

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
        output = """Error on line 3 col 24: Break"""
        self.assertTrue(TestParser.test(input, output, 270))

    def test_271(self):
        input = """
                    Class Shape{
                        Continue;
                    }   
                    """
        output = """Error on line 3 col 24: Continue"""
        self.assertTrue(TestParser.test(input, output, 271))

    def test_272(self):
        input = """
                    Class Shape{
                        func_tion(){
                            True=a;
                        }
                    }   
                    """
        output = """Error on line 4 col 32: ="""
        self.assertTrue(TestParser.test(input, output, 272))

    def test_273(self):
        input = """
                    Class Shape{
                        func_tion(){
                           1428172_231468=b==c==d;
                        }
                    }   
                    """
        output = """Error on line 4 col 41: ="""
        self.assertTrue(TestParser.test(input, output, 273))

    def test_274(self):
        input = """
                    Class Shape{
                        func_tion(){
                           421y12_23123=b<=c>=d;
                        }
                    }   
                    """
        output = """Error on line 4 col 30: y12_23123"""
        self.assertTrue(TestParser.test(input, output, 274))

    def test_275(self):
        input = """
                    Class Shape{
                        func_tion(){
                           321A_3123=b==c<d;
                        }
                    }   
                    """
        output = """Error on line 4 col 30: A_3123"""
        self.assertTrue(TestParser.test(input, output, 275))

    def test_276(self):
        input = """
                    Class Shape{
                        Foreach(i In 1 . . 100 by 2 ){}
                    }   
                    """
        output = """Error on line 3 col 24: Foreach"""
        self.assertTrue(TestParser.test(input, output, 276))

    def test_277(self):
        input = """
                    Class Shape{
                        Var fhawifawh: Array[Array[Array[1,1_12],1],1];
                    }   
                    """
        output = """Error on line 3 col 57: 1"""
        self.assertTrue(TestParser.test(input, output, 277))

    def test_278(self):
        input = """
                    Class Shape{
                        Var fhawifawh: Array[Array[Array[d,1_12],1],1];
                    }   
                    """
        output = """Error on line 3 col 57: d"""
        self.assertTrue(TestParser.test(input, output, 278))

    def test_279(self):
        input = """
                    Class Shape{
                        Var fhawifawh: Array[Array[Array[d,_1_12],1],1];
                    }   
                    """
        output = """Error on line 3 col 57: d"""
        self.assertTrue(TestParser.test(input, output, 279))

    def test_280(self):
        input = """
                    Class Shape{
                        Var Kanon : Array[b,Array[c,Array[d,1]]];
                    }   
                    """
        output = """Error on line 3 col 42: b"""
        self.assertTrue(TestParser.test(input, output, 280))

    def test_281(self):
        input = '''Class _:r{}Class _:R{Var _,__0,j_:Array[Array[Array[Float,04],2],0B1];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 281))

    def test_282(self):
        input = '''Class d:q{}Class G{}Class _{}Class _:2G{}Class _{Destructor(){} }Class N8_40IWV:B__{}'''
        expect = 'Error on line 1 col 37: 2'
        self.assertTrue(TestParser.test(input, expect, 282))

    def test_283(self):
        input = '''Class c:_{Destructor(){} }Class __:y_112361{Destructor(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 283))

    def test_284(self):
        input = '''Class Guitar:tW_{$_8(){}Var $_:Float;_(){} }Class D:_{}Class _3M:o_8__l{Constructor(_:W8){Break;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 284))

    def test_285(self):
        input = '''Class ATE2:__0{}Class A1235:_u1gP{}Class _{Val _,$5_,$__R_3v,Q,_,$_H,$9zV_4s_,J_,A6,_:String;}Class __:_v42{}Class F{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 285))

    def test_286(self):
        input = '''Class __:___b_{}Class e3{Var $H6:Float;Val $e_,$_9_:Boolean;Var $_,G,$0143:__1W_;}Class s:_{t(l8:Array[Array[Array[Int,0114],4],0X45];P_:Boolean){} }Class U{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 286))

    def test_287(self):
        input = '''Class _60{}Class __:_{}Class _4124214B:_{}Class z:jA{}Class _1{}Class x{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 287))

    def test_288(self):
        input = '''Class _{$2_1(){} }Class _t:_0{}Class A_:gO2136{$S(_:_;X,_3,_,_:Int){Return;Return!!!!!!New _().X61();{}Continue;} }Class _{}'''
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
        input = '''Class _{}Class dwagwadfasd_5{Val $_:Float;}Class F6_{Val $P_X_,$_,$91:String;}'''
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
        input = '''Class League_of_Legend{Destructor(){Return;_9::$g3k.m();} }Class classA1provip123:z{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 299))

    def test_300(self):
        input = '''
        Class ADWSD{Destructor(){Return;_9::$g3k.m();} }
        Class classA1provip123:z{}
        Class Unique{
                function(){
                   Unique = "HCMUT";
                }
            }
            function2(){
                   Unique = "vjp pro no 1"
            }'''
        expect = 'Error on line 9 col 12: function2'
        self.assertTrue(TestParser.test(input, expect, 300))








