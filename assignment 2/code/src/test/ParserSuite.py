import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_201(self):
        input = """Class A{foo(){Self::a = 1;}}"""
        output = "successful"
        self.assertTrue(TestParser.test(input, output, 201))