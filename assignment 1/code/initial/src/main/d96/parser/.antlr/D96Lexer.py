# Generated from c:\Users\Admin\Desktop\P\BK\212\Principles of Programming Languages\Assignment\ppl\assignment 1\code\initial\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u022d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\3\2\3\2\3\2\3\2\3\2\3\3\3\3")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3")
        buf.write("\b\3\b\3\t\3\t\5\t\u00ba\n\t\3\t\6\t\u00bd\n\t\r\t\16")
        buf.write("\t\u00be\3\n\3\n\6\n\u00c3\n\n\r\n\16\n\u00c4\3\13\3\13")
        buf.write("\3\f\3\f\5\f\u00cb\n\f\3\r\3\r\3\r\3\16\3\16\3\16\5\16")
        buf.write("\u00d3\n\16\3\17\3\17\3\17\3\17\7\17\u00d9\n\17\f\17\16")
        buf.write("\17\u00dc\13\17\3\17\3\17\3\17\3\17\3\17\3\20\3\20\6\20")
        buf.write("\u00e5\n\20\r\20\16\20\u00e6\3\21\3\21\3\21\6\21\u00ec")
        buf.write("\n\21\r\21\16\21\u00ed\3\22\5\22\u00f1\n\22\3\22\6\22")
        buf.write("\u00f4\n\22\r\22\16\22\u00f5\3\23\3\23\3\23\3\23\6\23")
        buf.write("\u00fc\n\23\r\23\16\23\u00fd\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\5\24\u0106\n\24\3\25\5\25\u0109\n\25\3\25\6\25\u010c")
        buf.write("\n\25\r\25\16\25\u010d\3\25\3\25\5\25\u0112\n\25\3\25")
        buf.write("\5\25\u0115\n\25\3\26\3\26\5\26\u0119\n\26\3\27\3\27\7")
        buf.write("\27\u011d\n\27\f\27\16\27\u0120\13\27\3\27\3\27\3\27\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\7\30\u012b\n\30\f\30\16\30")
        buf.write("\u012e\13\30\5\30\u0130\n\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\5\31\u0139\n\31\3\32\3\32\3\32\7\32\u013e\n")
        buf.write("\32\f\32\16\32\u0141\13\32\3\33\3\33\3\33\3\33\3\33\3")
        buf.write("\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3 \3!\3!\3!\3!\3")
        buf.write("!\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3")
        buf.write("%\3%\3%\3%\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\3\'\3")
        buf.write("\'\3\'\3(\3(\3(\3(\3(\3(\3(\3)\3)\3)\3)\3)\3)\3)\3*\3")
        buf.write("*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3,\3,\3,\3,\3-\3-\3-\3-\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3.\3/\3/\3/\3/\3/\3/\3")
        buf.write("/\3/\3/\3/\3/\3\60\3\60\3\60\3\60\3\61\3\61\3\61\3\62")
        buf.write("\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67")
        buf.write("\3\67\38\38\38\39\39\3:\3:\3:\3;\3;\3<\3<\3<\3=\3=\3=")
        buf.write("\3>\3>\3>\3>\3?\3?\3@\3@\3@\3A\3A\3A\3B\3B\3C\3C\3C\3")
        buf.write("D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3I\3J\3J\3K\3K\3L\3L\3")
        buf.write("M\6M\u020f\nM\rM\16M\u0210\3M\3M\3N\3N\3N\3O\3O\7O\u021a")
        buf.write("\nO\fO\16O\u021d\13O\3O\5O\u0220\nO\3O\3O\3P\3P\7P\u0226")
        buf.write("\nP\fP\16P\u0229\13P\3P\3P\3P\3\u00da\2Q\3\3\5\4\7\5\t")
        buf.write("\2\13\2\r\2\17\2\21\2\23\2\25\2\27\2\31\2\33\2\35\6\37")
        buf.write("\2!\2#\2%\2\'\7)\b+\t-\n/\13\61\f\63\r\65\16\67\179\20")
        buf.write(";\21=\22?\23A\24C\25E\26G\27I\30K\31M\32O\33Q\34S\35U")
        buf.write("\36W\37Y [!]\"_#a$c%e&g\'i(k)m*o+q,s-u.w/y\60{\61}\62")
        buf.write("\177\63\u0081\64\u0083\65\u0085\66\u0087\67\u00898\u008b")
        buf.write("9\u008d:\u008f;\u0091<\u0093=\u0095>\u0097?\u0099@\u009b")
        buf.write("A\u009dB\u009fC\3\2\16\4\2\62;aa\3\2c|\3\2C\\\5\2C\\a")
        buf.write("ac|\4\2GGgg\6\2\n\f\16\17))^^\t\2))^^ddhhppttvv\b\2))")
        buf.write("ddhhppttvv\4\2DDdd\4\2ZZzz\5\2\13\f\16\17\"\"\6\3\n\f")
        buf.write("\16\17$$^^\2\u023e\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2")
        buf.write("\2\35\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2")
        buf.write("\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2")
        buf.write("\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2")
        buf.write("\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3")
        buf.write("\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S")
        buf.write("\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2")
        buf.write("]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2")
        buf.write("\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2")
        buf.write("\2\2q\3\2\2\2\2s\3\2\2\2\2u\3\2\2\2\2w\3\2\2\2\2y\3\2")
        buf.write("\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2\u0081\3\2\2")
        buf.write("\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087\3\2\2\2\2\u0089")
        buf.write("\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3\2\2")
        buf.write("\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2\2\u0097")
        buf.write("\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2")
        buf.write("\2\2\u009f\3\2\2\2\3\u00a1\3\2\2\2\5\u00a6\3\2\2\2\7\u00aa")
        buf.write("\3\2\2\2\t\u00af\3\2\2\2\13\u00b1\3\2\2\2\r\u00b3\3\2")
        buf.write("\2\2\17\u00b5\3\2\2\2\21\u00b7\3\2\2\2\23\u00c0\3\2\2")
        buf.write("\2\25\u00c6\3\2\2\2\27\u00ca\3\2\2\2\31\u00cc\3\2\2\2")
        buf.write("\33\u00cf\3\2\2\2\35\u00d4\3\2\2\2\37\u00e2\3\2\2\2!\u00e8")
        buf.write("\3\2\2\2#\u00f0\3\2\2\2%\u00f7\3\2\2\2\'\u0105\3\2\2\2")
        buf.write(")\u0108\3\2\2\2+\u0118\3\2\2\2-\u011a\3\2\2\2/\u0124\3")
        buf.write("\2\2\2\61\u0138\3\2\2\2\63\u013a\3\2\2\2\65\u0142\3\2")
        buf.write("\2\2\67\u0148\3\2\2\29\u0151\3\2\2\2;\u0154\3\2\2\2=\u015b")
        buf.write("\3\2\2\2?\u0160\3\2\2\2A\u0168\3\2\2\2C\u016d\3\2\2\2")
        buf.write("E\u0173\3\2\2\2G\u0179\3\2\2\2I\u017c\3\2\2\2K\u0180\3")
        buf.write("\2\2\2M\u0186\3\2\2\2O\u018e\3\2\2\2Q\u0195\3\2\2\2S\u019c")
        buf.write("\3\2\2\2U\u01a1\3\2\2\2W\u01a7\3\2\2\2Y\u01ab\3\2\2\2")
        buf.write("[\u01af\3\2\2\2]\u01bb\3\2\2\2_\u01c6\3\2\2\2a\u01ca\3")
        buf.write("\2\2\2c\u01cd\3\2\2\2e\u01cf\3\2\2\2g\u01d1\3\2\2\2i\u01d3")
        buf.write("\3\2\2\2k\u01d5\3\2\2\2m\u01d7\3\2\2\2o\u01da\3\2\2\2")
        buf.write("q\u01dd\3\2\2\2s\u01df\3\2\2\2u\u01e2\3\2\2\2w\u01e4\3")
        buf.write("\2\2\2y\u01e7\3\2\2\2{\u01ea\3\2\2\2}\u01ee\3\2\2\2\177")
        buf.write("\u01f0\3\2\2\2\u0081\u01f3\3\2\2\2\u0083\u01f6\3\2\2\2")
        buf.write("\u0085\u01f8\3\2\2\2\u0087\u01fb\3\2\2\2\u0089\u01fd\3")
        buf.write("\2\2\2\u008b\u01ff\3\2\2\2\u008d\u0201\3\2\2\2\u008f\u0203")
        buf.write("\3\2\2\2\u0091\u0205\3\2\2\2\u0093\u0207\3\2\2\2\u0095")
        buf.write("\u0209\3\2\2\2\u0097\u020b\3\2\2\2\u0099\u020e\3\2\2\2")
        buf.write("\u009b\u0214\3\2\2\2\u009d\u0217\3\2\2\2\u009f\u0223\3")
        buf.write("\2\2\2\u00a1\u00a2\7o\2\2\u00a2\u00a3\7c\2\2\u00a3\u00a4")
        buf.write("\7k\2\2\u00a4\u00a5\7p\2\2\u00a5\4\3\2\2\2\u00a6\u00a7")
        buf.write("\7k\2\2\u00a7\u00a8\7p\2\2\u00a8\u00a9\7v\2\2\u00a9\6")
        buf.write("\3\2\2\2\u00aa\u00ab\7x\2\2\u00ab\u00ac\7q\2\2\u00ac\u00ad")
        buf.write("\7k\2\2\u00ad\u00ae\7f\2\2\u00ae\b\3\2\2\2\u00af\u00b0")
        buf.write("\t\2\2\2\u00b0\n\3\2\2\2\u00b1\u00b2\t\3\2\2\u00b2\f\3")
        buf.write("\2\2\2\u00b3\u00b4\t\4\2\2\u00b4\16\3\2\2\2\u00b5\u00b6")
        buf.write("\t\5\2\2\u00b6\20\3\2\2\2\u00b7\u00b9\t\6\2\2\u00b8\u00ba")
        buf.write("\7/\2\2\u00b9\u00b8\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba")
        buf.write("\u00bc\3\2\2\2\u00bb\u00bd\5\t\5\2\u00bc\u00bb\3\2\2\2")
        buf.write("\u00bd\u00be\3\2\2\2\u00be\u00bc\3\2\2\2\u00be\u00bf\3")
        buf.write("\2\2\2\u00bf\22\3\2\2\2\u00c0\u00c2\5\u0097L\2\u00c1\u00c3")
        buf.write("\5\t\5\2\u00c2\u00c1\3\2\2\2\u00c3\u00c4\3\2\2\2\u00c4")
        buf.write("\u00c2\3\2\2\2\u00c4\u00c5\3\2\2\2\u00c5\24\3\2\2\2\u00c6")
        buf.write("\u00c7\7$\2\2\u00c7\26\3\2\2\2\u00c8\u00cb\n\7\2\2\u00c9")
        buf.write("\u00cb\5\31\r\2\u00ca\u00c8\3\2\2\2\u00ca\u00c9\3\2\2")
        buf.write("\2\u00cb\30\3\2\2\2\u00cc\u00cd\7^\2\2\u00cd\u00ce\t\b")
        buf.write("\2\2\u00ce\32\3\2\2\2\u00cf\u00d2\7^\2\2\u00d0\u00d3\n")
        buf.write("\t\2\2\u00d1\u00d3\7^\2\2\u00d2\u00d0\3\2\2\2\u00d2\u00d1")
        buf.write("\3\2\2\2\u00d3\34\3\2\2\2\u00d4\u00d5\7%\2\2\u00d5\u00d6")
        buf.write("\7%\2\2\u00d6\u00da\3\2\2\2\u00d7\u00d9\13\2\2\2\u00d8")
        buf.write("\u00d7\3\2\2\2\u00d9\u00dc\3\2\2\2\u00da\u00db\3\2\2\2")
        buf.write("\u00da\u00d8\3\2\2\2\u00db\u00dd\3\2\2\2\u00dc\u00da\3")
        buf.write("\2\2\2\u00dd\u00de\7%\2\2\u00de\u00df\7%\2\2\u00df\u00e0")
        buf.write("\3\2\2\2\u00e0\u00e1\b\17\2\2\u00e1\36\3\2\2\2\u00e2\u00e4")
        buf.write("\7\62\2\2\u00e3\u00e5\5\t\5\2\u00e4\u00e3\3\2\2\2\u00e5")
        buf.write("\u00e6\3\2\2\2\u00e6\u00e4\3\2\2\2\u00e6\u00e7\3\2\2\2")
        buf.write("\u00e7 \3\2\2\2\u00e8\u00e9\7\62\2\2\u00e9\u00eb\t\n\2")
        buf.write("\2\u00ea\u00ec\4\62\63\2\u00eb\u00ea\3\2\2\2\u00ec\u00ed")
        buf.write("\3\2\2\2\u00ed\u00eb\3\2\2\2\u00ed\u00ee\3\2\2\2\u00ee")
        buf.write("\"\3\2\2\2\u00ef\u00f1\7/\2\2\u00f0\u00ef\3\2\2\2\u00f0")
        buf.write("\u00f1\3\2\2\2\u00f1\u00f3\3\2\2\2\u00f2\u00f4\5\t\5\2")
        buf.write("\u00f3\u00f2\3\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f3\3")
        buf.write("\2\2\2\u00f5\u00f6\3\2\2\2\u00f6$\3\2\2\2\u00f7\u00f8")
        buf.write("\7\62\2\2\u00f8\u00fb\t\13\2\2\u00f9\u00fc\5\r\7\2\u00fa")
        buf.write("\u00fc\5\t\5\2\u00fb\u00f9\3\2\2\2\u00fb\u00fa\3\2\2\2")
        buf.write("\u00fc\u00fd\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fe\3")
        buf.write("\2\2\2\u00fe&\3\2\2\2\u00ff\u0106\5\37\20\2\u0100\u0106")
        buf.write("\5!\21\2\u0101\u0106\5#\22\2\u0102\u0103\5%\23\2\u0103")
        buf.write("\u0104\b\24\3\2\u0104\u0106\3\2\2\2\u0105\u00ff\3\2\2")
        buf.write("\2\u0105\u0100\3\2\2\2\u0105\u0101\3\2\2\2\u0105\u0102")
        buf.write("\3\2\2\2\u0106(\3\2\2\2\u0107\u0109\7/\2\2\u0108\u0107")
        buf.write("\3\2\2\2\u0108\u0109\3\2\2\2\u0109\u010b\3\2\2\2\u010a")
        buf.write("\u010c\5\t\5\2\u010b\u010a\3\2\2\2\u010c\u010d\3\2\2\2")
        buf.write("\u010d\u010b\3\2\2\2\u010d\u010e\3\2\2\2\u010e\u0114\3")
        buf.write("\2\2\2\u010f\u0111\5\23\n\2\u0110\u0112\5\21\t\2\u0111")
        buf.write("\u0110\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0115\3\2\2\2")
        buf.write("\u0113\u0115\5\21\t\2\u0114\u010f\3\2\2\2\u0114\u0113")
        buf.write("\3\2\2\2\u0115*\3\2\2\2\u0116\u0119\5A!\2\u0117\u0119")
        buf.write("\5C\"\2\u0118\u0116\3\2\2\2\u0118\u0117\3\2\2\2\u0119")
        buf.write(",\3\2\2\2\u011a\u011e\5\25\13\2\u011b\u011d\5\27\f\2\u011c")
        buf.write("\u011b\3\2\2\2\u011d\u0120\3\2\2\2\u011e\u011c\3\2\2\2")
        buf.write("\u011e\u011f\3\2\2\2\u011f\u0121\3\2\2\2\u0120\u011e\3")
        buf.write("\2\2\2\u0121\u0122\5\25\13\2\u0122\u0123\b\27\4\2\u0123")
        buf.write(".\3\2\2\2\u0124\u0125\5E#\2\u0125\u012f\5\u0087D\2\u0126")
        buf.write("\u012c\5\61\31\2\u0127\u0128\5\u0095K\2\u0128\u0129\5")
        buf.write("\61\31\2\u0129\u012b\3\2\2\2\u012a\u0127\3\2\2\2\u012b")
        buf.write("\u012e\3\2\2\2\u012c\u012a\3\2\2\2\u012c\u012d\3\2\2\2")
        buf.write("\u012d\u0130\3\2\2\2\u012e\u012c\3\2\2\2\u012f\u0126\3")
        buf.write("\2\2\2\u012f\u0130\3\2\2\2\u0130\u0131\3\2\2\2\u0131\u0132")
        buf.write("\5\u0089E\2\u0132\60\3\2\2\2\u0133\u0139\5\'\24\2\u0134")
        buf.write("\u0139\5)\25\2\u0135\u0139\5+\26\2\u0136\u0139\5-\27\2")
        buf.write("\u0137\u0139\5/\30\2\u0138\u0133\3\2\2\2\u0138\u0134\3")
        buf.write("\2\2\2\u0138\u0135\3\2\2\2\u0138\u0136\3\2\2\2\u0138\u0137")
        buf.write("\3\2\2\2\u0139\62\3\2\2\2\u013a\u013f\5\17\b\2\u013b\u013e")
        buf.write("\5\17\b\2\u013c\u013e\5\t\5\2\u013d\u013b\3\2\2\2\u013d")
        buf.write("\u013c\3\2\2\2\u013e\u0141\3\2\2\2\u013f\u013d\3\2\2\2")
        buf.write("\u013f\u0140\3\2\2\2\u0140\64\3\2\2\2\u0141\u013f\3\2")
        buf.write("\2\2\u0142\u0143\7D\2\2\u0143\u0144\7t\2\2\u0144\u0145")
        buf.write("\7g\2\2\u0145\u0146\7c\2\2\u0146\u0147\7m\2\2\u0147\66")
        buf.write("\3\2\2\2\u0148\u0149\7E\2\2\u0149\u014a\7q\2\2\u014a\u014b")
        buf.write("\7p\2\2\u014b\u014c\7v\2\2\u014c\u014d\7k\2\2\u014d\u014e")
        buf.write("\7p\2\2\u014e\u014f\7w\2\2\u014f\u0150\7g\2\2\u01508\3")
        buf.write("\2\2\2\u0151\u0152\7K\2\2\u0152\u0153\7h\2\2\u0153:\3")
        buf.write("\2\2\2\u0154\u0155\7G\2\2\u0155\u0156\7n\2\2\u0156\u0157")
        buf.write("\7u\2\2\u0157\u0158\7g\2\2\u0158\u0159\7k\2\2\u0159\u015a")
        buf.write("\7h\2\2\u015a<\3\2\2\2\u015b\u015c\7G\2\2\u015c\u015d")
        buf.write("\7n\2\2\u015d\u015e\7u\2\2\u015e\u015f\7g\2\2\u015f>\3")
        buf.write("\2\2\2\u0160\u0161\7H\2\2\u0161\u0162\7q\2\2\u0162\u0163")
        buf.write("\7t\2\2\u0163\u0164\7g\2\2\u0164\u0165\7c\2\2\u0165\u0166")
        buf.write("\7e\2\2\u0166\u0167\7j\2\2\u0167@\3\2\2\2\u0168\u0169")
        buf.write("\7V\2\2\u0169\u016a\7t\2\2\u016a\u016b\7w\2\2\u016b\u016c")
        buf.write("\7g\2\2\u016cB\3\2\2\2\u016d\u016e\7H\2\2\u016e\u016f")
        buf.write("\7c\2\2\u016f\u0170\7n\2\2\u0170\u0171\7u\2\2\u0171\u0172")
        buf.write("\7g\2\2\u0172D\3\2\2\2\u0173\u0174\7C\2\2\u0174\u0175")
        buf.write("\7t\2\2\u0175\u0176\7t\2\2\u0176\u0177\7c\2\2\u0177\u0178")
        buf.write("\7{\2\2\u0178F\3\2\2\2\u0179\u017a\7K\2\2\u017a\u017b")
        buf.write("\7p\2\2\u017bH\3\2\2\2\u017c\u017d\7K\2\2\u017d\u017e")
        buf.write("\7p\2\2\u017e\u017f\7v\2\2\u017fJ\3\2\2\2\u0180\u0181")
        buf.write("\7H\2\2\u0181\u0182\7n\2\2\u0182\u0183\7q\2\2\u0183\u0184")
        buf.write("\7c\2\2\u0184\u0185\7v\2\2\u0185L\3\2\2\2\u0186\u0187")
        buf.write("\7D\2\2\u0187\u0188\7q\2\2\u0188\u0189\7q\2\2\u0189\u018a")
        buf.write("\7n\2\2\u018a\u018b\7g\2\2\u018b\u018c\7c\2\2\u018c\u018d")
        buf.write("\7p\2\2\u018dN\3\2\2\2\u018e\u018f\7U\2\2\u018f\u0190")
        buf.write("\7v\2\2\u0190\u0191\7t\2\2\u0191\u0192\7k\2\2\u0192\u0193")
        buf.write("\7p\2\2\u0193\u0194\7i\2\2\u0194P\3\2\2\2\u0195\u0196")
        buf.write("\7T\2\2\u0196\u0197\7g\2\2\u0197\u0198\7v\2\2\u0198\u0199")
        buf.write("\7w\2\2\u0199\u019a\7t\2\2\u019a\u019b\7p\2\2\u019bR\3")
        buf.write("\2\2\2\u019c\u019d\7P\2\2\u019d\u019e\7w\2\2\u019e\u019f")
        buf.write("\7n\2\2\u019f\u01a0\7n\2\2\u01a0T\3\2\2\2\u01a1\u01a2")
        buf.write("\7E\2\2\u01a2\u01a3\7n\2\2\u01a3\u01a4\7c\2\2\u01a4\u01a5")
        buf.write("\7u\2\2\u01a5\u01a6\7u\2\2\u01a6V\3\2\2\2\u01a7\u01a8")
        buf.write("\7X\2\2\u01a8\u01a9\7c\2\2\u01a9\u01aa\7n\2\2\u01aaX\3")
        buf.write("\2\2\2\u01ab\u01ac\7X\2\2\u01ac\u01ad\7c\2\2\u01ad\u01ae")
        buf.write("\7t\2\2\u01aeZ\3\2\2\2\u01af\u01b0\7E\2\2\u01b0\u01b1")
        buf.write("\7q\2\2\u01b1\u01b2\7p\2\2\u01b2\u01b3\7u\2\2\u01b3\u01b4")
        buf.write("\7v\2\2\u01b4\u01b5\7t\2\2\u01b5\u01b6\7w\2\2\u01b6\u01b7")
        buf.write("\7e\2\2\u01b7\u01b8\7v\2\2\u01b8\u01b9\7q\2\2\u01b9\u01ba")
        buf.write("\7t\2\2\u01ba\\\3\2\2\2\u01bb\u01bc\7F\2\2\u01bc\u01bd")
        buf.write("\7g\2\2\u01bd\u01be\7u\2\2\u01be\u01bf\7v\2\2\u01bf\u01c0")
        buf.write("\7t\2\2\u01c0\u01c1\7w\2\2\u01c1\u01c2\7e\2\2\u01c2\u01c3")
        buf.write("\7v\2\2\u01c3\u01c4\7q\2\2\u01c4\u01c5\7t\2\2\u01c5^\3")
        buf.write("\2\2\2\u01c6\u01c7\7P\2\2\u01c7\u01c8\7g\2\2\u01c8\u01c9")
        buf.write("\7y\2\2\u01c9`\3\2\2\2\u01ca\u01cb\7D\2\2\u01cb\u01cc")
        buf.write("\7{\2\2\u01ccb\3\2\2\2\u01cd\u01ce\7-\2\2\u01ced\3\2\2")
        buf.write("\2\u01cf\u01d0\7/\2\2\u01d0f\3\2\2\2\u01d1\u01d2\7,\2")
        buf.write("\2\u01d2h\3\2\2\2\u01d3\u01d4\7\61\2\2\u01d4j\3\2\2\2")
        buf.write("\u01d5\u01d6\7\'\2\2\u01d6l\3\2\2\2\u01d7\u01d8\7?\2\2")
        buf.write("\u01d8\u01d9\7?\2\2\u01d9n\3\2\2\2\u01da\u01db\7#\2\2")
        buf.write("\u01db\u01dc\7?\2\2\u01dcp\3\2\2\2\u01dd\u01de\7@\2\2")
        buf.write("\u01der\3\2\2\2\u01df\u01e0\7@\2\2\u01e0\u01e1\7?\2\2")
        buf.write("\u01e1t\3\2\2\2\u01e2\u01e3\7>\2\2\u01e3v\3\2\2\2\u01e4")
        buf.write("\u01e5\7>\2\2\u01e5\u01e6\7?\2\2\u01e6x\3\2\2\2\u01e7")
        buf.write("\u01e8\7-\2\2\u01e8\u01e9\7\60\2\2\u01e9z\3\2\2\2\u01ea")
        buf.write("\u01eb\7?\2\2\u01eb\u01ec\7?\2\2\u01ec\u01ed\7\60\2\2")
        buf.write("\u01ed|\3\2\2\2\u01ee\u01ef\7#\2\2\u01ef~\3\2\2\2\u01f0")
        buf.write("\u01f1\7(\2\2\u01f1\u01f2\7(\2\2\u01f2\u0080\3\2\2\2\u01f3")
        buf.write("\u01f4\7~\2\2\u01f4\u01f5\7~\2\2\u01f5\u0082\3\2\2\2\u01f6")
        buf.write("\u01f7\7?\2\2\u01f7\u0084\3\2\2\2\u01f8\u01f9\7<\2\2\u01f9")
        buf.write("\u01fa\7<\2\2\u01fa\u0086\3\2\2\2\u01fb\u01fc\7*\2\2\u01fc")
        buf.write("\u0088\3\2\2\2\u01fd\u01fe\7+\2\2\u01fe\u008a\3\2\2\2")
        buf.write("\u01ff\u0200\7]\2\2\u0200\u008c\3\2\2\2\u0201\u0202\7")
        buf.write("_\2\2\u0202\u008e\3\2\2\2\u0203\u0204\7}\2\2\u0204\u0090")
        buf.write("\3\2\2\2\u0205\u0206\7\177\2\2\u0206\u0092\3\2\2\2\u0207")
        buf.write("\u0208\7=\2\2\u0208\u0094\3\2\2\2\u0209\u020a\7.\2\2\u020a")
        buf.write("\u0096\3\2\2\2\u020b\u020c\7\60\2\2\u020c\u0098\3\2\2")
        buf.write("\2\u020d\u020f\t\f\2\2\u020e\u020d\3\2\2\2\u020f\u0210")
        buf.write("\3\2\2\2\u0210\u020e\3\2\2\2\u0210\u0211\3\2\2\2\u0211")
        buf.write("\u0212\3\2\2\2\u0212\u0213\bM\2\2\u0213\u009a\3\2\2\2")
        buf.write("\u0214\u0215\13\2\2\2\u0215\u0216\bN\5\2\u0216\u009c\3")
        buf.write("\2\2\2\u0217\u021b\5\25\13\2\u0218\u021a\5\27\f\2\u0219")
        buf.write("\u0218\3\2\2\2\u021a\u021d\3\2\2\2\u021b\u0219\3\2\2\2")
        buf.write("\u021b\u021c\3\2\2\2\u021c\u021f\3\2\2\2\u021d\u021b\3")
        buf.write("\2\2\2\u021e\u0220\t\r\2\2\u021f\u021e\3\2\2\2\u0220\u0221")
        buf.write("\3\2\2\2\u0221\u0222\bO\6\2\u0222\u009e\3\2\2\2\u0223")
        buf.write("\u0227\5\25\13\2\u0224\u0226\5\27\f\2\u0225\u0224\3\2")
        buf.write("\2\2\u0226\u0229\3\2\2\2\u0227\u0225\3\2\2\2\u0227\u0228")
        buf.write("\3\2\2\2\u0228\u022a\3\2\2\2\u0229\u0227\3\2\2\2\u022a")
        buf.write("\u022b\5\33\16\2\u022b\u022c\bP\7\2\u022c\u00a0\3\2\2")
        buf.write("\2\37\2\u00b9\u00be\u00c4\u00ca\u00d2\u00da\u00e6\u00ed")
        buf.write("\u00f0\u00f5\u00fb\u00fd\u0105\u0108\u010d\u0111\u0114")
        buf.write("\u0118\u011e\u012c\u012f\u0138\u013d\u013f\u0210\u021b")
        buf.write("\u021f\u0227\b\b\2\2\3\24\2\3\27\3\3N\4\3O\5\3P\6")
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
    IDX_ARRAY = 9
    DATALIT = 10
    ID = 11
    BREAK = 12
    CONTINUE = 13
    IF = 14
    ELSEIF = 15
    ELSE = 16
    FOREACH = 17
    TRUE = 18
    FALSE = 19
    ARRAY = 20
    IN = 21
    INT = 22
    FLOAT = 23
    BOOLEAN = 24
    STRING = 25
    RETURN = 26
    NULL = 27
    CLASS = 28
    VAL = 29
    VAR = 30
    CONSTRUCTOR = 31
    DESTRUCTOR = 32
    NEW = 33
    BY = 34
    ADD = 35
    SUB = 36
    MUL = 37
    DIV = 38
    MOD = 39
    EQ = 40
    NEQ = 41
    GT = 42
    GTE = 43
    LT = 44
    LTE = 45
    SADD = 46
    SEQ = 47
    NOT = 48
    AND = 49
    OR = 50
    ASSIGN = 51
    SCOPE = 52
    LB = 53
    RB = 54
    LSB = 55
    RSB = 56
    LCB = 57
    RCB = 58
    SM = 59
    CM = 60
    DOT = 61
    WS = 62
    ERROR_CHAR = 63
    UNCLOSE_STRING = 64
    ILLEGAL_ESCAPE = 65

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
            "BOOLIT", "STRLIT", "IDX_ARRAY", "DATALIT", "ID", "BREAK", "CONTINUE", 
            "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", 
            "IN", "INT", "FLOAT", "BOOLEAN", "STRING", "RETURN", "NULL", 
            "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", 
            "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", "NEQ", "GT", "GTE", 
            "LT", "LTE", "SADD", "SEQ", "NOT", "AND", "OR", "ASSIGN", "SCOPE", 
            "LB", "RB", "LSB", "RSB", "LCB", "RCB", "SM", "CM", "DOT", "WS", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "INTTYPE", "VOIDTYPE", "DIGIT", "LOWERCASE", "UPERCASE", 
                  "ALPHABET", "SCIENTIFIC", "DECIMAL_POINT", "DOUBLE_QUOTE", 
                  "STRING_LITERAL", "ESCAPE_SEQUENCE", "ILLEGAL_STRING", 
                  "BLOCK_COMMENT", "OCTAL", "BINARY", "DECIMAL", "HEXADECIMAL", 
                  "INTLIT", "FLOATLIT", "BOOLIT", "STRLIT", "IDX_ARRAY", 
                  "DATALIT", "ID", "BREAK", "CONTINUE", "IF", "ELSEIF", 
                  "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", "INT", 
                  "FLOAT", "BOOLEAN", "STRING", "RETURN", "NULL", "CLASS", 
                  "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", 
                  "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", "NEQ", "GT", 
                  "GTE", "LT", "LTE", "SADD", "SEQ", "NOT", "AND", "OR", 
                  "ASSIGN", "SCOPE", "LB", "RB", "LSB", "RSB", "LCB", "RCB", 
                  "SM", "CM", "DOT", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                  "ILLEGAL_ESCAPE" ]

    grammarFileName = "D96.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[18] = self.INTLIT_action 
            actions[21] = self.STRLIT_action 
            actions[76] = self.ERROR_CHAR_action 
            actions[77] = self.UNCLOSE_STRING_action 
            actions[78] = self.ILLEGAL_ESCAPE_action 
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
            	
     


