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
        self.assertTrue(TestLexer.checkLexeme(""" "Hello \s " ""","""Illegal escape in string: "Hello \s""",8))
    
    def test_09(self):
        input = """ var h nhatKhang = c{7, 1};"""
        expect = "var,h,nhatKhang,=,c,{,7,,,1,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 9))

    def test_10(self):
        input = "b %= 5; f -= 6; z += 9"
        expect = "b,%=,5,;,f,-=,6,;,z,+=,9,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 10))

    def test_11(self):
        input = "(false) {body}(true) {body} "
        expect = "(,false,),{,body,},(,true,),{,body,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 11))

    def test_12(self):
        input = "mAin MaIN MAIN"
        expect = "mAin,MaIN,MAIN,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 12))
    
    def test_13(self):
        input = """
            type Casio interface {
                Sub(x, y int) int;
                Subtract(a, b float, c int) [9]array;
                Reset()
                Show(name string);
            }"""
        expect = "type,Casio,interface,{,Sub,(,x,,,y,int,),int,;,Subtract,(,a,,,b,float,,,c,int,),[,9,],array,;,Reset,(,),;,Show,(,name,string,),;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 13))
    
    def test_14(self):
        self.assertTrue(TestLexer.checkLexeme(
            """func abc ( ) { }""", """func,abc,(,),{,},<EOF>""", 14))
    
    def test_15(self):
        input = "z = nil "
        expect = "z,=,nil,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 15))

    def test_16(self):
        input = """ for i >= 24 { body }"""
        expect = "for,i,>=,24,{,body,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 16))
    
    def test_17(self):
        input = "func haha "
        expect = "func,haha,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 17))

    def test_18(self):
        input = """
                    for var aa [7]int = 0; foo().a.b(); a := 6 {
                        // loop body
                    }
        """
        expect = "for,var,aa,[,7,],int,=,0,;,foo,(,),.,a,.,b,(,),;,a,:=,6,{,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 18))
    
    def test_19(self):
        input = "7+9-9/4/7-3++8-+6"
        expect = "7,+,9,-,9,/,4,/,7,-,3,+,+,8,-,+,6,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 19))

    def test_20(self):
        input = "00.34 00.e065 00.00e00"
        expect = "00.34,00.e065,00.00e00,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 20))

    def test_21(self):
        input = "0b320"
        expect = "0,b320,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 21))

    def test_22(self):
        input = "d -= op; i ++= 65; r --= 43 "
        expect = "d,-=,op,;,i,+,+=,65,;,r,-,-=,43,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 22))

    def test_23(self):
        input = "0xABG"
        expect = "0xAB,G,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 23))

    def test_24(self):
        input = "const a "
        expect = "const,a,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 24))

    def test_25(self):
        input = """ for index, value := range array { }"""
        expect = "for,index,,,value,:=,range,array,{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 25))

    def test_26(self):
        input = "const sd = ca.main(54) - d.e[43];"
        expect = "const,sd,=,ca,.,main,(,54,),-,d,.,e,[,43,],;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 178))

    def test_27(self):
        input = """ var c string; type Casio struct{} type Casio struct {} var f float;"""
        expect = "var,c,string,;,type,Casio,struct,{,},type,Casio,struct,{,},var,f,float,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 27))

    def test_28(self):
        input = "12433 -474530 +994327"
        expect = "12433,-,474530,+,994327,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 28))

    def test_29(self):
        input = "()[]{},;"
        expect = "(,),[,],{,},,,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 29))

    def test_30(self):
        input = "{return 404} "
        expect = "{,return,404,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 30))

    def test_31(self):
        input = """ if (x <= 10) { } """
        expect = "if,(,x,<=,10,),{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 31))

    def test_32(self):
        input = """ "This \" is \" string" """
        expect = "\"This \",is,\" string\",<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 32))

    def test_33(self):
        input = "var dfg"
        expect = "var,dfg,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 33))

    def test_34(self):
        input = "a - c < b && !(a - b > c) || a != b && a != c"
        expect = "a,-,c,<,b,&&,!,(,a,-,b,>,c,),||,a,!=,b,&&,a,!=,c,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 119))

    def test_35(self):
        input = """ func nhatKhang() {
                x  := haha() + 6 / 3;
                x.c[7][4] := 1 - 2;
            }"""
        expect = "func,nhatKhang,(,),{,x,:=,haha,(,),+,6,/,3,;,x,.,c,[,7,],[,4,],:=,1,-,2,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 35))

    def test_36(self):
        input = """ "This \\f is \\f string" """
        expect = "Illegal escape in string: \"This \\f"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 36))

    def test_37(self):
        input = "0. 45."
        expect = "0.,45.,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 37))

    def test_38(self):
        input = "e5 e+5 e-5"
        expect = "e5,e,+,5,e,-,5,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 38))

    def test_39(self):
        input = "main*23"
        expect = "main,*,23,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 39))
    
    def test_40(self):
        input = """
            func haha() {
                var z str;
                const ooo = c.d() + 5;
            }"""
        expect = "func,haha,(,),{,var,z,str,;,const,ooo,=,c,.,d,(,),+,5,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 184))
    
    def test_41(self):
        input = "0o239"
        expect = "0o23,9,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 41))
    
    def test_42(self):
        input = "0x000 0x0034"
        expect = "0x000,0x0034,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 42))

    def test_43(self):
        input = """ "hello 123" """
        expect = """\"hello 123\",<EOF>"""
        self.assertTrue(TestLexer.checkLexeme(input, expect, 43))
    
    def test_44(self):
        input = "0x12ab 0x12AB 0x12Ab"
        expect = "0x12ab,0x12AB,0x12Ab,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 44))

    def test_45(self):
        input = """ "This \\ is \\ string" """
        expect = "Illegal escape in string: \"This \ "
        self.assertTrue(TestLexer.checkLexeme(input, expect, 45))

    def test_46(self):
        input = """ // This is a comment main"""
        expect = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 46))

    def test_47(self):
        input = """ /*This is global comment
                        /* This is nest comment*/
                    This is global comment*/ main """
        expect = "main,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 47))

    def test_48(self):
        input = "()''[]"
        expect = "(,),ErrorToken '"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 48))

    def test_49(self):
        input = "_main ma_in"
        expect = "_main,ma_in,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 49))

    def test_50(self):
        input = "const MN = main()[0] + bc[2].b.b;"
        expect = "const,MN,=,main,(,),[,0,],+,bc,[,2,],.,b,.,b,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 50))
        
    def test_51(self):
        input = """ "This is a string  """
        expect = "Unclosed string: \"This is a string  "
        self.assertTrue(TestLexer.checkLexeme(input, expect, 51))

    def test_52(self):
        input = """ "This is a string with escaped: \\n \\t \\r \\\" \\\\" """
        expect = "\"This is a string with escaped: \\n \\t \\r \\\" \\\\\",<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 52))

    def test_53(self):
        input = """
            func main(x int, y int) int {}
            func main1() [2][6] ID {}
            func main2() {abc;}
        """
        expect = "func,main,(,x,int,,,y,int,),int,{,},;,func,main1,(,),[,2,],[,6,],ID,{,},;,func,main2,(,),{,abc,;,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 53))

    def test_54(self):
        input = "range array(){} "
        expect = "range,array,(,),{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 54))

    def test_55(self):
        input = "3.14 5.12"
        expect = "3.14,5.12,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 55))

    def test_56(self):
        input = """
            var x int = main() + 4 / 4;
            var y = "abc" / 4;
            var z str;
        """
        expect = "var,x,int,=,main,(,),+,4,/,4,;,var,y,=,\"abc\",/,4,;,var,z,str,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 56))

    def test_57(self):
        input = """ "This \" ?# \" string" """
        expect = "\"This \",ErrorToken ?"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 57))

    def test_58(self):
        input = "0b110 0B1011"
        expect = "0b110,0B1011,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 58))
    
    def test_59(self):
        input = """
            func (c Calculator) nhat() ID {}
            func (c Calculator) nhat(x float, y [2]nhat) {}
        """
        expect = "func,(,c,Calculator,),nhat,(,),ID,{,},;,func,(,c,Calculator,),nhat,(,x,float,,,y,[,2,],nhat,),{,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 59))

    def test_60(self):
        input = "const MN = [5][0]string{1, \"string\"};"
        expect = "const,MN,=,[,5,],[,0,],string,{,1,,,\"string\",},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 60))

    def test_61(self):
        input = "2.0e10 2.0e+10 2.0e-10"
        expect = "2.0e10,2.0e+10,2.0e-10,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 61))
    
    def test_62(self):
        input = "0x123 0X123"
        expect = "0x123,0X123,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 62))

    def test_63(self):
        input = "main23"
        expect = "main23,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 63))

    def test_64(self):
        input = "23main"
        expect = "23,main,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 64))

    def test_65(self):
        input = "a := c; a += 3; b -= c;"
        expect = "a,:=,c,;,a,+=,3,;,b,-=,c,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 65))

    def test_66(self):
        input = "0o975"
        expect = "0,o975,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 66))

    def test_67(self):
        input = "const MN = 1 || 2 && c"
        expect = "const,MN,=,1,||,2,&&,c,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 67))

    def test_68(self):
        input = "0o0000 0o0046"
        expect = "0o0000,0o0046,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 68))

    def test_69(self):
        input = "{break;} "
        expect = "{,break,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 69))

    def test_70(self):
        input = "int float string boolean "
        expect = "int,float,string,boolean,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 70))

    def test_71(self):
        input = """
                func Add() {
                    return (2 + 3).b
                    return -1.c
                }"""
        expect = "func,Add,(,),{,return,(,2,+,3,),.,b,;,return,-,1.,c,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 71))

    def test_72(self):
        input = "0b108"
        expect = "0b10,8,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 72))

    def test_73(self):
        input = """
                if (x.foo().b[2])
                {
                    if (){}
                }"""
        expect = "if,(,x,.,foo,(,),.,b,[,2,],),;,{,if,(,),{,},;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 73))

    def test_74(self):
        input = """ //This is first comment
                    //This is second comment
                    main
                """
        expect = "main,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 74))

    def test_75(self):
        input = "0 012 0046"
        expect = "0,0,12,0,0,46,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 75))

    def test_76(self):
        input = "10e5"
        expect = "10,e5,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 76))

    def test_77(self):
        input = """ if (x > 10) {

                } else if (x == 10) {
                    var z str;
                } else {
                    var z ID;
                }"""
        expect = "if,(,x,>,10,),{,},else,if,(,x,==,10,),{,var,z,str,;,},else,{,var,z,ID,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 77))

    def test_78(self):
        input = """ "This \' #? \' string" """
        expect = "\"This ' #? ' string\",<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 78))

    def test_79(self):
        input = "const MN = Person{}"
        expect = "const,MN,=,Person,{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 79))

    def test_80(self):
        input = "for()"
        expect = "for,(,),<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 80))

    def test_81(self):
        input = "10.e5"
        expect = "10.e5,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 81))

    def test_82(self):
        self.assertTrue(TestLexer.checkLexeme(
            "ab?sVN", "ab,ErrorToken ?", 82))

    def test_83(self):
        input = """
                    if (1) {}
                    else if(2) {return string}
                    else if(3) {reutrn int;}"""
        expect = "if,(,1,),{,},;,else,if,(,2,),{,return,string,},;,else,if,(,3,),{,reutrn,int,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 83))

    def test_84(self):
        input = """ /* Multi line comment
                    This is first comment
                    This is second comment */
                """
        expect = "<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 84))

    def test_85(self):
        input = "a ** b ; a ^ b;"
        expect = "a,*,*,b,;,a,ErrorToken ^"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 85))

    def test_86(self):
        input = """ "This is 
                    a string"  """
        expect = "Unclosed string: \"This is "
        self.assertTrue(TestLexer.checkLexeme(input, expect, 86))

    def test_87(self):
        input = "0o123 0O456"
        expect = "0o123,0O456,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 87))

    def test_88(self):
        input = "0b000 0b011 0b0010"
        expect = "0b000,0b011,0b0010,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 88))

    def test_89(self):
        input = ".15 .e20"
        expect = ".,15,.,e20,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 89))

    def test_90(self):
        input = """ "This is a string \n"  """
        expect = "Unclosed string: \"This is a string "
        self.assertTrue(TestLexer.checkLexeme(input, expect, 90))

    def test_91(self):
        input = """
                    func Add() {
                        a += 2;
                        a /= 2
                        a *= 2
                        a %= 2;
                        return a
                    }"""
        expect = "func,Add,(,),{,a,+=,2,;,a,/=,2,;,a,*=,2,;,a,%=,2,;,return,a,;,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 91))

    def test_92(self):
        input = "20.0e12.3"
        expect = "20.0e12,.,3,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 92))

    def test_93(self):
        input = "+30.12 -30.12"
        expect = "+,30.12,-,30.12,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 93))

    def test_94(self):
        input = """
            type nhatKhang struct {
                nhatKhang string ;
                nhatKhang [5][4]array ;
            }
            """
        expect = "type,nhatKhang,struct,{,nhatKhang,string,;,nhatKhang,[,5,],[,4,],array,;,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 94))

    def test_95(self):
        input = """ /*This is multi
                    line comment*/ multi
                // This is single line comment
                single
                """
        expect = "multi,;,single,;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 95))

    def test_96(self):
        input = "type Person struct"
        expect = "type,Person,struct,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 96))

    def test_97(self):
        input = "if () {} else if () {} else"
        expect = "if,(,),{,},else,if,(,),{,},else,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 97))

    def test_98(self):
        self.assertTrue(TestLexer.checkLexeme("abc", "abc,<EOF>", 98))

    def test_99(self):
        input = """func main() {};"""
        expect = "func,main,(,),{,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 99))

    def test_100(self):
        input = "a.b == 3 || c === d || c +== a || b -=== a"
        expect = "a,.,b,==,3,||,c,==,=,d,||,c,+=,=,a,||,b,-=,==,a,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 100))

    def test_101(self):
        input = """ for i := 0; i < 10; i += 1 { } """
        expect = "for,i,:=,0,;,i,<,10,;,i,+=,1,{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 101))

    def test_102(self):
        input = """ a[2+3&&2] += foo().b[2];"""
        expect = "a,[,2,+,3,&&,2,],+=,foo,(,),.,b,[,2,],;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 102))

    def test_103(self):
        input = """pham \t ba \r nhat \f khang"""
        expect = "pham,ba,nhat,khang,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 103))

    def test_104(self):
        input = "type Calculator interface"
        expect = "type,Calculator,interface,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 104))

    def test_105(self):
        input = """func foo () {
        };"""
        expect = "func,foo,(,),{,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 105))

    def test_106(self):
        input = """ for var i = 0; i < 10; i += 1 {
                        // loop body
                    }"""
        expect = "for,var,i,=,0,;,i,<,10,;,i,+=,1,{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 106))

    def test_107(self):
        self.assertTrue(TestLexer.checkLexeme(
            "var abc int ;", "var,abc,int,;,<EOF>", 107))

    def test_108(self):
        input = "{continue}; "
        expect = "{,continue,},;,<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 108))

    def test_109(self):
        input = """if () {}"""
        expect = "if,(,),{,},<EOF>"
        self.assertTrue(TestLexer.checkLexeme(input, expect, 109))

    

    

    
   


