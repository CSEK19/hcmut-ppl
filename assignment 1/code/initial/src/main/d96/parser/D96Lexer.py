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
        buf.write("\u0247\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\3\2\3\2\3\2\3\3\3\3\5\3\u00b1\n\3\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6")
        buf.write("\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3")
        buf.write("\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3")
        buf.write("\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24")
        buf.write("\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31")
        buf.write("\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3")
        buf.write("\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3\'\3")
        buf.write("(\3(\3(\3)\3)\3)\3)\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3.\3")
        buf.write(".\3/\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64")
        buf.write("\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:")
        buf.write("\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\5B\u019b")
        buf.write("\nB\3B\6B\u019e\nB\rB\16B\u019f\3C\3C\7C\u01a4\nC\fC\16")
        buf.write("C\u01a7\13C\3D\3D\3E\3E\3E\5E\u01ae\nE\3F\3F\3F\3G\3G")
        buf.write("\3G\3H\3H\3H\5H\u01b9\nH\3I\3I\3I\3I\7I\u01bf\nI\fI\16")
        buf.write("I\u01c2\13I\3I\3I\3I\3I\3I\3J\3J\3J\3J\5J\u01cd\nJ\3J")
        buf.write("\7J\u01d0\nJ\fJ\16J\u01d3\13J\5J\u01d5\nJ\3K\3K\3K\3K")
        buf.write("\3K\5K\u01dc\nK\3K\7K\u01df\nK\fK\16K\u01e2\13K\5K\u01e4")
        buf.write("\nK\3L\3L\3L\3L\7L\u01ea\nL\fL\16L\u01ed\13L\3L\5L\u01f0")
        buf.write("\nL\3M\3M\3M\3M\3M\5M\u01f7\nM\3M\5M\u01fa\nM\3M\3M\5")
        buf.write("M\u01fe\nM\7M\u0200\nM\fM\16M\u0203\13M\5M\u0205\nM\3")
        buf.write("N\3N\3N\3N\5N\u020b\nN\3N\3N\3O\5O\u0210\nO\3O\3O\5O\u0214")
        buf.write("\nO\3O\5O\u0217\nO\3O\3O\3P\3P\7P\u021d\nP\fP\16P\u0220")
        buf.write("\13P\3P\3P\3Q\3Q\7Q\u0226\nQ\fQ\16Q\u0229\13Q\3R\6R\u022c")
        buf.write("\nR\rR\16R\u022d\3R\3R\3S\3S\3S\3T\3T\7T\u0237\nT\fT\16")
        buf.write("T\u023a\13T\3T\3T\3U\3U\7U\u0240\nU\fU\16U\u0243\13U\3")
        buf.write("U\3U\3U\3\u01c0\2V\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'")
        buf.write("\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ")
        buf.write("?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g")
        buf.write("\65i\66k\67m8o9q\2s\2u\2w\2y\2{\2}\2\177\2\u0081\2\u0083")
        buf.write("\2\u0085\2\u0087\2\u0089\2\u008b\2\u008d\2\u008f\2\u0091")
        buf.write(":\u0093\2\u0095\2\u0097\2\u0099\2\u009b;\u009d<\u009f")
        buf.write("=\u00a1>\u00a3?\u00a5@\u00a7A\u00a9B\3\2\23\3\2\62;\3")
        buf.write("\2\62\63\3\2\629\3\2\639\3\2\63;\3\2c|\3\2C\\\4\2CHaa")
        buf.write("\5\2C\\aac|\4\2GGgg\b\2))ddhhppttvv\t\2))^^ddhhppttvv")
        buf.write("\6\2\n\f\16\17$$^^\4\2DDdd\4\2ZZzz\6\2\62;C\\aac|\5\2")
        buf.write("\13\f\16\17\"\"\2\u0253\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write("\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2")
        buf.write("\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2")
        buf.write("\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2")
        buf.write("!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2")
        buf.write("\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3")
        buf.write("\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2")
        buf.write("\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2")
        buf.write("\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2")
        buf.write("\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3")
        buf.write("\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c")
        buf.write("\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2")
        buf.write("m\3\2\2\2\2o\3\2\2\2\2\u0091\3\2\2\2\2\u009b\3\2\2\2\2")
        buf.write("\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3")
        buf.write("\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2\2\2\u00a9\3\2\2")
        buf.write("\2\3\u00ab\3\2\2\2\5\u00b0\3\2\2\2\7\u00b2\3\2\2\2\t\u00b8")
        buf.write("\3\2\2\2\13\u00c1\3\2\2\2\r\u00c4\3\2\2\2\17\u00cb\3\2")
        buf.write("\2\2\21\u00d0\3\2\2\2\23\u00d8\3\2\2\2\25\u00dd\3\2\2")
        buf.write("\2\27\u00e3\3\2\2\2\31\u00e9\3\2\2\2\33\u00ec\3\2\2\2")
        buf.write("\35\u00f0\3\2\2\2\37\u00f6\3\2\2\2!\u00fe\3\2\2\2#\u0105")
        buf.write("\3\2\2\2%\u010c\3\2\2\2\'\u0111\3\2\2\2)\u0117\3\2\2\2")
        buf.write("+\u011b\3\2\2\2-\u011f\3\2\2\2/\u012b\3\2\2\2\61\u0136")
        buf.write("\3\2\2\2\63\u013a\3\2\2\2\65\u013d\3\2\2\2\67\u0142\3")
        buf.write("\2\2\29\u0144\3\2\2\2;\u0146\3\2\2\2=\u0148\3\2\2\2?\u014a")
        buf.write("\3\2\2\2A\u014c\3\2\2\2C\u014e\3\2\2\2E\u0151\3\2\2\2")
        buf.write("G\u0154\3\2\2\2I\u0156\3\2\2\2K\u0159\3\2\2\2M\u015b\3")
        buf.write("\2\2\2O\u015e\3\2\2\2Q\u0161\3\2\2\2S\u0165\3\2\2\2U\u0167")
        buf.write("\3\2\2\2W\u016a\3\2\2\2Y\u016d\3\2\2\2[\u016f\3\2\2\2")
        buf.write("]\u0171\3\2\2\2_\u0174\3\2\2\2a\u0176\3\2\2\2c\u0178\3")
        buf.write("\2\2\2e\u017a\3\2\2\2g\u017c\3\2\2\2i\u017e\3\2\2\2k\u0180")
        buf.write("\3\2\2\2m\u0182\3\2\2\2o\u0184\3\2\2\2q\u0186\3\2\2\2")
        buf.write("s\u0188\3\2\2\2u\u018a\3\2\2\2w\u018c\3\2\2\2y\u018e\3")
        buf.write("\2\2\2{\u0190\3\2\2\2}\u0192\3\2\2\2\177\u0194\3\2\2\2")
        buf.write("\u0081\u0196\3\2\2\2\u0083\u0198\3\2\2\2\u0085\u01a1\3")
        buf.write("\2\2\2\u0087\u01a8\3\2\2\2\u0089\u01aa\3\2\2\2\u008b\u01af")
        buf.write("\3\2\2\2\u008d\u01b2\3\2\2\2\u008f\u01b8\3\2\2\2\u0091")
        buf.write("\u01ba\3\2\2\2\u0093\u01c8\3\2\2\2\u0095\u01d6\3\2\2\2")
        buf.write("\u0097\u01ef\3\2\2\2\u0099\u01f1\3\2\2\2\u009b\u020a\3")
        buf.write("\2\2\2\u009d\u020f\3\2\2\2\u009f\u021a\3\2\2\2\u00a1\u0223")
        buf.write("\3\2\2\2\u00a3\u022b\3\2\2\2\u00a5\u0231\3\2\2\2\u00a7")
        buf.write("\u0234\3\2\2\2\u00a9\u023d\3\2\2\2\u00ab\u00ac\7\60\2")
        buf.write("\2\u00ac\u00ad\7\60\2\2\u00ad\4\3\2\2\2\u00ae\u00b1\5")
        buf.write("\23\n\2\u00af\u00b1\5\25\13\2\u00b0\u00ae\3\2\2\2\u00b0")
        buf.write("\u00af\3\2\2\2\u00b1\6\3\2\2\2\u00b2\u00b3\7D\2\2\u00b3")
        buf.write("\u00b4\7t\2\2\u00b4\u00b5\7g\2\2\u00b5\u00b6\7c\2\2\u00b6")
        buf.write("\u00b7\7m\2\2\u00b7\b\3\2\2\2\u00b8\u00b9\7E\2\2\u00b9")
        buf.write("\u00ba\7q\2\2\u00ba\u00bb\7p\2\2\u00bb\u00bc\7v\2\2\u00bc")
        buf.write("\u00bd\7k\2\2\u00bd\u00be\7p\2\2\u00be\u00bf\7w\2\2\u00bf")
        buf.write("\u00c0\7g\2\2\u00c0\n\3\2\2\2\u00c1\u00c2\7K\2\2\u00c2")
        buf.write("\u00c3\7h\2\2\u00c3\f\3\2\2\2\u00c4\u00c5\7G\2\2\u00c5")
        buf.write("\u00c6\7n\2\2\u00c6\u00c7\7u\2\2\u00c7\u00c8\7g\2\2\u00c8")
        buf.write("\u00c9\7k\2\2\u00c9\u00ca\7h\2\2\u00ca\16\3\2\2\2\u00cb")
        buf.write("\u00cc\7G\2\2\u00cc\u00cd\7n\2\2\u00cd\u00ce\7u\2\2\u00ce")
        buf.write("\u00cf\7g\2\2\u00cf\20\3\2\2\2\u00d0\u00d1\7H\2\2\u00d1")
        buf.write("\u00d2\7q\2\2\u00d2\u00d3\7t\2\2\u00d3\u00d4\7g\2\2\u00d4")
        buf.write("\u00d5\7c\2\2\u00d5\u00d6\7e\2\2\u00d6\u00d7\7j\2\2\u00d7")
        buf.write("\22\3\2\2\2\u00d8\u00d9\7V\2\2\u00d9\u00da\7t\2\2\u00da")
        buf.write("\u00db\7w\2\2\u00db\u00dc\7g\2\2\u00dc\24\3\2\2\2\u00dd")
        buf.write("\u00de\7H\2\2\u00de\u00df\7c\2\2\u00df\u00e0\7n\2\2\u00e0")
        buf.write("\u00e1\7u\2\2\u00e1\u00e2\7g\2\2\u00e2\26\3\2\2\2\u00e3")
        buf.write("\u00e4\7C\2\2\u00e4\u00e5\7t\2\2\u00e5\u00e6\7t\2\2\u00e6")
        buf.write("\u00e7\7c\2\2\u00e7\u00e8\7{\2\2\u00e8\30\3\2\2\2\u00e9")
        buf.write("\u00ea\7K\2\2\u00ea\u00eb\7p\2\2\u00eb\32\3\2\2\2\u00ec")
        buf.write("\u00ed\7K\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef\7v\2\2\u00ef")
        buf.write("\34\3\2\2\2\u00f0\u00f1\7H\2\2\u00f1\u00f2\7n\2\2\u00f2")
        buf.write("\u00f3\7q\2\2\u00f3\u00f4\7c\2\2\u00f4\u00f5\7v\2\2\u00f5")
        buf.write("\36\3\2\2\2\u00f6\u00f7\7D\2\2\u00f7\u00f8\7q\2\2\u00f8")
        buf.write("\u00f9\7q\2\2\u00f9\u00fa\7n\2\2\u00fa\u00fb\7g\2\2\u00fb")
        buf.write("\u00fc\7c\2\2\u00fc\u00fd\7p\2\2\u00fd \3\2\2\2\u00fe")
        buf.write("\u00ff\7U\2\2\u00ff\u0100\7v\2\2\u0100\u0101\7t\2\2\u0101")
        buf.write("\u0102\7k\2\2\u0102\u0103\7p\2\2\u0103\u0104\7i\2\2\u0104")
        buf.write("\"\3\2\2\2\u0105\u0106\7T\2\2\u0106\u0107\7g\2\2\u0107")
        buf.write("\u0108\7v\2\2\u0108\u0109\7w\2\2\u0109\u010a\7t\2\2\u010a")
        buf.write("\u010b\7p\2\2\u010b$\3\2\2\2\u010c\u010d\7P\2\2\u010d")
        buf.write("\u010e\7w\2\2\u010e\u010f\7n\2\2\u010f\u0110\7n\2\2\u0110")
        buf.write("&\3\2\2\2\u0111\u0112\7E\2\2\u0112\u0113\7n\2\2\u0113")
        buf.write("\u0114\7c\2\2\u0114\u0115\7u\2\2\u0115\u0116\7u\2\2\u0116")
        buf.write("(\3\2\2\2\u0117\u0118\7X\2\2\u0118\u0119\7c\2\2\u0119")
        buf.write("\u011a\7n\2\2\u011a*\3\2\2\2\u011b\u011c\7X\2\2\u011c")
        buf.write("\u011d\7c\2\2\u011d\u011e\7t\2\2\u011e,\3\2\2\2\u011f")
        buf.write("\u0120\7E\2\2\u0120\u0121\7q\2\2\u0121\u0122\7p\2\2\u0122")
        buf.write("\u0123\7u\2\2\u0123\u0124\7v\2\2\u0124\u0125\7t\2\2\u0125")
        buf.write("\u0126\7w\2\2\u0126\u0127\7e\2\2\u0127\u0128\7v\2\2\u0128")
        buf.write("\u0129\7q\2\2\u0129\u012a\7t\2\2\u012a.\3\2\2\2\u012b")
        buf.write("\u012c\7F\2\2\u012c\u012d\7g\2\2\u012d\u012e\7u\2\2\u012e")
        buf.write("\u012f\7v\2\2\u012f\u0130\7t\2\2\u0130\u0131\7w\2\2\u0131")
        buf.write("\u0132\7e\2\2\u0132\u0133\7v\2\2\u0133\u0134\7q\2\2\u0134")
        buf.write("\u0135\7t\2\2\u0135\60\3\2\2\2\u0136\u0137\7P\2\2\u0137")
        buf.write("\u0138\7g\2\2\u0138\u0139\7y\2\2\u0139\62\3\2\2\2\u013a")
        buf.write("\u013b\7D\2\2\u013b\u013c\7{\2\2\u013c\64\3\2\2\2\u013d")
        buf.write("\u013e\7U\2\2\u013e\u013f\7g\2\2\u013f\u0140\7n\2\2\u0140")
        buf.write("\u0141\7h\2\2\u0141\66\3\2\2\2\u0142\u0143\7&\2\2\u0143")
        buf.write("8\3\2\2\2\u0144\u0145\7-\2\2\u0145:\3\2\2\2\u0146\u0147")
        buf.write("\7/\2\2\u0147<\3\2\2\2\u0148\u0149\7,\2\2\u0149>\3\2\2")
        buf.write("\2\u014a\u014b\7\61\2\2\u014b@\3\2\2\2\u014c\u014d\7\'")
        buf.write("\2\2\u014dB\3\2\2\2\u014e\u014f\7?\2\2\u014f\u0150\7?")
        buf.write("\2\2\u0150D\3\2\2\2\u0151\u0152\7#\2\2\u0152\u0153\7?")
        buf.write("\2\2\u0153F\3\2\2\2\u0154\u0155\7@\2\2\u0155H\3\2\2\2")
        buf.write("\u0156\u0157\7@\2\2\u0157\u0158\7?\2\2\u0158J\3\2\2\2")
        buf.write("\u0159\u015a\7>\2\2\u015aL\3\2\2\2\u015b\u015c\7>\2\2")
        buf.write("\u015c\u015d\7?\2\2\u015dN\3\2\2\2\u015e\u015f\7-\2\2")
        buf.write("\u015f\u0160\7\60\2\2\u0160P\3\2\2\2\u0161\u0162\7?\2")
        buf.write("\2\u0162\u0163\7?\2\2\u0163\u0164\7\60\2\2\u0164R\3\2")
        buf.write("\2\2\u0165\u0166\7#\2\2\u0166T\3\2\2\2\u0167\u0168\7(")
        buf.write("\2\2\u0168\u0169\7(\2\2\u0169V\3\2\2\2\u016a\u016b\7~")
        buf.write("\2\2\u016b\u016c\7~\2\2\u016cX\3\2\2\2\u016d\u016e\7<")
        buf.write("\2\2\u016eZ\3\2\2\2\u016f\u0170\7?\2\2\u0170\\\3\2\2\2")
        buf.write("\u0171\u0172\7<\2\2\u0172\u0173\7<\2\2\u0173^\3\2\2\2")
        buf.write("\u0174\u0175\7*\2\2\u0175`\3\2\2\2\u0176\u0177\7+\2\2")
        buf.write("\u0177b\3\2\2\2\u0178\u0179\7]\2\2\u0179d\3\2\2\2\u017a")
        buf.write("\u017b\7_\2\2\u017bf\3\2\2\2\u017c\u017d\7}\2\2\u017d")
        buf.write("h\3\2\2\2\u017e\u017f\7\177\2\2\u017fj\3\2\2\2\u0180\u0181")
        buf.write("\7=\2\2\u0181l\3\2\2\2\u0182\u0183\7.\2\2\u0183n\3\2\2")
        buf.write("\2\u0184\u0185\7\60\2\2\u0185p\3\2\2\2\u0186\u0187\t\2")
        buf.write("\2\2\u0187r\3\2\2\2\u0188\u0189\t\3\2\2\u0189t\3\2\2\2")
        buf.write("\u018a\u018b\t\4\2\2\u018bv\3\2\2\2\u018c\u018d\t\5\2")
        buf.write("\2\u018dx\3\2\2\2\u018e\u018f\t\6\2\2\u018fz\3\2\2\2\u0190")
        buf.write("\u0191\t\7\2\2\u0191|\3\2\2\2\u0192\u0193\t\b\2\2\u0193")
        buf.write("~\3\2\2\2\u0194\u0195\t\t\2\2\u0195\u0080\3\2\2\2\u0196")
        buf.write("\u0197\t\n\2\2\u0197\u0082\3\2\2\2\u0198\u019a\t\13\2")
        buf.write("\2\u0199\u019b\7/\2\2\u019a\u0199\3\2\2\2\u019a\u019b")
        buf.write("\3\2\2\2\u019b\u019d\3\2\2\2\u019c\u019e\5q9\2\u019d\u019c")
        buf.write("\3\2\2\2\u019e\u019f\3\2\2\2\u019f\u019d\3\2\2\2\u019f")
        buf.write("\u01a0\3\2\2\2\u01a0\u0084\3\2\2\2\u01a1\u01a5\5o8\2\u01a2")
        buf.write("\u01a4\5q9\2\u01a3\u01a2\3\2\2\2\u01a4\u01a7\3\2\2\2\u01a5")
        buf.write("\u01a3\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6\u0086\3\2\2\2")
        buf.write("\u01a7\u01a5\3\2\2\2\u01a8\u01a9\7$\2\2\u01a9\u0088\3")
        buf.write("\2\2\2\u01aa\u01ad\7^\2\2\u01ab\u01ae\n\f\2\2\u01ac\u01ae")
        buf.write("\7^\2\2\u01ad\u01ab\3\2\2\2\u01ad\u01ac\3\2\2\2\u01ae")
        buf.write("\u008a\3\2\2\2\u01af\u01b0\7)\2\2\u01b0\u01b1\7$\2\2\u01b1")
        buf.write("\u008c\3\2\2\2\u01b2\u01b3\7^\2\2\u01b3\u01b4\t\r\2\2")
        buf.write("\u01b4\u008e\3\2\2\2\u01b5\u01b9\n\16\2\2\u01b6\u01b9")
        buf.write("\5\u008dG\2\u01b7\u01b9\5\u008bF\2\u01b8\u01b5\3\2\2\2")
        buf.write("\u01b8\u01b6\3\2\2\2\u01b8\u01b7\3\2\2\2\u01b9\u0090\3")
        buf.write("\2\2\2\u01ba\u01bb\7%\2\2\u01bb\u01bc\7%\2\2\u01bc\u01c0")
        buf.write("\3\2\2\2\u01bd\u01bf\13\2\2\2\u01be\u01bd\3\2\2\2\u01bf")
        buf.write("\u01c2\3\2\2\2\u01c0\u01c1\3\2\2\2\u01c0\u01be\3\2\2\2")
        buf.write("\u01c1\u01c3\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c3\u01c4\7")
        buf.write("%\2\2\u01c4\u01c5\7%\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c7")
        buf.write("\bI\2\2\u01c7\u0092\3\2\2\2\u01c8\u01d4\7\62\2\2\u01c9")
        buf.write("\u01d5\7\62\2\2\u01ca\u01d1\5w<\2\u01cb\u01cd\7a\2\2\u01cc")
        buf.write("\u01cb\3\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01ce\3\2\2\2")
        buf.write("\u01ce\u01d0\5u;\2\u01cf\u01cc\3\2\2\2\u01d0\u01d3\3\2")
        buf.write("\2\2\u01d1\u01cf\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d5")
        buf.write("\3\2\2\2\u01d3\u01d1\3\2\2\2\u01d4\u01c9\3\2\2\2\u01d4")
        buf.write("\u01ca\3\2\2\2\u01d5\u0094\3\2\2\2\u01d6\u01d7\7\62\2")
        buf.write("\2\u01d7\u01e3\t\17\2\2\u01d8\u01e4\7\62\2\2\u01d9\u01e0")
        buf.write("\7\63\2\2\u01da\u01dc\7a\2\2\u01db\u01da\3\2\2\2\u01db")
        buf.write("\u01dc\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01df\5s:\2\u01de")
        buf.write("\u01db\3\2\2\2\u01df\u01e2\3\2\2\2\u01e0\u01de\3\2\2\2")
        buf.write("\u01e0\u01e1\3\2\2\2\u01e1\u01e4\3\2\2\2\u01e2\u01e0\3")
        buf.write("\2\2\2\u01e3\u01d8\3\2\2\2\u01e3\u01d9\3\2\2\2\u01e4\u0096")
        buf.write("\3\2\2\2\u01e5\u01eb\5y=\2\u01e6\u01e7\7a\2\2\u01e7\u01ea")
        buf.write("\5q9\2\u01e8\u01ea\5q9\2\u01e9\u01e6\3\2\2\2\u01e9\u01e8")
        buf.write("\3\2\2\2\u01ea\u01ed\3\2\2\2\u01eb\u01e9\3\2\2\2\u01eb")
        buf.write("\u01ec\3\2\2\2\u01ec\u01f0\3\2\2\2\u01ed\u01eb\3\2\2\2")
        buf.write("\u01ee\u01f0\7\62\2\2\u01ef\u01e5\3\2\2\2\u01ef\u01ee")
        buf.write("\3\2\2\2\u01f0\u0098\3\2\2\2\u01f1\u01f2\7\62\2\2\u01f2")
        buf.write("\u0204\t\20\2\2\u01f3\u0205\7\62\2\2\u01f4\u01f7\5y=\2")
        buf.write("\u01f5\u01f7\5\177@\2\u01f6\u01f4\3\2\2\2\u01f6\u01f5")
        buf.write("\3\2\2\2\u01f7\u0201\3\2\2\2\u01f8\u01fa\7a\2\2\u01f9")
        buf.write("\u01f8\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u01fd\3\2\2\2")
        buf.write("\u01fb\u01fe\5q9\2\u01fc\u01fe\5\177@\2\u01fd\u01fb\3")
        buf.write("\2\2\2\u01fd\u01fc\3\2\2\2\u01fe\u0200\3\2\2\2\u01ff\u01f9")
        buf.write("\3\2\2\2\u0200\u0203\3\2\2\2\u0201\u01ff\3\2\2\2\u0201")
        buf.write("\u0202\3\2\2\2\u0202\u0205\3\2\2\2\u0203\u0201\3\2\2\2")
        buf.write("\u0204\u01f3\3\2\2\2\u0204\u01f6\3\2\2\2\u0205\u009a\3")
        buf.write("\2\2\2\u0206\u020b\5\u0093J\2\u0207\u020b\5\u0095K\2\u0208")
        buf.write("\u020b\5\u0097L\2\u0209\u020b\5\u0099M\2\u020a\u0206\3")
        buf.write("\2\2\2\u020a\u0207\3\2\2\2\u020a\u0208\3\2\2\2\u020a\u0209")
        buf.write("\3\2\2\2\u020b\u020c\3\2\2\2\u020c\u020d\bN\3\2\u020d")
        buf.write("\u009c\3\2\2\2\u020e\u0210\5\u0097L\2\u020f\u020e\3\2")
        buf.write("\2\2\u020f\u0210\3\2\2\2\u0210\u0216\3\2\2\2\u0211\u0213")
        buf.write("\5\u0085C\2\u0212\u0214\5\u0083B\2\u0213\u0212\3\2\2\2")
        buf.write("\u0213\u0214\3\2\2\2\u0214\u0217\3\2\2\2\u0215\u0217\5")
        buf.write("\u0083B\2\u0216\u0211\3\2\2\2\u0216\u0215\3\2\2\2\u0217")
        buf.write("\u0218\3\2\2\2\u0218\u0219\bO\4\2\u0219\u009e\3\2\2\2")
        buf.write("\u021a\u021e\5\u0087D\2\u021b\u021d\5\u008fH\2\u021c\u021b")
        buf.write("\3\2\2\2\u021d\u0220\3\2\2\2\u021e\u021c\3\2\2\2\u021e")
        buf.write("\u021f\3\2\2\2\u021f\u0221\3\2\2\2\u0220\u021e\3\2\2\2")
        buf.write("\u0221\u0222\5\u0087D\2\u0222\u00a0\3\2\2\2\u0223\u0227")
        buf.write("\t\n\2\2\u0224\u0226\t\21\2\2\u0225\u0224\3\2\2\2\u0226")
        buf.write("\u0229\3\2\2\2\u0227\u0225\3\2\2\2\u0227\u0228\3\2\2\2")
        buf.write("\u0228\u00a2\3\2\2\2\u0229\u0227\3\2\2\2\u022a\u022c\t")
        buf.write("\22\2\2\u022b\u022a\3\2\2\2\u022c\u022d\3\2\2\2\u022d")
        buf.write("\u022b\3\2\2\2\u022d\u022e\3\2\2\2\u022e\u022f\3\2\2\2")
        buf.write("\u022f\u0230\bR\2\2\u0230\u00a4\3\2\2\2\u0231\u0232\13")
        buf.write("\2\2\2\u0232\u0233\bS\5\2\u0233\u00a6\3\2\2\2\u0234\u0238")
        buf.write("\5\u0087D\2\u0235\u0237\5\u008fH\2\u0236\u0235\3\2\2\2")
        buf.write("\u0237\u023a\3\2\2\2\u0238\u0236\3\2\2\2\u0238\u0239\3")
        buf.write("\2\2\2\u0239\u023b\3\2\2\2\u023a\u0238\3\2\2\2\u023b\u023c")
        buf.write("\bT\6\2\u023c\u00a8\3\2\2\2\u023d\u0241\5\u0087D\2\u023e")
        buf.write("\u0240\5\u008fH\2\u023f\u023e\3\2\2\2\u0240\u0243\3\2")
        buf.write("\2\2\u0241\u023f\3\2\2\2\u0241\u0242\3\2\2\2\u0242\u0244")
        buf.write("\3\2\2\2\u0243\u0241\3\2\2\2\u0244\u0245\5\u0089E\2\u0245")
        buf.write("\u0246\bU\7\2\u0246\u00aa\3\2\2\2!\2\u00b0\u019a\u019f")
        buf.write("\u01a5\u01ad\u01b8\u01c0\u01cc\u01d1\u01d4\u01db\u01e0")
        buf.write("\u01e3\u01e9\u01eb\u01ef\u01f6\u01f9\u01fd\u0201\u0204")
        buf.write("\u020a\u020f\u0213\u0216\u021e\u0227\u022d\u0238\u0241")
        buf.write("\b\b\2\2\3N\2\3O\3\3S\4\3T\5\3U\6")
        return buf.getvalue()


class D96Lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    BOOLLIT = 2
    BREAK = 3
    CONTINUE = 4
    IF = 5
    ELSEIF = 6
    ELSE = 7
    FOREACH = 8
    TRUE = 9
    FALSE = 10
    ARRAY = 11
    IN = 12
    INT = 13
    FLOAT = 14
    BOOLEAN = 15
    STRING = 16
    RETURN = 17
    NULL = 18
    CLASS = 19
    VAL = 20
    VAR = 21
    CONSTRUCTOR = 22
    DESTRUCTOR = 23
    NEW = 24
    BY = 25
    SELF = 26
    STATIC = 27
    ADD = 28
    SUB = 29
    MUL = 30
    DIV = 31
    MOD = 32
    EQ = 33
    NEQ = 34
    GT = 35
    GTE = 36
    LT = 37
    LTE = 38
    SADD = 39
    SEQ = 40
    NOT = 41
    AND = 42
    OR = 43
    COLON = 44
    ASSIGN = 45
    SCOPE = 46
    LB = 47
    RB = 48
    LSB = 49
    RSB = 50
    LCB = 51
    RCB = 52
    SM = 53
    CM = 54
    DOT = 55
    BLOCK_COMMENT = 56
    INTLIT = 57
    FLOATLIT = 58
    STRLIT = 59
    ID = 60
    WS = 61
    ERROR_CHAR = 62
    UNCLOSE_STRING = 63
    ILLEGAL_ESCAPE = 64

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'..'", "'Break'", "'Continue'", "'If'", "'Elseif'", "'Else'", 
            "'Foreach'", "'True'", "'False'", "'Array'", "'In'", "'Int'", 
            "'Float'", "'Boolean'", "'String'", "'Return'", "'Null'", "'Class'", 
            "'Val'", "'Var'", "'Constructor'", "'Destructor'", "'New'", 
            "'By'", "'Self'", "'$'", "'+'", "'-'", "'*'", "'/'", "'%'", 
            "'=='", "'!='", "'>'", "'>='", "'<'", "'<='", "'+.'", "'==.'", 
            "'!'", "'&&'", "'||'", "':'", "'='", "'::'", "'('", "')'", "'['", 
            "']'", "'{'", "'}'", "';'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "BOOLLIT", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
            "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
            "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
            "NEW", "BY", "SELF", "STATIC", "ADD", "SUB", "MUL", "DIV", "MOD", 
            "EQ", "NEQ", "GT", "GTE", "LT", "LTE", "SADD", "SEQ", "NOT", 
            "AND", "OR", "COLON", "ASSIGN", "SCOPE", "LB", "RB", "LSB", 
            "RSB", "LCB", "RCB", "SM", "CM", "DOT", "BLOCK_COMMENT", "INTLIT", 
            "FLOATLIT", "STRLIT", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
            "ILLEGAL_ESCAPE" ]

    ruleNames = [ "T__0", "BOOLLIT", "BREAK", "CONTINUE", "IF", "ELSEIF", 
                  "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", "IN", "INT", 
                  "FLOAT", "BOOLEAN", "STRING", "RETURN", "NULL", "CLASS", 
                  "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", "NEW", "BY", 
                  "SELF", "STATIC", "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", 
                  "NEQ", "GT", "GTE", "LT", "LTE", "SADD", "SEQ", "NOT", 
                  "AND", "OR", "COLON", "ASSIGN", "SCOPE", "LB", "RB", "LSB", 
                  "RSB", "LCB", "RCB", "SM", "CM", "DOT", "DIGIT", "DIGIT_01", 
                  "DIGIT_07", "DIGIT_17", "DIGIT_19", "LOWERCASE", "UPERCASE", 
                  "UPERCASE_AF", "ALPHABET", "SCIENTIFIC", "DECIMAL_POINT", 
                  "DOUBLE_QUOTE", "ILLEGAL_STRING", "QUOTE_IN_STR", "ESC_SEQ", 
                  "VALID_STRING", "BLOCK_COMMENT", "OCTAL", "BINARY", "DECIMAL", 
                  "HEXADECIMAL", "INTLIT", "FLOATLIT", "STRLIT", "ID", "WS", 
                  "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[76] = self.INTLIT_action 
            actions[77] = self.FLOATLIT_action 
            actions[81] = self.ERROR_CHAR_action 
            actions[82] = self.UNCLOSE_STRING_action 
            actions[83] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def INTLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:
            self.text = self.text.replace('_','')
     

    def FLOATLIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:
            self.text = self.text.replace('_','')
     

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

     


