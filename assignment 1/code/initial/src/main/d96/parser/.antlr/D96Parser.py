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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\u0276\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\3\2\6\2t\n")
        buf.write("\2\r\2\16\2u\3\2\3\2\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\7")
        buf.write("\4\u0082\n\4\f\4\16\4\u0085\13\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\7\5\u008d\n\5\f\5\16\5\u0090\13\5\3\6\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\3\6\5\6\u009c\n\6\3\7\3\7\3\7\3\7\3")
        buf.write("\7\5\7\u00a3\n\7\3\7\5\7\u00a6\n\7\3\b\5\b\u00a9\n\b\3")
        buf.write("\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00b2\n\b\3\t\3\t\3\t\3")
        buf.write("\t\3\t\5\t\u00b9\n\t\3\n\5\n\u00bc\n\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\5\n\u00c5\n\n\3\13\3\13\3\13\3\13\3\f\3\f")
        buf.write("\3\f\3\f\3\f\3\f\3\f\5\f\u00d2\n\f\3\f\3\f\3\f\3\f\3\f")
        buf.write("\5\f\u00d9\n\f\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\3\16\5\16\u00e6\n\16\3\16\5\16\u00e9\n\16\3\17\3")
        buf.write("\17\5\17\u00ed\n\17\3\20\3\20\5\20\u00f1\n\20\3\20\3\20")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\7\21\u0104\n\21\f\21\16\21\u0107")
        buf.write("\13\21\3\22\5\22\u010a\n\22\3\22\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\5\22\u0114\n\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\3\23\7\23\u011c\n\23\f\23\16\23\u011f\13\23\3\24\3\24")
        buf.write("\3\24\3\24\3\24\3\24\3\24\3\24\5\24\u0129\n\24\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\7\26\u013a\n\26\f\26\16\26\u013d\13\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\27\5\27\u0147\n")
        buf.write("\27\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31")
        buf.write("\u015d\n\31\7\31\u015f\n\31\f\31\16\31\u0162\13\31\3\32")
        buf.write("\3\32\5\32\u0166\n\32\3\33\3\33\3\33\5\33\u016b\n\33\3")
        buf.write("\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\3\34\5\34")
        buf.write("\u0177\n\34\3\35\3\35\5\35\u017b\n\35\3\36\3\36\3\36\3")
        buf.write("\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\5\37")
        buf.write("\u018a\n\37\3 \3 \3 \7 \u018f\n \f \16 \u0192\13 \5 \u0194")
        buf.write("\n \3!\3!\3!\3!\3!\5!\u019b\n!\3\"\3\"\3\"\3\"\3\"\3\"")
        buf.write("\3\"\3#\3#\3#\7#\u01a7\n#\f#\16#\u01aa\13#\3$\5$\u01ad")
        buf.write("\n$\3$\5$\u01b0\n$\3$\3$\3$\3$\3$\5$\u01b7\n$\3$\3$\3")
        buf.write("%\3%\5%\u01bd\n%\3&\3&\3&\3&\3&\3\'\3\'\3\'\3\'\3\'\7")
        buf.write("\'\u01c9\n\'\f\'\16\'\u01cc\13\'\3\'\3\'\3\'\3\'\3\'\7")
        buf.write("\'\u01d3\n\'\f\'\16\'\u01d6\13\'\7\'\u01d8\n\'\f\'\16")
        buf.write("\'\u01db\13\'\3\'\3\'\7\'\u01df\n\'\f\'\16\'\u01e2\13")
        buf.write("\'\5\'\u01e4\n\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\5(\u01ef\n")
        buf.write("(\3(\3(\3(\3)\3)\3)\3)\3*\3*\3*\5*\u01fb\n*\3*\3*\3+\3")
        buf.write("+\3+\3,\3,\5,\u0204\n,\3,\3,\3-\3-\3-\3.\3.\3.\3.\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\5.\u0216\n.\3/\7/\u0219\n/\f/\16/\u021c")
        buf.write("\13/\3\60\3\60\3\60\5\60\u0221\n\60\3\61\3\61\3\61\3\61")
        buf.write("\5\61\u0227\n\61\3\61\3\61\3\61\7\61\u022c\n\61\f\61\16")
        buf.write("\61\u022f\13\61\3\61\3\61\3\62\5\62\u0234\n\62\3\62\3")
        buf.write("\62\3\62\5\62\u0239\n\62\3\62\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\63\5\63\u0242\n\63\3\63\3\63\3\63\3\63\3\64\3\64\3")
        buf.write("\64\5\64\u024b\n\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65")
        buf.write("\3\65\3\66\3\66\3\66\7\66\u0258\n\66\f\66\16\66\u025b")
        buf.write("\13\66\3\67\3\67\3\67\3\67\38\38\38\38\38\78\u0266\n8")
        buf.write("\f8\168\u0269\138\58\u026b\n8\38\38\39\39\39\39\39\59")
        buf.write("\u0274\n9\39\2\b\6\b $*\60:\2\4\6\b\n\f\16\20\22\24\26")
        buf.write("\30\32\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\")
        buf.write("^`bdfhjlnp\2\t\3\2\"#\3\2$&\3\2\60\61\3\2-.\3\2\'(\3\2")
        buf.write("),\3\2\32\33\2\u02aa\2s\3\2\2\2\4y\3\2\2\2\6{\3\2\2\2")
        buf.write("\b\u0086\3\2\2\2\n\u009b\3\2\2\2\f\u00a5\3\2\2\2\16\u00b1")
        buf.write("\3\2\2\2\20\u00b8\3\2\2\2\22\u00c4\3\2\2\2\24\u00c6\3")
        buf.write("\2\2\2\26\u00d8\3\2\2\2\30\u00da\3\2\2\2\32\u00e8\3\2")
        buf.write("\2\2\34\u00ec\3\2\2\2\36\u00f0\3\2\2\2 \u00f4\3\2\2\2")
        buf.write("\"\u0113\3\2\2\2$\u0115\3\2\2\2&\u0128\3\2\2\2(\u012a")
        buf.write("\3\2\2\2*\u012f\3\2\2\2,\u0146\3\2\2\2.\u0148\3\2\2\2")
        buf.write("\60\u0150\3\2\2\2\62\u0165\3\2\2\2\64\u016a\3\2\2\2\66")
        buf.write("\u0176\3\2\2\28\u017a\3\2\2\2:\u017c\3\2\2\2<\u0189\3")
        buf.write("\2\2\2>\u0193\3\2\2\2@\u019a\3\2\2\2B\u019c\3\2\2\2D\u01a3")
        buf.write("\3\2\2\2F\u01ac\3\2\2\2H\u01bc\3\2\2\2J\u01be\3\2\2\2")
        buf.write("L\u01c3\3\2\2\2N\u01e5\3\2\2\2P\u01f3\3\2\2\2R\u01fa\3")
        buf.write("\2\2\2T\u01fe\3\2\2\2V\u0201\3\2\2\2X\u0207\3\2\2\2Z\u0215")
        buf.write("\3\2\2\2\\\u021a\3\2\2\2^\u0220\3\2\2\2`\u0222\3\2\2\2")
        buf.write("b\u0233\3\2\2\2d\u023d\3\2\2\2f\u0247\3\2\2\2h\u024f\3")
        buf.write("\2\2\2j\u0254\3\2\2\2l\u025c\3\2\2\2n\u0260\3\2\2\2p\u0273")
        buf.write("\3\2\2\2rt\5`\61\2sr\3\2\2\2tu\3\2\2\2us\3\2\2\2uv\3\2")
        buf.write("\2\2vw\3\2\2\2wx\7\2\2\3x\3\3\2\2\2yz\5\6\4\2z\5\3\2\2")
        buf.write("\2{|\b\4\1\2|}\5\b\5\2}\u0083\3\2\2\2~\177\f\4\2\2\177")
        buf.write("\u0080\t\2\2\2\u0080\u0082\5\b\5\2\u0081~\3\2\2\2\u0082")
        buf.write("\u0085\3\2\2\2\u0083\u0081\3\2\2\2\u0083\u0084\3\2\2\2")
        buf.write("\u0084\7\3\2\2\2\u0085\u0083\3\2\2\2\u0086\u0087\b\5\1")
        buf.write("\2\u0087\u0088\5\n\6\2\u0088\u008e\3\2\2\2\u0089\u008a")
        buf.write("\f\4\2\2\u008a\u008b\t\3\2\2\u008b\u008d\5\n\6\2\u008c")
        buf.write("\u0089\3\2\2\2\u008d\u0090\3\2\2\2\u008e\u008c\3\2\2\2")
        buf.write("\u008e\u008f\3\2\2\2\u008f\t\3\2\2\2\u0090\u008e\3\2\2")
        buf.write("\2\u0091\u009c\7>\2\2\u0092\u009c\7\5\2\2\u0093\u009c")
        buf.write("\7\6\2\2\u0094\u009c\5\64\33\2\u0095\u009c\5:\36\2\u0096")
        buf.write("\u009c\5\36\20\2\u0097\u0098\7\65\2\2\u0098\u0099\5\6")
        buf.write("\4\2\u0099\u009a\7\66\2\2\u009a\u009c\3\2\2\2\u009b\u0091")
        buf.write("\3\2\2\2\u009b\u0092\3\2\2\2\u009b\u0093\3\2\2\2\u009b")
        buf.write("\u0094\3\2\2\2\u009b\u0095\3\2\2\2\u009b\u0096\3\2\2\2")
        buf.write("\u009b\u0097\3\2\2\2\u009c\13\3\2\2\2\u009d\u009e\5\16")
        buf.write("\b\2\u009e\u009f\t\4\2\2\u009f\u00a0\5\f\7\2\u00a0\u00a6")
        buf.write("\3\2\2\2\u00a1\u00a3\7/\2\2\u00a2\u00a1\3\2\2\2\u00a2")
        buf.write("\u00a3\3\2\2\2\u00a3\u00a4\3\2\2\2\u00a4\u00a6\5\16\b")
        buf.write("\2\u00a5\u009d\3\2\2\2\u00a5\u00a2\3\2\2\2\u00a6\r\3\2")
        buf.write("\2\2\u00a7\u00a9\7!\2\2\u00a8\u00a7\3\2\2\2\u00a8\u00a9")
        buf.write("\3\2\2\2\u00a9\u00aa\3\2\2\2\u00aa\u00b2\7>\2\2\u00ab")
        buf.write("\u00b2\7\7\2\2\u00ac\u00b2\5\64\33\2\u00ad\u00ae\7\65")
        buf.write("\2\2\u00ae\u00af\5\f\7\2\u00af\u00b0\7\66\2\2\u00b0\u00b2")
        buf.write("\3\2\2\2\u00b1\u00a8\3\2\2\2\u00b1\u00ab\3\2\2\2\u00b1")
        buf.write("\u00ac\3\2\2\2\u00b1\u00ad\3\2\2\2\u00b2\17\3\2\2\2\u00b3")
        buf.write("\u00b4\5\22\n\2\u00b4\u00b5\t\5\2\2\u00b5\u00b6\5\20\t")
        buf.write("\2\u00b6\u00b9\3\2\2\2\u00b7\u00b9\5\22\n\2\u00b8\u00b3")
        buf.write("\3\2\2\2\u00b8\u00b7\3\2\2\2\u00b9\21\3\2\2\2\u00ba\u00bc")
        buf.write("\7!\2\2\u00bb\u00ba\3\2\2\2\u00bb\u00bc\3\2\2\2\u00bc")
        buf.write("\u00bd\3\2\2\2\u00bd\u00c5\7>\2\2\u00be\u00c5\7\b\2\2")
        buf.write("\u00bf\u00c5\5\64\33\2\u00c0\u00c1\7\65\2\2\u00c1\u00c2")
        buf.write("\5\20\t\2\u00c2\u00c3\7\66\2\2\u00c3\u00c5\3\2\2\2\u00c4")
        buf.write("\u00bb\3\2\2\2\u00c4\u00be\3\2\2\2\u00c4\u00bf\3\2\2\2")
        buf.write("\u00c4\u00c0\3\2\2\2\u00c5\23\3\2\2\2\u00c6\u00c7\5\26")
        buf.write("\f\2\u00c7\u00c8\t\6\2\2\u00c8\u00c9\5\26\f\2\u00c9\25")
        buf.write("\3\2\2\2\u00ca\u00cb\7\65\2\2\u00cb\u00cc\5<\37\2\u00cc")
        buf.write("\u00cd\7\66\2\2\u00cd\u00d9\3\2\2\2\u00ce\u00d9\7\5\2")
        buf.write("\2\u00cf\u00d9\7\7\2\2\u00d0\u00d2\7!\2\2\u00d1\u00d0")
        buf.write("\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3")
        buf.write("\u00d9\7>\2\2\u00d4\u00d5\7\65\2\2\u00d5\u00d6\5\24\13")
        buf.write("\2\u00d6\u00d7\7\66\2\2\u00d7\u00d9\3\2\2\2\u00d8\u00ca")
        buf.write("\3\2\2\2\u00d8\u00ce\3\2\2\2\u00d8\u00cf\3\2\2\2\u00d8")
        buf.write("\u00d1\3\2\2\2\u00d8\u00d4\3\2\2\2\u00d9\27\3\2\2\2\u00da")
        buf.write("\u00db\5\32\16\2\u00db\u00dc\t\7\2\2\u00dc\u00dd\5\32")
        buf.write("\16\2\u00dd\31\3\2\2\2\u00de\u00df\7\65\2\2\u00df\u00e0")
        buf.write("\5<\37\2\u00e0\u00e1\7\66\2\2\u00e1\u00e9\3\2\2\2\u00e2")
        buf.write("\u00e9\7\5\2\2\u00e3\u00e9\7\6\2\2\u00e4\u00e6\7!\2\2")
        buf.write("\u00e5\u00e4\3\2\2\2\u00e5\u00e6\3\2\2\2\u00e6\u00e7\3")
        buf.write("\2\2\2\u00e7\u00e9\7>\2\2\u00e8\u00de\3\2\2\2\u00e8\u00e2")
        buf.write("\3\2\2\2\u00e8\u00e3\3\2\2\2\u00e8\u00e5\3\2\2\2\u00e9")
        buf.write("\33\3\2\2\2\u00ea\u00ed\5\24\13\2\u00eb\u00ed\5\30\r\2")
        buf.write("\u00ec\u00ea\3\2\2\2\u00ec\u00eb\3\2\2\2\u00ed\35\3\2")
        buf.write("\2\2\u00ee\u00f1\5:\36\2\u00ef\u00f1\7>\2\2\u00f0\u00ee")
        buf.write("\3\2\2\2\u00f0\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2")
        buf.write("\u00f3\5 \21\2\u00f3\37\3\2\2\2\u00f4\u00f5\b\21\1\2\u00f5")
        buf.write("\u00f6\7\67\2\2\u00f6\u00f7\5\"\22\2\u00f7\u00f8\78\2")
        buf.write("\2\u00f8\u0105\3\2\2\2\u00f9\u00fa\f\4\2\2\u00fa\u00fb")
        buf.write("\7\67\2\2\u00fb\u00fc\5\"\22\2\u00fc\u00fd\78\2\2\u00fd")
        buf.write("\u0104\3\2\2\2\u00fe\u00ff\f\3\2\2\u00ff\u0100\7\67\2")
        buf.write("\2\u0100\u0101\5\36\20\2\u0101\u0102\78\2\2\u0102\u0104")
        buf.write("\3\2\2\2\u0103\u00f9\3\2\2\2\u0103\u00fe\3\2\2\2\u0104")
        buf.write("\u0107\3\2\2\2\u0105\u0103\3\2\2\2\u0105\u0106\3\2\2\2")
        buf.write("\u0106!\3\2\2\2\u0107\u0105\3\2\2\2\u0108\u010a\7!\2\2")
        buf.write("\u0109\u0108\3\2\2\2\u0109\u010a\3\2\2\2\u010a\u010b\3")
        buf.write("\2\2\2\u010b\u0114\7>\2\2\u010c\u0114\7\5\2\2\u010d\u0114")
        buf.write("\5<\37\2\u010e\u0114\5\36\20\2\u010f\u0110\7\65\2\2\u0110")
        buf.write("\u0111\5\36\20\2\u0111\u0112\7\66\2\2\u0112\u0114\3\2")
        buf.write("\2\2\u0113\u0109\3\2\2\2\u0113\u010c\3\2\2\2\u0113\u010d")
        buf.write("\3\2\2\2\u0113\u010e\3\2\2\2\u0113\u010f\3\2\2\2\u0114")
        buf.write("#\3\2\2\2\u0115\u0116\b\23\1\2\u0116\u0117\5&\24\2\u0117")
        buf.write("\u011d\3\2\2\2\u0118\u0119\f\4\2\2\u0119\u011a\7=\2\2")
        buf.write("\u011a\u011c\7>\2\2\u011b\u0118\3\2\2\2\u011c\u011f\3")
        buf.write("\2\2\2\u011d\u011b\3\2\2\2\u011d\u011e\3\2\2\2\u011e%")
        buf.write("\3\2\2\2\u011f\u011d\3\2\2\2\u0120\u0121\7\65\2\2\u0121")
        buf.write("\u0122\58\35\2\u0122\u0123\7\66\2\2\u0123\u0129\3\2\2")
        buf.write("\2\u0124\u0129\7>\2\2\u0125\u0129\7 \2\2\u0126\u0129\5")
        buf.write("(\25\2\u0127\u0129\5.\30\2\u0128\u0120\3\2\2\2\u0128\u0124")
        buf.write("\3\2\2\2\u0128\u0125\3\2\2\2\u0128\u0126\3\2\2\2\u0128")
        buf.write("\u0127\3\2\2\2\u0129\'\3\2\2\2\u012a\u012b\7>\2\2\u012b")
        buf.write("\u012c\7\64\2\2\u012c\u012d\7!\2\2\u012d\u012e\7>\2\2")
        buf.write("\u012e)\3\2\2\2\u012f\u0130\b\26\1\2\u0130\u0131\5,\27")
        buf.write("\2\u0131\u013b\3\2\2\2\u0132\u0133\f\4\2\2\u0133\u0134")
        buf.write("\7=\2\2\u0134\u0135\7>\2\2\u0135\u0136\7\65\2\2\u0136")
        buf.write("\u0137\5> \2\u0137\u0138\7\66\2\2\u0138\u013a\3\2\2\2")
        buf.write("\u0139\u0132\3\2\2\2\u013a\u013d\3\2\2\2\u013b\u0139\3")
        buf.write("\2\2\2\u013b\u013c\3\2\2\2\u013c+\3\2\2\2\u013d\u013b")
        buf.write("\3\2\2\2\u013e\u013f\7\65\2\2\u013f\u0140\58\35\2\u0140")
        buf.write("\u0141\7\66\2\2\u0141\u0147\3\2\2\2\u0142\u0147\7>\2\2")
        buf.write("\u0143\u0147\7 \2\2\u0144\u0147\5(\25\2\u0145\u0147\5")
        buf.write(".\30\2\u0146\u013e\3\2\2\2\u0146\u0142\3\2\2\2\u0146\u0143")
        buf.write("\3\2\2\2\u0146\u0144\3\2\2\2\u0146\u0145\3\2\2\2\u0147")
        buf.write("-\3\2\2\2\u0148\u0149\7>\2\2\u0149\u014a\7\64\2\2\u014a")
        buf.write("\u014b\7!\2\2\u014b\u014c\7>\2\2\u014c\u014d\7\65\2\2")
        buf.write("\u014d\u014e\5> \2\u014e\u014f\7\66\2\2\u014f/\3\2\2\2")
        buf.write("\u0150\u0151\b\31\1\2\u0151\u0152\5\62\32\2\u0152\u0160")
        buf.write("\3\2\2\2\u0153\u015c\f\4\2\2\u0154\u0155\7=\2\2\u0155")
        buf.write("\u015d\7>\2\2\u0156\u0157\7=\2\2\u0157\u0158\7>\2\2\u0158")
        buf.write("\u0159\7\65\2\2\u0159\u015a\5> \2\u015a\u015b\7\66\2\2")
        buf.write("\u015b\u015d\3\2\2\2\u015c\u0154\3\2\2\2\u015c\u0156\3")
        buf.write("\2\2\2\u015d\u015f\3\2\2\2\u015e\u0153\3\2\2\2\u015f\u0162")
        buf.write("\3\2\2\2\u0160\u015e\3\2\2\2\u0160\u0161\3\2\2\2\u0161")
        buf.write("\61\3\2\2\2\u0162\u0160\3\2\2\2\u0163\u0166\5$\23\2\u0164")
        buf.write("\u0166\5*\26\2\u0165\u0163\3\2\2\2\u0165\u0164\3\2\2\2")
        buf.write("\u0166\63\3\2\2\2\u0167\u016b\5\60\31\2\u0168\u016b\5")
        buf.write("(\25\2\u0169\u016b\5.\30\2\u016a\u0167\3\2\2\2\u016a\u0168")
        buf.write("\3\2\2\2\u016a\u0169\3\2\2\2\u016b\65\3\2\2\2\u016c\u016d")
        buf.write("\7\36\2\2\u016d\u016e\7>\2\2\u016e\u016f\7\65\2\2\u016f")
        buf.write("\u0170\5> \2\u0170\u0171\7\66\2\2\u0171\u0177\3\2\2\2")
        buf.write("\u0172\u0173\7\65\2\2\u0173\u0174\5\66\34\2\u0174\u0175")
        buf.write("\7\66\2\2\u0175\u0177\3\2\2\2\u0176\u016c\3\2\2\2\u0176")
        buf.write("\u0172\3\2\2\2\u0177\67\3\2\2\2\u0178\u017b\7>\2\2\u0179")
        buf.write("\u017b\5\66\34\2\u017a\u0178\3\2\2\2\u017a\u0179\3\2\2")
        buf.write("\2\u017b9\3\2\2\2\u017c\u017d\7>\2\2\u017d\u017e\7\65")
        buf.write("\2\2\u017e\u017f\5> \2\u017f\u0180\7\66\2\2\u0180;\3\2")
        buf.write("\2\2\u0181\u018a\5\66\34\2\u0182\u018a\5\64\33\2\u0183")
        buf.write("\u018a\5\4\3\2\u0184\u018a\5\f\7\2\u0185\u018a\5\20\t")
        buf.write("\2\u0186\u018a\5\36\20\2\u0187\u018a\5\34\17\2\u0188\u018a")
        buf.write("\5p9\2\u0189\u0181\3\2\2\2\u0189\u0182\3\2\2\2\u0189\u0183")
        buf.write("\3\2\2\2\u0189\u0184\3\2\2\2\u0189\u0185\3\2\2\2\u0189")
        buf.write("\u0186\3\2\2\2\u0189\u0187\3\2\2\2\u0189\u0188\3\2\2\2")
        buf.write("\u018a=\3\2\2\2\u018b\u0190\5<\37\2\u018c\u018d\7<\2\2")
        buf.write("\u018d\u018f\5<\37\2\u018e\u018c\3\2\2\2\u018f\u0192\3")
        buf.write("\2\2\2\u0190\u018e\3\2\2\2\u0190\u0191\3\2\2\2\u0191\u0194")
        buf.write("\3\2\2\2\u0192\u0190\3\2\2\2\u0193\u018b\3\2\2\2\u0193")
        buf.write("\u0194\3\2\2\2\u0194?\3\2\2\2\u0195\u019b\7\23\2\2\u0196")
        buf.write("\u019b\7\24\2\2\u0197\u019b\7\25\2\2\u0198\u019b\7\26")
        buf.write("\2\2\u0199\u019b\5B\"\2\u019a\u0195\3\2\2\2\u019a\u0196")
        buf.write("\3\2\2\2\u019a\u0197\3\2\2\2\u019a\u0198\3\2\2\2\u019a")
        buf.write("\u0199\3\2\2\2\u019bA\3\2\2\2\u019c\u019d\7\21\2\2\u019d")
        buf.write("\u019e\7\67\2\2\u019e\u019f\5@!\2\u019f\u01a0\7<\2\2\u01a0")
        buf.write("\u01a1\7\5\2\2\u01a1\u01a2\78\2\2\u01a2C\3\2\2\2\u01a3")
        buf.write("\u01a8\7>\2\2\u01a4\u01a5\7<\2\2\u01a5\u01a7\7>\2\2\u01a6")
        buf.write("\u01a4\3\2\2\2\u01a7\u01aa\3\2\2\2\u01a8\u01a6\3\2\2\2")
        buf.write("\u01a8\u01a9\3\2\2\2\u01a9E\3\2\2\2\u01aa\u01a8\3\2\2")
        buf.write("\2\u01ab\u01ad\t\b\2\2\u01ac\u01ab\3\2\2\2\u01ac\u01ad")
        buf.write("\3\2\2\2\u01ad\u01af\3\2\2\2\u01ae\u01b0\7!\2\2\u01af")
        buf.write("\u01ae\3\2\2\2\u01af\u01b0\3\2\2\2\u01b0\u01b1\3\2\2\2")
        buf.write("\u01b1\u01b2\5D#\2\u01b2\u01b3\7\62\2\2\u01b3\u01b6\5")
        buf.write("@!\2\u01b4\u01b5\7\63\2\2\u01b5\u01b7\5> \2\u01b6\u01b4")
        buf.write("\3\2\2\2\u01b6\u01b7\3\2\2\2\u01b7\u01b8\3\2\2\2\u01b8")
        buf.write("\u01b9\7;\2\2\u01b9G\3\2\2\2\u01ba\u01bd\7>\2\2\u01bb")
        buf.write("\u01bd\5<\37\2\u01bc\u01ba\3\2\2\2\u01bc\u01bb\3\2\2\2")
        buf.write("\u01bdI\3\2\2\2\u01be\u01bf\5H%\2\u01bf\u01c0\7\63\2\2")
        buf.write("\u01c0\u01c1\5<\37\2\u01c1\u01c2\7;\2\2\u01c2K\3\2\2\2")
        buf.write("\u01c3\u01c4\7\13\2\2\u01c4\u01c5\7\65\2\2\u01c5\u01c6")
        buf.write("\5<\37\2\u01c6\u01ca\7\66\2\2\u01c7\u01c9\5P)\2\u01c8")
        buf.write("\u01c7\3\2\2\2\u01c9\u01cc\3\2\2\2\u01ca\u01c8\3\2\2\2")
        buf.write("\u01ca\u01cb\3\2\2\2\u01cb\u01d9\3\2\2\2\u01cc\u01ca\3")
        buf.write("\2\2\2\u01cd\u01ce\7\f\2\2\u01ce\u01cf\7\65\2\2\u01cf")
        buf.write("\u01d0\5<\37\2\u01d0\u01d4\7\66\2\2\u01d1\u01d3\5P)\2")
        buf.write("\u01d2\u01d1\3\2\2\2\u01d3\u01d6\3\2\2\2\u01d4\u01d2\3")
        buf.write("\2\2\2\u01d4\u01d5\3\2\2\2\u01d5\u01d8\3\2\2\2\u01d6\u01d4")
        buf.write("\3\2\2\2\u01d7\u01cd\3\2\2\2\u01d8\u01db\3\2\2\2\u01d9")
        buf.write("\u01d7\3\2\2\2\u01d9\u01da\3\2\2\2\u01da\u01e3\3\2\2\2")
        buf.write("\u01db\u01d9\3\2\2\2\u01dc\u01e0\7\r\2\2\u01dd\u01df\5")
        buf.write("P)\2\u01de\u01dd\3\2\2\2\u01df\u01e2\3\2\2\2\u01e0\u01de")
        buf.write("\3\2\2\2\u01e0\u01e1\3\2\2\2\u01e1\u01e4\3\2\2\2\u01e2")
        buf.write("\u01e0\3\2\2\2\u01e3\u01dc\3\2\2\2\u01e3\u01e4\3\2\2\2")
        buf.write("\u01e4M\3\2\2\2\u01e5\u01e6\7\16\2\2\u01e6\u01e7\7\65")
        buf.write("\2\2\u01e7\u01e8\7>\2\2\u01e8\u01e9\7\22\2\2\u01e9\u01ea")
        buf.write("\5<\37\2\u01ea\u01eb\7\3\2\2\u01eb\u01ee\5<\37\2\u01ec")
        buf.write("\u01ed\7\37\2\2\u01ed\u01ef\5<\37\2\u01ee\u01ec\3\2\2")
        buf.write("\2\u01ee\u01ef\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01f1")
        buf.write("\7\66\2\2\u01f1\u01f2\5P)\2\u01f2O\3\2\2\2\u01f3\u01f4")
        buf.write("\79\2\2\u01f4\u01f5\5\\/\2\u01f5\u01f6\7:\2\2\u01f6Q\3")
        buf.write("\2\2\2\u01f7\u01fb\5*\26\2\u01f8\u01fb\5.\30\2\u01f9\u01fb")
        buf.write("\5:\36\2\u01fa\u01f7\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fa")
        buf.write("\u01f9\3\2\2\2\u01fb\u01fc\3\2\2\2\u01fc\u01fd\7;\2\2")
        buf.write("\u01fdS\3\2\2\2\u01fe\u01ff\7\n\2\2\u01ff\u0200\7;\2\2")
        buf.write("\u0200U\3\2\2\2\u0201\u0203\7\27\2\2\u0202\u0204\5<\37")
        buf.write("\2\u0203\u0202\3\2\2\2\u0203\u0204\3\2\2\2\u0204\u0205")
        buf.write("\3\2\2\2\u0205\u0206\7;\2\2\u0206W\3\2\2\2\u0207\u0208")
        buf.write("\7\t\2\2\u0208\u0209\7;\2\2\u0209Y\3\2\2\2\u020a\u0216")
        buf.write("\5F$\2\u020b\u0216\5J&\2\u020c\u0216\5L\'\2\u020d\u0216")
        buf.write("\5N(\2\u020e\u0216\5P)\2\u020f\u0216\5R*\2\u0210\u0216")
        buf.write("\5T+\2\u0211\u0216\5V,\2\u0212\u0216\5X-\2\u0213\u0216")
        buf.write("\5b\62\2\u0214\u0216\5^\60\2\u0215\u020a\3\2\2\2\u0215")
        buf.write("\u020b\3\2\2\2\u0215\u020c\3\2\2\2\u0215\u020d\3\2\2\2")
        buf.write("\u0215\u020e\3\2\2\2\u0215\u020f\3\2\2\2\u0215\u0210\3")
        buf.write("\2\2\2\u0215\u0211\3\2\2\2\u0215\u0212\3\2\2\2\u0215\u0213")
        buf.write("\3\2\2\2\u0215\u0214\3\2\2\2\u0216[\3\2\2\2\u0217\u0219")
        buf.write("\5Z.\2\u0218\u0217\3\2\2\2\u0219\u021c\3\2\2\2\u021a\u0218")
        buf.write("\3\2\2\2\u021a\u021b\3\2\2\2\u021b]\3\2\2\2\u021c\u021a")
        buf.write("\3\2\2\2\u021d\u0221\5f\64\2\u021e\u0221\5h\65\2\u021f")
        buf.write("\u0221\5d\63\2\u0220\u021d\3\2\2\2\u0220\u021e\3\2\2\2")
        buf.write("\u0220\u021f\3\2\2\2\u0221_\3\2\2\2\u0222\u0223\7\31\2")
        buf.write("\2\u0223\u0226\7>\2\2\u0224\u0225\7\62\2\2\u0225\u0227")
        buf.write("\7>\2\2\u0226\u0224\3\2\2\2\u0226\u0227\3\2\2\2\u0227")
        buf.write("\u0228\3\2\2\2\u0228\u022d\79\2\2\u0229\u022c\5F$\2\u022a")
        buf.write("\u022c\5b\62\2\u022b\u0229\3\2\2\2\u022b\u022a\3\2\2\2")
        buf.write("\u022c\u022f\3\2\2\2\u022d\u022b\3\2\2\2\u022d\u022e\3")
        buf.write("\2\2\2\u022e\u0230\3\2\2\2\u022f\u022d\3\2\2\2\u0230\u0231")
        buf.write("\7:\2\2\u0231a\3\2\2\2\u0232\u0234\7!\2\2\u0233\u0232")
        buf.write("\3\2\2\2\u0233\u0234\3\2\2\2\u0234\u0235\3\2\2\2\u0235")
        buf.write("\u0236\7>\2\2\u0236\u0238\7\65\2\2\u0237\u0239\5j\66\2")
        buf.write("\u0238\u0237\3\2\2\2\u0238\u0239\3\2\2\2\u0239\u023a\3")
        buf.write("\2\2\2\u023a\u023b\7\66\2\2\u023b\u023c\5P)\2\u023cc\3")
        buf.write("\2\2\2\u023d\u023e\7\31\2\2\u023e\u0241\7>\2\2\u023f\u0240")
        buf.write("\7\62\2\2\u0240\u0242\7>\2\2\u0241\u023f\3\2\2\2\u0241")
        buf.write("\u0242\3\2\2\2\u0242\u0243\3\2\2\2\u0243\u0244\79\2\2")
        buf.write("\u0244\u0245\5\\/\2\u0245\u0246\7:\2\2\u0246e\3\2\2\2")
        buf.write("\u0247\u0248\7\34\2\2\u0248\u024a\7\65\2\2\u0249\u024b")
        buf.write("\5j\66\2\u024a\u0249\3\2\2\2\u024a\u024b\3\2\2\2\u024b")
        buf.write("\u024c\3\2\2\2\u024c\u024d\7\66\2\2\u024d\u024e\5P)\2")
        buf.write("\u024eg\3\2\2\2\u024f\u0250\7\35\2\2\u0250\u0251\7\66")
        buf.write("\2\2\u0251\u0252\7\65\2\2\u0252\u0253\5P)\2\u0253i\3\2")
        buf.write("\2\2\u0254\u0259\5l\67\2\u0255\u0256\7;\2\2\u0256\u0258")
        buf.write("\5l\67\2\u0257\u0255\3\2\2\2\u0258\u025b\3\2\2\2\u0259")
        buf.write("\u0257\3\2\2\2\u0259\u025a\3\2\2\2\u025ak\3\2\2\2\u025b")
        buf.write("\u0259\3\2\2\2\u025c\u025d\5D#\2\u025d\u025e\7\62\2\2")
        buf.write("\u025e\u025f\5@!\2\u025fm\3\2\2\2\u0260\u0261\7\21\2\2")
        buf.write("\u0261\u026a\7\65\2\2\u0262\u0267\5p9\2\u0263\u0264\7")
        buf.write("<\2\2\u0264\u0266\5p9\2\u0265\u0263\3\2\2\2\u0266\u0269")
        buf.write("\3\2\2\2\u0267\u0265\3\2\2\2\u0267\u0268\3\2\2\2\u0268")
        buf.write("\u026b\3\2\2\2\u0269\u0267\3\2\2\2\u026a\u0262\3\2\2\2")
        buf.write("\u026a\u026b\3\2\2\2\u026b\u026c\3\2\2\2\u026c\u026d\7")
        buf.write("\66\2\2\u026do\3\2\2\2\u026e\u0274\7\5\2\2\u026f\u0274")
        buf.write("\7\6\2\2\u0270\u0274\7\7\2\2\u0271\u0274\7\b\2\2\u0272")
        buf.write("\u0274\5n8\2\u0273\u026e\3\2\2\2\u0273\u026f\3\2\2\2\u0273")
        buf.write("\u0270\3\2\2\2\u0273\u0271\3\2\2\2\u0273\u0272\3\2\2\2")
        buf.write("\u0274q\3\2\2\2@u\u0083\u008e\u009b\u00a2\u00a5\u00a8")
        buf.write("\u00b1\u00b8\u00bb\u00c4\u00d1\u00d8\u00e5\u00e8\u00ec")
        buf.write("\u00f0\u0103\u0105\u0109\u0113\u011d\u0128\u013b\u0146")
        buf.write("\u015c\u0160\u0165\u016a\u0176\u017a\u0189\u0190\u0193")
        buf.write("\u019a\u01a8\u01ac\u01af\u01b6\u01bc\u01ca\u01d4\u01d9")
        buf.write("\u01e0\u01e3\u01ee\u01fa\u0203\u0215\u021a\u0220\u0226")
        buf.write("\u022b\u022d\u0233\u0238\u0241\u024a\u0259\u0267\u026a")
        buf.write("\u0273")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'..'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "'Break'", "'Continue'", 
                     "'If'", "'Elseif'", "'Else'", "'Foreach'", "'True'", 
                     "'False'", "'Array'", "'In'", "'Int'", "'Float'", "'Boolean'", 
                     "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
                     "'Var'", "'Constructor'", "'Destructor'", "'New'", 
                     "'By'", "'Self'", "'$'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'=='", "'!='", "'>'", "'>='", "'<'", "'<='", 
                     "'+.'", "'==.'", "'!'", "'&&'", "'||'", "':'", "'='", 
                     "'::'", "'('", "')'", "'['", "']'", "'{'", "'}'", "';'", 
                     "','", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "BLOCK_COMMENT", "INTLIT", 
                      "FLOATLIT", "BOOLLIT", "STRLIT", "BREAK", "CONTINUE", 
                      "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", 
                      "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
                      "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", 
                      "DESTRUCTOR", "NEW", "BY", "SELF", "STATIC", "ADD", 
                      "SUB", "MUL", "DIV", "MOD", "EQ", "NEQ", "GT", "GTE", 
                      "LT", "LTE", "SADD", "SEQ", "NOT", "AND", "OR", "COLON", 
                      "ASSIGN", "SCOPE", "LB", "RB", "LSB", "RSB", "LCB", 
                      "RCB", "SM", "CM", "DOT", "ID", "WS", "ERROR_CHAR", 
                      "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_exp_IntFloat = 1
    RULE_exp_0 = 2
    RULE_exp_1 = 3
    RULE_exp_2 = 4
    RULE_exp_Bool = 5
    RULE_exp_TermBool = 6
    RULE_exp_Str = 7
    RULE_exp_TermStr = 8
    RULE_exp_EqualAndNotEqual = 9
    RULE_exp_TermEQANEQ = 10
    RULE_exp_LessLargeEqual = 11
    RULE_exp_TermLRE = 12
    RULE_exp_RelationalOperation = 13
    RULE_exp_Idx = 14
    RULE_exp_TermIdx = 15
    RULE_idx_Operators = 16
    RULE_exp_InstanceAttributeAccess = 17
    RULE_exp_InstanceAttributeAccessTerm = 18
    RULE_exp_StaticAttributeAccess = 19
    RULE_exp_InstanceMethodInvocation = 20
    RULE_exp_InstanceMethodInvocationTerm = 21
    RULE_exp_StaticMethodInvocation = 22
    RULE_exp_InstanceAttributeMethod = 23
    RULE_exp_InstanceAttributeMethodTerm = 24
    RULE_exp_MemberAccess = 25
    RULE_exp_ObjCreation = 26
    RULE_exp_ClassObject = 27
    RULE_exp_Method = 28
    RULE_expr = 29
    RULE_list_Expr = 30
    RULE_type_Data = 31
    RULE_array_Type = 32
    RULE_seq_ID = 33
    RULE_stmt_VarDeclaration = 34
    RULE_lhs = 35
    RULE_stmt_Assign = 36
    RULE_stmt_If = 37
    RULE_stmt_ForIn = 38
    RULE_stmt_Block = 39
    RULE_stmt_MethodInvocation = 40
    RULE_stmt_Continue = 41
    RULE_stmt_Return = 42
    RULE_stmt_Break = 43
    RULE_stmt = 44
    RULE_list_Stmt = 45
    RULE_stmt_Class = 46
    RULE_stmt_ClassDeclaration = 47
    RULE_stmt_MethodDeclaration = 48
    RULE_class_Declaration = 49
    RULE_class_Construction = 50
    RULE_class_Destruction = 51
    RULE_list_Parameters = 52
    RULE_seq_Parameters = 53
    RULE_idx_arraylit = 54
    RULE_datalit = 55

    ruleNames =  [ "program", "exp_IntFloat", "exp_0", "exp_1", "exp_2", 
                   "exp_Bool", "exp_TermBool", "exp_Str", "exp_TermStr", 
                   "exp_EqualAndNotEqual", "exp_TermEQANEQ", "exp_LessLargeEqual", 
                   "exp_TermLRE", "exp_RelationalOperation", "exp_Idx", 
                   "exp_TermIdx", "idx_Operators", "exp_InstanceAttributeAccess", 
                   "exp_InstanceAttributeAccessTerm", "exp_StaticAttributeAccess", 
                   "exp_InstanceMethodInvocation", "exp_InstanceMethodInvocationTerm", 
                   "exp_StaticMethodInvocation", "exp_InstanceAttributeMethod", 
                   "exp_InstanceAttributeMethodTerm", "exp_MemberAccess", 
                   "exp_ObjCreation", "exp_ClassObject", "exp_Method", "expr", 
                   "list_Expr", "type_Data", "array_Type", "seq_ID", "stmt_VarDeclaration", 
                   "lhs", "stmt_Assign", "stmt_If", "stmt_ForIn", "stmt_Block", 
                   "stmt_MethodInvocation", "stmt_Continue", "stmt_Return", 
                   "stmt_Break", "stmt", "list_Stmt", "stmt_Class", "stmt_ClassDeclaration", 
                   "stmt_MethodDeclaration", "class_Declaration", "class_Construction", 
                   "class_Destruction", "list_Parameters", "seq_Parameters", 
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
    COLON=48
    ASSIGN=49
    SCOPE=50
    LB=51
    RB=52
    LSB=53
    RSB=54
    LCB=55
    RCB=56
    SM=57
    CM=58
    DOT=59
    ID=60
    WS=61
    ERROR_CHAR=62
    UNCLOSE_STRING=63
    ILLEGAL_ESCAPE=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

        def stmt_ClassDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Stmt_ClassDeclarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.Stmt_ClassDeclarationContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_program




    def program(self):

        localctx = D96Parser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 112
                self.stmt_ClassDeclaration()
                self.state = 115 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 117
            self.match(D96Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_IntFloatContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_0(self):
            return self.getTypedRuleContext(D96Parser.Exp_0Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp_IntFloat




    def exp_IntFloat(self):

        localctx = D96Parser.Exp_IntFloatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_exp_IntFloat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.exp_0(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_0Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_1(self):
            return self.getTypedRuleContext(D96Parser.Exp_1Context,0)


        def exp_0(self):
            return self.getTypedRuleContext(D96Parser.Exp_0Context,0)


        def ADD(self):
            return self.getToken(D96Parser.ADD, 0)

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp_0



    def exp_0(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp_0Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_exp_0, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.exp_1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 129
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp_0Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_0)
                    self.state = 124
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 125
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 126
                    self.exp_1(0) 
                self.state = 131
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp_1Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_2(self):
            return self.getTypedRuleContext(D96Parser.Exp_2Context,0)


        def exp_1(self):
            return self.getTypedRuleContext(D96Parser.Exp_1Context,0)


        def MUL(self):
            return self.getToken(D96Parser.MUL, 0)

        def DIV(self):
            return self.getToken(D96Parser.DIV, 0)

        def MOD(self):
            return self.getToken(D96Parser.MOD, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp_1



    def exp_1(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp_1Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_exp_1, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133
            self.exp_2()
            self._ctx.stop = self._input.LT(-1)
            self.state = 140
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp_1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_1)
                    self.state = 135
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 136
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 137
                    self.exp_2() 
                self.state = 142
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp_2Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(D96Parser.FLOATLIT, 0)

        def exp_MemberAccess(self):
            return self.getTypedRuleContext(D96Parser.Exp_MemberAccessContext,0)


        def exp_Method(self):
            return self.getTypedRuleContext(D96Parser.Exp_MethodContext,0)


        def exp_Idx(self):
            return self.getTypedRuleContext(D96Parser.Exp_IdxContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp_0(self):
            return self.getTypedRuleContext(D96Parser.Exp_0Context,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp_2




    def exp_2(self):

        localctx = D96Parser.Exp_2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_exp_2)
        try:
            self.state = 153
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 143
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 144
                self.match(D96Parser.INTLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 145
                self.match(D96Parser.FLOATLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 146
                self.exp_MemberAccess()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 147
                self.exp_Method()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 148
                self.exp_Idx()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 149
                self.match(D96Parser.LB)
                self.state = 150
                self.exp_0(0)
                self.state = 151
                self.match(D96Parser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_BoolContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_TermBool(self):
            return self.getTypedRuleContext(D96Parser.Exp_TermBoolContext,0)


        def exp_Bool(self):
            return self.getTypedRuleContext(D96Parser.Exp_BoolContext,0)


        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp_Bool




    def exp_Bool(self):

        localctx = D96Parser.Exp_BoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_exp_Bool)
        self._la = 0 # Token type
        try:
            self.state = 163
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                self.exp_TermBool()
                self.state = 156
                _la = self._input.LA(1)
                if not(_la==D96Parser.AND or _la==D96Parser.OR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 157
                self.exp_Bool()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.NOT:
                    self.state = 159
                    self.match(D96Parser.NOT)


                self.state = 162
                self.exp_TermBool()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_TermBoolContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def BOOLLIT(self):
            return self.getToken(D96Parser.BOOLLIT, 0)

        def exp_MemberAccess(self):
            return self.getTypedRuleContext(D96Parser.Exp_MemberAccessContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp_Bool(self):
            return self.getTypedRuleContext(D96Parser.Exp_BoolContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp_TermBool




    def exp_TermBool(self):

        localctx = D96Parser.Exp_TermBoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_exp_TermBool)
        self._la = 0 # Token type
        try:
            self.state = 175
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.STATIC:
                    self.state = 165
                    self.match(D96Parser.STATIC)


                self.state = 168
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 169
                self.match(D96Parser.BOOLLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 170
                self.exp_MemberAccess()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 171
                self.match(D96Parser.LB)
                self.state = 172
                self.exp_Bool()
                self.state = 173
                self.match(D96Parser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_StrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_TermStr(self):
            return self.getTypedRuleContext(D96Parser.Exp_TermStrContext,0)


        def exp_Str(self):
            return self.getTypedRuleContext(D96Parser.Exp_StrContext,0)


        def SEQ(self):
            return self.getToken(D96Parser.SEQ, 0)

        def SADD(self):
            return self.getToken(D96Parser.SADD, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp_Str




    def exp_Str(self):

        localctx = D96Parser.Exp_StrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_exp_Str)
        self._la = 0 # Token type
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 177
                self.exp_TermStr()
                self.state = 178
                _la = self._input.LA(1)
                if not(_la==D96Parser.SADD or _la==D96Parser.SEQ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 179
                self.exp_Str()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 181
                self.exp_TermStr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_TermStrContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def STRLIT(self):
            return self.getToken(D96Parser.STRLIT, 0)

        def exp_MemberAccess(self):
            return self.getTypedRuleContext(D96Parser.Exp_MemberAccessContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp_Str(self):
            return self.getTypedRuleContext(D96Parser.Exp_StrContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp_TermStr




    def exp_TermStr(self):

        localctx = D96Parser.Exp_TermStrContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_exp_TermStr)
        self._la = 0 # Token type
        try:
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 185
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.STATIC:
                    self.state = 184
                    self.match(D96Parser.STATIC)


                self.state = 187
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 188
                self.match(D96Parser.STRLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 189
                self.exp_MemberAccess()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 190
                self.match(D96Parser.LB)
                self.state = 191
                self.exp_Str()
                self.state = 192
                self.match(D96Parser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_EqualAndNotEqualContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_TermEQANEQ(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Exp_TermEQANEQContext)
            else:
                return self.getTypedRuleContext(D96Parser.Exp_TermEQANEQContext,i)


        def EQ(self):
            return self.getToken(D96Parser.EQ, 0)

        def NEQ(self):
            return self.getToken(D96Parser.NEQ, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp_EqualAndNotEqual




    def exp_EqualAndNotEqual(self):

        localctx = D96Parser.Exp_EqualAndNotEqualContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_exp_EqualAndNotEqual)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.exp_TermEQANEQ()
            self.state = 197
            _la = self._input.LA(1)
            if not(_la==D96Parser.EQ or _la==D96Parser.NEQ):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 198
            self.exp_TermEQANEQ()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_TermEQANEQContext(ParserRuleContext):

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

        def exp_EqualAndNotEqual(self):
            return self.getTypedRuleContext(D96Parser.Exp_EqualAndNotEqualContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp_TermEQANEQ




    def exp_TermEQANEQ(self):

        localctx = D96Parser.Exp_TermEQANEQContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_exp_TermEQANEQ)
        self._la = 0 # Token type
        try:
            self.state = 214
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.match(D96Parser.LB)
                self.state = 201
                self.expr()
                self.state = 202
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.match(D96Parser.INTLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 205
                self.match(D96Parser.BOOLLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 207
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.STATIC:
                    self.state = 206
                    self.match(D96Parser.STATIC)


                self.state = 209
                self.match(D96Parser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 210
                self.match(D96Parser.LB)
                self.state = 211
                self.exp_EqualAndNotEqual()
                self.state = 212
                self.match(D96Parser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_LessLargeEqualContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_TermLRE(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Exp_TermLREContext)
            else:
                return self.getTypedRuleContext(D96Parser.Exp_TermLREContext,i)


        def GT(self):
            return self.getToken(D96Parser.GT, 0)

        def LT(self):
            return self.getToken(D96Parser.LT, 0)

        def LTE(self):
            return self.getToken(D96Parser.LTE, 0)

        def GTE(self):
            return self.getToken(D96Parser.GTE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp_LessLargeEqual




    def exp_LessLargeEqual(self):

        localctx = D96Parser.Exp_LessLargeEqualContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_exp_LessLargeEqual)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 216
            self.exp_TermLRE()
            self.state = 217
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.GT) | (1 << D96Parser.GTE) | (1 << D96Parser.LT) | (1 << D96Parser.LTE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 218
            self.exp_TermLRE()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_TermLREContext(ParserRuleContext):

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
            return D96Parser.RULE_exp_TermLRE




    def exp_TermLRE(self):

        localctx = D96Parser.Exp_TermLREContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_exp_TermLRE)
        self._la = 0 # Token type
        try:
            self.state = 230
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 220
                self.match(D96Parser.LB)
                self.state = 221
                self.expr()
                self.state = 222
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 224
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 225
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.STATIC, D96Parser.ID]:
                self.enterOuterAlt(localctx, 4)
                self.state = 227
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.STATIC:
                    self.state = 226
                    self.match(D96Parser.STATIC)


                self.state = 229
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


    class Exp_RelationalOperationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_EqualAndNotEqual(self):
            return self.getTypedRuleContext(D96Parser.Exp_EqualAndNotEqualContext,0)


        def exp_LessLargeEqual(self):
            return self.getTypedRuleContext(D96Parser.Exp_LessLargeEqualContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp_RelationalOperation




    def exp_RelationalOperation(self):

        localctx = D96Parser.Exp_RelationalOperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_exp_RelationalOperation)
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 232
                self.exp_EqualAndNotEqual()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 233
                self.exp_LessLargeEqual()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_IdxContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_TermIdx(self):
            return self.getTypedRuleContext(D96Parser.Exp_TermIdxContext,0)


        def exp_Method(self):
            return self.getTypedRuleContext(D96Parser.Exp_MethodContext,0)


        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp_Idx




    def exp_Idx(self):

        localctx = D96Parser.Exp_IdxContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_exp_Idx)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 238
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                self.state = 236
                self.exp_Method()
                pass

            elif la_ == 2:
                self.state = 237
                self.match(D96Parser.ID)
                pass


            self.state = 240
            self.exp_TermIdx(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_TermIdxContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def idx_Operators(self):
            return self.getTypedRuleContext(D96Parser.Idx_OperatorsContext,0)


        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def exp_TermIdx(self):
            return self.getTypedRuleContext(D96Parser.Exp_TermIdxContext,0)


        def exp_Idx(self):
            return self.getTypedRuleContext(D96Parser.Exp_IdxContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp_TermIdx



    def exp_TermIdx(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp_TermIdxContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 30
        self.enterRecursionRule(localctx, 30, self.RULE_exp_TermIdx, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 243
            self.match(D96Parser.LSB)
            self.state = 244
            self.idx_Operators()
            self.state = 245
            self.match(D96Parser.RSB)
            self._ctx.stop = self._input.LT(-1)
            self.state = 259
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 257
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp_TermIdxContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_TermIdx)
                        self.state = 247
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 248
                        self.match(D96Parser.LSB)
                        self.state = 249
                        self.idx_Operators()
                        self.state = 250
                        self.match(D96Parser.RSB)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp_TermIdxContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_TermIdx)
                        self.state = 252
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 253
                        self.match(D96Parser.LSB)
                        self.state = 254
                        self.exp_Idx()
                        self.state = 255
                        self.match(D96Parser.RSB)
                        pass

             
                self.state = 261
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Idx_OperatorsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def exp_Idx(self):
            return self.getTypedRuleContext(D96Parser.Exp_IdxContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_idx_Operators




    def idx_Operators(self):

        localctx = D96Parser.Idx_OperatorsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_idx_Operators)
        self._la = 0 # Token type
        try:
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 263
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.STATIC:
                    self.state = 262
                    self.match(D96Parser.STATIC)


                self.state = 265
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 266
                self.match(D96Parser.INTLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 267
                self.expr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 268
                self.exp_Idx()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 269
                self.match(D96Parser.LB)
                self.state = 270
                self.exp_Idx()
                self.state = 271
                self.match(D96Parser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_InstanceAttributeAccessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_InstanceAttributeAccessTerm(self):
            return self.getTypedRuleContext(D96Parser.Exp_InstanceAttributeAccessTermContext,0)


        def exp_InstanceAttributeAccess(self):
            return self.getTypedRuleContext(D96Parser.Exp_InstanceAttributeAccessContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp_InstanceAttributeAccess



    def exp_InstanceAttributeAccess(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp_InstanceAttributeAccessContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 34
        self.enterRecursionRule(localctx, 34, self.RULE_exp_InstanceAttributeAccess, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 276
            self.exp_InstanceAttributeAccessTerm()
            self._ctx.stop = self._input.LT(-1)
            self.state = 283
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp_InstanceAttributeAccessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_InstanceAttributeAccess)
                    self.state = 278
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 279
                    self.match(D96Parser.DOT)
                    self.state = 280
                    self.match(D96Parser.ID) 
                self.state = 285
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp_InstanceAttributeAccessTermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp_ClassObject(self):
            return self.getTypedRuleContext(D96Parser.Exp_ClassObjectContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def exp_StaticAttributeAccess(self):
            return self.getTypedRuleContext(D96Parser.Exp_StaticAttributeAccessContext,0)


        def exp_StaticMethodInvocation(self):
            return self.getTypedRuleContext(D96Parser.Exp_StaticMethodInvocationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp_InstanceAttributeAccessTerm




    def exp_InstanceAttributeAccessTerm(self):

        localctx = D96Parser.Exp_InstanceAttributeAccessTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_exp_InstanceAttributeAccessTerm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 294
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 286
                self.match(D96Parser.LB)
                self.state = 287
                self.exp_ClassObject()
                self.state = 288
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.state = 290
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.state = 291
                self.match(D96Parser.SELF)
                pass

            elif la_ == 4:
                self.state = 292
                self.exp_StaticAttributeAccess()
                pass

            elif la_ == 5:
                self.state = 293
                self.exp_StaticMethodInvocation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_StaticAttributeAccessContext(ParserRuleContext):

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

        def getRuleIndex(self):
            return D96Parser.RULE_exp_StaticAttributeAccess




    def exp_StaticAttributeAccess(self):

        localctx = D96Parser.Exp_StaticAttributeAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_exp_StaticAttributeAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            self.match(D96Parser.ID)
            self.state = 297
            self.match(D96Parser.SCOPE)
            self.state = 298
            self.match(D96Parser.STATIC)
            self.state = 299
            self.match(D96Parser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_InstanceMethodInvocationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_InstanceMethodInvocationTerm(self):
            return self.getTypedRuleContext(D96Parser.Exp_InstanceMethodInvocationTermContext,0)


        def exp_InstanceMethodInvocation(self):
            return self.getTypedRuleContext(D96Parser.Exp_InstanceMethodInvocationContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def list_Expr(self):
            return self.getTypedRuleContext(D96Parser.List_ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp_InstanceMethodInvocation



    def exp_InstanceMethodInvocation(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp_InstanceMethodInvocationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 40
        self.enterRecursionRule(localctx, 40, self.RULE_exp_InstanceMethodInvocation, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.exp_InstanceMethodInvocationTerm()
            self._ctx.stop = self._input.LT(-1)
            self.state = 313
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,23,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp_InstanceMethodInvocationContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_InstanceMethodInvocation)
                    self.state = 304
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 305
                    self.match(D96Parser.DOT)
                    self.state = 306
                    self.match(D96Parser.ID)
                    self.state = 307
                    self.match(D96Parser.LB)
                    self.state = 308
                    self.list_Expr()
                    self.state = 309
                    self.match(D96Parser.RB) 
                self.state = 315
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp_InstanceMethodInvocationTermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp_ClassObject(self):
            return self.getTypedRuleContext(D96Parser.Exp_ClassObjectContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def SELF(self):
            return self.getToken(D96Parser.SELF, 0)

        def exp_StaticAttributeAccess(self):
            return self.getTypedRuleContext(D96Parser.Exp_StaticAttributeAccessContext,0)


        def exp_StaticMethodInvocation(self):
            return self.getTypedRuleContext(D96Parser.Exp_StaticMethodInvocationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp_InstanceMethodInvocationTerm




    def exp_InstanceMethodInvocationTerm(self):

        localctx = D96Parser.Exp_InstanceMethodInvocationTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_exp_InstanceMethodInvocationTerm)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 324
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 316
                self.match(D96Parser.LB)
                self.state = 317
                self.exp_ClassObject()
                self.state = 318
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.state = 320
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.state = 321
                self.match(D96Parser.SELF)
                pass

            elif la_ == 4:
                self.state = 322
                self.exp_StaticAttributeAccess()
                pass

            elif la_ == 5:
                self.state = 323
                self.exp_StaticMethodInvocation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_StaticMethodInvocationContext(ParserRuleContext):

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

        def list_Expr(self):
            return self.getTypedRuleContext(D96Parser.List_ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp_StaticMethodInvocation




    def exp_StaticMethodInvocation(self):

        localctx = D96Parser.Exp_StaticMethodInvocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_exp_StaticMethodInvocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 326
            self.match(D96Parser.ID)
            self.state = 327
            self.match(D96Parser.SCOPE)
            self.state = 328
            self.match(D96Parser.STATIC)
            self.state = 329
            self.match(D96Parser.ID)
            self.state = 330
            self.match(D96Parser.LB)
            self.state = 331
            self.list_Expr()
            self.state = 332
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_InstanceAttributeMethodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_InstanceAttributeMethodTerm(self):
            return self.getTypedRuleContext(D96Parser.Exp_InstanceAttributeMethodTermContext,0)


        def exp_InstanceAttributeMethod(self):
            return self.getTypedRuleContext(D96Parser.Exp_InstanceAttributeMethodContext,0)


        def DOT(self):
            return self.getToken(D96Parser.DOT, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def list_Expr(self):
            return self.getTypedRuleContext(D96Parser.List_ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp_InstanceAttributeMethod



    def exp_InstanceAttributeMethod(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp_InstanceAttributeMethodContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 46
        self.enterRecursionRule(localctx, 46, self.RULE_exp_InstanceAttributeMethod, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 335
            self.exp_InstanceAttributeMethodTerm()
            self._ctx.stop = self._input.LT(-1)
            self.state = 350
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp_InstanceAttributeMethodContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_InstanceAttributeMethod)
                    self.state = 337
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 346
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                    if la_ == 1:
                        self.state = 338
                        self.match(D96Parser.DOT)
                        self.state = 339
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 2:
                        self.state = 340
                        self.match(D96Parser.DOT)
                        self.state = 341
                        self.match(D96Parser.ID)
                        self.state = 342
                        self.match(D96Parser.LB)
                        self.state = 343
                        self.list_Expr()
                        self.state = 344
                        self.match(D96Parser.RB)
                        pass

             
                self.state = 352
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Exp_InstanceAttributeMethodTermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_InstanceAttributeAccess(self):
            return self.getTypedRuleContext(D96Parser.Exp_InstanceAttributeAccessContext,0)


        def exp_InstanceMethodInvocation(self):
            return self.getTypedRuleContext(D96Parser.Exp_InstanceMethodInvocationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp_InstanceAttributeMethodTerm




    def exp_InstanceAttributeMethodTerm(self):

        localctx = D96Parser.Exp_InstanceAttributeMethodTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_exp_InstanceAttributeMethodTerm)
        try:
            self.state = 355
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 353
                self.exp_InstanceAttributeAccess(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 354
                self.exp_InstanceMethodInvocation(0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_MemberAccessContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_InstanceAttributeMethod(self):
            return self.getTypedRuleContext(D96Parser.Exp_InstanceAttributeMethodContext,0)


        def exp_StaticAttributeAccess(self):
            return self.getTypedRuleContext(D96Parser.Exp_StaticAttributeAccessContext,0)


        def exp_StaticMethodInvocation(self):
            return self.getTypedRuleContext(D96Parser.Exp_StaticMethodInvocationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp_MemberAccess




    def exp_MemberAccess(self):

        localctx = D96Parser.Exp_MemberAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_exp_MemberAccess)
        try:
            self.state = 360
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 357
                self.exp_InstanceAttributeMethod(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 358
                self.exp_StaticAttributeAccess()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 359
                self.exp_StaticMethodInvocation()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_ObjCreationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NEW(self):
            return self.getToken(D96Parser.NEW, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def list_Expr(self):
            return self.getTypedRuleContext(D96Parser.List_ExprContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def exp_ObjCreation(self):
            return self.getTypedRuleContext(D96Parser.Exp_ObjCreationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp_ObjCreation




    def exp_ObjCreation(self):

        localctx = D96Parser.Exp_ObjCreationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_exp_ObjCreation)
        try:
            self.state = 372
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.match(D96Parser.NEW)
                self.state = 363
                self.match(D96Parser.ID)
                self.state = 364
                self.match(D96Parser.LB)
                self.state = 365
                self.list_Expr()
                self.state = 366
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 368
                self.match(D96Parser.LB)
                self.state = 369
                self.exp_ObjCreation()
                self.state = 370
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


    class Exp_ClassObjectContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def exp_ObjCreation(self):
            return self.getTypedRuleContext(D96Parser.Exp_ObjCreationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp_ClassObject




    def exp_ClassObject(self):

        localctx = D96Parser.Exp_ClassObjectContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_exp_ClassObject)
        try:
            self.state = 376
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.NEW, D96Parser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 375
                self.exp_ObjCreation()
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


    class Exp_MethodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def list_Expr(self):
            return self.getTypedRuleContext(D96Parser.List_ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp_Method




    def exp_Method(self):

        localctx = D96Parser.Exp_MethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_exp_Method)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 378
            self.match(D96Parser.ID)
            self.state = 379
            self.match(D96Parser.LB)

            self.state = 380
            self.list_Expr()
            self.state = 381
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

        def exp_ObjCreation(self):
            return self.getTypedRuleContext(D96Parser.Exp_ObjCreationContext,0)


        def exp_MemberAccess(self):
            return self.getTypedRuleContext(D96Parser.Exp_MemberAccessContext,0)


        def exp_IntFloat(self):
            return self.getTypedRuleContext(D96Parser.Exp_IntFloatContext,0)


        def exp_Bool(self):
            return self.getTypedRuleContext(D96Parser.Exp_BoolContext,0)


        def exp_Str(self):
            return self.getTypedRuleContext(D96Parser.Exp_StrContext,0)


        def exp_Idx(self):
            return self.getTypedRuleContext(D96Parser.Exp_IdxContext,0)


        def exp_RelationalOperation(self):
            return self.getTypedRuleContext(D96Parser.Exp_RelationalOperationContext,0)


        def datalit(self):
            return self.getTypedRuleContext(D96Parser.DatalitContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr




    def expr(self):

        localctx = D96Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_expr)
        try:
            self.state = 391
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,31,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 383
                self.exp_ObjCreation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 384
                self.exp_MemberAccess()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 385
                self.exp_IntFloat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 386
                self.exp_Bool()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 387
                self.exp_Str()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 388
                self.exp_Idx()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 389
                self.exp_RelationalOperation()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 390
                self.datalit()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_ExprContext(ParserRuleContext):

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
            return D96Parser.RULE_list_Expr




    def list_Expr(self):

        localctx = D96Parser.List_ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_list_Expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLLIT) | (1 << D96Parser.STRLIT) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.STATIC) | (1 << D96Parser.NOT) | (1 << D96Parser.LB) | (1 << D96Parser.ID))) != 0):
                self.state = 393
                self.expr()
                self.state = 398
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.CM:
                    self.state = 394
                    self.match(D96Parser.CM)
                    self.state = 395
                    self.expr()
                    self.state = 400
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Type_DataContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(D96Parser.INT, 0)

        def FLOAT(self):
            return self.getToken(D96Parser.FLOAT, 0)

        def BOOLEAN(self):
            return self.getToken(D96Parser.BOOLEAN, 0)

        def STRING(self):
            return self.getToken(D96Parser.STRING, 0)

        def array_Type(self):
            return self.getTypedRuleContext(D96Parser.Array_TypeContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_type_Data




    def type_Data(self):

        localctx = D96Parser.Type_DataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_type_Data)
        try:
            self.state = 408
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 403
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 404
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 405
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 406
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 407
                self.array_Type()
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


    class Array_TypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LSB(self):
            return self.getToken(D96Parser.LSB, 0)

        def type_Data(self):
            return self.getTypedRuleContext(D96Parser.Type_DataContext,0)


        def CM(self):
            return self.getToken(D96Parser.CM, 0)

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def RSB(self):
            return self.getToken(D96Parser.RSB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_array_Type




    def array_Type(self):

        localctx = D96Parser.Array_TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_array_Type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(D96Parser.ARRAY)
            self.state = 411
            self.match(D96Parser.LSB)
            self.state = 412
            self.type_Data()
            self.state = 413
            self.match(D96Parser.CM)
            self.state = 414
            self.match(D96Parser.INTLIT)
            self.state = 415
            self.match(D96Parser.RSB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Seq_IDContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_seq_ID




    def seq_ID(self):

        localctx = D96Parser.Seq_IDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_seq_ID)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 417
            self.match(D96Parser.ID)
            self.state = 422
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 418
                self.match(D96Parser.CM)
                self.state = 419
                self.match(D96Parser.ID)
                self.state = 424
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_VarDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def seq_ID(self):
            return self.getTypedRuleContext(D96Parser.Seq_IDContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def type_Data(self):
            return self.getTypedRuleContext(D96Parser.Type_DataContext,0)


        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def list_Expr(self):
            return self.getTypedRuleContext(D96Parser.List_ExprContext,0)


        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stmt_VarDeclaration




    def stmt_VarDeclaration(self):

        localctx = D96Parser.Stmt_VarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_stmt_VarDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 426
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.VAL or _la==D96Parser.VAR:
                self.state = 425
                _la = self._input.LA(1)
                if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 429
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.STATIC:
                self.state = 428
                self.match(D96Parser.STATIC)


            self.state = 431
            self.seq_ID()
            self.state = 432
            self.match(D96Parser.COLON)
            self.state = 433
            self.type_Data()
            self.state = 436
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN:
                self.state = 434
                self.match(D96Parser.ASSIGN)
                self.state = 435
                self.list_Expr()


            self.state = 438
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_lhs




    def lhs(self):

        localctx = D96Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_lhs)
        try:
            self.state = 442
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 440
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 441
                self.expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_AssignContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(D96Parser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stmt_Assign




    def stmt_Assign(self):

        localctx = D96Parser.Stmt_AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_stmt_Assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 444
            self.lhs()
            self.state = 445
            self.match(D96Parser.ASSIGN)
            self.state = 446
            self.expr()
            self.state = 447
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_IfContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(D96Parser.IF, 0)

        def LB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.LB)
            else:
                return self.getToken(D96Parser.LB, i)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def RB(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.RB)
            else:
                return self.getToken(D96Parser.RB, i)

        def stmt_Block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Stmt_BlockContext)
            else:
                return self.getTypedRuleContext(D96Parser.Stmt_BlockContext,i)


        def ELSEIF(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ELSEIF)
            else:
                return self.getToken(D96Parser.ELSEIF, i)

        def ELSE(self):
            return self.getToken(D96Parser.ELSE, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stmt_If




    def stmt_If(self):

        localctx = D96Parser.Stmt_IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_stmt_If)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 449
            self.match(D96Parser.IF)
            self.state = 450
            self.match(D96Parser.LB)
            self.state = 451
            self.expr()
            self.state = 452
            self.match(D96Parser.RB)
            self.state = 456
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 453
                    self.stmt_Block() 
                self.state = 458
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

            self.state = 471
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 459
                self.match(D96Parser.ELSEIF)
                self.state = 460
                self.match(D96Parser.LB)
                self.state = 461
                self.expr()
                self.state = 462
                self.match(D96Parser.RB)
                self.state = 466
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 463
                        self.stmt_Block() 
                    self.state = 468
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

                self.state = 473
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 481
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 474
                self.match(D96Parser.ELSE)
                self.state = 478
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,43,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 475
                        self.stmt_Block() 
                    self.state = 480
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,43,self._ctx)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_ForInContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOREACH(self):
            return self.getToken(D96Parser.FOREACH, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def IN(self):
            return self.getToken(D96Parser.IN, 0)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.ExprContext)
            else:
                return self.getTypedRuleContext(D96Parser.ExprContext,i)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def stmt_Block(self):
            return self.getTypedRuleContext(D96Parser.Stmt_BlockContext,0)


        def BY(self):
            return self.getToken(D96Parser.BY, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stmt_ForIn




    def stmt_ForIn(self):

        localctx = D96Parser.Stmt_ForInContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_stmt_ForIn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 483
            self.match(D96Parser.FOREACH)
            self.state = 484
            self.match(D96Parser.LB)
            self.state = 485
            self.match(D96Parser.ID)
            self.state = 486
            self.match(D96Parser.IN)
            self.state = 487
            self.expr()
            self.state = 488
            self.match(D96Parser.T__0)
            self.state = 489
            self.expr()
            self.state = 492
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 490
                self.match(D96Parser.BY)
                self.state = 491
                self.expr()


            self.state = 494
            self.match(D96Parser.RB)
            self.state = 495
            self.stmt_Block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_BlockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def list_Stmt(self):
            return self.getTypedRuleContext(D96Parser.List_StmtContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt_Block




    def stmt_Block(self):

        localctx = D96Parser.Stmt_BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_stmt_Block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 497
            self.match(D96Parser.LCB)

            self.state = 498
            self.list_Stmt()
            self.state = 499
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_MethodInvocationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def exp_InstanceMethodInvocation(self):
            return self.getTypedRuleContext(D96Parser.Exp_InstanceMethodInvocationContext,0)


        def exp_StaticMethodInvocation(self):
            return self.getTypedRuleContext(D96Parser.Exp_StaticMethodInvocationContext,0)


        def exp_Method(self):
            return self.getTypedRuleContext(D96Parser.Exp_MethodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt_MethodInvocation




    def stmt_MethodInvocation(self):

        localctx = D96Parser.Stmt_MethodInvocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_stmt_MethodInvocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 504
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,46,self._ctx)
            if la_ == 1:
                self.state = 501
                self.exp_InstanceMethodInvocation(0)
                pass

            elif la_ == 2:
                self.state = 502
                self.exp_StaticMethodInvocation()
                pass

            elif la_ == 3:
                self.state = 503
                self.exp_Method()
                pass


            self.state = 506
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_ContinueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stmt_Continue




    def stmt_Continue(self):

        localctx = D96Parser.Stmt_ContinueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_stmt_Continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 508
            self.match(D96Parser.CONTINUE)
            self.state = 509
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_ReturnContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(D96Parser.RETURN, 0)

        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt_Return




    def stmt_Return(self):

        localctx = D96Parser.Stmt_ReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_stmt_Return)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511
            self.match(D96Parser.RETURN)
            self.state = 513
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLLIT) | (1 << D96Parser.STRLIT) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.STATIC) | (1 << D96Parser.NOT) | (1 << D96Parser.LB) | (1 << D96Parser.ID))) != 0):
                self.state = 512
                self.expr()


            self.state = 515
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_BreakContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stmt_Break




    def stmt_Break(self):

        localctx = D96Parser.Stmt_BreakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_stmt_Break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 517
            self.match(D96Parser.BREAK)
            self.state = 518
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_VarDeclaration(self):
            return self.getTypedRuleContext(D96Parser.Stmt_VarDeclarationContext,0)


        def stmt_Assign(self):
            return self.getTypedRuleContext(D96Parser.Stmt_AssignContext,0)


        def stmt_If(self):
            return self.getTypedRuleContext(D96Parser.Stmt_IfContext,0)


        def stmt_ForIn(self):
            return self.getTypedRuleContext(D96Parser.Stmt_ForInContext,0)


        def stmt_Block(self):
            return self.getTypedRuleContext(D96Parser.Stmt_BlockContext,0)


        def stmt_MethodInvocation(self):
            return self.getTypedRuleContext(D96Parser.Stmt_MethodInvocationContext,0)


        def stmt_Continue(self):
            return self.getTypedRuleContext(D96Parser.Stmt_ContinueContext,0)


        def stmt_Return(self):
            return self.getTypedRuleContext(D96Parser.Stmt_ReturnContext,0)


        def stmt_Break(self):
            return self.getTypedRuleContext(D96Parser.Stmt_BreakContext,0)


        def stmt_MethodDeclaration(self):
            return self.getTypedRuleContext(D96Parser.Stmt_MethodDeclarationContext,0)


        def stmt_Class(self):
            return self.getTypedRuleContext(D96Parser.Stmt_ClassContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_stmt)
        try:
            self.state = 531
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,48,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 520
                self.stmt_VarDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 521
                self.stmt_Assign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 522
                self.stmt_If()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 523
                self.stmt_ForIn()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 524
                self.stmt_Block()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 525
                self.stmt_MethodInvocation()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 526
                self.stmt_Continue()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 527
                self.stmt_Return()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 528
                self.stmt_Break()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 529
                self.stmt_MethodDeclaration()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 530
                self.stmt_Class()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_StmtContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.StmtContext)
            else:
                return self.getTypedRuleContext(D96Parser.StmtContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_list_Stmt




    def list_Stmt(self):

        localctx = D96Parser.List_StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_list_Stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 536
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLLIT) | (1 << D96Parser.STRLIT) | (1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.ARRAY) | (1 << D96Parser.RETURN) | (1 << D96Parser.CLASS) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.STATIC) | (1 << D96Parser.NOT) | (1 << D96Parser.LB) | (1 << D96Parser.LCB) | (1 << D96Parser.ID))) != 0):
                self.state = 533
                self.stmt()
                self.state = 538
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_ClassContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_Construction(self):
            return self.getTypedRuleContext(D96Parser.Class_ConstructionContext,0)


        def class_Destruction(self):
            return self.getTypedRuleContext(D96Parser.Class_DestructionContext,0)


        def class_Declaration(self):
            return self.getTypedRuleContext(D96Parser.Class_DeclarationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt_Class




    def stmt_Class(self):

        localctx = D96Parser.Stmt_ClassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_stmt_Class)
        try:
            self.state = 542
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 539
                self.class_Construction()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 540
                self.class_Destruction()
                pass
            elif token in [D96Parser.CLASS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 541
                self.class_Declaration()
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


    class Stmt_ClassDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def stmt_VarDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Stmt_VarDeclarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.Stmt_VarDeclarationContext,i)


        def stmt_MethodDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Stmt_MethodDeclarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.Stmt_MethodDeclarationContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt_ClassDeclaration




    def stmt_ClassDeclaration(self):

        localctx = D96Parser.Stmt_ClassDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_stmt_ClassDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 544
            self.match(D96Parser.CLASS)
            self.state = 545
            self.match(D96Parser.ID)
            self.state = 548
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 546
                self.match(D96Parser.COLON)
                self.state = 547
                self.match(D96Parser.ID)


            self.state = 550
            self.match(D96Parser.LCB)
            self.state = 555
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.STATIC) | (1 << D96Parser.ID))) != 0):
                self.state = 553
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
                if la_ == 1:
                    self.state = 551
                    self.stmt_VarDeclaration()
                    pass

                elif la_ == 2:
                    self.state = 552
                    self.stmt_MethodDeclaration()
                    pass


                self.state = 557
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 558
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_MethodDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def stmt_Block(self):
            return self.getTypedRuleContext(D96Parser.Stmt_BlockContext,0)


        def STATIC(self):
            return self.getToken(D96Parser.STATIC, 0)

        def list_Parameters(self):
            return self.getTypedRuleContext(D96Parser.List_ParametersContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt_MethodDeclaration




    def stmt_MethodDeclaration(self):

        localctx = D96Parser.Stmt_MethodDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_stmt_MethodDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 561
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.STATIC:
                self.state = 560
                self.match(D96Parser.STATIC)


            self.state = 563
            self.match(D96Parser.ID)
            self.state = 564
            self.match(D96Parser.LB)
            self.state = 566
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 565
                self.list_Parameters()


            self.state = 568
            self.match(D96Parser.RB)
            self.state = 569
            self.stmt_Block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def list_Stmt(self):
            return self.getTypedRuleContext(D96Parser.List_StmtContext,0)


        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_class_Declaration




    def class_Declaration(self):

        localctx = D96Parser.Class_DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_class_Declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 571
            self.match(D96Parser.CLASS)
            self.state = 572
            self.match(D96Parser.ID)
            self.state = 575
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 573
                self.match(D96Parser.COLON)
                self.state = 574
                self.match(D96Parser.ID)


            self.state = 577
            self.match(D96Parser.LCB)
            self.state = 578
            self.list_Stmt()
            self.state = 579
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_ConstructionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONSTRUCTOR(self):
            return self.getToken(D96Parser.CONSTRUCTOR, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def stmt_Block(self):
            return self.getTypedRuleContext(D96Parser.Stmt_BlockContext,0)


        def list_Parameters(self):
            return self.getTypedRuleContext(D96Parser.List_ParametersContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_Construction




    def class_Construction(self):

        localctx = D96Parser.Class_ConstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_class_Construction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 581
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 582
            self.match(D96Parser.LB)
            self.state = 584
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 583
                self.list_Parameters()


            self.state = 586
            self.match(D96Parser.RB)
            self.state = 587
            self.stmt_Block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_DestructionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DESTRUCTOR(self):
            return self.getToken(D96Parser.DESTRUCTOR, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def stmt_Block(self):
            return self.getTypedRuleContext(D96Parser.Stmt_BlockContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_Destruction




    def class_Destruction(self):

        localctx = D96Parser.Class_DestructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_class_Destruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 589
            self.match(D96Parser.DESTRUCTOR)
            self.state = 590
            self.match(D96Parser.RB)
            self.state = 591
            self.match(D96Parser.LB)
            self.state = 592
            self.stmt_Block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_ParametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def seq_Parameters(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Seq_ParametersContext)
            else:
                return self.getTypedRuleContext(D96Parser.Seq_ParametersContext,i)


        def SM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.SM)
            else:
                return self.getToken(D96Parser.SM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_list_Parameters




    def list_Parameters(self):

        localctx = D96Parser.List_ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_list_Parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 594
            self.seq_Parameters()
            self.state = 599
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SM:
                self.state = 595
                self.match(D96Parser.SM)
                self.state = 596
                self.seq_Parameters()
                self.state = 601
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Seq_ParametersContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def seq_ID(self):
            return self.getTypedRuleContext(D96Parser.Seq_IDContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def type_Data(self):
            return self.getTypedRuleContext(D96Parser.Type_DataContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_seq_Parameters




    def seq_Parameters(self):

        localctx = D96Parser.Seq_ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_seq_Parameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 602
            self.seq_ID()
            self.state = 603
            self.match(D96Parser.COLON)
            self.state = 604
            self.type_Data()
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
        self.enterRule(localctx, 108, self.RULE_idx_arraylit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 606
            self.match(D96Parser.ARRAY)
            self.state = 607
            self.match(D96Parser.LB)
            self.state = 616
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLLIT) | (1 << D96Parser.STRLIT) | (1 << D96Parser.ARRAY))) != 0):
                self.state = 608
                self.datalit()
                self.state = 613
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.CM:
                    self.state = 609
                    self.match(D96Parser.CM)
                    self.state = 610
                    self.datalit()
                    self.state = 615
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 618
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
        self.enterRule(localctx, 110, self.RULE_datalit)
        try:
            self.state = 625
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 620
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 621
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.BOOLLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 622
                self.match(D96Parser.BOOLLIT)
                pass
            elif token in [D96Parser.STRLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 623
                self.match(D96Parser.STRLIT)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 624
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
        self._predicates[2] = self.exp_0_sempred
        self._predicates[3] = self.exp_1_sempred
        self._predicates[15] = self.exp_TermIdx_sempred
        self._predicates[17] = self.exp_InstanceAttributeAccess_sempred
        self._predicates[20] = self.exp_InstanceMethodInvocation_sempred
        self._predicates[23] = self.exp_InstanceAttributeMethod_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def exp_0_sempred(self, localctx:Exp_0Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         

    def exp_1_sempred(self, localctx:Exp_1Context, predIndex:int):
            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         

    def exp_TermIdx_sempred(self, localctx:Exp_TermIdxContext, predIndex:int):
            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 1)
         

    def exp_InstanceAttributeAccess_sempred(self, localctx:Exp_InstanceAttributeAccessContext, predIndex:int):
            if predIndex == 4:
                return self.precpred(self._ctx, 2)
         

    def exp_InstanceMethodInvocation_sempred(self, localctx:Exp_InstanceMethodInvocationContext, predIndex:int):
            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def exp_InstanceAttributeMethod_sempred(self, localctx:Exp_InstanceAttributeMethodContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 2)
         




