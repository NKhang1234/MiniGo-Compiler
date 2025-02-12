import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

#------------------------------------------PROVIDED TEST -------------------------------------------------------------
    def test_simple_program(self):
        """Simple program: void main() {} """
        input = """func main() {
                    var a int
                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,301))

    def test_more_complex_program(self):
        """More complex program"""
        input = """func foo () {
        var a int;
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
    
    # ------------------------------------------VAR DECLARE ERROR----------------------------------------------
    # def test_200(self):
    #     input = """func main() {
    #         var i;
    #     };"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input, expect, 200))

    # def test_201(self):
    #     input = """func foo () {
    #         var i;
    #     };"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input, expect, 201))

    # def test_204(self):
    #     input = """var i ;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input, expect, 204))

    # def test_260(self):
    #     input = "var y;"
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input, expect, 260))

    # ------------------------------------------CATCH ERROR IN STRUCTLIT ERROR----------------------------------------------
    # def test_222(self):
    #     input = "const Mn = MinhNhat{name \"nhat\"};"
    #     expect = "Error on line 1 col 20: {"
    #     self.assertTrue(TestParser.checkParser(input, expect, 222))

    # def test_227(self):
    #     input = "const Mn = MinhNhat{\"nhat\"};"
    #     expect = "Error on line 1 col 20: {"
    #     self.assertTrue(TestParser.checkParser(input, expect, 227))

    # ------------------------------------------CATCH ERROR IN ARRAY ACCESS ERROR----------------------------------------------
    # def test_235(self):
    #     input = "var z nhat = a[2, 3]; "
    #     expect = "Error on line 1 col 15: ["
    #     self.assertTrue(TestParser.checkParser(input, expect, 235))

    # ------------------------------------------STRUCT ACCESS -> FIELD ERROR----------------------------------------------
    # def test_239(self):
    #     input = " var z Mn = nhat.1;"
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input, expect, 239))

    # ------------------------------------------LEFT HANDISDE OF ASSIGNMENT ERROR----------------------------------------------
    # def test_285(self):
    #     input = """
    #                                 func Add() {
    #                                     a.foo() += 2;
    #                                 }"""
    #     expect = "Error on line 4 col 38: <EOF>"
    #     self.assertTrue(TestParser.checkParser(input, expect, 285))

    # ------------------------------------------UPDATE IN FOR: SCALAR? ERROR----------------------------------------------
    # def test_290(self):
    #     input = """
    #                                 func Add() {
    #                                     for var i [2]int = 0; foo().a.b(); i[3] := 1 {
    #                                         // loop body
    #                                         break;
    #                                     }
    #                                 };"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input, expect, 290))

    # ------------------------------------------CAN ARRAY BE NUMBER ERROR----------------------------------------------
    # def test_293(self):
    #     input = """
    #                                 func Add() {
    #                                     for index, value := range 23 {
    #                                         break;
    #                                     }
    #                                 };"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input, expect, 293))

    
    