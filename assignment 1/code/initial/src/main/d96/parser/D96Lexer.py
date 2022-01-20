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
        buf.write("\u0243\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
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
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\3\2")
        buf.write("\3\2\3\2\3\3\3\3\5\3\u00af\n\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\t\3\t\3\t")
        buf.write("\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\25")
        buf.write("\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31\3\31")
        buf.write("\3\31\3\32\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\34\3\34")
        buf.write("\3\35\3\35\3\36\3\36\3\37\3\37\3 \3 \3!\3!\3\"\3\"\3\"")
        buf.write("\3#\3#\3#\3$\3$\3%\3%\3%\3&\3&\3\'\3\'\3\'\3(\3(\3(\3")
        buf.write(")\3)\3)\3)\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3.\3.\3/\3/\3")
        buf.write("/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63\3\64\3\64\3")
        buf.write("\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3")
        buf.write("<\3<\3=\3=\3>\3>\3?\3?\3@\3@\3A\3A\5A\u0197\nA\3A\6A\u019a")
        buf.write("\nA\rA\16A\u019b\3B\3B\7B\u01a0\nB\fB\16B\u01a3\13B\3")
        buf.write("C\3C\3D\3D\3D\5D\u01aa\nD\3E\3E\3E\3F\3F\3F\3G\3G\3G\5")
        buf.write("G\u01b5\nG\3H\3H\3H\3H\7H\u01bb\nH\fH\16H\u01be\13H\3")
        buf.write("H\3H\3H\3H\3H\3I\3I\3I\3I\5I\u01c9\nI\3I\7I\u01cc\nI\f")
        buf.write("I\16I\u01cf\13I\5I\u01d1\nI\3J\3J\3J\3J\3J\5J\u01d8\n")
        buf.write("J\3J\7J\u01db\nJ\fJ\16J\u01de\13J\5J\u01e0\nJ\3K\3K\3")
        buf.write("K\3K\7K\u01e6\nK\fK\16K\u01e9\13K\3K\5K\u01ec\nK\3L\3")
        buf.write("L\3L\3L\3L\5L\u01f3\nL\3L\5L\u01f6\nL\3L\3L\5L\u01fa\n")
        buf.write("L\7L\u01fc\nL\fL\16L\u01ff\13L\5L\u0201\nL\3M\3M\3M\3")
        buf.write("M\5M\u0207\nM\3M\3M\3N\5N\u020c\nN\3N\3N\5N\u0210\nN\3")
        buf.write("N\5N\u0213\nN\3N\3N\3O\3O\7O\u0219\nO\fO\16O\u021c\13")
        buf.write("O\3O\3O\3P\3P\7P\u0222\nP\fP\16P\u0225\13P\3Q\6Q\u0228")
        buf.write("\nQ\rQ\16Q\u0229\3Q\3Q\3R\3R\3R\3S\3S\7S\u0233\nS\fS\16")
        buf.write("S\u0236\13S\3S\3S\3T\3T\7T\u023c\nT\fT\16T\u023f\13T\3")
        buf.write("T\3T\3T\3\u01bc\2U\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write("\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'")
        buf.write("\25)\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ")
        buf.write("?!A\"C#E$G%I&K\'M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g")
        buf.write("\65i\66k\67m8o9q\2s\2u\2w\2y\2{\2}\2\177\2\u0081\2\u0083")
        buf.write("\2\u0085\2\u0087\2\u0089\2\u008b\2\u008d\2\u008f:\u0091")
        buf.write("\2\u0093\2\u0095\2\u0097\2\u0099;\u009b<\u009d=\u009f")
        buf.write(">\u00a1?\u00a3@\u00a5A\u00a7B\3\2\22\3\2\62;\3\2\63;\3")
        buf.write("\2\639\3\2\629\3\2c|\3\2C\\\4\2CHaa\5\2C\\aac|\4\2GGg")
        buf.write("g\b\2))ddhhppttvv\t\2))^^ddhhppttvv\6\2\n\f\16\17$$^^")
        buf.write("\4\2DDdd\4\2ZZzz\6\2\62;C\\aac|\5\2\13\f\16\17\"\"\2\u0250")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2")
        buf.write("\2\2\2_\3\2\2\2\2a\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3")
        buf.write("\2\2\2\2i\3\2\2\2\2k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2\u008f")
        buf.write("\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2\2\2\u009d\3\2\2")
        buf.write("\2\2\u009f\3\2\2\2\2\u00a1\3\2\2\2\2\u00a3\3\2\2\2\2\u00a5")
        buf.write("\3\2\2\2\2\u00a7\3\2\2\2\3\u00a9\3\2\2\2\5\u00ae\3\2\2")
        buf.write("\2\7\u00b0\3\2\2\2\t\u00b6\3\2\2\2\13\u00bf\3\2\2\2\r")
        buf.write("\u00c2\3\2\2\2\17\u00c9\3\2\2\2\21\u00ce\3\2\2\2\23\u00d6")
        buf.write("\3\2\2\2\25\u00db\3\2\2\2\27\u00e1\3\2\2\2\31\u00e7\3")
        buf.write("\2\2\2\33\u00ea\3\2\2\2\35\u00ee\3\2\2\2\37\u00f4\3\2")
        buf.write("\2\2!\u00fc\3\2\2\2#\u0103\3\2\2\2%\u010a\3\2\2\2\'\u010f")
        buf.write("\3\2\2\2)\u0115\3\2\2\2+\u0119\3\2\2\2-\u011d\3\2\2\2")
        buf.write("/\u0129\3\2\2\2\61\u0134\3\2\2\2\63\u0138\3\2\2\2\65\u013b")
        buf.write("\3\2\2\2\67\u0140\3\2\2\29\u0142\3\2\2\2;\u0144\3\2\2")
        buf.write("\2=\u0146\3\2\2\2?\u0148\3\2\2\2A\u014a\3\2\2\2C\u014c")
        buf.write("\3\2\2\2E\u014f\3\2\2\2G\u0152\3\2\2\2I\u0154\3\2\2\2")
        buf.write("K\u0157\3\2\2\2M\u0159\3\2\2\2O\u015c\3\2\2\2Q\u015f\3")
        buf.write("\2\2\2S\u0163\3\2\2\2U\u0165\3\2\2\2W\u0168\3\2\2\2Y\u016b")
        buf.write("\3\2\2\2[\u016d\3\2\2\2]\u016f\3\2\2\2_\u0172\3\2\2\2")
        buf.write("a\u0174\3\2\2\2c\u0176\3\2\2\2e\u0178\3\2\2\2g\u017a\3")
        buf.write("\2\2\2i\u017c\3\2\2\2k\u017e\3\2\2\2m\u0180\3\2\2\2o\u0182")
        buf.write("\3\2\2\2q\u0184\3\2\2\2s\u0186\3\2\2\2u\u0188\3\2\2\2")
        buf.write("w\u018a\3\2\2\2y\u018c\3\2\2\2{\u018e\3\2\2\2}\u0190\3")
        buf.write("\2\2\2\177\u0192\3\2\2\2\u0081\u0194\3\2\2\2\u0083\u019d")
        buf.write("\3\2\2\2\u0085\u01a4\3\2\2\2\u0087\u01a6\3\2\2\2\u0089")
        buf.write("\u01ab\3\2\2\2\u008b\u01ae\3\2\2\2\u008d\u01b4\3\2\2\2")
        buf.write("\u008f\u01b6\3\2\2\2\u0091\u01c4\3\2\2\2\u0093\u01d2\3")
        buf.write("\2\2\2\u0095\u01eb\3\2\2\2\u0097\u01ed\3\2\2\2\u0099\u0206")
        buf.write("\3\2\2\2\u009b\u020b\3\2\2\2\u009d\u0216\3\2\2\2\u009f")
        buf.write("\u021f\3\2\2\2\u00a1\u0227\3\2\2\2\u00a3\u022d\3\2\2\2")
        buf.write("\u00a5\u0230\3\2\2\2\u00a7\u0239\3\2\2\2\u00a9\u00aa\7")
        buf.write("\60\2\2\u00aa\u00ab\7\60\2\2\u00ab\4\3\2\2\2\u00ac\u00af")
        buf.write("\5\23\n\2\u00ad\u00af\5\25\13\2\u00ae\u00ac\3\2\2\2\u00ae")
        buf.write("\u00ad\3\2\2\2\u00af\6\3\2\2\2\u00b0\u00b1\7D\2\2\u00b1")
        buf.write("\u00b2\7t\2\2\u00b2\u00b3\7g\2\2\u00b3\u00b4\7c\2\2\u00b4")
        buf.write("\u00b5\7m\2\2\u00b5\b\3\2\2\2\u00b6\u00b7\7E\2\2\u00b7")
        buf.write("\u00b8\7q\2\2\u00b8\u00b9\7p\2\2\u00b9\u00ba\7v\2\2\u00ba")
        buf.write("\u00bb\7k\2\2\u00bb\u00bc\7p\2\2\u00bc\u00bd\7w\2\2\u00bd")
        buf.write("\u00be\7g\2\2\u00be\n\3\2\2\2\u00bf\u00c0\7K\2\2\u00c0")
        buf.write("\u00c1\7h\2\2\u00c1\f\3\2\2\2\u00c2\u00c3\7G\2\2\u00c3")
        buf.write("\u00c4\7n\2\2\u00c4\u00c5\7u\2\2\u00c5\u00c6\7g\2\2\u00c6")
        buf.write("\u00c7\7k\2\2\u00c7\u00c8\7h\2\2\u00c8\16\3\2\2\2\u00c9")
        buf.write("\u00ca\7G\2\2\u00ca\u00cb\7n\2\2\u00cb\u00cc\7u\2\2\u00cc")
        buf.write("\u00cd\7g\2\2\u00cd\20\3\2\2\2\u00ce\u00cf\7H\2\2\u00cf")
        buf.write("\u00d0\7q\2\2\u00d0\u00d1\7t\2\2\u00d1\u00d2\7g\2\2\u00d2")
        buf.write("\u00d3\7c\2\2\u00d3\u00d4\7e\2\2\u00d4\u00d5\7j\2\2\u00d5")
        buf.write("\22\3\2\2\2\u00d6\u00d7\7V\2\2\u00d7\u00d8\7t\2\2\u00d8")
        buf.write("\u00d9\7w\2\2\u00d9\u00da\7g\2\2\u00da\24\3\2\2\2\u00db")
        buf.write("\u00dc\7H\2\2\u00dc\u00dd\7c\2\2\u00dd\u00de\7n\2\2\u00de")
        buf.write("\u00df\7u\2\2\u00df\u00e0\7g\2\2\u00e0\26\3\2\2\2\u00e1")
        buf.write("\u00e2\7C\2\2\u00e2\u00e3\7t\2\2\u00e3\u00e4\7t\2\2\u00e4")
        buf.write("\u00e5\7c\2\2\u00e5\u00e6\7{\2\2\u00e6\30\3\2\2\2\u00e7")
        buf.write("\u00e8\7K\2\2\u00e8\u00e9\7p\2\2\u00e9\32\3\2\2\2\u00ea")
        buf.write("\u00eb\7K\2\2\u00eb\u00ec\7p\2\2\u00ec\u00ed\7v\2\2\u00ed")
        buf.write("\34\3\2\2\2\u00ee\u00ef\7H\2\2\u00ef\u00f0\7n\2\2\u00f0")
        buf.write("\u00f1\7q\2\2\u00f1\u00f2\7c\2\2\u00f2\u00f3\7v\2\2\u00f3")
        buf.write("\36\3\2\2\2\u00f4\u00f5\7D\2\2\u00f5\u00f6\7q\2\2\u00f6")
        buf.write("\u00f7\7q\2\2\u00f7\u00f8\7n\2\2\u00f8\u00f9\7g\2\2\u00f9")
        buf.write("\u00fa\7c\2\2\u00fa\u00fb\7p\2\2\u00fb \3\2\2\2\u00fc")
        buf.write("\u00fd\7U\2\2\u00fd\u00fe\7v\2\2\u00fe\u00ff\7t\2\2\u00ff")
        buf.write("\u0100\7k\2\2\u0100\u0101\7p\2\2\u0101\u0102\7i\2\2\u0102")
        buf.write("\"\3\2\2\2\u0103\u0104\7T\2\2\u0104\u0105\7g\2\2\u0105")
        buf.write("\u0106\7v\2\2\u0106\u0107\7w\2\2\u0107\u0108\7t\2\2\u0108")
        buf.write("\u0109\7p\2\2\u0109$\3\2\2\2\u010a\u010b\7P\2\2\u010b")
        buf.write("\u010c\7w\2\2\u010c\u010d\7n\2\2\u010d\u010e\7n\2\2\u010e")
        buf.write("&\3\2\2\2\u010f\u0110\7E\2\2\u0110\u0111\7n\2\2\u0111")
        buf.write("\u0112\7c\2\2\u0112\u0113\7u\2\2\u0113\u0114\7u\2\2\u0114")
        buf.write("(\3\2\2\2\u0115\u0116\7X\2\2\u0116\u0117\7c\2\2\u0117")
        buf.write("\u0118\7n\2\2\u0118*\3\2\2\2\u0119\u011a\7X\2\2\u011a")
        buf.write("\u011b\7c\2\2\u011b\u011c\7t\2\2\u011c,\3\2\2\2\u011d")
        buf.write("\u011e\7E\2\2\u011e\u011f\7q\2\2\u011f\u0120\7p\2\2\u0120")
        buf.write("\u0121\7u\2\2\u0121\u0122\7v\2\2\u0122\u0123\7t\2\2\u0123")
        buf.write("\u0124\7w\2\2\u0124\u0125\7e\2\2\u0125\u0126\7v\2\2\u0126")
        buf.write("\u0127\7q\2\2\u0127\u0128\7t\2\2\u0128.\3\2\2\2\u0129")
        buf.write("\u012a\7F\2\2\u012a\u012b\7g\2\2\u012b\u012c\7u\2\2\u012c")
        buf.write("\u012d\7v\2\2\u012d\u012e\7t\2\2\u012e\u012f\7w\2\2\u012f")
        buf.write("\u0130\7e\2\2\u0130\u0131\7v\2\2\u0131\u0132\7q\2\2\u0132")
        buf.write("\u0133\7t\2\2\u0133\60\3\2\2\2\u0134\u0135\7P\2\2\u0135")
        buf.write("\u0136\7g\2\2\u0136\u0137\7y\2\2\u0137\62\3\2\2\2\u0138")
        buf.write("\u0139\7D\2\2\u0139\u013a\7{\2\2\u013a\64\3\2\2\2\u013b")
        buf.write("\u013c\7U\2\2\u013c\u013d\7g\2\2\u013d\u013e\7n\2\2\u013e")
        buf.write("\u013f\7h\2\2\u013f\66\3\2\2\2\u0140\u0141\7&\2\2\u0141")
        buf.write("8\3\2\2\2\u0142\u0143\7-\2\2\u0143:\3\2\2\2\u0144\u0145")
        buf.write("\7/\2\2\u0145<\3\2\2\2\u0146\u0147\7,\2\2\u0147>\3\2\2")
        buf.write("\2\u0148\u0149\7\61\2\2\u0149@\3\2\2\2\u014a\u014b\7\'")
        buf.write("\2\2\u014bB\3\2\2\2\u014c\u014d\7?\2\2\u014d\u014e\7?")
        buf.write("\2\2\u014eD\3\2\2\2\u014f\u0150\7#\2\2\u0150\u0151\7?")
        buf.write("\2\2\u0151F\3\2\2\2\u0152\u0153\7@\2\2\u0153H\3\2\2\2")
        buf.write("\u0154\u0155\7@\2\2\u0155\u0156\7?\2\2\u0156J\3\2\2\2")
        buf.write("\u0157\u0158\7>\2\2\u0158L\3\2\2\2\u0159\u015a\7>\2\2")
        buf.write("\u015a\u015b\7?\2\2\u015bN\3\2\2\2\u015c\u015d\7-\2\2")
        buf.write("\u015d\u015e\7\60\2\2\u015eP\3\2\2\2\u015f\u0160\7?\2")
        buf.write("\2\u0160\u0161\7?\2\2\u0161\u0162\7\60\2\2\u0162R\3\2")
        buf.write("\2\2\u0163\u0164\7#\2\2\u0164T\3\2\2\2\u0165\u0166\7(")
        buf.write("\2\2\u0166\u0167\7(\2\2\u0167V\3\2\2\2\u0168\u0169\7~")
        buf.write("\2\2\u0169\u016a\7~\2\2\u016aX\3\2\2\2\u016b\u016c\7<")
        buf.write("\2\2\u016cZ\3\2\2\2\u016d\u016e\7?\2\2\u016e\\\3\2\2\2")
        buf.write("\u016f\u0170\7<\2\2\u0170\u0171\7<\2\2\u0171^\3\2\2\2")
        buf.write("\u0172\u0173\7*\2\2\u0173`\3\2\2\2\u0174\u0175\7+\2\2")
        buf.write("\u0175b\3\2\2\2\u0176\u0177\7]\2\2\u0177d\3\2\2\2\u0178")
        buf.write("\u0179\7_\2\2\u0179f\3\2\2\2\u017a\u017b\7}\2\2\u017b")
        buf.write("h\3\2\2\2\u017c\u017d\7\177\2\2\u017dj\3\2\2\2\u017e\u017f")
        buf.write("\7=\2\2\u017fl\3\2\2\2\u0180\u0181\7.\2\2\u0181n\3\2\2")
        buf.write("\2\u0182\u0183\7\60\2\2\u0183p\3\2\2\2\u0184\u0185\t\2")
        buf.write("\2\2\u0185r\3\2\2\2\u0186\u0187\t\3\2\2\u0187t\3\2\2\2")
        buf.write("\u0188\u0189\t\4\2\2\u0189v\3\2\2\2\u018a\u018b\t\5\2")
        buf.write("\2\u018bx\3\2\2\2\u018c\u018d\t\6\2\2\u018dz\3\2\2\2\u018e")
        buf.write("\u018f\t\7\2\2\u018f|\3\2\2\2\u0190\u0191\t\b\2\2\u0191")
        buf.write("~\3\2\2\2\u0192\u0193\t\t\2\2\u0193\u0080\3\2\2\2\u0194")
        buf.write("\u0196\t\n\2\2\u0195\u0197\7/\2\2\u0196\u0195\3\2\2\2")
        buf.write("\u0196\u0197\3\2\2\2\u0197\u0199\3\2\2\2\u0198\u019a\5")
        buf.write("q9\2\u0199\u0198\3\2\2\2\u019a\u019b\3\2\2\2\u019b\u0199")
        buf.write("\3\2\2\2\u019b\u019c\3\2\2\2\u019c\u0082\3\2\2\2\u019d")
        buf.write("\u01a1\5o8\2\u019e\u01a0\5q9\2\u019f\u019e\3\2\2\2\u01a0")
        buf.write("\u01a3\3\2\2\2\u01a1\u019f\3\2\2\2\u01a1\u01a2\3\2\2\2")
        buf.write("\u01a2\u0084\3\2\2\2\u01a3\u01a1\3\2\2\2\u01a4\u01a5\7")
        buf.write("$\2\2\u01a5\u0086\3\2\2\2\u01a6\u01a9\7^\2\2\u01a7\u01aa")
        buf.write("\n\13\2\2\u01a8\u01aa\7^\2\2\u01a9\u01a7\3\2\2\2\u01a9")
        buf.write("\u01a8\3\2\2\2\u01aa\u0088\3\2\2\2\u01ab\u01ac\7)\2\2")
        buf.write("\u01ac\u01ad\7$\2\2\u01ad\u008a\3\2\2\2\u01ae\u01af\7")
        buf.write("^\2\2\u01af\u01b0\t\f\2\2\u01b0\u008c\3\2\2\2\u01b1\u01b5")
        buf.write("\n\r\2\2\u01b2\u01b5\5\u008bF\2\u01b3\u01b5\5\u0089E\2")
        buf.write("\u01b4\u01b1\3\2\2\2\u01b4\u01b2\3\2\2\2\u01b4\u01b3\3")
        buf.write("\2\2\2\u01b5\u008e\3\2\2\2\u01b6\u01b7\7%\2\2\u01b7\u01b8")
        buf.write("\7%\2\2\u01b8\u01bc\3\2\2\2\u01b9\u01bb\13\2\2\2\u01ba")
        buf.write("\u01b9\3\2\2\2\u01bb\u01be\3\2\2\2\u01bc\u01bd\3\2\2\2")
        buf.write("\u01bc\u01ba\3\2\2\2\u01bd\u01bf\3\2\2\2\u01be\u01bc\3")
        buf.write("\2\2\2\u01bf\u01c0\7%\2\2\u01c0\u01c1\7%\2\2\u01c1\u01c2")
        buf.write("\3\2\2\2\u01c2\u01c3\bH\2\2\u01c3\u0090\3\2\2\2\u01c4")
        buf.write("\u01d0\7\62\2\2\u01c5\u01d1\7\62\2\2\u01c6\u01cd\5u;\2")
        buf.write("\u01c7\u01c9\7a\2\2\u01c8\u01c7\3\2\2\2\u01c8\u01c9\3")
        buf.write("\2\2\2\u01c9\u01ca\3\2\2\2\u01ca\u01cc\5w<\2\u01cb\u01c8")
        buf.write("\3\2\2\2\u01cc\u01cf\3\2\2\2\u01cd\u01cb\3\2\2\2\u01cd")
        buf.write("\u01ce\3\2\2\2\u01ce\u01d1\3\2\2\2\u01cf\u01cd\3\2\2\2")
        buf.write("\u01d0\u01c5\3\2\2\2\u01d0\u01c6\3\2\2\2\u01d1\u0092\3")
        buf.write("\2\2\2\u01d2\u01d3\7\62\2\2\u01d3\u01df\t\16\2\2\u01d4")
        buf.write("\u01e0\7\62\2\2\u01d5\u01dc\7\63\2\2\u01d6\u01d8\7a\2")
        buf.write("\2\u01d7\u01d6\3\2\2\2\u01d7\u01d8\3\2\2\2\u01d8\u01d9")
        buf.write("\3\2\2\2\u01d9\u01db\4\62\63\2\u01da\u01d7\3\2\2\2\u01db")
        buf.write("\u01de\3\2\2\2\u01dc\u01da\3\2\2\2\u01dc\u01dd\3\2\2\2")
        buf.write("\u01dd\u01e0\3\2\2\2\u01de\u01dc\3\2\2\2\u01df\u01d4\3")
        buf.write("\2\2\2\u01df\u01d5\3\2\2\2\u01e0\u0094\3\2\2\2\u01e1\u01e7")
        buf.write("\5s:\2\u01e2\u01e3\7a\2\2\u01e3\u01e6\5q9\2\u01e4\u01e6")
        buf.write("\5q9\2\u01e5\u01e2\3\2\2\2\u01e5\u01e4\3\2\2\2\u01e6\u01e9")
        buf.write("\3\2\2\2\u01e7\u01e5\3\2\2\2\u01e7\u01e8\3\2\2\2\u01e8")
        buf.write("\u01ec\3\2\2\2\u01e9\u01e7\3\2\2\2\u01ea\u01ec\7\62\2")
        buf.write("\2\u01eb\u01e1\3\2\2\2\u01eb\u01ea\3\2\2\2\u01ec\u0096")
        buf.write("\3\2\2\2\u01ed\u01ee\7\62\2\2\u01ee\u0200\t\17\2\2\u01ef")
        buf.write("\u0201\7\62\2\2\u01f0\u01f3\5s:\2\u01f1\u01f3\5}?\2\u01f2")
        buf.write("\u01f0\3\2\2\2\u01f2\u01f1\3\2\2\2\u01f3\u01fd\3\2\2\2")
        buf.write("\u01f4\u01f6\7a\2\2\u01f5\u01f4\3\2\2\2\u01f5\u01f6\3")
        buf.write("\2\2\2\u01f6\u01f9\3\2\2\2\u01f7\u01fa\5q9\2\u01f8\u01fa")
        buf.write("\5}?\2\u01f9\u01f7\3\2\2\2\u01f9\u01f8\3\2\2\2\u01fa\u01fc")
        buf.write("\3\2\2\2\u01fb\u01f5\3\2\2\2\u01fc\u01ff\3\2\2\2\u01fd")
        buf.write("\u01fb\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe\u0201\3\2\2\2")
        buf.write("\u01ff\u01fd\3\2\2\2\u0200\u01ef\3\2\2\2\u0200\u01f2\3")
        buf.write("\2\2\2\u0201\u0098\3\2\2\2\u0202\u0207\5\u0091I\2\u0203")
        buf.write("\u0207\5\u0093J\2\u0204\u0207\5\u0095K\2\u0205\u0207\5")
        buf.write("\u0097L\2\u0206\u0202\3\2\2\2\u0206\u0203\3\2\2\2\u0206")
        buf.write("\u0204\3\2\2\2\u0206\u0205\3\2\2\2\u0207\u0208\3\2\2\2")
        buf.write("\u0208\u0209\bM\3\2\u0209\u009a\3\2\2\2\u020a\u020c\5")
        buf.write("\u0095K\2\u020b\u020a\3\2\2\2\u020b\u020c\3\2\2\2\u020c")
        buf.write("\u0212\3\2\2\2\u020d\u020f\5\u0083B\2\u020e\u0210\5\u0081")
        buf.write("A\2\u020f\u020e\3\2\2\2\u020f\u0210\3\2\2\2\u0210\u0213")
        buf.write("\3\2\2\2\u0211\u0213\5\u0081A\2\u0212\u020d\3\2\2\2\u0212")
        buf.write("\u0211\3\2\2\2\u0213\u0214\3\2\2\2\u0214\u0215\bN\4\2")
        buf.write("\u0215\u009c\3\2\2\2\u0216\u021a\5\u0085C\2\u0217\u0219")
        buf.write("\5\u008dG\2\u0218\u0217\3\2\2\2\u0219\u021c\3\2\2\2\u021a")
        buf.write("\u0218\3\2\2\2\u021a\u021b\3\2\2\2\u021b\u021d\3\2\2\2")
        buf.write("\u021c\u021a\3\2\2\2\u021d\u021e\5\u0085C\2\u021e\u009e")
        buf.write("\3\2\2\2\u021f\u0223\t\t\2\2\u0220\u0222\t\20\2\2\u0221")
        buf.write("\u0220\3\2\2\2\u0222\u0225\3\2\2\2\u0223\u0221\3\2\2\2")
        buf.write("\u0223\u0224\3\2\2\2\u0224\u00a0\3\2\2\2\u0225\u0223\3")
        buf.write("\2\2\2\u0226\u0228\t\21\2\2\u0227\u0226\3\2\2\2\u0228")
        buf.write("\u0229\3\2\2\2\u0229\u0227\3\2\2\2\u0229\u022a\3\2\2\2")
        buf.write("\u022a\u022b\3\2\2\2\u022b\u022c\bQ\2\2\u022c\u00a2\3")
        buf.write("\2\2\2\u022d\u022e\13\2\2\2\u022e\u022f\bR\5\2\u022f\u00a4")
        buf.write("\3\2\2\2\u0230\u0234\5\u0085C\2\u0231\u0233\5\u008dG\2")
        buf.write("\u0232\u0231\3\2\2\2\u0233\u0236\3\2\2\2\u0234\u0232\3")
        buf.write("\2\2\2\u0234\u0235\3\2\2\2\u0235\u0237\3\2\2\2\u0236\u0234")
        buf.write("\3\2\2\2\u0237\u0238\bS\6\2\u0238\u00a6\3\2\2\2\u0239")
        buf.write("\u023d\5\u0085C\2\u023a\u023c\5\u008dG\2\u023b\u023a\3")
        buf.write("\2\2\2\u023c\u023f\3\2\2\2\u023d\u023b\3\2\2\2\u023d\u023e")
        buf.write("\3\2\2\2\u023e\u0240\3\2\2\2\u023f\u023d\3\2\2\2\u0240")
        buf.write("\u0241\5\u0087D\2\u0241\u0242\bT\7\2\u0242\u00a8\3\2\2")
        buf.write("\2!\2\u00ae\u0196\u019b\u01a1\u01a9\u01b4\u01bc\u01c8")
        buf.write("\u01cd\u01d0\u01d7\u01dc\u01df\u01e5\u01e7\u01eb\u01f2")
        buf.write("\u01f5\u01f9\u01fd\u0200\u0206\u020b\u020f\u0212\u021a")
        buf.write("\u0223\u0229\u0234\u023d\b\b\2\2\3M\2\3N\3\3R\4\3S\5\3")
        buf.write("T\6")
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
                  "RSB", "LCB", "RCB", "SM", "CM", "DOT", "DIGIT", "DIGIT_19", 
                  "DIGIT_17", "OCTAL_DIGIT", "LOWERCASE", "UPERCASE", "UPERCASE_AF", 
                  "ALPHABET", "SCIENTIFIC", "DECIMAL_POINT", "DOUBLE_QUOTE", 
                  "ILLEGAL_STRING", "QUOTE_IN_STR", "ESC_SEQ", "VALID_STRING", 
                  "BLOCK_COMMENT", "OCTAL", "BINARY", "DECIMAL", "HEXADECIMAL", 
                  "INTLIT", "FLOATLIT", "STRLIT", "ID", "WS", "ERROR_CHAR", 
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
            actions[75] = self.INTLIT_action 
            actions[76] = self.FLOATLIT_action 
            actions[80] = self.ERROR_CHAR_action 
            actions[81] = self.UNCLOSE_STRING_action 
            actions[82] = self.ILLEGAL_ESCAPE_action 
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

     


