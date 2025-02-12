# Generated from main/minigo/parser/MiniGo.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3A")
        buf.write("\u026a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\3\2\6\2\u008e\n\2\r\2\16\2\u008f\3\2\3\2")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u009a\n\3\3\4\3\4\3\4\3\4")
        buf.write("\3\4\3\4\5\4\u00a2\n\4\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\5\6\u00ae\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\t\3\t\3\t\3\t\5\t\u00be\n\t\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\r\5\r\u00d2\n\r\3\16\3\16\3\16\3\16\3\16\5\16")
        buf.write("\u00d9\n\16\3\16\3\16\3\17\3\17\5\17\u00df\n\17\3\20\3")
        buf.write("\20\3\20\3\20\3\20\5\20\u00e6\n\20\3\21\3\21\3\21\3\22")
        buf.write("\3\22\3\22\3\22\5\22\u00ef\n\22\3\23\3\23\3\23\3\23\3")
        buf.write("\23\3\23\3\23\3\23\3\23\5\23\u00fa\n\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\24\3\24\5\24\u0103\n\24\3\24\3\24\3\25\3")
        buf.write("\25\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u010f\n\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\27\3\27\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\5\30\u0122\n\30\3\30\3\30\3")
        buf.write("\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\33")
        buf.write("\3\33\3\33\3\33\3\33\5\33\u0135\n\33\3\34\3\34\3\34\5")
        buf.write("\34\u013a\n\34\3\35\3\35\3\35\3\35\3\35\3\36\3\36\5\36")
        buf.write("\u0143\n\36\3\37\3\37\3\37\3\37\3\37\5\37\u014a\n\37\3")
        buf.write(" \3 \3 \3 \3!\3!\3!\3!\3!\3\"\3\"\5\"\u0157\n\"\3#\3#")
        buf.write("\3#\3#\3#\5#\u015e\n#\3$\3$\5$\u0162\n$\3%\3%\3%\3%\3")
        buf.write("%\3%\7%\u016a\n%\f%\16%\u016d\13%\3&\3&\3&\3&\3&\3&\7")
        buf.write("&\u0175\n&\f&\16&\u0178\13&\3\'\3\'\3\'\3\'\3\'\3\'\7")
        buf.write("\'\u0180\n\'\f\'\16\'\u0183\13\'\3(\3(\3(\3(\3(\3(\7(")
        buf.write("\u018b\n(\f(\16(\u018e\13(\3)\3)\3)\3)\3)\3)\7)\u0196")
        buf.write("\n)\f)\16)\u0199\13)\3*\3*\3*\5*\u019e\n*\3+\3+\3+\3+")
        buf.write("\3+\3+\3+\3+\3+\3+\3+\3+\3+\3+\7+\u01ae\n+\f+\16+\u01b1")
        buf.write("\13+\3,\3,\3,\3,\3,\5,\u01b8\n,\3-\3-\3-\3-\3-\3-\3-\3")
        buf.write("-\5-\u01c2\n-\3-\5-\u01c5\n-\3.\3.\3.\5.\u01ca\n.\3/\3")
        buf.write("/\3/\3/\3/\3/\3/\3/\3/\5/\u01d5\n/\3/\3/\3\60\3\60\3\60")
        buf.write("\3\60\5\60\u01dd\n\60\3\61\3\61\3\61\3\61\3\61\3\61\3")
        buf.write("\61\3\61\3\61\5\61\u01e8\n\61\3\62\3\62\3\62\3\62\3\62")
        buf.write("\5\62\u01ef\n\62\3\63\3\63\3\63\3\63\3\64\3\64\3\64\3")
        buf.write("\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\7\64\u0200\n\64")
        buf.write("\f\64\16\64\u0203\13\64\3\65\3\65\3\66\3\66\3\67\3\67")
        buf.write("\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67\3\67")
        buf.write("\5\67\u0216\n\67\38\38\38\38\58\u021c\n8\39\39\39\39\3")
        buf.write("9\39\39\39\39\3:\3:\3:\5:\u022a\n:\3;\3;\3;\3;\3;\3;\3")
        buf.write("<\3<\3<\3<\3<\3<\3<\3<\3<\3<\3=\3=\5=\u023e\n=\3>\3>\3")
        buf.write(">\5>\u0243\n>\3>\3>\3>\3?\3?\3@\3@\3A\3A\3A\3A\3B\3B\3")
        buf.write("B\3B\3B\3B\3B\3B\3B\3B\3B\3C\3C\3D\3D\3E\3E\3E\3E\3E\5")
        buf.write("E\u0264\nE\3F\3F\5F\u0268\nF\3F\2\tHJLNPTfG\2\4\6\b\n")
        buf.write("\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\668:<")
        buf.write(">@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080\u0082\u0084\u0086")
        buf.write("\u0088\u008a\2\13\4\2\f\17\67\67\3\2\678\4\2\25\278:\3")
        buf.write("\2\35\"\3\2\30\31\3\2\32\34\4\2\31\31%%\3\2\',\4\2\3\3")
        buf.write("\67\67\2\u0269\2\u008d\3\2\2\2\4\u0099\3\2\2\2\6\u00a1")
        buf.write("\3\2\2\2\b\u00a3\3\2\2\2\n\u00ad\3\2\2\2\f\u00af\3\2\2")
        buf.write("\2\16\u00b7\3\2\2\2\20\u00bd\3\2\2\2\22\u00bf\3\2\2\2")
        buf.write("\24\u00c3\3\2\2\2\26\u00cb\3\2\2\2\30\u00d1\3\2\2\2\32")
        buf.write("\u00d3\3\2\2\2\34\u00de\3\2\2\2\36\u00e5\3\2\2\2 \u00e7")
        buf.write("\3\2\2\2\"\u00ee\3\2\2\2$\u00f0\3\2\2\2&\u00fd\3\2\2\2")
        buf.write("(\u0106\3\2\2\2*\u0108\3\2\2\2,\u0115\3\2\2\2.\u0117\3")
        buf.write("\2\2\2\60\u0128\3\2\2\2\62\u012b\3\2\2\2\64\u0134\3\2")
        buf.write("\2\2\66\u0139\3\2\2\28\u013b\3\2\2\2:\u0142\3\2\2\2<\u0149")
        buf.write("\3\2\2\2>\u014b\3\2\2\2@\u014f\3\2\2\2B\u0156\3\2\2\2")
        buf.write("D\u015d\3\2\2\2F\u0161\3\2\2\2H\u0163\3\2\2\2J\u016e\3")
        buf.write("\2\2\2L\u0179\3\2\2\2N\u0184\3\2\2\2P\u018f\3\2\2\2R\u019d")
        buf.write("\3\2\2\2T\u019f\3\2\2\2V\u01b7\3\2\2\2X\u01c4\3\2\2\2")
        buf.write("Z\u01c9\3\2\2\2\\\u01d4\3\2\2\2^\u01dc\3\2\2\2`\u01de")
        buf.write("\3\2\2\2b\u01e9\3\2\2\2d\u01f0\3\2\2\2f\u01f4\3\2\2\2")
        buf.write("h\u0204\3\2\2\2j\u0206\3\2\2\2l\u0208\3\2\2\2n\u021b\3")
        buf.write("\2\2\2p\u021d\3\2\2\2r\u0229\3\2\2\2t\u022b\3\2\2\2v\u0231")
        buf.write("\3\2\2\2x\u023d\3\2\2\2z\u023f\3\2\2\2|\u0247\3\2\2\2")
        buf.write("~\u0249\3\2\2\2\u0080\u024b\3\2\2\2\u0082\u024f\3\2\2")
        buf.write("\2\u0084\u025a\3\2\2\2\u0086\u025c\3\2\2\2\u0088\u0263")
        buf.write("\3\2\2\2\u008a\u0265\3\2\2\2\u008c\u008e\5\4\3\2\u008d")
        buf.write("\u008c\3\2\2\2\u008e\u008f\3\2\2\2\u008f\u008d\3\2\2\2")
        buf.write("\u008f\u0090\3\2\2\2\u0090\u0091\3\2\2\2\u0091\u0092\7")
        buf.write("\2\2\3\u0092\3\3\2\2\2\u0093\u009a\5\f\7\2\u0094\u009a")
        buf.write("\5\24\13\2\u0095\u009a\5$\23\2\u0096\u009a\5&\24\2\u0097")
        buf.write("\u009a\5*\26\2\u0098\u009a\5.\30\2\u0099\u0093\3\2\2\2")
        buf.write("\u0099\u0094\3\2\2\2\u0099\u0095\3\2\2\2\u0099\u0096\3")
        buf.write("\2\2\2\u0099\u0097\3\2\2\2\u0099\u0098\3\2\2\2\u009a\5")
        buf.write("\3\2\2\2\u009b\u00a2\7\r\2\2\u009c\u00a2\7\16\2\2\u009d")
        buf.write("\u00a2\7\17\2\2\u009e\u00a2\7\f\2\2\u009f\u00a2\5\b\5")
        buf.write("\2\u00a0\u00a2\7\67\2\2\u00a1\u009b\3\2\2\2\u00a1\u009c")
        buf.write("\3\2\2\2\u00a1\u009d\3\2\2\2\u00a1\u009e\3\2\2\2\u00a1")
        buf.write("\u009f\3\2\2\2\u00a1\u00a0\3\2\2\2\u00a2\7\3\2\2\2\u00a3")
        buf.write("\u00a4\5\n\6\2\u00a4\u00a5\t\2\2\2\u00a5\t\3\2\2\2\u00a6")
        buf.write("\u00a7\7\63\2\2\u00a7\u00a8\t\3\2\2\u00a8\u00a9\7\64\2")
        buf.write("\2\u00a9\u00ae\5\n\6\2\u00aa\u00ab\7\63\2\2\u00ab\u00ac")
        buf.write("\t\3\2\2\u00ac\u00ae\7\64\2\2\u00ad\u00a6\3\2\2\2\u00ad")
        buf.write("\u00aa\3\2\2\2\u00ae\13\3\2\2\2\u00af\u00b0\7\t\2\2\u00b0")
        buf.write("\u00b1\7\67\2\2\u00b1\u00b2\7\n\2\2\u00b2\u00b3\7\61\2")
        buf.write("\2\u00b3\u00b4\5\16\b\2\u00b4\u00b5\7\62\2\2\u00b5\u00b6")
        buf.write("\7\66\2\2\u00b6\r\3\2\2\2\u00b7\u00b8\5\20\t\2\u00b8\17")
        buf.write("\3\2\2\2\u00b9\u00ba\5\22\n\2\u00ba\u00bb\5\20\t\2\u00bb")
        buf.write("\u00be\3\2\2\2\u00bc\u00be\5\22\n\2\u00bd\u00b9\3\2\2")
        buf.write("\2\u00bd\u00bc\3\2\2\2\u00be\21\3\2\2\2\u00bf\u00c0\7")
        buf.write("\67\2\2\u00c0\u00c1\5\6\4\2\u00c1\u00c2\7\66\2\2\u00c2")
        buf.write("\23\3\2\2\2\u00c3\u00c4\7\t\2\2\u00c4\u00c5\7\67\2\2\u00c5")
        buf.write("\u00c6\7\13\2\2\u00c6\u00c7\7\61\2\2\u00c7\u00c8\5\26")
        buf.write("\f\2\u00c8\u00c9\7\62\2\2\u00c9\u00ca\7\66\2\2\u00ca\25")
        buf.write("\3\2\2\2\u00cb\u00cc\5\30\r\2\u00cc\27\3\2\2\2\u00cd\u00ce")
        buf.write("\5\32\16\2\u00ce\u00cf\5\30\r\2\u00cf\u00d2\3\2\2\2\u00d0")
        buf.write("\u00d2\5\32\16\2\u00d1\u00cd\3\2\2\2\u00d1\u00d0\3\2\2")
        buf.write("\2\u00d2\31\3\2\2\2\u00d3\u00d4\7\67\2\2\u00d4\u00d5\7")
        buf.write("/\2\2\u00d5\u00d6\5\34\17\2\u00d6\u00d8\7\60\2\2\u00d7")
        buf.write("\u00d9\5\6\4\2\u00d8\u00d7\3\2\2\2\u00d8\u00d9\3\2\2\2")
        buf.write("\u00d9\u00da\3\2\2\2\u00da\u00db\7\66\2\2\u00db\33\3\2")
        buf.write("\2\2\u00dc\u00df\5\36\20\2\u00dd\u00df\3\2\2\2\u00de\u00dc")
        buf.write("\3\2\2\2\u00de\u00dd\3\2\2\2\u00df\35\3\2\2\2\u00e0\u00e1")
        buf.write("\5 \21\2\u00e1\u00e2\7\65\2\2\u00e2\u00e3\5\36\20\2\u00e3")
        buf.write("\u00e6\3\2\2\2\u00e4\u00e6\5 \21\2\u00e5\u00e0\3\2\2\2")
        buf.write("\u00e5\u00e4\3\2\2\2\u00e6\37\3\2\2\2\u00e7\u00e8\5\"")
        buf.write("\22\2\u00e8\u00e9\5\6\4\2\u00e9!\3\2\2\2\u00ea\u00eb\7")
        buf.write("\67\2\2\u00eb\u00ec\7\65\2\2\u00ec\u00ef\5\"\22\2\u00ed")
        buf.write("\u00ef\7\67\2\2\u00ee\u00ea\3\2\2\2\u00ee\u00ed\3\2\2")
        buf.write("\2\u00ef#\3\2\2\2\u00f0\u00f1\7\21\2\2\u00f1\u00f9\7\67")
        buf.write("\2\2\u00f2\u00f3\5\6\4\2\u00f3\u00f4\7&\2\2\u00f4\u00f5")
        buf.write("\5H%\2\u00f5\u00fa\3\2\2\2\u00f6\u00f7\7&\2\2\u00f7\u00fa")
        buf.write("\5H%\2\u00f8\u00fa\5\6\4\2\u00f9\u00f2\3\2\2\2\u00f9\u00f6")
        buf.write("\3\2\2\2\u00f9\u00f8\3\2\2\2\u00fa\u00fb\3\2\2\2\u00fb")
        buf.write("\u00fc\7\66\2\2\u00fc%\3\2\2\2\u00fd\u00fe\7\20\2\2\u00fe")
        buf.write("\u00ff\7\67\2\2\u00ff\u0102\7&\2\2\u0100\u0103\5(\25\2")
        buf.write("\u0101\u0103\5H%\2\u0102\u0100\3\2\2\2\u0102\u0101\3\2")
        buf.write("\2\2\u0103\u0104\3\2\2\2\u0104\u0105\7\66\2\2\u0105\'")
        buf.write("\3\2\2\2\u0106\u0107\t\4\2\2\u0107)\3\2\2\2\u0108\u0109")
        buf.write("\7\b\2\2\u0109\u010a\7\67\2\2\u010a\u010b\7/\2\2\u010b")
        buf.write("\u010c\5\34\17\2\u010c\u010e\7\60\2\2\u010d\u010f\5\6")
        buf.write("\4\2\u010e\u010d\3\2\2\2\u010e\u010f\3\2\2\2\u010f\u0110")
        buf.write("\3\2\2\2\u0110\u0111\7\61\2\2\u0111\u0112\5,\27\2\u0112")
        buf.write("\u0113\7\62\2\2\u0113\u0114\7\66\2\2\u0114+\3\2\2\2\u0115")
        buf.write("\u0116\5^\60\2\u0116-\3\2\2\2\u0117\u0118\7\b\2\2\u0118")
        buf.write("\u0119\7/\2\2\u0119\u011a\7\67\2\2\u011a\u011b\7\67\2")
        buf.write("\2\u011b\u011c\7\60\2\2\u011c\u011d\7\67\2\2\u011d\u011e")
        buf.write("\7/\2\2\u011e\u011f\5\34\17\2\u011f\u0121\7\60\2\2\u0120")
        buf.write("\u0122\5\6\4\2\u0121\u0120\3\2\2\2\u0121\u0122\3\2\2\2")
        buf.write("\u0122\u0123\3\2\2\2\u0123\u0124\7\61\2\2\u0124\u0125")
        buf.write("\5,\27\2\u0125\u0126\7\62\2\2\u0126\u0127\7\66\2\2\u0127")
        buf.write("/\3\2\2\2\u0128\u0129\5\b\5\2\u0129\u012a\5\62\32\2\u012a")
        buf.write("\61\3\2\2\2\u012b\u012c\7\61\2\2\u012c\u012d\5\64\33\2")
        buf.write("\u012d\u012e\7\62\2\2\u012e\63\3\2\2\2\u012f\u0130\5\66")
        buf.write("\34\2\u0130\u0131\7\65\2\2\u0131\u0132\5\64\33\2\u0132")
        buf.write("\u0135\3\2\2\2\u0133\u0135\5\66\34\2\u0134\u012f\3\2\2")
        buf.write("\2\u0134\u0133\3\2\2\2\u0135\65\3\2\2\2\u0136\u013a\5")
        buf.write("(\25\2\u0137\u013a\58\35\2\u0138\u013a\5\62\32\2\u0139")
        buf.write("\u0136\3\2\2\2\u0139\u0137\3\2\2\2\u0139\u0138\3\2\2\2")
        buf.write("\u013a\67\3\2\2\2\u013b\u013c\7\67\2\2\u013c\u013d\7\61")
        buf.write("\2\2\u013d\u013e\5:\36\2\u013e\u013f\7\62\2\2\u013f9\3")
        buf.write("\2\2\2\u0140\u0143\5<\37\2\u0141\u0143\3\2\2\2\u0142\u0140")
        buf.write("\3\2\2\2\u0142\u0141\3\2\2\2\u0143;\3\2\2\2\u0144\u0145")
        buf.write("\5> \2\u0145\u0146\7\65\2\2\u0146\u0147\5<\37\2\u0147")
        buf.write("\u014a\3\2\2\2\u0148\u014a\5> \2\u0149\u0144\3\2\2\2\u0149")
        buf.write("\u0148\3\2\2\2\u014a=\3\2\2\2\u014b\u014c\7\67\2\2\u014c")
        buf.write("\u014d\7.\2\2\u014d\u014e\5H%\2\u014e?\3\2\2\2\u014f\u0150")
        buf.write("\7\67\2\2\u0150\u0151\7/\2\2\u0151\u0152\5B\"\2\u0152")
        buf.write("\u0153\7\60\2\2\u0153A\3\2\2\2\u0154\u0157\5D#\2\u0155")
        buf.write("\u0157\3\2\2\2\u0156\u0154\3\2\2\2\u0156\u0155\3\2\2\2")
        buf.write("\u0157C\3\2\2\2\u0158\u0159\5F$\2\u0159\u015a\7\65\2\2")
        buf.write("\u015a\u015b\5D#\2\u015b\u015e\3\2\2\2\u015c\u015e\5F")
        buf.write("$\2\u015d\u0158\3\2\2\2\u015d\u015c\3\2\2\2\u015eE\3\2")
        buf.write("\2\2\u015f\u0162\5H%\2\u0160\u0162\5\62\32\2\u0161\u015f")
        buf.write("\3\2\2\2\u0161\u0160\3\2\2\2\u0162G\3\2\2\2\u0163\u0164")
        buf.write("\b%\1\2\u0164\u0165\5J&\2\u0165\u016b\3\2\2\2\u0166\u0167")
        buf.write("\f\4\2\2\u0167\u0168\7$\2\2\u0168\u016a\5J&\2\u0169\u0166")
        buf.write("\3\2\2\2\u016a\u016d\3\2\2\2\u016b\u0169\3\2\2\2\u016b")
        buf.write("\u016c\3\2\2\2\u016cI\3\2\2\2\u016d\u016b\3\2\2\2\u016e")
        buf.write("\u016f\b&\1\2\u016f\u0170\5L\'\2\u0170\u0176\3\2\2\2\u0171")
        buf.write("\u0172\f\4\2\2\u0172\u0173\7#\2\2\u0173\u0175\5L\'\2\u0174")
        buf.write("\u0171\3\2\2\2\u0175\u0178\3\2\2\2\u0176\u0174\3\2\2\2")
        buf.write("\u0176\u0177\3\2\2\2\u0177K\3\2\2\2\u0178\u0176\3\2\2")
        buf.write("\2\u0179\u017a\b\'\1\2\u017a\u017b\5N(\2\u017b\u0181\3")
        buf.write("\2\2\2\u017c\u017d\f\4\2\2\u017d\u017e\t\5\2\2\u017e\u0180")
        buf.write("\5N(\2\u017f\u017c\3\2\2\2\u0180\u0183\3\2\2\2\u0181\u017f")
        buf.write("\3\2\2\2\u0181\u0182\3\2\2\2\u0182M\3\2\2\2\u0183\u0181")
        buf.write("\3\2\2\2\u0184\u0185\b(\1\2\u0185\u0186\5P)\2\u0186\u018c")
        buf.write("\3\2\2\2\u0187\u0188\f\4\2\2\u0188\u0189\t\6\2\2\u0189")
        buf.write("\u018b\5P)\2\u018a\u0187\3\2\2\2\u018b\u018e\3\2\2\2\u018c")
        buf.write("\u018a\3\2\2\2\u018c\u018d\3\2\2\2\u018dO\3\2\2\2\u018e")
        buf.write("\u018c\3\2\2\2\u018f\u0190\b)\1\2\u0190\u0191\5R*\2\u0191")
        buf.write("\u0197\3\2\2\2\u0192\u0193\f\4\2\2\u0193\u0194\t\7\2\2")
        buf.write("\u0194\u0196\5R*\2\u0195\u0192\3\2\2\2\u0196\u0199\3\2")
        buf.write("\2\2\u0197\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198Q\3")
        buf.write("\2\2\2\u0199\u0197\3\2\2\2\u019a\u019b\t\b\2\2\u019b\u019e")
        buf.write("\5R*\2\u019c\u019e\5T+\2\u019d\u019a\3\2\2\2\u019d\u019c")
        buf.write("\3\2\2\2\u019eS\3\2\2\2\u019f\u01a0\b+\1\2\u01a0\u01a1")
        buf.write("\5V,\2\u01a1\u01af\3\2\2\2\u01a2\u01a3\f\6\2\2\u01a3\u01a4")
        buf.write("\7\63\2\2\u01a4\u01a5\5H%\2\u01a5\u01a6\7\64\2\2\u01a6")
        buf.write("\u01ae\3\2\2\2\u01a7\u01a8\f\5\2\2\u01a8\u01a9\7-\2\2")
        buf.write("\u01a9\u01ae\7\67\2\2\u01aa\u01ab\f\4\2\2\u01ab\u01ac")
        buf.write("\7-\2\2\u01ac\u01ae\5@!\2\u01ad\u01a2\3\2\2\2\u01ad\u01a7")
        buf.write("\3\2\2\2\u01ad\u01aa\3\2\2\2\u01ae\u01b1\3\2\2\2\u01af")
        buf.write("\u01ad\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0U\3\2\2\2\u01b1")
        buf.write("\u01af\3\2\2\2\u01b2\u01b3\7/\2\2\u01b3\u01b4\5H%\2\u01b4")
        buf.write("\u01b5\7\60\2\2\u01b5\u01b8\3\2\2\2\u01b6\u01b8\5X-\2")
        buf.write("\u01b7\u01b2\3\2\2\2\u01b7\u01b6\3\2\2\2\u01b8W\3\2\2")
        buf.write("\2\u01b9\u01c5\5Z.\2\u01ba\u01c5\5@!\2\u01bb\u01c1\7\67")
        buf.write("\2\2\u01bc\u01bd\7\61\2\2\u01bd\u01be\5:\36\2\u01be\u01bf")
        buf.write("\7\62\2\2\u01bf\u01c2\3\2\2\2\u01c0\u01c2\3\2\2\2\u01c1")
        buf.write("\u01bc\3\2\2\2\u01c1\u01c0\3\2\2\2\u01c2\u01c5\3\2\2\2")
        buf.write("\u01c3\u01c5\7\67\2\2\u01c4\u01b9\3\2\2\2\u01c4\u01ba")
        buf.write("\3\2\2\2\u01c4\u01bb\3\2\2\2\u01c4\u01c3\3\2\2\2\u01c5")
        buf.write("Y\3\2\2\2\u01c6\u01ca\5(\25\2\u01c7\u01ca\5\60\31\2\u01c8")
        buf.write("\u01ca\58\35\2\u01c9\u01c6\3\2\2\2\u01c9\u01c7\3\2\2\2")
        buf.write("\u01c9\u01c8\3\2\2\2\u01ca[\3\2\2\2\u01cb\u01d5\5`\61")
        buf.write("\2\u01cc\u01d5\5b\62\2\u01cd\u01d5\5d\63\2\u01ce\u01d5")
        buf.write("\5l\67\2\u01cf\u01d5\5r:\2\u01d0\u01d5\5\u0084C\2\u01d1")
        buf.write("\u01d5\5\u0086D\2\u01d2\u01d5\5\u0088E\2\u01d3\u01d5\5")
        buf.write("\u008aF\2\u01d4\u01cb\3\2\2\2\u01d4\u01cc\3\2\2\2\u01d4")
        buf.write("\u01cd\3\2\2\2\u01d4\u01ce\3\2\2\2\u01d4\u01cf\3\2\2\2")
        buf.write("\u01d4\u01d0\3\2\2\2\u01d4\u01d1\3\2\2\2\u01d4\u01d2\3")
        buf.write("\2\2\2\u01d4\u01d3\3\2\2\2\u01d5\u01d6\3\2\2\2\u01d6\u01d7")
        buf.write("\7\66\2\2\u01d7]\3\2\2\2\u01d8\u01d9\5\\/\2\u01d9\u01da")
        buf.write("\5^\60\2\u01da\u01dd\3\2\2\2\u01db\u01dd\5\\/\2\u01dc")
        buf.write("\u01d8\3\2\2\2\u01dc\u01db\3\2\2\2\u01dd_\3\2\2\2\u01de")
        buf.write("\u01df\7\21\2\2\u01df\u01e7\7\67\2\2\u01e0\u01e1\5\6\4")
        buf.write("\2\u01e1\u01e2\7&\2\2\u01e2\u01e3\5H%\2\u01e3\u01e8\3")
        buf.write("\2\2\2\u01e4\u01e5\7&\2\2\u01e5\u01e8\5H%\2\u01e6\u01e8")
        buf.write("\5\6\4\2\u01e7\u01e0\3\2\2\2\u01e7\u01e4\3\2\2\2\u01e7")
        buf.write("\u01e6\3\2\2\2\u01e8a\3\2\2\2\u01e9\u01ea\7\20\2\2\u01ea")
        buf.write("\u01eb\7\67\2\2\u01eb\u01ee\7&\2\2\u01ec\u01ef\5(\25\2")
        buf.write("\u01ed\u01ef\5H%\2\u01ee\u01ec\3\2\2\2\u01ee\u01ed\3\2")
        buf.write("\2\2\u01efc\3\2\2\2\u01f0\u01f1\5f\64\2\u01f1\u01f2\5")
        buf.write("h\65\2\u01f2\u01f3\5j\66\2\u01f3e\3\2\2\2\u01f4\u01f5")
        buf.write("\b\64\1\2\u01f5\u01f6\7\67\2\2\u01f6\u0201\3\2\2\2\u01f7")
        buf.write("\u01f8\f\5\2\2\u01f8\u01f9\7\63\2\2\u01f9\u01fa\5H%\2")
        buf.write("\u01fa\u01fb\7\64\2\2\u01fb\u0200\3\2\2\2\u01fc\u01fd")
        buf.write("\f\4\2\2\u01fd\u01fe\7-\2\2\u01fe\u0200\7\67\2\2\u01ff")
        buf.write("\u01f7\3\2\2\2\u01ff\u01fc\3\2\2\2\u0200\u0203\3\2\2\2")
        buf.write("\u0201\u01ff\3\2\2\2\u0201\u0202\3\2\2\2\u0202g\3\2\2")
        buf.write("\2\u0203\u0201\3\2\2\2\u0204\u0205\t\t\2\2\u0205i\3\2")
        buf.write("\2\2\u0206\u0207\5H%\2\u0207k\3\2\2\2\u0208\u0209\7\4")
        buf.write("\2\2\u0209\u020a\7/\2\2\u020a\u020b\5H%\2\u020b\u020c")
        buf.write("\7\60\2\2\u020c\u020d\7\61\2\2\u020d\u020e\5^\60\2\u020e")
        buf.write("\u020f\7\62\2\2\u020f\u0215\5n8\2\u0210\u0211\7\5\2\2")
        buf.write("\u0211\u0212\7\61\2\2\u0212\u0213\5^\60\2\u0213\u0214")
        buf.write("\7\62\2\2\u0214\u0216\3\2\2\2\u0215\u0210\3\2\2\2\u0215")
        buf.write("\u0216\3\2\2\2\u0216m\3\2\2\2\u0217\u0218\5p9\2\u0218")
        buf.write("\u0219\5n8\2\u0219\u021c\3\2\2\2\u021a\u021c\3\2\2\2\u021b")
        buf.write("\u0217\3\2\2\2\u021b\u021a\3\2\2\2\u021co\3\2\2\2\u021d")
        buf.write("\u021e\7\5\2\2\u021e\u021f\7\4\2\2\u021f\u0220\7/\2\2")
        buf.write("\u0220\u0221\5H%\2\u0221\u0222\7\60\2\2\u0222\u0223\7")
        buf.write("\61\2\2\u0223\u0224\5^\60\2\u0224\u0225\7\62\2\2\u0225")
        buf.write("q\3\2\2\2\u0226\u022a\5t;\2\u0227\u022a\5v<\2\u0228\u022a")
        buf.write("\5\u0082B\2\u0229\u0226\3\2\2\2\u0229\u0227\3\2\2\2\u0229")
        buf.write("\u0228\3\2\2\2\u022as\3\2\2\2\u022b\u022c\7\6\2\2\u022c")
        buf.write("\u022d\5H%\2\u022d\u022e\7\61\2\2\u022e\u022f\5^\60\2")
        buf.write("\u022f\u0230\7\62\2\2\u0230u\3\2\2\2\u0231\u0232\7\6\2")
        buf.write("\2\u0232\u0233\5x=\2\u0233\u0234\7\66\2\2\u0234\u0235")
        buf.write("\5|?\2\u0235\u0236\7\66\2\2\u0236\u0237\5~@\2\u0237\u0238")
        buf.write("\7\61\2\2\u0238\u0239\5^\60\2\u0239\u023a\7\62\2\2\u023a")
        buf.write("w\3\2\2\2\u023b\u023e\5\u0080A\2\u023c\u023e\5z>\2\u023d")
        buf.write("\u023b\3\2\2\2\u023d\u023c\3\2\2\2\u023ey\3\2\2\2\u023f")
        buf.write("\u0240\7\21\2\2\u0240\u0242\7\67\2\2\u0241\u0243\5\6\4")
        buf.write("\2\u0242\u0241\3\2\2\2\u0242\u0243\3\2\2\2\u0243\u0244")
        buf.write("\3\2\2\2\u0244\u0245\7&\2\2\u0245\u0246\5H%\2\u0246{\3")
        buf.write("\2\2\2\u0247\u0248\5H%\2\u0248}\3\2\2\2\u0249\u024a\5")
        buf.write("\u0080A\2\u024a\177\3\2\2\2\u024b\u024c\7\67\2\2\u024c")
        buf.write("\u024d\5h\65\2\u024d\u024e\5H%\2\u024e\u0081\3\2\2\2\u024f")
        buf.write("\u0250\7\6\2\2\u0250\u0251\t\n\2\2\u0251\u0252\7\65\2")
        buf.write("\2\u0252\u0253\7\67\2\2\u0253\u0254\7\'\2\2\u0254\u0255")
        buf.write("\7\24\2\2\u0255\u0256\5f\64\2\u0256\u0257\7\61\2\2\u0257")
        buf.write("\u0258\5^\60\2\u0258\u0259\7\62\2\2\u0259\u0083\3\2\2")
        buf.write("\2\u025a\u025b\7\23\2\2\u025b\u0085\3\2\2\2\u025c\u025d")
        buf.write("\7\22\2\2\u025d\u0087\3\2\2\2\u025e\u0264\5@!\2\u025f")
        buf.write("\u0260\5H%\2\u0260\u0261\7-\2\2\u0261\u0262\5@!\2\u0262")
        buf.write("\u0264\3\2\2\2\u0263\u025e\3\2\2\2\u0263\u025f\3\2\2\2")
        buf.write("\u0264\u0089\3\2\2\2\u0265\u0267\7\7\2\2\u0266\u0268\5")
        buf.write("H%\2\u0267\u0266\3\2\2\2\u0267\u0268\3\2\2\2\u0268\u008b")
        buf.write("\3\2\2\2\60\u008f\u0099\u00a1\u00ad\u00bd\u00d1\u00d8")
        buf.write("\u00de\u00e5\u00ee\u00f9\u0102\u010e\u0121\u0134\u0139")
        buf.write("\u0142\u0149\u0156\u015d\u0161\u016b\u0176\u0181\u018c")
        buf.write("\u0197\u019d\u01ad\u01af\u01b7\u01c1\u01c4\u01c9\u01d4")
        buf.write("\u01dc\u01e7\u01ee\u01ff\u0201\u0215\u021b\u0229\u023d")
        buf.write("\u0242\u0263\u0267")
        return buf.getvalue()


class MiniGoParser ( Parser ):

    grammarFileName = "MiniGo.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'_'", "'if'", "'else'", "'for'", "'return'", 
                     "'func'", "'type'", "'struct'", "'interface'", "'string'", 
                     "'int'", "'float'", "'boolean'", "'const'", "'var'", 
                     "'continue'", "'break'", "'range'", "'nil'", "'true'", 
                     "'false'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
                     "'!='", "'<'", "'<='", "'>'", "'>='", "'&&'", "'||'", 
                     "'!'", "'='", "':='", "'+='", "'-='", "'*='", "'/='", 
                     "'%='", "'.'", "':'", "'('", "')'", "'{'", "'}'", "'['", 
                     "']'", "','", "';'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "'\n'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "IF", "ELSE", "FOR", "RETURN", 
                      "FUNC", "TYPE", "STRUCT", "INTERFACE", "STRING", "INT", 
                      "FLOAT", "BOOLEAN", "CONST", "VAR", "CONTINUE", "BREAK", 
                      "RANGE", "NIL", "TRUE", "FALSE", "PLUS", "MINUS", 
                      "MULTI", "DIV", "MODULO", "EQUAL", "NOT_EQUAL", "LESS_THAN", 
                      "LESS_EQUAL", "GREATER_THAN", "GREATER_EQUAL", "AND", 
                      "OR", "NOT", "ASSIGN", "ASSIGN1", "PLUS_EQUAL", "MINUS_EQUAL", 
                      "MULTI_EQUAL", "DIV_EQUAL", "MODULO_EQUAL", "DOT", 
                      "COLON", "OPEN_ROUND", "CLOSE_ROUND", "OPEN_CURVE", 
                      "CLOSE_CURVE", "OPEN_SQUARE", "CLOSE_SQUARE", "COMMA", 
                      "SEMICOLON", "ID", "INT_LIT", "FLOAT_LIT", "STRING_LIT", 
                      "COMMENT_INLINE", "COMMENT_BLOCK", "NL", "WS", "ILLEGAL_ESCAPE", 
                      "UNCLOSE_STRING", "ERROR_CHAR" ]

    RULE_program = 0
    RULE_decl = 1
    RULE_typee = 2
    RULE_arrType = 3
    RULE_dimenList = 4
    RULE_structDecl = 5
    RULE_structBody = 6
    RULE_listField = 7
    RULE_field = 8
    RULE_interfaceDecl = 9
    RULE_interfaceBody = 10
    RULE_listMethod = 11
    RULE_method = 12
    RULE_paramList = 13
    RULE_paramPrime = 14
    RULE_param = 15
    RULE_nameList = 16
    RULE_varDecl = 17
    RULE_constDecl = 18
    RULE_literalConst = 19
    RULE_funcDecl = 20
    RULE_funcBody = 21
    RULE_methodStructDecl = 22
    RULE_arrLit = 23
    RULE_arrBody = 24
    RULE_elementList = 25
    RULE_element = 26
    RULE_structLit = 27
    RULE_structElList = 28
    RULE_structELPrime = 29
    RULE_structEL = 30
    RULE_funcCall = 31
    RULE_argumentList = 32
    RULE_argumentListPrime = 33
    RULE_argument = 34
    RULE_expr = 35
    RULE_expr1 = 36
    RULE_expr2 = 37
    RULE_expr3 = 38
    RULE_expr4 = 39
    RULE_expr5 = 40
    RULE_expr6 = 41
    RULE_expr7 = 42
    RULE_operand = 43
    RULE_literal = 44
    RULE_statement = 45
    RULE_statementList = 46
    RULE_varDeclStatement = 47
    RULE_constDeclStatement = 48
    RULE_assignment = 49
    RULE_lhs = 50
    RULE_assignOperator = 51
    RULE_rhs = 52
    RULE_ifStatement = 53
    RULE_elifList = 54
    RULE_eliff = 55
    RULE_forStatement = 56
    RULE_forBasic = 57
    RULE_forInitial = 58
    RULE_initialization = 59
    RULE_varDeclInitial = 60
    RULE_condition = 61
    RULE_update = 62
    RULE_assignScalar = 63
    RULE_forRange = 64
    RULE_breakStatement = 65
    RULE_continueStatement = 66
    RULE_callStatement = 67
    RULE_returnStatement = 68

    ruleNames =  [ "program", "decl", "typee", "arrType", "dimenList", "structDecl", 
                   "structBody", "listField", "field", "interfaceDecl", 
                   "interfaceBody", "listMethod", "method", "paramList", 
                   "paramPrime", "param", "nameList", "varDecl", "constDecl", 
                   "literalConst", "funcDecl", "funcBody", "methodStructDecl", 
                   "arrLit", "arrBody", "elementList", "element", "structLit", 
                   "structElList", "structELPrime", "structEL", "funcCall", 
                   "argumentList", "argumentListPrime", "argument", "expr", 
                   "expr1", "expr2", "expr3", "expr4", "expr5", "expr6", 
                   "expr7", "operand", "literal", "statement", "statementList", 
                   "varDeclStatement", "constDeclStatement", "assignment", 
                   "lhs", "assignOperator", "rhs", "ifStatement", "elifList", 
                   "eliff", "forStatement", "forBasic", "forInitial", "initialization", 
                   "varDeclInitial", "condition", "update", "assignScalar", 
                   "forRange", "breakStatement", "continueStatement", "callStatement", 
                   "returnStatement" ]

    EOF = Token.EOF
    T__0=1
    IF=2
    ELSE=3
    FOR=4
    RETURN=5
    FUNC=6
    TYPE=7
    STRUCT=8
    INTERFACE=9
    STRING=10
    INT=11
    FLOAT=12
    BOOLEAN=13
    CONST=14
    VAR=15
    CONTINUE=16
    BREAK=17
    RANGE=18
    NIL=19
    TRUE=20
    FALSE=21
    PLUS=22
    MINUS=23
    MULTI=24
    DIV=25
    MODULO=26
    EQUAL=27
    NOT_EQUAL=28
    LESS_THAN=29
    LESS_EQUAL=30
    GREATER_THAN=31
    GREATER_EQUAL=32
    AND=33
    OR=34
    NOT=35
    ASSIGN=36
    ASSIGN1=37
    PLUS_EQUAL=38
    MINUS_EQUAL=39
    MULTI_EQUAL=40
    DIV_EQUAL=41
    MODULO_EQUAL=42
    DOT=43
    COLON=44
    OPEN_ROUND=45
    CLOSE_ROUND=46
    OPEN_CURVE=47
    CLOSE_CURVE=48
    OPEN_SQUARE=49
    CLOSE_SQUARE=50
    COMMA=51
    SEMICOLON=52
    ID=53
    INT_LIT=54
    FLOAT_LIT=55
    STRING_LIT=56
    COMMENT_INLINE=57
    COMMENT_BLOCK=58
    NL=59
    WS=60
    ILLEGAL_ESCAPE=61
    UNCLOSE_STRING=62
    ERROR_CHAR=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(MiniGoParser.EOF, 0)

        def decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.DeclContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.DeclContext,i)


        def getRuleIndex(self):
            return MiniGoParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = MiniGoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 138
                self.decl()
                self.state = 141 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR))) != 0)):
                    break

            self.state = 143
            self.match(MiniGoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structDecl(self):
            return self.getTypedRuleContext(MiniGoParser.StructDeclContext,0)


        def interfaceDecl(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceDeclContext,0)


        def varDecl(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclContext,0)


        def constDecl(self):
            return self.getTypedRuleContext(MiniGoParser.ConstDeclContext,0)


        def funcDecl(self):
            return self.getTypedRuleContext(MiniGoParser.FuncDeclContext,0)


        def methodStructDecl(self):
            return self.getTypedRuleContext(MiniGoParser.MethodStructDeclContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_decl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDecl" ):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = MiniGoParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_decl)
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 145
                self.structDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 146
                self.interfaceDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 147
                self.varDecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 148
                self.constDecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 149
                self.funcDecl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 150
                self.methodStructDecl()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def arrType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrTypeContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_typee

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypee" ):
                return visitor.visitTypee(self)
            else:
                return visitor.visitChildren(self)




    def typee(self):

        localctx = MiniGoParser.TypeeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_typee)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 159
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT]:
                self.state = 153
                self.match(MiniGoParser.INT)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.state = 154
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.state = 155
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.STRING]:
                self.state = 156
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.OPEN_SQUARE]:
                self.state = 157
                self.arrType()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 158
                self.match(MiniGoParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrTypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dimenList(self):
            return self.getTypedRuleContext(MiniGoParser.DimenListContext,0)


        def INT(self):
            return self.getToken(MiniGoParser.INT, 0)

        def FLOAT(self):
            return self.getToken(MiniGoParser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(MiniGoParser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(MiniGoParser.STRING, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrType

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrType" ):
                return visitor.visitArrType(self)
            else:
                return visitor.visitChildren(self)




    def arrType(self):

        localctx = MiniGoParser.ArrTypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_arrType)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 161
            self.dimenList()
            self.state = 162
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.ID))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DimenListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_SQUARE(self):
            return self.getToken(MiniGoParser.OPEN_SQUARE, 0)

        def CLOSE_SQUARE(self):
            return self.getToken(MiniGoParser.CLOSE_SQUARE, 0)

        def dimenList(self):
            return self.getTypedRuleContext(MiniGoParser.DimenListContext,0)


        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_dimenList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDimenList" ):
                return visitor.visitDimenList(self)
            else:
                return visitor.visitChildren(self)




    def dimenList(self):

        localctx = MiniGoParser.DimenListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_dimenList)
        self._la = 0 # Token type
        try:
            self.state = 171
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 164
                self.match(MiniGoParser.OPEN_SQUARE)
                self.state = 165
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.ID or _la==MiniGoParser.INT_LIT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 166
                self.match(MiniGoParser.CLOSE_SQUARE)
                self.state = 167
                self.dimenList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.match(MiniGoParser.OPEN_SQUARE)
                self.state = 169
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.ID or _la==MiniGoParser.INT_LIT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 170
                self.match(MiniGoParser.CLOSE_SQUARE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def STRUCT(self):
            return self.getToken(MiniGoParser.STRUCT, 0)

        def OPEN_CURVE(self):
            return self.getToken(MiniGoParser.OPEN_CURVE, 0)

        def structBody(self):
            return self.getTypedRuleContext(MiniGoParser.StructBodyContext,0)


        def CLOSE_CURVE(self):
            return self.getToken(MiniGoParser.CLOSE_CURVE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructDecl" ):
                return visitor.visitStructDecl(self)
            else:
                return visitor.visitChildren(self)




    def structDecl(self):

        localctx = MiniGoParser.StructDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_structDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(MiniGoParser.TYPE)
            self.state = 174
            self.match(MiniGoParser.ID)
            self.state = 175
            self.match(MiniGoParser.STRUCT)
            self.state = 176
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 177
            self.structBody()
            self.state = 178
            self.match(MiniGoParser.CLOSE_CURVE)
            self.state = 179
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listField(self):
            return self.getTypedRuleContext(MiniGoParser.ListFieldContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structBody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructBody" ):
                return visitor.visitStructBody(self)
            else:
                return visitor.visitChildren(self)




    def structBody(self):

        localctx = MiniGoParser.StructBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_structBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 181
            self.listField()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListFieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def field(self):
            return self.getTypedRuleContext(MiniGoParser.FieldContext,0)


        def listField(self):
            return self.getTypedRuleContext(MiniGoParser.ListFieldContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_listField

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListField" ):
                return visitor.visitListField(self)
            else:
                return visitor.visitChildren(self)




    def listField(self):

        localctx = MiniGoParser.ListFieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_listField)
        try:
            self.state = 187
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.field()
                self.state = 184
                self.listField()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.field()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FieldContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def typee(self):
            return self.getTypedRuleContext(MiniGoParser.TypeeContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_field

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitField" ):
                return visitor.visitField(self)
            else:
                return visitor.visitChildren(self)




    def field(self):

        localctx = MiniGoParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_field)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            self.match(MiniGoParser.ID)
            self.state = 190
            self.typee()
            self.state = 191
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE(self):
            return self.getToken(MiniGoParser.TYPE, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def INTERFACE(self):
            return self.getToken(MiniGoParser.INTERFACE, 0)

        def OPEN_CURVE(self):
            return self.getToken(MiniGoParser.OPEN_CURVE, 0)

        def interfaceBody(self):
            return self.getTypedRuleContext(MiniGoParser.InterfaceBodyContext,0)


        def CLOSE_CURVE(self):
            return self.getToken(MiniGoParser.CLOSE_CURVE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceDecl" ):
                return visitor.visitInterfaceDecl(self)
            else:
                return visitor.visitChildren(self)




    def interfaceDecl(self):

        localctx = MiniGoParser.InterfaceDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_interfaceDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(MiniGoParser.TYPE)
            self.state = 194
            self.match(MiniGoParser.ID)
            self.state = 195
            self.match(MiniGoParser.INTERFACE)
            self.state = 196
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 197
            self.interfaceBody()
            self.state = 198
            self.match(MiniGoParser.CLOSE_CURVE)
            self.state = 199
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InterfaceBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listMethod(self):
            return self.getTypedRuleContext(MiniGoParser.ListMethodContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_interfaceBody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInterfaceBody" ):
                return visitor.visitInterfaceBody(self)
            else:
                return visitor.visitChildren(self)




    def interfaceBody(self):

        localctx = MiniGoParser.InterfaceBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_interfaceBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.listMethod()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListMethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def method(self):
            return self.getTypedRuleContext(MiniGoParser.MethodContext,0)


        def listMethod(self):
            return self.getTypedRuleContext(MiniGoParser.ListMethodContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_listMethod

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitListMethod" ):
                return visitor.visitListMethod(self)
            else:
                return visitor.visitChildren(self)




    def listMethod(self):

        localctx = MiniGoParser.ListMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_listMethod)
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.method()
                self.state = 204
                self.listMethod()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
                self.method()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def OPEN_ROUND(self):
            return self.getToken(MiniGoParser.OPEN_ROUND, 0)

        def paramList(self):
            return self.getTypedRuleContext(MiniGoParser.ParamListContext,0)


        def CLOSE_ROUND(self):
            return self.getToken(MiniGoParser.CLOSE_ROUND, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def typee(self):
            return self.getTypedRuleContext(MiniGoParser.TypeeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_method

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethod" ):
                return visitor.visitMethod(self)
            else:
                return visitor.visitChildren(self)




    def method(self):

        localctx = MiniGoParser.MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(MiniGoParser.ID)
            self.state = 210
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 211
            self.paramList()
            self.state = 212
            self.match(MiniGoParser.CLOSE_ROUND)
            self.state = 214
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.OPEN_SQUARE) | (1 << MiniGoParser.ID))) != 0):
                self.state = 213
                self.typee()


            self.state = 216
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramPrime(self):
            return self.getTypedRuleContext(MiniGoParser.ParamPrimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = MiniGoParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_paramList)
        try:
            self.state = 220
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 218
                self.paramPrime()
                pass
            elif token in [MiniGoParser.CLOSE_ROUND]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self):
            return self.getTypedRuleContext(MiniGoParser.ParamContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def paramPrime(self):
            return self.getTypedRuleContext(MiniGoParser.ParamPrimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramPrime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamPrime" ):
                return visitor.visitParamPrime(self)
            else:
                return visitor.visitChildren(self)




    def paramPrime(self):

        localctx = MiniGoParser.ParamPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_paramPrime)
        try:
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.param()
                self.state = 223
                self.match(MiniGoParser.COMMA)
                self.state = 224
                self.paramPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.param()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def nameList(self):
            return self.getTypedRuleContext(MiniGoParser.NameListContext,0)


        def typee(self):
            return self.getTypedRuleContext(MiniGoParser.TypeeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_param

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = MiniGoParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.nameList()
            self.state = 230
            self.typee()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NameListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def nameList(self):
            return self.getTypedRuleContext(MiniGoParser.NameListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_nameList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNameList" ):
                return visitor.visitNameList(self)
            else:
                return visitor.visitChildren(self)




    def nameList(self):

        localctx = MiniGoParser.NameListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_nameList)
        try:
            self.state = 236
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.match(MiniGoParser.ID)
                self.state = 233
                self.match(MiniGoParser.COMMA)
                self.state = 234
                self.nameList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def typee(self):
            return self.getTypedRuleContext(MiniGoParser.TypeeContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_varDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDecl" ):
                return visitor.visitVarDecl(self)
            else:
                return visitor.visitChildren(self)




    def varDecl(self):

        localctx = MiniGoParser.VarDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_varDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self.match(MiniGoParser.VAR)
            self.state = 239
            self.match(MiniGoParser.ID)
            self.state = 247
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 240
                self.typee()
                self.state = 241
                self.match(MiniGoParser.ASSIGN)
                self.state = 242
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 244
                self.match(MiniGoParser.ASSIGN)
                self.state = 245
                self.expr(0)
                pass

            elif la_ == 3:
                self.state = 246
                self.typee()
                pass


            self.state = 249
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def literalConst(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralConstContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstDecl" ):
                return visitor.visitConstDecl(self)
            else:
                return visitor.visitChildren(self)




    def constDecl(self):

        localctx = MiniGoParser.ConstDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_constDecl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(MiniGoParser.CONST)
            self.state = 252
            self.match(MiniGoParser.ID)
            self.state = 253
            self.match(MiniGoParser.ASSIGN)
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 254
                self.literalConst()
                pass

            elif la_ == 2:
                self.state = 255
                self.expr(0)
                pass


            self.state = 258
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralConstContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(MiniGoParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(MiniGoParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(MiniGoParser.STRING_LIT, 0)

        def TRUE(self):
            return self.getToken(MiniGoParser.TRUE, 0)

        def FALSE(self):
            return self.getToken(MiniGoParser.FALSE, 0)

        def NIL(self):
            return self.getToken(MiniGoParser.NIL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_literalConst

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteralConst" ):
                return visitor.visitLiteralConst(self)
            else:
                return visitor.visitChildren(self)




    def literalConst(self):

        localctx = MiniGoParser.LiteralConstContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_literalConst)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def OPEN_ROUND(self):
            return self.getToken(MiniGoParser.OPEN_ROUND, 0)

        def paramList(self):
            return self.getTypedRuleContext(MiniGoParser.ParamListContext,0)


        def CLOSE_ROUND(self):
            return self.getToken(MiniGoParser.CLOSE_ROUND, 0)

        def OPEN_CURVE(self):
            return self.getToken(MiniGoParser.OPEN_CURVE, 0)

        def funcBody(self):
            return self.getTypedRuleContext(MiniGoParser.FuncBodyContext,0)


        def CLOSE_CURVE(self):
            return self.getToken(MiniGoParser.CLOSE_CURVE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def typee(self):
            return self.getTypedRuleContext(MiniGoParser.TypeeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncDecl" ):
                return visitor.visitFuncDecl(self)
            else:
                return visitor.visitChildren(self)




    def funcDecl(self):

        localctx = MiniGoParser.FuncDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_funcDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 262
            self.match(MiniGoParser.FUNC)
            self.state = 263
            self.match(MiniGoParser.ID)
            self.state = 264
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 265
            self.paramList()
            self.state = 266
            self.match(MiniGoParser.CLOSE_ROUND)
            self.state = 268
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.OPEN_SQUARE) | (1 << MiniGoParser.ID))) != 0):
                self.state = 267
                self.typee()


            self.state = 270
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 271
            self.funcBody()
            self.state = 272
            self.match(MiniGoParser.CLOSE_CURVE)
            self.state = 273
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementList(self):
            return self.getTypedRuleContext(MiniGoParser.StatementListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_funcBody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncBody" ):
                return visitor.visitFuncBody(self)
            else:
                return visitor.visitChildren(self)




    def funcBody(self):

        localctx = MiniGoParser.FuncBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_funcBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.statementList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MethodStructDeclContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNC(self):
            return self.getToken(MiniGoParser.FUNC, 0)

        def OPEN_ROUND(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.OPEN_ROUND)
            else:
                return self.getToken(MiniGoParser.OPEN_ROUND, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def CLOSE_ROUND(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.CLOSE_ROUND)
            else:
                return self.getToken(MiniGoParser.CLOSE_ROUND, i)

        def paramList(self):
            return self.getTypedRuleContext(MiniGoParser.ParamListContext,0)


        def OPEN_CURVE(self):
            return self.getToken(MiniGoParser.OPEN_CURVE, 0)

        def funcBody(self):
            return self.getTypedRuleContext(MiniGoParser.FuncBodyContext,0)


        def CLOSE_CURVE(self):
            return self.getToken(MiniGoParser.CLOSE_CURVE, 0)

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def typee(self):
            return self.getTypedRuleContext(MiniGoParser.TypeeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_methodStructDecl

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodStructDecl" ):
                return visitor.visitMethodStructDecl(self)
            else:
                return visitor.visitChildren(self)




    def methodStructDecl(self):

        localctx = MiniGoParser.MethodStructDeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_methodStructDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
            self.match(MiniGoParser.FUNC)
            self.state = 278
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 279
            self.match(MiniGoParser.ID)
            self.state = 280
            self.match(MiniGoParser.ID)
            self.state = 281
            self.match(MiniGoParser.CLOSE_ROUND)
            self.state = 282
            self.match(MiniGoParser.ID)
            self.state = 283
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 284
            self.paramList()
            self.state = 285
            self.match(MiniGoParser.CLOSE_ROUND)
            self.state = 287
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.OPEN_SQUARE) | (1 << MiniGoParser.ID))) != 0):
                self.state = 286
                self.typee()


            self.state = 289
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 290
            self.funcBody()
            self.state = 291
            self.match(MiniGoParser.CLOSE_CURVE)
            self.state = 292
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arrType(self):
            return self.getTypedRuleContext(MiniGoParser.ArrTypeContext,0)


        def arrBody(self):
            return self.getTypedRuleContext(MiniGoParser.ArrBodyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrLit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrLit" ):
                return visitor.visitArrLit(self)
            else:
                return visitor.visitChildren(self)




    def arrLit(self):

        localctx = MiniGoParser.ArrLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_arrLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self.arrType()
            self.state = 295
            self.arrBody()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrBodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_CURVE(self):
            return self.getToken(MiniGoParser.OPEN_CURVE, 0)

        def elementList(self):
            return self.getTypedRuleContext(MiniGoParser.ElementListContext,0)


        def CLOSE_CURVE(self):
            return self.getToken(MiniGoParser.CLOSE_CURVE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_arrBody

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrBody" ):
                return visitor.visitArrBody(self)
            else:
                return visitor.visitChildren(self)




    def arrBody(self):

        localctx = MiniGoParser.ArrBodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_arrBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 298
            self.elementList()
            self.state = 299
            self.match(MiniGoParser.CLOSE_CURVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element(self):
            return self.getTypedRuleContext(MiniGoParser.ElementContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def elementList(self):
            return self.getTypedRuleContext(MiniGoParser.ElementListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elementList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElementList" ):
                return visitor.visitElementList(self)
            else:
                return visitor.visitChildren(self)




    def elementList(self):

        localctx = MiniGoParser.ElementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_elementList)
        try:
            self.state = 306
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self.element()
                self.state = 302
                self.match(MiniGoParser.COMMA)
                self.state = 303
                self.elementList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
                self.element()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literalConst(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralConstContext,0)


        def structLit(self):
            return self.getTypedRuleContext(MiniGoParser.StructLitContext,0)


        def arrBody(self):
            return self.getTypedRuleContext(MiniGoParser.ArrBodyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_element

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElement" ):
                return visitor.visitElement(self)
            else:
                return visitor.visitChildren(self)




    def element(self):

        localctx = MiniGoParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_element)
        try:
            self.state = 311
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 308
                self.literalConst()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
                self.structLit()
                pass
            elif token in [MiniGoParser.OPEN_CURVE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 310
                self.arrBody()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructLitContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def OPEN_CURVE(self):
            return self.getToken(MiniGoParser.OPEN_CURVE, 0)

        def structElList(self):
            return self.getTypedRuleContext(MiniGoParser.StructElListContext,0)


        def CLOSE_CURVE(self):
            return self.getToken(MiniGoParser.CLOSE_CURVE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structLit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructLit" ):
                return visitor.visitStructLit(self)
            else:
                return visitor.visitChildren(self)




    def structLit(self):

        localctx = MiniGoParser.StructLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_structLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 313
            self.match(MiniGoParser.ID)
            self.state = 314
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 315
            self.structElList()
            self.state = 316
            self.match(MiniGoParser.CLOSE_CURVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructElListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structELPrime(self):
            return self.getTypedRuleContext(MiniGoParser.StructELPrimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structElList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructElList" ):
                return visitor.visitStructElList(self)
            else:
                return visitor.visitChildren(self)




    def structElList(self):

        localctx = MiniGoParser.StructElListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_structElList)
        try:
            self.state = 320
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 318
                self.structELPrime()
                pass
            elif token in [MiniGoParser.CLOSE_CURVE]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructELPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def structEL(self):
            return self.getTypedRuleContext(MiniGoParser.StructELContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def structELPrime(self):
            return self.getTypedRuleContext(MiniGoParser.StructELPrimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structELPrime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructELPrime" ):
                return visitor.visitStructELPrime(self)
            else:
                return visitor.visitChildren(self)




    def structELPrime(self):

        localctx = MiniGoParser.StructELPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_structELPrime)
        try:
            self.state = 327
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 322
                self.structEL()
                self.state = 323
                self.match(MiniGoParser.COMMA)
                self.state = 324
                self.structELPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 326
                self.structEL()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructELContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def COLON(self):
            return self.getToken(MiniGoParser.COLON, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_structEL

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructEL" ):
                return visitor.visitStructEL(self)
            else:
                return visitor.visitChildren(self)




    def structEL(self):

        localctx = MiniGoParser.StructELContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_structEL)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(MiniGoParser.ID)
            self.state = 330
            self.match(MiniGoParser.COLON)
            self.state = 331
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def OPEN_ROUND(self):
            return self.getToken(MiniGoParser.OPEN_ROUND, 0)

        def argumentList(self):
            return self.getTypedRuleContext(MiniGoParser.ArgumentListContext,0)


        def CLOSE_ROUND(self):
            return self.getToken(MiniGoParser.CLOSE_ROUND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_funcCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncCall" ):
                return visitor.visitFuncCall(self)
            else:
                return visitor.visitChildren(self)




    def funcCall(self):

        localctx = MiniGoParser.FuncCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_funcCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            self.match(MiniGoParser.ID)
            self.state = 334
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 335
            self.argumentList()
            self.state = 336
            self.match(MiniGoParser.CLOSE_ROUND)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argumentListPrime(self):
            return self.getTypedRuleContext(MiniGoParser.ArgumentListPrimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_argumentList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = MiniGoParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_argumentList)
        try:
            self.state = 340
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.MINUS, MiniGoParser.NOT, MiniGoParser.OPEN_ROUND, MiniGoParser.OPEN_CURVE, MiniGoParser.OPEN_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 338
                self.argumentListPrime()
                pass
            elif token in [MiniGoParser.CLOSE_ROUND]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def argument(self):
            return self.getTypedRuleContext(MiniGoParser.ArgumentContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def argumentListPrime(self):
            return self.getTypedRuleContext(MiniGoParser.ArgumentListPrimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_argumentListPrime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentListPrime" ):
                return visitor.visitArgumentListPrime(self)
            else:
                return visitor.visitChildren(self)




    def argumentListPrime(self):

        localctx = MiniGoParser.ArgumentListPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_argumentListPrime)
        try:
            self.state = 347
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                self.argument()
                self.state = 343
                self.match(MiniGoParser.COMMA)
                self.state = 344
                self.argumentListPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 346
                self.argument()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def arrBody(self):
            return self.getTypedRuleContext(MiniGoParser.ArrBodyContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_argument

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgument" ):
                return visitor.visitArgument(self)
            else:
                return visitor.visitChildren(self)




    def argument(self):

        localctx = MiniGoParser.ArgumentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_argument)
        try:
            self.state = 351
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.MINUS, MiniGoParser.NOT, MiniGoParser.OPEN_ROUND, MiniGoParser.OPEN_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 349
                self.expr(0)
                pass
            elif token in [MiniGoParser.OPEN_CURVE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 350
                self.arrBody()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 361
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 356
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 357
                    self.match(MiniGoParser.OR)
                    self.state = 358
                    self.expr1(0) 
                self.state = 363
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def expr1(self):
            return self.getTypedRuleContext(MiniGoParser.Expr1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr1" ):
                return visitor.visitExpr1(self)
            else:
                return visitor.visitChildren(self)



    def expr1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 372
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 367
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 368
                    self.match(MiniGoParser.AND)
                    self.state = 369
                    self.expr2(0) 
                self.state = 374
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def expr2(self):
            return self.getTypedRuleContext(MiniGoParser.Expr2Context,0)


        def EQUAL(self):
            return self.getToken(MiniGoParser.EQUAL, 0)

        def NOT_EQUAL(self):
            return self.getToken(MiniGoParser.NOT_EQUAL, 0)

        def LESS_THAN(self):
            return self.getToken(MiniGoParser.LESS_THAN, 0)

        def LESS_EQUAL(self):
            return self.getToken(MiniGoParser.LESS_EQUAL, 0)

        def GREATER_THAN(self):
            return self.getToken(MiniGoParser.GREATER_THAN, 0)

        def GREATER_EQUAL(self):
            return self.getToken(MiniGoParser.GREATER_EQUAL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr2" ):
                return visitor.visitExpr2(self)
            else:
                return visitor.visitChildren(self)



    def expr2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 383
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 378
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 379
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUAL) | (1 << MiniGoParser.NOT_EQUAL) | (1 << MiniGoParser.LESS_THAN) | (1 << MiniGoParser.LESS_EQUAL) | (1 << MiniGoParser.GREATER_THAN) | (1 << MiniGoParser.GREATER_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 380
                    self.expr3(0) 
                self.state = 385
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def expr3(self):
            return self.getTypedRuleContext(MiniGoParser.Expr3Context,0)


        def PLUS(self):
            return self.getToken(MiniGoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr3" ):
                return visitor.visitExpr3(self)
            else:
                return visitor.visitChildren(self)



    def expr3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 394
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 389
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 390
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 391
                    self.expr4(0) 
                self.state = 396
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def expr4(self):
            return self.getTypedRuleContext(MiniGoParser.Expr4Context,0)


        def MULTI(self):
            return self.getToken(MiniGoParser.MULTI, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MODULO(self):
            return self.getToken(MiniGoParser.MODULO, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_expr4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr4" ):
                return visitor.visitExpr4(self)
            else:
                return visitor.visitChildren(self)



    def expr4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 405
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 400
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 401
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MULTI) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 402
                    self.expr5() 
                self.state = 407
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr5(self):
            return self.getTypedRuleContext(MiniGoParser.Expr5Context,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr5" ):
                return visitor.visitExpr5(self)
            else:
                return visitor.visitChildren(self)




    def expr5(self):

        localctx = MiniGoParser.Expr5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 411
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.MINUS, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 408
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.MINUS or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 409
                self.expr5()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.OPEN_ROUND, MiniGoParser.OPEN_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 410
                self.expr6(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr7(self):
            return self.getTypedRuleContext(MiniGoParser.Expr7Context,0)


        def expr6(self):
            return self.getTypedRuleContext(MiniGoParser.Expr6Context,0)


        def OPEN_SQUARE(self):
            return self.getToken(MiniGoParser.OPEN_SQUARE, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def CLOSE_SQUARE(self):
            return self.getToken(MiniGoParser.CLOSE_SQUARE, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def funcCall(self):
            return self.getTypedRuleContext(MiniGoParser.FuncCallContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)



    def expr6(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.Expr6Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_expr6, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.expr7()
            self._ctx.stop = self._input.LT(-1)
            self.state = 429
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 427
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 416
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 417
                        self.match(MiniGoParser.OPEN_SQUARE)
                        self.state = 418
                        self.expr(0)
                        self.state = 419
                        self.match(MiniGoParser.CLOSE_SQUARE)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 421
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 422
                        self.match(MiniGoParser.DOT)
                        self.state = 423
                        self.match(MiniGoParser.ID)
                        pass

                    elif la_ == 3:
                        localctx = MiniGoParser.Expr6Context(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr6)
                        self.state = 424
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 425
                        self.match(MiniGoParser.DOT)
                        self.state = 426
                        self.funcCall()
                        pass

             
                self.state = 431
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expr7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_ROUND(self):
            return self.getToken(MiniGoParser.OPEN_ROUND, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def CLOSE_ROUND(self):
            return self.getToken(MiniGoParser.CLOSE_ROUND, 0)

        def operand(self):
            return self.getTypedRuleContext(MiniGoParser.OperandContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr7" ):
                return visitor.visitExpr7(self)
            else:
                return visitor.visitChildren(self)




    def expr7(self):

        localctx = MiniGoParser.Expr7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_expr7)
        try:
            self.state = 437
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.OPEN_ROUND]:
                self.enterOuterAlt(localctx, 1)
                self.state = 432
                self.match(MiniGoParser.OPEN_ROUND)
                self.state = 433
                self.expr(0)
                self.state = 434
                self.match(MiniGoParser.CLOSE_ROUND)
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.OPEN_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 436
                self.operand()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def funcCall(self):
            return self.getTypedRuleContext(MiniGoParser.FuncCallContext,0)


        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def OPEN_CURVE(self):
            return self.getToken(MiniGoParser.OPEN_CURVE, 0)

        def structElList(self):
            return self.getTypedRuleContext(MiniGoParser.StructElListContext,0)


        def CLOSE_CURVE(self):
            return self.getToken(MiniGoParser.CLOSE_CURVE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = MiniGoParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_operand)
        try:
            self.state = 450
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 439
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 440
                self.funcCall()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 441
                self.match(MiniGoParser.ID)
                self.state = 447
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
                if la_ == 1:
                    self.state = 442
                    self.match(MiniGoParser.OPEN_CURVE)
                    self.state = 443
                    self.structElList()
                    self.state = 444
                    self.match(MiniGoParser.CLOSE_CURVE)
                    pass

                elif la_ == 2:
                    pass


                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 449
                self.match(MiniGoParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literalConst(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralConstContext,0)


        def arrLit(self):
            return self.getTypedRuleContext(MiniGoParser.ArrLitContext,0)


        def structLit(self):
            return self.getTypedRuleContext(MiniGoParser.StructLitContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = MiniGoParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_literal)
        try:
            self.state = 455
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 452
                self.literalConst()
                pass
            elif token in [MiniGoParser.OPEN_SQUARE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 453
                self.arrLit()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 454
                self.structLit()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

        def varDeclStatement(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclStatementContext,0)


        def constDeclStatement(self):
            return self.getTypedRuleContext(MiniGoParser.ConstDeclStatementContext,0)


        def assignment(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(MiniGoParser.IfStatementContext,0)


        def forStatement(self):
            return self.getTypedRuleContext(MiniGoParser.ForStatementContext,0)


        def breakStatement(self):
            return self.getTypedRuleContext(MiniGoParser.BreakStatementContext,0)


        def continueStatement(self):
            return self.getTypedRuleContext(MiniGoParser.ContinueStatementContext,0)


        def callStatement(self):
            return self.getTypedRuleContext(MiniGoParser.CallStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(MiniGoParser.ReturnStatementContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = MiniGoParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 466
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 457
                self.varDeclStatement()
                pass

            elif la_ == 2:
                self.state = 458
                self.constDeclStatement()
                pass

            elif la_ == 3:
                self.state = 459
                self.assignment()
                pass

            elif la_ == 4:
                self.state = 460
                self.ifStatement()
                pass

            elif la_ == 5:
                self.state = 461
                self.forStatement()
                pass

            elif la_ == 6:
                self.state = 462
                self.breakStatement()
                pass

            elif la_ == 7:
                self.state = 463
                self.continueStatement()
                pass

            elif la_ == 8:
                self.state = 464
                self.callStatement()
                pass

            elif la_ == 9:
                self.state = 465
                self.returnStatement()
                pass


            self.state = 468
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def statementList(self):
            return self.getTypedRuleContext(MiniGoParser.StatementListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statementList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementList" ):
                return visitor.visitStatementList(self)
            else:
                return visitor.visitChildren(self)




    def statementList(self):

        localctx = MiniGoParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_statementList)
        try:
            self.state = 474
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 470
                self.statement()
                self.state = 471
                self.statementList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 473
                self.statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def typee(self):
            return self.getTypedRuleContext(MiniGoParser.TypeeContext,0)


        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_varDeclStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclStatement" ):
                return visitor.visitVarDeclStatement(self)
            else:
                return visitor.visitChildren(self)




    def varDeclStatement(self):

        localctx = MiniGoParser.VarDeclStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_varDeclStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 476
            self.match(MiniGoParser.VAR)
            self.state = 477
            self.match(MiniGoParser.ID)
            self.state = 485
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.state = 478
                self.typee()
                self.state = 479
                self.match(MiniGoParser.ASSIGN)
                self.state = 480
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 482
                self.match(MiniGoParser.ASSIGN)
                self.state = 483
                self.expr(0)
                pass

            elif la_ == 3:
                self.state = 484
                self.typee()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstDeclStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONST(self):
            return self.getToken(MiniGoParser.CONST, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def literalConst(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralConstContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_constDeclStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstDeclStatement" ):
                return visitor.visitConstDeclStatement(self)
            else:
                return visitor.visitChildren(self)




    def constDeclStatement(self):

        localctx = MiniGoParser.ConstDeclStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_constDeclStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 487
            self.match(MiniGoParser.CONST)
            self.state = 488
            self.match(MiniGoParser.ID)
            self.state = 489
            self.match(MiniGoParser.ASSIGN)
            self.state = 492
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.state = 490
                self.literalConst()
                pass

            elif la_ == 2:
                self.state = 491
                self.expr(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def assignOperator(self):
            return self.getTypedRuleContext(MiniGoParser.AssignOperatorContext,0)


        def rhs(self):
            return self.getTypedRuleContext(MiniGoParser.RhsContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignment

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = MiniGoParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 494
            self.lhs(0)
            self.state = 495
            self.assignOperator()
            self.state = 496
            self.rhs()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def OPEN_SQUARE(self):
            return self.getToken(MiniGoParser.OPEN_SQUARE, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def CLOSE_SQUARE(self):
            return self.getToken(MiniGoParser.CLOSE_SQUARE, 0)

        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)



    def lhs(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.LhsContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 100
        self.enterRecursionRule(localctx, 100, self.RULE_lhs, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 499
            self.match(MiniGoParser.ID)
            self._ctx.stop = self._input.LT(-1)
            self.state = 511
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,38,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 509
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
                    if la_ == 1:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 501
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 502
                        self.match(MiniGoParser.OPEN_SQUARE)
                        self.state = 503
                        self.expr(0)
                        self.state = 504
                        self.match(MiniGoParser.CLOSE_SQUARE)
                        pass

                    elif la_ == 2:
                        localctx = MiniGoParser.LhsContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_lhs)
                        self.state = 506
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 507
                        self.match(MiniGoParser.DOT)
                        self.state = 508
                        self.match(MiniGoParser.ID)
                        pass

             
                self.state = 513
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,38,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AssignOperatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ASSIGN1(self):
            return self.getToken(MiniGoParser.ASSIGN1, 0)

        def PLUS_EQUAL(self):
            return self.getToken(MiniGoParser.PLUS_EQUAL, 0)

        def MINUS_EQUAL(self):
            return self.getToken(MiniGoParser.MINUS_EQUAL, 0)

        def MULTI_EQUAL(self):
            return self.getToken(MiniGoParser.MULTI_EQUAL, 0)

        def DIV_EQUAL(self):
            return self.getToken(MiniGoParser.DIV_EQUAL, 0)

        def MODULO_EQUAL(self):
            return self.getToken(MiniGoParser.MODULO_EQUAL, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_assignOperator

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignOperator" ):
                return visitor.visitAssignOperator(self)
            else:
                return visitor.visitChildren(self)




    def assignOperator(self):

        localctx = MiniGoParser.AssignOperatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_assignOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.ASSIGN1) | (1 << MiniGoParser.PLUS_EQUAL) | (1 << MiniGoParser.MINUS_EQUAL) | (1 << MiniGoParser.MULTI_EQUAL) | (1 << MiniGoParser.DIV_EQUAL) | (1 << MiniGoParser.MODULO_EQUAL))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_rhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRhs" ):
                return visitor.visitRhs(self)
            else:
                return visitor.visitChildren(self)




    def rhs(self):

        localctx = MiniGoParser.RhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_rhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 516
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def OPEN_ROUND(self):
            return self.getToken(MiniGoParser.OPEN_ROUND, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def CLOSE_ROUND(self):
            return self.getToken(MiniGoParser.CLOSE_ROUND, 0)

        def OPEN_CURVE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.OPEN_CURVE)
            else:
                return self.getToken(MiniGoParser.OPEN_CURVE, i)

        def statementList(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(MiniGoParser.StatementListContext)
            else:
                return self.getTypedRuleContext(MiniGoParser.StatementListContext,i)


        def CLOSE_CURVE(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.CLOSE_CURVE)
            else:
                return self.getToken(MiniGoParser.CLOSE_CURVE, i)

        def elifList(self):
            return self.getTypedRuleContext(MiniGoParser.ElifListContext,0)


        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_ifStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = MiniGoParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 518
            self.match(MiniGoParser.IF)
            self.state = 519
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 520
            self.expr(0)
            self.state = 521
            self.match(MiniGoParser.CLOSE_ROUND)
            self.state = 522
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 523
            self.statementList()
            self.state = 524
            self.match(MiniGoParser.CLOSE_CURVE)
            self.state = 525
            self.elifList()
            self.state = 531
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 526
                self.match(MiniGoParser.ELSE)
                self.state = 527
                self.match(MiniGoParser.OPEN_CURVE)
                self.state = 528
                self.statementList()
                self.state = 529
                self.match(MiniGoParser.CLOSE_CURVE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElifListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def eliff(self):
            return self.getTypedRuleContext(MiniGoParser.EliffContext,0)


        def elifList(self):
            return self.getTypedRuleContext(MiniGoParser.ElifListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_elifList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElifList" ):
                return visitor.visitElifList(self)
            else:
                return visitor.visitChildren(self)




    def elifList(self):

        localctx = MiniGoParser.ElifListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_elifList)
        try:
            self.state = 537
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 533
                self.eliff()
                self.state = 534
                self.elifList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EliffContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ELSE(self):
            return self.getToken(MiniGoParser.ELSE, 0)

        def IF(self):
            return self.getToken(MiniGoParser.IF, 0)

        def OPEN_ROUND(self):
            return self.getToken(MiniGoParser.OPEN_ROUND, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def CLOSE_ROUND(self):
            return self.getToken(MiniGoParser.CLOSE_ROUND, 0)

        def OPEN_CURVE(self):
            return self.getToken(MiniGoParser.OPEN_CURVE, 0)

        def statementList(self):
            return self.getTypedRuleContext(MiniGoParser.StatementListContext,0)


        def CLOSE_CURVE(self):
            return self.getToken(MiniGoParser.CLOSE_CURVE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_eliff

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEliff" ):
                return visitor.visitEliff(self)
            else:
                return visitor.visitChildren(self)




    def eliff(self):

        localctx = MiniGoParser.EliffContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_eliff)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 539
            self.match(MiniGoParser.ELSE)
            self.state = 540
            self.match(MiniGoParser.IF)
            self.state = 541
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 542
            self.expr(0)
            self.state = 543
            self.match(MiniGoParser.CLOSE_ROUND)
            self.state = 544
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 545
            self.statementList()
            self.state = 546
            self.match(MiniGoParser.CLOSE_CURVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def forBasic(self):
            return self.getTypedRuleContext(MiniGoParser.ForBasicContext,0)


        def forInitial(self):
            return self.getTypedRuleContext(MiniGoParser.ForInitialContext,0)


        def forRange(self):
            return self.getTypedRuleContext(MiniGoParser.ForRangeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_forStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStatement" ):
                return visitor.visitForStatement(self)
            else:
                return visitor.visitChildren(self)




    def forStatement(self):

        localctx = MiniGoParser.ForStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_forStatement)
        try:
            self.state = 551
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,41,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 548
                self.forBasic()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 549
                self.forInitial()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 550
                self.forRange()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForBasicContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def OPEN_CURVE(self):
            return self.getToken(MiniGoParser.OPEN_CURVE, 0)

        def statementList(self):
            return self.getTypedRuleContext(MiniGoParser.StatementListContext,0)


        def CLOSE_CURVE(self):
            return self.getToken(MiniGoParser.CLOSE_CURVE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_forBasic

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForBasic" ):
                return visitor.visitForBasic(self)
            else:
                return visitor.visitChildren(self)




    def forBasic(self):

        localctx = MiniGoParser.ForBasicContext(self, self._ctx, self.state)
        self.enterRule(localctx, 114, self.RULE_forBasic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 553
            self.match(MiniGoParser.FOR)
            self.state = 554
            self.expr(0)
            self.state = 555
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 556
            self.statementList()
            self.state = 557
            self.match(MiniGoParser.CLOSE_CURVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForInitialContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def initialization(self):
            return self.getTypedRuleContext(MiniGoParser.InitializationContext,0)


        def SEMICOLON(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.SEMICOLON)
            else:
                return self.getToken(MiniGoParser.SEMICOLON, i)

        def condition(self):
            return self.getTypedRuleContext(MiniGoParser.ConditionContext,0)


        def update(self):
            return self.getTypedRuleContext(MiniGoParser.UpdateContext,0)


        def OPEN_CURVE(self):
            return self.getToken(MiniGoParser.OPEN_CURVE, 0)

        def statementList(self):
            return self.getTypedRuleContext(MiniGoParser.StatementListContext,0)


        def CLOSE_CURVE(self):
            return self.getToken(MiniGoParser.CLOSE_CURVE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_forInitial

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForInitial" ):
                return visitor.visitForInitial(self)
            else:
                return visitor.visitChildren(self)




    def forInitial(self):

        localctx = MiniGoParser.ForInitialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 116, self.RULE_forInitial)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 559
            self.match(MiniGoParser.FOR)
            self.state = 560
            self.initialization()
            self.state = 561
            self.match(MiniGoParser.SEMICOLON)
            self.state = 562
            self.condition()
            self.state = 563
            self.match(MiniGoParser.SEMICOLON)
            self.state = 564
            self.update()
            self.state = 565
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 566
            self.statementList()
            self.state = 567
            self.match(MiniGoParser.CLOSE_CURVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class InitializationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignScalar(self):
            return self.getTypedRuleContext(MiniGoParser.AssignScalarContext,0)


        def varDeclInitial(self):
            return self.getTypedRuleContext(MiniGoParser.VarDeclInitialContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_initialization

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInitialization" ):
                return visitor.visitInitialization(self)
            else:
                return visitor.visitChildren(self)




    def initialization(self):

        localctx = MiniGoParser.InitializationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_initialization)
        try:
            self.state = 571
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 569
                self.assignScalar()
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 570
                self.varDeclInitial()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarDeclInitialContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(MiniGoParser.VAR, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(MiniGoParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def typee(self):
            return self.getTypedRuleContext(MiniGoParser.TypeeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_varDeclInitial

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVarDeclInitial" ):
                return visitor.visitVarDeclInitial(self)
            else:
                return visitor.visitChildren(self)




    def varDeclInitial(self):

        localctx = MiniGoParser.VarDeclInitialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_varDeclInitial)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 573
            self.match(MiniGoParser.VAR)
            self.state = 574
            self.match(MiniGoParser.ID)
            self.state = 576
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.OPEN_SQUARE) | (1 << MiniGoParser.ID))) != 0):
                self.state = 575
                self.typee()


            self.state = 578
            self.match(MiniGoParser.ASSIGN)
            self.state = 579
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_condition

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondition" ):
                return visitor.visitCondition(self)
            else:
                return visitor.visitChildren(self)




    def condition(self):

        localctx = MiniGoParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class UpdateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignScalar(self):
            return self.getTypedRuleContext(MiniGoParser.AssignScalarContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_update

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdate" ):
                return visitor.visitUpdate(self)
            else:
                return visitor.visitChildren(self)




    def update(self):

        localctx = MiniGoParser.UpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 583
            self.assignScalar()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignScalarContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def assignOperator(self):
            return self.getTypedRuleContext(MiniGoParser.AssignOperatorContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_assignScalar

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignScalar" ):
                return visitor.visitAssignScalar(self)
            else:
                return visitor.visitChildren(self)




    def assignScalar(self):

        localctx = MiniGoParser.AssignScalarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_assignScalar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
            self.match(MiniGoParser.ID)
            self.state = 586
            self.assignOperator()
            self.state = 587
            self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForRangeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(MiniGoParser.FOR, 0)

        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(MiniGoParser.ID)
            else:
                return self.getToken(MiniGoParser.ID, i)

        def ASSIGN1(self):
            return self.getToken(MiniGoParser.ASSIGN1, 0)

        def RANGE(self):
            return self.getToken(MiniGoParser.RANGE, 0)

        def lhs(self):
            return self.getTypedRuleContext(MiniGoParser.LhsContext,0)


        def OPEN_CURVE(self):
            return self.getToken(MiniGoParser.OPEN_CURVE, 0)

        def statementList(self):
            return self.getTypedRuleContext(MiniGoParser.StatementListContext,0)


        def CLOSE_CURVE(self):
            return self.getToken(MiniGoParser.CLOSE_CURVE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_forRange

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForRange" ):
                return visitor.visitForRange(self)
            else:
                return visitor.visitChildren(self)




    def forRange(self):

        localctx = MiniGoParser.ForRangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_forRange)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 589
            self.match(MiniGoParser.FOR)
            self.state = 590
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.T__0 or _la==MiniGoParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 591
            self.match(MiniGoParser.COMMA)
            self.state = 592
            self.match(MiniGoParser.ID)
            self.state = 593
            self.match(MiniGoParser.ASSIGN1)
            self.state = 594
            self.match(MiniGoParser.RANGE)
            self.state = 595
            self.lhs(0)
            self.state = 596
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 597
            self.statementList()
            self.state = 598
            self.match(MiniGoParser.CLOSE_CURVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(MiniGoParser.BREAK, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_breakStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStatement" ):
                return visitor.visitBreakStatement(self)
            else:
                return visitor.visitChildren(self)




    def breakStatement(self):

        localctx = MiniGoParser.BreakStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 130, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 600
            self.match(MiniGoParser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ContinueStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(MiniGoParser.CONTINUE, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_continueStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinueStatement" ):
                return visitor.visitContinueStatement(self)
            else:
                return visitor.visitChildren(self)




    def continueStatement(self):

        localctx = MiniGoParser.ContinueStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 132, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 602
            self.match(MiniGoParser.CONTINUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CallStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcCall(self):
            return self.getTypedRuleContext(MiniGoParser.FuncCallContext,0)


        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_callStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallStatement" ):
                return visitor.visitCallStatement(self)
            else:
                return visitor.visitChildren(self)




    def callStatement(self):

        localctx = MiniGoParser.CallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 134, self.RULE_callStatement)
        try:
            self.state = 609
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 604
                self.funcCall()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 605
                self.expr(0)
                self.state = 606
                self.match(MiniGoParser.DOT)
                self.state = 607
                self.funcCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(MiniGoParser.RETURN, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_returnStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = MiniGoParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 136, self.RULE_returnStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 611
            self.match(MiniGoParser.RETURN)
            self.state = 613
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.NIL) | (1 << MiniGoParser.TRUE) | (1 << MiniGoParser.FALSE) | (1 << MiniGoParser.MINUS) | (1 << MiniGoParser.NOT) | (1 << MiniGoParser.OPEN_ROUND) | (1 << MiniGoParser.OPEN_SQUARE) | (1 << MiniGoParser.ID) | (1 << MiniGoParser.INT_LIT) | (1 << MiniGoParser.FLOAT_LIT) | (1 << MiniGoParser.STRING_LIT))) != 0):
                self.state = 612
                self.expr(0)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[35] = self.expr_sempred
        self._predicates[36] = self.expr1_sempred
        self._predicates[37] = self.expr2_sempred
        self._predicates[38] = self.expr3_sempred
        self._predicates[39] = self.expr4_sempred
        self._predicates[41] = self.expr6_sempred
        self._predicates[50] = self.lhs_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def expr6_sempred(self, localctx:Expr6Context, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 6:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def lhs_sempred(self, localctx:LhsContext, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         




