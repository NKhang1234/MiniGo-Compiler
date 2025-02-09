import unittest
from TestUtils import TestParser

class ParserSuite(unittest.TestCase):

#------------------------------------------PROVIDED TEST -------------------------------------------------------------
    def test_simple_program(self):
        """Simple program: void main() {} """
        input = """func main() {
                    var a int
                    }"""
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
    
    # ------------------------- Newline or Semicolon END declared ERROR

    def test_267(self):
        """declared struct"""
        input = """
            type khang struct {
                khang string ;
                khang [1][3]khang ;                     
            }
            type khang struct {
                khang string ;
            }                                                                       
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 267))
        

    # def test_269(self):
    #     """declared Interface"""
    #     input = """
    #         type Calculator interface {
                                        
    #             Add(x, y int) int;
    #             Subtract(a, b float, c int) [3]ID;
    #             Reset()
                                        
    #             SayHello(name string);
                                        
    #         }
    #         type khang interface {}                                                                       
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input, expect, 269))

    # def test_271(self):
    #     """if_statement"""
    #     input = """    
    #         func khang() {
    #             if (x > 10) {} 
    #             if (x > 10) {
                  
    #             } else if (x == 10) {
    #                 var z str;
    #             } else {
    #                 var z ID;
    #             }
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input, expect, 271))

    # def test_272(self):
    #     """for_statement"""
    #     input = """    
    #         func khang() {
    #             for i < 10 {}
    #             for i := 0; i < 10; i += 1 {}
    #             for index, value := range array {}
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input ,expect, 272))


    # def test_273(self):
    #     """break and continue, return, Call  statement"""
    #     input = """    
    #         func khang() {                           
    #             for i < 10 {break;}
    #             break;
    #             continue;
    #             return 1;
    #             return
    #             foo(2 + x, 4 / y); m.goo();                        
    #          }
                                        
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser( input, expect, 273))
         

    # def test_275(self):
    #     """Declared"""
    #     input = """    
    #         type Calculator interface {
    #             Add(x, y [2]ID) [2]int;
    #             Subtract(a, b float, c, e int);
    #             Reset()
    #             SayHello(name string)
    #         }
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser( input, expect, 275))
        
    # def test_276(self):
    #     """Declared"""
    #     input = """
    #         type Calculator interface {}
    #         type Person struct {};
    #     """
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input, expect, 276))
        
    # def test_277(self):
    #     """Declared"""
    #     input = """
                                        
    #         func (c c) Add(x int)  {}
            
    #         func Add(x int, y int) {} var c int;
            
    #         var c int; type Calculator struct{} type Calculator struct {} var c int;
    #     """
    #     expect = "Error on line 7 col 49: type"
    #     self.assertTrue(TestParser.checkParser(input, expect, 277))
        
    # def test_282(self):
    #     """Statement"""
    #     input = """
    #             func Add() {
    #                 const a = a[2].b
    #                 var a = a[2].b; var a = "s";           
    #             }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input, expect, 282))
        
    # def test_283(self):
    #     """Statement"""
    #     input ="""
    #             func Add() {
    #                 a += 2;
    #                 a -= a[2].b();
    #                 a /= 2
    #                 a *= 2
    #                 a %= 2;         
    #             }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input ,expect, 283))
        
    
    # def test_286(self):
    #     """Statement"""
    #     input = """
    #                                 func Add() {
    #                                     2 + 2 += 2;          
    #                                 }"""
    #     expect = "Error on line 3 col 41: 2"
    #     self.assertTrue(TestParser.checkParser(input,expect, 286))
    
    
    # def test_287(self):
    #     """Statement"""
    #     input = """
    #                                 func Add() {
    #                                    a[2+3&&2] += foo().b[2];       
    #                                 }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect, 287))
        
    # def test_288(self):
    #     """Statement"""
    #     input = """
    #                                 func Add() {
    #                                     if (x.foo().b[2])
    #                                     {
    #                                         if (){}
    #                                     }
    #                                 }"""
    #     expect = "Error on line 5 col 49: )"
    #     self.assertTrue(TestParser.checkParser(input, expect, 288))
        
    # def test_289(self):
    #     """Statement"""
    #     input = """
    #                                 func Add() {
    #                                     for var i = 0; i < 10; i += 1 {
    #                                         // loop body
    #                                     }
    #                                 }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect, 289))
    
    # def test_290(self):
    #     """Statement"""
    #     input = """
    #                                 func Add() {
    #                                     for var i [2]int = 0; foo().a.b(); i[3] := 1 {
    #                                         // loop body
    #                                     }
    #                                 }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect, 290))
        
    # def test_291(self):
    #     """Statement"""
    #     input = """
    #                                 func Add() {
    #                                     for index[2], value := range arr {
    #                                     // index: 0, 1, 2
    #                                     // value: 10, 20, 30
    #                                     }
    #                                 }"""
    #     expect = "Error on line 3 col 53: ,"
    #     self.assertTrue(TestParser.checkParser(input, expect, 291))
    
    # def test_292(self):
    #     """Statement"""
    #     input = """
    #                                 func Add() {
    #                                     for index, value := range arr[2] {
    #                                     }
    #                                 }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect, 292))
    
    # def test_293(self):
    #     """Statement"""
    #     input = """
    #                                 func Add() {
    #                                     for index, value := range 23 {
    #                                     }
    #                                 }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect, 293))
    
    # def test_294(self):
    #     """Statement"""
    #     input ="""
    #                                 func Add() {
    #                                     (1+2).foo(2 + 3, a {a:2})
    #                                 }"""
    #     expect = "Error on line 3 col 41: ("
    #     self.assertTrue(TestParser.checkParser(input,expect, 294)) 
    
    # def test_295(self):
    #     """Statement"""
    #     input = """
    #                                 func Add() {
    #                                     a[2][3].foo(2 + 3, a {a:2})
    #                                 }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input,expect, 295))
    
    # def test_296(self):
    #     """Statement"""
    #     input = """
    #                                 func Add() {
    #                                     return (2 + 3).b
    #                                     return -1.c
    #                                 }"""
    #     expect = "Error on line 4 col 51: c"
    #     self.assertTrue(TestParser.checkParser(input, expect, 296))
        
    # def test_297(self):
    #     """Statement"""
    #     input = """
    #                                 func Add() {
    #                                     if (1) {}
    #                                     else if(2) {return string}
    #                                     else if(3) {reutrn int;}
    #                                 }"""
    #     expect = "Error on line 4 col 60: string"
    #     self.assertTrue(TestParser.checkParser(input,expect, 297))
        
        
    # def test_298(self):
    #     """Expression"""
    #     input = """const a = (-1).c;"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input, expect, 298))
    
    # def test_299(self):
    #     """Statement"""
    #     input = """
    #                                 func Add() {
    #                                     if (1) {
    #                                         if(true){}
    #                                         else {}
    #                                     }
    #                                     else if(2) {
    #                                         if(true) {}
    #                                         else {}
    #                                     }
    #                                     else {
    #                                         if (true) {}
    #                                         else {}
    #                                     }
    #                                 }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser(input, expect, 299))
        
    # def test_300(self):
    #     """Statement"""
    #     input = """
    #                                 func Add() {
    #                                     if (1) {
    #                                         if (true) {
    #                                             if(false) {
    #                                                 if(true) {
    #                                                     return \"duy\"
    #                                                 } else {
    #                                                     return \"khang\"
    #                                                 }
    #                                             }
    #                                             else {}     
    #                                         }
    #                                         else {
                                                
    #                                         }
    #                                     }
    #                                 }"""
    #     expect = "successful"
    #     self.assertTrue(TestParser.checkParser( input,expect, 300))    
           