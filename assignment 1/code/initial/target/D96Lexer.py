# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2B")
        buf.write("\u021b\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b")
        buf.write("\3\t\3\t\5\t\u00b8\n\t\3\t\6\t\u00bb\n\t\r\t\16\t\u00bc")
        buf.write("\3\n\3\n\6\n\u00c1\n\n\r\n\16\n\u00c2\3\13\3\13\3\f\3")
        buf.write("\f\5\f\u00c9\n\f\3\r\3\r\3\r\3\16\3\16\3\16\5\16\u00d1")
        buf.write("\n\16\3\17\3\17\3\17\3\17\7\17\u00d7\n\17\f\17\16\17\u00da")
        buf.write("\13\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\6\20\u00e3\n")
        buf.write("\20\r\20\16\20\u00e4\3\21\3\21\3\21\6\21\u00ea\n\21\r")
        buf.write("\21\16\21\u00eb\3\22\5\22\u00ef\n\22\3\22\6\22\u00f2\n")
        buf.write("\22\r\22\16\22\u00f3\3\23\3\23\3\23\3\23\6\23\u00fa\n")
        buf.write("\23\r\23\16\23\u00fb\3\24\3\24\3\24\3\24\3\24\3\24\5\24")
        buf.write("\u0104\n\24\3\25\5\25\u0107\n\25\3\25\6\25\u010a\n\25")
        buf.write("\r\25\16\25\u010b\3\25\3\25\5\25\u0110\n\25\3\25\5\25")
        buf.write("\u0113\n\25\3\26\3\26\5\26\u0117\n\26\3\27\3\27\7\27\u011b")
        buf.write("\n\27\f\27\16\27\u011e\13\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\5\30\u0127\n\30\3\31\3\31\3\31\7\31\u012c\n")
        buf.write("\31\f\31\16\31\u012f\13\31\3\32\3\32\3\32\3\32\3\32\3")
        buf.write("\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\36\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3 \3 \3 \3 \3 \3!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(")
        buf.write("\3(\3(\3(\3)\3)\3)\3)\3)\3*\3*\3*\3*\3*\3*\3+\3+\3+\3")
        buf.write("+\3,\3,\3,\3,\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3-\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3\60\3\60\3\60")
        buf.write("\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66")
        buf.write("\3\66\3\66\3\67\3\67\3\67\38\38\39\39\39\3:\3:\3;\3;\3")
        buf.write(";\3<\3<\3<\3=\3=\3=\3=\3>\3>\3?\3?\3?\3@\3@\3@\3A\3A\3")
        buf.write("B\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3")
        buf.write("J\3K\3K\3L\6L\u01fd\nL\rL\16L\u01fe\3L\3L\3M\3M\3M\3N")
        buf.write("\3N\7N\u0208\nN\fN\16N\u020b\13N\3N\5N\u020e\nN\3N\3N")
        buf.write("\3O\3O\7O\u0214\nO\fO\16O\u0217\13O\3O\3O\3O\3\u00d8\2")
        buf.write("P\3\3\5\4\7\5\t\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2\31")
        buf.write("\2\33\2\35\6\37\2!\2#\2%\2\'\7)\b+\t-\n/\13\61\f\63\r")
        buf.write("\65\16\67\179\20;\21=\22?\23A\24C\25E\26G\27I\30K\31M")
        buf.write("\32O\33Q\34S\35U\36W\37Y [!]\"_#a$c%e&g\'i(k)m*o+q,s-")
        buf.write("u.w/y\60{\61}\62\177\63\u0081\64\u0083\65\u0085\66\u0087")
        buf.write("\67\u00898\u008b9\u008d:\u008f;\u0091<\u0093=\u0095>\u0097")
        buf.write("?\u0099@\u009bA\u009dB\3\2\16\4\2\62;aa\3\2c|\3\2C\\\5")
        buf.write("\2C\\aac|\4\2GGgg\6\2\n\f\16\17))^^\t\2))^^ddhhppttvv")
        buf.write("\b\2))ddhhppttvv\4\2DDdd\4\2ZZzz\5\2\13\f\16\17\"\"\6")
        buf.write("\3\n\f\16\17$$^^\2\u0229\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\35\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2")
        buf.write("\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65")
        buf.write("\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2")
        buf.write("\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2")
        buf.write("\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2")
        buf.write("\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3")
        buf.write("\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e")
        buf.write("\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2")
        buf.write("o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2")
        buf.write("\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081")
        buf.write("\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2")
        buf.write("\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2")
        buf.write("\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d")
        buf.write("\3\2\2\2\3\u009f\3\2\2\2\5\u00a4\3\2\2\2\7\u00a8\3\2\2")
        buf.write("\2\t\u00ad\3\2\2\2\13\u00af\3\2\2\2\r\u00b1\3\2\2\2\17")
        buf.write("\u00b3\3\2\2\2\21\u00b5\3\2\2\2\23\u00be\3\2\2\2\25\u00c4")
        buf.write("\3\2\2\2\27\u00c8\3\2\2\2\31\u00ca\3\2\2\2\33\u00cd\3")
        buf.write("\2\2\2\35\u00d2\3\2\2\2\37\u00e0\3\2\2\2!\u00e6\3\2\2")
        buf.write("\2#\u00ee\3\2\2\2%\u00f5\3\2\2\2\'\u0103\3\2\2\2)\u0106")
        buf.write("\3\2\2\2+\u0116\3\2\2\2-\u0118\3\2\2\2/\u0126\3\2\2\2")
        buf.write("\61\u0128\3\2\2\2\63\u0130\3\2\2\2\65\u0136\3\2\2\2\67")
        buf.write("\u013f\3\2\2\29\u0142\3\2\2\2;\u0149\3\2\2\2=\u014e\3")
        buf.write("\2\2\2?\u0156\3\2\2\2A\u015b\3\2\2\2C\u0161\3\2\2\2E\u0167")
        buf.write("\3\2\2\2G\u016a\3\2\2\2I\u016e\3\2\2\2K\u0174\3\2\2\2")
        buf.write("M\u017c\3\2\2\2O\u0183\3\2\2\2Q\u018a\3\2\2\2S\u018f\3")
        buf.write("\2\2\2U\u0195\3\2\2\2W\u0199\3\2\2\2Y\u019d\3\2\2\2[\u01a9")
        buf.write("\3\2\2\2]\u01b4\3\2\2\2_\u01b8\3\2\2\2a\u01bb\3\2\2\2")
        buf.write("c\u01bd\3\2\2\2e\u01bf\3\2\2\2g\u01c1\3\2\2\2i\u01c3\3")
        buf.write("\2\2\2k\u01c5\3\2\2\2m\u01c8\3\2\2\2o\u01cb\3\2\2\2q\u01cd")
        buf.write("\3\2\2\2s\u01d0\3\2\2\2u\u01d2\3\2\2\2w\u01d5\3\2\2\2")
        buf.write("y\u01d8\3\2\2\2{\u01dc\3\2\2\2}\u01de\3\2\2\2\177\u01e1")
        buf.write("\3\2\2\2\u0081\u01e4\3\2\2\2\u0083\u01e6\3\2\2\2\u0085")
        buf.write("\u01e9\3\2\2\2\u0087\u01eb\3\2\2\2\u0089\u01ed\3\2\2\2")
        buf.write("\u008b\u01ef\3\2\2\2\u008d\u01f1\3\2\2\2\u008f\u01f3\3")
        buf.write("\2\2\2\u0091\u01f5\3\2\2\2\u0093\u01f7\3\2\2\2\u0095\u01f9")
        buf.write("\3\2\2\2\u0097\u01fc\3\2\2\2\u0099\u0202\3\2\2\2\u009b")
        buf.write("\u0205\3\2\2\2\u009d\u0211\3\2\2\2\u009f\u00a0\7o\2\2")
        buf.write("\u00a0\u00a1\7c\2\2\u00a1\u00a2\7k\2\2\u00a2\u00a3\7p")
        buf.write("\2\2\u00a3\4\3\2\2\2\u00a4\u00a5\7k\2\2\u00a5\u00a6\7")
        buf.write("p\2\2\u00a6\u00a7\7v\2\2\u00a7\6\3\2\2\2\u00a8\u00a9\7")
        buf.write("x\2\2\u00a9\u00aa\7q\2\2\u00aa\u00ab\7k\2\2\u00ab\u00ac")
        buf.write("\7f\2\2\u00ac\b\3\2\2\2\u00ad\u00ae\t\2\2\2\u00ae\n\3")
        buf.write("\2\2\2\u00af\u00b0\t\3\2\2\u00b0\f\3\2\2\2\u00b1\u00b2")
        buf.write("\t\4\2\2\u00b2\16\3\2\2\2\u00b3\u00b4\t\5\2\2\u00b4\20")
        buf.write("\3\2\2\2\u00b5\u00b7\t\6\2\2\u00b6\u00b8\7/\2\2\u00b7")
        buf.write("\u00b6\3\2\2\2\u00b7\u00b8\3\2\2\2\u00b8\u00ba\3\2\2\2")
        buf.write("\u00b9\u00bb\5\t\5\2\u00ba\u00b9\3\2\2\2\u00bb\u00bc\3")
        buf.write("\2\2\2\u00bc\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\22")
        buf.write("\3\2\2\2\u00be\u00c0\5\u0095K\2\u00bf\u00c1\5\t\5\2\u00c0")
        buf.write("\u00bf\3\2\2\2\u00c1\u00c2\3\2\2\2\u00c2\u00c0\3\2\2\2")
        buf.write("\u00c2\u00c3\3\2\2\2\u00c3\24\3\2\2\2\u00c4\u00c5\7$\2")
        buf.write("\2\u00c5\26\3\2\2\2\u00c6\u00c9\n\7\2\2\u00c7\u00c9\5")
        buf.write("\31\r\2\u00c8\u00c6\3\2\2\2\u00c8\u00c7\3\2\2\2\u00c9")
        buf.write("\30\3\2\2\2\u00ca\u00cb\7^\2\2\u00cb\u00cc\t\b\2\2\u00cc")
        buf.write("\32\3\2\2\2\u00cd\u00d0\7^\2\2\u00ce\u00d1\n\t\2\2\u00cf")
        buf.write("\u00d1\7^\2\2\u00d0\u00ce\3\2\2\2\u00d0\u00cf\3\2\2\2")
        buf.write("\u00d1\34\3\2\2\2\u00d2\u00d3\7%\2\2\u00d3\u00d4\7%\2")
        buf.write("\2\u00d4\u00d8\3\2\2\2\u00d5\u00d7\13\2\2\2\u00d6\u00d5")
        buf.write("\3\2\2\2\u00d7\u00da\3\2\2\2\u00d8\u00d9\3\2\2\2\u00d8")
        buf.write("\u00d6\3\2\2\2\u00d9\u00db\3\2\2\2\u00da\u00d8\3\2\2\2")
        buf.write("\u00db\u00dc\7%\2\2\u00dc\u00dd\7%\2\2\u00dd\u00de\3\2")
        buf.write("\2\2\u00de\u00df\b\17\2\2\u00df\36\3\2\2\2\u00e0\u00e2")
        buf.write("\7\62\2\2\u00e1\u00e3\5\t\5\2\u00e2\u00e1\3\2\2\2\u00e3")
        buf.write("\u00e4\3\2\2\2\u00e4\u00e2\3\2\2\2\u00e4\u00e5\3\2\2\2")
        buf.write("\u00e5 \3\2\2\2\u00e6\u00e7\7\62\2\2\u00e7\u00e9\t\n\2")
        buf.write("\2\u00e8\u00ea\4\62\63\2\u00e9\u00e8\3\2\2\2\u00ea\u00eb")
        buf.write("\3\2\2\2\u00eb\u00e9\3\2\2\2\u00eb\u00ec\3\2\2\2\u00ec")
        buf.write("\"\3\2\2\2\u00ed\u00ef\7/\2\2\u00ee\u00ed\3\2\2\2\u00ee")
        buf.write("\u00ef\3\2\2\2\u00ef\u00f1\3\2\2\2\u00f0\u00f2\5\t\5\2")
        buf.write("\u00f1\u00f0\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3\u00f1\3")
        buf.write("\2\2\2\u00f3\u00f4\3\2\2\2\u00f4$\3\2\2\2\u00f5\u00f6")
        buf.write("\7\62\2\2\u00f6\u00f9\t\13\2\2\u00f7\u00fa\5\r\7\2\u00f8")
        buf.write("\u00fa\5\t\5\2\u00f9\u00f7\3\2\2\2\u00f9\u00f8\3\2\2\2")
        buf.write("\u00fa\u00fb\3\2\2\2\u00fb\u00f9\3\2\2\2\u00fb\u00fc\3")
        buf.write("\2\2\2\u00fc&\3\2\2\2\u00fd\u0104\5\37\20\2\u00fe\u0104")
        buf.write("\5!\21\2\u00ff\u0104\5#\22\2\u0100\u0101\5%\23\2\u0101")
        buf.write("\u0102\b\24\3\2\u0102\u0104\3\2\2\2\u0103\u00fd\3\2\2")
        buf.write("\2\u0103\u00fe\3\2\2\2\u0103\u00ff\3\2\2\2\u0103\u0100")
        buf.write("\3\2\2\2\u0104(\3\2\2\2\u0105\u0107\7/\2\2\u0106\u0105")
        buf.write("\3\2\2\2\u0106\u0107\3\2\2\2\u0107\u0109\3\2\2\2\u0108")
        buf.write("\u010a\5\t\5\2\u0109\u0108\3\2\2\2\u010a\u010b\3\2\2\2")
        buf.write("\u010b\u0109\3\2\2\2\u010b\u010c\3\2\2\2\u010c\u0112\3")
        buf.write("\2\2\2\u010d\u010f\5\23\n\2\u010e\u0110\5\21\t\2\u010f")
        buf.write("\u010e\3\2\2\2\u010f\u0110\3\2\2\2\u0110\u0113\3\2\2\2")
        buf.write("\u0111\u0113\5\21\t\2\u0112\u010d\3\2\2\2\u0112\u0111")
        buf.write("\3\2\2\2\u0113*\3\2\2\2\u0114\u0117\5? \2\u0115\u0117")
        buf.write("\5A!\2\u0116\u0114\3\2\2\2\u0116\u0115\3\2\2\2\u0117,")
        buf.write("\3\2\2\2\u0118\u011c\5\25\13\2\u0119\u011b\5\27\f\2\u011a")
        buf.write("\u0119\3\2\2\2\u011b\u011e\3\2\2\2\u011c\u011a\3\2\2\2")
        buf.write("\u011c\u011d\3\2\2\2\u011d\u011f\3\2\2\2\u011e\u011c\3")
        buf.write("\2\2\2\u011f\u0120\5\25\13\2\u0120\u0121\b\27\4\2\u0121")
        buf.write(".\3\2\2\2\u0122\u0127\5\'\24\2\u0123\u0127\5)\25\2\u0124")
        buf.write("\u0127\5+\26\2\u0125\u0127\5-\27\2\u0126\u0122\3\2\2\2")
        buf.write("\u0126\u0123\3\2\2\2\u0126\u0124\3\2\2\2\u0126\u0125\3")
        buf.write("\2\2\2\u0127\60\3\2\2\2\u0128\u012d\5\17\b\2\u0129\u012c")
        buf.write("\5\17\b\2\u012a\u012c\5\t\5\2\u012b\u0129\3\2\2\2\u012b")
        buf.write("\u012a\3\2\2\2\u012c\u012f\3\2\2\2\u012d\u012b\3\2\2\2")
        buf.write("\u012d\u012e\3\2\2\2\u012e\62\3\2\2\2\u012f\u012d\3\2")
        buf.write("\2\2\u0130\u0131\7D\2\2\u0131\u0132\7t\2\2\u0132\u0133")
        buf.write("\7g\2\2\u0133\u0134\7c\2\2\u0134\u0135\7m\2\2\u0135\64")
        buf.write("\3\2\2\2\u0136\u0137\7E\2\2\u0137\u0138\7q\2\2\u0138\u0139")
        buf.write("\7p\2\2\u0139\u013a\7v\2\2\u013a\u013b\7k\2\2\u013b\u013c")
        buf.write("\7p\2\2\u013c\u013d\7w\2\2\u013d\u013e\7g\2\2\u013e\66")
        buf.write("\3\2\2\2\u013f\u0140\7K\2\2\u0140\u0141\7h\2\2\u01418")
        buf.write("\3\2\2\2\u0142\u0143\7G\2\2\u0143\u0144\7n\2\2\u0144\u0145")
        buf.write("\7u\2\2\u0145\u0146\7g\2\2\u0146\u0147\7k\2\2\u0147\u0148")
        buf.write("\7h\2\2\u0148:\3\2\2\2\u0149\u014a\7G\2\2\u014a\u014b")
        buf.write("\7n\2\2\u014b\u014c\7u\2\2\u014c\u014d\7g\2\2\u014d<\3")
        buf.write("\2\2\2\u014e\u014f\7H\2\2\u014f\u0150\7q\2\2\u0150\u0151")
        buf.write("\7t\2\2\u0151\u0152\7g\2\2\u0152\u0153\7c\2\2\u0153\u0154")
        buf.write("\7e\2\2\u0154\u0155\7j\2\2\u0155>\3\2\2\2\u0156\u0157")
        buf.write("\7V\2\2\u0157\u0158\7t\2\2\u0158\u0159\7w\2\2\u0159\u015a")
        buf.write("\7g\2\2\u015a@\3\2\2\2\u015b\u015c\7H\2\2\u015c\u015d")
        buf.write("\7c\2\2\u015d\u015e\7n\2\2\u015e\u015f\7u\2\2\u015f\u0160")
        buf.write("\7g\2\2\u0160B\3\2\2\2\u0161\u0162\7C\2\2\u0162\u0163")
        buf.write("\7t\2\2\u0163\u0164\7t\2\2\u0164\u0165\7c\2\2\u0165\u0166")
        buf.write("\7{\2\2\u0166D\3\2\2\2\u0167\u0168\7K\2\2\u0168\u0169")
        buf.write("\7p\2\2\u0169F\3\2\2\2\u016a\u016b\7K\2\2\u016b\u016c")
        buf.write("\7p\2\2\u016c\u016d\7v\2\2\u016dH\3\2\2\2\u016e\u016f")
        buf.write("\7H\2\2\u016f\u0170\7n\2\2\u0170\u0171\7q\2\2\u0171\u0172")
        buf.write("\7c\2\2\u0172\u0173\7v\2\2\u0173J\3\2\2\2\u0174\u0175")
        buf.write("\7D\2\2\u0175\u0176\7q\2\2\u0176\u0177\7q\2\2\u0177\u0178")
        buf.write("\7n\2\2\u0178\u0179\7g\2\2\u0179\u017a\7c\2\2\u017a\u017b")
        buf.write("\7p\2\2\u017bL\3\2\2\2\u017c\u017d\7U\2\2\u017d\u017e")
        buf.write("\7v\2\2\u017e\u017f\7t\2\2\u017f\u0180\7k\2\2\u0180\u0181")
        buf.write("\7p\2\2\u0181\u0182\7i\2\2\u0182N\3\2\2\2\u0183\u0184")
        buf.write("\7T\2\2\u0184\u0185\7g\2\2\u0185\u0186\7v\2\2\u0186\u0187")
        buf.write("\7w\2\2\u0187\u0188\7t\2\2\u0188\u0189\7p\2\2\u0189P\3")
        buf.write("\2\2\2\u018a\u018b\7P\2\2\u018b\u018c\7w\2\2\u018c\u018d")
        buf.write("\7n\2\2\u018d\u018e\7n\2\2\u018eR\3\2\2\2\u018f\u0190")
        buf.write("\7E\2\2\u0190\u0191\7n\2\2\u0191\u0192\7c\2\2\u0192\u0193")
        buf.write("\7u\2\2\u0193\u0194\7u\2\2\u0194T\3\2\2\2\u0195\u0196")
        buf.write("\7X\2\2\u0196\u0197\7c\2\2\u0197\u0198\7n\2\2\u0198V\3")
        buf.write("\2\2\2\u0199\u019a\7X\2\2\u019a\u019b\7c\2\2\u019b\u019c")
        buf.write("\7t\2\2\u019cX\3\2\2\2\u019d\u019e\7E\2\2\u019e\u019f")
        buf.write("\7q\2\2\u019f\u01a0\7p\2\2\u01a0\u01a1\7u\2\2\u01a1\u01a2")
        buf.write("\7v\2\2\u01a2\u01a3\7t\2\2\u01a3\u01a4\7w\2\2\u01a4\u01a5")
        buf.write("\7e\2\2\u01a5\u01a6\7v\2\2\u01a6\u01a7\7q\2\2\u01a7\u01a8")
        buf.write("\7t\2\2\u01a8Z\3\2\2\2\u01a9\u01aa\7F\2\2\u01aa\u01ab")
        buf.write("\7g\2\2\u01ab\u01ac\7u\2\2\u01ac\u01ad\7v\2\2\u01ad\u01ae")
        buf.write("\7t\2\2\u01ae\u01af\7w\2\2\u01af\u01b0\7e\2\2\u01b0\u01b1")
        buf.write("\7v\2\2\u01b1\u01b2\7q\2\2\u01b2\u01b3\7t\2\2\u01b3\\")
        buf.write("\3\2\2\2\u01b4\u01b5\7P\2\2\u01b5\u01b6\7g\2\2\u01b6\u01b7")
        buf.write("\7y\2\2\u01b7^\3\2\2\2\u01b8\u01b9\7D\2\2\u01b9\u01ba")
        buf.write("\7{\2\2\u01ba`\3\2\2\2\u01bb\u01bc\7-\2\2\u01bcb\3\2\2")
        buf.write("\2\u01bd\u01be\7/\2\2\u01bed\3\2\2\2\u01bf\u01c0\7,\2")
        buf.write("\2\u01c0f\3\2\2\2\u01c1\u01c2\7\61\2\2\u01c2h\3\2\2\2")
        buf.write("\u01c3\u01c4\7\'\2\2\u01c4j\3\2\2\2\u01c5\u01c6\7?\2\2")
        buf.write("\u01c6\u01c7\7?\2\2\u01c7l\3\2\2\2\u01c8\u01c9\7#\2\2")
        buf.write("\u01c9\u01ca\7?\2\2\u01can\3\2\2\2\u01cb\u01cc\7@\2\2")
        buf.write("\u01ccp\3\2\2\2\u01cd\u01ce\7@\2\2\u01ce\u01cf\7?\2\2")
        buf.write("\u01cfr\3\2\2\2\u01d0\u01d1\7>\2\2\u01d1t\3\2\2\2\u01d2")
        buf.write("\u01d3\7>\2\2\u01d3\u01d4\7?\2\2\u01d4v\3\2\2\2\u01d5")
        buf.write("\u01d6\7-\2\2\u01d6\u01d7\7\60\2\2\u01d7x\3\2\2\2\u01d8")
        buf.write("\u01d9\7?\2\2\u01d9\u01da\7?\2\2\u01da\u01db\7\60\2\2")
        buf.write("\u01dbz\3\2\2\2\u01dc\u01dd\7#\2\2\u01dd|\3\2\2\2\u01de")
        buf.write("\u01df\7(\2\2\u01df\u01e0\7(\2\2\u01e0~\3\2\2\2\u01e1")
        buf.write("\u01e2\7~\2\2\u01e2\u01e3\7~\2\2\u01e3\u0080\3\2\2\2\u01e4")
        buf.write("\u01e5\7?\2\2\u01e5\u0082\3\2\2\2\u01e6\u01e7\7<\2\2\u01e7")
        buf.write("\u01e8\7<\2\2\u01e8\u0084\3\2\2\2\u01e9\u01ea\7*\2\2\u01ea")
        buf.write("\u0086\3\2\2\2\u01eb\u01ec\7+\2\2\u01ec\u0088\3\2\2\2")
        buf.write("\u01ed\u01ee\7]\2\2\u01ee\u008a\3\2\2\2\u01ef\u01f0\7")
        buf.write("_\2\2\u01f0\u008c\3\2\2\2\u01f1\u01f2\7}\2\2\u01f2\u008e")
        buf.write("\3\2\2\2\u01f3\u01f4\7\177\2\2\u01f4\u0090\3\2\2\2\u01f5")
        buf.write("\u01f6\7=\2\2\u01f6\u0092\3\2\2\2\u01f7\u01f8\7.\2\2\u01f8")
        buf.write("\u0094\3\2\2\2\u01f9\u01fa\7\60\2\2\u01fa\u0096\3\2\2")
        buf.write("\2\u01fb\u01fd\t\f\2\2\u01fc\u01fb\3\2\2\2\u01fd\u01fe")
        buf.write("\3\2\2\2\u01fe\u01fc\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff")
        buf.write("\u0200\3\2\2\2\u0200\u0201\bL\2\2\u0201\u0098\3\2\2\2")
        buf.write("\u0202\u0203\13\2\2\2\u0203\u0204\bM\5\2\u0204\u009a\3")
        buf.write("\2\2\2\u0205\u0209\5\25\13\2\u0206\u0208\5\27\f\2\u0207")
        buf.write("\u0206\3\2\2\2\u0208\u020b\3\2\2\2\u0209\u0207\3\2\2\2")
        buf.write("\u0209\u020a\3\2\2\2\u020a\u020d\3\2\2\2\u020b\u0209\3")
        buf.write("\2\2\2\u020c\u020e\t\r\2\2\u020d\u020c\3\2\2\2\u020e\u020f")
        buf.write("\3\2\2\2\u020f\u0210\bN\6\2\u0210\u009c\3\2\2\2\u0211")
        buf.write("\u0215\5\25\13\2\u0212\u0214\5\27\f\2\u0213\u0212\3\2")
        buf.write("\2\2\u0214\u0217\3\2\2\2\u0215\u0213\3\2\2\2\u0215\u0216")
        buf.write("\3\2\2\2\u0216\u0218\3\2\2\2\u0217\u0215\3\2\2\2\u0218")
        buf.write("\u0219\5\33\16\2\u0219\u021a\bO\7\2\u021a\u009e\3\2\2")
        buf.write("\2\35\2\u00b7\u00bc\u00c2\u00c8\u00d0\u00d8\u00e4\u00eb")
        buf.write("\u00ee\u00f3\u00f9\u00fb\u0103\u0106\u010b\u010f\u0112")
        buf.write("\u0116\u011c\u0126\u012b\u012d\u01fe\u0209\u020d\u0215")
        buf.write("\b\b\2\2\3\24\2\3\27\3\3M\4\3N\5\3O\6")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    INTTYPE = 2
    VOIDTYPE = 3
    BLOCK_COMMENT = 4
    INTLIT = 5
    FLOATLIT = 6
    BOOLIT = 7
    STRLIT = 8
    DATALIT = 9
    ID = 10
    BREAK = 11
    CONTINUE = 12
    IF = 13
    ELSEIF = 14
    ELSE = 15
    FOREACH = 16
    TRUE = 17
    FALSE = 18
    ARRAY = 19
    IN = 20
    INT = 21
    FLOAT = 22
    BOOLEAN = 23
    STRING = 24
    RETURN = 25
    NULL = 26
    CLASS = 27
    VAL = 28
    VAR = 29
    CONSTRUCTOR = 30
    DESTRUCTOR = 31
    NEW = 32
    BY = 33
    ADD = 34
    SUB = 35
    MUL = 36
    DIV = 37
    MOD = 38
    EQ = 39
    NEQ = 40
    GT = 41
    GTE = 42
    LT = 43
    LTE = 44
    SADD = 45
    SEQ = 46
    NOT = 47
    AND = 48
    OR = 49
    ASSIGN = 50
    SCOPE = 51
    LB = 52
    RB = 53
    LSB = 54
    RSB = 55
    LCB = 56
    RCB = 57
    SM = 58
    CM = 59
    DOT = 60
    WS = 61
    ERROR_CHAR = 62
    UNCLOSE_STRING = 63
    ILLEGAL_ESCAPE = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'int'", "'void'", "'Break'", "'Continue'", "'If'", 
            "'Elseif'", "'Else'", "'Foreach'", "'True'", "'False'", "'Array'", 
            "'In'", "'Int'", "'Float'", "'Boolean'", "'String'", "'Return'", 
            "'Null'", "'Class'", "'Val'", "'Var'", "'Constructor'", "'Destructor'", 
            "'New'", "'By'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
            "'!='", "'>'", "'>='", "'<'", "'<='", "'+.'", "'==.'", "'!'", 
            "'&&'", "'||'", "'='", "'::'", "'('", "')'", "'['", "']'", "'{'", 
            "'}'", "';'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "INTTYPE", "VOIDTYPE", "BLOCK_COMMENT", "INTLIT", "FLOATLIT", 
            "BOOLIT", "STRLIT", "DATALIT", "ID", "BREAK", "CONTINUE", "IF", 
            "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", 
            "INT", "FLOAT", "BOOLEAN", "STRING", "RETURN", "NULL", "CLASS", 
            "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", "ADD", 
            "SUB", "MUL", "DIV", "MOD", "EQ", "NEQ", "GT", "GTE", "LT", 
            "LTE", "SADD", "SEQ", "NOT", "AND", "OR", "ASSIGN", "SCOPE", 
            "LB", "RB", "LSB", "RSB", "LCB", "RCB", "SM", "CM", "DOT", "WS", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "INTTYPE", "VOIDTYPE", "DIGIT", "LOWERCASE", "UPERCASE", 
                  "ALPHABET", "SCIENTIFIC", "DECIMAL_POINT", "DOUBLE_QUOTE", 
                  "STRING_LITERAL", "ESCAPE_SEQUENCE", "ILLEGAL_STRING", 
                  "BLOCK_COMMENT", "OCTAL", "BINARY", "DECIMAL", "HEXADECIMAL", 
                  "INTLIT", "FLOATLIT", "BOOLIT", "STRLIT", "DATALIT", "ID", 
                  "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
                  "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", 
                  "STRING", "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", 
                  "DESTRUCTOR", "NEW", "BY", "ADD", "SUB", "MUL", "DIV", 
                  "MOD", "EQ", "NEQ", "GT", "GTE", "LT", "LTE", "SADD", 
                  "SEQ", "NOT", "AND", "OR", "ASSIGN", "SCOPE", "LB", "RB", 
                  "LSB", "RSB", "LCB", "RCB", "SM", "CM", "DOT", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[18] = self.INTLIT_action 
            actions[21] = self.STRLIT_action 
            actions[75] = self.ERROR_CHAR_action 
            actions[76] = self.UNCLOSE_STRING_action 
            actions[77] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

    def STRLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

            	content = str(self.text)
            	self.text = content[1:-1]

     

    def ERROR_CHAR_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:
            raise ErrorToken(self.text)
     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 3:

                    unclose_str = str(self.text)
                    possible = ['\b', '\t', '\f', '\n', '\r', '"', '\\']
                    if unclose_str[-1] in possible:
                        raise UncloseString(unclose_str[1:-1])
                    else:
                        raise UncloseString(unclose_str[1:])
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            	
            		illegal_str = str(self.text)
            		raise IllegalEscape(illegal_str[1:])
            	
     


