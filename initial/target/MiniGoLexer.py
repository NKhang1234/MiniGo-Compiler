# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO

 
from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u0212\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\3\2")
        buf.write("\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\37\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3&\3&\3&\3\'\3\'\3")
        buf.write("\'\3(\3(\3(\3)\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3-\3-\3.")
        buf.write("\3.\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64")
        buf.write("\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\58\u015f\n8")
        buf.write("\38\38\38\78\u0164\n8\f8\168\u0167\138\39\39\39\39\59")
        buf.write("\u016d\n9\3:\3:\3:\7:\u0172\n:\f:\16:\u0175\13:\5:\u0177")
        buf.write("\n:\3;\3;\3;\6;\u017c\n;\r;\16;\u017d\3<\3<\3<\6<\u0183")
        buf.write("\n<\r<\16<\u0184\3=\3=\3=\6=\u018a\n=\r=\16=\u018b\3>")
        buf.write("\3>\5>\u0190\n>\3?\6?\u0193\n?\r?\16?\u0194\3?\3?\7?\u0199")
        buf.write("\n?\f?\16?\u019c\13?\3@\6@\u019f\n@\r@\16@\u01a0\3@\3")
        buf.write("@\7@\u01a5\n@\f@\16@\u01a8\13@\3@\3@\5@\u01ac\n@\3@\6")
        buf.write("@\u01af\n@\r@\16@\u01b0\3A\3A\3A\7A\u01b6\nA\fA\16A\u01b9")
        buf.write("\13A\3A\3A\3A\3B\3B\3C\3C\3C\3C\3C\3C\3C\3C\3C\3C\5C\u01ca")
        buf.write("\nC\3D\3D\3D\3D\7D\u01d0\nD\fD\16D\u01d3\13D\3D\5D\u01d6")
        buf.write("\nD\3D\3D\3E\3E\3E\3E\3E\7E\u01df\nE\fE\16E\u01e2\13E")
        buf.write("\3E\3E\3E\3E\3E\3F\3F\3F\3G\6G\u01ed\nG\rG\16G\u01ee\3")
        buf.write("G\3G\3H\3H\3H\3I\3I\3I\7I\u01f9\nI\fI\16I\u01fc\13I\3")
        buf.write("I\3I\3I\3J\3J\3J\7J\u0204\nJ\fJ\16J\u0207\13J\3J\3J\3")
        buf.write("J\3J\5J\u020d\nJ\3J\3J\3K\3K\2\2L\3\3\5\4\7\5\t\6\13\7")
        buf.write("\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21")
        buf.write("!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67")
        buf.write("\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61")
        buf.write("a\62c\63e\64g\65i\66k\2m\2o\67q8s\2u\2w\2y\2{9}\2\177")
        buf.write("\2\u0081:\u0083\2\u0085\2\u0087;\u0089<\u008b=\u008d>")
        buf.write("\u008f\2\u0091?\u0093@\u0095A\3\2\23\4\2C\\c|\3\2\62;")
        buf.write("\3\2\63;\4\2DDdd\3\2\62\63\4\2QQqq\3\2\629\4\2ZZzz\5\2")
        buf.write("\62;CHch\4\2GGgg\4\2--//\5\2\f\f$$^^\3\2\f\f\3\3\f\f\4")
        buf.write("\2,,\61\61\5\2\13\13\16\17\"\"\7\2$$^^ppttvv\2\u0229\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2{\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2")
        buf.write("\2\2\u008d\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\3\u0097\3\2\2\2\5\u0099\3\2\2\2\7\u009c\3\2\2")
        buf.write("\2\t\u00a1\3\2\2\2\13\u00a5\3\2\2\2\r\u00ac\3\2\2\2\17")
        buf.write("\u00b1\3\2\2\2\21\u00b6\3\2\2\2\23\u00bd\3\2\2\2\25\u00c7")
        buf.write("\3\2\2\2\27\u00ce\3\2\2\2\31\u00d2\3\2\2\2\33\u00d8\3")
        buf.write("\2\2\2\35\u00e0\3\2\2\2\37\u00e6\3\2\2\2!\u00ea\3\2\2")
        buf.write("\2#\u00f3\3\2\2\2%\u00f9\3\2\2\2\'\u00ff\3\2\2\2)\u0103")
        buf.write("\3\2\2\2+\u0108\3\2\2\2-\u010e\3\2\2\2/\u0110\3\2\2\2")
        buf.write("\61\u0112\3\2\2\2\63\u0114\3\2\2\2\65\u0116\3\2\2\2\67")
        buf.write("\u0118\3\2\2\29\u011b\3\2\2\2;\u011e\3\2\2\2=\u0120\3")
        buf.write("\2\2\2?\u0123\3\2\2\2A\u0125\3\2\2\2C\u0128\3\2\2\2E\u012b")
        buf.write("\3\2\2\2G\u012e\3\2\2\2I\u0130\3\2\2\2K\u0132\3\2\2\2")
        buf.write("M\u0135\3\2\2\2O\u0138\3\2\2\2Q\u013b\3\2\2\2S\u013e\3")
        buf.write("\2\2\2U\u0141\3\2\2\2W\u0144\3\2\2\2Y\u0146\3\2\2\2[\u0148")
        buf.write("\3\2\2\2]\u014a\3\2\2\2_\u014c\3\2\2\2a\u014e\3\2\2\2")
        buf.write("c\u0150\3\2\2\2e\u0152\3\2\2\2g\u0154\3\2\2\2i\u0156\3")
        buf.write("\2\2\2k\u0158\3\2\2\2m\u015a\3\2\2\2o\u015e\3\2\2\2q\u016c")
        buf.write("\3\2\2\2s\u0176\3\2\2\2u\u0178\3\2\2\2w\u017f\3\2\2\2")
        buf.write("y\u0186\3\2\2\2{\u018f\3\2\2\2}\u0192\3\2\2\2\177\u019e")
        buf.write("\3\2\2\2\u0081\u01b2\3\2\2\2\u0083\u01bd\3\2\2\2\u0085")
        buf.write("\u01c9\3\2\2\2\u0087\u01cb\3\2\2\2\u0089\u01d9\3\2\2\2")
        buf.write("\u008b\u01e8\3\2\2\2\u008d\u01ec\3\2\2\2\u008f\u01f2\3")
        buf.write("\2\2\2\u0091\u01f5\3\2\2\2\u0093\u0200\3\2\2\2\u0095\u0210")
        buf.write("\3\2\2\2\u0097\u0098\7a\2\2\u0098\4\3\2\2\2\u0099\u009a")
        buf.write("\7k\2\2\u009a\u009b\7h\2\2\u009b\6\3\2\2\2\u009c\u009d")
        buf.write("\7g\2\2\u009d\u009e\7n\2\2\u009e\u009f\7u\2\2\u009f\u00a0")
        buf.write("\7g\2\2\u00a0\b\3\2\2\2\u00a1\u00a2\7h\2\2\u00a2\u00a3")
        buf.write("\7q\2\2\u00a3\u00a4\7t\2\2\u00a4\n\3\2\2\2\u00a5\u00a6")
        buf.write("\7t\2\2\u00a6\u00a7\7g\2\2\u00a7\u00a8\7v\2\2\u00a8\u00a9")
        buf.write("\7w\2\2\u00a9\u00aa\7t\2\2\u00aa\u00ab\7p\2\2\u00ab\f")
        buf.write("\3\2\2\2\u00ac\u00ad\7h\2\2\u00ad\u00ae\7w\2\2\u00ae\u00af")
        buf.write("\7p\2\2\u00af\u00b0\7e\2\2\u00b0\16\3\2\2\2\u00b1\u00b2")
        buf.write("\7v\2\2\u00b2\u00b3\7{\2\2\u00b3\u00b4\7r\2\2\u00b4\u00b5")
        buf.write("\7g\2\2\u00b5\20\3\2\2\2\u00b6\u00b7\7u\2\2\u00b7\u00b8")
        buf.write("\7v\2\2\u00b8\u00b9\7t\2\2\u00b9\u00ba\7w\2\2\u00ba\u00bb")
        buf.write("\7e\2\2\u00bb\u00bc\7v\2\2\u00bc\22\3\2\2\2\u00bd\u00be")
        buf.write("\7k\2\2\u00be\u00bf\7p\2\2\u00bf\u00c0\7v\2\2\u00c0\u00c1")
        buf.write("\7g\2\2\u00c1\u00c2\7t\2\2\u00c2\u00c3\7h\2\2\u00c3\u00c4")
        buf.write("\7c\2\2\u00c4\u00c5\7e\2\2\u00c5\u00c6\7g\2\2\u00c6\24")
        buf.write("\3\2\2\2\u00c7\u00c8\7u\2\2\u00c8\u00c9\7v\2\2\u00c9\u00ca")
        buf.write("\7t\2\2\u00ca\u00cb\7k\2\2\u00cb\u00cc\7p\2\2\u00cc\u00cd")
        buf.write("\7i\2\2\u00cd\26\3\2\2\2\u00ce\u00cf\7k\2\2\u00cf\u00d0")
        buf.write("\7p\2\2\u00d0\u00d1\7v\2\2\u00d1\30\3\2\2\2\u00d2\u00d3")
        buf.write("\7h\2\2\u00d3\u00d4\7n\2\2\u00d4\u00d5\7q\2\2\u00d5\u00d6")
        buf.write("\7c\2\2\u00d6\u00d7\7v\2\2\u00d7\32\3\2\2\2\u00d8\u00d9")
        buf.write("\7d\2\2\u00d9\u00da\7q\2\2\u00da\u00db\7q\2\2\u00db\u00dc")
        buf.write("\7n\2\2\u00dc\u00dd\7g\2\2\u00dd\u00de\7c\2\2\u00de\u00df")
        buf.write("\7p\2\2\u00df\34\3\2\2\2\u00e0\u00e1\7e\2\2\u00e1\u00e2")
        buf.write("\7q\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4\7u\2\2\u00e4\u00e5")
        buf.write("\7v\2\2\u00e5\36\3\2\2\2\u00e6\u00e7\7x\2\2\u00e7\u00e8")
        buf.write("\7c\2\2\u00e8\u00e9\7t\2\2\u00e9 \3\2\2\2\u00ea\u00eb")
        buf.write("\7e\2\2\u00eb\u00ec\7q\2\2\u00ec\u00ed\7p\2\2\u00ed\u00ee")
        buf.write("\7v\2\2\u00ee\u00ef\7k\2\2\u00ef\u00f0\7p\2\2\u00f0\u00f1")
        buf.write("\7w\2\2\u00f1\u00f2\7g\2\2\u00f2\"\3\2\2\2\u00f3\u00f4")
        buf.write("\7d\2\2\u00f4\u00f5\7t\2\2\u00f5\u00f6\7g\2\2\u00f6\u00f7")
        buf.write("\7c\2\2\u00f7\u00f8\7m\2\2\u00f8$\3\2\2\2\u00f9\u00fa")
        buf.write("\7t\2\2\u00fa\u00fb\7c\2\2\u00fb\u00fc\7p\2\2\u00fc\u00fd")
        buf.write("\7i\2\2\u00fd\u00fe\7g\2\2\u00fe&\3\2\2\2\u00ff\u0100")
        buf.write("\7p\2\2\u0100\u0101\7k\2\2\u0101\u0102\7n\2\2\u0102(\3")
        buf.write("\2\2\2\u0103\u0104\7v\2\2\u0104\u0105\7t\2\2\u0105\u0106")
        buf.write("\7w\2\2\u0106\u0107\7g\2\2\u0107*\3\2\2\2\u0108\u0109")
        buf.write("\7h\2\2\u0109\u010a\7c\2\2\u010a\u010b\7n\2\2\u010b\u010c")
        buf.write("\7u\2\2\u010c\u010d\7g\2\2\u010d,\3\2\2\2\u010e\u010f")
        buf.write("\7-\2\2\u010f.\3\2\2\2\u0110\u0111\7/\2\2\u0111\60\3\2")
        buf.write("\2\2\u0112\u0113\7,\2\2\u0113\62\3\2\2\2\u0114\u0115\7")
        buf.write("\61\2\2\u0115\64\3\2\2\2\u0116\u0117\7\'\2\2\u0117\66")
        buf.write("\3\2\2\2\u0118\u0119\7?\2\2\u0119\u011a\7?\2\2\u011a8")
        buf.write("\3\2\2\2\u011b\u011c\7#\2\2\u011c\u011d\7?\2\2\u011d:")
        buf.write("\3\2\2\2\u011e\u011f\7>\2\2\u011f<\3\2\2\2\u0120\u0121")
        buf.write("\7>\2\2\u0121\u0122\7?\2\2\u0122>\3\2\2\2\u0123\u0124")
        buf.write("\7@\2\2\u0124@\3\2\2\2\u0125\u0126\7@\2\2\u0126\u0127")
        buf.write("\7?\2\2\u0127B\3\2\2\2\u0128\u0129\7(\2\2\u0129\u012a")
        buf.write("\7(\2\2\u012aD\3\2\2\2\u012b\u012c\7~\2\2\u012c\u012d")
        buf.write("\7~\2\2\u012dF\3\2\2\2\u012e\u012f\7#\2\2\u012fH\3\2\2")
        buf.write("\2\u0130\u0131\7?\2\2\u0131J\3\2\2\2\u0132\u0133\7<\2")
        buf.write("\2\u0133\u0134\7?\2\2\u0134L\3\2\2\2\u0135\u0136\7-\2")
        buf.write("\2\u0136\u0137\7?\2\2\u0137N\3\2\2\2\u0138\u0139\7/\2")
        buf.write("\2\u0139\u013a\7?\2\2\u013aP\3\2\2\2\u013b\u013c\7,\2")
        buf.write("\2\u013c\u013d\7?\2\2\u013dR\3\2\2\2\u013e\u013f\7\61")
        buf.write("\2\2\u013f\u0140\7?\2\2\u0140T\3\2\2\2\u0141\u0142\7\'")
        buf.write("\2\2\u0142\u0143\7?\2\2\u0143V\3\2\2\2\u0144\u0145\7\60")
        buf.write("\2\2\u0145X\3\2\2\2\u0146\u0147\7<\2\2\u0147Z\3\2\2\2")
        buf.write("\u0148\u0149\7*\2\2\u0149\\\3\2\2\2\u014a\u014b\7+\2\2")
        buf.write("\u014b^\3\2\2\2\u014c\u014d\7}\2\2\u014d`\3\2\2\2\u014e")
        buf.write("\u014f\7\177\2\2\u014fb\3\2\2\2\u0150\u0151\7]\2\2\u0151")
        buf.write("d\3\2\2\2\u0152\u0153\7_\2\2\u0153f\3\2\2\2\u0154\u0155")
        buf.write("\7.\2\2\u0155h\3\2\2\2\u0156\u0157\7=\2\2\u0157j\3\2\2")
        buf.write("\2\u0158\u0159\t\2\2\2\u0159l\3\2\2\2\u015a\u015b\t\3")
        buf.write("\2\2\u015bn\3\2\2\2\u015c\u015f\5k\66\2\u015d\u015f\7")
        buf.write("a\2\2\u015e\u015c\3\2\2\2\u015e\u015d\3\2\2\2\u015f\u0165")
        buf.write("\3\2\2\2\u0160\u0164\5k\66\2\u0161\u0164\5m\67\2\u0162")
        buf.write("\u0164\7a\2\2\u0163\u0160\3\2\2\2\u0163\u0161\3\2\2\2")
        buf.write("\u0163\u0162\3\2\2\2\u0164\u0167\3\2\2\2\u0165\u0163\3")
        buf.write("\2\2\2\u0165\u0166\3\2\2\2\u0166p\3\2\2\2\u0167\u0165")
        buf.write("\3\2\2\2\u0168\u016d\5s:\2\u0169\u016d\5u;\2\u016a\u016d")
        buf.write("\5w<\2\u016b\u016d\5y=\2\u016c\u0168\3\2\2\2\u016c\u0169")
        buf.write("\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016b\3\2\2\2\u016d")
        buf.write("r\3\2\2\2\u016e\u0177\7\62\2\2\u016f\u0173\t\4\2\2\u0170")
        buf.write("\u0172\5m\67\2\u0171\u0170\3\2\2\2\u0172\u0175\3\2\2\2")
        buf.write("\u0173\u0171\3\2\2\2\u0173\u0174\3\2\2\2\u0174\u0177\3")
        buf.write("\2\2\2\u0175\u0173\3\2\2\2\u0176\u016e\3\2\2\2\u0176\u016f")
        buf.write("\3\2\2\2\u0177t\3\2\2\2\u0178\u0179\7\62\2\2\u0179\u017b")
        buf.write("\t\5\2\2\u017a\u017c\t\6\2\2\u017b\u017a\3\2\2\2\u017c")
        buf.write("\u017d\3\2\2\2\u017d\u017b\3\2\2\2\u017d\u017e\3\2\2\2")
        buf.write("\u017ev\3\2\2\2\u017f\u0180\7\62\2\2\u0180\u0182\t\7\2")
        buf.write("\2\u0181\u0183\t\b\2\2\u0182\u0181\3\2\2\2\u0183\u0184")
        buf.write("\3\2\2\2\u0184\u0182\3\2\2\2\u0184\u0185\3\2\2\2\u0185")
        buf.write("x\3\2\2\2\u0186\u0187\7\62\2\2\u0187\u0189\t\t\2\2\u0188")
        buf.write("\u018a\t\n\2\2\u0189\u0188\3\2\2\2\u018a\u018b\3\2\2\2")
        buf.write("\u018b\u0189\3\2\2\2\u018b\u018c\3\2\2\2\u018cz\3\2\2")
        buf.write("\2\u018d\u0190\5}?\2\u018e\u0190\5\177@\2\u018f\u018d")
        buf.write("\3\2\2\2\u018f\u018e\3\2\2\2\u0190|\3\2\2\2\u0191\u0193")
        buf.write("\5m\67\2\u0192\u0191\3\2\2\2\u0193\u0194\3\2\2\2\u0194")
        buf.write("\u0192\3\2\2\2\u0194\u0195\3\2\2\2\u0195\u0196\3\2\2\2")
        buf.write("\u0196\u019a\7\60\2\2\u0197\u0199\5m\67\2\u0198\u0197")
        buf.write("\3\2\2\2\u0199\u019c\3\2\2\2\u019a\u0198\3\2\2\2\u019a")
        buf.write("\u019b\3\2\2\2\u019b~\3\2\2\2\u019c\u019a\3\2\2\2\u019d")
        buf.write("\u019f\5m\67\2\u019e\u019d\3\2\2\2\u019f\u01a0\3\2\2\2")
        buf.write("\u01a0\u019e\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u01a2\3")
        buf.write("\2\2\2\u01a2\u01a6\7\60\2\2\u01a3\u01a5\5m\67\2\u01a4")
        buf.write("\u01a3\3\2\2\2\u01a5\u01a8\3\2\2\2\u01a6\u01a4\3\2\2\2")
        buf.write("\u01a6\u01a7\3\2\2\2\u01a7\u01a9\3\2\2\2\u01a8\u01a6\3")
        buf.write("\2\2\2\u01a9\u01ab\t\13\2\2\u01aa\u01ac\t\f\2\2\u01ab")
        buf.write("\u01aa\3\2\2\2\u01ab\u01ac\3\2\2\2\u01ac\u01ae\3\2\2\2")
        buf.write("\u01ad\u01af\5m\67\2\u01ae\u01ad\3\2\2\2\u01af\u01b0\3")
        buf.write("\2\2\2\u01b0\u01ae\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1\u0080")
        buf.write("\3\2\2\2\u01b2\u01b7\7$\2\2\u01b3\u01b6\5\u0083B\2\u01b4")
        buf.write("\u01b6\5\u0085C\2\u01b5\u01b3\3\2\2\2\u01b5\u01b4\3\2")
        buf.write("\2\2\u01b6\u01b9\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b7\u01b8")
        buf.write("\3\2\2\2\u01b8\u01ba\3\2\2\2\u01b9\u01b7\3\2\2\2\u01ba")
        buf.write("\u01bb\7$\2\2\u01bb\u01bc\bA\2\2\u01bc\u0082\3\2\2\2\u01bd")
        buf.write("\u01be\n\r\2\2\u01be\u0084\3\2\2\2\u01bf\u01c0\7^\2\2")
        buf.write("\u01c0\u01ca\7p\2\2\u01c1\u01c2\7^\2\2\u01c2\u01ca\7v")
        buf.write("\2\2\u01c3\u01c4\7^\2\2\u01c4\u01ca\7t\2\2\u01c5\u01c6")
        buf.write("\7^\2\2\u01c6\u01ca\7$\2\2\u01c7\u01c8\7^\2\2\u01c8\u01ca")
        buf.write("\7^\2\2\u01c9\u01bf\3\2\2\2\u01c9\u01c1\3\2\2\2\u01c9")
        buf.write("\u01c3\3\2\2\2\u01c9\u01c5\3\2\2\2\u01c9\u01c7\3\2\2\2")
        buf.write("\u01ca\u0086\3\2\2\2\u01cb\u01cc\7\61\2\2\u01cc\u01cd")
        buf.write("\7\61\2\2\u01cd\u01d1\3\2\2\2\u01ce\u01d0\n\16\2\2\u01cf")
        buf.write("\u01ce\3\2\2\2\u01d0\u01d3\3\2\2\2\u01d1\u01cf\3\2\2\2")
        buf.write("\u01d1\u01d2\3\2\2\2\u01d2\u01d5\3\2\2\2\u01d3\u01d1\3")
        buf.write("\2\2\2\u01d4\u01d6\t\17\2\2\u01d5\u01d4\3\2\2\2\u01d6")
        buf.write("\u01d7\3\2\2\2\u01d7\u01d8\bD\3\2\u01d8\u0088\3\2\2\2")
        buf.write("\u01d9\u01da\7\61\2\2\u01da\u01db\7,\2\2\u01db\u01e0\3")
        buf.write("\2\2\2\u01dc\u01df\n\20\2\2\u01dd\u01df\5\u0089E\2\u01de")
        buf.write("\u01dc\3\2\2\2\u01de\u01dd\3\2\2\2\u01df\u01e2\3\2\2\2")
        buf.write("\u01e0\u01de\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1\u01e3\3")
        buf.write("\2\2\2\u01e2\u01e0\3\2\2\2\u01e3\u01e4\7,\2\2\u01e4\u01e5")
        buf.write("\7\61\2\2\u01e5\u01e6\3\2\2\2\u01e6\u01e7\bE\3\2\u01e7")
        buf.write("\u008a\3\2\2\2\u01e8\u01e9\7\f\2\2\u01e9\u01ea\bF\4\2")
        buf.write("\u01ea\u008c\3\2\2\2\u01eb\u01ed\t\21\2\2\u01ec\u01eb")
        buf.write("\3\2\2\2\u01ed\u01ee\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ee")
        buf.write("\u01ef\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01f1\bG\3\2")
        buf.write("\u01f1\u008e\3\2\2\2\u01f2\u01f3\7^\2\2\u01f3\u01f4\n")
        buf.write("\22\2\2\u01f4\u0090\3\2\2\2\u01f5\u01fa\7$\2\2\u01f6\u01f9")
        buf.write("\5\u0083B\2\u01f7\u01f9\5\u0085C\2\u01f8\u01f6\3\2\2\2")
        buf.write("\u01f8\u01f7\3\2\2\2\u01f9\u01fc\3\2\2\2\u01fa\u01f8\3")
        buf.write("\2\2\2\u01fa\u01fb\3\2\2\2\u01fb\u01fd\3\2\2\2\u01fc\u01fa")
        buf.write("\3\2\2\2\u01fd\u01fe\5\u008fH\2\u01fe\u01ff\bI\5\2\u01ff")
        buf.write("\u0092\3\2\2\2\u0200\u0205\7$\2\2\u0201\u0204\5\u0083")
        buf.write("B\2\u0202\u0204\5\u0085C\2\u0203\u0201\3\2\2\2\u0203\u0202")
        buf.write("\3\2\2\2\u0204\u0207\3\2\2\2\u0205\u0203\3\2\2\2\u0205")
        buf.write("\u0206\3\2\2\2\u0206\u020c\3\2\2\2\u0207\u0205\3\2\2\2")
        buf.write("\u0208\u020d\7\f\2\2\u0209\u020a\7\17\2\2\u020a\u020d")
        buf.write("\7\f\2\2\u020b\u020d\7\2\2\3\u020c\u0208\3\2\2\2\u020c")
        buf.write("\u0209\3\2\2\2\u020c\u020b\3\2\2\2\u020d\u020e\3\2\2\2")
        buf.write("\u020e\u020f\bJ\6\2\u020f\u0094\3\2\2\2\u0210\u0211\13")
        buf.write("\2\2\2\u0211\u0096\3\2\2\2 \2\u015e\u0163\u0165\u016c")
        buf.write("\u0173\u0176\u017d\u0184\u018b\u018f\u0194\u019a\u01a0")
        buf.write("\u01a6\u01ab\u01b0\u01b5\u01b7\u01c9\u01d1\u01d5\u01de")
        buf.write("\u01e0\u01ee\u01f8\u01fa\u0203\u0205\u020c\7\3A\2\b\2")
        buf.write("\2\3F\3\3I\4\3J\5")
        return buf.getvalue()


class MiniGoLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    IF = 2
    ELSE = 3
    FOR = 4
    RETURN = 5
    FUNC = 6
    TYPE = 7
    STRUCT = 8
    INTERFACE = 9
    STRING = 10
    INT = 11
    FLOAT = 12
    BOOLEAN = 13
    CONST = 14
    VAR = 15
    CONTINUE = 16
    BREAK = 17
    RANGE = 18
    NIL = 19
    TRUE = 20
    FALSE = 21
    PLUS = 22
    MINUS = 23
    MULTI = 24
    DIV = 25
    MODULO = 26
    EQUAL = 27
    NOT_EQUAL = 28
    LESS_THAN = 29
    LESS_EQUAL = 30
    GREATER_THAN = 31
    GREATER_EQUAL = 32
    AND = 33
    OR = 34
    NOT = 35
    ASSIGN = 36
    ASSIGN1 = 37
    PLUS_EQUAL = 38
    MINUS_EQUAL = 39
    MULTI_EQUAL = 40
    DIV_EQUAL = 41
    MODULO_EQUAL = 42
    DOT = 43
    COLON = 44
    OPEN_ROUND = 45
    CLOSE_ROUND = 46
    OPEN_CURVE = 47
    CLOSE_CURVE = 48
    OPEN_SQUARE = 49
    CLOSE_SQUARE = 50
    COMMA = 51
    SEMICOLON = 52
    ID = 53
    INT_LIT = 54
    FLOAT_LIT = 55
    STRING_LIT = 56
    COMMENT_INLINE = 57
    COMMENT_BLOCK = 58
    NL = 59
    WS = 60
    ILLEGAL_ESCAPE = 61
    UNCLOSE_STRING = 62
    ERROR_CHAR = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'_'", "'if'", "'else'", "'for'", "'return'", "'func'", "'type'", 
            "'struct'", "'interface'", "'string'", "'int'", "'float'", "'boolean'", 
            "'const'", "'var'", "'continue'", "'break'", "'range'", "'nil'", 
            "'true'", "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
            "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", "'!'", 
            "'='", "':='", "'+='", "'-='", "'*='", "'/='", "'%='", "'.'", 
            "':'", "'('", "')'", "'{'", "'}'", "'['", "']'", "','", "';'", 
            "'\n'" ]

    symbolicNames = [ "<INVALID>",
            "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", "STRUCT", "INTERFACE", 
            "STRING", "INT", "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", 
            "BREAK", "RANGE", "NIL", "TRUE", "FALSE", "PLUS", "MINUS", "MULTI", 
            "DIV", "MODULO", "EQUAL", "NOT_EQUAL", "LESS_THAN", "LESS_EQUAL", 
            "GREATER_THAN", "GREATER_EQUAL", "AND", "OR", "NOT", "ASSIGN", 
            "ASSIGN1", "PLUS_EQUAL", "MINUS_EQUAL", "MULTI_EQUAL", "DIV_EQUAL", 
            "MODULO_EQUAL", "DOT", "COLON", "OPEN_ROUND", "CLOSE_ROUND", 
            "OPEN_CURVE", "CLOSE_CURVE", "OPEN_SQUARE", "CLOSE_SQUARE", 
            "COMMA", "SEMICOLON", "ID", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
            "COMMENT_INLINE", "COMMENT_BLOCK", "NL", "WS", "ILLEGAL_ESCAPE", 
            "UNCLOSE_STRING", "ERROR_CHAR" ]

    ruleNames = [ "T__0", "IF", "ELSE", "FOR", "RETURN", "FUNC", "TYPE", 
                  "STRUCT", "INTERFACE", "STRING", "INT", "FLOAT", "BOOLEAN", 
                  "CONST", "VAR", "CONTINUE", "BREAK", "RANGE", "NIL", "TRUE", 
                  "FALSE", "PLUS", "MINUS", "MULTI", "DIV", "MODULO", "EQUAL", 
                  "NOT_EQUAL", "LESS_THAN", "LESS_EQUAL", "GREATER_THAN", 
                  "GREATER_EQUAL", "AND", "OR", "NOT", "ASSIGN", "ASSIGN1", 
                  "PLUS_EQUAL", "MINUS_EQUAL", "MULTI_EQUAL", "DIV_EQUAL", 
                  "MODULO_EQUAL", "DOT", "COLON", "OPEN_ROUND", "CLOSE_ROUND", 
                  "OPEN_CURVE", "CLOSE_CURVE", "OPEN_SQUARE", "CLOSE_SQUARE", 
                  "COMMA", "SEMICOLON", "Letter", "Digit", "ID", "INT_LIT", 
                  "Decimal", "Binary", "Octal", "Hex", "FLOAT_LIT", "No_exponent", 
                  "Exponent", "STRING_LIT", "String_Character", "String_Escape", 
                  "COMMENT_INLINE", "COMMENT_BLOCK", "NL", "WS", "ILL_ESC", 
                  "ILLEGAL_ESCAPE", "UNCLOSE_STRING", "ERROR_CHAR" ]

    grammarFileName = "MiniGo.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    _prev_token_type = 0
    def emit(self):
        tk = self.type
        if tk == self.UNCLOSE_STRING:       
            result = super().emit();
            raise UncloseString(result.text);
        elif tk == self.ILLEGAL_ESCAPE:
            result = super().emit();
            raise IllegalEscape(result.text);
        elif tk == self.ERROR_CHAR:
            result = super().emit();
            raise ErrorToken(result.text); 
        else:
            token = super().emit();
            self._prev_token_type = token.type;
            return token;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[63] = self.STRING_LIT_action 
            actions[68] = self.NL_action 
            actions[71] = self.ILLEGAL_ESCAPE_action 
            actions[72] = self.UNCLOSE_STRING_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                self.text = self.text[1:-1]
                # print(f"string lit: {self.text}")

     

    def NL_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                # print(f"prev_token: {self._prev_token_type}")
                if(self._prev_token_type in {self.ID,self.INT_LIT, self.FLOAT_LIT, self.TRUE, self.FALSE, self.STRING_LIT, self.INT, self.FLOAT, self.BOOLEAN, self.STRING, self.RETURN, self.CONTINUE, self.BREAK, self.CLOSE_ROUND, self.CLOSE_CURVE, self.CLOSE_SQUARE}):
                    # print(f"Im in, before me: {self._prev_token_type}")
                    # self.emitToken(self.commonToken(self.SEMICOLON, ';'))
                    self.text = ';'  
                    self.type = self.SEMICOLON
                else:
                    self.skip()

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                self.text = self.text[1:]

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                if(len(self.text) >= 2 and self.text[-2] == '\r' and self.text[-1] == '\n'):
                    self.text = self.text[:-2]
                elif(self.text[-1] == '\n'):
                    self.text = self.text[:-1]
                else:
                    self.text = self.text[1:]

     


