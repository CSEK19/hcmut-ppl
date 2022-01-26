# Generated from c:\Users\Admin\Desktop\P\BK\212\Principles of Programming Languages\Assignment\ppl\assignment 1\code\initial\src\main\d96\parser\D96.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2D")
        buf.write("\u025a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("U\4V\tV\4W\tW\3\2\3\2\3\2\3\3\3\3\5\3\u00b5\n\3\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f")
        buf.write("\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3")
        buf.write("\17\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\22\3\22\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\34\3\34\3\35\3\35\3\36\3\36\3\37\3\37\3 ")
        buf.write("\3 \3!\3!\3\"\3\"\3\"\3#\3#\3#\3$\3$\3%\3%\3%\3&\3&\3")
        buf.write("\'\3\'\3\'\3(\3(\3(\3)\3)\3)\3)\3*\3*\3+\3+\3+\3,\3,\3")
        buf.write(",\3-\3-\3.\3.\3/\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3")
        buf.write("\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\3")
        buf.write("8\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3")
        buf.write("A\3B\3B\5B\u019f\nB\3B\6B\u01a2\nB\rB\16B\u01a3\3C\3C")
        buf.write("\7C\u01a8\nC\fC\16C\u01ab\13C\3D\3D\3E\3E\3E\3F\3F\3F")
        buf.write("\3G\3G\3G\3H\3H\3H\5H\u01bb\nH\3I\3I\3I\3I\7I\u01c1\n")
        buf.write("I\fI\16I\u01c4\13I\3I\3I\3I\3I\3I\3J\3J\3J\5J\u01ce\n")
        buf.write("J\3J\7J\u01d1\nJ\fJ\16J\u01d4\13J\3K\3K\3K\3K\5K\u01da")
        buf.write("\nK\3K\7K\u01dd\nK\fK\16K\u01e0\13K\3L\3L\3L\3L\7L\u01e6")
        buf.write("\nL\fL\16L\u01e9\13L\3M\3M\3M\3M\5M\u01ef\nM\3M\5M\u01f2")
        buf.write("\nM\3M\3M\5M\u01f6\nM\7M\u01f8\nM\fM\16M\u01fb\13M\3N")
        buf.write("\3N\3N\3N\5N\u0201\nN\3N\3N\3O\3O\3O\3O\3O\3O\5O\u020b")
        buf.write("\nO\3O\3O\3O\5O\u0210\nO\3O\3O\3P\3P\7P\u0216\nP\fP\16")
        buf.write("P\u0219\13P\3P\3P\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q\3Q")
        buf.write("\3Q\3Q\3Q\5Q\u022c\nQ\3R\3R\6R\u0230\nR\rR\16R\u0231\3")
        buf.write("S\3S\7S\u0236\nS\fS\16S\u0239\13S\3T\6T\u023c\nT\rT\16")
        buf.write("T\u023d\3T\3T\3U\3U\3U\3V\3V\7V\u0247\nV\fV\16V\u024a")
        buf.write("\13V\3V\5V\u024d\nV\3V\3V\3W\3W\7W\u0253\nW\fW\16W\u0256")
        buf.write("\13W\3W\3W\3W\3\u01c2\2X\3\3\5\4\7\5\t\6\13\7\r\b\17\t")
        buf.write("\21\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23")
        buf.write("%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67\29\35;")
        buf.write("\36=\37? A!C\"E#G$I%K&M\'O(Q)S*U+W,Y-[.]/_\60a\61c\62")
        buf.write("e\63g\64i\65k\66m\67o8q\2s\2u\2w\2y\2{\2}\2\177\2\u0081")
        buf.write("\2\u0083\2\u0085\2\u00879\u0089\2\u008b\2\u008d\2\u008f")
        buf.write("\2\u0091:\u0093\2\u0095\2\u0097\2\u0099\2\u009b;\u009d")
        buf.write("<\u009f=\u00a1>\u00a3?\u00a5@\u00a7A\u00a9B\u00abC\u00ad")
        buf.write("D\3\2\23\3\2\62;\3\2\62\63\3\2\629\3\2\639\3\2\63;\3\2")
        buf.write("c|\3\2C\\\3\2CH\5\2C\\aac|\4\2GGgg\t\2))^^ddhhppttvv\6")
        buf.write("\2\n\f\16\17$$^^\4\2DDdd\4\2ZZzz\6\2\62;C\\aac|\5\2\13")
        buf.write("\f\16\17\"\"\4\3\f\f\17\17\2\u0267\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2")
        buf.write("=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2")
        buf.write("\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2")
        buf.write("\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2")
        buf.write("\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3")
        buf.write("\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m")
        buf.write("\3\2\2\2\2o\3\2\2\2\2\u0087\3\2\2\2\2\u0091\3\2\2\2\2")
        buf.write("\u009b\3\2\2\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a1")
        buf.write("\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5\3\2\2\2\2\u00a7\3\2\2")
        buf.write("\2\2\u00a9\3\2\2\2\2\u00ab\3\2\2\2\2\u00ad\3\2\2\2\3\u00af")
        buf.write("\3\2\2\2\5\u00b4\3\2\2\2\7\u00b6\3\2\2\2\t\u00bc\3\2\2")
        buf.write("\2\13\u00c5\3\2\2\2\r\u00c8\3\2\2\2\17\u00cf\3\2\2\2\21")
        buf.write("\u00d4\3\2\2\2\23\u00dc\3\2\2\2\25\u00e1\3\2\2\2\27\u00e7")
        buf.write("\3\2\2\2\31\u00ed\3\2\2\2\33\u00f0\3\2\2\2\35\u00f4\3")
        buf.write("\2\2\2\37\u00fa\3\2\2\2!\u0102\3\2\2\2#\u0109\3\2\2\2")
        buf.write("%\u0110\3\2\2\2\'\u0115\3\2\2\2)\u011b\3\2\2\2+\u011f")
        buf.write("\3\2\2\2-\u0123\3\2\2\2/\u012f\3\2\2\2\61\u013a\3\2\2")
        buf.write("\2\63\u013e\3\2\2\2\65\u0141\3\2\2\2\67\u0146\3\2\2\2")
        buf.write("9\u0148\3\2\2\2;\u014a\3\2\2\2=\u014c\3\2\2\2?\u014e\3")
        buf.write("\2\2\2A\u0150\3\2\2\2C\u0152\3\2\2\2E\u0155\3\2\2\2G\u0158")
        buf.write("\3\2\2\2I\u015a\3\2\2\2K\u015d\3\2\2\2M\u015f\3\2\2\2")
        buf.write("O\u0162\3\2\2\2Q\u0165\3\2\2\2S\u0169\3\2\2\2U\u016b\3")
        buf.write("\2\2\2W\u016e\3\2\2\2Y\u0171\3\2\2\2[\u0173\3\2\2\2]\u0175")
        buf.write("\3\2\2\2_\u0178\3\2\2\2a\u017a\3\2\2\2c\u017c\3\2\2\2")
        buf.write("e\u017e\3\2\2\2g\u0180\3\2\2\2i\u0182\3\2\2\2k\u0184\3")
        buf.write("\2\2\2m\u0186\3\2\2\2o\u0188\3\2\2\2q\u018a\3\2\2\2s\u018c")
        buf.write("\3\2\2\2u\u018e\3\2\2\2w\u0190\3\2\2\2y\u0192\3\2\2\2")
        buf.write("{\u0194\3\2\2\2}\u0196\3\2\2\2\177\u0198\3\2\2\2\u0081")
        buf.write("\u019a\3\2\2\2\u0083\u019c\3\2\2\2\u0085\u01a5\3\2\2\2")
        buf.write("\u0087\u01ac\3\2\2\2\u0089\u01ae\3\2\2\2\u008b\u01b1\3")
        buf.write("\2\2\2\u008d\u01b4\3\2\2\2\u008f\u01ba\3\2\2\2\u0091\u01bc")
        buf.write("\3\2\2\2\u0093\u01ca\3\2\2\2\u0095\u01d5\3\2\2\2\u0097")
        buf.write("\u01e1\3\2\2\2\u0099\u01ea\3\2\2\2\u009b\u0200\3\2\2\2")
        buf.write("\u009d\u020f\3\2\2\2\u009f\u0213\3\2\2\2\u00a1\u022b\3")
        buf.write("\2\2\2\u00a3\u022d\3\2\2\2\u00a5\u0233\3\2\2\2\u00a7\u023b")
        buf.write("\3\2\2\2\u00a9\u0241\3\2\2\2\u00ab\u0244\3\2\2\2\u00ad")
        buf.write("\u0250\3\2\2\2\u00af\u00b0\7\60\2\2\u00b0\u00b1\7\60\2")
        buf.write("\2\u00b1\4\3\2\2\2\u00b2\u00b5\5\23\n\2\u00b3\u00b5\5")
        buf.write("\25\13\2\u00b4\u00b2\3\2\2\2\u00b4\u00b3\3\2\2\2\u00b5")
        buf.write("\6\3\2\2\2\u00b6\u00b7\7D\2\2\u00b7\u00b8\7t\2\2\u00b8")
        buf.write("\u00b9\7g\2\2\u00b9\u00ba\7c\2\2\u00ba\u00bb\7m\2\2\u00bb")
        buf.write("\b\3\2\2\2\u00bc\u00bd\7E\2\2\u00bd\u00be\7q\2\2\u00be")
        buf.write("\u00bf\7p\2\2\u00bf\u00c0\7v\2\2\u00c0\u00c1\7k\2\2\u00c1")
        buf.write("\u00c2\7p\2\2\u00c2\u00c3\7w\2\2\u00c3\u00c4\7g\2\2\u00c4")
        buf.write("\n\3\2\2\2\u00c5\u00c6\7K\2\2\u00c6\u00c7\7h\2\2\u00c7")
        buf.write("\f\3\2\2\2\u00c8\u00c9\7G\2\2\u00c9\u00ca\7n\2\2\u00ca")
        buf.write("\u00cb\7u\2\2\u00cb\u00cc\7g\2\2\u00cc\u00cd\7k\2\2\u00cd")
        buf.write("\u00ce\7h\2\2\u00ce\16\3\2\2\2\u00cf\u00d0\7G\2\2\u00d0")
        buf.write("\u00d1\7n\2\2\u00d1\u00d2\7u\2\2\u00d2\u00d3\7g\2\2\u00d3")
        buf.write("\20\3\2\2\2\u00d4\u00d5\7H\2\2\u00d5\u00d6\7q\2\2\u00d6")
        buf.write("\u00d7\7t\2\2\u00d7\u00d8\7g\2\2\u00d8\u00d9\7c\2\2\u00d9")
        buf.write("\u00da\7e\2\2\u00da\u00db\7j\2\2\u00db\22\3\2\2\2\u00dc")
        buf.write("\u00dd\7V\2\2\u00dd\u00de\7t\2\2\u00de\u00df\7w\2\2\u00df")
        buf.write("\u00e0\7g\2\2\u00e0\24\3\2\2\2\u00e1\u00e2\7H\2\2\u00e2")
        buf.write("\u00e3\7c\2\2\u00e3\u00e4\7n\2\2\u00e4\u00e5\7u\2\2\u00e5")
        buf.write("\u00e6\7g\2\2\u00e6\26\3\2\2\2\u00e7\u00e8\7C\2\2\u00e8")
        buf.write("\u00e9\7t\2\2\u00e9\u00ea\7t\2\2\u00ea\u00eb\7c\2\2\u00eb")
        buf.write("\u00ec\7{\2\2\u00ec\30\3\2\2\2\u00ed\u00ee\7K\2\2\u00ee")
        buf.write("\u00ef\7p\2\2\u00ef\32\3\2\2\2\u00f0\u00f1\7K\2\2\u00f1")
        buf.write("\u00f2\7p\2\2\u00f2\u00f3\7v\2\2\u00f3\34\3\2\2\2\u00f4")
        buf.write("\u00f5\7H\2\2\u00f5\u00f6\7n\2\2\u00f6\u00f7\7q\2\2\u00f7")
        buf.write("\u00f8\7c\2\2\u00f8\u00f9\7v\2\2\u00f9\36\3\2\2\2\u00fa")
        buf.write("\u00fb\7D\2\2\u00fb\u00fc\7q\2\2\u00fc\u00fd\7q\2\2\u00fd")
        buf.write("\u00fe\7n\2\2\u00fe\u00ff\7g\2\2\u00ff\u0100\7c\2\2\u0100")
        buf.write("\u0101\7p\2\2\u0101 \3\2\2\2\u0102\u0103\7U\2\2\u0103")
        buf.write("\u0104\7v\2\2\u0104\u0105\7t\2\2\u0105\u0106\7k\2\2\u0106")
        buf.write("\u0107\7p\2\2\u0107\u0108\7i\2\2\u0108\"\3\2\2\2\u0109")
        buf.write("\u010a\7T\2\2\u010a\u010b\7g\2\2\u010b\u010c\7v\2\2\u010c")
        buf.write("\u010d\7w\2\2\u010d\u010e\7t\2\2\u010e\u010f\7p\2\2\u010f")
        buf.write("$\3\2\2\2\u0110\u0111\7P\2\2\u0111\u0112\7w\2\2\u0112")
        buf.write("\u0113\7n\2\2\u0113\u0114\7n\2\2\u0114&\3\2\2\2\u0115")
        buf.write("\u0116\7E\2\2\u0116\u0117\7n\2\2\u0117\u0118\7c\2\2\u0118")
        buf.write("\u0119\7u\2\2\u0119\u011a\7u\2\2\u011a(\3\2\2\2\u011b")
        buf.write("\u011c\7X\2\2\u011c\u011d\7c\2\2\u011d\u011e\7n\2\2\u011e")
        buf.write("*\3\2\2\2\u011f\u0120\7X\2\2\u0120\u0121\7c\2\2\u0121")
        buf.write("\u0122\7t\2\2\u0122,\3\2\2\2\u0123\u0124\7E\2\2\u0124")
        buf.write("\u0125\7q\2\2\u0125\u0126\7p\2\2\u0126\u0127\7u\2\2\u0127")
        buf.write("\u0128\7v\2\2\u0128\u0129\7t\2\2\u0129\u012a\7w\2\2\u012a")
        buf.write("\u012b\7e\2\2\u012b\u012c\7v\2\2\u012c\u012d\7q\2\2\u012d")
        buf.write("\u012e\7t\2\2\u012e.\3\2\2\2\u012f\u0130\7F\2\2\u0130")
        buf.write("\u0131\7g\2\2\u0131\u0132\7u\2\2\u0132\u0133\7v\2\2\u0133")
        buf.write("\u0134\7t\2\2\u0134\u0135\7w\2\2\u0135\u0136\7e\2\2\u0136")
        buf.write("\u0137\7v\2\2\u0137\u0138\7q\2\2\u0138\u0139\7t\2\2\u0139")
        buf.write("\60\3\2\2\2\u013a\u013b\7P\2\2\u013b\u013c\7g\2\2\u013c")
        buf.write("\u013d\7y\2\2\u013d\62\3\2\2\2\u013e\u013f\7D\2\2\u013f")
        buf.write("\u0140\7{\2\2\u0140\64\3\2\2\2\u0141\u0142\7U\2\2\u0142")
        buf.write("\u0143\7g\2\2\u0143\u0144\7n\2\2\u0144\u0145\7h\2\2\u0145")
        buf.write("\66\3\2\2\2\u0146\u0147\7&\2\2\u01478\3\2\2\2\u0148\u0149")
        buf.write("\7-\2\2\u0149:\3\2\2\2\u014a\u014b\7/\2\2\u014b<\3\2\2")
        buf.write("\2\u014c\u014d\7,\2\2\u014d>\3\2\2\2\u014e\u014f\7\61")
        buf.write("\2\2\u014f@\3\2\2\2\u0150\u0151\7\'\2\2\u0151B\3\2\2\2")
        buf.write("\u0152\u0153\7?\2\2\u0153\u0154\7?\2\2\u0154D\3\2\2\2")
        buf.write("\u0155\u0156\7#\2\2\u0156\u0157\7?\2\2\u0157F\3\2\2\2")
        buf.write("\u0158\u0159\7@\2\2\u0159H\3\2\2\2\u015a\u015b\7@\2\2")
        buf.write("\u015b\u015c\7?\2\2\u015cJ\3\2\2\2\u015d\u015e\7>\2\2")
        buf.write("\u015eL\3\2\2\2\u015f\u0160\7>\2\2\u0160\u0161\7?\2\2")
        buf.write("\u0161N\3\2\2\2\u0162\u0163\7-\2\2\u0163\u0164\7\60\2")
        buf.write("\2\u0164P\3\2\2\2\u0165\u0166\7?\2\2\u0166\u0167\7?\2")
        buf.write("\2\u0167\u0168\7\60\2\2\u0168R\3\2\2\2\u0169\u016a\7#")
        buf.write("\2\2\u016aT\3\2\2\2\u016b\u016c\7(\2\2\u016c\u016d\7(")
        buf.write("\2\2\u016dV\3\2\2\2\u016e\u016f\7~\2\2\u016f\u0170\7~")
        buf.write("\2\2\u0170X\3\2\2\2\u0171\u0172\7<\2\2\u0172Z\3\2\2\2")
        buf.write("\u0173\u0174\7?\2\2\u0174\\\3\2\2\2\u0175\u0176\7<\2\2")
        buf.write("\u0176\u0177\7<\2\2\u0177^\3\2\2\2\u0178\u0179\7*\2\2")
        buf.write("\u0179`\3\2\2\2\u017a\u017b\7+\2\2\u017bb\3\2\2\2\u017c")
        buf.write("\u017d\7]\2\2\u017dd\3\2\2\2\u017e\u017f\7_\2\2\u017f")
        buf.write("f\3\2\2\2\u0180\u0181\7}\2\2\u0181h\3\2\2\2\u0182\u0183")
        buf.write("\7\177\2\2\u0183j\3\2\2\2\u0184\u0185\7=\2\2\u0185l\3")
        buf.write("\2\2\2\u0186\u0187\7.\2\2\u0187n\3\2\2\2\u0188\u0189\7")
        buf.write("\60\2\2\u0189p\3\2\2\2\u018a\u018b\t\2\2\2\u018br\3\2")
        buf.write("\2\2\u018c\u018d\t\3\2\2\u018dt\3\2\2\2\u018e\u018f\t")
        buf.write("\4\2\2\u018fv\3\2\2\2\u0190\u0191\t\5\2\2\u0191x\3\2\2")
        buf.write("\2\u0192\u0193\t\6\2\2\u0193z\3\2\2\2\u0194\u0195\t\7")
        buf.write("\2\2\u0195|\3\2\2\2\u0196\u0197\t\b\2\2\u0197~\3\2\2\2")
        buf.write("\u0198\u0199\t\t\2\2\u0199\u0080\3\2\2\2\u019a\u019b\t")
        buf.write("\n\2\2\u019b\u0082\3\2\2\2\u019c\u019e\t\13\2\2\u019d")
        buf.write("\u019f\7/\2\2\u019e\u019d\3\2\2\2\u019e\u019f\3\2\2\2")
        buf.write("\u019f\u01a1\3\2\2\2\u01a0\u01a2\5q9\2\u01a1\u01a0\3\2")
        buf.write("\2\2\u01a2\u01a3\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a3\u01a4")
        buf.write("\3\2\2\2\u01a4\u0084\3\2\2\2\u01a5\u01a9\5o8\2\u01a6\u01a8")
        buf.write("\5q9\2\u01a7\u01a6\3\2\2\2\u01a8\u01ab\3\2\2\2\u01a9\u01a7")
        buf.write("\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u0086\3\2\2\2\u01ab")
        buf.write("\u01a9\3\2\2\2\u01ac\u01ad\7$\2\2\u01ad\u0088\3\2\2\2")
        buf.write("\u01ae\u01af\7^\2\2\u01af\u01b0\n\f\2\2\u01b0\u008a\3")
        buf.write("\2\2\2\u01b1\u01b2\7)\2\2\u01b2\u01b3\7$\2\2\u01b3\u008c")
        buf.write("\3\2\2\2\u01b4\u01b5\7^\2\2\u01b5\u01b6\t\f\2\2\u01b6")
        buf.write("\u008e\3\2\2\2\u01b7\u01bb\n\r\2\2\u01b8\u01bb\5\u008d")
        buf.write("G\2\u01b9\u01bb\5\u008bF\2\u01ba\u01b7\3\2\2\2\u01ba\u01b8")
        buf.write("\3\2\2\2\u01ba\u01b9\3\2\2\2\u01bb\u0090\3\2\2\2\u01bc")
        buf.write("\u01bd\7%\2\2\u01bd\u01be\7%\2\2\u01be\u01c2\3\2\2\2\u01bf")
        buf.write("\u01c1\13\2\2\2\u01c0\u01bf\3\2\2\2\u01c1\u01c4\3\2\2")
        buf.write("\2\u01c2\u01c3\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c3\u01c5")
        buf.write("\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c5\u01c6\7%\2\2\u01c6")
        buf.write("\u01c7\7%\2\2\u01c7\u01c8\3\2\2\2\u01c8\u01c9\bI\2\2\u01c9")
        buf.write("\u0092\3\2\2\2\u01ca\u01cb\7\62\2\2\u01cb\u01d2\5w<\2")
        buf.write("\u01cc\u01ce\7a\2\2\u01cd\u01cc\3\2\2\2\u01cd\u01ce\3")
        buf.write("\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01d1\5u;\2\u01d0\u01cd")
        buf.write("\3\2\2\2\u01d1\u01d4\3\2\2\2\u01d2\u01d0\3\2\2\2\u01d2")
        buf.write("\u01d3\3\2\2\2\u01d3\u0094\3\2\2\2\u01d4\u01d2\3\2\2\2")
        buf.write("\u01d5\u01d6\7\62\2\2\u01d6\u01d7\t\16\2\2\u01d7\u01de")
        buf.write("\7\63\2\2\u01d8\u01da\7a\2\2\u01d9\u01d8\3\2\2\2\u01d9")
        buf.write("\u01da\3\2\2\2\u01da\u01db\3\2\2\2\u01db\u01dd\5s:\2\u01dc")
        buf.write("\u01d9\3\2\2\2\u01dd\u01e0\3\2\2\2\u01de\u01dc\3\2\2\2")
        buf.write("\u01de\u01df\3\2\2\2\u01df\u0096\3\2\2\2\u01e0\u01de\3")
        buf.write("\2\2\2\u01e1\u01e7\5y=\2\u01e2\u01e3\7a\2\2\u01e3\u01e6")
        buf.write("\5q9\2\u01e4\u01e6\5q9\2\u01e5\u01e2\3\2\2\2\u01e5\u01e4")
        buf.write("\3\2\2\2\u01e6\u01e9\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e7")
        buf.write("\u01e8\3\2\2\2\u01e8\u0098\3\2\2\2\u01e9\u01e7\3\2\2\2")
        buf.write("\u01ea\u01eb\7\62\2\2\u01eb\u01ee\t\17\2\2\u01ec\u01ef")
        buf.write("\5y=\2\u01ed\u01ef\5\177@\2\u01ee\u01ec\3\2\2\2\u01ee")
        buf.write("\u01ed\3\2\2\2\u01ef\u01f9\3\2\2\2\u01f0\u01f2\7a\2\2")
        buf.write("\u01f1\u01f0\3\2\2\2\u01f1\u01f2\3\2\2\2\u01f2\u01f5\3")
        buf.write("\2\2\2\u01f3\u01f6\5q9\2\u01f4\u01f6\5\177@\2\u01f5\u01f3")
        buf.write("\3\2\2\2\u01f5\u01f4\3\2\2\2\u01f6\u01f8\3\2\2\2\u01f7")
        buf.write("\u01f1\3\2\2\2\u01f8\u01fb\3\2\2\2\u01f9\u01f7\3\2\2\2")
        buf.write("\u01f9\u01fa\3\2\2\2\u01fa\u009a\3\2\2\2\u01fb\u01f9\3")
        buf.write("\2\2\2\u01fc\u0201\5\u0093J\2\u01fd\u0201\5\u0095K\2\u01fe")
        buf.write("\u0201\5\u0097L\2\u01ff\u0201\5\u0099M\2\u0200\u01fc\3")
        buf.write("\2\2\2\u0200\u01fd\3\2\2\2\u0200\u01fe\3\2\2\2\u0200\u01ff")
        buf.write("\3\2\2\2\u0201\u0202\3\2\2\2\u0202\u0203\bN\3\2\u0203")
        buf.write("\u009c\3\2\2\2\u0204\u020a\5\u0097L\2\u0205\u020b\5\u0085")
        buf.write("C\2\u0206\u020b\5\u0083B\2\u0207\u0208\5\u0085C\2\u0208")
        buf.write("\u0209\5\u0083B\2\u0209\u020b\3\2\2\2\u020a\u0205\3\2")
        buf.write("\2\2\u020a\u0206\3\2\2\2\u020a\u0207\3\2\2\2\u020b\u0210")
        buf.write("\3\2\2\2\u020c\u020d\5\u0085C\2\u020d\u020e\5\u0083B\2")
        buf.write("\u020e\u0210\3\2\2\2\u020f\u0204\3\2\2\2\u020f\u020c\3")
        buf.write("\2\2\2\u0210\u0211\3\2\2\2\u0211\u0212\bO\4\2\u0212\u009e")
        buf.write("\3\2\2\2\u0213\u0217\5\u0087D\2\u0214\u0216\5\u008fH\2")
        buf.write("\u0215\u0214\3\2\2\2\u0216\u0219\3\2\2\2\u0217\u0215\3")
        buf.write("\2\2\2\u0217\u0218\3\2\2\2\u0218\u021a\3\2\2\2\u0219\u0217")
        buf.write("\3\2\2\2\u021a\u021b\5\u0087D\2\u021b\u00a0\3\2\2\2\u021c")
        buf.write("\u022c\7\62\2\2\u021d\u021e\7\62\2\2\u021e\u022c\7\62")
        buf.write("\2\2\u021f\u0220\7\62\2\2\u0220\u0221\7d\2\2\u0221\u022c")
        buf.write("\7\62\2\2\u0222\u0223\7\62\2\2\u0223\u0224\7D\2\2\u0224")
        buf.write("\u022c\7\62\2\2\u0225\u0226\7\62\2\2\u0226\u0227\7z\2")
        buf.write("\2\u0227\u022c\7\62\2\2\u0228\u0229\7\62\2\2\u0229\u022a")
        buf.write("\7Z\2\2\u022a\u022c\7\62\2\2\u022b\u021c\3\2\2\2\u022b")
        buf.write("\u021d\3\2\2\2\u022b\u021f\3\2\2\2\u022b\u0222\3\2\2\2")
        buf.write("\u022b\u0225\3\2\2\2\u022b\u0228\3\2\2\2\u022c\u00a2\3")
        buf.write("\2\2\2\u022d\u022f\5\67\34\2\u022e\u0230\t\20\2\2\u022f")
        buf.write("\u022e\3\2\2\2\u0230\u0231\3\2\2\2\u0231\u022f\3\2\2\2")
        buf.write("\u0231\u0232\3\2\2\2\u0232\u00a4\3\2\2\2\u0233\u0237\t")
        buf.write("\n\2\2\u0234\u0236\t\20\2\2\u0235\u0234\3\2\2\2\u0236")
        buf.write("\u0239\3\2\2\2\u0237\u0235\3\2\2\2\u0237\u0238\3\2\2\2")
        buf.write("\u0238\u00a6\3\2\2\2\u0239\u0237\3\2\2\2\u023a\u023c\t")
        buf.write("\21\2\2\u023b\u023a\3\2\2\2\u023c\u023d\3\2\2\2\u023d")
        buf.write("\u023b\3\2\2\2\u023d\u023e\3\2\2\2\u023e\u023f\3\2\2\2")
        buf.write("\u023f\u0240\bT\2\2\u0240\u00a8\3\2\2\2\u0241\u0242\13")
        buf.write("\2\2\2\u0242\u0243\bU\5\2\u0243\u00aa\3\2\2\2\u0244\u0248")
        buf.write("\5\u0087D\2\u0245\u0247\5\u008fH\2\u0246\u0245\3\2\2\2")
        buf.write("\u0247\u024a\3\2\2\2\u0248\u0246\3\2\2\2\u0248\u0249\3")
        buf.write("\2\2\2\u0249\u024c\3\2\2\2\u024a\u0248\3\2\2\2\u024b\u024d")
        buf.write("\t\22\2\2\u024c\u024b\3\2\2\2\u024d\u024e\3\2\2\2\u024e")
        buf.write("\u024f\bV\6\2\u024f\u00ac\3\2\2\2\u0250\u0254\5\u0087")
        buf.write("D\2\u0251\u0253\5\u008fH\2\u0252\u0251\3\2\2\2\u0253\u0256")
        buf.write("\3\2\2\2\u0254\u0252\3\2\2\2\u0254\u0255\3\2\2\2\u0255")
        buf.write("\u0257\3\2\2\2\u0256\u0254\3\2\2\2\u0257\u0258\5\u0089")
        buf.write("E\2\u0258\u0259\bW\7\2\u0259\u00ae\3\2\2\2\36\2\u00b4")
        buf.write("\u019e\u01a3\u01a9\u01ba\u01c2\u01cd\u01d2\u01d9\u01de")
        buf.write("\u01e5\u01e7\u01ee\u01f1\u01f5\u01f9\u0200\u020a\u020f")
        buf.write("\u0217\u022b\u0231\u0237\u023d\u0248\u024c\u0254\b\b\2")
        buf.write("\2\3N\2\3O\3\3U\4\3V\5\3W\6")
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
    DOUBLE_QUOTE = 55
    BLOCK_COMMENT = 56
    INTLIT = 57
    FLOATLIT = 58
    STRLIT = 59
    ZERO = 60
    STATIC_ID = 61
    ID = 62
    WS = 63
    ERROR_CHAR = 64
    UNCLOSE_STRING = 65
    ILLEGAL_ESCAPE = 66

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
            "'{'", "'}'", "';'", "','", "'.'", "'\"'" ]

    symbolicNames = [ "<INVALID>",
            "BOOLLIT", "BREAK", "CONTINUE", "IF", "ELSEIF", "ELSE", "FOREACH", 
            "TRUE", "FALSE", "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
            "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
            "NEW", "BY", "SELF", "ADD", "SUB", "MUL", "DIV", "MOD", "EQ", 
            "NEQ", "GT", "GTE", "LT", "LTE", "SADD", "SEQ", "NOT", "AND", 
            "OR", "COLON", "ASSIGN", "SCOPE", "LB", "RB", "LSB", "RSB", 
            "LCB", "RCB", "SM", "CM", "DOT", "DOUBLE_QUOTE", "BLOCK_COMMENT", 
            "INTLIT", "FLOATLIT", "STRLIT", "ZERO", "STATIC_ID", "ID", "WS", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

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
                  "HEXADECIMAL", "INTLIT", "FLOATLIT", "STRLIT", "ZERO", 
                  "STATIC_ID", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
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
            actions[76] = self.INTLIT_action 
            actions[77] = self.FLOATLIT_action 
            actions[83] = self.ERROR_CHAR_action 
            actions[84] = self.UNCLOSE_STRING_action 
            actions[85] = self.ILLEGAL_ESCAPE_action 
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

                    text = str(self.text)
                    if (text[-1] == '\r') or (text[-1] == '\n'):
                        raise UncloseString(text[1:-1])
                    else:
                        raise UncloseString(text[1:])

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 4:

            		illegal_str = str(self.text)
            		raise IllegalEscape(illegal_str[1:])

     


