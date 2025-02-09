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
        buf.write("\u0380\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\tC\4D\t")
        buf.write("D\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\tL\4M\t")
        buf.write("M\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\tU\4V\t")
        buf.write("V\4W\tW\4X\tX\4Y\tY\4Z\tZ\4[\t[\4\\\t\\\4]\t]\4^\t^\4")
        buf.write("_\t_\4`\t`\4a\ta\4b\tb\3\2\6\2\u00c6\n\2\r\2\16\2\u00c7")
        buf.write("\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u00d2\n\3\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\5\4\u00da\n\4\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\6\3\6\5\6\u00e6\n\6\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\5\t\u00f6\n\t\3\n\3\n")
        buf.write("\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\r\5\r\u010a\n\r\3\16\3\16\3\16\3\16\3")
        buf.write("\16\5\16\u0111\n\16\3\16\3\16\3\17\3\17\5\17\u0117\n\17")
        buf.write("\3\20\3\20\3\20\3\20\3\20\5\20\u011e\n\20\3\21\3\21\3")
        buf.write("\21\3\22\3\22\3\22\3\22\5\22\u0127\n\22\3\23\3\23\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u0132\n\23\3\23\3")
        buf.write("\23\3\24\3\24\3\24\3\24\3\24\5\24\u013b\n\24\3\24\3\24")
        buf.write("\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u0147\n")
        buf.write("\26\3\26\3\26\3\26\3\26\5\26\u014d\n\26\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\5\30\u015b")
        buf.write("\n\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\5\32\u016d\n\32\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\7\33\u0175\n\33\f\33\16\33\u0178")
        buf.write("\13\33\3\34\3\34\3\34\3\34\3\34\3\34\7\34\u0180\n\34\f")
        buf.write("\34\16\34\u0183\13\34\3\35\3\35\3\35\3\35\3\35\3\35\7")
        buf.write("\35\u018b\n\35\f\35\16\35\u018e\13\35\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\36\7\36\u0196\n\36\f\36\16\36\u0199\13\36\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\7\37\u01a1\n\37\f\37\16\37")
        buf.write("\u01a4\13\37\3 \3 \3 \5 \u01a9\n \3!\3!\3!\3!\3!\5!\u01b0")
        buf.write("\n!\3\"\3\"\3\"\5\"\u01b5\n\"\3#\3#\3#\3#\3$\3$\3$\3$")
        buf.write("\3$\3$\7$\u01c1\n$\f$\16$\u01c4\13$\3%\3%\3%\3%\3%\3%")
        buf.write("\7%\u01cc\n%\f%\16%\u01cf\13%\3&\3&\3&\3&\3&\3&\7&\u01d7")
        buf.write("\n&\f&\16&\u01da\13&\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u01e2")
        buf.write("\n\'\f\'\16\'\u01e5\13\'\3(\3(\3(\3(\3(\3(\7(\u01ed\n")
        buf.write("(\f(\16(\u01f0\13(\3)\3)\3)\3)\3)\3)\7)\u01f8\n)\f)\16")
        buf.write(")\u01fb\13)\3*\3*\3*\5*\u0200\n*\3+\3+\3+\3+\3+\5+\u0207")
        buf.write("\n+\3,\3,\5,\u020b\n,\3-\3-\3-\5-\u0210\n-\3-\3-\7-\u0214")
        buf.write("\n-\f-\16-\u0217\13-\3.\3.\5.\u021b\n.\3/\3/\3/\3\60\3")
        buf.write("\60\3\60\3\60\3\61\3\61\3\61\3\61\3\61\5\61\u0229\n\61")
        buf.write("\3\62\3\62\5\62\u022d\n\62\3\63\3\63\3\63\3\63\3\63\3")
        buf.write("\64\3\64\5\64\u0236\n\64\3\65\3\65\3\65\3\65\3\65\5\65")
        buf.write("\u023d\n\65\3\66\3\66\3\66\3\66\3\67\3\67\3\67\3\67\3")
        buf.write("\67\38\38\58\u024a\n8\39\39\39\39\39\39\39\3:\3:\3:\3")
        buf.write(":\3:\3:\7:\u0259\n:\f:\16:\u025c\13:\3;\3;\3;\3;\3;\3")
        buf.write(";\7;\u0264\n;\f;\16;\u0267\13;\3<\3<\3<\3<\3<\3<\7<\u026f")
        buf.write("\n<\f<\16<\u0272\13<\3=\3=\3=\3=\3=\3=\7=\u027a\n=\f=")
        buf.write("\16=\u027d\13=\3>\3>\3>\3>\3>\3>\7>\u0285\n>\f>\16>\u0288")
        buf.write("\13>\3?\3?\3?\5?\u028d\n?\3@\3@\3@\3@\3@\5@\u0294\n@\3")
        buf.write("A\3A\3A\5A\u0299\nA\3B\3B\3B\3B\3B\3B\7B\u02a1\nB\fB\16")
        buf.write("B\u02a4\13B\3C\3C\3C\3C\3C\3C\7C\u02ac\nC\fC\16C\u02af")
        buf.write("\13C\3D\3D\3D\3D\3D\3D\7D\u02b7\nD\fD\16D\u02ba\13D\3")
        buf.write("E\3E\3E\3E\3E\3E\7E\u02c2\nE\fE\16E\u02c5\13E\3F\3F\3")
        buf.write("F\3F\3F\3F\7F\u02cd\nF\fF\16F\u02d0\13F\3G\3G\3G\5G\u02d5")
        buf.write("\nG\3H\3H\3H\3H\3H\5H\u02dc\nH\3I\3I\3I\3I\3I\3I\5I\u02e4")
        buf.write("\nI\3I\3I\3I\3I\3I\5I\u02eb\nI\3J\3J\3J\5J\u02f0\nJ\3")
        buf.write("K\3K\3K\3K\3K\3K\3K\3K\3K\5K\u02fb\nK\3K\3K\3L\3L\3L\3")
        buf.write("L\5L\u0303\nL\3M\3M\3M\3M\3M\3M\3M\3M\3M\5M\u030e\nM\3")
        buf.write("N\3N\3N\3N\3N\5N\u0315\nN\3O\3O\3O\3O\3P\3P\5P\u031d\n")
        buf.write("P\3Q\3Q\3R\3R\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\3S\5")
        buf.write("S\u0330\nS\3T\3T\3T\3T\5T\u0336\nT\3U\3U\3U\3U\3U\3U\3")
        buf.write("U\3U\3U\3V\3V\3V\5V\u0344\nV\3W\3W\3W\3W\3W\3W\3X\3X\3")
        buf.write("X\3X\3X\3X\3X\3X\3X\3X\3Y\3Y\5Y\u0358\nY\3Z\3Z\3Z\5Z\u035d")
        buf.write("\nZ\3Z\3Z\3Z\3[\3[\3\\\3\\\3]\3]\3]\3]\3^\3^\3^\3^\3^")
        buf.write("\3^\3^\3^\3^\3^\3^\3_\3_\3`\3`\3a\3a\5a\u037b\na\3b\3")
        buf.write("b\3b\3b\2\30\64\668:<FHJLNPXrtvxz\u0082\u0084\u0086\u0088")
        buf.write("\u008ac\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*")
        buf.write(",.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz|~\u0080")
        buf.write("\u0082\u0084\u0086\u0088\u008a\u008c\u008e\u0090\u0092")
        buf.write("\u0094\u0096\u0098\u009a\u009c\u009e\u00a0\u00a2\u00a4")
        buf.write("\u00a6\u00a8\u00aa\u00ac\u00ae\u00b0\u00b2\u00b4\u00b6")
        buf.write("\u00b8\u00ba\u00bc\u00be\u00c0\u00c2\2\13\4\2\f\17\67")
        buf.write("\67\3\2\678\4\2\25\278:\3\2\35\"\3\2\30\31\3\2\32\34\4")
        buf.write("\2\31\31%%\3\2\',\4\2\3\3\67\67\2\u037d\2\u00c5\3\2\2")
        buf.write("\2\4\u00d1\3\2\2\2\6\u00d9\3\2\2\2\b\u00db\3\2\2\2\n\u00e5")
        buf.write("\3\2\2\2\f\u00e7\3\2\2\2\16\u00ef\3\2\2\2\20\u00f5\3\2")
        buf.write("\2\2\22\u00f7\3\2\2\2\24\u00fb\3\2\2\2\26\u0103\3\2\2")
        buf.write("\2\30\u0109\3\2\2\2\32\u010b\3\2\2\2\34\u0116\3\2\2\2")
        buf.write("\36\u011d\3\2\2\2 \u011f\3\2\2\2\"\u0126\3\2\2\2$\u0128")
        buf.write("\3\2\2\2&\u0135\3\2\2\2(\u013e\3\2\2\2*\u0140\3\2\2\2")
        buf.write(",\u014e\3\2\2\2.\u0150\3\2\2\2\60\u0160\3\2\2\2\62\u016c")
        buf.write("\3\2\2\2\64\u016e\3\2\2\2\66\u0179\3\2\2\28\u0184\3\2")
        buf.write("\2\2:\u018f\3\2\2\2<\u019a\3\2\2\2>\u01a8\3\2\2\2@\u01af")
        buf.write("\3\2\2\2B\u01b4\3\2\2\2D\u01b6\3\2\2\2F\u01ba\3\2\2\2")
        buf.write("H\u01c5\3\2\2\2J\u01d0\3\2\2\2L\u01db\3\2\2\2N\u01e6\3")
        buf.write("\2\2\2P\u01f1\3\2\2\2R\u01ff\3\2\2\2T\u0206\3\2\2\2V\u020a")
        buf.write("\3\2\2\2X\u020f\3\2\2\2Z\u021a\3\2\2\2\\\u021c\3\2\2\2")
        buf.write("^\u021f\3\2\2\2`\u0228\3\2\2\2b\u022c\3\2\2\2d\u022e\3")
        buf.write("\2\2\2f\u0235\3\2\2\2h\u023c\3\2\2\2j\u023e\3\2\2\2l\u0242")
        buf.write("\3\2\2\2n\u0249\3\2\2\2p\u024b\3\2\2\2r\u0252\3\2\2\2")
        buf.write("t\u025d\3\2\2\2v\u0268\3\2\2\2x\u0273\3\2\2\2z\u027e\3")
        buf.write("\2\2\2|\u028c\3\2\2\2~\u0293\3\2\2\2\u0080\u0298\3\2\2")
        buf.write("\2\u0082\u029a\3\2\2\2\u0084\u02a5\3\2\2\2\u0086\u02b0")
        buf.write("\3\2\2\2\u0088\u02bb\3\2\2\2\u008a\u02c6\3\2\2\2\u008c")
        buf.write("\u02d4\3\2\2\2\u008e\u02db\3\2\2\2\u0090\u02ea\3\2\2\2")
        buf.write("\u0092\u02ef\3\2\2\2\u0094\u02fa\3\2\2\2\u0096\u0302\3")
        buf.write("\2\2\2\u0098\u0304\3\2\2\2\u009a\u030f\3\2\2\2\u009c\u0316")
        buf.write("\3\2\2\2\u009e\u031c\3\2\2\2\u00a0\u031e\3\2\2\2\u00a2")
        buf.write("\u0320\3\2\2\2\u00a4\u0322\3\2\2\2\u00a6\u0335\3\2\2\2")
        buf.write("\u00a8\u0337\3\2\2\2\u00aa\u0343\3\2\2\2\u00ac\u0345\3")
        buf.write("\2\2\2\u00ae\u034b\3\2\2\2\u00b0\u0357\3\2\2\2\u00b2\u0359")
        buf.write("\3\2\2\2\u00b4\u0361\3\2\2\2\u00b6\u0363\3\2\2\2\u00b8")
        buf.write("\u0365\3\2\2\2\u00ba\u0369\3\2\2\2\u00bc\u0374\3\2\2\2")
        buf.write("\u00be\u0376\3\2\2\2\u00c0\u037a\3\2\2\2\u00c2\u037c\3")
        buf.write("\2\2\2\u00c4\u00c6\5\4\3\2\u00c5\u00c4\3\2\2\2\u00c6\u00c7")
        buf.write("\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c7\u00c8\3\2\2\2\u00c8")
        buf.write("\u00c9\3\2\2\2\u00c9\u00ca\7\2\2\3\u00ca\3\3\2\2\2\u00cb")
        buf.write("\u00d2\5\f\7\2\u00cc\u00d2\5\24\13\2\u00cd\u00d2\5$\23")
        buf.write("\2\u00ce\u00d2\5&\24\2\u00cf\u00d2\5*\26\2\u00d0\u00d2")
        buf.write("\5.\30\2\u00d1\u00cb\3\2\2\2\u00d1\u00cc\3\2\2\2\u00d1")
        buf.write("\u00cd\3\2\2\2\u00d1\u00ce\3\2\2\2\u00d1\u00cf\3\2\2\2")
        buf.write("\u00d1\u00d0\3\2\2\2\u00d2\5\3\2\2\2\u00d3\u00da\7\r\2")
        buf.write("\2\u00d4\u00da\7\16\2\2\u00d5\u00da\7\17\2\2\u00d6\u00da")
        buf.write("\7\f\2\2\u00d7\u00da\5\b\5\2\u00d8\u00da\7\67\2\2\u00d9")
        buf.write("\u00d3\3\2\2\2\u00d9\u00d4\3\2\2\2\u00d9\u00d5\3\2\2\2")
        buf.write("\u00d9\u00d6\3\2\2\2\u00d9\u00d7\3\2\2\2\u00d9\u00d8\3")
        buf.write("\2\2\2\u00da\7\3\2\2\2\u00db\u00dc\5\n\6\2\u00dc\u00dd")
        buf.write("\t\2\2\2\u00dd\t\3\2\2\2\u00de\u00df\7\63\2\2\u00df\u00e0")
        buf.write("\t\3\2\2\u00e0\u00e1\7\64\2\2\u00e1\u00e6\5\n\6\2\u00e2")
        buf.write("\u00e3\7\63\2\2\u00e3\u00e4\t\3\2\2\u00e4\u00e6\7\64\2")
        buf.write("\2\u00e5\u00de\3\2\2\2\u00e5\u00e2\3\2\2\2\u00e6\13\3")
        buf.write("\2\2\2\u00e7\u00e8\7\t\2\2\u00e8\u00e9\7\67\2\2\u00e9")
        buf.write("\u00ea\7\n\2\2\u00ea\u00eb\7\61\2\2\u00eb\u00ec\5\16\b")
        buf.write("\2\u00ec\u00ed\7\62\2\2\u00ed\u00ee\7\66\2\2\u00ee\r\3")
        buf.write("\2\2\2\u00ef\u00f0\5\20\t\2\u00f0\17\3\2\2\2\u00f1\u00f2")
        buf.write("\5\22\n\2\u00f2\u00f3\5\20\t\2\u00f3\u00f6\3\2\2\2\u00f4")
        buf.write("\u00f6\5\22\n\2\u00f5\u00f1\3\2\2\2\u00f5\u00f4\3\2\2")
        buf.write("\2\u00f6\21\3\2\2\2\u00f7\u00f8\7\67\2\2\u00f8\u00f9\5")
        buf.write("\6\4\2\u00f9\u00fa\7\66\2\2\u00fa\23\3\2\2\2\u00fb\u00fc")
        buf.write("\7\t\2\2\u00fc\u00fd\7\67\2\2\u00fd\u00fe\7\13\2\2\u00fe")
        buf.write("\u00ff\7\61\2\2\u00ff\u0100\5\26\f\2\u0100\u0101\7\62")
        buf.write("\2\2\u0101\u0102\7\66\2\2\u0102\25\3\2\2\2\u0103\u0104")
        buf.write("\5\30\r\2\u0104\27\3\2\2\2\u0105\u0106\5\32\16\2\u0106")
        buf.write("\u0107\5\30\r\2\u0107\u010a\3\2\2\2\u0108\u010a\5\32\16")
        buf.write("\2\u0109\u0105\3\2\2\2\u0109\u0108\3\2\2\2\u010a\31\3")
        buf.write("\2\2\2\u010b\u010c\7\67\2\2\u010c\u010d\7/\2\2\u010d\u010e")
        buf.write("\5\34\17\2\u010e\u0110\7\60\2\2\u010f\u0111\5\6\4\2\u0110")
        buf.write("\u010f\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u0112\3\2\2\2")
        buf.write("\u0112\u0113\7\66\2\2\u0113\33\3\2\2\2\u0114\u0117\5\36")
        buf.write("\20\2\u0115\u0117\3\2\2\2\u0116\u0114\3\2\2\2\u0116\u0115")
        buf.write("\3\2\2\2\u0117\35\3\2\2\2\u0118\u0119\5 \21\2\u0119\u011a")
        buf.write("\7\65\2\2\u011a\u011b\5\36\20\2\u011b\u011e\3\2\2\2\u011c")
        buf.write("\u011e\5 \21\2\u011d\u0118\3\2\2\2\u011d\u011c\3\2\2\2")
        buf.write("\u011e\37\3\2\2\2\u011f\u0120\5\"\22\2\u0120\u0121\5\6")
        buf.write("\4\2\u0121!\3\2\2\2\u0122\u0123\7\67\2\2\u0123\u0124\7")
        buf.write("\65\2\2\u0124\u0127\5\"\22\2\u0125\u0127\7\67\2\2\u0126")
        buf.write("\u0122\3\2\2\2\u0126\u0125\3\2\2\2\u0127#\3\2\2\2\u0128")
        buf.write("\u0129\7\21\2\2\u0129\u0131\7\67\2\2\u012a\u012b\5\6\4")
        buf.write("\2\u012b\u012c\7&\2\2\u012c\u012d\5\u0082B\2\u012d\u0132")
        buf.write("\3\2\2\2\u012e\u012f\7&\2\2\u012f\u0132\5\u0082B\2\u0130")
        buf.write("\u0132\5\6\4\2\u0131\u012a\3\2\2\2\u0131\u012e\3\2\2\2")
        buf.write("\u0131\u0130\3\2\2\2\u0132\u0133\3\2\2\2\u0133\u0134\7")
        buf.write("\66\2\2\u0134%\3\2\2\2\u0135\u0136\7\20\2\2\u0136\u0137")
        buf.write("\7\67\2\2\u0137\u013a\7&\2\2\u0138\u013b\5(\25\2\u0139")
        buf.write("\u013b\5\u0082B\2\u013a\u0138\3\2\2\2\u013a\u0139\3\2")
        buf.write("\2\2\u013b\u013c\3\2\2\2\u013c\u013d\7\66\2\2\u013d\'")
        buf.write("\3\2\2\2\u013e\u013f\t\4\2\2\u013f)\3\2\2\2\u0140\u0141")
        buf.write("\7\b\2\2\u0141\u0142\7\67\2\2\u0142\u0143\7/\2\2\u0143")
        buf.write("\u0144\5\34\17\2\u0144\u0146\7\60\2\2\u0145\u0147\5\6")
        buf.write("\4\2\u0146\u0145\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u0148")
        buf.write("\3\2\2\2\u0148\u0149\7\61\2\2\u0149\u014a\5,\27\2\u014a")
        buf.write("\u014c\7\62\2\2\u014b\u014d\7\66\2\2\u014c\u014b\3\2\2")
        buf.write("\2\u014c\u014d\3\2\2\2\u014d+\3\2\2\2\u014e\u014f\5\u0096")
        buf.write("L\2\u014f-\3\2\2\2\u0150\u0151\7\b\2\2\u0151\u0152\7/")
        buf.write("\2\2\u0152\u0153\7\67\2\2\u0153\u0154\7\67\2\2\u0154\u0155")
        buf.write("\7\60\2\2\u0155\u0156\7\67\2\2\u0156\u0157\7/\2\2\u0157")
        buf.write("\u0158\5\34\17\2\u0158\u015a\7\60\2\2\u0159\u015b\5\6")
        buf.write("\4\2\u015a\u0159\3\2\2\2\u015a\u015b\3\2\2\2\u015b\u015c")
        buf.write("\3\2\2\2\u015c\u015d\7\61\2\2\u015d\u015e\5,\27\2\u015e")
        buf.write("\u015f\7\62\2\2\u015f/\3\2\2\2\u0160\u0161\5\64\33\2\u0161")
        buf.write("\u0162\5\62\32\2\u0162\61\3\2\2\2\u0163\u0164\7\63\2\2")
        buf.write("\u0164\u0165\5\u0082B\2\u0165\u0166\7\64\2\2\u0166\u0167")
        buf.write("\5\62\32\2\u0167\u016d\3\2\2\2\u0168\u0169\7\63\2\2\u0169")
        buf.write("\u016a\5\u0082B\2\u016a\u016b\7\64\2\2\u016b\u016d\3\2")
        buf.write("\2\2\u016c\u0163\3\2\2\2\u016c\u0168\3\2\2\2\u016d\63")
        buf.write("\3\2\2\2\u016e\u016f\b\33\1\2\u016f\u0170\5\66\34\2\u0170")
        buf.write("\u0176\3\2\2\2\u0171\u0172\f\4\2\2\u0172\u0173\7$\2\2")
        buf.write("\u0173\u0175\5\66\34\2\u0174\u0171\3\2\2\2\u0175\u0178")
        buf.write("\3\2\2\2\u0176\u0174\3\2\2\2\u0176\u0177\3\2\2\2\u0177")
        buf.write("\65\3\2\2\2\u0178\u0176\3\2\2\2\u0179\u017a\b\34\1\2\u017a")
        buf.write("\u017b\58\35\2\u017b\u0181\3\2\2\2\u017c\u017d\f\4\2\2")
        buf.write("\u017d\u017e\7#\2\2\u017e\u0180\58\35\2\u017f\u017c\3")
        buf.write("\2\2\2\u0180\u0183\3\2\2\2\u0181\u017f\3\2\2\2\u0181\u0182")
        buf.write("\3\2\2\2\u0182\67\3\2\2\2\u0183\u0181\3\2\2\2\u0184\u0185")
        buf.write("\b\35\1\2\u0185\u0186\5:\36\2\u0186\u018c\3\2\2\2\u0187")
        buf.write("\u0188\f\4\2\2\u0188\u0189\t\5\2\2\u0189\u018b\5:\36\2")
        buf.write("\u018a\u0187\3\2\2\2\u018b\u018e\3\2\2\2\u018c\u018a\3")
        buf.write("\2\2\2\u018c\u018d\3\2\2\2\u018d9\3\2\2\2\u018e\u018c")
        buf.write("\3\2\2\2\u018f\u0190\b\36\1\2\u0190\u0191\5<\37\2\u0191")
        buf.write("\u0197\3\2\2\2\u0192\u0193\f\4\2\2\u0193\u0194\t\6\2\2")
        buf.write("\u0194\u0196\5<\37\2\u0195\u0192\3\2\2\2\u0196\u0199\3")
        buf.write("\2\2\2\u0197\u0195\3\2\2\2\u0197\u0198\3\2\2\2\u0198;")
        buf.write("\3\2\2\2\u0199\u0197\3\2\2\2\u019a\u019b\b\37\1\2\u019b")
        buf.write("\u019c\5> \2\u019c\u01a2\3\2\2\2\u019d\u019e\f\4\2\2\u019e")
        buf.write("\u019f\t\7\2\2\u019f\u01a1\5> \2\u01a0\u019d\3\2\2\2\u01a1")
        buf.write("\u01a4\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2")
        buf.write("\u01a3=\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a5\u01a6\t\b\2")
        buf.write("\2\u01a6\u01a9\5> \2\u01a7\u01a9\5@!\2\u01a8\u01a5\3\2")
        buf.write("\2\2\u01a8\u01a7\3\2\2\2\u01a9?\3\2\2\2\u01aa\u01ab\7")
        buf.write("/\2\2\u01ab\u01ac\5\64\33\2\u01ac\u01ad\7\60\2\2\u01ad")
        buf.write("\u01b0\3\2\2\2\u01ae\u01b0\5B\"\2\u01af\u01aa\3\2\2\2")
        buf.write("\u01af\u01ae\3\2\2\2\u01b0A\3\2\2\2\u01b1\u01b5\7\67\2")
        buf.write("\2\u01b2\u01b5\5\u0092J\2\u01b3\u01b5\5l\67\2\u01b4\u01b1")
        buf.write("\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b4\u01b3\3\2\2\2\u01b5")
        buf.write("C\3\2\2\2\u01b6\u01b7\5F$\2\u01b7\u01b8\7-\2\2\u01b8\u01b9")
        buf.write("\7\67\2\2\u01b9E\3\2\2\2\u01ba\u01bb\b$\1\2\u01bb\u01bc")
        buf.write("\5H%\2\u01bc\u01c2\3\2\2\2\u01bd\u01be\f\4\2\2\u01be\u01bf")
        buf.write("\7-\2\2\u01bf\u01c1\5H%\2\u01c0\u01bd\3\2\2\2\u01c1\u01c4")
        buf.write("\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3")
        buf.write("G\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c5\u01c6\b%\1\2\u01c6")
        buf.write("\u01c7\5J&\2\u01c7\u01cd\3\2\2\2\u01c8\u01c9\f\4\2\2\u01c9")
        buf.write("\u01ca\7$\2\2\u01ca\u01cc\5J&\2\u01cb\u01c8\3\2\2\2\u01cc")
        buf.write("\u01cf\3\2\2\2\u01cd\u01cb\3\2\2\2\u01cd\u01ce\3\2\2\2")
        buf.write("\u01ceI\3\2\2\2\u01cf\u01cd\3\2\2\2\u01d0\u01d1\b&\1\2")
        buf.write("\u01d1\u01d2\5L\'\2\u01d2\u01d8\3\2\2\2\u01d3\u01d4\f")
        buf.write("\4\2\2\u01d4\u01d5\7#\2\2\u01d5\u01d7\5L\'\2\u01d6\u01d3")
        buf.write("\3\2\2\2\u01d7\u01da\3\2\2\2\u01d8\u01d6\3\2\2\2\u01d8")
        buf.write("\u01d9\3\2\2\2\u01d9K\3\2\2\2\u01da\u01d8\3\2\2\2\u01db")
        buf.write("\u01dc\b\'\1\2\u01dc\u01dd\5N(\2\u01dd\u01e3\3\2\2\2\u01de")
        buf.write("\u01df\f\4\2\2\u01df\u01e0\t\5\2\2\u01e0\u01e2\5N(\2\u01e1")
        buf.write("\u01de\3\2\2\2\u01e2\u01e5\3\2\2\2\u01e3\u01e1\3\2\2\2")
        buf.write("\u01e3\u01e4\3\2\2\2\u01e4M\3\2\2\2\u01e5\u01e3\3\2\2")
        buf.write("\2\u01e6\u01e7\b(\1\2\u01e7\u01e8\5P)\2\u01e8\u01ee\3")
        buf.write("\2\2\2\u01e9\u01ea\f\4\2\2\u01ea\u01eb\t\6\2\2\u01eb\u01ed")
        buf.write("\5P)\2\u01ec\u01e9\3\2\2\2\u01ed\u01f0\3\2\2\2\u01ee\u01ec")
        buf.write("\3\2\2\2\u01ee\u01ef\3\2\2\2\u01efO\3\2\2\2\u01f0\u01ee")
        buf.write("\3\2\2\2\u01f1\u01f2\b)\1\2\u01f2\u01f3\5R*\2\u01f3\u01f9")
        buf.write("\3\2\2\2\u01f4\u01f5\f\4\2\2\u01f5\u01f6\t\7\2\2\u01f6")
        buf.write("\u01f8\5R*\2\u01f7\u01f4\3\2\2\2\u01f8\u01fb\3\2\2\2\u01f9")
        buf.write("\u01f7\3\2\2\2\u01f9\u01fa\3\2\2\2\u01faQ\3\2\2\2\u01fb")
        buf.write("\u01f9\3\2\2\2\u01fc\u01fd\t\b\2\2\u01fd\u0200\5R*\2\u01fe")
        buf.write("\u0200\5T+\2\u01ff\u01fc\3\2\2\2\u01ff\u01fe\3\2\2\2\u0200")
        buf.write("S\3\2\2\2\u0201\u0202\7/\2\2\u0202\u0203\5H%\2\u0203\u0204")
        buf.write("\7\60\2\2\u0204\u0207\3\2\2\2\u0205\u0207\5V,\2\u0206")
        buf.write("\u0201\3\2\2\2\u0206\u0205\3\2\2\2\u0207U\3\2\2\2\u0208")
        buf.write("\u020b\7\67\2\2\u0209\u020b\5\60\31\2\u020a\u0208\3\2")
        buf.write("\2\2\u020a\u0209\3\2\2\2\u020bW\3\2\2\2\u020c\u020d\b")
        buf.write("-\1\2\u020d\u0210\5Z.\2\u020e\u0210\5\60\31\2\u020f\u020c")
        buf.write("\3\2\2\2\u020f\u020e\3\2\2\2\u0210\u0215\3\2\2\2\u0211")
        buf.write("\u0212\f\5\2\2\u0212\u0214\5Z.\2\u0213\u0211\3\2\2\2\u0214")
        buf.write("\u0217\3\2\2\2\u0215\u0213\3\2\2\2\u0215\u0216\3\2\2\2")
        buf.write("\u0216Y\3\2\2\2\u0217\u0215\3\2\2\2\u0218\u021b\5\62\32")
        buf.write("\2\u0219\u021b\5D#\2\u021a\u0218\3\2\2\2\u021a\u0219\3")
        buf.write("\2\2\2\u021b[\3\2\2\2\u021c\u021d\5\b\5\2\u021d\u021e")
        buf.write("\5^\60\2\u021e]\3\2\2\2\u021f\u0220\7\61\2\2\u0220\u0221")
        buf.write("\5`\61\2\u0221\u0222\7\62\2\2\u0222_\3\2\2\2\u0223\u0224")
        buf.write("\5b\62\2\u0224\u0225\7\65\2\2\u0225\u0226\5`\61\2\u0226")
        buf.write("\u0229\3\2\2\2\u0227\u0229\5b\62\2\u0228\u0223\3\2\2\2")
        buf.write("\u0228\u0227\3\2\2\2\u0229a\3\2\2\2\u022a\u022d\5\u0082")
        buf.write("B\2\u022b\u022d\5^\60\2\u022c\u022a\3\2\2\2\u022c\u022b")
        buf.write("\3\2\2\2\u022dc\3\2\2\2\u022e\u022f\7\67\2\2\u022f\u0230")
        buf.write("\7\61\2\2\u0230\u0231\5f\64\2\u0231\u0232\7\62\2\2\u0232")
        buf.write("e\3\2\2\2\u0233\u0236\5h\65\2\u0234\u0236\3\2\2\2\u0235")
        buf.write("\u0233\3\2\2\2\u0235\u0234\3\2\2\2\u0236g\3\2\2\2\u0237")
        buf.write("\u0238\5j\66\2\u0238\u0239\7\65\2\2\u0239\u023a\5h\65")
        buf.write("\2\u023a\u023d\3\2\2\2\u023b\u023d\5j\66\2\u023c\u0237")
        buf.write("\3\2\2\2\u023c\u023b\3\2\2\2\u023di\3\2\2\2\u023e\u023f")
        buf.write("\7\67\2\2\u023f\u0240\7.\2\2\u0240\u0241\5\u0082B\2\u0241")
        buf.write("k\3\2\2\2\u0242\u0243\7\67\2\2\u0243\u0244\7/\2\2\u0244")
        buf.write("\u0245\5n8\2\u0245\u0246\7\60\2\2\u0246m\3\2\2\2\u0247")
        buf.write("\u024a\5`\61\2\u0248\u024a\3\2\2\2\u0249\u0247\3\2\2\2")
        buf.write("\u0249\u0248\3\2\2\2\u024ao\3\2\2\2\u024b\u024c\5r:\2")
        buf.write("\u024c\u024d\7-\2\2\u024d\u024e\7\67\2\2\u024e\u024f\7")
        buf.write("/\2\2\u024f\u0250\5n8\2\u0250\u0251\7\60\2\2\u0251q\3")
        buf.write("\2\2\2\u0252\u0253\b:\1\2\u0253\u0254\5t;\2\u0254\u025a")
        buf.write("\3\2\2\2\u0255\u0256\f\4\2\2\u0256\u0257\7$\2\2\u0257")
        buf.write("\u0259\5t;\2\u0258\u0255\3\2\2\2\u0259\u025c\3\2\2\2\u025a")
        buf.write("\u0258\3\2\2\2\u025a\u025b\3\2\2\2\u025bs\3\2\2\2\u025c")
        buf.write("\u025a\3\2\2\2\u025d\u025e\b;\1\2\u025e\u025f\5v<\2\u025f")
        buf.write("\u0265\3\2\2\2\u0260\u0261\f\4\2\2\u0261\u0262\7#\2\2")
        buf.write("\u0262\u0264\5v<\2\u0263\u0260\3\2\2\2\u0264\u0267\3\2")
        buf.write("\2\2\u0265\u0263\3\2\2\2\u0265\u0266\3\2\2\2\u0266u\3")
        buf.write("\2\2\2\u0267\u0265\3\2\2\2\u0268\u0269\b<\1\2\u0269\u026a")
        buf.write("\5x=\2\u026a\u0270\3\2\2\2\u026b\u026c\f\4\2\2\u026c\u026d")
        buf.write("\t\5\2\2\u026d\u026f\5x=\2\u026e\u026b\3\2\2\2\u026f\u0272")
        buf.write("\3\2\2\2\u0270\u026e\3\2\2\2\u0270\u0271\3\2\2\2\u0271")
        buf.write("w\3\2\2\2\u0272\u0270\3\2\2\2\u0273\u0274\b=\1\2\u0274")
        buf.write("\u0275\5z>\2\u0275\u027b\3\2\2\2\u0276\u0277\f\4\2\2\u0277")
        buf.write("\u0278\t\6\2\2\u0278\u027a\5z>\2\u0279\u0276\3\2\2\2\u027a")
        buf.write("\u027d\3\2\2\2\u027b\u0279\3\2\2\2\u027b\u027c\3\2\2\2")
        buf.write("\u027cy\3\2\2\2\u027d\u027b\3\2\2\2\u027e\u027f\b>\1\2")
        buf.write("\u027f\u0280\5|?\2\u0280\u0286\3\2\2\2\u0281\u0282\f\4")
        buf.write("\2\2\u0282\u0283\t\7\2\2\u0283\u0285\5|?\2\u0284\u0281")
        buf.write("\3\2\2\2\u0285\u0288\3\2\2\2\u0286\u0284\3\2\2\2\u0286")
        buf.write("\u0287\3\2\2\2\u0287{\3\2\2\2\u0288\u0286\3\2\2\2\u0289")
        buf.write("\u028a\t\b\2\2\u028a\u028d\5|?\2\u028b\u028d\5~@\2\u028c")
        buf.write("\u0289\3\2\2\2\u028c\u028b\3\2\2\2\u028d}\3\2\2\2\u028e")
        buf.write("\u028f\7/\2\2\u028f\u0290\5r:\2\u0290\u0291\7\60\2\2\u0291")
        buf.write("\u0294\3\2\2\2\u0292\u0294\5\u0080A\2\u0293\u028e\3\2")
        buf.write("\2\2\u0293\u0292\3\2\2\2\u0294\177\3\2\2\2\u0295\u0299")
        buf.write("\7\67\2\2\u0296\u0299\5\u0092J\2\u0297\u0299\5X-\2\u0298")
        buf.write("\u0295\3\2\2\2\u0298\u0296\3\2\2\2\u0298\u0297\3\2\2\2")
        buf.write("\u0299\u0081\3\2\2\2\u029a\u029b\bB\1\2\u029b\u029c\5")
        buf.write("\u0084C\2\u029c\u02a2\3\2\2\2\u029d\u029e\f\4\2\2\u029e")
        buf.write("\u029f\7$\2\2\u029f\u02a1\5\u0084C\2\u02a0\u029d\3\2\2")
        buf.write("\2\u02a1\u02a4\3\2\2\2\u02a2\u02a0\3\2\2\2\u02a2\u02a3")
        buf.write("\3\2\2\2\u02a3\u0083\3\2\2\2\u02a4\u02a2\3\2\2\2\u02a5")
        buf.write("\u02a6\bC\1\2\u02a6\u02a7\5\u0086D\2\u02a7\u02ad\3\2\2")
        buf.write("\2\u02a8\u02a9\f\4\2\2\u02a9\u02aa\7#\2\2\u02aa\u02ac")
        buf.write("\5\u0086D\2\u02ab\u02a8\3\2\2\2\u02ac\u02af\3\2\2\2\u02ad")
        buf.write("\u02ab\3\2\2\2\u02ad\u02ae\3\2\2\2\u02ae\u0085\3\2\2\2")
        buf.write("\u02af\u02ad\3\2\2\2\u02b0\u02b1\bD\1\2\u02b1\u02b2\5")
        buf.write("\u0088E\2\u02b2\u02b8\3\2\2\2\u02b3\u02b4\f\4\2\2\u02b4")
        buf.write("\u02b5\t\5\2\2\u02b5\u02b7\5\u0088E\2\u02b6\u02b3\3\2")
        buf.write("\2\2\u02b7\u02ba\3\2\2\2\u02b8\u02b6\3\2\2\2\u02b8\u02b9")
        buf.write("\3\2\2\2\u02b9\u0087\3\2\2\2\u02ba\u02b8\3\2\2\2\u02bb")
        buf.write("\u02bc\bE\1\2\u02bc\u02bd\5\u008aF\2\u02bd\u02c3\3\2\2")
        buf.write("\2\u02be\u02bf\f\4\2\2\u02bf\u02c0\t\6\2\2\u02c0\u02c2")
        buf.write("\5\u008aF\2\u02c1\u02be\3\2\2\2\u02c2\u02c5\3\2\2\2\u02c3")
        buf.write("\u02c1\3\2\2\2\u02c3\u02c4\3\2\2\2\u02c4\u0089\3\2\2\2")
        buf.write("\u02c5\u02c3\3\2\2\2\u02c6\u02c7\bF\1\2\u02c7\u02c8\5")
        buf.write("\u008cG\2\u02c8\u02ce\3\2\2\2\u02c9\u02ca\f\4\2\2\u02ca")
        buf.write("\u02cb\t\7\2\2\u02cb\u02cd\5\u008cG\2\u02cc\u02c9\3\2")
        buf.write("\2\2\u02cd\u02d0\3\2\2\2\u02ce\u02cc\3\2\2\2\u02ce\u02cf")
        buf.write("\3\2\2\2\u02cf\u008b\3\2\2\2\u02d0\u02ce\3\2\2\2\u02d1")
        buf.write("\u02d2\t\b\2\2\u02d2\u02d5\5\u008cG\2\u02d3\u02d5\5\u008e")
        buf.write("H\2\u02d4\u02d1\3\2\2\2\u02d4\u02d3\3\2\2\2\u02d5\u008d")
        buf.write("\3\2\2\2\u02d6\u02d7\7/\2\2\u02d7\u02d8\5\u0082B\2\u02d8")
        buf.write("\u02d9\7\60\2\2\u02d9\u02dc\3\2\2\2\u02da\u02dc\5\u0090")
        buf.write("I\2\u02db\u02d6\3\2\2\2\u02db\u02da\3\2\2\2\u02dc\u008f")
        buf.write("\3\2\2\2\u02dd\u02e3\7\67\2\2\u02de\u02df\7\61\2\2\u02df")
        buf.write("\u02e0\5f\64\2\u02e0\u02e1\7\62\2\2\u02e1\u02e4\3\2\2")
        buf.write("\2\u02e2\u02e4\3\2\2\2\u02e3\u02de\3\2\2\2\u02e3\u02e2")
        buf.write("\3\2\2\2\u02e4\u02eb\3\2\2\2\u02e5\u02eb\5\u0092J\2\u02e6")
        buf.write("\u02eb\7\67\2\2\u02e7\u02eb\5l\67\2\u02e8\u02eb\5p9\2")
        buf.write("\u02e9\u02eb\5X-\2\u02ea\u02dd\3\2\2\2\u02ea\u02e5\3\2")
        buf.write("\2\2\u02ea\u02e6\3\2\2\2\u02ea\u02e7\3\2\2\2\u02ea\u02e8")
        buf.write("\3\2\2\2\u02ea\u02e9\3\2\2\2\u02eb\u0091\3\2\2\2\u02ec")
        buf.write("\u02f0\5(\25\2\u02ed\u02f0\5\\/\2\u02ee\u02f0\5d\63\2")
        buf.write("\u02ef\u02ec\3\2\2\2\u02ef\u02ed\3\2\2\2\u02ef\u02ee\3")
        buf.write("\2\2\2\u02f0\u0093\3\2\2\2\u02f1\u02fb\5\u0098M\2\u02f2")
        buf.write("\u02fb\5\u009aN\2\u02f3\u02fb\5\u009cO\2\u02f4\u02fb\5")
        buf.write("\u00a4S\2\u02f5\u02fb\5\u00aaV\2\u02f6\u02fb\5\u00bc_")
        buf.write("\2\u02f7\u02fb\5\u00be`\2\u02f8\u02fb\5\u00c0a\2\u02f9")
        buf.write("\u02fb\5\u00c2b\2\u02fa\u02f1\3\2\2\2\u02fa\u02f2\3\2")
        buf.write("\2\2\u02fa\u02f3\3\2\2\2\u02fa\u02f4\3\2\2\2\u02fa\u02f5")
        buf.write("\3\2\2\2\u02fa\u02f6\3\2\2\2\u02fa\u02f7\3\2\2\2\u02fa")
        buf.write("\u02f8\3\2\2\2\u02fa\u02f9\3\2\2\2\u02fb\u02fc\3\2\2\2")
        buf.write("\u02fc\u02fd\7\66\2\2\u02fd\u0095\3\2\2\2\u02fe\u02ff")
        buf.write("\5\u0094K\2\u02ff\u0300\5\u0096L\2\u0300\u0303\3\2\2\2")
        buf.write("\u0301\u0303\5\u0094K\2\u0302\u02fe\3\2\2\2\u0302\u0301")
        buf.write("\3\2\2\2\u0303\u0097\3\2\2\2\u0304\u0305\7\21\2\2\u0305")
        buf.write("\u030d\7\67\2\2\u0306\u0307\5\6\4\2\u0307\u0308\7&\2\2")
        buf.write("\u0308\u0309\5\u0082B\2\u0309\u030e\3\2\2\2\u030a\u030b")
        buf.write("\7&\2\2\u030b\u030e\5\u0082B\2\u030c\u030e\5\6\4\2\u030d")
        buf.write("\u0306\3\2\2\2\u030d\u030a\3\2\2\2\u030d\u030c\3\2\2\2")
        buf.write("\u030e\u0099\3\2\2\2\u030f\u0310\7\20\2\2\u0310\u0311")
        buf.write("\7\67\2\2\u0311\u0314\7&\2\2\u0312\u0315\5(\25\2\u0313")
        buf.write("\u0315\5\u0082B\2\u0314\u0312\3\2\2\2\u0314\u0313\3\2")
        buf.write("\2\2\u0315\u009b\3\2\2\2\u0316\u0317\5\u009eP\2\u0317")
        buf.write("\u0318\5\u00a0Q\2\u0318\u0319\5\u00a2R\2\u0319\u009d\3")
        buf.write("\2\2\2\u031a\u031d\7\67\2\2\u031b\u031d\5X-\2\u031c\u031a")
        buf.write("\3\2\2\2\u031c\u031b\3\2\2\2\u031d\u009f\3\2\2\2\u031e")
        buf.write("\u031f\t\t\2\2\u031f\u00a1\3\2\2\2\u0320\u0321\5\u0082")
        buf.write("B\2\u0321\u00a3\3\2\2\2\u0322\u0323\7\4\2\2\u0323\u0324")
        buf.write("\7/\2\2\u0324\u0325\5\u0082B\2\u0325\u0326\7\60\2\2\u0326")
        buf.write("\u0327\7\61\2\2\u0327\u0328\5\u0096L\2\u0328\u0329\7\62")
        buf.write("\2\2\u0329\u032f\5\u00a6T\2\u032a\u032b\7\5\2\2\u032b")
        buf.write("\u032c\7\61\2\2\u032c\u032d\5\u0096L\2\u032d\u032e\7\62")
        buf.write("\2\2\u032e\u0330\3\2\2\2\u032f\u032a\3\2\2\2\u032f\u0330")
        buf.write("\3\2\2\2\u0330\u00a5\3\2\2\2\u0331\u0332\5\u00a8U\2\u0332")
        buf.write("\u0333\5\u00a6T\2\u0333\u0336\3\2\2\2\u0334\u0336\3\2")
        buf.write("\2\2\u0335\u0331\3\2\2\2\u0335\u0334\3\2\2\2\u0336\u00a7")
        buf.write("\3\2\2\2\u0337\u0338\7\5\2\2\u0338\u0339\7\4\2\2\u0339")
        buf.write("\u033a\7/\2\2\u033a\u033b\5\u0082B\2\u033b\u033c\7\60")
        buf.write("\2\2\u033c\u033d\7\61\2\2\u033d\u033e\5\u0096L\2\u033e")
        buf.write("\u033f\7\62\2\2\u033f\u00a9\3\2\2\2\u0340\u0344\5\u00ac")
        buf.write("W\2\u0341\u0344\5\u00aeX\2\u0342\u0344\5\u00ba^\2\u0343")
        buf.write("\u0340\3\2\2\2\u0343\u0341\3\2\2\2\u0343\u0342\3\2\2\2")
        buf.write("\u0344\u00ab\3\2\2\2\u0345\u0346\7\6\2\2\u0346\u0347\5")
        buf.write("\u0082B\2\u0347\u0348\7\61\2\2\u0348\u0349\5\u0096L\2")
        buf.write("\u0349\u034a\7\62\2\2\u034a\u00ad\3\2\2\2\u034b\u034c")
        buf.write("\7\6\2\2\u034c\u034d\5\u00b0Y\2\u034d\u034e\7\66\2\2\u034e")
        buf.write("\u034f\5\u00b4[\2\u034f\u0350\7\66\2\2\u0350\u0351\5\u00b6")
        buf.write("\\\2\u0351\u0352\7\61\2\2\u0352\u0353\5\u0096L\2\u0353")
        buf.write("\u0354\7\62\2\2\u0354\u00af\3\2\2\2\u0355\u0358\5\u00b8")
        buf.write("]\2\u0356\u0358\5\u00b2Z\2\u0357\u0355\3\2\2\2\u0357\u0356")
        buf.write("\3\2\2\2\u0358\u00b1\3\2\2\2\u0359\u035a\7\21\2\2\u035a")
        buf.write("\u035c\7\67\2\2\u035b\u035d\5\6\4\2\u035c\u035b\3\2\2")
        buf.write("\2\u035c\u035d\3\2\2\2\u035d\u035e\3\2\2\2\u035e\u035f")
        buf.write("\7&\2\2\u035f\u0360\5\u0082B\2\u0360\u00b3\3\2\2\2\u0361")
        buf.write("\u0362\5\u0082B\2\u0362\u00b5\3\2\2\2\u0363\u0364\5\u00b8")
        buf.write("]\2\u0364\u00b7\3\2\2\2\u0365\u0366\7\67\2\2\u0366\u0367")
        buf.write("\5\u00a0Q\2\u0367\u0368\5\u0082B\2\u0368\u00b9\3\2\2\2")
        buf.write("\u0369\u036a\7\6\2\2\u036a\u036b\t\n\2\2\u036b\u036c\7")
        buf.write("\65\2\2\u036c\u036d\7\67\2\2\u036d\u036e\7\'\2\2\u036e")
        buf.write("\u036f\7\24\2\2\u036f\u0370\7\67\2\2\u0370\u0371\7\61")
        buf.write("\2\2\u0371\u0372\5\u0096L\2\u0372\u0373\7\62\2\2\u0373")
        buf.write("\u00bb\3\2\2\2\u0374\u0375\7\23\2\2\u0375\u00bd\3\2\2")
        buf.write("\2\u0376\u0377\7\22\2\2\u0377\u00bf\3\2\2\2\u0378\u037b")
        buf.write("\5l\67\2\u0379\u037b\5p9\2\u037a\u0378\3\2\2\2\u037a\u0379")
        buf.write("\3\2\2\2\u037b\u00c1\3\2\2\2\u037c\u037d\7\7\2\2\u037d")
        buf.write("\u037e\5\u0082B\2\u037e\u00c3\3\2\2\2H\u00c7\u00d1\u00d9")
        buf.write("\u00e5\u00f5\u0109\u0110\u0116\u011d\u0126\u0131\u013a")
        buf.write("\u0146\u014c\u015a\u016c\u0176\u0181\u018c\u0197\u01a2")
        buf.write("\u01a8\u01af\u01b4\u01c2\u01cd\u01d8\u01e3\u01ee\u01f9")
        buf.write("\u01ff\u0206\u020a\u020f\u0215\u021a\u0228\u022c\u0235")
        buf.write("\u023c\u0249\u025a\u0265\u0270\u027b\u0286\u028c\u0293")
        buf.write("\u0298\u02a2\u02ad\u02b8\u02c3\u02ce\u02d4\u02db\u02e3")
        buf.write("\u02ea\u02ef\u02fa\u0302\u030d\u0314\u031c\u032f\u0335")
        buf.write("\u0343\u0357\u035c\u037a")
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
    RULE_arrAccess = 23
    RULE_positionList = 24
    RULE_exprA = 25
    RULE_exprA1 = 26
    RULE_exprA2 = 27
    RULE_exprA3 = 28
    RULE_exprA4 = 29
    RULE_exprA5 = 30
    RULE_exprA6 = 31
    RULE_operandA = 32
    RULE_structAccess = 33
    RULE_refList = 34
    RULE_exprS = 35
    RULE_exprS1 = 36
    RULE_exprS2 = 37
    RULE_exprS3 = 38
    RULE_exprS4 = 39
    RULE_exprS5 = 40
    RULE_exprS6 = 41
    RULE_operandS = 42
    RULE_arrStructAccess = 43
    RULE_accessList = 44
    RULE_arrLit = 45
    RULE_arrBody = 46
    RULE_elementList = 47
    RULE_element = 48
    RULE_structLit = 49
    RULE_structElList = 50
    RULE_structELPrime = 51
    RULE_structEL = 52
    RULE_funcCall = 53
    RULE_argumentList = 54
    RULE_methodCall = 55
    RULE_exprM = 56
    RULE_exprM1 = 57
    RULE_exprM2 = 58
    RULE_exprM3 = 59
    RULE_exprM4 = 60
    RULE_exprM5 = 61
    RULE_exprM6 = 62
    RULE_operandM = 63
    RULE_expr = 64
    RULE_expr1 = 65
    RULE_expr2 = 66
    RULE_expr3 = 67
    RULE_expr4 = 68
    RULE_expr5 = 69
    RULE_expr6 = 70
    RULE_operand = 71
    RULE_literal = 72
    RULE_statement = 73
    RULE_statementList = 74
    RULE_varDeclStatement = 75
    RULE_constDeclStatement = 76
    RULE_assignment = 77
    RULE_lhs = 78
    RULE_assignOperator = 79
    RULE_rhs = 80
    RULE_ifStatement = 81
    RULE_elifList = 82
    RULE_eliff = 83
    RULE_forStatement = 84
    RULE_forBasic = 85
    RULE_forInitial = 86
    RULE_initialization = 87
    RULE_varDeclInitial = 88
    RULE_condition = 89
    RULE_update = 90
    RULE_assignScalar = 91
    RULE_forRange = 92
    RULE_breakStatement = 93
    RULE_continueStatement = 94
    RULE_callStatement = 95
    RULE_returnStatement = 96

    ruleNames =  [ "program", "decl", "typee", "arrType", "dimenList", "structDecl", 
                   "structBody", "listField", "field", "interfaceDecl", 
                   "interfaceBody", "listMethod", "method", "paramList", 
                   "paramPrime", "param", "nameList", "varDecl", "constDecl", 
                   "literalConst", "funcDecl", "funcBody", "methodStructDecl", 
                   "arrAccess", "positionList", "exprA", "exprA1", "exprA2", 
                   "exprA3", "exprA4", "exprA5", "exprA6", "operandA", "structAccess", 
                   "refList", "exprS", "exprS1", "exprS2", "exprS3", "exprS4", 
                   "exprS5", "exprS6", "operandS", "arrStructAccess", "accessList", 
                   "arrLit", "arrBody", "elementList", "element", "structLit", 
                   "structElList", "structELPrime", "structEL", "funcCall", 
                   "argumentList", "methodCall", "exprM", "exprM1", "exprM2", 
                   "exprM3", "exprM4", "exprM5", "exprM6", "operandM", "expr", 
                   "expr1", "expr2", "expr3", "expr4", "expr5", "expr6", 
                   "operand", "literal", "statement", "statementList", "varDeclStatement", 
                   "constDeclStatement", "assignment", "lhs", "assignOperator", 
                   "rhs", "ifStatement", "elifList", "eliff", "forStatement", 
                   "forBasic", "forInitial", "initialization", "varDeclInitial", 
                   "condition", "update", "assignScalar", "forRange", "breakStatement", 
                   "continueStatement", "callStatement", "returnStatement" ]

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
            self.state = 195 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 194
                self.decl()
                self.state = 197 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR))) != 0)):
                    break

            self.state = 199
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
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 201
                self.structDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 202
                self.interfaceDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 203
                self.varDecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 204
                self.constDecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 205
                self.funcDecl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 206
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
            self.state = 215
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT]:
                self.state = 209
                self.match(MiniGoParser.INT)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.state = 210
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.state = 211
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.STRING]:
                self.state = 212
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.OPEN_SQUARE]:
                self.state = 213
                self.arrType()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 214
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
            self.state = 217
            self.dimenList()
            self.state = 218
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
            self.state = 227
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.match(MiniGoParser.OPEN_SQUARE)
                self.state = 221
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.ID or _la==MiniGoParser.INT_LIT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 222
                self.match(MiniGoParser.CLOSE_SQUARE)
                self.state = 223
                self.dimenList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.match(MiniGoParser.OPEN_SQUARE)
                self.state = 225
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.ID or _la==MiniGoParser.INT_LIT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 226
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
            self.state = 229
            self.match(MiniGoParser.TYPE)
            self.state = 230
            self.match(MiniGoParser.ID)
            self.state = 231
            self.match(MiniGoParser.STRUCT)
            self.state = 232
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 233
            self.structBody()
            self.state = 234
            self.match(MiniGoParser.CLOSE_CURVE)
            self.state = 235
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
            self.state = 237
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
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 239
                self.field()
                self.state = 240
                self.listField()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 242
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
            self.state = 245
            self.match(MiniGoParser.ID)
            self.state = 246
            self.typee()
            self.state = 247
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
            self.state = 249
            self.match(MiniGoParser.TYPE)
            self.state = 250
            self.match(MiniGoParser.ID)
            self.state = 251
            self.match(MiniGoParser.INTERFACE)
            self.state = 252
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 253
            self.interfaceBody()
            self.state = 254
            self.match(MiniGoParser.CLOSE_CURVE)
            self.state = 255
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
            self.state = 257
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
            self.state = 263
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 259
                self.method()
                self.state = 260
                self.listMethod()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 262
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
            self.state = 265
            self.match(MiniGoParser.ID)
            self.state = 266
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 267
            self.paramList()
            self.state = 268
            self.match(MiniGoParser.CLOSE_ROUND)
            self.state = 270
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.OPEN_SQUARE) | (1 << MiniGoParser.ID))) != 0):
                self.state = 269
                self.typee()


            self.state = 272
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
            self.state = 276
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 274
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
            self.state = 283
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 278
                self.param()
                self.state = 279
                self.match(MiniGoParser.COMMA)
                self.state = 280
                self.paramPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 282
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
            self.state = 285
            self.nameList()
            self.state = 286
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
            self.state = 292
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 288
                self.match(MiniGoParser.ID)
                self.state = 289
                self.match(MiniGoParser.COMMA)
                self.state = 290
                self.nameList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
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
            self.state = 294
            self.match(MiniGoParser.VAR)
            self.state = 295
            self.match(MiniGoParser.ID)
            self.state = 303
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 296
                self.typee()
                self.state = 297
                self.match(MiniGoParser.ASSIGN)
                self.state = 298
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 300
                self.match(MiniGoParser.ASSIGN)
                self.state = 301
                self.expr(0)
                pass

            elif la_ == 3:
                self.state = 302
                self.typee()
                pass


            self.state = 305
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
            self.state = 307
            self.match(MiniGoParser.CONST)
            self.state = 308
            self.match(MiniGoParser.ID)
            self.state = 309
            self.match(MiniGoParser.ASSIGN)
            self.state = 312
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 310
                self.literalConst()
                pass

            elif la_ == 2:
                self.state = 311
                self.expr(0)
                pass


            self.state = 314
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
            self.state = 316
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

        def typee(self):
            return self.getTypedRuleContext(MiniGoParser.TypeeContext,0)


        def SEMICOLON(self):
            return self.getToken(MiniGoParser.SEMICOLON, 0)

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
            self.state = 318
            self.match(MiniGoParser.FUNC)
            self.state = 319
            self.match(MiniGoParser.ID)
            self.state = 320
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 321
            self.paramList()
            self.state = 322
            self.match(MiniGoParser.CLOSE_ROUND)
            self.state = 324
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.OPEN_SQUARE) | (1 << MiniGoParser.ID))) != 0):
                self.state = 323
                self.typee()


            self.state = 326
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 327
            self.funcBody()
            self.state = 328
            self.match(MiniGoParser.CLOSE_CURVE)
            self.state = 330
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.SEMICOLON:
                self.state = 329
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
            self.state = 332
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
            self.state = 334
            self.match(MiniGoParser.FUNC)
            self.state = 335
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 336
            self.match(MiniGoParser.ID)
            self.state = 337
            self.match(MiniGoParser.ID)
            self.state = 338
            self.match(MiniGoParser.CLOSE_ROUND)
            self.state = 339
            self.match(MiniGoParser.ID)
            self.state = 340
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 341
            self.paramList()
            self.state = 342
            self.match(MiniGoParser.CLOSE_ROUND)
            self.state = 344
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.OPEN_SQUARE) | (1 << MiniGoParser.ID))) != 0):
                self.state = 343
                self.typee()


            self.state = 346
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 347
            self.funcBody()
            self.state = 348
            self.match(MiniGoParser.CLOSE_CURVE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprA(self):
            return self.getTypedRuleContext(MiniGoParser.ExprAContext,0)


        def positionList(self):
            return self.getTypedRuleContext(MiniGoParser.PositionListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrAccess

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrAccess" ):
                return visitor.visitArrAccess(self)
            else:
                return visitor.visitChildren(self)




    def arrAccess(self):

        localctx = MiniGoParser.ArrAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_arrAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.exprA(0)
            self.state = 351
            self.positionList()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PositionListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_SQUARE(self):
            return self.getToken(MiniGoParser.OPEN_SQUARE, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def CLOSE_SQUARE(self):
            return self.getToken(MiniGoParser.CLOSE_SQUARE, 0)

        def positionList(self):
            return self.getTypedRuleContext(MiniGoParser.PositionListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_positionList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPositionList" ):
                return visitor.visitPositionList(self)
            else:
                return visitor.visitChildren(self)




    def positionList(self):

        localctx = MiniGoParser.PositionListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_positionList)
        try:
            self.state = 362
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.match(MiniGoParser.OPEN_SQUARE)
                self.state = 354
                self.expr(0)
                self.state = 355
                self.match(MiniGoParser.CLOSE_SQUARE)
                self.state = 356
                self.positionList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 358
                self.match(MiniGoParser.OPEN_SQUARE)
                self.state = 359
                self.expr(0)
                self.state = 360
                self.match(MiniGoParser.CLOSE_SQUARE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprAContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprA1(self):
            return self.getTypedRuleContext(MiniGoParser.ExprA1Context,0)


        def exprA(self):
            return self.getTypedRuleContext(MiniGoParser.ExprAContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_exprA

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprA" ):
                return visitor.visitExprA(self)
            else:
                return visitor.visitChildren(self)



    def exprA(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprAContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 50
        self.enterRecursionRule(localctx, 50, self.RULE_exprA, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 365
            self.exprA1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 372
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprAContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprA)
                    self.state = 367
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 368
                    self.match(MiniGoParser.OR)
                    self.state = 369
                    self.exprA1(0) 
                self.state = 374
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprA1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprA2(self):
            return self.getTypedRuleContext(MiniGoParser.ExprA2Context,0)


        def exprA1(self):
            return self.getTypedRuleContext(MiniGoParser.ExprA1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_exprA1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprA1" ):
                return visitor.visitExprA1(self)
            else:
                return visitor.visitChildren(self)



    def exprA1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprA1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 52
        self.enterRecursionRule(localctx, 52, self.RULE_exprA1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 376
            self.exprA2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 383
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprA1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprA1)
                    self.state = 378
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 379
                    self.match(MiniGoParser.AND)
                    self.state = 380
                    self.exprA2(0) 
                self.state = 385
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprA2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprA3(self):
            return self.getTypedRuleContext(MiniGoParser.ExprA3Context,0)


        def exprA2(self):
            return self.getTypedRuleContext(MiniGoParser.ExprA2Context,0)


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
            return MiniGoParser.RULE_exprA2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprA2" ):
                return visitor.visitExprA2(self)
            else:
                return visitor.visitChildren(self)



    def exprA2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprA2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_exprA2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 387
            self.exprA3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 394
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprA2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprA2)
                    self.state = 389
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 390
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUAL) | (1 << MiniGoParser.NOT_EQUAL) | (1 << MiniGoParser.LESS_THAN) | (1 << MiniGoParser.LESS_EQUAL) | (1 << MiniGoParser.GREATER_THAN) | (1 << MiniGoParser.GREATER_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 391
                    self.exprA3(0) 
                self.state = 396
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprA3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprA4(self):
            return self.getTypedRuleContext(MiniGoParser.ExprA4Context,0)


        def exprA3(self):
            return self.getTypedRuleContext(MiniGoParser.ExprA3Context,0)


        def PLUS(self):
            return self.getToken(MiniGoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_exprA3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprA3" ):
                return visitor.visitExprA3(self)
            else:
                return visitor.visitChildren(self)



    def exprA3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprA3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_exprA3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            self.exprA4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 405
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprA3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprA3)
                    self.state = 400
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 401
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 402
                    self.exprA4(0) 
                self.state = 407
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprA4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprA5(self):
            return self.getTypedRuleContext(MiniGoParser.ExprA5Context,0)


        def exprA4(self):
            return self.getTypedRuleContext(MiniGoParser.ExprA4Context,0)


        def MULTI(self):
            return self.getToken(MiniGoParser.MULTI, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MODULO(self):
            return self.getToken(MiniGoParser.MODULO, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_exprA4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprA4" ):
                return visitor.visitExprA4(self)
            else:
                return visitor.visitChildren(self)



    def exprA4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprA4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_exprA4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 409
            self.exprA5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 416
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprA4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprA4)
                    self.state = 411
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 412
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MULTI) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 413
                    self.exprA5() 
                self.state = 418
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprA5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprA5(self):
            return self.getTypedRuleContext(MiniGoParser.ExprA5Context,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def exprA6(self):
            return self.getTypedRuleContext(MiniGoParser.ExprA6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exprA5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprA5" ):
                return visitor.visitExprA5(self)
            else:
                return visitor.visitChildren(self)




    def exprA5(self):

        localctx = MiniGoParser.ExprA5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_exprA5)
        self._la = 0 # Token type
        try:
            self.state = 422
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.MINUS, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 419
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.MINUS or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 420
                self.exprA5()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.OPEN_ROUND, MiniGoParser.OPEN_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 421
                self.exprA6()
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


    class ExprA6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_ROUND(self):
            return self.getToken(MiniGoParser.OPEN_ROUND, 0)

        def exprA(self):
            return self.getTypedRuleContext(MiniGoParser.ExprAContext,0)


        def CLOSE_ROUND(self):
            return self.getToken(MiniGoParser.CLOSE_ROUND, 0)

        def operandA(self):
            return self.getTypedRuleContext(MiniGoParser.OperandAContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exprA6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprA6" ):
                return visitor.visitExprA6(self)
            else:
                return visitor.visitChildren(self)




    def exprA6(self):

        localctx = MiniGoParser.ExprA6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_exprA6)
        try:
            self.state = 429
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.OPEN_ROUND]:
                self.enterOuterAlt(localctx, 1)
                self.state = 424
                self.match(MiniGoParser.OPEN_ROUND)
                self.state = 425
                self.exprA(0)
                self.state = 426
                self.match(MiniGoParser.CLOSE_ROUND)
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.OPEN_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                self.operandA()
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


    class OperandAContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def funcCall(self):
            return self.getTypedRuleContext(MiniGoParser.FuncCallContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_operandA

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperandA" ):
                return visitor.visitOperandA(self)
            else:
                return visitor.visitChildren(self)




    def operandA(self):

        localctx = MiniGoParser.OperandAContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_operandA)
        try:
            self.state = 434
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 431
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 432
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 433
                self.funcCall()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def refList(self):
            return self.getTypedRuleContext(MiniGoParser.RefListContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_structAccess

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructAccess" ):
                return visitor.visitStructAccess(self)
            else:
                return visitor.visitChildren(self)




    def structAccess(self):

        localctx = MiniGoParser.StructAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_structAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 436
            self.refList(0)
            self.state = 437
            self.match(MiniGoParser.DOT)
            self.state = 438
            self.match(MiniGoParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RefListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprS(self):
            return self.getTypedRuleContext(MiniGoParser.ExprSContext,0)


        def refList(self):
            return self.getTypedRuleContext(MiniGoParser.RefListContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_refList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRefList" ):
                return visitor.visitRefList(self)
            else:
                return visitor.visitChildren(self)



    def refList(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.RefListContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 68
        self.enterRecursionRule(localctx, 68, self.RULE_refList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 441
            self.exprS(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 448
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,24,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.RefListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_refList)
                    self.state = 443
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 444
                    self.match(MiniGoParser.DOT)
                    self.state = 445
                    self.exprS(0) 
                self.state = 450
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,24,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprSContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprS1(self):
            return self.getTypedRuleContext(MiniGoParser.ExprS1Context,0)


        def exprS(self):
            return self.getTypedRuleContext(MiniGoParser.ExprSContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_exprS

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprS" ):
                return visitor.visitExprS(self)
            else:
                return visitor.visitChildren(self)



    def exprS(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprSContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 70
        self.enterRecursionRule(localctx, 70, self.RULE_exprS, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self.exprS1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 459
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprSContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprS)
                    self.state = 454
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 455
                    self.match(MiniGoParser.OR)
                    self.state = 456
                    self.exprS1(0) 
                self.state = 461
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprS1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprS2(self):
            return self.getTypedRuleContext(MiniGoParser.ExprS2Context,0)


        def exprS1(self):
            return self.getTypedRuleContext(MiniGoParser.ExprS1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_exprS1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprS1" ):
                return visitor.visitExprS1(self)
            else:
                return visitor.visitChildren(self)



    def exprS1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprS1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 72
        self.enterRecursionRule(localctx, 72, self.RULE_exprS1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 463
            self.exprS2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 470
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprS1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprS1)
                    self.state = 465
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 466
                    self.match(MiniGoParser.AND)
                    self.state = 467
                    self.exprS2(0) 
                self.state = 472
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprS2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprS3(self):
            return self.getTypedRuleContext(MiniGoParser.ExprS3Context,0)


        def exprS2(self):
            return self.getTypedRuleContext(MiniGoParser.ExprS2Context,0)


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
            return MiniGoParser.RULE_exprS2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprS2" ):
                return visitor.visitExprS2(self)
            else:
                return visitor.visitChildren(self)



    def exprS2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprS2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_exprS2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 474
            self.exprS3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 481
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprS2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprS2)
                    self.state = 476
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 477
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUAL) | (1 << MiniGoParser.NOT_EQUAL) | (1 << MiniGoParser.LESS_THAN) | (1 << MiniGoParser.LESS_EQUAL) | (1 << MiniGoParser.GREATER_THAN) | (1 << MiniGoParser.GREATER_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 478
                    self.exprS3(0) 
                self.state = 483
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprS3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprS4(self):
            return self.getTypedRuleContext(MiniGoParser.ExprS4Context,0)


        def exprS3(self):
            return self.getTypedRuleContext(MiniGoParser.ExprS3Context,0)


        def PLUS(self):
            return self.getToken(MiniGoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_exprS3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprS3" ):
                return visitor.visitExprS3(self)
            else:
                return visitor.visitChildren(self)



    def exprS3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprS3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_exprS3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 485
            self.exprS4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 492
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprS3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprS3)
                    self.state = 487
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 488
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 489
                    self.exprS4(0) 
                self.state = 494
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprS4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprS5(self):
            return self.getTypedRuleContext(MiniGoParser.ExprS5Context,0)


        def exprS4(self):
            return self.getTypedRuleContext(MiniGoParser.ExprS4Context,0)


        def MULTI(self):
            return self.getToken(MiniGoParser.MULTI, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MODULO(self):
            return self.getToken(MiniGoParser.MODULO, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_exprS4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprS4" ):
                return visitor.visitExprS4(self)
            else:
                return visitor.visitChildren(self)



    def exprS4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprS4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_exprS4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 496
            self.exprS5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 503
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprS4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprS4)
                    self.state = 498
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 499
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MULTI) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 500
                    self.exprS5() 
                self.state = 505
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprS5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprS5(self):
            return self.getTypedRuleContext(MiniGoParser.ExprS5Context,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def exprS6(self):
            return self.getTypedRuleContext(MiniGoParser.ExprS6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exprS5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprS5" ):
                return visitor.visitExprS5(self)
            else:
                return visitor.visitChildren(self)




    def exprS5(self):

        localctx = MiniGoParser.ExprS5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_exprS5)
        self._la = 0 # Token type
        try:
            self.state = 509
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 506
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.MINUS or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 507
                self.exprS5()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 508
                self.exprS6()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprS6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_ROUND(self):
            return self.getToken(MiniGoParser.OPEN_ROUND, 0)

        def exprS(self):
            return self.getTypedRuleContext(MiniGoParser.ExprSContext,0)


        def CLOSE_ROUND(self):
            return self.getToken(MiniGoParser.CLOSE_ROUND, 0)

        def operandS(self):
            return self.getTypedRuleContext(MiniGoParser.OperandSContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exprS6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprS6" ):
                return visitor.visitExprS6(self)
            else:
                return visitor.visitChildren(self)




    def exprS6(self):

        localctx = MiniGoParser.ExprS6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_exprS6)
        try:
            self.state = 516
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 511
                self.match(MiniGoParser.OPEN_ROUND)
                self.state = 512
                self.exprS(0)
                self.state = 513
                self.match(MiniGoParser.CLOSE_ROUND)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 515
                self.operandS()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandSContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def arrAccess(self):
            return self.getTypedRuleContext(MiniGoParser.ArrAccessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_operandS

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperandS" ):
                return visitor.visitOperandS(self)
            else:
                return visitor.visitChildren(self)




    def operandS(self):

        localctx = MiniGoParser.OperandSContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_operandS)
        try:
            self.state = 520
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 518
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 519
                self.arrAccess()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArrStructAccessContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def accessList(self):
            return self.getTypedRuleContext(MiniGoParser.AccessListContext,0)


        def arrAccess(self):
            return self.getTypedRuleContext(MiniGoParser.ArrAccessContext,0)


        def arrStructAccess(self):
            return self.getTypedRuleContext(MiniGoParser.ArrStructAccessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_arrStructAccess

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArrStructAccess" ):
                return visitor.visitArrStructAccess(self)
            else:
                return visitor.visitChildren(self)



    def arrStructAccess(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ArrStructAccessContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 86
        self.enterRecursionRule(localctx, 86, self.RULE_arrStructAccess, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 525
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.state = 523
                self.accessList()
                pass

            elif la_ == 2:
                self.state = 524
                self.arrAccess()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 531
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,34,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ArrStructAccessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_arrStructAccess)
                    self.state = 527
                    if not self.precpred(self._ctx, 3):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                    self.state = 528
                    self.accessList() 
                self.state = 533
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,34,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AccessListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def positionList(self):
            return self.getTypedRuleContext(MiniGoParser.PositionListContext,0)


        def structAccess(self):
            return self.getTypedRuleContext(MiniGoParser.StructAccessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_accessList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAccessList" ):
                return visitor.visitAccessList(self)
            else:
                return visitor.visitChildren(self)




    def accessList(self):

        localctx = MiniGoParser.AccessListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_accessList)
        try:
            self.state = 536
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,35,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 534
                self.positionList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 535
                self.structAccess()
                pass


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
        self.enterRule(localctx, 90, self.RULE_arrLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 538
            self.arrType()
            self.state = 539
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
        self.enterRule(localctx, 92, self.RULE_arrBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 541
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 542
            self.elementList()
            self.state = 543
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
        self.enterRule(localctx, 94, self.RULE_elementList)
        try:
            self.state = 550
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 545
                self.element()
                self.state = 546
                self.match(MiniGoParser.COMMA)
                self.state = 547
                self.elementList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 549
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

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


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
        self.enterRule(localctx, 96, self.RULE_element)
        try:
            self.state = 554
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.MINUS, MiniGoParser.NOT, MiniGoParser.OPEN_ROUND, MiniGoParser.OPEN_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 552
                self.expr(0)
                pass
            elif token in [MiniGoParser.OPEN_CURVE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 553
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
        self.enterRule(localctx, 98, self.RULE_structLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 556
            self.match(MiniGoParser.ID)
            self.state = 557
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 558
            self.structElList()
            self.state = 559
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
        self.enterRule(localctx, 100, self.RULE_structElList)
        try:
            self.state = 563
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 561
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
        self.enterRule(localctx, 102, self.RULE_structELPrime)
        try:
            self.state = 570
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 565
                self.structEL()
                self.state = 566
                self.match(MiniGoParser.COMMA)
                self.state = 567
                self.structELPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 569
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
        self.enterRule(localctx, 104, self.RULE_structEL)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 572
            self.match(MiniGoParser.ID)
            self.state = 573
            self.match(MiniGoParser.COLON)
            self.state = 574
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
        self.enterRule(localctx, 106, self.RULE_funcCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 576
            self.match(MiniGoParser.ID)
            self.state = 577
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 578
            self.argumentList()
            self.state = 579
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

        def elementList(self):
            return self.getTypedRuleContext(MiniGoParser.ElementListContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_argumentList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = MiniGoParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_argumentList)
        try:
            self.state = 583
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.MINUS, MiniGoParser.NOT, MiniGoParser.OPEN_ROUND, MiniGoParser.OPEN_CURVE, MiniGoParser.OPEN_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 581
                self.elementList()
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


    class MethodCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprM(self):
            return self.getTypedRuleContext(MiniGoParser.ExprMContext,0)


        def DOT(self):
            return self.getToken(MiniGoParser.DOT, 0)

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def OPEN_ROUND(self):
            return self.getToken(MiniGoParser.OPEN_ROUND, 0)

        def argumentList(self):
            return self.getTypedRuleContext(MiniGoParser.ArgumentListContext,0)


        def CLOSE_ROUND(self):
            return self.getToken(MiniGoParser.CLOSE_ROUND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_methodCall

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMethodCall" ):
                return visitor.visitMethodCall(self)
            else:
                return visitor.visitChildren(self)




    def methodCall(self):

        localctx = MiniGoParser.MethodCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_methodCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 585
            self.exprM(0)
            self.state = 586
            self.match(MiniGoParser.DOT)
            self.state = 587
            self.match(MiniGoParser.ID)
            self.state = 588
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 589
            self.argumentList()
            self.state = 590
            self.match(MiniGoParser.CLOSE_ROUND)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprMContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprM1(self):
            return self.getTypedRuleContext(MiniGoParser.ExprM1Context,0)


        def exprM(self):
            return self.getTypedRuleContext(MiniGoParser.ExprMContext,0)


        def OR(self):
            return self.getToken(MiniGoParser.OR, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_exprM

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprM" ):
                return visitor.visitExprM(self)
            else:
                return visitor.visitChildren(self)



    def exprM(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprMContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 112
        self.enterRecursionRule(localctx, 112, self.RULE_exprM, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 593
            self.exprM1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 600
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprMContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprM)
                    self.state = 595
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 596
                    self.match(MiniGoParser.OR)
                    self.state = 597
                    self.exprM1(0) 
                self.state = 602
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprM1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprM2(self):
            return self.getTypedRuleContext(MiniGoParser.ExprM2Context,0)


        def exprM1(self):
            return self.getTypedRuleContext(MiniGoParser.ExprM1Context,0)


        def AND(self):
            return self.getToken(MiniGoParser.AND, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_exprM1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprM1" ):
                return visitor.visitExprM1(self)
            else:
                return visitor.visitChildren(self)



    def exprM1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprM1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 114
        self.enterRecursionRule(localctx, 114, self.RULE_exprM1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
            self.exprM2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 611
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprM1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprM1)
                    self.state = 606
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 607
                    self.match(MiniGoParser.AND)
                    self.state = 608
                    self.exprM2(0) 
                self.state = 613
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprM2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprM3(self):
            return self.getTypedRuleContext(MiniGoParser.ExprM3Context,0)


        def exprM2(self):
            return self.getTypedRuleContext(MiniGoParser.ExprM2Context,0)


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
            return MiniGoParser.RULE_exprM2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprM2" ):
                return visitor.visitExprM2(self)
            else:
                return visitor.visitChildren(self)



    def exprM2(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprM2Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 116
        self.enterRecursionRule(localctx, 116, self.RULE_exprM2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 615
            self.exprM3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 622
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprM2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprM2)
                    self.state = 617
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 618
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUAL) | (1 << MiniGoParser.NOT_EQUAL) | (1 << MiniGoParser.LESS_THAN) | (1 << MiniGoParser.LESS_EQUAL) | (1 << MiniGoParser.GREATER_THAN) | (1 << MiniGoParser.GREATER_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 619
                    self.exprM3(0) 
                self.state = 624
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprM3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprM4(self):
            return self.getTypedRuleContext(MiniGoParser.ExprM4Context,0)


        def exprM3(self):
            return self.getTypedRuleContext(MiniGoParser.ExprM3Context,0)


        def PLUS(self):
            return self.getToken(MiniGoParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_exprM3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprM3" ):
                return visitor.visitExprM3(self)
            else:
                return visitor.visitChildren(self)



    def exprM3(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprM3Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 118
        self.enterRecursionRule(localctx, 118, self.RULE_exprM3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 626
            self.exprM4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 633
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprM3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprM3)
                    self.state = 628
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 629
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 630
                    self.exprM4(0) 
                self.state = 635
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprM4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprM5(self):
            return self.getTypedRuleContext(MiniGoParser.ExprM5Context,0)


        def exprM4(self):
            return self.getTypedRuleContext(MiniGoParser.ExprM4Context,0)


        def MULTI(self):
            return self.getToken(MiniGoParser.MULTI, 0)

        def DIV(self):
            return self.getToken(MiniGoParser.DIV, 0)

        def MODULO(self):
            return self.getToken(MiniGoParser.MODULO, 0)

        def getRuleIndex(self):
            return MiniGoParser.RULE_exprM4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprM4" ):
                return visitor.visitExprM4(self)
            else:
                return visitor.visitChildren(self)



    def exprM4(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = MiniGoParser.ExprM4Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 120
        self.enterRecursionRule(localctx, 120, self.RULE_exprM4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 637
            self.exprM5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 644
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,45,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprM4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprM4)
                    self.state = 639
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 640
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MULTI) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 641
                    self.exprM5() 
                self.state = 646
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,45,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class ExprM5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exprM5(self):
            return self.getTypedRuleContext(MiniGoParser.ExprM5Context,0)


        def NOT(self):
            return self.getToken(MiniGoParser.NOT, 0)

        def MINUS(self):
            return self.getToken(MiniGoParser.MINUS, 0)

        def exprM6(self):
            return self.getTypedRuleContext(MiniGoParser.ExprM6Context,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exprM5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprM5" ):
                return visitor.visitExprM5(self)
            else:
                return visitor.visitChildren(self)




    def exprM5(self):

        localctx = MiniGoParser.ExprM5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 122, self.RULE_exprM5)
        self._la = 0 # Token type
        try:
            self.state = 650
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 647
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.MINUS or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 648
                self.exprM5()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 649
                self.exprM6()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprM6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPEN_ROUND(self):
            return self.getToken(MiniGoParser.OPEN_ROUND, 0)

        def exprM(self):
            return self.getTypedRuleContext(MiniGoParser.ExprMContext,0)


        def CLOSE_ROUND(self):
            return self.getToken(MiniGoParser.CLOSE_ROUND, 0)

        def operandM(self):
            return self.getTypedRuleContext(MiniGoParser.OperandMContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_exprM6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExprM6" ):
                return visitor.visitExprM6(self)
            else:
                return visitor.visitChildren(self)




    def exprM6(self):

        localctx = MiniGoParser.ExprM6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 124, self.RULE_exprM6)
        try:
            self.state = 657
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 652
                self.match(MiniGoParser.OPEN_ROUND)
                self.state = 653
                self.exprM(0)
                self.state = 654
                self.match(MiniGoParser.CLOSE_ROUND)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 656
                self.operandM()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperandMContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def arrStructAccess(self):
            return self.getTypedRuleContext(MiniGoParser.ArrStructAccessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_operandM

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperandM" ):
                return visitor.visitOperandM(self)
            else:
                return visitor.visitChildren(self)




    def operandM(self):

        localctx = MiniGoParser.OperandMContext(self, self._ctx, self.state)
        self.enterRule(localctx, 126, self.RULE_operandM)
        try:
            self.state = 662
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 659
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 660
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 661
                self.arrStructAccess(0)
                pass


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
        _startState = 128
        self.enterRecursionRule(localctx, 128, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 665
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 672
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,49,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 667
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 668
                    self.match(MiniGoParser.OR)
                    self.state = 669
                    self.expr1(0) 
                self.state = 674
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,49,self._ctx)

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
        _startState = 130
        self.enterRecursionRule(localctx, 130, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 676
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 683
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 678
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 679
                    self.match(MiniGoParser.AND)
                    self.state = 680
                    self.expr2(0) 
                self.state = 685
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

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
        _startState = 132
        self.enterRecursionRule(localctx, 132, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 687
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 694
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 689
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 690
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUAL) | (1 << MiniGoParser.NOT_EQUAL) | (1 << MiniGoParser.LESS_THAN) | (1 << MiniGoParser.LESS_EQUAL) | (1 << MiniGoParser.GREATER_THAN) | (1 << MiniGoParser.GREATER_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 691
                    self.expr3(0) 
                self.state = 696
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

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
        _startState = 134
        self.enterRecursionRule(localctx, 134, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 698
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 705
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,52,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 700
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 701
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 702
                    self.expr4(0) 
                self.state = 707
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,52,self._ctx)

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
        _startState = 136
        self.enterRecursionRule(localctx, 136, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 709
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 716
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,53,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 711
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 712
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MULTI) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 713
                    self.expr5() 
                self.state = 718
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,53,self._ctx)

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
        self.enterRule(localctx, 138, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 722
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 719
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.MINUS or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 720
                self.expr5()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 721
                self.expr6()
                pass


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

        def OPEN_ROUND(self):
            return self.getToken(MiniGoParser.OPEN_ROUND, 0)

        def expr(self):
            return self.getTypedRuleContext(MiniGoParser.ExprContext,0)


        def CLOSE_ROUND(self):
            return self.getToken(MiniGoParser.CLOSE_ROUND, 0)

        def operand(self):
            return self.getTypedRuleContext(MiniGoParser.OperandContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_expr6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr6" ):
                return visitor.visitExpr6(self)
            else:
                return visitor.visitChildren(self)




    def expr6(self):

        localctx = MiniGoParser.Expr6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 140, self.RULE_expr6)
        try:
            self.state = 729
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,55,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 724
                self.match(MiniGoParser.OPEN_ROUND)
                self.state = 725
                self.expr(0)
                self.state = 726
                self.match(MiniGoParser.CLOSE_ROUND)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 728
                self.operand()
                pass


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

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def OPEN_CURVE(self):
            return self.getToken(MiniGoParser.OPEN_CURVE, 0)

        def structElList(self):
            return self.getTypedRuleContext(MiniGoParser.StructElListContext,0)


        def CLOSE_CURVE(self):
            return self.getToken(MiniGoParser.CLOSE_CURVE, 0)

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def funcCall(self):
            return self.getTypedRuleContext(MiniGoParser.FuncCallContext,0)


        def methodCall(self):
            return self.getTypedRuleContext(MiniGoParser.MethodCallContext,0)


        def arrStructAccess(self):
            return self.getTypedRuleContext(MiniGoParser.ArrStructAccessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = MiniGoParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 142, self.RULE_operand)
        try:
            self.state = 744
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,57,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 731
                self.match(MiniGoParser.ID)
                self.state = 737
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
                if la_ == 1:
                    self.state = 732
                    self.match(MiniGoParser.OPEN_CURVE)
                    self.state = 733
                    self.structElList()
                    self.state = 734
                    self.match(MiniGoParser.CLOSE_CURVE)
                    pass

                elif la_ == 2:
                    pass


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 739
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 740
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 741
                self.funcCall()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 742
                self.methodCall()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 743
                self.arrStructAccess(0)
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
        self.enterRule(localctx, 144, self.RULE_literal)
        try:
            self.state = 749
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 746
                self.literalConst()
                pass
            elif token in [MiniGoParser.OPEN_SQUARE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 747
                self.arrLit()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 748
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
        self.enterRule(localctx, 146, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 760
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.state = 751
                self.varDeclStatement()
                pass

            elif la_ == 2:
                self.state = 752
                self.constDeclStatement()
                pass

            elif la_ == 3:
                self.state = 753
                self.assignment()
                pass

            elif la_ == 4:
                self.state = 754
                self.ifStatement()
                pass

            elif la_ == 5:
                self.state = 755
                self.forStatement()
                pass

            elif la_ == 6:
                self.state = 756
                self.breakStatement()
                pass

            elif la_ == 7:
                self.state = 757
                self.continueStatement()
                pass

            elif la_ == 8:
                self.state = 758
                self.callStatement()
                pass

            elif la_ == 9:
                self.state = 759
                self.returnStatement()
                pass


            self.state = 762
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
        self.enterRule(localctx, 148, self.RULE_statementList)
        try:
            self.state = 768
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 764
                self.statement()
                self.state = 765
                self.statementList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 767
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
        self.enterRule(localctx, 150, self.RULE_varDeclStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 770
            self.match(MiniGoParser.VAR)
            self.state = 771
            self.match(MiniGoParser.ID)
            self.state = 779
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.state = 772
                self.typee()
                self.state = 773
                self.match(MiniGoParser.ASSIGN)
                self.state = 774
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 776
                self.match(MiniGoParser.ASSIGN)
                self.state = 777
                self.expr(0)
                pass

            elif la_ == 3:
                self.state = 778
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
        self.enterRule(localctx, 152, self.RULE_constDeclStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 781
            self.match(MiniGoParser.CONST)
            self.state = 782
            self.match(MiniGoParser.ID)
            self.state = 783
            self.match(MiniGoParser.ASSIGN)
            self.state = 786
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,62,self._ctx)
            if la_ == 1:
                self.state = 784
                self.literalConst()
                pass

            elif la_ == 2:
                self.state = 785
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
        self.enterRule(localctx, 154, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 788
            self.lhs()
            self.state = 789
            self.assignOperator()
            self.state = 790
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

        def arrStructAccess(self):
            return self.getTypedRuleContext(MiniGoParser.ArrStructAccessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = MiniGoParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 156, self.RULE_lhs)
        try:
            self.state = 794
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 792
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 793
                self.arrStructAccess(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
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
        self.enterRule(localctx, 158, self.RULE_assignOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 796
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
        self.enterRule(localctx, 160, self.RULE_rhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 798
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
        self.enterRule(localctx, 162, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 800
            self.match(MiniGoParser.IF)
            self.state = 801
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 802
            self.expr(0)
            self.state = 803
            self.match(MiniGoParser.CLOSE_ROUND)
            self.state = 804
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 805
            self.statementList()
            self.state = 806
            self.match(MiniGoParser.CLOSE_CURVE)
            self.state = 807
            self.elifList()
            self.state = 813
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 808
                self.match(MiniGoParser.ELSE)
                self.state = 809
                self.match(MiniGoParser.OPEN_CURVE)
                self.state = 810
                self.statementList()
                self.state = 811
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
        self.enterRule(localctx, 164, self.RULE_elifList)
        try:
            self.state = 819
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,65,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 815
                self.eliff()
                self.state = 816
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
        self.enterRule(localctx, 166, self.RULE_eliff)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 821
            self.match(MiniGoParser.ELSE)
            self.state = 822
            self.match(MiniGoParser.IF)
            self.state = 823
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 824
            self.expr(0)
            self.state = 825
            self.match(MiniGoParser.CLOSE_ROUND)
            self.state = 826
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 827
            self.statementList()
            self.state = 828
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
        self.enterRule(localctx, 168, self.RULE_forStatement)
        try:
            self.state = 833
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,66,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 830
                self.forBasic()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 831
                self.forInitial()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 832
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
        self.enterRule(localctx, 170, self.RULE_forBasic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 835
            self.match(MiniGoParser.FOR)
            self.state = 836
            self.expr(0)
            self.state = 837
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 838
            self.statementList()
            self.state = 839
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
        self.enterRule(localctx, 172, self.RULE_forInitial)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 841
            self.match(MiniGoParser.FOR)
            self.state = 842
            self.initialization()
            self.state = 843
            self.match(MiniGoParser.SEMICOLON)
            self.state = 844
            self.condition()
            self.state = 845
            self.match(MiniGoParser.SEMICOLON)
            self.state = 846
            self.update()
            self.state = 847
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 848
            self.statementList()
            self.state = 849
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
        self.enterRule(localctx, 174, self.RULE_initialization)
        try:
            self.state = 853
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 851
                self.assignScalar()
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 852
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
        self.enterRule(localctx, 176, self.RULE_varDeclInitial)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 855
            self.match(MiniGoParser.VAR)
            self.state = 856
            self.match(MiniGoParser.ID)
            self.state = 858
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.OPEN_SQUARE) | (1 << MiniGoParser.ID))) != 0):
                self.state = 857
                self.typee()


            self.state = 860
            self.match(MiniGoParser.ASSIGN)
            self.state = 861
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
        self.enterRule(localctx, 178, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 863
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
        self.enterRule(localctx, 180, self.RULE_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 865
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
        self.enterRule(localctx, 182, self.RULE_assignScalar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 867
            self.match(MiniGoParser.ID)
            self.state = 868
            self.assignOperator()
            self.state = 869
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
        self.enterRule(localctx, 184, self.RULE_forRange)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 871
            self.match(MiniGoParser.FOR)
            self.state = 872
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.T__0 or _la==MiniGoParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 873
            self.match(MiniGoParser.COMMA)
            self.state = 874
            self.match(MiniGoParser.ID)
            self.state = 875
            self.match(MiniGoParser.ASSIGN1)
            self.state = 876
            self.match(MiniGoParser.RANGE)
            self.state = 877
            self.match(MiniGoParser.ID)
            self.state = 878
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 879
            self.statementList()
            self.state = 880
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
        self.enterRule(localctx, 186, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 882
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
        self.enterRule(localctx, 188, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 884
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


        def methodCall(self):
            return self.getTypedRuleContext(MiniGoParser.MethodCallContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_callStatement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCallStatement" ):
                return visitor.visitCallStatement(self)
            else:
                return visitor.visitChildren(self)




    def callStatement(self):

        localctx = MiniGoParser.CallStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 190, self.RULE_callStatement)
        try:
            self.state = 888
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,69,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 886
                self.funcCall()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 887
                self.methodCall()
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
        self.enterRule(localctx, 192, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 890
            self.match(MiniGoParser.RETURN)
            self.state = 891
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
        self._predicates[25] = self.exprA_sempred
        self._predicates[26] = self.exprA1_sempred
        self._predicates[27] = self.exprA2_sempred
        self._predicates[28] = self.exprA3_sempred
        self._predicates[29] = self.exprA4_sempred
        self._predicates[34] = self.refList_sempred
        self._predicates[35] = self.exprS_sempred
        self._predicates[36] = self.exprS1_sempred
        self._predicates[37] = self.exprS2_sempred
        self._predicates[38] = self.exprS3_sempred
        self._predicates[39] = self.exprS4_sempred
        self._predicates[43] = self.arrStructAccess_sempred
        self._predicates[56] = self.exprM_sempred
        self._predicates[57] = self.exprM1_sempred
        self._predicates[58] = self.exprM2_sempred
        self._predicates[59] = self.exprM3_sempred
        self._predicates[60] = self.exprM4_sempred
        self._predicates[64] = self.expr_sempred
        self._predicates[65] = self.expr1_sempred
        self._predicates[66] = self.expr2_sempred
        self._predicates[67] = self.expr3_sempred
        self._predicates[68] = self.expr4_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exprA_sempred(self, localctx:ExprAContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exprA1_sempred(self, localctx:ExprA1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exprA2_sempred(self, localctx:ExprA2Context, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def exprA3_sempred(self, localctx:ExprA3Context, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         

    def exprA4_sempred(self, localctx:ExprA4Context, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def refList_sempred(self, localctx:RefListContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def exprS_sempred(self, localctx:ExprSContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         

    def exprS1_sempred(self, localctx:ExprS1Context, predIndex:int):
            if predIndex == 7:
                return self.precpred(self._ctx, 2)
         

    def exprS2_sempred(self, localctx:ExprS2Context, predIndex:int):
            if predIndex == 8:
                return self.precpred(self._ctx, 2)
         

    def exprS3_sempred(self, localctx:ExprS3Context, predIndex:int):
            if predIndex == 9:
                return self.precpred(self._ctx, 2)
         

    def exprS4_sempred(self, localctx:ExprS4Context, predIndex:int):
            if predIndex == 10:
                return self.precpred(self._ctx, 2)
         

    def arrStructAccess_sempred(self, localctx:ArrStructAccessContext, predIndex:int):
            if predIndex == 11:
                return self.precpred(self._ctx, 3)
         

    def exprM_sempred(self, localctx:ExprMContext, predIndex:int):
            if predIndex == 12:
                return self.precpred(self._ctx, 2)
         

    def exprM1_sempred(self, localctx:ExprM1Context, predIndex:int):
            if predIndex == 13:
                return self.precpred(self._ctx, 2)
         

    def exprM2_sempred(self, localctx:ExprM2Context, predIndex:int):
            if predIndex == 14:
                return self.precpred(self._ctx, 2)
         

    def exprM3_sempred(self, localctx:ExprM3Context, predIndex:int):
            if predIndex == 15:
                return self.precpred(self._ctx, 2)
         

    def exprM4_sempred(self, localctx:ExprM4Context, predIndex:int):
            if predIndex == 16:
                return self.precpred(self._ctx, 2)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 17:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 18:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 19:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 20:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 21:
                return self.precpred(self._ctx, 2)
         




