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
        buf.write("\u0250\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("U\4V\tV\3\2\3\2\3\2\3\3\3\3\5\3\u00b3\n\3\3\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3")
        buf.write("\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21")
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
        buf.write("\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\3B\3B\5B\u019d")
        buf.write("\nB\3B\6B\u01a0\nB\rB\16B\u01a1\3C\3C\7C\u01a6\nC\fC\16")
        buf.write("C\u01a9\13C\3D\3D\3E\3E\3E\3F\3F\3F\3G\3G\3G\3H\3H\3H")
        buf.write("\5H\u01b9\nH\3I\3I\3I\3I\7I\u01bf\nI\fI\16I\u01c2\13I")
        buf.write("\3I\3I\3I\3I\3I\3J\3J\3J\3J\5J\u01cd\nJ\3J\7J\u01d0\n")
        buf.write("J\fJ\16J\u01d3\13J\5J\u01d5\nJ\3K\3K\3K\3K\3K\5K\u01dc")
        buf.write("\nK\3K\7K\u01df\nK\fK\16K\u01e2\13K\5K\u01e4\nK\3L\3L")
        buf.write("\3L\3L\7L\u01ea\nL\fL\16L\u01ed\13L\3L\5L\u01f0\nL\3M")
        buf.write("\3M\3M\3M\3M\5M\u01f7\nM\3M\5M\u01fa\nM\3M\3M\5M\u01fe")
        buf.write("\nM\7M\u0200\nM\fM\16M\u0203\13M\5M\u0205\nM\3N\3N\3N")
        buf.write("\3N\5N\u020b\nN\3N\3N\3O\3O\3O\3O\3O\3O\5O\u0215\nO\3")
        buf.write("O\3O\3O\5O\u021a\nO\3O\3O\3P\3P\7P\u0220\nP\fP\16P\u0223")
        buf.write("\13P\3P\3P\3Q\3Q\6Q\u0229\nQ\rQ\16Q\u022a\3R\3R\7R\u022f")
        buf.write("\nR\fR\16R\u0232\13R\3S\6S\u0235\nS\rS\16S\u0236\3S\3")
        buf.write("S\3T\3T\3T\3U\3U\7U\u0240\nU\fU\16U\u0243\13U\3U\3U\3")
        buf.write("V\3V\7V\u0249\nV\fV\16V\u024c\13V\3V\3V\3V\3\u01c0\2W")
        buf.write("\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31")
        buf.write("\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31")
        buf.write("\61\32\63\33\65\34\67\29\35;\36=\37? A!C\"E#G$I%K&M\'")
        buf.write("O(Q)S*U+W,Y-[.]/_\60a\61c\62e\63g\64i\65k\66m\67o8q\2")
        buf.write("s\2u\2w\2y\2{\2}\2\177\2\u0081\2\u0083\2\u0085\2\u0087")
        buf.write("\2\u0089\2\u008b\2\u008d\2\u008f\2\u00919\u0093\2\u0095")
        buf.write("\2\u0097\2\u0099\2\u009b:\u009d;\u009f<\u00a1=\u00a3>")
        buf.write("\u00a5?\u00a7@\u00a9A\u00abB\3\2\22\3\2\62;\3\2\62\63")
        buf.write("\3\2\629\3\2\639\3\2\63;\3\2c|\3\2C\\\4\2CHaa\5\2C\\a")
        buf.write("ac|\4\2GGgg\t\2))^^ddhhppttvv\6\2\n\f\16\17$$^^\4\2DD")
        buf.write("dd\4\2ZZzz\6\2\62;C\\aac|\5\2\13\f\16\17\"\"\2\u025b\2")
        buf.write("\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3")
        buf.write("\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2")
        buf.write("\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2")
        buf.write("\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%")
        buf.write("\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\29")
        buf.write("\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2")
        buf.write("C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2")
        buf.write("\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2")
        buf.write("\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2")
        buf.write("\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3")
        buf.write("\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2\u0091\3\2\2")
        buf.write("\2\2\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1")
        buf.write("\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2")
        buf.write("\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\3\u00ad\3\2\2\2\5\u00b2")
        buf.write("\3\2\2\2\7\u00b4\3\2\2\2\t\u00ba\3\2\2\2\13\u00c3\3\2")
        buf.write("\2\2\r\u00c6\3\2\2\2\17\u00cd\3\2\2\2\21\u00d2\3\2\2\2")
        buf.write("\23\u00da\3\2\2\2\25\u00df\3\2\2\2\27\u00e5\3\2\2\2\31")
        buf.write("\u00eb\3\2\2\2\33\u00ee\3\2\2\2\35\u00f2\3\2\2\2\37\u00f8")
        buf.write("\3\2\2\2!\u0100\3\2\2\2#\u0107\3\2\2\2%\u010e\3\2\2\2")
        buf.write("\'\u0113\3\2\2\2)\u0119\3\2\2\2+\u011d\3\2\2\2-\u0121")
        buf.write("\3\2\2\2/\u012d\3\2\2\2\61\u0138\3\2\2\2\63\u013c\3\2")
        buf.write("\2\2\65\u013f\3\2\2\2\67\u0144\3\2\2\29\u0146\3\2\2\2")
        buf.write(";\u0148\3\2\2\2=\u014a\3\2\2\2?\u014c\3\2\2\2A\u014e\3")
        buf.write("\2\2\2C\u0150\3\2\2\2E\u0153\3\2\2\2G\u0156\3\2\2\2I\u0158")
        buf.write("\3\2\2\2K\u015b\3\2\2\2M\u015d\3\2\2\2O\u0160\3\2\2\2")
        buf.write("Q\u0163\3\2\2\2S\u0167\3\2\2\2U\u0169\3\2\2\2W\u016c\3")
        buf.write("\2\2\2Y\u016f\3\2\2\2[\u0171\3\2\2\2]\u0173\3\2\2\2_\u0176")
        buf.write("\3\2\2\2a\u0178\3\2\2\2c\u017a\3\2\2\2e\u017c\3\2\2\2")
        buf.write("g\u017e\3\2\2\2i\u0180\3\2\2\2k\u0182\3\2\2\2m\u0184\3")
        buf.write("\2\2\2o\u0186\3\2\2\2q\u0188\3\2\2\2s\u018a\3\2\2\2u\u018c")
        buf.write("\3\2\2\2w\u018e\3\2\2\2y\u0190\3\2\2\2{\u0192\3\2\2\2")
        buf.write("}\u0194\3\2\2\2\177\u0196\3\2\2\2\u0081\u0198\3\2\2\2")
        buf.write("\u0083\u019a\3\2\2\2\u0085\u01a3\3\2\2\2\u0087\u01aa\3")
        buf.write("\2\2\2\u0089\u01ac\3\2\2\2\u008b\u01af\3\2\2\2\u008d\u01b2")
        buf.write("\3\2\2\2\u008f\u01b8\3\2\2\2\u0091\u01ba\3\2\2\2\u0093")
        buf.write("\u01c8\3\2\2\2\u0095\u01d6\3\2\2\2\u0097\u01ef\3\2\2\2")
        buf.write("\u0099\u01f1\3\2\2\2\u009b\u020a\3\2\2\2\u009d\u0219\3")
        buf.write("\2\2\2\u009f\u021d\3\2\2\2\u00a1\u0226\3\2\2\2\u00a3\u022c")
        buf.write("\3\2\2\2\u00a5\u0234\3\2\2\2\u00a7\u023a\3\2\2\2\u00a9")
        buf.write("\u023d\3\2\2\2\u00ab\u0246\3\2\2\2\u00ad\u00ae\7\60\2")
        buf.write("\2\u00ae\u00af\7\60\2\2\u00af\4\3\2\2\2\u00b0\u00b3\5")
        buf.write("\23\n\2\u00b1\u00b3\5\25\13\2\u00b2\u00b0\3\2\2\2\u00b2")
        buf.write("\u00b1\3\2\2\2\u00b3\6\3\2\2\2\u00b4\u00b5\7D\2\2\u00b5")
        buf.write("\u00b6\7t\2\2\u00b6\u00b7\7g\2\2\u00b7\u00b8\7c\2\2\u00b8")
        buf.write("\u00b9\7m\2\2\u00b9\b\3\2\2\2\u00ba\u00bb\7E\2\2\u00bb")
        buf.write("\u00bc\7q\2\2\u00bc\u00bd\7p\2\2\u00bd\u00be\7v\2\2\u00be")
        buf.write("\u00bf\7k\2\2\u00bf\u00c0\7p\2\2\u00c0\u00c1\7w\2\2\u00c1")
        buf.write("\u00c2\7g\2\2\u00c2\n\3\2\2\2\u00c3\u00c4\7K\2\2\u00c4")
        buf.write("\u00c5\7h\2\2\u00c5\f\3\2\2\2\u00c6\u00c7\7G\2\2\u00c7")
        buf.write("\u00c8\7n\2\2\u00c8\u00c9\7u\2\2\u00c9\u00ca\7g\2\2\u00ca")
        buf.write("\u00cb\7k\2\2\u00cb\u00cc\7h\2\2\u00cc\16\3\2\2\2\u00cd")
        buf.write("\u00ce\7G\2\2\u00ce\u00cf\7n\2\2\u00cf\u00d0\7u\2\2\u00d0")
        buf.write("\u00d1\7g\2\2\u00d1\20\3\2\2\2\u00d2\u00d3\7H\2\2\u00d3")
        buf.write("\u00d4\7q\2\2\u00d4\u00d5\7t\2\2\u00d5\u00d6\7g\2\2\u00d6")
        buf.write("\u00d7\7c\2\2\u00d7\u00d8\7e\2\2\u00d8\u00d9\7j\2\2\u00d9")
        buf.write("\22\3\2\2\2\u00da\u00db\7V\2\2\u00db\u00dc\7t\2\2\u00dc")
        buf.write("\u00dd\7w\2\2\u00dd\u00de\7g\2\2\u00de\24\3\2\2\2\u00df")
        buf.write("\u00e0\7H\2\2\u00e0\u00e1\7c\2\2\u00e1\u00e2\7n\2\2\u00e2")
        buf.write("\u00e3\7u\2\2\u00e3\u00e4\7g\2\2\u00e4\26\3\2\2\2\u00e5")
        buf.write("\u00e6\7C\2\2\u00e6\u00e7\7t\2\2\u00e7\u00e8\7t\2\2\u00e8")
        buf.write("\u00e9\7c\2\2\u00e9\u00ea\7{\2\2\u00ea\30\3\2\2\2\u00eb")
        buf.write("\u00ec\7K\2\2\u00ec\u00ed\7p\2\2\u00ed\32\3\2\2\2\u00ee")
        buf.write("\u00ef\7K\2\2\u00ef\u00f0\7p\2\2\u00f0\u00f1\7v\2\2\u00f1")
        buf.write("\34\3\2\2\2\u00f2\u00f3\7H\2\2\u00f3\u00f4\7n\2\2\u00f4")
        buf.write("\u00f5\7q\2\2\u00f5\u00f6\7c\2\2\u00f6\u00f7\7v\2\2\u00f7")
        buf.write("\36\3\2\2\2\u00f8\u00f9\7D\2\2\u00f9\u00fa\7q\2\2\u00fa")
        buf.write("\u00fb\7q\2\2\u00fb\u00fc\7n\2\2\u00fc\u00fd\7g\2\2\u00fd")
        buf.write("\u00fe\7c\2\2\u00fe\u00ff\7p\2\2\u00ff \3\2\2\2\u0100")
        buf.write("\u0101\7U\2\2\u0101\u0102\7v\2\2\u0102\u0103\7t\2\2\u0103")
        buf.write("\u0104\7k\2\2\u0104\u0105\7p\2\2\u0105\u0106\7i\2\2\u0106")
        buf.write("\"\3\2\2\2\u0107\u0108\7T\2\2\u0108\u0109\7g\2\2\u0109")
        buf.write("\u010a\7v\2\2\u010a\u010b\7w\2\2\u010b\u010c\7t\2\2\u010c")
        buf.write("\u010d\7p\2\2\u010d$\3\2\2\2\u010e\u010f\7P\2\2\u010f")
        buf.write("\u0110\7w\2\2\u0110\u0111\7n\2\2\u0111\u0112\7n\2\2\u0112")
        buf.write("&\3\2\2\2\u0113\u0114\7E\2\2\u0114\u0115\7n\2\2\u0115")
        buf.write("\u0116\7c\2\2\u0116\u0117\7u\2\2\u0117\u0118\7u\2\2\u0118")
        buf.write("(\3\2\2\2\u0119\u011a\7X\2\2\u011a\u011b\7c\2\2\u011b")
        buf.write("\u011c\7n\2\2\u011c*\3\2\2\2\u011d\u011e\7X\2\2\u011e")
        buf.write("\u011f\7c\2\2\u011f\u0120\7t\2\2\u0120,\3\2\2\2\u0121")
        buf.write("\u0122\7E\2\2\u0122\u0123\7q\2\2\u0123\u0124\7p\2\2\u0124")
        buf.write("\u0125\7u\2\2\u0125\u0126\7v\2\2\u0126\u0127\7t\2\2\u0127")
        buf.write("\u0128\7w\2\2\u0128\u0129\7e\2\2\u0129\u012a\7v\2\2\u012a")
        buf.write("\u012b\7q\2\2\u012b\u012c\7t\2\2\u012c.\3\2\2\2\u012d")
        buf.write("\u012e\7F\2\2\u012e\u012f\7g\2\2\u012f\u0130\7u\2\2\u0130")
        buf.write("\u0131\7v\2\2\u0131\u0132\7t\2\2\u0132\u0133\7w\2\2\u0133")
        buf.write("\u0134\7e\2\2\u0134\u0135\7v\2\2\u0135\u0136\7q\2\2\u0136")
        buf.write("\u0137\7t\2\2\u0137\60\3\2\2\2\u0138\u0139\7P\2\2\u0139")
        buf.write("\u013a\7g\2\2\u013a\u013b\7y\2\2\u013b\62\3\2\2\2\u013c")
        buf.write("\u013d\7D\2\2\u013d\u013e\7{\2\2\u013e\64\3\2\2\2\u013f")
        buf.write("\u0140\7U\2\2\u0140\u0141\7g\2\2\u0141\u0142\7n\2\2\u0142")
        buf.write("\u0143\7h\2\2\u0143\66\3\2\2\2\u0144\u0145\7&\2\2\u0145")
        buf.write("8\3\2\2\2\u0146\u0147\7-\2\2\u0147:\3\2\2\2\u0148\u0149")
        buf.write("\7/\2\2\u0149<\3\2\2\2\u014a\u014b\7,\2\2\u014b>\3\2\2")
        buf.write("\2\u014c\u014d\7\61\2\2\u014d@\3\2\2\2\u014e\u014f\7\'")
        buf.write("\2\2\u014fB\3\2\2\2\u0150\u0151\7?\2\2\u0151\u0152\7?")
        buf.write("\2\2\u0152D\3\2\2\2\u0153\u0154\7#\2\2\u0154\u0155\7?")
        buf.write("\2\2\u0155F\3\2\2\2\u0156\u0157\7@\2\2\u0157H\3\2\2\2")
        buf.write("\u0158\u0159\7@\2\2\u0159\u015a\7?\2\2\u015aJ\3\2\2\2")
        buf.write("\u015b\u015c\7>\2\2\u015cL\3\2\2\2\u015d\u015e\7>\2\2")
        buf.write("\u015e\u015f\7?\2\2\u015fN\3\2\2\2\u0160\u0161\7-\2\2")
        buf.write("\u0161\u0162\7\60\2\2\u0162P\3\2\2\2\u0163\u0164\7?\2")
        buf.write("\2\u0164\u0165\7?\2\2\u0165\u0166\7\60\2\2\u0166R\3\2")
        buf.write("\2\2\u0167\u0168\7#\2\2\u0168T\3\2\2\2\u0169\u016a\7(")
        buf.write("\2\2\u016a\u016b\7(\2\2\u016bV\3\2\2\2\u016c\u016d\7~")
        buf.write("\2\2\u016d\u016e\7~\2\2\u016eX\3\2\2\2\u016f\u0170\7<")
        buf.write("\2\2\u0170Z\3\2\2\2\u0171\u0172\7?\2\2\u0172\\\3\2\2\2")
        buf.write("\u0173\u0174\7<\2\2\u0174\u0175\7<\2\2\u0175^\3\2\2\2")
        buf.write("\u0176\u0177\7*\2\2\u0177`\3\2\2\2\u0178\u0179\7+\2\2")
        buf.write("\u0179b\3\2\2\2\u017a\u017b\7]\2\2\u017bd\3\2\2\2\u017c")
        buf.write("\u017d\7_\2\2\u017df\3\2\2\2\u017e\u017f\7}\2\2\u017f")
        buf.write("h\3\2\2\2\u0180\u0181\7\177\2\2\u0181j\3\2\2\2\u0182\u0183")
        buf.write("\7=\2\2\u0183l\3\2\2\2\u0184\u0185\7.\2\2\u0185n\3\2\2")
        buf.write("\2\u0186\u0187\7\60\2\2\u0187p\3\2\2\2\u0188\u0189\t\2")
        buf.write("\2\2\u0189r\3\2\2\2\u018a\u018b\t\3\2\2\u018bt\3\2\2\2")
        buf.write("\u018c\u018d\t\4\2\2\u018dv\3\2\2\2\u018e\u018f\t\5\2")
        buf.write("\2\u018fx\3\2\2\2\u0190\u0191\t\6\2\2\u0191z\3\2\2\2\u0192")
        buf.write("\u0193\t\7\2\2\u0193|\3\2\2\2\u0194\u0195\t\b\2\2\u0195")
        buf.write("~\3\2\2\2\u0196\u0197\t\t\2\2\u0197\u0080\3\2\2\2\u0198")
        buf.write("\u0199\t\n\2\2\u0199\u0082\3\2\2\2\u019a\u019c\t\13\2")
        buf.write("\2\u019b\u019d\7/\2\2\u019c\u019b\3\2\2\2\u019c\u019d")
        buf.write("\3\2\2\2\u019d\u019f\3\2\2\2\u019e\u01a0\5q9\2\u019f\u019e")
        buf.write("\3\2\2\2\u01a0\u01a1\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1")
        buf.write("\u01a2\3\2\2\2\u01a2\u0084\3\2\2\2\u01a3\u01a7\5o8\2\u01a4")
        buf.write("\u01a6\5q9\2\u01a5\u01a4\3\2\2\2\u01a6\u01a9\3\2\2\2\u01a7")
        buf.write("\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2\u01a8\u0086\3\2\2\2")
        buf.write("\u01a9\u01a7\3\2\2\2\u01aa\u01ab\7$\2\2\u01ab\u0088\3")
        buf.write("\2\2\2\u01ac\u01ad\7^\2\2\u01ad\u01ae\n\f\2\2\u01ae\u008a")
        buf.write("\3\2\2\2\u01af\u01b0\7)\2\2\u01b0\u01b1\7$\2\2\u01b1\u008c")
        buf.write("\3\2\2\2\u01b2\u01b3\7^\2\2\u01b3\u01b4\t\f\2\2\u01b4")
        buf.write("\u008e\3\2\2\2\u01b5\u01b9\n\r\2\2\u01b6\u01b9\5\u008d")
        buf.write("G\2\u01b7\u01b9\5\u008bF\2\u01b8\u01b5\3\2\2\2\u01b8\u01b6")
        buf.write("\3\2\2\2\u01b8\u01b7\3\2\2\2\u01b9\u0090\3\2\2\2\u01ba")
        buf.write("\u01bb\7%\2\2\u01bb\u01bc\7%\2\2\u01bc\u01c0\3\2\2\2\u01bd")
        buf.write("\u01bf\13\2\2\2\u01be\u01bd\3\2\2\2\u01bf\u01c2\3\2\2")
        buf.write("\2\u01c0\u01c1\3\2\2\2\u01c0\u01be\3\2\2\2\u01c1\u01c3")
        buf.write("\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c3\u01c4\7%\2\2\u01c4")
        buf.write("\u01c5\7%\2\2\u01c5\u01c6\3\2\2\2\u01c6\u01c7\bI\2\2\u01c7")
        buf.write("\u0092\3\2\2\2\u01c8\u01d4\7\62\2\2\u01c9\u01d5\7\62\2")
        buf.write("\2\u01ca\u01d1\5w<\2\u01cb\u01cd\7a\2\2\u01cc\u01cb\3")
        buf.write("\2\2\2\u01cc\u01cd\3\2\2\2\u01cd\u01ce\3\2\2\2\u01ce\u01d0")
        buf.write("\5u;\2\u01cf\u01cc\3\2\2\2\u01d0\u01d3\3\2\2\2\u01d1\u01cf")
        buf.write("\3\2\2\2\u01d1\u01d2\3\2\2\2\u01d2\u01d5\3\2\2\2\u01d3")
        buf.write("\u01d1\3\2\2\2\u01d4\u01c9\3\2\2\2\u01d4\u01ca\3\2\2\2")
        buf.write("\u01d5\u0094\3\2\2\2\u01d6\u01d7\7\62\2\2\u01d7\u01e3")
        buf.write("\t\16\2\2\u01d8\u01e4\7\62\2\2\u01d9\u01e0\7\63\2\2\u01da")
        buf.write("\u01dc\7a\2\2\u01db\u01da\3\2\2\2\u01db\u01dc\3\2\2\2")
        buf.write("\u01dc\u01dd\3\2\2\2\u01dd\u01df\5s:\2\u01de\u01db\3\2")
        buf.write("\2\2\u01df\u01e2\3\2\2\2\u01e0\u01de\3\2\2\2\u01e0\u01e1")
        buf.write("\3\2\2\2\u01e1\u01e4\3\2\2\2\u01e2\u01e0\3\2\2\2\u01e3")
        buf.write("\u01d8\3\2\2\2\u01e3\u01d9\3\2\2\2\u01e4\u0096\3\2\2\2")
        buf.write("\u01e5\u01eb\5y=\2\u01e6\u01e7\7a\2\2\u01e7\u01ea\5q9")
        buf.write("\2\u01e8\u01ea\5q9\2\u01e9\u01e6\3\2\2\2\u01e9\u01e8\3")
        buf.write("\2\2\2\u01ea\u01ed\3\2\2\2\u01eb\u01e9\3\2\2\2\u01eb\u01ec")
        buf.write("\3\2\2\2\u01ec\u01f0\3\2\2\2\u01ed\u01eb\3\2\2\2\u01ee")
        buf.write("\u01f0\7\62\2\2\u01ef\u01e5\3\2\2\2\u01ef\u01ee\3\2\2")
        buf.write("\2\u01f0\u0098\3\2\2\2\u01f1\u01f2\7\62\2\2\u01f2\u0204")
        buf.write("\t\17\2\2\u01f3\u0205\7\62\2\2\u01f4\u01f7\5y=\2\u01f5")
        buf.write("\u01f7\5\177@\2\u01f6\u01f4\3\2\2\2\u01f6\u01f5\3\2\2")
        buf.write("\2\u01f7\u0201\3\2\2\2\u01f8\u01fa\7a\2\2\u01f9\u01f8")
        buf.write("\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u01fd\3\2\2\2\u01fb")
        buf.write("\u01fe\5q9\2\u01fc\u01fe\5\177@\2\u01fd\u01fb\3\2\2\2")
        buf.write("\u01fd\u01fc\3\2\2\2\u01fe\u0200\3\2\2\2\u01ff\u01f9\3")
        buf.write("\2\2\2\u0200\u0203\3\2\2\2\u0201\u01ff\3\2\2\2\u0201\u0202")
        buf.write("\3\2\2\2\u0202\u0205\3\2\2\2\u0203\u0201\3\2\2\2\u0204")
        buf.write("\u01f3\3\2\2\2\u0204\u01f6\3\2\2\2\u0205\u009a\3\2\2\2")
        buf.write("\u0206\u020b\5\u0093J\2\u0207\u020b\5\u0095K\2\u0208\u020b")
        buf.write("\5\u0097L\2\u0209\u020b\5\u0099M\2\u020a\u0206\3\2\2\2")
        buf.write("\u020a\u0207\3\2\2\2\u020a\u0208\3\2\2\2\u020a\u0209\3")
        buf.write("\2\2\2\u020b\u020c\3\2\2\2\u020c\u020d\bN\3\2\u020d\u009c")
        buf.write("\3\2\2\2\u020e\u0214\5\u0097L\2\u020f\u0215\5\u0085C\2")
        buf.write("\u0210\u0215\5\u0083B\2\u0211\u0212\5\u0085C\2\u0212\u0213")
        buf.write("\5\u0083B\2\u0213\u0215\3\2\2\2\u0214\u020f\3\2\2\2\u0214")
        buf.write("\u0210\3\2\2\2\u0214\u0211\3\2\2\2\u0215\u021a\3\2\2\2")
        buf.write("\u0216\u0217\5\u0085C\2\u0217\u0218\5\u0083B\2\u0218\u021a")
        buf.write("\3\2\2\2\u0219\u020e\3\2\2\2\u0219\u0216\3\2\2\2\u021a")
        buf.write("\u021b\3\2\2\2\u021b\u021c\bO\4\2\u021c\u009e\3\2\2\2")
        buf.write("\u021d\u0221\5\u0087D\2\u021e\u0220\5\u008fH\2\u021f\u021e")
        buf.write("\3\2\2\2\u0220\u0223\3\2\2\2\u0221\u021f\3\2\2\2\u0221")
        buf.write("\u0222\3\2\2\2\u0222\u0224\3\2\2\2\u0223\u0221\3\2\2\2")
        buf.write("\u0224\u0225\5\u0087D\2\u0225\u00a0\3\2\2\2\u0226\u0228")
        buf.write("\5\67\34\2\u0227\u0229\t\20\2\2\u0228\u0227\3\2\2\2\u0229")
        buf.write("\u022a\3\2\2\2\u022a\u0228\3\2\2\2\u022a\u022b\3\2\2\2")
        buf.write("\u022b\u00a2\3\2\2\2\u022c\u0230\t\n\2\2\u022d\u022f\t")
        buf.write("\20\2\2\u022e\u022d\3\2\2\2\u022f\u0232\3\2\2\2\u0230")
        buf.write("\u022e\3\2\2\2\u0230\u0231\3\2\2\2\u0231\u00a4\3\2\2\2")
        buf.write("\u0232\u0230\3\2\2\2\u0233\u0235\t\21\2\2\u0234\u0233")
        buf.write("\3\2\2\2\u0235\u0236\3\2\2\2\u0236\u0234\3\2\2\2\u0236")
        buf.write("\u0237\3\2\2\2\u0237\u0238\3\2\2\2\u0238\u0239\bS\2\2")
        buf.write("\u0239\u00a6\3\2\2\2\u023a\u023b\13\2\2\2\u023b\u023c")
        buf.write("\bT\5\2\u023c\u00a8\3\2\2\2\u023d\u0241\5\u0087D\2\u023e")
        buf.write("\u0240\5\u008fH\2\u023f\u023e\3\2\2\2\u0240\u0243\3\2")
        buf.write("\2\2\u0241\u023f\3\2\2\2\u0241\u0242\3\2\2\2\u0242\u0244")
        buf.write("\3\2\2\2\u0243\u0241\3\2\2\2\u0244\u0245\bU\6\2\u0245")
        buf.write("\u00aa\3\2\2\2\u0246\u024a\5\u0087D\2\u0247\u0249\5\u008f")
        buf.write("H\2\u0248\u0247\3\2\2\2\u0249\u024c\3\2\2\2\u024a\u0248")
        buf.write("\3\2\2\2\u024a\u024b\3\2\2\2\u024b\u024d\3\2\2\2\u024c")
        buf.write("\u024a\3\2\2\2\u024d\u024e\5\u0089E\2\u024e\u024f\bV\7")
        buf.write("\2\u024f\u00ac\3\2\2\2 \2\u00b2\u019c\u01a1\u01a7\u01b8")
        buf.write("\u01c0\u01cc\u01d1\u01d4\u01db\u01e0\u01e3\u01e9\u01eb")
        buf.write("\u01ef\u01f6\u01f9\u01fd\u0201\u0204\u020a\u0214\u0219")
        buf.write("\u0221\u022a\u0230\u0236\u0241\u024a\b\b\2\2\3N\2\3O\3")
        buf.write("\3T\4\3U\5\3V\6")
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
    ADD = 27
    SUB = 28
    MUL = 29
    DIV = 30
    MOD = 31
    EQ = 32
    NEQ = 33
    GT = 34
    GTE = 35
    LT = 36
    LTE = 37
    SADD = 38
    SEQ = 39
    NOT = 40
    AND = 41
    OR = 42
    COLON = 43
    ASSIGN = 44
    SCOPE = 45
    LB = 46
    RB = 47
    LSB = 48
    RSB = 49
    LCB = 50
    RCB = 51
    SM = 52
    CM = 53
    DOT = 54
    BLOCK_COMMENT = 55
    INTLIT = 56
    FLOATLIT = 57
    STRLIT = 58
    STATIC_ID = 59
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
            "'By'", "'Self'", "'+'", "'-'", "'*'", "'/'", "'%'", "'=='", 
            "'!='", "'>'", "'>='", "'<'", "'<='", "'+.'", "'==.'", "'!'", 
            "'&&'", "'||'", "':'", "'='", "'::'", "'('", "')'", "'['", "']'", 
            "'{'", "'}'", "';'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>",
            "BOOLLIT", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
            "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
            "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
            "NEW", "BY", "SELF", "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", 
            "NEQ", "GT", "GTE", "LT", "LTE", "SADD", "SEQ", "NOT", "AND", 
            "OR", "COLON", "ASSIGN", "SCOPE", "LB", "RB", "LSB", "RSB", 
            "LCB", "RCB", "SM", "CM", "DOT", "BLOCK_COMMENT", "INTLIT", 
            "FLOATLIT", "STRLIT", "STATIC_ID", "ID", "WS", "ERROR_CHAR", 
            "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
                  "HEXADECIMAL", "INTLIT", "FLOATLIT", "STRLIT", "STATIC_ID", 
                  "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
            actions[82] = self.ERROR_CHAR_action 
            actions[83] = self.UNCLOSE_STRING_action 
            actions[84] = self.ILLEGAL_ESCAPE_action 
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

     


