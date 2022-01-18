# Generated from c:\Users\Admin\Desktop\P\BK\212\Principles of Programming Languages\Assignment\ppl\assignment 1\code\initial\src\main\d96\parser\D96.g4 by ANTLR 4.8
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
        buf.write("\u0161\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\3\2\3\2\3\2\3\2\3\2\3\2")
        buf.write("\5\2K\n\2\3\2\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\5\3\5\5\5")
        buf.write("W\n\5\3\6\3\6\3\6\5\6\\\n\6\3\6\3\6\3\7\3\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\7\bh\n\b\f\b\16\bk\13\b\3\t\3\t\3\t\3\t")
        buf.write("\3\t\3\t\7\ts\n\t\f\t\16\tv\13\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\5\n\u0080\n\n\3\13\3\13\3\13\3\13\3\13\5\13")
        buf.write("\u0087\n\13\3\13\5\13\u008a\n\13\3\f\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\f\5\f\u0093\n\f\3\r\3\r\3\r\3\r\3\r\5\r\u009a\n\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00a3\n\16\3")
        buf.write("\17\3\17\5\17\u00a7\n\17\3\17\3\17\3\20\3\20\3\20\3\20")
        buf.write("\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20")
        buf.write("\7\20\u00ba\n\20\f\20\16\20\u00bd\13\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\5\21\u00c7\n\21\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u00d3\n\22")
        buf.write("\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24")
        buf.write("\5\24\u00e0\n\24\3\24\3\24\3\24\3\24\3\24\5\24\u00e7\n")
        buf.write("\24\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\5\26\u00f4\n\26\3\26\5\26\u00f7\n\26\3\27\3\27\5")
        buf.write("\27\u00fb\n\27\3\30\3\30\5\30\u00ff\n\30\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\5\31\u0107\n\31\3\31\3\31\3\31\3\32\3")
        buf.write("\32\3\32\3\32\3\32\5\32\u0111\n\32\3\32\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\5\33\u011d\n\33\3\33\3")
        buf.write("\33\3\33\3\33\3\33\3\33\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\35\3\35\3\35\3\35\5\35\u0131\n\35\3\36\3")
        buf.write("\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\5\37\u0140\n\37\3 \3 \3 \7 \u0145\n \f \16 \u0148")
        buf.write("\13 \5 \u014a\n \3!\3!\3!\3!\3!\7!\u0151\n!\f!\16!\u0154")
        buf.write("\13!\5!\u0156\n!\3!\3!\3\"\3\"\3\"\3\"\3\"\5\"\u015f\n")
        buf.write("\"\3\"\2\5\16\20\36#\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\668:<>@B\2\b\3\2\"#\3\2$&\3\2")
        buf.write("\60\61\3\2-.\3\2\'(\3\2),\2\u017b\2D\3\2\2\2\4O\3\2\2")
        buf.write("\2\6Q\3\2\2\2\bV\3\2\2\2\nX\3\2\2\2\f_\3\2\2\2\16a\3\2")
        buf.write("\2\2\20l\3\2\2\2\22\177\3\2\2\2\24\u0089\3\2\2\2\26\u0092")
        buf.write("\3\2\2\2\30\u0099\3\2\2\2\32\u00a2\3\2\2\2\34\u00a6\3")
        buf.write("\2\2\2\36\u00aa\3\2\2\2 \u00c6\3\2\2\2\"\u00d2\3\2\2\2")
        buf.write("$\u00d4\3\2\2\2&\u00e6\3\2\2\2(\u00e8\3\2\2\2*\u00f6\3")
        buf.write("\2\2\2,\u00fa\3\2\2\2.\u00fe\3\2\2\2\60\u0106\3\2\2\2")
        buf.write("\62\u0110\3\2\2\2\64\u011c\3\2\2\2\66\u0124\3\2\2\28\u0130")
        buf.write("\3\2\2\2:\u0132\3\2\2\2<\u013f\3\2\2\2>\u0149\3\2\2\2")
        buf.write("@\u014b\3\2\2\2B\u015e\3\2\2\2DE\5\4\3\2EF\7\3\2\2FG\7")
        buf.write("\64\2\2GH\7\65\2\2HJ\78\2\2IK\5\6\4\2JI\3\2\2\2JK\3\2")
        buf.write("\2\2KL\3\2\2\2LM\79\2\2MN\7\2\2\3N\3\3\2\2\2OP\7\31\2")
        buf.write("\2P\5\3\2\2\2QR\5\n\6\2RS\7:\2\2S\7\3\2\2\2TW\5\n\6\2")
        buf.write("UW\7\5\2\2VT\3\2\2\2VU\3\2\2\2W\t\3\2\2\2XY\7=\2\2Y[\7")
        buf.write("\66\2\2Z\\\5\b\5\2[Z\3\2\2\2[\\\3\2\2\2\\]\3\2\2\2]^\7")
        buf.write("\67\2\2^\13\3\2\2\2_`\5\16\b\2`\r\3\2\2\2ab\b\b\1\2bc")
        buf.write("\5\20\t\2ci\3\2\2\2de\f\4\2\2ef\t\2\2\2fh\5\20\t\2gd\3")
        buf.write("\2\2\2hk\3\2\2\2ig\3\2\2\2ij\3\2\2\2j\17\3\2\2\2ki\3\2")
        buf.write("\2\2lm\b\t\1\2mn\5\22\n\2nt\3\2\2\2op\f\4\2\2pq\t\3\2")
        buf.write("\2qs\5\22\n\2ro\3\2\2\2sv\3\2\2\2tr\3\2\2\2tu\3\2\2\2")
        buf.write("u\21\3\2\2\2vt\3\2\2\2w\u0080\7=\2\2x\u0080\7\5\2\2y\u0080")
        buf.write("\7\6\2\2z\u0080\58\35\2{|\7\64\2\2|}\5\16\b\2}~\7\65\2")
        buf.write("\2~\u0080\3\2\2\2\177w\3\2\2\2\177x\3\2\2\2\177y\3\2\2")
        buf.write("\2\177z\3\2\2\2\177{\3\2\2\2\u0080\23\3\2\2\2\u0081\u0082")
        buf.write("\5\26\f\2\u0082\u0083\t\4\2\2\u0083\u0084\5\24\13\2\u0084")
        buf.write("\u008a\3\2\2\2\u0085\u0087\7/\2\2\u0086\u0085\3\2\2\2")
        buf.write("\u0086\u0087\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u008a\5")
        buf.write("\26\f\2\u0089\u0081\3\2\2\2\u0089\u0086\3\2\2\2\u008a")
        buf.write("\25\3\2\2\2\u008b\u0093\7=\2\2\u008c\u0093\7\7\2\2\u008d")
        buf.write("\u0093\58\35\2\u008e\u008f\7\64\2\2\u008f\u0090\5\24\13")
        buf.write("\2\u0090\u0091\7\65\2\2\u0091\u0093\3\2\2\2\u0092\u008b")
        buf.write("\3\2\2\2\u0092\u008c\3\2\2\2\u0092\u008d\3\2\2\2\u0092")
        buf.write("\u008e\3\2\2\2\u0093\27\3\2\2\2\u0094\u0095\5\32\16\2")
        buf.write("\u0095\u0096\t\5\2\2\u0096\u0097\5\30\r\2\u0097\u009a")
        buf.write("\3\2\2\2\u0098\u009a\5\32\16\2\u0099\u0094\3\2\2\2\u0099")
        buf.write("\u0098\3\2\2\2\u009a\31\3\2\2\2\u009b\u00a3\7=\2\2\u009c")
        buf.write("\u00a3\7\b\2\2\u009d\u00a3\58\35\2\u009e\u009f\7\64\2")
        buf.write("\2\u009f\u00a0\5\30\r\2\u00a0\u00a1\7\65\2\2\u00a1\u00a3")
        buf.write("\3\2\2\2\u00a2\u009b\3\2\2\2\u00a2\u009c\3\2\2\2\u00a2")
        buf.write("\u009d\3\2\2\2\u00a2\u009e\3\2\2\2\u00a3\33\3\2\2\2\u00a4")
        buf.write("\u00a7\5:\36\2\u00a5\u00a7\7=\2\2\u00a6\u00a4\3\2\2\2")
        buf.write("\u00a6\u00a5\3\2\2\2\u00a7\u00a8\3\2\2\2\u00a8\u00a9\5")
        buf.write("\36\20\2\u00a9\35\3\2\2\2\u00aa\u00ab\b\20\1\2\u00ab\u00ac")
        buf.write("\7\66\2\2\u00ac\u00ad\5 \21\2\u00ad\u00ae\7\67\2\2\u00ae")
        buf.write("\u00bb\3\2\2\2\u00af\u00b0\f\4\2\2\u00b0\u00b1\7\66\2")
        buf.write("\2\u00b1\u00b2\5 \21\2\u00b2\u00b3\7\67\2\2\u00b3\u00ba")
        buf.write("\3\2\2\2\u00b4\u00b5\f\3\2\2\u00b5\u00b6\7\66\2\2\u00b6")
        buf.write("\u00b7\5\34\17\2\u00b7\u00b8\7\67\2\2\u00b8\u00ba\3\2")
        buf.write("\2\2\u00b9\u00af\3\2\2\2\u00b9\u00b4\3\2\2\2\u00ba\u00bd")
        buf.write("\3\2\2\2\u00bb\u00b9\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc")
        buf.write("\37\3\2\2\2\u00bd\u00bb\3\2\2\2\u00be\u00c7\7=\2\2\u00bf")
        buf.write("\u00c7\7\5\2\2\u00c0\u00c7\5<\37\2\u00c1\u00c7\5\34\17")
        buf.write("\2\u00c2\u00c3\7\64\2\2\u00c3\u00c4\5\34\17\2\u00c4\u00c5")
        buf.write("\7\65\2\2\u00c5\u00c7\3\2\2\2\u00c6\u00be\3\2\2\2\u00c6")
        buf.write("\u00bf\3\2\2\2\u00c6\u00c0\3\2\2\2\u00c6\u00c1\3\2\2\2")
        buf.write("\u00c6\u00c2\3\2\2\2\u00c7!\3\2\2\2\u00c8\u00c9\7\36\2")
        buf.write("\2\u00c9\u00ca\7=\2\2\u00ca\u00cb\7\64\2\2\u00cb\u00cc")
        buf.write("\5> \2\u00cc\u00cd\7\65\2\2\u00cd\u00d3\3\2\2\2\u00ce")
        buf.write("\u00cf\7\64\2\2\u00cf\u00d0\5\"\22\2\u00d0\u00d1\7\65")
        buf.write("\2\2\u00d1\u00d3\3\2\2\2\u00d2\u00c8\3\2\2\2\u00d2\u00ce")
        buf.write("\3\2\2\2\u00d3#\3\2\2\2\u00d4\u00d5\5&\24\2\u00d5\u00d6")
        buf.write("\t\6\2\2\u00d6\u00d7\5&\24\2\u00d7%\3\2\2\2\u00d8\u00d9")
        buf.write("\7\64\2\2\u00d9\u00da\5<\37\2\u00da\u00db\7\65\2\2\u00db")
        buf.write("\u00e7\3\2\2\2\u00dc\u00e7\7\5\2\2\u00dd\u00e7\7\7\2\2")
        buf.write("\u00de\u00e0\7!\2\2\u00df\u00de\3\2\2\2\u00df\u00e0\3")
        buf.write("\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e7\7=\2\2\u00e2\u00e3")
        buf.write("\7\64\2\2\u00e3\u00e4\5$\23\2\u00e4\u00e5\7\65\2\2\u00e5")
        buf.write("\u00e7\3\2\2\2\u00e6\u00d8\3\2\2\2\u00e6\u00dc\3\2\2\2")
        buf.write("\u00e6\u00dd\3\2\2\2\u00e6\u00df\3\2\2\2\u00e6\u00e2\3")
        buf.write("\2\2\2\u00e7\'\3\2\2\2\u00e8\u00e9\5*\26\2\u00e9\u00ea")
        buf.write("\t\7\2\2\u00ea\u00eb\5*\26\2\u00eb)\3\2\2\2\u00ec\u00ed")
        buf.write("\7\64\2\2\u00ed\u00ee\5<\37\2\u00ee\u00ef\7\65\2\2\u00ef")
        buf.write("\u00f7\3\2\2\2\u00f0\u00f7\7\5\2\2\u00f1\u00f7\7\6\2\2")
        buf.write("\u00f2\u00f4\7!\2\2\u00f3\u00f2\3\2\2\2\u00f3\u00f4\3")
        buf.write("\2\2\2\u00f4\u00f5\3\2\2\2\u00f5\u00f7\7=\2\2\u00f6\u00ec")
        buf.write("\3\2\2\2\u00f6\u00f0\3\2\2\2\u00f6\u00f1\3\2\2\2\u00f6")
        buf.write("\u00f3\3\2\2\2\u00f7+\3\2\2\2\u00f8\u00fb\5$\23\2\u00f9")
        buf.write("\u00fb\5(\25\2\u00fa\u00f8\3\2\2\2\u00fa\u00f9\3\2\2\2")
        buf.write("\u00fb-\3\2\2\2\u00fc\u00ff\7=\2\2\u00fd\u00ff\5\"\22")
        buf.write("\2\u00fe\u00fc\3\2\2\2\u00fe\u00fd\3\2\2\2\u00ff/\3\2")
        buf.write("\2\2\u0100\u0101\7\64\2\2\u0101\u0102\5.\30\2\u0102\u0103")
        buf.write("\7\65\2\2\u0103\u0107\3\2\2\2\u0104\u0107\7=\2\2\u0105")
        buf.write("\u0107\7 \2\2\u0106\u0100\3\2\2\2\u0106\u0104\3\2\2\2")
        buf.write("\u0106\u0105\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u0109\7")
        buf.write("<\2\2\u0109\u010a\7=\2\2\u010a\61\3\2\2\2\u010b\u010c")
        buf.write("\7\64\2\2\u010c\u010d\5.\30\2\u010d\u010e\7\65\2\2\u010e")
        buf.write("\u0111\3\2\2\2\u010f\u0111\7=\2\2\u0110\u010b\3\2\2\2")
        buf.write("\u0110\u010f\3\2\2\2\u0111\u0112\3\2\2\2\u0112\u0113\7")
        buf.write("\63\2\2\u0113\u0114\7!\2\2\u0114\u0115\7=\2\2\u0115\63")
        buf.write("\3\2\2\2\u0116\u0117\7\64\2\2\u0117\u0118\5.\30\2\u0118")
        buf.write("\u0119\7\65\2\2\u0119\u011d\3\2\2\2\u011a\u011d\7=\2\2")
        buf.write("\u011b\u011d\7 \2\2\u011c\u0116\3\2\2\2\u011c\u011a\3")
        buf.write("\2\2\2\u011c\u011b\3\2\2\2\u011d\u011e\3\2\2\2\u011e\u011f")
        buf.write("\7<\2\2\u011f\u0120\7=\2\2\u0120\u0121\7\64\2\2\u0121")
        buf.write("\u0122\5> \2\u0122\u0123\7\65\2\2\u0123\65\3\2\2\2\u0124")
        buf.write("\u0125\7=\2\2\u0125\u0126\7\63\2\2\u0126\u0127\7!\2\2")
        buf.write("\u0127\u0128\7=\2\2\u0128\u0129\7\64\2\2\u0129\u012a\5")
        buf.write("> \2\u012a\u012b\7\65\2\2\u012b\67\3\2\2\2\u012c\u0131")
        buf.write("\5\60\31\2\u012d\u0131\5\62\32\2\u012e\u0131\5\64\33\2")
        buf.write("\u012f\u0131\5\66\34\2\u0130\u012c\3\2\2\2\u0130\u012d")
        buf.write("\3\2\2\2\u0130\u012e\3\2\2\2\u0130\u012f\3\2\2\2\u0131")
        buf.write("9\3\2\2\2\u0132\u0133\7=\2\2\u0133\u0134\7\64\2\2\u0134")
        buf.write("\u0135\5> \2\u0135\u0136\7\65\2\2\u0136;\3\2\2\2\u0137")
        buf.write("\u0140\58\35\2\u0138\u0140\5\f\7\2\u0139\u0140\5\24\13")
        buf.write("\2\u013a\u0140\5\30\r\2\u013b\u0140\5\34\17\2\u013c\u0140")
        buf.write("\5\"\22\2\u013d\u0140\5,\27\2\u013e\u0140\5:\36\2\u013f")
        buf.write("\u0137\3\2\2\2\u013f\u0138\3\2\2\2\u013f\u0139\3\2\2\2")
        buf.write("\u013f\u013a\3\2\2\2\u013f\u013b\3\2\2\2\u013f\u013c\3")
        buf.write("\2\2\2\u013f\u013d\3\2\2\2\u013f\u013e\3\2\2\2\u0140=")
        buf.write("\3\2\2\2\u0141\u0146\5<\37\2\u0142\u0143\7;\2\2\u0143")
        buf.write("\u0145\5<\37\2\u0144\u0142\3\2\2\2\u0145\u0148\3\2\2\2")
        buf.write("\u0146\u0144\3\2\2\2\u0146\u0147\3\2\2\2\u0147\u014a\3")
        buf.write("\2\2\2\u0148\u0146\3\2\2\2\u0149\u0141\3\2\2\2\u0149\u014a")
        buf.write("\3\2\2\2\u014a?\3\2\2\2\u014b\u014c\7\21\2\2\u014c\u0155")
        buf.write("\7\64\2\2\u014d\u0152\5B\"\2\u014e\u014f\7;\2\2\u014f")
        buf.write("\u0151\5B\"\2\u0150\u014e\3\2\2\2\u0151\u0154\3\2\2\2")
        buf.write("\u0152\u0150\3\2\2\2\u0152\u0153\3\2\2\2\u0153\u0156\3")
        buf.write("\2\2\2\u0154\u0152\3\2\2\2\u0155\u014d\3\2\2\2\u0155\u0156")
        buf.write("\3\2\2\2\u0156\u0157\3\2\2\2\u0157\u0158\7\65\2\2\u0158")
        buf.write("A\3\2\2\2\u0159\u015f\7\5\2\2\u015a\u015f\7\6\2\2\u015b")
        buf.write("\u015f\7\7\2\2\u015c\u015f\7\b\2\2\u015d\u015f\5@!\2\u015e")
        buf.write("\u0159\3\2\2\2\u015e\u015a\3\2\2\2\u015e\u015b\3\2\2\2")
        buf.write("\u015e\u015c\3\2\2\2\u015e\u015d\3\2\2\2\u015fC\3\2\2")
        buf.write("\2\"JV[it\177\u0086\u0089\u0092\u0099\u00a2\u00a6\u00b9")
        buf.write("\u00bb\u00c6\u00d2\u00df\u00e6\u00f3\u00f6\u00fa\u00fe")
        buf.write("\u0106\u0110\u011c\u0130\u013f\u0146\u0149\u0152\u0155")
        buf.write("\u015e")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'main'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'Break'", "'Continue'", 
                     "'If'", "'Elseif'", "'Else'", "'Foreach'", "'True'", 
                     "'False'", "'Array'", "'In'", "'Int'", "'Float'", "'Boolean'", 
                     "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
                     "'Var'", "'Constructor'", "'Destructor'", "'New'", 
                     "'By'", "'Self'", "'$'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'=='", "'!='", "'>'", "'>='", "'<'", "'<='", 
                     "'+.'", "'==.'", "'!'", "'&&'", "'||'", "'='", "'::'", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'", "';'", "','", 
                     "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "BLOCK_COMMENT", "INTLIT", 
                      "FLOATLIT", "BOOLLIT", "STRLIT", "BREAK", "CONTINUE", 
                      "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", 
                      "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
                      "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", 
                      "DESTRUCTOR", "NEW", "BY", "SELF", "STATIC", "ADD", 
                      "SUB", "MUL", "DIV", "MOD", "EQ", "NEQ", "GT", "GTE", 
                      "LT", "LTE", "SADD", "SEQ", "NOT", "AND", "OR", "ASSIGN", 
                      "SCOPE", "LB", "RB", "LSB", "RSB", "LCB", "RCB", "SM", 
                      "CM", "DOT", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_mptype = 1
    RULE_body = 2
    RULE_exp = 3
    RULE_funcall = 4
    RULE_expIntFloat = 5
    RULE_exp0 = 6
    RULE_exp1 = 7
    RULE_exp2 = 8
    RULE_expBool = 9
    RULE_expTermBool = 10
    RULE_expStr = 11
    RULE_expTermStr = 12
    RULE_expIdx = 13
    RULE_expTermIdx = 14
    RULE_idxOperators = 15
    RULE_expObjCreation = 16
    RULE_expEqualAndNotEqual = 17
    RULE_expTermpEQANEQ = 18
    RULE_expLessLargeEqual = 19
    RULE_expTermLRE = 20
    RULE_expRelationalOperation = 21
    RULE_expClassObject = 22
    RULE_expInstanceAttributeAccess = 23
    RULE_expStaticAttributeAccess = 24
    RULE_expInstanceMethodInvocation = 25
    RULE_expStaticMethodInvocation = 26
    RULE_expMemberAccess = 27
    RULE_expMethod = 28
    RULE_expr = 29
    RULE_listOfExp = 30
    RULE_idx_arraylit = 31
    RULE_datalit = 32

    ruleNames =  [ "program", "mptype", "body", "exp", "funcall", "expIntFloat", 
                   "exp0", "exp1", "exp2", "expBool", "expTermBool", "expStr", 
                   "expTermStr", "expIdx", "expTermIdx", "idxOperators", 
                   "expObjCreation", "expEqualAndNotEqual", "expTermpEQANEQ", 
                   "expLessLargeEqual", "expTermLRE", "expRelationalOperation", 
                   "expClassObject", "expInstanceAttributeAccess", "expStaticAttributeAccess", 
                   "expInstanceMethodInvocation", "expStaticMethodInvocation", 
                   "expMemberAccess", "expMethod", "expr", "listOfExp", 
                   "idx_arraylit", "datalit" ]

    EOF = Token.EOF
    T__0=1
    BLOCK_COMMENT=2
    INTLIT=3
    FLOATLIT=4
    BOOLLIT=5
    STRLIT=6
    BREAK=7
    CONTINUE=8
    IF=9
    ELSEIF=10
    ELSE=11
    FOREACH=12
    TRUE=13
    FALSE=14
    ARRAY=15
    IN=16
    INT=17
    FLOAT=18
    BOOLEAN=19
    STRING=20
    RETURN=21
    NULL=22
    CLASS=23
    VAL=24
    VAR=25
    CONSTRUCTOR=26
    DESTRUCTOR=27
    NEW=28
    BY=29
    SELF=30
    STATIC=31
    ADD=32
    SUB=33
    MUL=34
    DIV=35
    MOD=36
    EQ=37
    NEQ=38
    GT=39
    GTE=40
    LT=41
    LTE=42
    SADD=43
    SEQ=44
    NOT=45
    AND=46
    OR=47
    ASSIGN=48
    SCOPE=49
    LB=50
    RB=51
    LSB=52
    RSB=53
    LCB=54
    RCB=55
    SM=56
    CM=57
    DOT=58
    ID=59
    WS=60
    ERROR_CHAR=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def mptype(self):
            return self.getTypedRuleContext(D96Parser.MptypeContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def body(self):
            return self.getTypedRuleContext(D96Parser.BodyContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_program




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.mptype()
            self.state = 67
            self.match(D96Parser.T__0)
            self.state = 68
            self.match(D96Parser.LB)
            self.state = 69
            self.match(D96Parser.RB)
            self.state = 70
            self.match(D96Parser.LCB)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 71
                self.body()


            self.state = 74
            self.match(D96Parser.RCB)
            self.state = 75
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MptypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_mptype




    def mptype(self):

        localctx = D96Parser.MptypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_mptype)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 77
            self.match(D96Parser.CLASS)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BodyContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(D96Parser.FuncallContext,0)


        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_body




    def body(self):

        localctx = D96Parser.BodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.funcall()
            self.state = 80
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def funcall(self):
            return self.getTypedRuleContext(D96Parser.FuncallContext,0)


        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp




    def exp(self):

        localctx = D96Parser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_exp)
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.funcall()
                pass
            elif token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.match(D96Parser.INTLIT)
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


    class FuncallContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def exp(self):
            return self.getTypedRuleContext(D96Parser.ExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_funcall




    def funcall(self):

        localctx = D96Parser.FuncallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_funcall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(D96Parser.ID)
            self.state = 87
            self.match(D96Parser.LSB)
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.INTLIT or _la==D96Parser.ID:
                self.state = 88
                self.exp()


            self.state = 91
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpIntFloatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp0(self):
            return self.getTypedRuleContext(D96Parser.Exp0Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expIntFloat




    def expIntFloat(self):

        localctx = D96Parser.ExpIntFloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expIntFloat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.exp0(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp0Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp1(self):
            return self.getTypedRuleContext(D96Parser.Exp1Context,0)


        def exp0(self):
            return self.getTypedRuleContext(D96Parser.Exp0Context,0)


        def ADD(self):
            return self.getToken(D96Parser.ADD, 0)

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp0



    def exp0(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp0Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 12
        self.enterRecursionRule(localctx, 12, self.RULE_exp0, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.exp1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 103
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp0Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp0)
                    self.state = 98
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 99
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 100
                    self.exp1(0) 
                self.state = 105
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp2(self):
            return self.getTypedRuleContext(D96Parser.Exp2Context,0)


        def exp1(self):
            return self.getTypedRuleContext(D96Parser.Exp1Context,0)


        def MUL(self):
            return self.getToken(D96Parser.MUL, 0)

        def DIV(self):
            return self.getToken(D96Parser.DIV, 0)

        def MOD(self):
            return self.getToken(D96Parser.MOD, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp1



    def exp1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_exp1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.exp2()
            self._ctx.stop = self._input.LT(-1)
            self.state = 114
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp1)
                    self.state = 109
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 110
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 111
                    self.exp2() 
                self.state = 116
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(D96Parser.FLOATLIT, 0)

        def expMemberAccess(self):
            return self.getTypedRuleContext(D96Parser.ExpMemberAccessContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp0(self):
            return self.getTypedRuleContext(D96Parser.Exp0Context,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp2




    def exp2(self):

        localctx = D96Parser.Exp2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_exp2)
        try:
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 118
                self.match(D96Parser.INTLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 119
                self.match(D96Parser.FLOATLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 120
                self.expMemberAccess()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 121
                self.match(D96Parser.LB)
                self.state = 122
                self.exp0(0)
                self.state = 123
                self.match(D96Parser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpBoolContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expTermBool(self):
            return self.getTypedRuleContext(D96Parser.ExpTermBoolContext,0)


        def expBool(self):
            return self.getTypedRuleContext(D96Parser.ExpBoolContext,0)


        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expBool




    def expBool(self):

        localctx = D96Parser.ExpBoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expBool)
        self._la = 0 # Token type
        try:
            self.state = 135
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 127
                self.expTermBool()
                self.state = 128
                _la = self._input.LA(1)
                if not(_la==D96Parser.AND or _la==D96Parser.OR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 129
                self.expBool()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.NOT:
                    self.state = 131
                    self.match(D96Parser.NOT)


                self.state = 134
                self.expTermBool()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpTermBoolContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def BOOLLIT(self):
            return self.getToken(D96Parser.BOOLLIT, 0)

        def expMemberAccess(self):
            return self.getTypedRuleContext(D96Parser.ExpMemberAccessContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expBool(self):
            return self.getTypedRuleContext(D96Parser.ExpBoolContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expTermBool




    def expTermBool(self):

        localctx = D96Parser.ExpTermBoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expTermBool)
        try:
            self.state = 144
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.match(D96Parser.BOOLLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 139
                self.expMemberAccess()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 140
                self.match(D96Parser.LB)
                self.state = 141
                self.expBool()
                self.state = 142
                self.match(D96Parser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpStrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expTermStr(self):
            return self.getTypedRuleContext(D96Parser.ExpTermStrContext,0)


        def expStr(self):
            return self.getTypedRuleContext(D96Parser.ExpStrContext,0)


        def SEQ(self):
            return self.getToken(D96Parser.SEQ, 0)

        def SADD(self):
            return self.getToken(D96Parser.SADD, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expStr




    def expStr(self):

        localctx = D96Parser.ExpStrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_expStr)
        self._la = 0 # Token type
        try:
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 146
                self.expTermStr()
                self.state = 147
                _la = self._input.LA(1)
                if not(_la==D96Parser.SADD or _la==D96Parser.SEQ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 148
                self.expStr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 150
                self.expTermStr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpTermStrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def STRLIT(self):
            return self.getToken(D96Parser.STRLIT, 0)

        def expMemberAccess(self):
            return self.getTypedRuleContext(D96Parser.ExpMemberAccessContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expStr(self):
            return self.getTypedRuleContext(D96Parser.ExpStrContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expTermStr




    def expTermStr(self):

        localctx = D96Parser.ExpTermStrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expTermStr)
        try:
            self.state = 160
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self.match(D96Parser.STRLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 155
                self.expMemberAccess()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 156
                self.match(D96Parser.LB)
                self.state = 157
                self.expStr()
                self.state = 158
                self.match(D96Parser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpIdxContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expTermIdx(self):
            return self.getTypedRuleContext(D96Parser.ExpTermIdxContext,0)


        def expMethod(self):
            return self.getTypedRuleContext(D96Parser.ExpMethodContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expIdx




    def expIdx(self):

        localctx = D96Parser.ExpIdxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expIdx)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.state = 162
                self.expMethod()
                pass

            elif la_ == 2:
                self.state = 163
                self.match(D96Parser.ID)
                pass


            self.state = 166
            self.expTermIdx(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpTermIdxContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def idxOperators(self):
            return self.getTypedRuleContext(D96Parser.IdxOperatorsContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def expTermIdx(self):
            return self.getTypedRuleContext(D96Parser.ExpTermIdxContext,0)


        def expIdx(self):
            return self.getTypedRuleContext(D96Parser.ExpIdxContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expTermIdx



    def expTermIdx(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.ExpTermIdxContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 28
        self.enterRecursionRule(localctx, 28, self.RULE_expTermIdx, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(D96Parser.LSB)
            self.state = 170
            self.idxOperators()
            self.state = 171
            self.match(D96Parser.RSB)
            self._ctx.stop = self._input.LT(-1)
            self.state = 185
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 183
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.ExpTermIdxContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expTermIdx)
                        self.state = 173
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 174
                        self.match(D96Parser.LSB)
                        self.state = 175
                        self.idxOperators()
                        self.state = 176
                        self.match(D96Parser.RSB)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.ExpTermIdxContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expTermIdx)
                        self.state = 178
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 179
                        self.match(D96Parser.LSB)
                        self.state = 180
                        self.expIdx()
                        self.state = 181
                        self.match(D96Parser.RSB)
                        pass

             
                self.state = 187
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class IdxOperatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def expIdx(self):
            return self.getTypedRuleContext(D96Parser.ExpIdxContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_idxOperators




    def idxOperators(self):

        localctx = D96Parser.IdxOperatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_idxOperators)
        try:
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 188
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 189
                self.match(D96Parser.INTLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 190
                self.expr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 191
                self.expIdx()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 192
                self.match(D96Parser.LB)
                self.state = 193
                self.expIdx()
                self.state = 194
                self.match(D96Parser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpObjCreationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def listOfExp(self):
            return self.getTypedRuleContext(D96Parser.ListOfExpContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def expObjCreation(self):
            return self.getTypedRuleContext(D96Parser.ExpObjCreationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expObjCreation




    def expObjCreation(self):

        localctx = D96Parser.ExpObjCreationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_expObjCreation)
        try:
            self.state = 208
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.match(D96Parser.NEW)
                self.state = 199
                self.match(D96Parser.ID)
                self.state = 200
                self.match(D96Parser.LB)
                self.state = 201
                self.listOfExp()
                self.state = 202
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.match(D96Parser.LB)
                self.state = 205
                self.expObjCreation()
                self.state = 206
                self.match(D96Parser.RB)
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


    class ExpEqualAndNotEqualContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expTermpEQANEQ(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpTermpEQANEQContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpTermpEQANEQContext,i)


        def EQ(self):
            return self.getToken(D96Parser.EQ, 0)

        def NEQ(self):
            return self.getToken(D96Parser.NEQ, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expEqualAndNotEqual




    def expEqualAndNotEqual(self):

        localctx = D96Parser.ExpEqualAndNotEqualContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_expEqualAndNotEqual)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.expTermpEQANEQ()
            self.state = 211
            _la = self._input.LA(1)
            if not(_la==D96Parser.EQ or _la==D96Parser.NEQ):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 212
            self.expTermpEQANEQ()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpTermpEQANEQContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def BOOLLIT(self):
            return self.getToken(D96Parser.BOOLLIT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def expEqualAndNotEqual(self):
            return self.getTypedRuleContext(D96Parser.ExpEqualAndNotEqualContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expTermpEQANEQ




    def expTermpEQANEQ(self):

        localctx = D96Parser.ExpTermpEQANEQContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_expTermpEQANEQ)
        self._la = 0 # Token type
        try:
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.match(D96Parser.LB)
                self.state = 215
                self.expr()
                self.state = 216
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.match(D96Parser.INTLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 219
                self.match(D96Parser.BOOLLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 221
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.STATIC:
                    self.state = 220
                    self.match(D96Parser.STATIC)


                self.state = 223
                self.match(D96Parser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 224
                self.match(D96Parser.LB)
                self.state = 225
                self.expEqualAndNotEqual()
                self.state = 226
                self.match(D96Parser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpLessLargeEqualContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expTermLRE(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExpTermLREContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExpTermLREContext,i)


        def GT(self):
            return self.getToken(D96Parser.GT, 0)

        def LT(self):
            return self.getToken(D96Parser.LT, 0)

        def LTE(self):
            return self.getToken(D96Parser.LTE, 0)

        def GTE(self):
            return self.getToken(D96Parser.GTE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expLessLargeEqual




    def expLessLargeEqual(self):

        localctx = D96Parser.ExpLessLargeEqualContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_expLessLargeEqual)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self.expTermLRE()
            self.state = 231
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.GT) | (1 << D96Parser.GTE) | (1 << D96Parser.LT) | (1 << D96Parser.LTE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 232
            self.expTermLRE()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpTermLREContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(D96Parser.FLOATLIT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expTermLRE




    def expTermLRE(self):

        localctx = D96Parser.ExpTermLREContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_expTermLRE)
        self._la = 0 # Token type
        try:
            self.state = 244
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 234
                self.match(D96Parser.LB)
                self.state = 235
                self.expr()
                self.state = 236
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 239
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.STATIC, D96Parser.ID]:
                self.enterOuterAlt(localctx, 4)
                self.state = 241
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.STATIC:
                    self.state = 240
                    self.match(D96Parser.STATIC)


                self.state = 243
                self.match(D96Parser.ID)
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


    class ExpRelationalOperationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expEqualAndNotEqual(self):
            return self.getTypedRuleContext(D96Parser.ExpEqualAndNotEqualContext,0)


        def expLessLargeEqual(self):
            return self.getTypedRuleContext(D96Parser.ExpLessLargeEqualContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expRelationalOperation




    def expRelationalOperation(self):

        localctx = D96Parser.ExpRelationalOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_expRelationalOperation)
        try:
            self.state = 248
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 246
                self.expEqualAndNotEqual()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 247
                self.expLessLargeEqual()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpClassObjectContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def expObjCreation(self):
            return self.getTypedRuleContext(D96Parser.ExpObjCreationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expClassObject




    def expClassObject(self):

        localctx = D96Parser.ExpClassObjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_expClassObject)
        try:
            self.state = 252
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.NEW, D96Parser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
                self.expObjCreation()
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


    class ExpInstanceAttributeAccessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expClassObject(self):
            return self.getTypedRuleContext(D96Parser.ExpClassObjectContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expInstanceAttributeAccess




    def expInstanceAttributeAccess(self):

        localctx = D96Parser.ExpInstanceAttributeAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_expInstanceAttributeAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 260
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LB]:
                self.state = 254
                self.match(D96Parser.LB)
                self.state = 255
                self.expClassObject()
                self.state = 256
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.ID]:
                self.state = 258
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.SELF]:
                self.state = 259
                self.match(D96Parser.SELF)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 262
            self.match(D96Parser.DOT)
            self.state = 263
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpStaticAttributeAccessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SCOPE(self):
            return self.getToken(D96Parser.SCOPE, 0)

        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def expClassObject(self):
            return self.getTypedRuleContext(D96Parser.ExpClassObjectContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expStaticAttributeAccess




    def expStaticAttributeAccess(self):

        localctx = D96Parser.ExpStaticAttributeAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_expStaticAttributeAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 270
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LB]:
                self.state = 265
                self.match(D96Parser.LB)
                self.state = 266
                self.expClassObject()
                self.state = 267
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.ID]:
                self.state = 269
                self.match(D96Parser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 272
            self.match(D96Parser.SCOPE)
            self.state = 273
            self.match(D96Parser.STATIC)
            self.state = 274
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpInstanceMethodInvocationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def LB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LB)
            else:
                return self.getToken(D96Parser.LB, i)

        def listOfExp(self):
            return self.getTypedRuleContext(D96Parser.ListOfExpContext,0)


        def RB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RB)
            else:
                return self.getToken(D96Parser.RB, i)

        def expClassObject(self):
            return self.getTypedRuleContext(D96Parser.ExpClassObjectContext,0)


        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expInstanceMethodInvocation




    def expInstanceMethodInvocation(self):

        localctx = D96Parser.ExpInstanceMethodInvocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_expInstanceMethodInvocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LB]:
                self.state = 276
                self.match(D96Parser.LB)
                self.state = 277
                self.expClassObject()
                self.state = 278
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.ID]:
                self.state = 280
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.SELF]:
                self.state = 281
                self.match(D96Parser.SELF)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 284
            self.match(D96Parser.DOT)
            self.state = 285
            self.match(D96Parser.ID)
            self.state = 286
            self.match(D96Parser.LB)
            self.state = 287
            self.listOfExp()
            self.state = 288
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpStaticMethodInvocationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def SCOPE(self):
            return self.getToken(D96Parser.SCOPE, 0)

        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def listOfExp(self):
            return self.getTypedRuleContext(D96Parser.ListOfExpContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_expStaticMethodInvocation




    def expStaticMethodInvocation(self):

        localctx = D96Parser.ExpStaticMethodInvocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expStaticMethodInvocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.match(D96Parser.ID)
            self.state = 291
            self.match(D96Parser.SCOPE)
            self.state = 292
            self.match(D96Parser.STATIC)
            self.state = 293
            self.match(D96Parser.ID)
            self.state = 294
            self.match(D96Parser.LB)
            self.state = 295
            self.listOfExp()
            self.state = 296
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpMemberAccessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expInstanceAttributeAccess(self):
            return self.getTypedRuleContext(D96Parser.ExpInstanceAttributeAccessContext,0)


        def expStaticAttributeAccess(self):
            return self.getTypedRuleContext(D96Parser.ExpStaticAttributeAccessContext,0)


        def expInstanceMethodInvocation(self):
            return self.getTypedRuleContext(D96Parser.ExpInstanceMethodInvocationContext,0)


        def expStaticMethodInvocation(self):
            return self.getTypedRuleContext(D96Parser.ExpStaticMethodInvocationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expMemberAccess




    def expMemberAccess(self):

        localctx = D96Parser.ExpMemberAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_expMemberAccess)
        try:
            self.state = 302
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 298
                self.expInstanceAttributeAccess()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 299
                self.expStaticAttributeAccess()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 300
                self.expInstanceMethodInvocation()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 301
                self.expStaticMethodInvocation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpMethodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def listOfExp(self):
            return self.getTypedRuleContext(D96Parser.ListOfExpContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expMethod




    def expMethod(self):

        localctx = D96Parser.ExpMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_expMethod)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 304
            self.match(D96Parser.ID)
            self.state = 305
            self.match(D96Parser.LB)

            self.state = 306
            self.listOfExp()
            self.state = 307
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expMemberAccess(self):
            return self.getTypedRuleContext(D96Parser.ExpMemberAccessContext,0)


        def expIntFloat(self):
            return self.getTypedRuleContext(D96Parser.ExpIntFloatContext,0)


        def expBool(self):
            return self.getTypedRuleContext(D96Parser.ExpBoolContext,0)


        def expStr(self):
            return self.getTypedRuleContext(D96Parser.ExpStrContext,0)


        def expIdx(self):
            return self.getTypedRuleContext(D96Parser.ExpIdxContext,0)


        def expObjCreation(self):
            return self.getTypedRuleContext(D96Parser.ExpObjCreationContext,0)


        def expRelationalOperation(self):
            return self.getTypedRuleContext(D96Parser.ExpRelationalOperationContext,0)


        def expMethod(self):
            return self.getTypedRuleContext(D96Parser.ExpMethodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr




    def expr(self):

        localctx = D96Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expr)
        try:
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 309
                self.expMemberAccess()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 310
                self.expIntFloat()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 311
                self.expBool()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 312
                self.expStr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 313
                self.expIdx()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 314
                self.expObjCreation()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 315
                self.expRelationalOperation()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 316
                self.expMethod()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListOfExpContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_listOfExp




    def listOfExp(self):

        localctx = D96Parser.ListOfExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_listOfExp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 327
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLLIT) | (1 << D96Parser.STRLIT) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.STATIC) | (1 << D96Parser.NOT) | (1 << D96Parser.LB) | (1 << D96Parser.ID))) != 0):
                self.state = 319
                self.expr()
                self.state = 324
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.CM:
                    self.state = 320
                    self.match(D96Parser.CM)
                    self.state = 321
                    self.expr()
                    self.state = 326
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idx_arraylitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def datalit(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.DatalitContext)
            else:
                return self.getTypedRuleContext(D96Parser.DatalitContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_idx_arraylit




    def idx_arraylit(self):

        localctx = D96Parser.Idx_arraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_idx_arraylit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 329
            self.match(D96Parser.ARRAY)
            self.state = 330
            self.match(D96Parser.LB)
            self.state = 339
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLLIT) | (1 << D96Parser.STRLIT) | (1 << D96Parser.ARRAY))) != 0):
                self.state = 331
                self.datalit()
                self.state = 336
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.CM:
                    self.state = 332
                    self.match(D96Parser.CM)
                    self.state = 333
                    self.datalit()
                    self.state = 338
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 341
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DatalitContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(D96Parser.FLOATLIT, 0)

        def BOOLLIT(self):
            return self.getToken(D96Parser.BOOLLIT, 0)

        def STRLIT(self):
            return self.getToken(D96Parser.STRLIT, 0)

        def idx_arraylit(self):
            return self.getTypedRuleContext(D96Parser.Idx_arraylitContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_datalit




    def datalit(self):

        localctx = D96Parser.DatalitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_datalit)
        try:
            self.state = 348
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 343
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 344
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.BOOLLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 345
                self.match(D96Parser.BOOLLIT)
                pass
            elif token in [D96Parser.STRLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 346
                self.match(D96Parser.STRLIT)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 347
                self.idx_arraylit()
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



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[6] = self.exp0_sempred
        self._predicates[7] = self.exp1_sempred
        self._predicates[14] = self.expTermIdx_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp0_sempred(self, localctx:Exp0Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp1_sempred(self, localctx:Exp1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def expTermIdx_sempred(self, localctx:ExpTermIdxContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         




