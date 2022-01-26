import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_201(self):
        input = """Class Program{}"""
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 201))

    def test_202(self):
        input = """Class Program{
            main(){
            }
        }"""
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 202))

    def test_203(self):
        input = """Class Program{
            main(){
                Val a:Int = 2;
            }
        }"""
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 203))

    def test_203(self):
        input = """Class Program{
            main(){
                Val $a:Int = 2;
            }
        }"""
        output = "Error on line 3 col 20: $a"
        self.assertTrue(TestParser.test(input, output, 203))

    def test_204(self):
        input = """Class Program{
                    main(){
                        Val $a:Int = 2;
                    }
                }"""
        output = "Error on line 3 col 28: $a"
        self.assertTrue(TestParser.test(input, output, 204))

    def test_205(self):
        input = """Class Program{
            main(){
                Val a: Int = 0;
                Val b: Int = 0;
                Var c, d: Int;
            }
        }"""
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 205))

    def test_205(self):
        input = """Class Program{
                Val a: Int = 0;
                Val b: Int = 0;
                Var c, d: Int;
        }"""
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 205))

    def test_206(self):
        input = """Class Program{
                Val a: Int = 0;
                Val b: Int = 0;
                Var c, d: Int;
                main(){
                }
                foo(){}
        }"""
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 206))

    def test_207(self):
        input = """Class Program{
                Val a: Int = 0;
                Val b: Int = 0;
                Var c, d: Int;
                main(){
                    Var $var1:String = "str1";
                }
                foo(){}
        }"""
        output = "Error on line 6 col 24: $var1"
        self.assertTrue(TestParser.test(input, output, 207))

    def test_208(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo()
        }
        """
        output = "Error on line 10 col 8: }"
        self.assertTrue(TestParser.test(input, output, 208))

    def test_209(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo();
        }
        """
        output = "Error on line 9 col 17: ;"
        self.assertTrue(TestParser.test(input, output, 209))

    def test_210(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
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
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                Return True;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 211))

    def test_212(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Return True;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 212))

    def test_213(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var $b = 1 >= 3;
                Val val1 = True == False;
                b = ! val1;
                Return True;
            }
        }
        """
        output = "Error on line 13 col 20: $b"
        self.assertTrue(TestParser.test(input, output, 213))

    def test_214(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
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
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
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
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Constructor(){}
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
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Val speed: Int;
            Constructor(){
                Self.speed = 30;
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
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Val speed: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int){
                Self.speed = speed;
            }
            Destructor(){}
            run(){
                Self.running = True;
            }
            stop(){
                Self.running = False;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 218))

    def test_219(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int, model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                Self.running = True;
            }
            stop(){
                Self.running = False;
            }
        }
        Class Car:Vehicle{}
        """
        output = "Error on line 27 col 34: ,"
        self.assertTrue(TestParser.test(input, output, 219))

    def test_220(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                Self.running = True;
            }
            stop(){
                Self.running = False;
            }
        }
        Class Car:Vehicle{}
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 220))

    def test_220(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                Self.running = True;
            }
            stop(){
                Self.running = False;
            }
        }
        Class Car:Vehicle{}
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 220))

    def test_221(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }
        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            openCabin(){
                ## Open cabin ##
                openedCabin = True;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 221))

    def test_222(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }
        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                }
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 222))

    def test_223(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }
        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                }
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 223))

    def test_223(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }
        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True
                }
                Else 
                    Return False;
            }
        }
        """
        output = "Error on line 48 col 16: }"
        self.assertTrue(TestParser.test(input, output, 223))

    def test_224(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }
        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True
                }
                Else {
                    Return False;
                }
            }
        }
        """
        output = "Error on line 48 col 16: }"
        self.assertTrue(TestParser.test(input, output, 224))

    def test_225(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }
        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            openAllDoor(){
            }
            }
        }
        """
        output = "Error on line 52 col 25: {"
        self.assertTrue(TestParser.test(input, output, 225))

    def test_226(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }
        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            Val doors: Array[Boolean, 4];
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            }
            openAllDoor(){
                Foreach (i In 1 .. 4 By 1){
                    doors[i] = True;
                }
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 226))

    def test_227(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }
        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            Val doors: Array[Boolean, 4];
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            }
            openAllDoor(){
                Foreach (i In 1 .. 4 By 1){
                    doors[i] = True;
                    foo1();
                }
            }
            closeAllDoor(){
                Foreach (i In 4 .. 1 By -1){
                    doors[i] = False;
                    foo2();
                }
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 227))

    def test_228(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;
            main(){
                Var var1:String = "str1";
            }
            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }
        Class Door{}
        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            Val doors: Array[Boolean, 4];
            Val backDoor: Door = New Door();
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            }
            openAllDoor(){
                Foreach (i In 1 .. 4 By 1){
                    doors[i] = True;
                    foo1();
                }
            }
            closeAllDoor(){
                Foreach (i In 4 .. 1 By -1){
                    doors[i] = False;
                    foo2();
                }
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 228))

    def test_229(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }

        Class Door{
            Val hasSunScreen: Boolean = True;
        }

        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            Val doors: Array[Boolean, 4];
            Val backDoor: Door = New Door();
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            }
            openAllDoor(){
                Foreach (i In 1 .. 4 By 1){
                    doors[i] = True;
                    foo1();
                }
            }
            closeAllDoor(){
                Foreach (i In 4 .. 1 By -1){
                    doors[i] = False;
                    foo2();
                }
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 229))

    def test_230(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }

        Class Door{
            Val hasSunScreen: Boolean = True;
        }

        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            Val doors: Array[Boolean, 4];
            Val backDoor: Door = New Door();
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            }
            openAllDoor(){
                Foreach (i In 1 .. 4 By 1){
                    doors[i] = True;
                    foo1();
                }
            }
            closeAllDoor(){
                Foreach (i In 4 .. 1 By -1){
                    doors[i] = False;
                    foo2();
                }
            }
        }

        class Motor:Vehicle{
            Var $motorList:Array[Motor, 100];
        }
        """
        output = "Error on line 76 col 8: class"
        self.assertTrue(TestParser.test(input, output, 230))

    def test_231(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }

        Class Door{
            Val hasSunScreen: Boolean = True;
        }

        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            Val doors: Array[Boolean, 4];
            Val backDoor: Door = New Door();
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            }
            openAllDoor(){
                Foreach (i In 1 .. 4 By 1){
                    doors[i] = True;
                    foo1();
                }
            }
            closeAllDoor(){
                Foreach (i In 4 .. 1 By -1){
                    doors[i] = False;
                    foo2();
                }
            }
        }

        Class Motor:Vehicle{
            Var $motorList:Array[Motor, 100];
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 231))

    def test_232(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }

        Class Door{
            Val hasSunScreen: Boolean = True;
        }

        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            Val doors: Array[Boolean, 4];
            Val backDoor: Door = New Door();
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            }
            openAllDoor(){
                Foreach (i In 1 .. 4 By 1){
                    doors[i] = True;
                    foo1();
                }
            }
            closeAllDoor(){
                Foreach (i In 4 .. 1 By -1){
                    doors[i] = False;
                    foo2();
                }
            }
        }

        Class Motor:Vehicle{
            Var $motorList:Array[Motor, 100];
            Val maxSpeed: Int = 40;
            Constructor(){

            }
            Constructor(maxSpeed:Int){
                Self.maxSpeed = maxSpeed;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 232))

    def test_233(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }

        Class Door{
            Val hasSunScreen: Boolean = True;
        }

        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            Val doors: Array[Boolean, 4];
            Val backDoor: Door = New Door();
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            }
            openAllDoor(){
                Foreach (i In 1 .. 4 By 1){
                    doors[i] = True;
                    foo1();
                }
            }
            closeAllDoor(){
                Foreach (i In 4 .. 1 By -1){
                    doors[i] = False;
                    foo2();
                }
            }
        }

        Class Motor:Vehicle{
            Var $motorList:Array[Motor, 100];
            Val maxSpeed: Int = 40;
            Constructor(){

            }
            Constructor(maxSpeed:Int){
                Self.maxSpeed = maxSpeed;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 233))

    def test_234(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }

        Class Door{
            Val hasSunScreen: Boolean = True;
        }

        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            Val doors: Array[Boolean, 4];
            Val backDoor: Door = New Door();
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            }
            openAllDoor(){
                Foreach (i In 1 .. 4 By 1){
                    doors[i] = True;
                    foo1();
                }
            }
            closeAllDoor(){
                Foreach (i In 4 .. 1 By -1){
                    doors[i] = False;
                    foo2();
                }
            }
        }

        Class Motor:Vehicle{
            Var $motorList:Array[Motor, 100];
            Var $numOfMotor: Int = 0;
            Val maxSpeed: Int = 40;
            Constructor(){
                motorList[Motor::$numOfMotor] = Self;
                Motor::$numOfMotor += 1;
            }
            Constructor(maxSpeed:Int){
                Self.maxSpeed = maxSpeed;
            }
        }
        """
        output = "Error on line 82 col 36: ="
        self.assertTrue(TestParser.test(input, output, 234))

    def test_235(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }

        Class Door{
            Val hasSunScreen: Boolean = True;
        }

        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            Val doors: Array[Boolean, 4];
            Val backDoor: Door = New Door();
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            }
            openAllDoor(){
                Foreach (i In 1 .. 4 By 1){
                    doors[i] = True;
                    foo1();
                }
            }
            closeAllDoor(){
                Foreach (i In 4 .. 1 By -1){
                    doors[i] = False;
                    foo2();
                }
            }
        }

        Class Motor:Vehicle{
            Var $motorList:Array[Motor, 100];
            Var $numOfMotor: Int = 0;
            Val maxSpeed: Int = 40;
            Constructor(){
                motorList[Motor::$numOfMotor] = Self;
                Self::$numOfMotor = Motor::$numOfMotor + 1;
            }
            Constructor(maxSpeed:Int){
                Self.maxSpeed = maxSpeed;
            }
        }


        """
        output = "Error on line 82 col 20: ::"
        self.assertTrue(TestParser.test(input, output, 235))

    def test_236(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }

        Class Door{
            Val hasSunScreen: Boolean = True;
        }

        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            Val doors: Array[Boolean, 4];
            Val backDoor: Door = New Door();
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            }
            openAllDoor(){
                Foreach (i In 1 .. 4 By 1){
                    doors[i] = True;
                    foo1();
                }
            }
            closeAllDoor(){
                Foreach (i In 4 .. 1 By -1){
                    doors[i] = False;
                    foo2();
                }
            }
        }

        Class Motor:Vehicle{
            Var $motorList:Array[Motor, 100];
            Var $numOfMotor: Int = 0;
            Val maxSpeed: Int = 40;
            Constructor(){
                motorList[Motor::$numOfMotor] = Self;
                Motor::$numOfMotor = Motor::$numOfMotor + 1;
            }
            Constructor(maxSpeed:Int){
                Self.maxSpeed = maxSpeed;
            }
            Destructor{
                a = b;
            }
        }
        """
        output = "Error on line 87 col 22: {"
        self.assertTrue(TestParser.test(input, output, 236))

    def test_237(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }

        Class Door{
            Val hasSunScreen: Boolean = True;
        }

        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            Val doors: Array[Boolean, 4];
            Val backDoor: Door = New Door();
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            }
            openAllDoor(){
                Foreach (i In 1 .. 4 By 1){
                    doors[i] = True;
                    foo1();
                }
            }
            closeAllDoor(){
                Foreach (i In 4 .. 1 By -1){
                    doors[i] = False;
                    foo2();
                }
            }
        }

        Class Motor:Vehicle{
            Var $motorList:Array[Motor, 100];
            Var $numOfMotor: Int = 0;
            Val maxSpeed: Int = 40;
            Constructor(){
                motorList[Motor::$numOfMotor] = Self;
                Motor::$numOfMotor = Motor::$numOfMotor + 1;
            }
            Constructor(maxSpeed:Int){
                Self.maxSpeed = maxSpeed;
            }
            Destructor(){
                a = b;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 237))

    def test_238(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }

        Class Door{
            Val hasSunScreen: Boolean = True;
        }

        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            Val doors: Array[Boolean, 4];
            Val backDoor: Door = New Door();
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            }
            openAllDoor(){
                Foreach (i In 1 .. 4 By 1){
                    doors[i] = True;
                    foo1();
                }
            }
            closeAllDoor(){
                Foreach (i In 4 .. 1 By -1){
                    doors[i] = False;
                    foo2();
                }
            }
        }

        Class Motor:Vehicle{
            Var $motorList:Array[Motor, 100];
            Var $numOfMotor: Int = 0;
            Val maxSpeed: Int = 40;
            Constructor(){
                motorList[Motor::$numOfMotor] = Self;
                Motor::$numOfMotor = Motor::$numOfMotor + 1;
            }
            Constructor(maxSpeed:Int){
                Self.maxSpeed = maxSpeed;
            }
            Destructor(){
                Foreach(i In Motor::$numOfMotor .. 1 By -1){}
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 238))

    def test_239(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }
        Class Vehicle{
            Var running: Boolean = True;
            Var speed: Int;
            Var model_name: String;
            Var $numOfVehicle: Int;
            Constructor(){
                Self.speed = 30;
            }
            Constructor(speed: Int; model_name: String){
                Self.speed = speed;
                Self.model_name = model_name;
            }
            Destructor(){}
            run(){
                ## Start running ##
                Self.running = True;
            }
            stop(){
                ## Stop ##
                Self.running = False;
            }
        }

        Class Door{
            Val hasSunScreen: Boolean = True;
        }

        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            Val doors: Array[Boolean, 4];
            Val backDoor: Door = New Door();
            openCabin(){
                ## Open cabin ##
                If (openedCabin==False){
                    openedCabin = True;
                    Return True;
                }
                Else {
                    Return False;
                }
            }
            openAllDoor(){
                Foreach (i In 1 .. 4 By 1){
                    doors[i] = True;
                    foo1();
                }
            }
            closeAllDoor(){
                Foreach (i In 4 .. 1 By -1){
                    doors[i] = False;
                    foo2();
                }
            }
        }

        Class Motor:Vehicle{
            Var $motorList:Array[Motor, 100];
            Var $numOfMotor: Int = 0;
            Val maxSpeed: Int = 40;
            Constructor(){
                motorList[Motor::$numOfMotor] = Self;
                Motor::$numOfMotor = Motor::$numOfMotor + 1;
            }
            Constructor(maxSpeed:Int){
                Self.maxSpeed = maxSpeed;
            }
            Destructor(){
                Foreach(i In Motor::$numOfMotor .. 1 By -1){
                    Motor::$motorList[i] = Null;
                }
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 239))

    def test_240(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }

        Class Diary{
            Val $arr: Array[Array[String, 2], 5];
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 240))

    def test_241(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }

        Class Diary{
            Val $arr: Array[Array[String, 2], 5];
            Constructor(){}
            addDiary(diary: Array[String, 2]){
                Diary::arr[0] = diary;
            }
        }
        """
        output = "Error on line 26 col 23: arr"
        self.assertTrue(TestParser.test(input, output, 241))

    def test_242(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }

        Class Diary{
            Val $arr: Array[Array[String, 2], 5];
            Constructor(){}
            addDiary(diary: Array[String, 2]){
                Diary::$arr[0] = diary;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 242))

    def test_243(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }

        Class Diary{
            Var $arr: Array[Array[String, 2], 5];
            Var $numOfDiary = 0;
            Constructor(){
                Diary::$numOfDiary = Diary::$numOfDiary + 1;
            }
            addDiary(diary: Array[String, 2]){
                Diary::$arr[Diary::$numOfDiary] = diary;
            }
        }
        """
        output = "Error on line 24 col 28: ="
        self.assertTrue(TestParser.test(input, output, 243))

    def test_244(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }

        Class Diary{
            Var $arr: Array[Array[String, 2], 5];
            Var $numOfDiary: Int = 0;
            Constructor(){
                Diary::$numOfDiary = Diary::$numOfDiary + 1;
            }
            getNumOfDiary(){
                Return Motor::$numOfDiary;
            }
            addDiary(diary: Array[String, 2]){
                Diary::$arr[Diary::$numOfDiary] = diary;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 244))

    def test_245(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }

        Class Diary{
            Var $arr: Array[Array[String, 2], 5];
            Var $numOfDiary: Int = 0;
            Constructor(){
                Diary::$numOfDiary = Diary::$numOfDiary + 1;
            }
            getNumOfDiary(){
                Return Motor::$numOfDiary;
            }
            addDiary(diary: Array[String, 2]){
                Diary::$arr[Self.getNumOfDiary()] = diary;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 245))

    def test_246(self):
        input = """
        Class Program{
            Val a: Int = 0;
            Val b: Int = 0;
            Var c, d: Int;

            main(){
                Var var1:String = "str1";
            }

            foo(){
                a = b%c + foo();
                foo2(param1, param2);
                a1 = foo3(param1, param2);
                Var b: Boolean = 1 >= 3;
                Val val1: Boolean = True == False;
                b = ! val1;
                Return True;
            }
        }

        Class Diary{
            Var $arr: Array[Array[String, 2], 5];
            Var $numOfDiary: Int = 0;
            Constructor(){
                Diary::$numOfDiary = Diary::$numOfDiary + 1;
            }
            getNumOfDiary(){
                Return Motor::$numOfDiary;
            }
            addDiary(diary: Array[String, 2]){
                Diary::$arr[Self.getNumOfDiary()] = diary;
            }
            deleteDiary(id: Int){
                Diary::$arr[id] = Null;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 246))

    def test_247(self):
        input = """
        Class Diary{
            Var $arr: Array[Array[String, 2], 5];
            Var $numOfDiary: Int = 0;
            Constructor(){
                Diary::$numOfDiary = Diary::$numOfDiary + 1;
            }
            Destructor(){
                Foreach (i in Motor::$numOfDiary .. 1 By -1){
                    If (Motor::$arr[i] == Null){
                        Continue;
                    }
                    Else{
                        Motor::$arr[i] = Null;
                    }
                }
            }
            getNumOfDiary(){
                Return Motor::$numOfDiary;
            }
            addDiary(diary: Array[String, 2]){
                Diary::$arr[Self.getNumOfDiary()] = diary;
            }
            deleteDiary(id: Int){
                Diary::$arr[id] = Null;
            }
        }
        """
        output = "Error on line 9 col 27: in"
        self.assertTrue(TestParser.test(input, output, 247))

    def test_248(self):
        input = """
        Class Diary{
            Var $arr: Array[Array[String, 2], 5];
            Var $numOfDiary: Int = 0;
            Constructor(){
                Diary::$numOfDiary = Diary::$numOfDiary + 1;
            }
            Destructor(){
                Foreach (i In Motor::$numOfDiary .. 1 By -1){
                    If (Motor::$arr[i] == Null){
                        Continue;
                    }
                    Else{
                        Motor::$arr[i] = Null;
                    }
                }
            }
            getNumOfDiary(){
                Return Motor::$numOfDiary;
            }
            addDiary(diary: Array[String, 2]){
                Diary::$arr[Self.getNumOfDiary()] = diary;
            }
            deleteDiary(id: Int){
                Diary::$arr[id] = Null;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 248))

    def test_249(self):
        input = """
        Class Diary{
            Var $arr: Array[Array[String, 2], 5];
            Var $numOfDiary: Int = 0;
            Var id:Int = 0;
            Constructor(){
                Diary::$numOfDiary = Diary::$numOfDiary + 1;
            }
            Destructor(){
                Foreach (i In Motor::$numOfDiary .. 1 By -1){
                    If (Motor::$arr[i] == Null){
                        Continue;
                    }
                }
            }
            getNumOfDiary(){
                Return Motor::$numOfDiary;
            }
            addDiary(diary: Array[String, 2]){
                Diary::$arr[Self.getNumOfDiary()] = diary;
            }
            deleteDiary(id: Int){
                Diary::$arr[id] = Null;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 249))

    def test_250(self):
        input = """
        Class Diary{
            Var $arr: Array[Array[String, 2], 5];
            Var $numOfDiary: Int = 0;
            Var id:Int = 0;
            Constructor(){
                Diary::$numOfDiary = Diary::$numOfDiary + 1;
            }
            Destructor(){
                Foreach (i In Motor::$numOfDiary .. 1 By -1){
                    Motor::$arr[Self.id] = Null;
                }
            }
            getNumOfDiary(){
                Return Motor::$numOfDiary;
            }
            addDiary(diary: Array[String, 2]){
                Diary::$arr[Self.getNumOfDiary()] = diary;
            }
            deleteDiary(id: Int){
                Diary::$arr[id] = Null;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 250))

    def test_251(self):
        input = """
        Class Diary{
            Var $arr: Array[Array[String, 2], 5];
            Var $numOfDiary: Int = 0;
            Var id:Int = 0;
            Var a,b: Int = 1;
            Constructor(){
                Diary::$numOfDiary = Diary::$numOfDiary + 1;
            }
            Destructor(){
                Foreach (i In Motor::$numOfDiary .. 1 By -1){
                    Motor::$arr[Self.id] = Null;
                }
            }
            getNumOfDiary(){
                Return Motor::$numOfDiary;
            }
            addDiary(diary: Array[String, 2]){
                Diary::$arr[Self.getNumOfDiary()] = diary;
            }
            deleteDiary(id: Int){
                Diary::$arr[id] = Null;
            }
        }
        """
        output = "Error on line 6 col 28: ;"
        self.assertTrue(TestParser.test(input, output, 251))

    def test_252(self):
        input = """
        Class Diary{
            Var $arr: Array[Array[String, 2], 5];
            Var $numOfDiary: Int = 0;
            Var id:Int = 0;
            Var a,b: Int = 1,2;
            Constructor(){
                Diary::$numOfDiary = Diary::$numOfDiary + 1;
            }
            Destructor(){
                Foreach (i In Motor::$numOfDiary .. 1 By -1){
                    Motor::$arr[Self.id] = Null;
                }
            }
            getNumOfDiary(){
                Return Motor::$numOfDiary;
            }
            addDiary(diary: Array[String, 2]){
                Diary::$arr[Self.getNumOfDiary()] = diary;
            }
            deleteDiary(id: Int){
                Diary::$arr[id] = Null;
            }
        }
        """
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 252))

