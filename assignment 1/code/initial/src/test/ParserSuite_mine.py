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
        Class Triangle:Shape{
        Val arr : Array[Student,3];
        foo(){
            Var a : Student = New Student();
        }
        }
        """
        expect = "successful"
        self.assertTrue(TestParser.test(input, expect, 206))




