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
        expect = "successful"
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
            Val a: Boolean = !!True;
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
        expect = "successful"
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
        expect = "successful"
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


