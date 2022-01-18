# Generated from c:\Users\Admin\Desktop\P\BK\212\Principles of Programming Languages\Assignment\ppl\assignment 1\code\initial\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2A")
        buf.write("\u0213\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\3\2\3\2\3\2\3\2\3\2\3\3\3\3\3\4\3")
        buf.write("\4\3\5\3\5\3\6\3\6\3\7\3\7\5\7\u00af\n\7\3\7\6\7\u00b2")
        buf.write("\n\7\r\7\16\7\u00b3\3\b\3\b\6\b\u00b8\n\b\r\b\16\b\u00b9")
        buf.write("\3\t\3\t\3\n\3\n\3\n\5\n\u00c1\n\n\3\13\3\13\3\13\3\f")
        buf.write("\3\f\3\f\3\r\3\r\3\r\5\r\u00cc\n\r\3\16\3\16\3\16\3\16")
        buf.write("\7\16\u00d2\n\16\f\16\16\16\u00d5\13\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\17\3\17\6\17\u00de\n\17\r\17\16\17\u00df")
        buf.write("\3\20\3\20\3\20\6\20\u00e5\n\20\r\20\16\20\u00e6\3\21")
        buf.write("\5\21\u00ea\n\21\3\21\6\21\u00ed\n\21\r\21\16\21\u00ee")
        buf.write("\3\22\3\22\3\22\3\22\6\22\u00f5\n\22\r\22\16\22\u00f6")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\5\23\u00ff\n\23\3\24\5")
        buf.write("\24\u0102\n\24\3\24\6\24\u0105\n\24\r\24\16\24\u0106\3")
        buf.write("\24\3\24\5\24\u010b\n\24\3\24\5\24\u010e\n\24\3\25\3\25")
        buf.write("\5\25\u0112\n\25\3\26\3\26\7\26\u0116\n\26\f\26\16\26")
        buf.write("\u0119\13\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3!\3!\3!\3!\3")
        buf.write("\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\3$\3$\3")
        buf.write("$\3$\3$\3$\3$\3%\3%\3%\3%\3%\3%\3%\3&\3&\3&\3&\3&\3\'")
        buf.write("\3\'\3\'\3\'\3\'\3\'\3(\3(\3(\3(\3)\3)\3)\3)\3*\3*\3*")
        buf.write("\3*\3*\3*\3*\3*\3*\3*\3*\3*\3+\3+\3+\3+\3+\3+\3+\3+\3")
        buf.write("+\3+\3+\3,\3,\3,\3,\3-\3-\3-\3.\3.\3.\3.\3.\3/\3/\3\60")
        buf.write("\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65")
        buf.write("\3\65\3\66\3\66\3\66\3\67\3\67\38\38\38\39\39\3:\3:\3")
        buf.write(":\3;\3;\3;\3<\3<\3<\3<\3=\3=\3>\3>\3>\3?\3?\3?\3@\3@\3")
        buf.write("A\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3F\3F\3G\3G\3H\3H\3I\3")
        buf.write("I\3J\3J\3K\3K\7K\u01f2\nK\fK\16K\u01f5\13K\3L\6L\u01f8")
        buf.write("\nL\rL\16L\u01f9\3L\3L\3M\3M\3M\3N\3N\7N\u0203\nN\fN\16")
        buf.write("N\u0206\13N\3N\3N\3O\3O\7O\u020c\nO\fO\16O\u020f\13O\3")
        buf.write("O\3O\3O\3\u00d3\2P\3\3\5\2\7\2\t\2\13\2\r\2\17\2\21\2")
        buf.write("\23\2\25\2\27\2\31\2\33\4\35\2\37\2!\2#\2%\5\'\6)\7+\b")
        buf.write("-\t/\n\61\13\63\f\65\r\67\169\17;\20=\21?\22A\23C\24E")
        buf.write("\25G\26I\27K\30M\31O\32Q\33S\34U\35W\36Y\37[ ]!_\"a#c")
        buf.write("$e%g&i\'k(m)o*q+s,u-w.y/{\60}\61\177\62\u0081\63\u0083")
        buf.write("\64\u0085\65\u0087\66\u0089\67\u008b8\u008d9\u008f:\u0091")
        buf.write(";\u0093<\u0095=\u0097>\u0099?\u009b@\u009dA\3\2\17\4\2")
        buf.write("\62;aa\3\2c|\3\2C\\\5\2C\\aac|\4\2GGgg\b\2))ddhhppttv")
        buf.write("v\t\2))^^ddhhppttvv\7\2\n\f\16\17$$))^^\4\2DDdd\4\2ZZ")
        buf.write("zz\6\2&&C\\`ac|\6\2\62;C\\aac|\5\2\13\f\16\17\"\"\2\u021d")
        buf.write("\2\3\3\2\2\2\2\33\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3")
        buf.write("\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2")
        buf.write("\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3")
        buf.write("\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E")
        buf.write("\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2")
        buf.write("O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2")
        buf.write("\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2")
        buf.write("\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2")
        buf.write("\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2\2u\3")
        buf.write("\2\2\2\2w\3\2\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177")
        buf.write("\3\2\2\2\2\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2")
        buf.write("\2\2\u0087\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d")
        buf.write("\3\2\2\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2")
        buf.write("\2\2\u0095\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b")
        buf.write("\3\2\2\2\2\u009d\3\2\2\2\3\u009f\3\2\2\2\5\u00a4\3\2\2")
        buf.write("\2\7\u00a6\3\2\2\2\t\u00a8\3\2\2\2\13\u00aa\3\2\2\2\r")
        buf.write("\u00ac\3\2\2\2\17\u00b5\3\2\2\2\21\u00bb\3\2\2\2\23\u00bd")
        buf.write("\3\2\2\2\25\u00c2\3\2\2\2\27\u00c5\3\2\2\2\31\u00cb\3")
        buf.write("\2\2\2\33\u00cd\3\2\2\2\35\u00db\3\2\2\2\37\u00e1\3\2")
        buf.write("\2\2!\u00e9\3\2\2\2#\u00f0\3\2\2\2%\u00fe\3\2\2\2\'\u0101")
        buf.write("\3\2\2\2)\u0111\3\2\2\2+\u0113\3\2\2\2-\u011d\3\2\2\2")
        buf.write("/\u0123\3\2\2\2\61\u012c\3\2\2\2\63\u012f\3\2\2\2\65\u0136")
        buf.write("\3\2\2\2\67\u013b\3\2\2\29\u0143\3\2\2\2;\u0148\3\2\2")
        buf.write("\2=\u014e\3\2\2\2?\u0154\3\2\2\2A\u0157\3\2\2\2C\u015b")
        buf.write("\3\2\2\2E\u0161\3\2\2\2G\u0169\3\2\2\2I\u0170\3\2\2\2")
        buf.write("K\u0177\3\2\2\2M\u017c\3\2\2\2O\u0182\3\2\2\2Q\u0186\3")
        buf.write("\2\2\2S\u018a\3\2\2\2U\u0196\3\2\2\2W\u01a1\3\2\2\2Y\u01a5")
        buf.write("\3\2\2\2[\u01a8\3\2\2\2]\u01ad\3\2\2\2_\u01af\3\2\2\2")
        buf.write("a\u01b1\3\2\2\2c\u01b3\3\2\2\2e\u01b5\3\2\2\2g\u01b7\3")
        buf.write("\2\2\2i\u01b9\3\2\2\2k\u01bc\3\2\2\2m\u01bf\3\2\2\2o\u01c1")
        buf.write("\3\2\2\2q\u01c4\3\2\2\2s\u01c6\3\2\2\2u\u01c9\3\2\2\2")
        buf.write("w\u01cc\3\2\2\2y\u01d0\3\2\2\2{\u01d2\3\2\2\2}\u01d5\3")
        buf.write("\2\2\2\177\u01d8\3\2\2\2\u0081\u01da\3\2\2\2\u0083\u01dd")
        buf.write("\3\2\2\2\u0085\u01df\3\2\2\2\u0087\u01e1\3\2\2\2\u0089")
        buf.write("\u01e3\3\2\2\2\u008b\u01e5\3\2\2\2\u008d\u01e7\3\2\2\2")
        buf.write("\u008f\u01e9\3\2\2\2\u0091\u01eb\3\2\2\2\u0093\u01ed\3")
        buf.write("\2\2\2\u0095\u01ef\3\2\2\2\u0097\u01f7\3\2\2\2\u0099\u01fd")
        buf.write("\3\2\2\2\u009b\u0200\3\2\2\2\u009d\u0209\3\2\2\2\u009f")
        buf.write("\u00a0\7o\2\2\u00a0\u00a1\7c\2\2\u00a1\u00a2\7k\2\2\u00a2")
        buf.write("\u00a3\7p\2\2\u00a3\4\3\2\2\2\u00a4\u00a5\t\2\2\2\u00a5")
        buf.write("\6\3\2\2\2\u00a6\u00a7\t\3\2\2\u00a7\b\3\2\2\2\u00a8\u00a9")
        buf.write("\t\4\2\2\u00a9\n\3\2\2\2\u00aa\u00ab\t\5\2\2\u00ab\f\3")
        buf.write("\2\2\2\u00ac\u00ae\t\6\2\2\u00ad\u00af\7/\2\2\u00ae\u00ad")
        buf.write("\3\2\2\2\u00ae\u00af\3\2\2\2\u00af\u00b1\3\2\2\2\u00b0")
        buf.write("\u00b2\5\5\3\2\u00b1\u00b0\3\2\2\2\u00b2\u00b3\3\2\2\2")
        buf.write("\u00b3\u00b1\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\16\3\2")
        buf.write("\2\2\u00b5\u00b7\5\u0093J\2\u00b6\u00b8\5\5\3\2\u00b7")
        buf.write("\u00b6\3\2\2\2\u00b8\u00b9\3\2\2\2\u00b9\u00b7\3\2\2\2")
        buf.write("\u00b9\u00ba\3\2\2\2\u00ba\20\3\2\2\2\u00bb\u00bc\7$\2")
        buf.write("\2\u00bc\22\3\2\2\2\u00bd\u00c0\7^\2\2\u00be\u00c1\n\7")
        buf.write("\2\2\u00bf\u00c1\7^\2\2\u00c0\u00be\3\2\2\2\u00c0\u00bf")
        buf.write("\3\2\2\2\u00c1\24\3\2\2\2\u00c2\u00c3\7)\2\2\u00c3\u00c4")
        buf.write("\7$\2\2\u00c4\26\3\2\2\2\u00c5\u00c6\7^\2\2\u00c6\u00c7")
        buf.write("\t\b\2\2\u00c7\30\3\2\2\2\u00c8\u00cc\n\t\2\2\u00c9\u00cc")
        buf.write("\5\27\f\2\u00ca\u00cc\5\25\13\2\u00cb\u00c8\3\2\2\2\u00cb")
        buf.write("\u00c9\3\2\2\2\u00cb\u00ca\3\2\2\2\u00cc\32\3\2\2\2\u00cd")
        buf.write("\u00ce\7%\2\2\u00ce\u00cf\7%\2\2\u00cf\u00d3\3\2\2\2\u00d0")
        buf.write("\u00d2\13\2\2\2\u00d1\u00d0\3\2\2\2\u00d2\u00d5\3\2\2")
        buf.write("\2\u00d3\u00d4\3\2\2\2\u00d3\u00d1\3\2\2\2\u00d4\u00d6")
        buf.write("\3\2\2\2\u00d5\u00d3\3\2\2\2\u00d6\u00d7\7%\2\2\u00d7")
        buf.write("\u00d8\7%\2\2\u00d8\u00d9\3\2\2\2\u00d9\u00da\b\16\2\2")
        buf.write("\u00da\34\3\2\2\2\u00db\u00dd\7\62\2\2\u00dc\u00de\5\5")
        buf.write("\3\2\u00dd\u00dc\3\2\2\2\u00de\u00df\3\2\2\2\u00df\u00dd")
        buf.write("\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0\36\3\2\2\2\u00e1\u00e2")
        buf.write("\7\62\2\2\u00e2\u00e4\t\n\2\2\u00e3\u00e5\4\62\63\2\u00e4")
        buf.write("\u00e3\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e4\3\2\2\2")
        buf.write("\u00e6\u00e7\3\2\2\2\u00e7 \3\2\2\2\u00e8\u00ea\7/\2\2")
        buf.write("\u00e9\u00e8\3\2\2\2\u00e9\u00ea\3\2\2\2\u00ea\u00ec\3")
        buf.write("\2\2\2\u00eb\u00ed\5\5\3\2\u00ec\u00eb\3\2\2\2\u00ed\u00ee")
        buf.write("\3\2\2\2\u00ee\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2\u00ef")
        buf.write("\"\3\2\2\2\u00f0\u00f1\7\62\2\2\u00f1\u00f4\t\13\2\2\u00f2")
        buf.write("\u00f5\5\t\5\2\u00f3\u00f5\5\5\3\2\u00f4\u00f2\3\2\2\2")
        buf.write("\u00f4\u00f3\3\2\2\2\u00f5\u00f6\3\2\2\2\u00f6\u00f4\3")
        buf.write("\2\2\2\u00f6\u00f7\3\2\2\2\u00f7$\3\2\2\2\u00f8\u00ff")
        buf.write("\5\35\17\2\u00f9\u00ff\5\37\20\2\u00fa\u00ff\5!\21\2\u00fb")
        buf.write("\u00fc\5#\22\2\u00fc\u00fd\b\23\3\2\u00fd\u00ff\3\2\2")
        buf.write("\2\u00fe\u00f8\3\2\2\2\u00fe\u00f9\3\2\2\2\u00fe\u00fa")
        buf.write("\3\2\2\2\u00fe\u00fb\3\2\2\2\u00ff&\3\2\2\2\u0100\u0102")
        buf.write("\7/\2\2\u0101\u0100\3\2\2\2\u0101\u0102\3\2\2\2\u0102")
        buf.write("\u0104\3\2\2\2\u0103\u0105\5\5\3\2\u0104\u0103\3\2\2\2")
        buf.write("\u0105\u0106\3\2\2\2\u0106\u0104\3\2\2\2\u0106\u0107\3")
        buf.write("\2\2\2\u0107\u010d\3\2\2\2\u0108\u010a\5\17\b\2\u0109")
        buf.write("\u010b\5\r\7\2\u010a\u0109\3\2\2\2\u010a\u010b\3\2\2\2")
        buf.write("\u010b\u010e\3\2\2\2\u010c\u010e\5\r\7\2\u010d\u0108\3")
        buf.write("\2\2\2\u010d\u010c\3\2\2\2\u010e(\3\2\2\2\u010f\u0112")
        buf.write("\59\35\2\u0110\u0112\5;\36\2\u0111\u010f\3\2\2\2\u0111")
        buf.write("\u0110\3\2\2\2\u0112*\3\2\2\2\u0113\u0117\5\21\t\2\u0114")
        buf.write("\u0116\5\31\r\2\u0115\u0114\3\2\2\2\u0116\u0119\3\2\2")
        buf.write("\2\u0117\u0115\3\2\2\2\u0117\u0118\3\2\2\2\u0118\u011a")
        buf.write("\3\2\2\2\u0119\u0117\3\2\2\2\u011a\u011b\5\21\t\2\u011b")
        buf.write("\u011c\b\26\4\2\u011c,\3\2\2\2\u011d\u011e\7D\2\2\u011e")
        buf.write("\u011f\7t\2\2\u011f\u0120\7g\2\2\u0120\u0121\7c\2\2\u0121")
        buf.write("\u0122\7m\2\2\u0122.\3\2\2\2\u0123\u0124\7E\2\2\u0124")
        buf.write("\u0125\7q\2\2\u0125\u0126\7p\2\2\u0126\u0127\7v\2\2\u0127")
        buf.write("\u0128\7k\2\2\u0128\u0129\7p\2\2\u0129\u012a\7w\2\2\u012a")
        buf.write("\u012b\7g\2\2\u012b\60\3\2\2\2\u012c\u012d\7K\2\2\u012d")
        buf.write("\u012e\7h\2\2\u012e\62\3\2\2\2\u012f\u0130\7G\2\2\u0130")
        buf.write("\u0131\7n\2\2\u0131\u0132\7u\2\2\u0132\u0133\7g\2\2\u0133")
        buf.write("\u0134\7k\2\2\u0134\u0135\7h\2\2\u0135\64\3\2\2\2\u0136")
        buf.write("\u0137\7G\2\2\u0137\u0138\7n\2\2\u0138\u0139\7u\2\2\u0139")
        buf.write("\u013a\7g\2\2\u013a\66\3\2\2\2\u013b\u013c\7H\2\2\u013c")
        buf.write("\u013d\7q\2\2\u013d\u013e\7t\2\2\u013e\u013f\7g\2\2\u013f")
        buf.write("\u0140\7c\2\2\u0140\u0141\7e\2\2\u0141\u0142\7j\2\2\u0142")
        buf.write("8\3\2\2\2\u0143\u0144\7V\2\2\u0144\u0145\7t\2\2\u0145")
        buf.write("\u0146\7w\2\2\u0146\u0147\7g\2\2\u0147:\3\2\2\2\u0148")
        buf.write("\u0149\7H\2\2\u0149\u014a\7c\2\2\u014a\u014b\7n\2\2\u014b")
        buf.write("\u014c\7u\2\2\u014c\u014d\7g\2\2\u014d<\3\2\2\2\u014e")
        buf.write("\u014f\7C\2\2\u014f\u0150\7t\2\2\u0150\u0151\7t\2\2\u0151")
        buf.write("\u0152\7c\2\2\u0152\u0153\7{\2\2\u0153>\3\2\2\2\u0154")
        buf.write("\u0155\7K\2\2\u0155\u0156\7p\2\2\u0156@\3\2\2\2\u0157")
        buf.write("\u0158\7K\2\2\u0158\u0159\7p\2\2\u0159\u015a\7v\2\2\u015a")
        buf.write("B\3\2\2\2\u015b\u015c\7H\2\2\u015c\u015d\7n\2\2\u015d")
        buf.write("\u015e\7q\2\2\u015e\u015f\7c\2\2\u015f\u0160\7v\2\2\u0160")
        buf.write("D\3\2\2\2\u0161\u0162\7D\2\2\u0162\u0163\7q\2\2\u0163")
        buf.write("\u0164\7q\2\2\u0164\u0165\7n\2\2\u0165\u0166\7g\2\2\u0166")
        buf.write("\u0167\7c\2\2\u0167\u0168\7p\2\2\u0168F\3\2\2\2\u0169")
        buf.write("\u016a\7U\2\2\u016a\u016b\7v\2\2\u016b\u016c\7t\2\2\u016c")
        buf.write("\u016d\7k\2\2\u016d\u016e\7p\2\2\u016e\u016f\7i\2\2\u016f")
        buf.write("H\3\2\2\2\u0170\u0171\7T\2\2\u0171\u0172\7g\2\2\u0172")
        buf.write("\u0173\7v\2\2\u0173\u0174\7w\2\2\u0174\u0175\7t\2\2\u0175")
        buf.write("\u0176\7p\2\2\u0176J\3\2\2\2\u0177\u0178\7P\2\2\u0178")
        buf.write("\u0179\7w\2\2\u0179\u017a\7n\2\2\u017a\u017b\7n\2\2\u017b")
        buf.write("L\3\2\2\2\u017c\u017d\7E\2\2\u017d\u017e\7n\2\2\u017e")
        buf.write("\u017f\7c\2\2\u017f\u0180\7u\2\2\u0180\u0181\7u\2\2\u0181")
        buf.write("N\3\2\2\2\u0182\u0183\7X\2\2\u0183\u0184\7c\2\2\u0184")
        buf.write("\u0185\7n\2\2\u0185P\3\2\2\2\u0186\u0187\7X\2\2\u0187")
        buf.write("\u0188\7c\2\2\u0188\u0189\7t\2\2\u0189R\3\2\2\2\u018a")
        buf.write("\u018b\7E\2\2\u018b\u018c\7q\2\2\u018c\u018d\7p\2\2\u018d")
        buf.write("\u018e\7u\2\2\u018e\u018f\7v\2\2\u018f\u0190\7t\2\2\u0190")
        buf.write("\u0191\7w\2\2\u0191\u0192\7e\2\2\u0192\u0193\7v\2\2\u0193")
        buf.write("\u0194\7q\2\2\u0194\u0195\7t\2\2\u0195T\3\2\2\2\u0196")
        buf.write("\u0197\7F\2\2\u0197\u0198\7g\2\2\u0198\u0199\7u\2\2\u0199")
        buf.write("\u019a\7v\2\2\u019a\u019b\7t\2\2\u019b\u019c\7w\2\2\u019c")
        buf.write("\u019d\7e\2\2\u019d\u019e\7v\2\2\u019e\u019f\7q\2\2\u019f")
        buf.write("\u01a0\7t\2\2\u01a0V\3\2\2\2\u01a1\u01a2\7P\2\2\u01a2")
        buf.write("\u01a3\7g\2\2\u01a3\u01a4\7y\2\2\u01a4X\3\2\2\2\u01a5")
        buf.write("\u01a6\7D\2\2\u01a6\u01a7\7{\2\2\u01a7Z\3\2\2\2\u01a8")
        buf.write("\u01a9\7U\2\2\u01a9\u01aa\7g\2\2\u01aa\u01ab\7n\2\2\u01ab")
        buf.write("\u01ac\7h\2\2\u01ac\\\3\2\2\2\u01ad\u01ae\7&\2\2\u01ae")
        buf.write("^\3\2\2\2\u01af\u01b0\7-\2\2\u01b0`\3\2\2\2\u01b1\u01b2")
        buf.write("\7/\2\2\u01b2b\3\2\2\2\u01b3\u01b4\7,\2\2\u01b4d\3\2\2")
        buf.write("\2\u01b5\u01b6\7\61\2\2\u01b6f\3\2\2\2\u01b7\u01b8\7\'")
        buf.write("\2\2\u01b8h\3\2\2\2\u01b9\u01ba\7?\2\2\u01ba\u01bb\7?")
        buf.write("\2\2\u01bbj\3\2\2\2\u01bc\u01bd\7#\2\2\u01bd\u01be\7?")
        buf.write("\2\2\u01bel\3\2\2\2\u01bf\u01c0\7@\2\2\u01c0n\3\2\2\2")
        buf.write("\u01c1\u01c2\7@\2\2\u01c2\u01c3\7?\2\2\u01c3p\3\2\2\2")
        buf.write("\u01c4\u01c5\7>\2\2\u01c5r\3\2\2\2\u01c6\u01c7\7>\2\2")
        buf.write("\u01c7\u01c8\7?\2\2\u01c8t\3\2\2\2\u01c9\u01ca\7-\2\2")
        buf.write("\u01ca\u01cb\7\60\2\2\u01cbv\3\2\2\2\u01cc\u01cd\7?\2")
        buf.write("\2\u01cd\u01ce\7?\2\2\u01ce\u01cf\7\60\2\2\u01cfx\3\2")
        buf.write("\2\2\u01d0\u01d1\7#\2\2\u01d1z\3\2\2\2\u01d2\u01d3\7(")
        buf.write("\2\2\u01d3\u01d4\7(\2\2\u01d4|\3\2\2\2\u01d5\u01d6\7~")
        buf.write("\2\2\u01d6\u01d7\7~\2\2\u01d7~\3\2\2\2\u01d8\u01d9\7?")
        buf.write("\2\2\u01d9\u0080\3\2\2\2\u01da\u01db\7<\2\2\u01db\u01dc")
        buf.write("\7<\2\2\u01dc\u0082\3\2\2\2\u01dd\u01de\7*\2\2\u01de\u0084")
        buf.write("\3\2\2\2\u01df\u01e0\7+\2\2\u01e0\u0086\3\2\2\2\u01e1")
        buf.write("\u01e2\7]\2\2\u01e2\u0088\3\2\2\2\u01e3\u01e4\7_\2\2\u01e4")
        buf.write("\u008a\3\2\2\2\u01e5\u01e6\7}\2\2\u01e6\u008c\3\2\2\2")
        buf.write("\u01e7\u01e8\7\177\2\2\u01e8\u008e\3\2\2\2\u01e9\u01ea")
        buf.write("\7=\2\2\u01ea\u0090\3\2\2\2\u01eb\u01ec\7.\2\2\u01ec\u0092")
        buf.write("\3\2\2\2\u01ed\u01ee\7\60\2\2\u01ee\u0094\3\2\2\2\u01ef")
        buf.write("\u01f3\t\f\2\2\u01f0\u01f2\t\r\2\2\u01f1\u01f0\3\2\2\2")
        buf.write("\u01f2\u01f5\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f3\u01f4\3")
        buf.write("\2\2\2\u01f4\u0096\3\2\2\2\u01f5\u01f3\3\2\2\2\u01f6\u01f8")
        buf.write("\t\16\2\2\u01f7\u01f6\3\2\2\2\u01f8\u01f9\3\2\2\2\u01f9")
        buf.write("\u01f7\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u01fb\3\2\2\2")
        buf.write("\u01fb\u01fc\bL\2\2\u01fc\u0098\3\2\2\2\u01fd\u01fe\13")
        buf.write("\2\2\2\u01fe\u01ff\bM\5\2\u01ff\u009a\3\2\2\2\u0200\u0204")
        buf.write("\5\21\t\2\u0201\u0203\5\31\r\2\u0202\u0201\3\2\2\2\u0203")
        buf.write("\u0206\3\2\2\2\u0204\u0202\3\2\2\2\u0204\u0205\3\2\2\2")
        buf.write("\u0205\u0207\3\2\2\2\u0206\u0204\3\2\2\2\u0207\u0208\b")
        buf.write("N\6\2\u0208\u009c\3\2\2\2\u0209\u020d\5\21\t\2\u020a\u020c")
        buf.write("\5\31\r\2\u020b\u020a\3\2\2\2\u020c\u020f\3\2\2\2\u020d")
        buf.write("\u020b\3\2\2\2\u020d\u020e\3\2\2\2\u020e\u0210\3\2\2\2")
        buf.write("\u020f\u020d\3\2\2\2\u0210\u0211\5\23\n\2\u0211\u0212")
        buf.write("\bO\7\2\u0212\u009e\3\2\2\2\32\2\u00ae\u00b3\u00b9\u00c0")
        buf.write("\u00cb\u00d3\u00df\u00e6\u00e9\u00ee\u00f4\u00f6\u00fe")
        buf.write("\u0101\u0106\u010a\u010d\u0111\u0117\u01f3\u01f9\u0204")
        buf.write("\u020d\b\b\2\2\3\23\2\3\26\3\3M\4\3N\5\3O\6")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    BLOCK_COMMENT = 2
    INTLIT = 3
    FLOATLIT = 4
    BOOLLIT = 5
    STRLIT = 6
    BREAK = 7
    CONTINUE = 8
    IF = 9
    ELSEIF = 10
    ELSE = 11
    FOREACH = 12
    TRUE = 13
    FALSE = 14
    ARRAY = 15
    IN = 16
    INT = 17
    FLOAT = 18
    BOOLEAN = 19
    STRING = 20
    RETURN = 21
    NULL = 22
    CLASS = 23
    VAL = 24
    VAR = 25
    CONSTRUCTOR = 26
    DESTRUCTOR = 27
    NEW = 28
    BY = 29
    SELF = 30
    STATIC = 31
    ADD = 32
    SUB = 33
    MUL = 34
    DIV = 35
    MOD = 36
    EQ = 37
    NEQ = 38
    GT = 39
    GTE = 40
    LT = 41
    LTE = 42
    SADD = 43
    SEQ = 44
    NOT = 45
    AND = 46
    OR = 47
    ASSIGN = 48
    SCOPE = 49
    LB = 50
    RB = 51
    LSB = 52
    RSB = 53
    LCB = 54
    RCB = 55
    SM = 56
    CM = 57
    DOT = 58
    ID = 59
    WS = 60
    ERROR_CHAR = 61
    UNCLOSE_STRING = 62
    ILLEGAL_ESCAPE = 63

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'main'", "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", 
            "'Foreach'", "'True'", "'False'", "'Array'", "'In'", "'Int'", 
            "'Float'", "'Boolean'", "'String'", "'Return'", "'Null'", "'Class'", 
            "'Val'", "'Var'", "'Constructor'", "'Destructor'", "'New'", 
            "'By'", "'Self'", "'$'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'=='", "'!='", "'>'", "'>='", "'<'", "'<='", "'+.'", "'==.'", 
            "'!'", "'&&'", "'||'", "'='", "'::'", "'('", "')'", "'['", "']'", 
            "'{'", "'}'", "';'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "BLOCK_COMMENT", "INTLIT", "FLOATLIT", "BOOLLIT", "STRLIT", 
            "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", 
            "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
            "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
            "NEW", "BY", "SELF", "STATIC", "ADD", "SUB", "MUL", "DIV", "MOD", 
            "EQ", "NEQ", "GT", "GTE", "LT", "LTE", "SADD", "SEQ", "NOT", 
            "AND", "OR", "ASSIGN", "SCOPE", "LB", "RB", "LSB", "RSB", "LCB", 
            "RCB", "SM", "CM", "DOT", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "DIGIT", "LOWERCASE", "UPERCASE", "ALPHABET", 
                  "SCIENTIFIC", "DECIMAL_POINT", "DOUBLE_QUOTE", "ILLEGAL_STRING", 
                  "QUOTE_IN_STR", "ESC_SEQ", "VALID_STRING", "BLOCK_COMMENT", 
                  "OCTAL", "BINARY", "DECIMAL", "HEXADECIMAL", "INTLIT", 
                  "FLOATLIT", "BOOLLIT", "STRLIT", "BREAK", "CONTINUE", 
                  "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", 
                  "IN", "INT", "FLOAT", "BOOLEAN", "STRING", "RETURN", "NULL", 
                  "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", "NEW", 
                  "BY", "SELF", "STATIC", "ADD", "SUB", "MUL", "DIV", "MOD", 
                  "EQ", "NEQ", "GT", "GTE", "LT", "LTE", "SADD", "SEQ", 
                  "NOT", "AND", "OR", "ASSIGN", "SCOPE", "LB", "RB", "LSB", 
                  "RSB", "LCB", "RCB", "SM", "CM", "DOT", "ID", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[17] = self.INTLIT_action 
            actions[20] = self.STRLIT_action 
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

                    raise UncloseString(self.text[1:])
                
     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:
            	
            		illegal_str = str(self.text)
            		raise IllegalEscape(illegal_str[1:])
            	
     


