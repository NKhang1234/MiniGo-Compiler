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
        self.assertTrue(TestParser.checkParser(input,expect,302))

    def test_more_complex_program(self):
        """More complex program"""
        input = """func foo () {
        var a int;
        };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,303))
    
    def test_wrong_miss_close(self):
        """Miss ) void main( {}"""
        input = """func main({};"""
        expect = "Error on line 1 col 11: {"
        self.assertTrue(TestParser.checkParser(input,expect,304))
    def test_wrong_variable(self):
        input = """var int;"""
        expect = "Error on line 1 col 5: int"
        self.assertTrue(TestParser.checkParser(input,expect,305))
    def test_wrong_index(self):
        input = """var i ;"""
        expect = "Error on line 1 col 7: ;"
        self.assertTrue(TestParser.checkParser(input,expect,306))

#------------------------------------------MYSELF TEST -------------------------------------------------------------

    def test_201(self):
        input = """
                func add(a int, b int) int {
                    return a + b
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 201))

    def test_202(self):
        input = """
                func Process() {
                    for i, v := range numbers {
                        putInt(v);
                    }
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 202))

    def test_203(self):
        input = """func Process() {
                        for i, v := range 10 {
                            putInt(v);
                        }
                    }
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 203))

    def test_204(self):
        input = """func Calculate() {
                        var x =;
                    }
                    """
        expect = "Error on line 2 col 32: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 204))

    def test_205(self):
        input = """func Compute() {
                        for i := 0; i < 3; i += 1 {
                            for j := 0; j < 2; j += 1 {
                                putInt(i * j);
                            }
                        }
                    }
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 205))

    def test_206(self):
        input = """func LoopError() {
                        for ;; {
                            putString("Infinite Loop");
                        }
                    }
                    """
        expect = "Error on line 2 col 29: ;"
        self.assertTrue(TestParser.checkParser(input , expect, 206))

    def test_207(self):
        input = """    
            func ExitLoop() {
                for i := 0; i < 10; i += 1 {
                    if i == 5 {
                        break;
                    }
                }
            }

        """
        expect = "Error on line 4 col 24: i"
        self.assertTrue(TestParser.checkParser( input, expect, 207))

    def test_208(self):
        input = """    
            func khang() {                           
                for i < 10 {break;}
                break;
                continue;
                return 1;
                return
                foo(2 + x, 4 / y); m.goo();                        
             }
                                        
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser( input, expect, 208))

    def test_209(self):
        input = """func test() {
                        break;
                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 209))

    def test_210(self):
        input = """func SkipEven() {
                        for i := 0; i < 10; i += 1 {
                            if i % 2 == 0 {
                                continue;
                            }
                            putInt(i);
                        }
                    }
                    """ 
        expect = "Error on line 3 col 32: i"
        self.assertTrue(TestParser.checkParser(input,expect, 210))

    def test_211(self):
        input = """func hehe() {
                        continue;
                    }
                    
                    """ 
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 211))

    def test_212(self):
        input = """func PrintArray() {
                        var arr [3]int = {1, 2, 3};
                        for _, value := range arr {
                            putInt(value);
                        }
                    }
                    """
        expect = "Error on line 2 col 42: {"
        self.assertTrue(TestParser.checkParser(input, expect, 212))

    def test_213(self):
        input = """func PrintArray() {
                        for _, value := range arr {
                            putInt(value);
                        }
                    }
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 213))

    def test_214(self):
        input = """
            type Person struct {
                name string;
                age int;
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 214))

    def test_215(self):
        input = """func PrintPersons() {
                        var people [2]Person = {Person{name: "Alice", age: 25}, Person{name: "Bob", age: 30}};
                        for _, p := range people {
                            putStringLn(p.name);
                        }
                    }""" 
        expect = "Error on line 2 col 48: {"
        self.assertTrue(TestParser.checkParser(input , expect, 215))

    def test_216(self):
        input = """func AccessError() {
                        var p Person;
                        putStringLn(p.name); // Uninitialized field
                    }"""
        expect = "Error on line 4 col 22: <EOF>"
        self.assertTrue(TestParser.checkParser(input , expect, 216))

    def test_217(self):
        input = """func Sum(a int, b int) int {
                        return a + b;
                    }
                    """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input , expect, 217))

    def test_218(self):
        input = """
                func Main() {
                    var result int = Sum(5, 3);
                    putInt(result);
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.checkParser( input,expect, 218))

    def test_219(self):
        input = """    
            func Main() {
                var result int = Sum(5);
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input ,expect, 219))

    def test_220(self):
        input = """func GetNumbers() [3]int {
                        return [3]int{1, 2, 3};
                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 220))

    def test_221(self):
        input = """    
            func Main() {
                var arr [3]int = GetNumbers();
            }
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser( input, expect, 221))

    def test_222(self):
        input = """func GetNumbers() [3]int {
                        return {1, 2, 3};
                    }
                    """
        expect = "Error on line 2 col 32: {"
        self.assertTrue(TestParser.checkParser(input, expect, 222))

    def test_223(self):
        input = """
            func CheckNumbers(x int) {
                if x > 0 {
                    if x % 2 == 0 {
                        putStringLn("Positive Even");
                    } else {
                        putStringLn("Positive Odd");
                    }
                } else {
                    putStringLn("Non-Positive");
                }
            }
                                                     
        """
        expect = "Error on line 3 col 20: x"
        self.assertTrue(TestParser.checkParser(input,expect, 223))

    def test_224(self):
        input = """
        type Computer struct {
            name string;
            model string
            brand string;                                                    
        }      
"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,224))

    def test_225(self):
        input = """    
            func khangKhang() {
                var m int = Computer.arr[0] + 3 / 4;
                var n = "Hello" / b[78];   
                var o float;
                                        
                const khang = Table.fall + 5;
            }                                       
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 225))

    def test_226(self):
        input = "const hehe = Bloom{age: 21, name: \"khang\"};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 226))

    def test_227(self):
        input = "const hoho = [14]float{43,65,54.76,54,432.654,43,65.74,76.88};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 227))

    def test_228(self):
        input = "const test = 12 + 34 - 56 * 78 / (98 + 76) - 54 % 321;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 228))

    def test_229(self):
        input = " var z testAccess = HCMUT.CSE.ComputerScience.PPL;" 
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 229))

    def test_230(self):
        input = "var z hoho = a.b[3].c.d.e[43]; "
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 230))

    def test_231(self):
        input = """    
            func Multi(d) [5][4][3]s {}
        """
        expect = "Error on line 2 col 25: )"
        self.assertTrue(TestParser.checkParser( input, expect, 231))

    def test_232(self):
        input = "const ffff = Restaurant{name: \"Ngon\", address: \"232 Hai Ba Trung\"};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 232))

    def test_233(self):
        input = "const dddd = [4+5+6+7]arr{1+2-3+4,5453,56.5};"
        expect = "Error on line 1 col 16: +"
        self.assertTrue(TestParser.checkParser(input, expect, 233))

    def test_234(self):
        input = "const aaaa = Table{name: \"HCMUT\", material: \"wood\"};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 234))

    def test_235(self):
        input = """
            func test(a, b, c int) float  {return hehe;};
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser( input, expect, 235))

    def test_236(self):
        input = """func test() {
                        if (x > 10) {
                            println("x is greater than 10");
                            if (x>11) {
                                println("x is greater than 10");
                                if (x>11) {
                                    println("x is greater than 10");
                                } else {
                                    println("x is greater than 10");
                                }
                            } else {
                                println("x is greater than 10");
                            }
                        } else {
                            println("x is greater than 10");
                        }
                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect,236))

    def test_237(self):
        input = " var z fffff = sub(t int, f string);" 
        expect = "Error on line 1 col 22: int"
        self.assertTrue(TestParser.checkParser(input,expect, 237))

    def test_238(self):
        input = """
                                    func Sub() {
                                        for var a = 0; hehe().g.d.f[65]; d := 43 {
                                            // loop body
                                                for var a = 0; hehe().g.d.f[65]; d := 43 {
                                                    // loop body
                                                    for var a = 0; hehe().g.d.f[65]; d := 43 {
                                                        // loop body
                                                        break;
                                                    }
                                                    break;
                                                }
                                            break;
                                        }
                                    };"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 238))

    def test_239(self):
        input = " var z ss = mul(h,j,f,d,h,arr[6],f.h);" 
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input,expect, 239))

    def test_240(self):
        input = """
            func test() {
                        if (x > 10) {
                            println("x is greater than 10");
                            if (x>11) {
                                println("x is greater than 10");
                                if (x>11) {
                                    println("x is greater than 10");
                                } else {
                                    println("x is greater than 10");
                                    for var a = 0; hehe().g.d.f[65]; d := 43 {
                                        // loop body
                                        for var a = 0; hehe().g.d.f[65]; d := 43 {
                                            // loop body
                                            break;
                                        }
                                        break;
                                    }
                                }
                            } else {
                                println("x is greater than 10");
                            }
                        } else {
                            println("x is greater than 10");
                        }
                    };
        """
        expect = "successful"
        self.assertTrue(TestParser.checkParser( input, expect, 240))

    def test_241(self):
        input = "const x = 12 * (5 + 7) - 9 / 3;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 241))

    def test_242(self):
        input = "func myFunc(a int, b float) { return a + b; };"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 242))

    def test_243(self):
        input = "const y = [3]int{1, 2, 3};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 243))

    def test_244(self):
        input = "var arr = [4]float{1.2, 3.4, 5.6, 7.8"
        expect = "Error on line 1 col 38: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 244))

    def test_245(self):
        input = "func invalidFunc(a, b, int c) string { return \"test\"; }"
        expect = "Error on line 1 col 24: int"
        self.assertTrue(TestParser.checkParser(input, expect, 245))

    def test_246(self):
        input = "var result = compute(5, 6) + otherFunc();"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 246))

    def test_247(self):
        input = "const flag = true && false || true;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 247))

    def test_248(self):
        input = "const myArray = [2]bool{true, false, true};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 248))

    def test_249(self):
        input = "func test() { if (x == 5) return 10; else return 20; };"
        expect = "Error on line 1 col 27: return"
        self.assertTrue(TestParser.checkParser(input, expect, 249))

    def test_250(self):
        input = "func test() { while (x < 10) { x = x + 1; } };"
        expect = "Error on line 1 col 30: {"
        self.assertTrue(TestParser.checkParser(input, expect, 250))

    def test_251(self):
        input = """var a === 4"""
        expect = "Error on line 1 col 7: =="
        self.assertTrue(TestParser.checkParser(input, expect, 251))

    def test_252(self):
        input = "var complex = [3][4]int{ {1,2,3,4}, {5,6,7,8}, {9,10,11,12} };"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 252))

    def test_253(self):
        input = "func invalid() { return 5 + ; };"
        expect = "Error on line 1 col 29: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 253))

    def test_254(self):
        input = "const mixed = [2]string{ \"hello\", 123 };"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 254))

    def test_255(self):
        input = "func test() { for i = 0; i < 10; i++ { println(i); } };"
        expect = "Error on line 1 col 21: ="
        self.assertTrue(TestParser.checkParser(input, expect, 255))

    def test_256(self):
        input = "const val = 3.14e-2 + 42.0;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 256))

    def test_257(self):
        input = "func test(a int, b float, c bool { return a + b; }"
        expect = "Error on line 1 col 34: {"
        self.assertTrue(TestParser.checkParser(input, expect, 257))

    def test_258(self):
        input = "var obj = myStruct{field1: 10, field2: 20};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 258))

    def test_259(self):
        input = "func nested() { if (x < 5) { if (y > 2) return x * y; else return y; } else return x; };"
        expect = "Error on line 1 col 41: return"
        self.assertTrue(TestParser.checkParser(input, expect, 259))

    def test_260(self):
        input = "func invalidForLoop() { for var i = 0; i < 10 i++ { println(i); } };"
        expect = "Error on line 1 col 47: i"
        self.assertTrue(TestParser.checkParser(input, expect, 260))

    def test_261(self):
        input = "const pi = 3.14159;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 261))

    def test_262(self):
        input = "var x = [5]int{1,2,3,4,5,6};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 262))

    def test_263(self):
        input = "func greet() { println(\"Hello, world!\"); };"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 263))

    def test_264(self):
        input = "var arr = [3]float{1.5, 2.5, 3.5,};"
        expect = "Error on line 1 col 34: }"
        self.assertTrue(TestParser.checkParser(input, expect, 264))

    def test_265(self):
        input = "const data = Person{name: \"Alice\", age: 25};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 265))

    def test_266(self):
        input = "func testFunc(a int, b string) { return a + b; };"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 266))

    def test_267(self):
        input = "const val = 1_000_000;"
        expect = "Error on line 1 col 14: _000_000"
        self.assertTrue(TestParser.checkParser(input, expect, 267))

    def test_268(self):
        input = "var invalid = [3]string{\"hi\", 42, \"hello\"};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 268))

    def test_269(self):
        input = "func checkEven(n int) bool { return n % 2 == 0; };"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 269))

    def test_270(self):
        input = "func broken() { return (5 + 3 * ; };"
        expect = "Error on line 1 col 33: ;"
        self.assertTrue(TestParser.checkParser(input, expect, 270))

    def test_271(self):
        input = """const myVar = "string without closing"; """
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 271))

    def test_272(self):
        input = "var user = Account{id: 123, balance: 1000.0};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 272))

    def test_273(self):
        input = "func loopExample() { for i = 0; i < 10; i++ println(i); };"
        expect = "Error on line 1 col 28: ="
        self.assertTrue(TestParser.checkParser(input, expect, 273))

    def test_274(self):
        input = """const wrongSyntax = [4]char{"a","b","c"};"""
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 274))

    def test_275(self):
        input = "var nested = Data{key: [2]int{5, 10}, value: 20};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 275))

    def test_276(self):
        input = "func incorrect() { for var i = 0; i < 10 i++ { }; };"
        expect = "Error on line 1 col 42: i"
        self.assertTrue(TestParser.checkParser(input, expect, 276))

    def test_277(self):
        input = "const sum = 4 + 5 * (2 - 3);"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 277))

    def test_278(self):
        input = "func myFunc(x int, y float, z bool) { return x * y + z; };"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 278))

    def test_279(self):
        input = "var matrix = [2][2]int{{1, 2}, {3, 4}};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 279))

    def test_280(self):
        input = "func invalidSyntax() { if x == 5 { return true; } };"
        expect = "Error on line 1 col 27: x"
        self.assertTrue(TestParser.checkParser(input, expect, 280))

    def test_281(self):
        input = "const x = (5 + 3) * 2 - 4 / 2;"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 281))

    def test_282(self):
        input = "var list = [3]bool{true, false, true, false};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 282))

    def test_283(self):
        input = "func add(a int, b int) int { return a + b; };"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 283))

    def test_284(self):
        input = "const invalid = User{name: \"Alice\", age:};"
        expect = "Error on line 1 col 41: }"
        self.assertTrue(TestParser.checkParser(input, expect, 284))

    def test_285(self):
        input = "func divide(a float, b float) float { return a / b; };"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 285))

    def test_286(self):
        input = "var numbers = [5]int{1, 2, 3, 4};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 286))

    def test_287(self):
        input = "func printMsg() { println(\"Hello, world!\" };"
        expect = "Error on line 1 col 43: }"
        self.assertTrue(TestParser.checkParser(input, expect, 287))

    def test_288(self):
        input = "const correct = Person{name: \"John\", age: 30};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 288))

    def test_289(self):
        input = "func loopTest() { for i = 0; i < 5; i++ { println(i); }; }"
        expect = "Error on line 1 col 25: ="
        self.assertTrue(TestParser.checkParser(input, expect, 289))

    def test_290(self):
        input = "const errorTest = [3]string{\"a\", \"b\", 5};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 290))

    def test_291(self):
        input = "var result = calculate(10, 20, 30);"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 291))

    def test_292(self):
        input = "func broken() { return (4 + 5 * ); };"
        expect = "Error on line 1 col 33: )"
        self.assertTrue(TestParser.checkParser(input, expect, 292))

    def test_293(self):
        input = "var sample = [4]int{10, 20, 30, 40};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 293))

    def test_294(self):
        input = "const invalidStruct = Struct{name: \"Test\" age: 25};"
        expect = "Error on line 1 col 43: age"
        self.assertTrue(TestParser.checkParser(input, expect, 294))

    def test_295(self):
        input = "func conditional() { if (x > 10) return; else return; };"
        expect = "Error on line 1 col 34: return"
        self.assertTrue(TestParser.checkParser(input, expect, 295))

    def test_296(self):
        input = """const missingQuote = "This is missing an end quote" """
        expect = "Error on line 1 col 53: <EOF>"
        self.assertTrue(TestParser.checkParser(input, expect, 296))

    def test_297(self):
        input = "var dictionary = Dict{key: \"value\", number: 42};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 297))

    def test_298(self):
        input = "func badSyntax() { while x < 5 { println(x); }; }"
        expect = "Error on line 1 col 26: x"
        self.assertTrue(TestParser.checkParser(input, expect, 298))

    def test_299(self):
        input = "var array = [3][2]int{{1,2}, {3,4}, {5,6}};"
        expect = "successful"
        self.assertTrue(TestParser.checkParser(input, expect, 299))

    def test_300(self):
        input = "func missingBracket() { for i = 0; i < 5; i++ println(i) };"
        expect = "Error on line 1 col 31: ="
        self.assertTrue(TestParser.checkParser(input, expect, 300))
