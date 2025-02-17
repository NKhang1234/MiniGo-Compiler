import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
#------------------------------------------PROVIDED TEST -------------------------------------------------------------
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",110))
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?sVN","ab,ErrorToken ?",111))
    def test_keyword_var(self):
        """test keyword var"""
        self.assertTrue(TestLexer.checkLexeme("var abc int ;","var,abc,int,;,<EOF>",112))
    def test_keyword_func(self):
        """test keyword func"""
        self.assertTrue(TestLexer.checkLexeme("""func abc ( ) ""","""func,abc,(,),<EOF>""",113))
    def test_Phuc(self):
        """test keyword func"""
        self.assertTrue(TestLexer.checkLexeme("""/*level1 /*lv2 /*lv3 */*/*/ code /*ff*/""","""code,<EOF>""",1000))
#------------------------------------------MYSELF TEST -------------------------------------------------------------
    def test_01(self):
        """test keyword"""
        self.assertTrue(TestLexer.checkLexeme("""if else for return func type struct interface string int float boolean const var continue break range nil true false""",
                                                """if,else,for,return,func,type,struct,interface,string,int,float,boolean,const,var,continue,break,range,nil,true,false,<EOF>""",1))
    def test_02(self):
        """ test int literal """
        self.assertTrue(TestLexer.checkLexeme("1234 0b11 0B11 0o11 0O11 0x11 0X11","1234,0b11,0B11,0o11,0O11,0x11,0X11,<EOF>",2))
    def test_03(self):
        """ test int literal """
        self.assertTrue(TestLexer.checkLexeme("3.14 0. 2.0e10","3.14,0.,2.0e10,<EOF>",3))
    def test_04(self):
        """ test string literal """
        self.assertTrue(TestLexer.checkLexeme(""" "hello world" """,""""hello world",<EOF>""",4))
    def test_05(self):
        """ test string with tab escape literal """
        self.assertTrue(TestLexer.checkLexeme(""" "newline\t" """,""""newline\t",<EOF>""",5))
    def test_06(self):
        """ test inline comment """
        self.assertTrue(TestLexer.checkLexeme("""//hahaha
        hihi""","hihi,<EOF>",6))
    def test_07(self):
        """ test block comment """
        self.assertTrue(TestLexer.checkLexeme(""" /* haha /*ddd*/ gggg
        hohooh*/""","<EOF>",7))
    def test_08(self):
        """ test illegal escape """
        self.assertTrue(TestLexer.checkLexeme(""" "Hello \\s " ""","""Illegal escape in string: "Hello \\s""",8))
    
    def test_09(self):
        input = """var b c = z"""
        expect = "var,b,c,=,z,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 9))

    def test_10(self):
        input = "a += 1; b -= 2; c %= 3"
        expect = "a,+=,1,;,b,-=,2,;,c,%=,3,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 10))

    def test_11(self):
        input = "if(a>23) { };"
        expect = "if,(,a,>,23,),{,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 11))

    def test_12(self):
        input = "func Func fUnc fuNce"
        expect = "func,Func,fUnc,fuNce,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 12))
    
    def test_13(self):
        input = """
            type Sharp interface {
                Add(x, y int) int
                Multiply(a, b float64, c int) (result float64)
                Clear()
                Display(model string) string
            }"""
        expect = "type,Sharp,interface,{,Add,(,x,,,y,int,),int,;,Multiply,(,a,,,b,float64,,,c,int,),(,result,float64,),;,Clear,(,),;,Display,(,model,string,),string,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 13))
    
    def test_14(self):
        input = "func,hello,(,1,-,2,+,3,-,4,),{,var,a,=,1,;,}"
        output = "func,,,hello,,,(,,,1,,,-,,,2,,,+,,,3,,,-,,,4,,,),,,{,,,var,,,a,,,=,,,1,,,;,,,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, output, 14))
    
    def test_15(self):
        input = "haha = nil "
        expect = "haha,=,nil,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 15))

    def test_16(self):
        input = """ for z < 2 { i += 1 }"""
        expect = "for,z,<,2,{,i,+=,1,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 16))
    
    def test_17(self):
        input = "func haha hoho hehe"
        expect = "func,haha,hoho,hehe,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 17))

    def test_18(self):
        input = """
                for var bb [5]int = [5]int{1.1, 2.2, 3.3, 4.4, 5.5}; bar().x.y(); z := 10 {
                    // loop body
                }
        """
        expect = "for,var,bb,[,5,],int,=,[,5,],int,{,1.1,,,2.2,,,3.3,,,4.4,,,5.5,},;,bar,(,),.,x,.,y,(,),;,z,:=,10,{,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 18))
    
    def test_19(self):
        input = "2+3-4%5*6-7+(3-4)"
        expect = "2,+,3,-,4,%,5,*,6,-,7,+,(,3,-,4,),<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 19))

    def test_20(self):
        input = "01.27  02.e348  00.99e05"
        expect = "01.27,02.e348,00.99e05,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 20))

    def test_21(self):
        input = "0b1234"
        expect = "0b1,234,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 21))

    def test_22(self):
        input = "x -= val; y ++= 12; z --= 89"
        expect = "x,-=,val,;,y,+,+=,12,;,z,-,-=,89,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 22))

    def test_23(self):
        input = "0xABCD"
        expect = "0xABCD,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 23))

    def test_24(self):
        input = "const f "
        expect = "const,f,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 24))

    def test_25(self):
        input = """ for pos, num := range numbers { }"""
        expect = "for,pos,,,num,:=,range,numbers,{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 25))

    def test_26(self):
        input = "const result = obj.method(34) / arr[5] "
        expect = "const,result,=,obj,.,method,(,34,),/,arr,[,5,],<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 26))

    def test_27(self):
        input = """var name string; type Device struct{}; type Device struct {}; var price float64;"""
        expect = "var,name,string,;,type,Device,struct,{,},;,type,Device,struct,{,},;,var,price,float64,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 27))

    def test_28(self):
        input = "1234 -123450 +12345"
        expect = "1234,-,123450,+,12345,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 28))

    def test_29(self):
        input = "{ { } } ( ( ) ) [ [ ] ],;"
        expect = "{,{,},},(,(,),),[,[,],],,,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 29))

    def test_30(self):
        input = "{return 404 error} "
        expect = "{,return,404,error,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 30))

    def test_31(self):
        input = """ if (x % 2) { var i -= 2;} """
        expect = "if,(,x,%,2,),{,var,i,-=,2,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 31))

    def test_32(self):
        input = """ "This "is" a sample string" """
        expect = """"This ",is," a sample string",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 32))

    def test_33(self):
        input = "var hehehe"
        expect = "var,hehehe,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 33))

    def test_34(self):
        input = "p - q <= r || !(p / r > q) && p != r || q == r "
        expect = "p,-,q,<=,r,||,!,(,p,/,r,>,q,),&&,p,!=,r,||,q,==,r,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 34))

    def test_35(self):
        input = """ func hoho() {  
                    y := foo() * 8 - 2  
                    y.d[5][2] = 3 + 4  
                } """
        expect = "func,hoho,(,),{,y,:=,foo,(,),*,8,-,2,;,y,.,d,[,5,],[,2,],=,3,+,4,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 35))

    def test_36(self):
        input = """ "This \\a is \\a string with illegal escape" """
        expect = """Illegal escape in string: "This \\a"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 36))

    def test_37(self):
        input = "0.6543,."
        expect = "0.6543,,,.,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 37))

    def test_38(self):
        input = "e2 e-3 e+7"
        expect = "e2,e,-,3,e,+,7,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 38))

    def test_39(self):
        input = "main+-*/23"
        expect = "main,+,-,*,/,23,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 39))
    
    def test_40(self):
        input = """
            func foo() {  
                var x int  
                const value = a.b() - 10  
            } """
        expect = "func,foo,(,),{,var,x,int,;,const,value,=,a,.,b,(,),-,10,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 40))
    
    def test_41(self):
        input = "0o2323238"
        expect = "0o232323,8,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 41))
    
    def test_42(self):
        input = "0x0ABC 0x0123"
        expect = "0x0ABC,0x0123,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 42))

    def test_43(self):
        input = """ "aaaa 123" """
        expect = """\"aaaa 123\",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 43))
    
    def test_44(self):
        input = "0xA1B2  0xA1b2  0xA1B2"
        expect = "0xA1B2,0xA1b2,0xA1B2,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 44))

    def test_45(self):
        input = """ "This \\s is \\s string with illegal escape" """
        expect = """Illegal escape in string: "This \s"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 45))

    def test_46(self):
        input = """ // inline comment"""
        expect = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 46))

    def test_47(self):
        input = """ /*This is outer comment
                        /* This is nest comment*/
                    This is outer comment*/ main """
        expect = "main,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 47))

    def test_48(self):
        input = "[]]]'hehehe'"
        expect = "[,],],],ErrorToken '"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 48))

    def test_49(self):
        input = "m_ain mai_n ma_in"
        expect = "m_ain,mai_n,ma_in,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 49))

    def test_50(self):
        input = "const PQ = generate()[3] + items[1].z.w"
        expect = "const,PQ,=,generate,(,),[,3,],+,items,[,1,],.,z,.,w,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 50))
        
    def test_51(self):
        input = """ "This is a string  without closing"""
        expect = """Unclosed string: "This is a string  without closing"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 51))

    def test_52(self):
        input = """ "This is a string with escaped: \t """
        expect = """Unclosed string: "This is a string with escaped: 	 """
        self.assertTrue(TestLexer.checkLexeme(input, expect, 52))

    def test_53(self):
        input = """
            func calculate(x int, y string) string {}  
            func transform() [5][7] StructType {}  
            func analyze() {run();}
        """
        expect = "func,calculate,(,x,int,,,y,string,),string,{,},;,func,transform,(,),[,5,],[,7,],StructType,{,},;,func,analyze,(,),{,run,(,),;,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 53))

    def test_54(self):
        input = "for i in range foods { i -= 2;} "
        expect = "for,i,in,range,foods,{,i,-=,2,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 54))

    def test_55(self):
        input = "5435.32432 43432.223"
        expect = "5435.32432,43432.223,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 55))

    def test_56(self):
        input = """
            var a float64 = compute() - 3 * 2  
            var b = "hello" + "world"  
            var c bool  
            var d char = getValue() % 5  
            var e = myFunc() * 10  
            var f myType
        """
        expect = """var,a,float64,=,compute,(,),-,3,*,2,;,var,b,=,"hello",+,"world",;,var,c,bool,;,var,d,char,=,getValue,(,),%,5,;,var,e,=,myFunc,(,),*,10,;,var,f,myType,;,<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 56))

    def test_57(self):
        input = """ "This \" ? is strange token" """
        expect = "\"This \",ErrorToken ?"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 57))

    def test_58(self):
        input = "0b0101 0B0011"
        expect = "0b0101,0B0011,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 58))
    
    def test_59(self):
        input = """
            func (p Processor) execute() Data {}  
            func (p Processor) execute(x string, y [5]Task) {} 
        """
        expect = "func,(,p,Processor,),execute,(,),Data,{,},;,func,(,p,Processor,),execute,(,x,string,,,y,[,5,],Task,),{,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 59))

    def test_60(self):
        input = "const AB = [4][2]float{3.14, 2.71} "
        expect = "const,AB,=,[,4,],[,2,],float,{,3.14,,,2.71,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 60))

    def test_61(self):
        input = "123 0x1A3F 0XABC"
        expect = "123,0x1A3F,0XABC,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 61))

    def test_62(self):
        input = "3.14 2e10 1.23E-4"
        expect = "3.14,2,e10,1.23E-4,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 62))

    def test_63(self):
        input = "'a' 'Z' '\\n'"
        expect = "ErrorToken '"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 63))

    def test_64(self):
        input = "\"Hello, world!\" \"String with \\\" escape\""
        expect = "\"Hello, world!\",\"String with \\\" escape\",<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 64))

    def test_65(self):
        input = "true false nil"
        expect = "true,false,nil,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 65))

    def test_66(self):
        input = "if (x < 10) { return x; }"
        expect = "if,(,x,<,10,),{,return,x,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 66))

    def test_67(self):
        input = "while (y > 0) y = y - 1;"
        expect = "while,(,y,>,0,),y,=,y,-,1,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 67))

    def test_68(self):
        input = "for i in 1..10 { print(i); }"
        expect = "for,i,in,1.,.,10,{,print,(,i,),;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 68))

    def test_69(self):
        input = "arr[5] = 42;"
        expect = "arr,[,5,],=,42,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 69))

    def test_70(self):
        input = "func foo() int { return 5; }"
        expect = "func,foo,(,),int,{,return,5,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 70))

    def test_71(self):
        input = "class MyClass { var x: int; }"
        expect = "class,MyClass,{,var,x,:,int,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 71))

    def test_72(self):
        input = "x = y ? 10 : 20;"
        expect = "x,=,y,ErrorToken ?"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 72))

    def test_73(self):
        input = "& | ^ ~ << >>"
        expect = "ErrorToken &"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 73))

    def test_74(self):
        input = "0b1101 0B1010"
        expect = "0b1101,0B1010,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 74))

    def test_75(self):
        input = "// This is a comment"
        expect = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 75))

    def test_76(self):
        input = "/* Multi-line \n comment */"
        expect = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 76))

    def test_77(self):
        input = "var a, b = 10, 20;"
        expect = "var,a,,,b,=,10,,,20,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 77))

    def test_78(self):
        input = "const PI = 3.14159;"
        expect = "const,PI,=,3.14159,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 78))

    def test_79(self):
        input = "switch(x) { case 1: break; }"
        expect = "switch,(,x,),{,case,1,:,break,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 79))

    def test_80(self):
        input = "try { riskyCode(); } catch (e) { handleError(e); }"
        expect = "try,{,riskyCode,(,),;,},catch,(,e,),{,handleError,(,e,),;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 80))

    def test_81(self):
        input = "func sum(a int, b int) int { return a + b; }"
        expect = "func,sum,(,a,int,,,b,int,),int,{,return,a,+,b,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 81))

    def test_82(self):
        input = "var x = 5 > 3 && 10 <= 20;"
        expect = "var,x,=,5,>,3,&&,10,<=,20,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 82))

    def test_83(self):
        input = "arr[10] = arr[5] + arr[2];"
        expect = "arr,[,10,],=,arr,[,5,],+,arr,[,2,],;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 83))

    def test_84(self):
        input = "\"String with newline \\n and tab \\t\""
        expect = "\"String with newline \\n and tab \\t\",<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 84))

    def test_85(self):
        input = "do { x++; } while (x < 100);"
        expect = "do,{,x,+,+,;,},while,(,x,<,100,),;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 85))

    def test_86(self):
        input = "return funcCall(a, b, c);"
        expect = "return,funcCall,(,a,,,b,,,c,),;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 86))

    def test_87(self):
        input = "struct Point { x, y int }"
        expect = "struct,Point,{,x,,,y,int,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 87))

    def test_88(self):
        input = "interface Shape { area() float64 }"
        expect = "interface,Shape,{,area,(,),float64,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 88))

    def test_89(self):
        input = "package main; import \"fmt\""
        expect = "package,main,;,import,\"fmt\",<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 89))

    def test_90(self):
        input = "var set map[string]int"
        expect = "var,set,map,[,string,],int,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 90))

    def test_91(self):
        input = "chan <- message"
        expect = "chan,<,-,message,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 91))

    def test_92(self):
        input = "select { case x <- ch: break; }"
        expect = "select,{,case,x,<,-,ch,:,break,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 92))

    def test_93(self):
        input = "defer cleanup()"
        expect = "defer,cleanup,(,),<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 93))

    def test_94(self):
        input = "go startProcess()"
        expect = "go,startProcess,(,),<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 94))

    def test_95(self):
        input = "const MAX_SIZE = 1000;"
        expect = "const,MAX_SIZE,=,1000,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 95))

    def test_96(self):
        input = "`Raw string literal with `backticks` included`"
        expect = "ErrorToken `"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 96))

    def test_97(self):
        input = "0xABCD 0X1234 0xab12"
        expect = "0xABCD,0X1234,0xab12,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 97))

    def test_98(self):
        input = "switch mode { case 'A': actionA(); case 'B': actionB(); default: exit(); }"
        expect = "switch,mode,{,case,ErrorToken '"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 98))

    def test_99(self):
        input = """ "Unterminated string\n """
        expect = """Unclosed string: "Unterminated string"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 99))

    def test_100(self):
        input = "func (p Processor) Execute() int { return p.data * 2; }"
        expect = "func,(,p,Processor,),Execute,(,),int,{,return,p,.,data,*,2,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 100))



    

    

    
   


