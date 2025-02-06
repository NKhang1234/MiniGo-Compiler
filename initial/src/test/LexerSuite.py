import unittest
from TestUtils import TestLexer

class LexerSuite(unittest.TestCase):
#------------------------------------------MYSELF TEST -------------------------------------------------------------
    def test_01(self):
        """test keyword"""
        self.assertTrue(TestLexer.checkLexeme("""if else for return func type struct interface string int float boolean const var continue break range nil true false""",
                                                """if,else,for,return,func,type,struct,interface,string,int,float,boolean,const,var,continue,break,range,nil,true,false,<EOF>""",1))
    def test_02(self):
        """ test int literal """
        self.assertTrue(TestLexer.checkLexeme("1234 0b11 0B11 0o11 0O11 0x11 0X11","1234,3,3,9,9,17,17,<EOF>",2))
    def test_03(self):
        """ test int literal """
        self.assertTrue(TestLexer.checkLexeme("3.14 0. 2.0e10","3.14,0.,2.0e10,<EOF>",3))
    def test_04(self):
        """ test string literal """
        self.assertTrue(TestLexer.checkLexeme("\"hello\\\"World\" \"123\"","hello\\\"World,123,<EOF>",4))
    def test_05(self):
        """ test string with tab escape literal """
        self.assertTrue(TestLexer.checkLexeme("""\"newline\t\"""","newline\t,<EOF>",5))
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
        self.assertTrue(TestLexer.checkLexeme(""" "Hello \s " ""","Illegal escape in string: Hello \s",8))
#------------------------------------------PROVIDED TEST -------------------------------------------------------------
    def test_lower_identifier(self):
        """test identifiers"""
        self.assertTrue(TestLexer.checkLexeme("abc","abc,<EOF>",50))
    def test_wrong_token(self):
        self.assertTrue(TestLexer.checkLexeme("ab?sVN","ab,ErrorToken ?",51))
    def test_keyword_var(self):
        """test keyword var"""
        self.assertTrue(TestLexer.checkLexeme("var abc int ;","var,abc,int,;,<EOF>",52))
    def test_keyword_func(self):
        """test keyword func"""
        self.assertTrue(TestLexer.checkLexeme("""func abc ( ) ""","""func,abc,(,),<EOF>""",53))
#------------------------------------------ Problem TEST -------------------------------------------------------------

    def test_007(self):
        """Literals FLOAT"""
        self.assertTrue(TestLexer.checkLexeme("12.e-8","12.e-8,<EOF>", 107))
    
    def test_010(self):
        """COMEMENTS"""
        self.assertTrue(TestLexer.checkLexeme("/* VO /* /*TIEN*/ */ SHIBA","SHIBA,<EOF>", 110))


