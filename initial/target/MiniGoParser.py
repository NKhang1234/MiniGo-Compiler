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
        buf.write("\u037b\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("_\t_\4`\t`\4a\ta\4b\tb\4c\tc\3\2\6\2\u00c8\n\2\r\2\16")
        buf.write("\2\u00c9\3\2\3\2\3\3\3\3\3\3\3\3\3\3\3\3\5\3\u00d4\n\3")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u00dc\n\4\3\5\3\5\3\5\3\6")
        buf.write("\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u00e8\n\6\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\7\3\7\3\7\3\b\3\b\3\t\3\t\3\t\3\t\5\t\u00f8\n\t")
        buf.write("\3\n\3\n\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\r\3\r\3\r\3\r\5\r\u010c\n\r\3\16\3\16\3")
        buf.write("\16\3\16\3\16\5\16\u0113\n\16\3\16\3\16\3\17\3\17\5\17")
        buf.write("\u0119\n\17\3\20\3\20\3\20\3\20\3\20\5\20\u0120\n\20\3")
        buf.write("\21\3\21\3\21\3\22\3\22\3\22\3\22\5\22\u0129\n\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u0134\n")
        buf.write("\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\5\24\u013d\n\24")
        buf.write("\3\24\3\24\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\5\26")
        buf.write("\u0149\n\26\3\26\3\26\3\26\3\26\3\26\3\27\3\27\5\27\u0152")
        buf.write("\n\27\3\30\3\30\3\30\3\30\3\30\5\30\u0159\n\30\3\31\3")
        buf.write("\31\3\31\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\5\33\u016a\n\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35")
        buf.write("\3\35\3\35\5\35\u017d\n\35\3\36\3\36\3\36\3\36\3\36\3")
        buf.write("\36\7\36\u0185\n\36\f\36\16\36\u0188\13\36\3\37\3\37\3")
        buf.write("\37\3\37\3\37\3\37\7\37\u0190\n\37\f\37\16\37\u0193\13")
        buf.write("\37\3 \3 \3 \3 \3 \3 \7 \u019b\n \f \16 \u019e\13 \3!")
        buf.write("\3!\3!\3!\3!\3!\7!\u01a6\n!\f!\16!\u01a9\13!\3\"\3\"\3")
        buf.write("\"\3\"\3\"\3\"\7\"\u01b1\n\"\f\"\16\"\u01b4\13\"\3#\3")
        buf.write("#\3#\5#\u01b9\n#\3$\3$\3$\3$\3$\5$\u01c0\n$\3%\3%\3%\5")
        buf.write("%\u01c5\n%\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\7\'\u01d1")
        buf.write("\n\'\f\'\16\'\u01d4\13\'\3(\3(\3(\3(\3(\3(\7(\u01dc\n")
        buf.write("(\f(\16(\u01df\13(\3)\3)\3)\3)\3)\3)\7)\u01e7\n)\f)\16")
        buf.write(")\u01ea\13)\3*\3*\3*\3*\3*\3*\7*\u01f2\n*\f*\16*\u01f5")
        buf.write("\13*\3+\3+\3+\3+\3+\3+\7+\u01fd\n+\f+\16+\u0200\13+\3")
        buf.write(",\3,\3,\3,\3,\3,\7,\u0208\n,\f,\16,\u020b\13,\3-\3-\3")
        buf.write("-\5-\u0210\n-\3.\3.\3.\3.\3.\5.\u0217\n.\3/\3/\5/\u021b")
        buf.write("\n/\3\60\3\60\3\60\3\61\3\61\3\61\3\61\3\62\3\62\3\62")
        buf.write("\3\62\3\62\5\62\u0229\n\62\3\63\3\63\5\63\u022d\n\63\3")
        buf.write("\64\3\64\3\64\3\64\3\64\3\65\3\65\5\65\u0236\n\65\3\66")
        buf.write("\3\66\3\66\3\66\3\66\5\66\u023d\n\66\3\67\3\67\3\67\3")
        buf.write("\67\38\38\38\38\38\39\39\59\u024a\n9\3:\3:\3:\3:\3:\3")
        buf.write(":\3:\3;\3;\3;\3;\3;\3;\7;\u0259\n;\f;\16;\u025c\13;\3")
        buf.write("<\3<\3<\3<\3<\3<\7<\u0264\n<\f<\16<\u0267\13<\3=\3=\3")
        buf.write("=\3=\3=\3=\7=\u026f\n=\f=\16=\u0272\13=\3>\3>\3>\3>\3")
        buf.write(">\3>\7>\u027a\n>\f>\16>\u027d\13>\3?\3?\3?\3?\3?\3?\7")
        buf.write("?\u0285\n?\f?\16?\u0288\13?\3@\3@\3@\5@\u028d\n@\3A\3")
        buf.write("A\3A\3A\3A\5A\u0294\nA\3B\3B\3B\3B\5B\u029a\nB\3C\3C\3")
        buf.write("C\3C\3C\3C\7C\u02a2\nC\fC\16C\u02a5\13C\3D\3D\3D\3D\3")
        buf.write("D\3D\7D\u02ad\nD\fD\16D\u02b0\13D\3E\3E\3E\3E\3E\3E\7")
        buf.write("E\u02b8\nE\fE\16E\u02bb\13E\3F\3F\3F\3F\3F\3F\7F\u02c3")
        buf.write("\nF\fF\16F\u02c6\13F\3G\3G\3G\3G\3G\3G\7G\u02ce\nG\fG")
        buf.write("\16G\u02d1\13G\3H\3H\3H\5H\u02d6\nH\3I\3I\3I\3I\3I\5I")
        buf.write("\u02dd\nI\3J\3J\3J\3J\3J\3J\5J\u02e5\nJ\3K\3K\3K\5K\u02ea")
        buf.write("\nK\3L\3L\3L\3L\3L\3L\3L\3L\3L\5L\u02f5\nL\3L\3L\3M\3")
        buf.write("M\5M\u02fb\nM\3N\3N\3N\3N\5N\u0301\nN\3O\3O\3O\3O\3O\3")
        buf.write("O\3O\3O\3O\5O\u030c\nO\3P\3P\3P\3P\3P\5P\u0313\nP\3Q\3")
        buf.write("Q\3Q\3Q\3R\3R\3R\5R\u031c\nR\3S\3S\3T\3T\3U\3U\3U\3U\3")
        buf.write("U\3U\3U\3U\3U\3U\3U\3U\3U\5U\u032f\nU\3V\3V\3V\3V\5V\u0335")
        buf.write("\nV\3W\3W\3W\3W\3W\3W\3W\3W\3W\3X\3X\3X\5X\u0343\nX\3")
        buf.write("Y\3Y\3Y\3Y\3Y\3Y\3Z\3Z\3Z\3Z\3Z\3Z\3Z\3Z\3Z\3Z\3[\3[\5")
        buf.write("[\u0357\n[\3\\\3\\\3\\\5\\\u035c\n\\\3\\\3\\\3\\\3]\3")
        buf.write("]\3^\3^\3_\3_\3_\3_\3_\3_\3_\3_\3_\3_\3_\3`\3`\3a\3a\3")
        buf.write("b\3b\5b\u0376\nb\3c\3c\3c\3c\2\27:<>@BLNPRTVtvxz|\u0084")
        buf.write("\u0086\u0088\u008a\u008cd\2\4\6\b\n\f\16\20\22\24\26\30")
        buf.write("\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`b")
        buf.write("dfhjlnprtvxz|~\u0080\u0082\u0084\u0086\u0088\u008a\u008c")
        buf.write("\u008e\u0090\u0092\u0094\u0096\u0098\u009a\u009c\u009e")
        buf.write("\u00a0\u00a2\u00a4\u00a6\u00a8\u00aa\u00ac\u00ae\u00b0")
        buf.write("\u00b2\u00b4\u00b6\u00b8\u00ba\u00bc\u00be\u00c0\u00c2")
        buf.write("\u00c4\2\f\4\2\f\17\67\67\3\2\678\4\2\66\66==\4\2\25\27")
        buf.write("8:\3\2\35\"\3\2\30\31\3\2\32\34\4\2\31\31%%\3\2\',\4\2")
        buf.write("\3\3\67\67\2\u0377\2\u00c7\3\2\2\2\4\u00d3\3\2\2\2\6\u00db")
        buf.write("\3\2\2\2\b\u00dd\3\2\2\2\n\u00e7\3\2\2\2\f\u00e9\3\2\2")
        buf.write("\2\16\u00f1\3\2\2\2\20\u00f7\3\2\2\2\22\u00f9\3\2\2\2")
        buf.write("\24\u00fd\3\2\2\2\26\u0105\3\2\2\2\30\u010b\3\2\2\2\32")
        buf.write("\u010d\3\2\2\2\34\u0118\3\2\2\2\36\u011f\3\2\2\2 \u0121")
        buf.write("\3\2\2\2\"\u0128\3\2\2\2$\u012a\3\2\2\2&\u0137\3\2\2\2")
        buf.write("(\u0140\3\2\2\2*\u0142\3\2\2\2,\u0151\3\2\2\2.\u0158\3")
        buf.write("\2\2\2\60\u015a\3\2\2\2\62\u015d\3\2\2\2\64\u015f\3\2")
        buf.write("\2\2\66\u0170\3\2\2\28\u017c\3\2\2\2:\u017e\3\2\2\2<\u0189")
        buf.write("\3\2\2\2>\u0194\3\2\2\2@\u019f\3\2\2\2B\u01aa\3\2\2\2")
        buf.write("D\u01b8\3\2\2\2F\u01bf\3\2\2\2H\u01c4\3\2\2\2J\u01c6\3")
        buf.write("\2\2\2L\u01ca\3\2\2\2N\u01d5\3\2\2\2P\u01e0\3\2\2\2R\u01eb")
        buf.write("\3\2\2\2T\u01f6\3\2\2\2V\u0201\3\2\2\2X\u020f\3\2\2\2")
        buf.write("Z\u0216\3\2\2\2\\\u021a\3\2\2\2^\u021c\3\2\2\2`\u021f")
        buf.write("\3\2\2\2b\u0228\3\2\2\2d\u022c\3\2\2\2f\u022e\3\2\2\2")
        buf.write("h\u0235\3\2\2\2j\u023c\3\2\2\2l\u023e\3\2\2\2n\u0242\3")
        buf.write("\2\2\2p\u0249\3\2\2\2r\u024b\3\2\2\2t\u0252\3\2\2\2v\u025d")
        buf.write("\3\2\2\2x\u0268\3\2\2\2z\u0273\3\2\2\2|\u027e\3\2\2\2")
        buf.write("~\u028c\3\2\2\2\u0080\u0293\3\2\2\2\u0082\u0299\3\2\2")
        buf.write("\2\u0084\u029b\3\2\2\2\u0086\u02a6\3\2\2\2\u0088\u02b1")
        buf.write("\3\2\2\2\u008a\u02bc\3\2\2\2\u008c\u02c7\3\2\2\2\u008e")
        buf.write("\u02d5\3\2\2\2\u0090\u02dc\3\2\2\2\u0092\u02e4\3\2\2\2")
        buf.write("\u0094\u02e9\3\2\2\2\u0096\u02f4\3\2\2\2\u0098\u02fa\3")
        buf.write("\2\2\2\u009a\u0300\3\2\2\2\u009c\u0302\3\2\2\2\u009e\u030d")
        buf.write("\3\2\2\2\u00a0\u0314\3\2\2\2\u00a2\u031b\3\2\2\2\u00a4")
        buf.write("\u031d\3\2\2\2\u00a6\u031f\3\2\2\2\u00a8\u0321\3\2\2\2")
        buf.write("\u00aa\u0334\3\2\2\2\u00ac\u0336\3\2\2\2\u00ae\u0342\3")
        buf.write("\2\2\2\u00b0\u0344\3\2\2\2\u00b2\u034a\3\2\2\2\u00b4\u0356")
        buf.write("\3\2\2\2\u00b6\u0358\3\2\2\2\u00b8\u0360\3\2\2\2\u00ba")
        buf.write("\u0362\3\2\2\2\u00bc\u0364\3\2\2\2\u00be\u036f\3\2\2\2")
        buf.write("\u00c0\u0371\3\2\2\2\u00c2\u0375\3\2\2\2\u00c4\u0377\3")
        buf.write("\2\2\2\u00c6\u00c8\5\4\3\2\u00c7\u00c6\3\2\2\2\u00c8\u00c9")
        buf.write("\3\2\2\2\u00c9\u00c7\3\2\2\2\u00c9\u00ca\3\2\2\2\u00ca")
        buf.write("\u00cb\3\2\2\2\u00cb\u00cc\7\2\2\3\u00cc\3\3\2\2\2\u00cd")
        buf.write("\u00d4\5\f\7\2\u00ce\u00d4\5\24\13\2\u00cf\u00d4\5$\23")
        buf.write("\2\u00d0\u00d4\5&\24\2\u00d1\u00d4\5*\26\2\u00d2\u00d4")
        buf.write("\5\64\33\2\u00d3\u00cd\3\2\2\2\u00d3\u00ce\3\2\2\2\u00d3")
        buf.write("\u00cf\3\2\2\2\u00d3\u00d0\3\2\2\2\u00d3\u00d1\3\2\2\2")
        buf.write("\u00d3\u00d2\3\2\2\2\u00d4\5\3\2\2\2\u00d5\u00dc\7\r\2")
        buf.write("\2\u00d6\u00dc\7\16\2\2\u00d7\u00dc\7\17\2\2\u00d8\u00dc")
        buf.write("\7\f\2\2\u00d9\u00dc\5\b\5\2\u00da\u00dc\7\67\2\2\u00db")
        buf.write("\u00d5\3\2\2\2\u00db\u00d6\3\2\2\2\u00db\u00d7\3\2\2\2")
        buf.write("\u00db\u00d8\3\2\2\2\u00db\u00d9\3\2\2\2\u00db\u00da\3")
        buf.write("\2\2\2\u00dc\7\3\2\2\2\u00dd\u00de\5\n\6\2\u00de\u00df")
        buf.write("\t\2\2\2\u00df\t\3\2\2\2\u00e0\u00e1\7\63\2\2\u00e1\u00e2")
        buf.write("\t\3\2\2\u00e2\u00e3\7\64\2\2\u00e3\u00e8\5\n\6\2\u00e4")
        buf.write("\u00e5\7\63\2\2\u00e5\u00e6\t\3\2\2\u00e6\u00e8\7\64\2")
        buf.write("\2\u00e7\u00e0\3\2\2\2\u00e7\u00e4\3\2\2\2\u00e8\13\3")
        buf.write("\2\2\2\u00e9\u00ea\7\t\2\2\u00ea\u00eb\7\67\2\2\u00eb")
        buf.write("\u00ec\7\n\2\2\u00ec\u00ed\7\61\2\2\u00ed\u00ee\5\16\b")
        buf.write("\2\u00ee\u00ef\7\62\2\2\u00ef\u00f0\t\4\2\2\u00f0\r\3")
        buf.write("\2\2\2\u00f1\u00f2\5\20\t\2\u00f2\17\3\2\2\2\u00f3\u00f4")
        buf.write("\5\22\n\2\u00f4\u00f5\5\20\t\2\u00f5\u00f8\3\2\2\2\u00f6")
        buf.write("\u00f8\5\22\n\2\u00f7\u00f3\3\2\2\2\u00f7\u00f6\3\2\2")
        buf.write("\2\u00f8\21\3\2\2\2\u00f9\u00fa\7\67\2\2\u00fa\u00fb\5")
        buf.write("\6\4\2\u00fb\u00fc\t\4\2\2\u00fc\23\3\2\2\2\u00fd\u00fe")
        buf.write("\7\t\2\2\u00fe\u00ff\7\67\2\2\u00ff\u0100\7\13\2\2\u0100")
        buf.write("\u0101\7\61\2\2\u0101\u0102\5\26\f\2\u0102\u0103\7\62")
        buf.write("\2\2\u0103\u0104\t\4\2\2\u0104\25\3\2\2\2\u0105\u0106")
        buf.write("\5\30\r\2\u0106\27\3\2\2\2\u0107\u0108\5\32\16\2\u0108")
        buf.write("\u0109\5\30\r\2\u0109\u010c\3\2\2\2\u010a\u010c\5\32\16")
        buf.write("\2\u010b\u0107\3\2\2\2\u010b\u010a\3\2\2\2\u010c\31\3")
        buf.write("\2\2\2\u010d\u010e\7\67\2\2\u010e\u010f\7/\2\2\u010f\u0110")
        buf.write("\5\34\17\2\u0110\u0112\7\60\2\2\u0111\u0113\5\6\4\2\u0112")
        buf.write("\u0111\3\2\2\2\u0112\u0113\3\2\2\2\u0113\u0114\3\2\2\2")
        buf.write("\u0114\u0115\t\4\2\2\u0115\33\3\2\2\2\u0116\u0119\5\36")
        buf.write("\20\2\u0117\u0119\3\2\2\2\u0118\u0116\3\2\2\2\u0118\u0117")
        buf.write("\3\2\2\2\u0119\35\3\2\2\2\u011a\u011b\5 \21\2\u011b\u011c")
        buf.write("\7\65\2\2\u011c\u011d\5\36\20\2\u011d\u0120\3\2\2\2\u011e")
        buf.write("\u0120\5 \21\2\u011f\u011a\3\2\2\2\u011f\u011e\3\2\2\2")
        buf.write("\u0120\37\3\2\2\2\u0121\u0122\5\"\22\2\u0122\u0123\5\6")
        buf.write("\4\2\u0123!\3\2\2\2\u0124\u0125\7\67\2\2\u0125\u0126\7")
        buf.write("\65\2\2\u0126\u0129\5\"\22\2\u0127\u0129\7\67\2\2\u0128")
        buf.write("\u0124\3\2\2\2\u0128\u0127\3\2\2\2\u0129#\3\2\2\2\u012a")
        buf.write("\u012b\7\21\2\2\u012b\u0133\7\67\2\2\u012c\u012d\5\6\4")
        buf.write("\2\u012d\u012e\7&\2\2\u012e\u012f\5\u0084C\2\u012f\u0134")
        buf.write("\3\2\2\2\u0130\u0131\7&\2\2\u0131\u0134\5\u0084C\2\u0132")
        buf.write("\u0134\5\6\4\2\u0133\u012c\3\2\2\2\u0133\u0130\3\2\2\2")
        buf.write("\u0133\u0132\3\2\2\2\u0134\u0135\3\2\2\2\u0135\u0136\7")
        buf.write("\66\2\2\u0136%\3\2\2\2\u0137\u0138\7\20\2\2\u0138\u0139")
        buf.write("\7\67\2\2\u0139\u013c\7&\2\2\u013a\u013d\5(\25\2\u013b")
        buf.write("\u013d\5\u0084C\2\u013c\u013a\3\2\2\2\u013c\u013b\3\2")
        buf.write("\2\2\u013d\u013e\3\2\2\2\u013e\u013f\7\66\2\2\u013f\'")
        buf.write("\3\2\2\2\u0140\u0141\t\5\2\2\u0141)\3\2\2\2\u0142\u0143")
        buf.write("\7\b\2\2\u0143\u0144\7\67\2\2\u0144\u0145\7/\2\2\u0145")
        buf.write("\u0146\5,\27\2\u0146\u0148\7\60\2\2\u0147\u0149\5\6\4")
        buf.write("\2\u0148\u0147\3\2\2\2\u0148\u0149\3\2\2\2\u0149\u014a")
        buf.write("\3\2\2\2\u014a\u014b\7\61\2\2\u014b\u014c\5\62\32\2\u014c")
        buf.write("\u014d\7\62\2\2\u014d\u014e\7\66\2\2\u014e+\3\2\2\2\u014f")
        buf.write("\u0152\5.\30\2\u0150\u0152\3\2\2\2\u0151\u014f\3\2\2\2")
        buf.write("\u0151\u0150\3\2\2\2\u0152-\3\2\2\2\u0153\u0154\5\60\31")
        buf.write("\2\u0154\u0155\7\65\2\2\u0155\u0156\5.\30\2\u0156\u0159")
        buf.write("\3\2\2\2\u0157\u0159\5\60\31\2\u0158\u0153\3\2\2\2\u0158")
        buf.write("\u0157\3\2\2\2\u0159/\3\2\2\2\u015a\u015b\7\67\2\2\u015b")
        buf.write("\u015c\5\6\4\2\u015c\61\3\2\2\2\u015d\u015e\5\u0098M\2")
        buf.write("\u015e\63\3\2\2\2\u015f\u0160\7\b\2\2\u0160\u0161\7/\2")
        buf.write("\2\u0161\u0162\7\67\2\2\u0162\u0163\7\67\2\2\u0163\u0164")
        buf.write("\7\60\2\2\u0164\u0165\7\67\2\2\u0165\u0166\7/\2\2\u0166")
        buf.write("\u0167\5,\27\2\u0167\u0169\7\60\2\2\u0168\u016a\5\6\4")
        buf.write("\2\u0169\u0168\3\2\2\2\u0169\u016a\3\2\2\2\u016a\u016b")
        buf.write("\3\2\2\2\u016b\u016c\7\61\2\2\u016c\u016d\5\62\32\2\u016d")
        buf.write("\u016e\7\62\2\2\u016e\u016f\7\66\2\2\u016f\65\3\2\2\2")
        buf.write("\u0170\u0171\5:\36\2\u0171\u0172\58\35\2\u0172\67\3\2")
        buf.write("\2\2\u0173\u0174\7\63\2\2\u0174\u0175\5\u0084C\2\u0175")
        buf.write("\u0176\7\64\2\2\u0176\u0177\58\35\2\u0177\u017d\3\2\2")
        buf.write("\2\u0178\u0179\7\63\2\2\u0179\u017a\5\u0084C\2\u017a\u017b")
        buf.write("\7\64\2\2\u017b\u017d\3\2\2\2\u017c\u0173\3\2\2\2\u017c")
        buf.write("\u0178\3\2\2\2\u017d9\3\2\2\2\u017e\u017f\b\36\1\2\u017f")
        buf.write("\u0180\5<\37\2\u0180\u0186\3\2\2\2\u0181\u0182\f\4\2\2")
        buf.write("\u0182\u0183\7$\2\2\u0183\u0185\5<\37\2\u0184\u0181\3")
        buf.write("\2\2\2\u0185\u0188\3\2\2\2\u0186\u0184\3\2\2\2\u0186\u0187")
        buf.write("\3\2\2\2\u0187;\3\2\2\2\u0188\u0186\3\2\2\2\u0189\u018a")
        buf.write("\b\37\1\2\u018a\u018b\5> \2\u018b\u0191\3\2\2\2\u018c")
        buf.write("\u018d\f\4\2\2\u018d\u018e\7#\2\2\u018e\u0190\5> \2\u018f")
        buf.write("\u018c\3\2\2\2\u0190\u0193\3\2\2\2\u0191\u018f\3\2\2\2")
        buf.write("\u0191\u0192\3\2\2\2\u0192=\3\2\2\2\u0193\u0191\3\2\2")
        buf.write("\2\u0194\u0195\b \1\2\u0195\u0196\5@!\2\u0196\u019c\3")
        buf.write("\2\2\2\u0197\u0198\f\4\2\2\u0198\u0199\t\6\2\2\u0199\u019b")
        buf.write("\5@!\2\u019a\u0197\3\2\2\2\u019b\u019e\3\2\2\2\u019c\u019a")
        buf.write("\3\2\2\2\u019c\u019d\3\2\2\2\u019d?\3\2\2\2\u019e\u019c")
        buf.write("\3\2\2\2\u019f\u01a0\b!\1\2\u01a0\u01a1\5B\"\2\u01a1\u01a7")
        buf.write("\3\2\2\2\u01a2\u01a3\f\4\2\2\u01a3\u01a4\t\7\2\2\u01a4")
        buf.write("\u01a6\5B\"\2\u01a5\u01a2\3\2\2\2\u01a6\u01a9\3\2\2\2")
        buf.write("\u01a7\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8A\3\2\2")
        buf.write("\2\u01a9\u01a7\3\2\2\2\u01aa\u01ab\b\"\1\2\u01ab\u01ac")
        buf.write("\5D#\2\u01ac\u01b2\3\2\2\2\u01ad\u01ae\f\4\2\2\u01ae\u01af")
        buf.write("\t\b\2\2\u01af\u01b1\5D#\2\u01b0\u01ad\3\2\2\2\u01b1\u01b4")
        buf.write("\3\2\2\2\u01b2\u01b0\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3")
        buf.write("C\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b5\u01b6\t\t\2\2\u01b6")
        buf.write("\u01b9\5D#\2\u01b7\u01b9\5F$\2\u01b8\u01b5\3\2\2\2\u01b8")
        buf.write("\u01b7\3\2\2\2\u01b9E\3\2\2\2\u01ba\u01bb\7/\2\2\u01bb")
        buf.write("\u01bc\5:\36\2\u01bc\u01bd\7\60\2\2\u01bd\u01c0\3\2\2")
        buf.write("\2\u01be\u01c0\5H%\2\u01bf\u01ba\3\2\2\2\u01bf\u01be\3")
        buf.write("\2\2\2\u01c0G\3\2\2\2\u01c1\u01c5\7\67\2\2\u01c2\u01c5")
        buf.write("\5\u0094K\2\u01c3\u01c5\5n8\2\u01c4\u01c1\3\2\2\2\u01c4")
        buf.write("\u01c2\3\2\2\2\u01c4\u01c3\3\2\2\2\u01c5I\3\2\2\2\u01c6")
        buf.write("\u01c7\5L\'\2\u01c7\u01c8\7-\2\2\u01c8\u01c9\7\67\2\2")
        buf.write("\u01c9K\3\2\2\2\u01ca\u01cb\b\'\1\2\u01cb\u01cc\5N(\2")
        buf.write("\u01cc\u01d2\3\2\2\2\u01cd\u01ce\f\4\2\2\u01ce\u01cf\7")
        buf.write("-\2\2\u01cf\u01d1\5N(\2\u01d0\u01cd\3\2\2\2\u01d1\u01d4")
        buf.write("\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d2\u01d3\3\2\2\2\u01d3")
        buf.write("M\3\2\2\2\u01d4\u01d2\3\2\2\2\u01d5\u01d6\b(\1\2\u01d6")
        buf.write("\u01d7\5P)\2\u01d7\u01dd\3\2\2\2\u01d8\u01d9\f\4\2\2\u01d9")
        buf.write("\u01da\7$\2\2\u01da\u01dc\5P)\2\u01db\u01d8\3\2\2\2\u01dc")
        buf.write("\u01df\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd\u01de\3\2\2\2")
        buf.write("\u01deO\3\2\2\2\u01df\u01dd\3\2\2\2\u01e0\u01e1\b)\1\2")
        buf.write("\u01e1\u01e2\5R*\2\u01e2\u01e8\3\2\2\2\u01e3\u01e4\f\4")
        buf.write("\2\2\u01e4\u01e5\7#\2\2\u01e5\u01e7\5R*\2\u01e6\u01e3")
        buf.write("\3\2\2\2\u01e7\u01ea\3\2\2\2\u01e8\u01e6\3\2\2\2\u01e8")
        buf.write("\u01e9\3\2\2\2\u01e9Q\3\2\2\2\u01ea\u01e8\3\2\2\2\u01eb")
        buf.write("\u01ec\b*\1\2\u01ec\u01ed\5T+\2\u01ed\u01f3\3\2\2\2\u01ee")
        buf.write("\u01ef\f\4\2\2\u01ef\u01f0\t\6\2\2\u01f0\u01f2\5T+\2\u01f1")
        buf.write("\u01ee\3\2\2\2\u01f2\u01f5\3\2\2\2\u01f3\u01f1\3\2\2\2")
        buf.write("\u01f3\u01f4\3\2\2\2\u01f4S\3\2\2\2\u01f5\u01f3\3\2\2")
        buf.write("\2\u01f6\u01f7\b+\1\2\u01f7\u01f8\5V,\2\u01f8\u01fe\3")
        buf.write("\2\2\2\u01f9\u01fa\f\4\2\2\u01fa\u01fb\t\7\2\2\u01fb\u01fd")
        buf.write("\5V,\2\u01fc\u01f9\3\2\2\2\u01fd\u0200\3\2\2\2\u01fe\u01fc")
        buf.write("\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ffU\3\2\2\2\u0200\u01fe")
        buf.write("\3\2\2\2\u0201\u0202\b,\1\2\u0202\u0203\5X-\2\u0203\u0209")
        buf.write("\3\2\2\2\u0204\u0205\f\4\2\2\u0205\u0206\t\b\2\2\u0206")
        buf.write("\u0208\5X-\2\u0207\u0204\3\2\2\2\u0208\u020b\3\2\2\2\u0209")
        buf.write("\u0207\3\2\2\2\u0209\u020a\3\2\2\2\u020aW\3\2\2\2\u020b")
        buf.write("\u0209\3\2\2\2\u020c\u020d\t\t\2\2\u020d\u0210\5X-\2\u020e")
        buf.write("\u0210\5Z.\2\u020f\u020c\3\2\2\2\u020f\u020e\3\2\2\2\u0210")
        buf.write("Y\3\2\2\2\u0211\u0212\7/\2\2\u0212\u0213\5N(\2\u0213\u0214")
        buf.write("\7\60\2\2\u0214\u0217\3\2\2\2\u0215\u0217\5\\/\2\u0216")
        buf.write("\u0211\3\2\2\2\u0216\u0215\3\2\2\2\u0217[\3\2\2\2\u0218")
        buf.write("\u021b\7\67\2\2\u0219\u021b\5\66\34\2\u021a\u0218\3\2")
        buf.write("\2\2\u021a\u0219\3\2\2\2\u021b]\3\2\2\2\u021c\u021d\5")
        buf.write("\b\5\2\u021d\u021e\5`\61\2\u021e_\3\2\2\2\u021f\u0220")
        buf.write("\7\61\2\2\u0220\u0221\5b\62\2\u0221\u0222\7\62\2\2\u0222")
        buf.write("a\3\2\2\2\u0223\u0224\5d\63\2\u0224\u0225\7\65\2\2\u0225")
        buf.write("\u0226\5b\62\2\u0226\u0229\3\2\2\2\u0227\u0229\5d\63\2")
        buf.write("\u0228\u0223\3\2\2\2\u0228\u0227\3\2\2\2\u0229c\3\2\2")
        buf.write("\2\u022a\u022d\5\u0084C\2\u022b\u022d\5`\61\2\u022c\u022a")
        buf.write("\3\2\2\2\u022c\u022b\3\2\2\2\u022de\3\2\2\2\u022e\u022f")
        buf.write("\7\67\2\2\u022f\u0230\7\61\2\2\u0230\u0231\5h\65\2\u0231")
        buf.write("\u0232\7\62\2\2\u0232g\3\2\2\2\u0233\u0236\5j\66\2\u0234")
        buf.write("\u0236\3\2\2\2\u0235\u0233\3\2\2\2\u0235\u0234\3\2\2\2")
        buf.write("\u0236i\3\2\2\2\u0237\u0238\5l\67\2\u0238\u0239\7\65\2")
        buf.write("\2\u0239\u023a\5j\66\2\u023a\u023d\3\2\2\2\u023b\u023d")
        buf.write("\5l\67\2\u023c\u0237\3\2\2\2\u023c\u023b\3\2\2\2\u023d")
        buf.write("k\3\2\2\2\u023e\u023f\7\67\2\2\u023f\u0240\7.\2\2\u0240")
        buf.write("\u0241\5\u0084C\2\u0241m\3\2\2\2\u0242\u0243\7\67\2\2")
        buf.write("\u0243\u0244\7/\2\2\u0244\u0245\5p9\2\u0245\u0246\7\60")
        buf.write("\2\2\u0246o\3\2\2\2\u0247\u024a\5b\62\2\u0248\u024a\3")
        buf.write("\2\2\2\u0249\u0247\3\2\2\2\u0249\u0248\3\2\2\2\u024aq")
        buf.write("\3\2\2\2\u024b\u024c\5t;\2\u024c\u024d\7-\2\2\u024d\u024e")
        buf.write("\7\67\2\2\u024e\u024f\7/\2\2\u024f\u0250\5p9\2\u0250\u0251")
        buf.write("\7\60\2\2\u0251s\3\2\2\2\u0252\u0253\b;\1\2\u0253\u0254")
        buf.write("\5v<\2\u0254\u025a\3\2\2\2\u0255\u0256\f\4\2\2\u0256\u0257")
        buf.write("\7$\2\2\u0257\u0259\5v<\2\u0258\u0255\3\2\2\2\u0259\u025c")
        buf.write("\3\2\2\2\u025a\u0258\3\2\2\2\u025a\u025b\3\2\2\2\u025b")
        buf.write("u\3\2\2\2\u025c\u025a\3\2\2\2\u025d\u025e\b<\1\2\u025e")
        buf.write("\u025f\5x=\2\u025f\u0265\3\2\2\2\u0260\u0261\f\4\2\2\u0261")
        buf.write("\u0262\7#\2\2\u0262\u0264\5x=\2\u0263\u0260\3\2\2\2\u0264")
        buf.write("\u0267\3\2\2\2\u0265\u0263\3\2\2\2\u0265\u0266\3\2\2\2")
        buf.write("\u0266w\3\2\2\2\u0267\u0265\3\2\2\2\u0268\u0269\b=\1\2")
        buf.write("\u0269\u026a\5z>\2\u026a\u0270\3\2\2\2\u026b\u026c\f\4")
        buf.write("\2\2\u026c\u026d\t\6\2\2\u026d\u026f\5z>\2\u026e\u026b")
        buf.write("\3\2\2\2\u026f\u0272\3\2\2\2\u0270\u026e\3\2\2\2\u0270")
        buf.write("\u0271\3\2\2\2\u0271y\3\2\2\2\u0272\u0270\3\2\2\2\u0273")
        buf.write("\u0274\b>\1\2\u0274\u0275\5|?\2\u0275\u027b\3\2\2\2\u0276")
        buf.write("\u0277\f\4\2\2\u0277\u0278\t\7\2\2\u0278\u027a\5|?\2\u0279")
        buf.write("\u0276\3\2\2\2\u027a\u027d\3\2\2\2\u027b\u0279\3\2\2\2")
        buf.write("\u027b\u027c\3\2\2\2\u027c{\3\2\2\2\u027d\u027b\3\2\2")
        buf.write("\2\u027e\u027f\b?\1\2\u027f\u0280\5~@\2\u0280\u0286\3")
        buf.write("\2\2\2\u0281\u0282\f\4\2\2\u0282\u0283\t\b\2\2\u0283\u0285")
        buf.write("\5~@\2\u0284\u0281\3\2\2\2\u0285\u0288\3\2\2\2\u0286\u0284")
        buf.write("\3\2\2\2\u0286\u0287\3\2\2\2\u0287}\3\2\2\2\u0288\u0286")
        buf.write("\3\2\2\2\u0289\u028a\t\t\2\2\u028a\u028d\5~@\2\u028b\u028d")
        buf.write("\5\u0080A\2\u028c\u0289\3\2\2\2\u028c\u028b\3\2\2\2\u028d")
        buf.write("\177\3\2\2\2\u028e\u028f\7/\2\2\u028f\u0290\5t;\2\u0290")
        buf.write("\u0291\7\60\2\2\u0291\u0294\3\2\2\2\u0292\u0294\5\u0082")
        buf.write("B\2\u0293\u028e\3\2\2\2\u0293\u0292\3\2\2\2\u0294\u0081")
        buf.write("\3\2\2\2\u0295\u029a\7\67\2\2\u0296\u029a\5\u0094K\2\u0297")
        buf.write("\u029a\5\66\34\2\u0298\u029a\5J&\2\u0299\u0295\3\2\2\2")
        buf.write("\u0299\u0296\3\2\2\2\u0299\u0297\3\2\2\2\u0299\u0298\3")
        buf.write("\2\2\2\u029a\u0083\3\2\2\2\u029b\u029c\bC\1\2\u029c\u029d")
        buf.write("\5\u0086D\2\u029d\u02a3\3\2\2\2\u029e\u029f\f\4\2\2\u029f")
        buf.write("\u02a0\7$\2\2\u02a0\u02a2\5\u0086D\2\u02a1\u029e\3\2\2")
        buf.write("\2\u02a2\u02a5\3\2\2\2\u02a3\u02a1\3\2\2\2\u02a3\u02a4")
        buf.write("\3\2\2\2\u02a4\u0085\3\2\2\2\u02a5\u02a3\3\2\2\2\u02a6")
        buf.write("\u02a7\bD\1\2\u02a7\u02a8\5\u0088E\2\u02a8\u02ae\3\2\2")
        buf.write("\2\u02a9\u02aa\f\4\2\2\u02aa\u02ab\7#\2\2\u02ab\u02ad")
        buf.write("\5\u0088E\2\u02ac\u02a9\3\2\2\2\u02ad\u02b0\3\2\2\2\u02ae")
        buf.write("\u02ac\3\2\2\2\u02ae\u02af\3\2\2\2\u02af\u0087\3\2\2\2")
        buf.write("\u02b0\u02ae\3\2\2\2\u02b1\u02b2\bE\1\2\u02b2\u02b3\5")
        buf.write("\u008aF\2\u02b3\u02b9\3\2\2\2\u02b4\u02b5\f\4\2\2\u02b5")
        buf.write("\u02b6\t\6\2\2\u02b6\u02b8\5\u008aF\2\u02b7\u02b4\3\2")
        buf.write("\2\2\u02b8\u02bb\3\2\2\2\u02b9\u02b7\3\2\2\2\u02b9\u02ba")
        buf.write("\3\2\2\2\u02ba\u0089\3\2\2\2\u02bb\u02b9\3\2\2\2\u02bc")
        buf.write("\u02bd\bF\1\2\u02bd\u02be\5\u008cG\2\u02be\u02c4\3\2\2")
        buf.write("\2\u02bf\u02c0\f\4\2\2\u02c0\u02c1\t\7\2\2\u02c1\u02c3")
        buf.write("\5\u008cG\2\u02c2\u02bf\3\2\2\2\u02c3\u02c6\3\2\2\2\u02c4")
        buf.write("\u02c2\3\2\2\2\u02c4\u02c5\3\2\2\2\u02c5\u008b\3\2\2\2")
        buf.write("\u02c6\u02c4\3\2\2\2\u02c7\u02c8\bG\1\2\u02c8\u02c9\5")
        buf.write("\u008eH\2\u02c9\u02cf\3\2\2\2\u02ca\u02cb\f\4\2\2\u02cb")
        buf.write("\u02cc\t\b\2\2\u02cc\u02ce\5\u008eH\2\u02cd\u02ca\3\2")
        buf.write("\2\2\u02ce\u02d1\3\2\2\2\u02cf\u02cd\3\2\2\2\u02cf\u02d0")
        buf.write("\3\2\2\2\u02d0\u008d\3\2\2\2\u02d1\u02cf\3\2\2\2\u02d2")
        buf.write("\u02d3\t\t\2\2\u02d3\u02d6\5\u008eH\2\u02d4\u02d6\5\u0090")
        buf.write("I\2\u02d5\u02d2\3\2\2\2\u02d5\u02d4\3\2\2\2\u02d6\u008f")
        buf.write("\3\2\2\2\u02d7\u02d8\7/\2\2\u02d8\u02d9\5\u0084C\2\u02d9")
        buf.write("\u02da\7\60\2\2\u02da\u02dd\3\2\2\2\u02db\u02dd\5\u0092")
        buf.write("J\2\u02dc\u02d7\3\2\2\2\u02dc\u02db\3\2\2\2\u02dd\u0091")
        buf.write("\3\2\2\2\u02de\u02e5\7\67\2\2\u02df\u02e5\5\u0094K\2\u02e0")
        buf.write("\u02e5\5n8\2\u02e1\u02e5\5r:\2\u02e2\u02e5\5\66\34\2\u02e3")
        buf.write("\u02e5\5J&\2\u02e4\u02de\3\2\2\2\u02e4\u02df\3\2\2\2\u02e4")
        buf.write("\u02e0\3\2\2\2\u02e4\u02e1\3\2\2\2\u02e4\u02e2\3\2\2\2")
        buf.write("\u02e4\u02e3\3\2\2\2\u02e5\u0093\3\2\2\2\u02e6\u02ea\5")
        buf.write("(\25\2\u02e7\u02ea\5^\60\2\u02e8\u02ea\5f\64\2\u02e9\u02e6")
        buf.write("\3\2\2\2\u02e9\u02e7\3\2\2\2\u02e9\u02e8\3\2\2\2\u02ea")
        buf.write("\u0095\3\2\2\2\u02eb\u02f5\5\u009cO\2\u02ec\u02f5\5\u009e")
        buf.write("P\2\u02ed\u02f5\5\u00a0Q\2\u02ee\u02f5\5\u00a8U\2\u02ef")
        buf.write("\u02f5\5\u00aeX\2\u02f0\u02f5\5\u00be`\2\u02f1\u02f5\5")
        buf.write("\u00c0a\2\u02f2\u02f5\5\u00c2b\2\u02f3\u02f5\5\u00c4c")
        buf.write("\2\u02f4\u02eb\3\2\2\2\u02f4\u02ec\3\2\2\2\u02f4\u02ed")
        buf.write("\3\2\2\2\u02f4\u02ee\3\2\2\2\u02f4\u02ef\3\2\2\2\u02f4")
        buf.write("\u02f0\3\2\2\2\u02f4\u02f1\3\2\2\2\u02f4\u02f2\3\2\2\2")
        buf.write("\u02f4\u02f3\3\2\2\2\u02f5\u02f6\3\2\2\2\u02f6\u02f7\t")
        buf.write("\4\2\2\u02f7\u0097\3\2\2\2\u02f8\u02fb\5\u009aN\2\u02f9")
        buf.write("\u02fb\3\2\2\2\u02fa\u02f8\3\2\2\2\u02fa\u02f9\3\2\2\2")
        buf.write("\u02fb\u0099\3\2\2\2\u02fc\u02fd\5\u0096L\2\u02fd\u02fe")
        buf.write("\5\u009aN\2\u02fe\u0301\3\2\2\2\u02ff\u0301\5\u0096L\2")
        buf.write("\u0300\u02fc\3\2\2\2\u0300\u02ff\3\2\2\2\u0301\u009b\3")
        buf.write("\2\2\2\u0302\u0303\7\21\2\2\u0303\u030b\7\67\2\2\u0304")
        buf.write("\u0305\5\6\4\2\u0305\u0306\7&\2\2\u0306\u0307\5\u0084")
        buf.write("C\2\u0307\u030c\3\2\2\2\u0308\u0309\7&\2\2\u0309\u030c")
        buf.write("\5\u0084C\2\u030a\u030c\5\6\4\2\u030b\u0304\3\2\2\2\u030b")
        buf.write("\u0308\3\2\2\2\u030b\u030a\3\2\2\2\u030c\u009d\3\2\2\2")
        buf.write("\u030d\u030e\7\20\2\2\u030e\u030f\7\67\2\2\u030f\u0312")
        buf.write("\7&\2\2\u0310\u0313\5(\25\2\u0311\u0313\5\u0084C\2\u0312")
        buf.write("\u0310\3\2\2\2\u0312\u0311\3\2\2\2\u0313\u009f\3\2\2\2")
        buf.write("\u0314\u0315\5\u00a2R\2\u0315\u0316\5\u00a4S\2\u0316\u0317")
        buf.write("\5\u00a6T\2\u0317\u00a1\3\2\2\2\u0318\u031c\7\67\2\2\u0319")
        buf.write("\u031c\5\66\34\2\u031a\u031c\5J&\2\u031b\u0318\3\2\2\2")
        buf.write("\u031b\u0319\3\2\2\2\u031b\u031a\3\2\2\2\u031c\u00a3\3")
        buf.write("\2\2\2\u031d\u031e\t\n\2\2\u031e\u00a5\3\2\2\2\u031f\u0320")
        buf.write("\5\u0084C\2\u0320\u00a7\3\2\2\2\u0321\u0322\7\4\2\2\u0322")
        buf.write("\u0323\7/\2\2\u0323\u0324\5\u0084C\2\u0324\u0325\7\60")
        buf.write("\2\2\u0325\u0326\7\61\2\2\u0326\u0327\5\u0098M\2\u0327")
        buf.write("\u0328\7\62\2\2\u0328\u032e\5\u00aaV\2\u0329\u032a\7\5")
        buf.write("\2\2\u032a\u032b\7\61\2\2\u032b\u032c\5\u0098M\2\u032c")
        buf.write("\u032d\7\62\2\2\u032d\u032f\3\2\2\2\u032e\u0329\3\2\2")
        buf.write("\2\u032e\u032f\3\2\2\2\u032f\u00a9\3\2\2\2\u0330\u0331")
        buf.write("\5\u00acW\2\u0331\u0332\5\u00aaV\2\u0332\u0335\3\2\2\2")
        buf.write("\u0333\u0335\3\2\2\2\u0334\u0330\3\2\2\2\u0334\u0333\3")
        buf.write("\2\2\2\u0335\u00ab\3\2\2\2\u0336\u0337\7\5\2\2\u0337\u0338")
        buf.write("\7\4\2\2\u0338\u0339\7/\2\2\u0339\u033a\5\u0084C\2\u033a")
        buf.write("\u033b\7\60\2\2\u033b\u033c\7\61\2\2\u033c\u033d\5\u0098")
        buf.write("M\2\u033d\u033e\7\62\2\2\u033e\u00ad\3\2\2\2\u033f\u0343")
        buf.write("\5\u00b0Y\2\u0340\u0343\5\u00b2Z\2\u0341\u0343\5\u00bc")
        buf.write("_\2\u0342\u033f\3\2\2\2\u0342\u0340\3\2\2\2\u0342\u0341")
        buf.write("\3\2\2\2\u0343\u00af\3\2\2\2\u0344\u0345\7\6\2\2\u0345")
        buf.write("\u0346\5\u0084C\2\u0346\u0347\7\61\2\2\u0347\u0348\5\u0098")
        buf.write("M\2\u0348\u0349\7\62\2\2\u0349\u00b1\3\2\2\2\u034a\u034b")
        buf.write("\7\6\2\2\u034b\u034c\5\u00b4[\2\u034c\u034d\7\66\2\2\u034d")
        buf.write("\u034e\5\u00b8]\2\u034e\u034f\7\66\2\2\u034f\u0350\5\u00ba")
        buf.write("^\2\u0350\u0351\7\61\2\2\u0351\u0352\5\u0098M\2\u0352")
        buf.write("\u0353\7\62\2\2\u0353\u00b3\3\2\2\2\u0354\u0357\5\u00a0")
        buf.write("Q\2\u0355\u0357\5\u00b6\\\2\u0356\u0354\3\2\2\2\u0356")
        buf.write("\u0355\3\2\2\2\u0357\u00b5\3\2\2\2\u0358\u0359\7\21\2")
        buf.write("\2\u0359\u035b\7\67\2\2\u035a\u035c\5\6\4\2\u035b\u035a")
        buf.write("\3\2\2\2\u035b\u035c\3\2\2\2\u035c\u035d\3\2\2\2\u035d")
        buf.write("\u035e\7&\2\2\u035e\u035f\5\u0084C\2\u035f\u00b7\3\2\2")
        buf.write("\2\u0360\u0361\5\u0084C\2\u0361\u00b9\3\2\2\2\u0362\u0363")
        buf.write("\5\u00a0Q\2\u0363\u00bb\3\2\2\2\u0364\u0365\7\6\2\2\u0365")
        buf.write("\u0366\t\13\2\2\u0366\u0367\7\65\2\2\u0367\u0368\7\67")
        buf.write("\2\2\u0368\u0369\7\'\2\2\u0369\u036a\7\24\2\2\u036a\u036b")
        buf.write("\7\67\2\2\u036b\u036c\7\61\2\2\u036c\u036d\5\u0098M\2")
        buf.write("\u036d\u036e\7\62\2\2\u036e\u00bd\3\2\2\2\u036f\u0370")
        buf.write("\7\23\2\2\u0370\u00bf\3\2\2\2\u0371\u0372\7\22\2\2\u0372")
        buf.write("\u00c1\3\2\2\2\u0373\u0376\5n8\2\u0374\u0376\5r:\2\u0375")
        buf.write("\u0373\3\2\2\2\u0375\u0374\3\2\2\2\u0376\u00c3\3\2\2\2")
        buf.write("\u0377\u0378\7\7\2\2\u0378\u0379\5\u0084C\2\u0379\u00c5")
        buf.write("\3\2\2\2F\u00c9\u00d3\u00db\u00e7\u00f7\u010b\u0112\u0118")
        buf.write("\u011f\u0128\u0133\u013c\u0148\u0151\u0158\u0169\u017c")
        buf.write("\u0186\u0191\u019c\u01a7\u01b2\u01b8\u01bf\u01c4\u01d2")
        buf.write("\u01dd\u01e8\u01f3\u01fe\u0209\u020f\u0216\u021a\u0228")
        buf.write("\u022c\u0235\u023c\u0249\u025a\u0265\u0270\u027b\u0286")
        buf.write("\u028c\u0293\u0299\u02a3\u02ae\u02b9\u02c4\u02cf\u02d5")
        buf.write("\u02dc\u02e4\u02e9\u02f4\u02fa\u0300\u030b\u0312\u031b")
        buf.write("\u032e\u0334\u0342\u0356\u035b\u0375")
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
    RULE_paramListFunc = 21
    RULE_paramPrimeFunc = 22
    RULE_paramFunc = 23
    RULE_funcBody = 24
    RULE_methodStructDecl = 25
    RULE_arrAccess = 26
    RULE_positionList = 27
    RULE_exprA = 28
    RULE_exprA1 = 29
    RULE_exprA2 = 30
    RULE_exprA3 = 31
    RULE_exprA4 = 32
    RULE_exprA5 = 33
    RULE_exprA6 = 34
    RULE_operandA = 35
    RULE_structAccess = 36
    RULE_refList = 37
    RULE_exprS = 38
    RULE_exprS1 = 39
    RULE_exprS2 = 40
    RULE_exprS3 = 41
    RULE_exprS4 = 42
    RULE_exprS5 = 43
    RULE_exprS6 = 44
    RULE_operandS = 45
    RULE_arrLit = 46
    RULE_arrBody = 47
    RULE_elementList = 48
    RULE_element = 49
    RULE_structLit = 50
    RULE_structElList = 51
    RULE_structELPrime = 52
    RULE_structEL = 53
    RULE_funcCall = 54
    RULE_argumentList = 55
    RULE_methodCall = 56
    RULE_exprM = 57
    RULE_exprM1 = 58
    RULE_exprM2 = 59
    RULE_exprM3 = 60
    RULE_exprM4 = 61
    RULE_exprM5 = 62
    RULE_exprM6 = 63
    RULE_operandM = 64
    RULE_expr = 65
    RULE_expr1 = 66
    RULE_expr2 = 67
    RULE_expr3 = 68
    RULE_expr4 = 69
    RULE_expr5 = 70
    RULE_expr6 = 71
    RULE_operand = 72
    RULE_literal = 73
    RULE_statement = 74
    RULE_statementList = 75
    RULE_statementListPrime = 76
    RULE_varDeclStatement = 77
    RULE_constDeclStatement = 78
    RULE_assignment = 79
    RULE_lhs = 80
    RULE_assignOperator = 81
    RULE_rhs = 82
    RULE_ifStatement = 83
    RULE_elifList = 84
    RULE_eliff = 85
    RULE_forStatement = 86
    RULE_forBasic = 87
    RULE_forInitial = 88
    RULE_initialization = 89
    RULE_varDeclInitial = 90
    RULE_condition = 91
    RULE_update = 92
    RULE_forRange = 93
    RULE_breakStatement = 94
    RULE_continueStatement = 95
    RULE_callStatement = 96
    RULE_returnStatement = 97

    ruleNames =  [ "program", "decl", "typee", "arrType", "dimenList", "structDecl", 
                   "structBody", "listField", "field", "interfaceDecl", 
                   "interfaceBody", "listMethod", "method", "paramList", 
                   "paramPrime", "param", "nameList", "varDecl", "constDecl", 
                   "literalConst", "funcDecl", "paramListFunc", "paramPrimeFunc", 
                   "paramFunc", "funcBody", "methodStructDecl", "arrAccess", 
                   "positionList", "exprA", "exprA1", "exprA2", "exprA3", 
                   "exprA4", "exprA5", "exprA6", "operandA", "structAccess", 
                   "refList", "exprS", "exprS1", "exprS2", "exprS3", "exprS4", 
                   "exprS5", "exprS6", "operandS", "arrLit", "arrBody", 
                   "elementList", "element", "structLit", "structElList", 
                   "structELPrime", "structEL", "funcCall", "argumentList", 
                   "methodCall", "exprM", "exprM1", "exprM2", "exprM3", 
                   "exprM4", "exprM5", "exprM6", "operandM", "expr", "expr1", 
                   "expr2", "expr3", "expr4", "expr5", "expr6", "operand", 
                   "literal", "statement", "statementList", "statementListPrime", 
                   "varDeclStatement", "constDeclStatement", "assignment", 
                   "lhs", "assignOperator", "rhs", "ifStatement", "elifList", 
                   "eliff", "forStatement", "forBasic", "forInitial", "initialization", 
                   "varDeclInitial", "condition", "update", "forRange", 
                   "breakStatement", "continueStatement", "callStatement", 
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
            self.state = 197 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 196
                self.decl()
                self.state = 199 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.FUNC) | (1 << MiniGoParser.TYPE) | (1 << MiniGoParser.CONST) | (1 << MiniGoParser.VAR))) != 0)):
                    break

            self.state = 201
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
            self.state = 209
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 203
                self.structDecl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.interfaceDecl()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 205
                self.varDecl()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 206
                self.constDecl()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 207
                self.funcDecl()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 208
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
            self.state = 217
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.INT]:
                self.state = 211
                self.match(MiniGoParser.INT)
                pass
            elif token in [MiniGoParser.FLOAT]:
                self.state = 212
                self.match(MiniGoParser.FLOAT)
                pass
            elif token in [MiniGoParser.BOOLEAN]:
                self.state = 213
                self.match(MiniGoParser.BOOLEAN)
                pass
            elif token in [MiniGoParser.STRING]:
                self.state = 214
                self.match(MiniGoParser.STRING)
                pass
            elif token in [MiniGoParser.OPEN_SQUARE]:
                self.state = 215
                self.arrType()
                pass
            elif token in [MiniGoParser.ID]:
                self.state = 216
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
            self.state = 219
            self.dimenList()
            self.state = 220
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
            self.state = 229
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.match(MiniGoParser.OPEN_SQUARE)
                self.state = 223
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.ID or _la==MiniGoParser.INT_LIT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 224
                self.match(MiniGoParser.CLOSE_SQUARE)
                self.state = 225
                self.dimenList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.match(MiniGoParser.OPEN_SQUARE)
                self.state = 227
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.ID or _la==MiniGoParser.INT_LIT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 228
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

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 231
            self.match(MiniGoParser.TYPE)
            self.state = 232
            self.match(MiniGoParser.ID)
            self.state = 233
            self.match(MiniGoParser.STRUCT)
            self.state = 234
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 235
            self.structBody()
            self.state = 236
            self.match(MiniGoParser.CLOSE_CURVE)
            self.state = 237
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NL):
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
            self.state = 239
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
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.field()
                self.state = 242
                self.listField()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
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

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.match(MiniGoParser.ID)
            self.state = 248
            self.typee()
            self.state = 249
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NL):
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

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 251
            self.match(MiniGoParser.TYPE)
            self.state = 252
            self.match(MiniGoParser.ID)
            self.state = 253
            self.match(MiniGoParser.INTERFACE)
            self.state = 254
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 255
            self.interfaceBody()
            self.state = 256
            self.match(MiniGoParser.CLOSE_CURVE)
            self.state = 257
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NL):
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
            self.state = 259
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
            self.state = 265
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 261
                self.method()
                self.state = 262
                self.listMethod()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 264
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

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

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
            self.state = 267
            self.match(MiniGoParser.ID)
            self.state = 268
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 269
            self.paramList()
            self.state = 270
            self.match(MiniGoParser.CLOSE_ROUND)
            self.state = 272
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.OPEN_SQUARE) | (1 << MiniGoParser.ID))) != 0):
                self.state = 271
                self.typee()


            self.state = 274
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NL):
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
            self.state = 278
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 276
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
            self.state = 285
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.param()
                self.state = 281
                self.match(MiniGoParser.COMMA)
                self.state = 282
                self.paramPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 284
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
            self.state = 287
            self.nameList()
            self.state = 288
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
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 290
                self.match(MiniGoParser.ID)
                self.state = 291
                self.match(MiniGoParser.COMMA)
                self.state = 292
                self.nameList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 293
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
            self.state = 296
            self.match(MiniGoParser.VAR)
            self.state = 297
            self.match(MiniGoParser.ID)
            self.state = 305
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 298
                self.typee()
                self.state = 299
                self.match(MiniGoParser.ASSIGN)
                self.state = 300
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 302
                self.match(MiniGoParser.ASSIGN)
                self.state = 303
                self.expr(0)
                pass

            elif la_ == 3:
                self.state = 304
                self.typee()
                pass


            self.state = 307
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
            self.state = 309
            self.match(MiniGoParser.CONST)
            self.state = 310
            self.match(MiniGoParser.ID)
            self.state = 311
            self.match(MiniGoParser.ASSIGN)
            self.state = 314
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 312
                self.literalConst()
                pass

            elif la_ == 2:
                self.state = 313
                self.expr(0)
                pass


            self.state = 316
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
            self.state = 318
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

        def paramListFunc(self):
            return self.getTypedRuleContext(MiniGoParser.ParamListFuncContext,0)


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
            self.state = 320
            self.match(MiniGoParser.FUNC)
            self.state = 321
            self.match(MiniGoParser.ID)
            self.state = 322
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 323
            self.paramListFunc()
            self.state = 324
            self.match(MiniGoParser.CLOSE_ROUND)
            self.state = 326
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.OPEN_SQUARE) | (1 << MiniGoParser.ID))) != 0):
                self.state = 325
                self.typee()


            self.state = 328
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 329
            self.funcBody()
            self.state = 330
            self.match(MiniGoParser.CLOSE_CURVE)
            self.state = 331
            self.match(MiniGoParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramPrimeFunc(self):
            return self.getTypedRuleContext(MiniGoParser.ParamPrimeFuncContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramListFunc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamListFunc" ):
                return visitor.visitParamListFunc(self)
            else:
                return visitor.visitChildren(self)




    def paramListFunc(self):

        localctx = MiniGoParser.ParamListFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_paramListFunc)
        try:
            self.state = 335
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 333
                self.paramPrimeFunc()
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


    class ParamPrimeFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def paramFunc(self):
            return self.getTypedRuleContext(MiniGoParser.ParamFuncContext,0)


        def COMMA(self):
            return self.getToken(MiniGoParser.COMMA, 0)

        def paramPrimeFunc(self):
            return self.getTypedRuleContext(MiniGoParser.ParamPrimeFuncContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramPrimeFunc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamPrimeFunc" ):
                return visitor.visitParamPrimeFunc(self)
            else:
                return visitor.visitChildren(self)




    def paramPrimeFunc(self):

        localctx = MiniGoParser.ParamPrimeFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_paramPrimeFunc)
        try:
            self.state = 342
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 337
                self.paramFunc()
                self.state = 338
                self.match(MiniGoParser.COMMA)
                self.state = 339
                self.paramPrimeFunc()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 341
                self.paramFunc()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamFuncContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(MiniGoParser.ID, 0)

        def typee(self):
            return self.getTypedRuleContext(MiniGoParser.TypeeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_paramFunc

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamFunc" ):
                return visitor.visitParamFunc(self)
            else:
                return visitor.visitChildren(self)




    def paramFunc(self):

        localctx = MiniGoParser.ParamFuncContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_paramFunc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 344
            self.match(MiniGoParser.ID)
            self.state = 345
            self.typee()
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
        self.enterRule(localctx, 48, self.RULE_funcBody)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 347
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

        def paramListFunc(self):
            return self.getTypedRuleContext(MiniGoParser.ParamListFuncContext,0)


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
        self.enterRule(localctx, 50, self.RULE_methodStructDecl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 349
            self.match(MiniGoParser.FUNC)
            self.state = 350
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 351
            self.match(MiniGoParser.ID)
            self.state = 352
            self.match(MiniGoParser.ID)
            self.state = 353
            self.match(MiniGoParser.CLOSE_ROUND)
            self.state = 354
            self.match(MiniGoParser.ID)
            self.state = 355
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 356
            self.paramListFunc()
            self.state = 357
            self.match(MiniGoParser.CLOSE_ROUND)
            self.state = 359
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.OPEN_SQUARE) | (1 << MiniGoParser.ID))) != 0):
                self.state = 358
                self.typee()


            self.state = 361
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 362
            self.funcBody()
            self.state = 363
            self.match(MiniGoParser.CLOSE_CURVE)
            self.state = 364
            self.match(MiniGoParser.SEMICOLON)
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
        self.enterRule(localctx, 52, self.RULE_arrAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 366
            self.exprA(0)
            self.state = 367
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
        self.enterRule(localctx, 54, self.RULE_positionList)
        try:
            self.state = 378
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.match(MiniGoParser.OPEN_SQUARE)
                self.state = 370
                self.expr(0)
                self.state = 371
                self.match(MiniGoParser.CLOSE_SQUARE)
                self.state = 372
                self.positionList()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 374
                self.match(MiniGoParser.OPEN_SQUARE)
                self.state = 375
                self.expr(0)
                self.state = 376
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
        _startState = 56
        self.enterRecursionRule(localctx, 56, self.RULE_exprA, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 381
            self.exprA1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 388
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprAContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprA)
                    self.state = 383
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 384
                    self.match(MiniGoParser.OR)
                    self.state = 385
                    self.exprA1(0) 
                self.state = 390
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
        _startState = 58
        self.enterRecursionRule(localctx, 58, self.RULE_exprA1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 392
            self.exprA2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 399
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprA1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprA1)
                    self.state = 394
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 395
                    self.match(MiniGoParser.AND)
                    self.state = 396
                    self.exprA2(0) 
                self.state = 401
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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
        _startState = 60
        self.enterRecursionRule(localctx, 60, self.RULE_exprA2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 403
            self.exprA3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 410
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprA2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprA2)
                    self.state = 405
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 406
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUAL) | (1 << MiniGoParser.NOT_EQUAL) | (1 << MiniGoParser.LESS_THAN) | (1 << MiniGoParser.LESS_EQUAL) | (1 << MiniGoParser.GREATER_THAN) | (1 << MiniGoParser.GREATER_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 407
                    self.exprA3(0) 
                self.state = 412
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

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
        _startState = 62
        self.enterRecursionRule(localctx, 62, self.RULE_exprA3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 414
            self.exprA4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 421
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprA3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprA3)
                    self.state = 416
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 417
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 418
                    self.exprA4(0) 
                self.state = 423
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
        _startState = 64
        self.enterRecursionRule(localctx, 64, self.RULE_exprA4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.exprA5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 432
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprA4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprA4)
                    self.state = 427
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 428
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MULTI) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 429
                    self.exprA5() 
                self.state = 434
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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
        self.enterRule(localctx, 66, self.RULE_exprA5)
        self._la = 0 # Token type
        try:
            self.state = 438
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.MINUS, MiniGoParser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.MINUS or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 436
                self.exprA5()
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.OPEN_ROUND, MiniGoParser.OPEN_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 437
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
        self.enterRule(localctx, 68, self.RULE_exprA6)
        try:
            self.state = 445
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.OPEN_ROUND]:
                self.enterOuterAlt(localctx, 1)
                self.state = 440
                self.match(MiniGoParser.OPEN_ROUND)
                self.state = 441
                self.exprA(0)
                self.state = 442
                self.match(MiniGoParser.CLOSE_ROUND)
                pass
            elif token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.OPEN_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 444
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
        self.enterRule(localctx, 70, self.RULE_operandA)
        try:
            self.state = 450
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 447
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 448
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 449
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
        self.enterRule(localctx, 72, self.RULE_structAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self.refList(0)
            self.state = 453
            self.match(MiniGoParser.DOT)
            self.state = 454
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
        _startState = 74
        self.enterRecursionRule(localctx, 74, self.RULE_refList, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 457
            self.exprS(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 464
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.RefListContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_refList)
                    self.state = 459
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 460
                    self.match(MiniGoParser.DOT)
                    self.state = 461
                    self.exprS(0) 
                self.state = 466
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
        _startState = 76
        self.enterRecursionRule(localctx, 76, self.RULE_exprS, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 468
            self.exprS1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 475
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprSContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprS)
                    self.state = 470
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 471
                    self.match(MiniGoParser.OR)
                    self.state = 472
                    self.exprS1(0) 
                self.state = 477
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

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
        _startState = 78
        self.enterRecursionRule(localctx, 78, self.RULE_exprS1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 479
            self.exprS2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 486
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprS1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprS1)
                    self.state = 481
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 482
                    self.match(MiniGoParser.AND)
                    self.state = 483
                    self.exprS2(0) 
                self.state = 488
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

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
        _startState = 80
        self.enterRecursionRule(localctx, 80, self.RULE_exprS2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 490
            self.exprS3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 497
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,28,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprS2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprS2)
                    self.state = 492
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 493
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUAL) | (1 << MiniGoParser.NOT_EQUAL) | (1 << MiniGoParser.LESS_THAN) | (1 << MiniGoParser.LESS_EQUAL) | (1 << MiniGoParser.GREATER_THAN) | (1 << MiniGoParser.GREATER_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 494
                    self.exprS3(0) 
                self.state = 499
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,28,self._ctx)

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
        _startState = 82
        self.enterRecursionRule(localctx, 82, self.RULE_exprS3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 501
            self.exprS4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 508
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,29,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprS3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprS3)
                    self.state = 503
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 504
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 505
                    self.exprS4(0) 
                self.state = 510
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,29,self._ctx)

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
        _startState = 84
        self.enterRecursionRule(localctx, 84, self.RULE_exprS4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 512
            self.exprS5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 519
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprS4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exprS4)
                    self.state = 514
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 515
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MULTI) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 516
                    self.exprS5() 
                self.state = 521
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

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
        self.enterRule(localctx, 86, self.RULE_exprS5)
        self._la = 0 # Token type
        try:
            self.state = 525
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 522
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.MINUS or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 523
                self.exprS5()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 524
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
        self.enterRule(localctx, 88, self.RULE_exprS6)
        try:
            self.state = 532
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 527
                self.match(MiniGoParser.OPEN_ROUND)
                self.state = 528
                self.exprS(0)
                self.state = 529
                self.match(MiniGoParser.CLOSE_ROUND)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 531
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
        self.enterRule(localctx, 90, self.RULE_operandS)
        try:
            self.state = 536
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 534
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 535
                self.arrAccess()
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
        self.enterRule(localctx, 92, self.RULE_arrLit)
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
        self.enterRule(localctx, 94, self.RULE_arrBody)
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
        self.enterRule(localctx, 96, self.RULE_elementList)
        try:
            self.state = 550
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
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
        self.enterRule(localctx, 98, self.RULE_element)
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
        self.enterRule(localctx, 100, self.RULE_structLit)
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
        self.enterRule(localctx, 102, self.RULE_structElList)
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
        self.enterRule(localctx, 104, self.RULE_structELPrime)
        try:
            self.state = 570
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
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
        self.enterRule(localctx, 106, self.RULE_structEL)
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
        self.enterRule(localctx, 108, self.RULE_funcCall)
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
        self.enterRule(localctx, 110, self.RULE_argumentList)
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
        self.enterRule(localctx, 112, self.RULE_methodCall)
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
        _startState = 114
        self.enterRecursionRule(localctx, 114, self.RULE_exprM, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 593
            self.exprM1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 600
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
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
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

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
        _startState = 116
        self.enterRecursionRule(localctx, 116, self.RULE_exprM1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 604
            self.exprM2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 611
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
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
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

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
        _startState = 118
        self.enterRecursionRule(localctx, 118, self.RULE_exprM2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 615
            self.exprM3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 622
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
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
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

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
        _startState = 120
        self.enterRecursionRule(localctx, 120, self.RULE_exprM3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 626
            self.exprM4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 633
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
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
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

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
        _startState = 122
        self.enterRecursionRule(localctx, 122, self.RULE_exprM4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 637
            self.exprM5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 644
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
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
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)

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
        self.enterRule(localctx, 124, self.RULE_exprM5)
        self._la = 0 # Token type
        try:
            self.state = 650
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
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
        self.enterRule(localctx, 126, self.RULE_exprM6)
        try:
            self.state = 657
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
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


        def arrAccess(self):
            return self.getTypedRuleContext(MiniGoParser.ArrAccessContext,0)


        def structAccess(self):
            return self.getTypedRuleContext(MiniGoParser.StructAccessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_operandM

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperandM" ):
                return visitor.visitOperandM(self)
            else:
                return visitor.visitChildren(self)




    def operandM(self):

        localctx = MiniGoParser.OperandMContext(self, self._ctx, self.state)
        self.enterRule(localctx, 128, self.RULE_operandM)
        try:
            self.state = 663
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
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
                self.arrAccess()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 662
                self.structAccess()
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
        _startState = 130
        self.enterRecursionRule(localctx, 130, self.RULE_expr, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 666
            self.expr1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 673
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,47,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.ExprContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                    self.state = 668
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 669
                    self.match(MiniGoParser.OR)
                    self.state = 670
                    self.expr1(0) 
                self.state = 675
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,47,self._ctx)

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
        _startState = 132
        self.enterRecursionRule(localctx, 132, self.RULE_expr1, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 677
            self.expr2(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 684
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,48,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr1)
                    self.state = 679
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 680
                    self.match(MiniGoParser.AND)
                    self.state = 681
                    self.expr2(0) 
                self.state = 686
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,48,self._ctx)

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
        _startState = 134
        self.enterRecursionRule(localctx, 134, self.RULE_expr2, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 688
            self.expr3(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 695
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,49,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr2Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr2)
                    self.state = 690
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 691
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.EQUAL) | (1 << MiniGoParser.NOT_EQUAL) | (1 << MiniGoParser.LESS_THAN) | (1 << MiniGoParser.LESS_EQUAL) | (1 << MiniGoParser.GREATER_THAN) | (1 << MiniGoParser.GREATER_EQUAL))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 692
                    self.expr3(0) 
                self.state = 697
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,49,self._ctx)

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
        _startState = 136
        self.enterRecursionRule(localctx, 136, self.RULE_expr3, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 699
            self.expr4(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 706
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,50,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr3Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr3)
                    self.state = 701
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 702
                    _la = self._input.LA(1)
                    if not(_la==MiniGoParser.PLUS or _la==MiniGoParser.MINUS):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 703
                    self.expr4(0) 
                self.state = 708
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,50,self._ctx)

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
        _startState = 138
        self.enterRecursionRule(localctx, 138, self.RULE_expr4, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 710
            self.expr5()
            self._ctx.stop = self._input.LT(-1)
            self.state = 717
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,51,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = MiniGoParser.Expr4Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expr4)
                    self.state = 712
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 713
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.MULTI) | (1 << MiniGoParser.DIV) | (1 << MiniGoParser.MODULO))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 714
                    self.expr5() 
                self.state = 719
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,51,self._ctx)

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
        self.enterRule(localctx, 140, self.RULE_expr5)
        self._la = 0 # Token type
        try:
            self.state = 723
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 720
                _la = self._input.LA(1)
                if not(_la==MiniGoParser.MINUS or _la==MiniGoParser.NOT):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 721
                self.expr5()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 722
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
        self.enterRule(localctx, 142, self.RULE_expr6)
        try:
            self.state = 730
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 725
                self.match(MiniGoParser.OPEN_ROUND)
                self.state = 726
                self.expr(0)
                self.state = 727
                self.match(MiniGoParser.CLOSE_ROUND)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 729
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

        def literal(self):
            return self.getTypedRuleContext(MiniGoParser.LiteralContext,0)


        def funcCall(self):
            return self.getTypedRuleContext(MiniGoParser.FuncCallContext,0)


        def methodCall(self):
            return self.getTypedRuleContext(MiniGoParser.MethodCallContext,0)


        def arrAccess(self):
            return self.getTypedRuleContext(MiniGoParser.ArrAccessContext,0)


        def structAccess(self):
            return self.getTypedRuleContext(MiniGoParser.StructAccessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_operand

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperand" ):
                return visitor.visitOperand(self)
            else:
                return visitor.visitChildren(self)




    def operand(self):

        localctx = MiniGoParser.OperandContext(self, self._ctx, self.state)
        self.enterRule(localctx, 144, self.RULE_operand)
        try:
            self.state = 738
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,54,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 732
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 733
                self.literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 734
                self.funcCall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 735
                self.methodCall()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 736
                self.arrAccess()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 737
                self.structAccess()
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
        self.enterRule(localctx, 146, self.RULE_literal)
        try:
            self.state = 743
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 740
                self.literalConst()
                pass
            elif token in [MiniGoParser.OPEN_SQUARE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 741
                self.arrLit()
                pass
            elif token in [MiniGoParser.ID]:
                self.enterOuterAlt(localctx, 3)
                self.state = 742
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

        def NL(self):
            return self.getToken(MiniGoParser.NL, 0)

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
        self.enterRule(localctx, 148, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 754
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,56,self._ctx)
            if la_ == 1:
                self.state = 745
                self.varDeclStatement()
                pass

            elif la_ == 2:
                self.state = 746
                self.constDeclStatement()
                pass

            elif la_ == 3:
                self.state = 747
                self.assignment()
                pass

            elif la_ == 4:
                self.state = 748
                self.ifStatement()
                pass

            elif la_ == 5:
                self.state = 749
                self.forStatement()
                pass

            elif la_ == 6:
                self.state = 750
                self.breakStatement()
                pass

            elif la_ == 7:
                self.state = 751
                self.continueStatement()
                pass

            elif la_ == 8:
                self.state = 752
                self.callStatement()
                pass

            elif la_ == 9:
                self.state = 753
                self.returnStatement()
                pass


            self.state = 756
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.SEMICOLON or _la==MiniGoParser.NL):
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


    class StatementListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statementListPrime(self):
            return self.getTypedRuleContext(MiniGoParser.StatementListPrimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statementList

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementList" ):
                return visitor.visitStatementList(self)
            else:
                return visitor.visitChildren(self)




    def statementList(self):

        localctx = MiniGoParser.StatementListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 150, self.RULE_statementList)
        try:
            self.state = 760
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.IF, MiniGoParser.FOR, MiniGoParser.RETURN, MiniGoParser.CONST, MiniGoParser.VAR, MiniGoParser.CONTINUE, MiniGoParser.BREAK, MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.MINUS, MiniGoParser.NOT, MiniGoParser.OPEN_ROUND, MiniGoParser.OPEN_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 758
                self.statementListPrime()
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


    class StatementListPrimeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(MiniGoParser.StatementContext,0)


        def statementListPrime(self):
            return self.getTypedRuleContext(MiniGoParser.StatementListPrimeContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_statementListPrime

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatementListPrime" ):
                return visitor.visitStatementListPrime(self)
            else:
                return visitor.visitChildren(self)




    def statementListPrime(self):

        localctx = MiniGoParser.StatementListPrimeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 152, self.RULE_statementListPrime)
        try:
            self.state = 766
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,58,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 762
                self.statement()
                self.state = 763
                self.statementListPrime()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 765
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
        self.enterRule(localctx, 154, self.RULE_varDeclStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 768
            self.match(MiniGoParser.VAR)
            self.state = 769
            self.match(MiniGoParser.ID)
            self.state = 777
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,59,self._ctx)
            if la_ == 1:
                self.state = 770
                self.typee()
                self.state = 771
                self.match(MiniGoParser.ASSIGN)
                self.state = 772
                self.expr(0)
                pass

            elif la_ == 2:
                self.state = 774
                self.match(MiniGoParser.ASSIGN)
                self.state = 775
                self.expr(0)
                pass

            elif la_ == 3:
                self.state = 776
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
        self.enterRule(localctx, 156, self.RULE_constDeclStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 779
            self.match(MiniGoParser.CONST)
            self.state = 780
            self.match(MiniGoParser.ID)
            self.state = 781
            self.match(MiniGoParser.ASSIGN)
            self.state = 784
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,60,self._ctx)
            if la_ == 1:
                self.state = 782
                self.literalConst()
                pass

            elif la_ == 2:
                self.state = 783
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
        self.enterRule(localctx, 158, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 786
            self.lhs()
            self.state = 787
            self.assignOperator()
            self.state = 788
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

        def arrAccess(self):
            return self.getTypedRuleContext(MiniGoParser.ArrAccessContext,0)


        def structAccess(self):
            return self.getTypedRuleContext(MiniGoParser.StructAccessContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = MiniGoParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 160, self.RULE_lhs)
        try:
            self.state = 793
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,61,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 790
                self.match(MiniGoParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 791
                self.arrAccess()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 792
                self.structAccess()
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
        self.enterRule(localctx, 162, self.RULE_assignOperator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 795
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
        self.enterRule(localctx, 164, self.RULE_rhs)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 797
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
        self.enterRule(localctx, 166, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 799
            self.match(MiniGoParser.IF)
            self.state = 800
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 801
            self.expr(0)
            self.state = 802
            self.match(MiniGoParser.CLOSE_ROUND)
            self.state = 803
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 804
            self.statementList()
            self.state = 805
            self.match(MiniGoParser.CLOSE_CURVE)
            self.state = 806
            self.elifList()
            self.state = 812
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==MiniGoParser.ELSE:
                self.state = 807
                self.match(MiniGoParser.ELSE)
                self.state = 808
                self.match(MiniGoParser.OPEN_CURVE)
                self.state = 809
                self.statementList()
                self.state = 810
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
        self.enterRule(localctx, 168, self.RULE_elifList)
        try:
            self.state = 818
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,63,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 814
                self.eliff()
                self.state = 815
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
        self.enterRule(localctx, 170, self.RULE_eliff)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 820
            self.match(MiniGoParser.ELSE)
            self.state = 821
            self.match(MiniGoParser.IF)
            self.state = 822
            self.match(MiniGoParser.OPEN_ROUND)
            self.state = 823
            self.expr(0)
            self.state = 824
            self.match(MiniGoParser.CLOSE_ROUND)
            self.state = 825
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 826
            self.statementList()
            self.state = 827
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
        self.enterRule(localctx, 172, self.RULE_forStatement)
        try:
            self.state = 832
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,64,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 829
                self.forBasic()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 830
                self.forInitial()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 831
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
        self.enterRule(localctx, 174, self.RULE_forBasic)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 834
            self.match(MiniGoParser.FOR)
            self.state = 835
            self.expr(0)
            self.state = 836
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 837
            self.statementList()
            self.state = 838
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
        self.enterRule(localctx, 176, self.RULE_forInitial)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 840
            self.match(MiniGoParser.FOR)
            self.state = 841
            self.initialization()
            self.state = 842
            self.match(MiniGoParser.SEMICOLON)
            self.state = 843
            self.condition()
            self.state = 844
            self.match(MiniGoParser.SEMICOLON)
            self.state = 845
            self.update()
            self.state = 846
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 847
            self.statementList()
            self.state = 848
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

        def assignment(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentContext,0)


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
        self.enterRule(localctx, 178, self.RULE_initialization)
        try:
            self.state = 852
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [MiniGoParser.NIL, MiniGoParser.TRUE, MiniGoParser.FALSE, MiniGoParser.MINUS, MiniGoParser.NOT, MiniGoParser.OPEN_ROUND, MiniGoParser.OPEN_SQUARE, MiniGoParser.ID, MiniGoParser.INT_LIT, MiniGoParser.FLOAT_LIT, MiniGoParser.STRING_LIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 850
                self.assignment()
                pass
            elif token in [MiniGoParser.VAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 851
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
        self.enterRule(localctx, 180, self.RULE_varDeclInitial)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 854
            self.match(MiniGoParser.VAR)
            self.state = 855
            self.match(MiniGoParser.ID)
            self.state = 857
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << MiniGoParser.STRING) | (1 << MiniGoParser.INT) | (1 << MiniGoParser.FLOAT) | (1 << MiniGoParser.BOOLEAN) | (1 << MiniGoParser.OPEN_SQUARE) | (1 << MiniGoParser.ID))) != 0):
                self.state = 856
                self.typee()


            self.state = 859
            self.match(MiniGoParser.ASSIGN)
            self.state = 860
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
        self.enterRule(localctx, 182, self.RULE_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 862
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

        def assignment(self):
            return self.getTypedRuleContext(MiniGoParser.AssignmentContext,0)


        def getRuleIndex(self):
            return MiniGoParser.RULE_update

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitUpdate" ):
                return visitor.visitUpdate(self)
            else:
                return visitor.visitChildren(self)




    def update(self):

        localctx = MiniGoParser.UpdateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 184, self.RULE_update)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 864
            self.assignment()
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
        self.enterRule(localctx, 186, self.RULE_forRange)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 866
            self.match(MiniGoParser.FOR)
            self.state = 867
            _la = self._input.LA(1)
            if not(_la==MiniGoParser.T__0 or _la==MiniGoParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 868
            self.match(MiniGoParser.COMMA)
            self.state = 869
            self.match(MiniGoParser.ID)
            self.state = 870
            self.match(MiniGoParser.ASSIGN1)
            self.state = 871
            self.match(MiniGoParser.RANGE)
            self.state = 872
            self.match(MiniGoParser.ID)
            self.state = 873
            self.match(MiniGoParser.OPEN_CURVE)
            self.state = 874
            self.statementList()
            self.state = 875
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
        self.enterRule(localctx, 188, self.RULE_breakStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 877
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
        self.enterRule(localctx, 190, self.RULE_continueStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 879
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
        self.enterRule(localctx, 192, self.RULE_callStatement)
        try:
            self.state = 883
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,67,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 881
                self.funcCall()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 882
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
        self.enterRule(localctx, 194, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 885
            self.match(MiniGoParser.RETURN)
            self.state = 886
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
        self._predicates[28] = self.exprA_sempred
        self._predicates[29] = self.exprA1_sempred
        self._predicates[30] = self.exprA2_sempred
        self._predicates[31] = self.exprA3_sempred
        self._predicates[32] = self.exprA4_sempred
        self._predicates[37] = self.refList_sempred
        self._predicates[38] = self.exprS_sempred
        self._predicates[39] = self.exprS1_sempred
        self._predicates[40] = self.exprS2_sempred
        self._predicates[41] = self.exprS3_sempred
        self._predicates[42] = self.exprS4_sempred
        self._predicates[57] = self.exprM_sempred
        self._predicates[58] = self.exprM1_sempred
        self._predicates[59] = self.exprM2_sempred
        self._predicates[60] = self.exprM3_sempred
        self._predicates[61] = self.exprM4_sempred
        self._predicates[65] = self.expr_sempred
        self._predicates[66] = self.expr1_sempred
        self._predicates[67] = self.expr2_sempred
        self._predicates[68] = self.expr3_sempred
        self._predicates[69] = self.expr4_sempred
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
         

    def exprM_sempred(self, localctx:ExprMContext, predIndex:int):
            if predIndex == 11:
                return self.precpred(self._ctx, 2)
         

    def exprM1_sempred(self, localctx:ExprM1Context, predIndex:int):
            if predIndex == 12:
                return self.precpred(self._ctx, 2)
         

    def exprM2_sempred(self, localctx:ExprM2Context, predIndex:int):
            if predIndex == 13:
                return self.precpred(self._ctx, 2)
         

    def exprM3_sempred(self, localctx:ExprM3Context, predIndex:int):
            if predIndex == 14:
                return self.precpred(self._ctx, 2)
         

    def exprM4_sempred(self, localctx:ExprM4Context, predIndex:int):
            if predIndex == 15:
                return self.precpred(self._ctx, 2)
         

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 16:
                return self.precpred(self._ctx, 2)
         

    def expr1_sempred(self, localctx:Expr1Context, predIndex:int):
            if predIndex == 17:
                return self.precpred(self._ctx, 2)
         

    def expr2_sempred(self, localctx:Expr2Context, predIndex:int):
            if predIndex == 18:
                return self.precpred(self._ctx, 2)
         

    def expr3_sempred(self, localctx:Expr3Context, predIndex:int):
            if predIndex == 19:
                return self.precpred(self._ctx, 2)
         

    def expr4_sempred(self, localctx:Expr4Context, predIndex:int):
            if predIndex == 20:
                return self.precpred(self._ctx, 2)
         




