import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

#------------------------------------------PROVIDED TEST -------------------------------------------------------------
    def test_simple_program(self):
        """Simple program: void main() {} """
        input = """func main() {};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,301))

    def test_more_complex_program(self):
        """More complex program"""
        input = """func foo () {
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,302))
    
    def test_wrong_miss_close(self):
        """Miss ) void main( {}"""
        input = """func main({};"""
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input,expect,303))
    def test_wrong_variable(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,304))
    def test_wrong_index(self):
        input = """var i ;"""
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input,expect,305))

#------------------------------------------MYSELF TEST -------------------------------------------------------------

#------------------------------------------ Problem TEST -------------------------------------------------------------
    
    # ------------------------- CATCH ERROR POSITION

    # def test_222(self):
    #     """Literal struct not colon between field name and expression"""
    #     input = "const Dk = DUYKHANG{name \"khang\"};"
    #     expect = "Error on line 1 col 26: khang"
    #     self.assertTrue(TestParser.checkParser(input, expect, 222))
        
    
    # def test_225(self):
    #     """Literal struct not in curly braces"""
    #     input = "const Dk = DUYKHANG(name: , age: 21);"
    #     expect = "Error on line 1 col 25: :"
    #     self.assertTrue(TestParser.checkParser(input, expect, 225))
        
    # def test_227(self):
    #     """Literal struct not field name"""
    #     input = "const Dk = DUYKHANG{\"khang\"};"
    #     expect = "Error on line 1 col 21: khang"
    #     self.assertTrue(TestParser.checkParser(input, expect, 227))
        
    # def test_235(self):
    #     """Expressions access array fail"""
    #     input = "var z khang = a[2, 3]; "
    #     expect = "Error on line 1 col 18: ,"
    #     self.assertTrue(TestParser.checkParser(input,expect, 235))
        
    # def test_238(self):
    #     """Expressions access struct field fail"""
    #     input = " var z DK = khang..name;" 
    #     expect = "Error on line 1 col 19: ."
    #     self.assertTrue(TestParser.checkParser(input,expect, 238))
        
    # def test_239(self):
    #     """Expressions access struct field fail"""
    #     input = " var z DK = khang.1;" 
    #     expect = "Error on line 1 col 19: 1"
    #     self.assertTrue(TestParser.checkParser(input,expect, 239))

    # ------------------------- EXPRESSION ERROR

    def test_247(self):
        """expression"""
        input = "const Dk = 1[2] + foo()[2] + ID[2].b.b;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,247))

    def test_248(self):
        """expression"""
        input = "const Dk = ca.foo(132) + b.c[2];"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,"successful", 248))

    def test_249(self):
        """expression"""
        input = "const Dk = a.a.foo();"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 249))
        
           