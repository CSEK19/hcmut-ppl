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

    def test_4(self):
        """More complex program"""
        input = """1 + 1 + a.foo()"""
        expect = "Error on line 1 col 0: 1"
        self.assertTrue(TestParser.test(input, expect, 204))

    def test_5(self):
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

    def test_6(self):
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

    def test_7(self):
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

    def test_8(self):
        """More complex program"""
        input = """
    Class Shape {
        sum(a,b:Int; c,d:Float){}
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 208))

    def test_9(self):
        """More complex program"""
        input = """
    Class Shape {
        Var a :Array[Array[Int,2],2] = Array(Array(1,1),Array(1,1));
    }
    """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 209))







