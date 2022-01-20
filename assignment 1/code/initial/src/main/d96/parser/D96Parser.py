# Generated from main/d96/parser/D96.g4 by ANTLR 4.9.3
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
        buf.write("\u0275\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
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
        buf.write("\3\"\3#\5#\u01a5\n#\3#\3#\3#\5#\u01aa\n#\3#\7#\u01ad\n")
        buf.write("#\f#\16#\u01b0\13#\3$\5$\u01b3\n$\3$\3$\3$\3$\3$\5$\u01ba")
        buf.write("\n$\3$\3$\3%\3%\5%\u01c0\n%\3&\3&\3&\3&\3&\3\'\3\'\3\'")
        buf.write("\3\'\3\'\7\'\u01cc\n\'\f\'\16\'\u01cf\13\'\3\'\3\'\3\'")
        buf.write("\3\'\3\'\7\'\u01d6\n\'\f\'\16\'\u01d9\13\'\7\'\u01db\n")
        buf.write("\'\f\'\16\'\u01de\13\'\3\'\3\'\7\'\u01e2\n\'\f\'\16\'")
        buf.write("\u01e5\13\'\5\'\u01e7\n\'\3(\3(\3(\3(\3(\3(\3(\3(\3(\5")
        buf.write("(\u01f2\n(\3(\3(\3(\3)\3)\3)\3)\3*\3*\3*\5*\u01fe\n*\3")
        buf.write("*\3*\3+\3+\3+\3,\3,\5,\u0207\n,\3,\3,\3-\3-\3-\3.\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3.\3.\5.\u0219\n.\3/\7/\u021c\n/\f")
        buf.write("/\16/\u021f\13/\3\60\3\60\3\60\5\60\u0224\n\60\3\61\3")
        buf.write("\61\3\61\3\61\3\61\7\61\u022b\n\61\f\61\16\61\u022e\13")
        buf.write("\61\3\61\3\61\3\62\5\62\u0233\n\62\3\62\3\62\3\62\5\62")
        buf.write("\u0238\n\62\3\62\3\62\3\62\3\63\3\63\3\63\3\63\5\63\u0241")
        buf.write("\n\63\3\63\3\63\3\63\3\63\3\64\3\64\3\64\5\64\u024a\n")
        buf.write("\64\3\64\3\64\3\64\3\65\3\65\3\65\3\65\3\65\3\66\3\66")
        buf.write("\3\66\7\66\u0257\n\66\f\66\16\66\u025a\13\66\3\67\3\67")
        buf.write("\3\67\3\67\38\38\38\38\38\78\u0265\n8\f8\168\u0268\13")
        buf.write("8\58\u026a\n8\38\38\39\39\39\39\39\59\u0273\n9\39\2\b")
        buf.write("\6\b $*\60:\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"")
        buf.write("$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnp\2\t\3")
        buf.write("\2\35\36\3\2\37!\3\2+,\3\2()\3\2\"#\3\2$\'\3\2\25\26\2")
        buf.write("\u02a9\2s\3\2\2\2\4y\3\2\2\2\6{\3\2\2\2\b\u0086\3\2\2")
        buf.write("\2\n\u009b\3\2\2\2\f\u00a5\3\2\2\2\16\u00b1\3\2\2\2\20")
        buf.write("\u00b8\3\2\2\2\22\u00c4\3\2\2\2\24\u00c6\3\2\2\2\26\u00d8")
        buf.write("\3\2\2\2\30\u00da\3\2\2\2\32\u00e8\3\2\2\2\34\u00ec\3")
        buf.write("\2\2\2\36\u00f0\3\2\2\2 \u00f4\3\2\2\2\"\u0113\3\2\2\2")
        buf.write("$\u0115\3\2\2\2&\u0128\3\2\2\2(\u012a\3\2\2\2*\u012f\3")
        buf.write("\2\2\2,\u0146\3\2\2\2.\u0148\3\2\2\2\60\u0150\3\2\2\2")
        buf.write("\62\u0165\3\2\2\2\64\u016a\3\2\2\2\66\u0176\3\2\2\28\u017a")
        buf.write("\3\2\2\2:\u017c\3\2\2\2<\u0189\3\2\2\2>\u0193\3\2\2\2")
        buf.write("@\u019a\3\2\2\2B\u019c\3\2\2\2D\u01a4\3\2\2\2F\u01b2\3")
        buf.write("\2\2\2H\u01bf\3\2\2\2J\u01c1\3\2\2\2L\u01c6\3\2\2\2N\u01e8")
        buf.write("\3\2\2\2P\u01f6\3\2\2\2R\u01fd\3\2\2\2T\u0201\3\2\2\2")
        buf.write("V\u0204\3\2\2\2X\u020a\3\2\2\2Z\u0218\3\2\2\2\\\u021d")
        buf.write("\3\2\2\2^\u0223\3\2\2\2`\u0225\3\2\2\2b\u0232\3\2\2\2")
        buf.write("d\u023c\3\2\2\2f\u0246\3\2\2\2h\u024e\3\2\2\2j\u0253\3")
        buf.write("\2\2\2l\u025b\3\2\2\2n\u025f\3\2\2\2p\u0272\3\2\2\2rt")
        buf.write("\5`\61\2sr\3\2\2\2tu\3\2\2\2us\3\2\2\2uv\3\2\2\2vw\3\2")
        buf.write("\2\2wx\7\2\2\3x\3\3\2\2\2yz\5\6\4\2z\5\3\2\2\2{|\b\4\1")
        buf.write("\2|}\5\b\5\2}\u0083\3\2\2\2~\177\f\4\2\2\177\u0080\t\2")
        buf.write("\2\2\u0080\u0082\5\b\5\2\u0081~\3\2\2\2\u0082\u0085\3")
        buf.write("\2\2\2\u0083\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084\7")
        buf.write("\3\2\2\2\u0085\u0083\3\2\2\2\u0086\u0087\b\5\1\2\u0087")
        buf.write("\u0088\5\n\6\2\u0088\u008e\3\2\2\2\u0089\u008a\f\4\2\2")
        buf.write("\u008a\u008b\t\3\2\2\u008b\u008d\5\n\6\2\u008c\u0089\3")
        buf.write("\2\2\2\u008d\u0090\3\2\2\2\u008e\u008c\3\2\2\2\u008e\u008f")
        buf.write("\3\2\2\2\u008f\t\3\2\2\2\u0090\u008e\3\2\2\2\u0091\u009c")
        buf.write("\7>\2\2\u0092\u009c\7:\2\2\u0093\u009c\7;\2\2\u0094\u009c")
        buf.write("\5\64\33\2\u0095\u009c\5:\36\2\u0096\u009c\5\36\20\2\u0097")
        buf.write("\u0098\7\60\2\2\u0098\u0099\5\6\4\2\u0099\u009a\7\61\2")
        buf.write("\2\u009a\u009c\3\2\2\2\u009b\u0091\3\2\2\2\u009b\u0092")
        buf.write("\3\2\2\2\u009b\u0093\3\2\2\2\u009b\u0094\3\2\2\2\u009b")
        buf.write("\u0095\3\2\2\2\u009b\u0096\3\2\2\2\u009b\u0097\3\2\2\2")
        buf.write("\u009c\13\3\2\2\2\u009d\u009e\5\16\b\2\u009e\u009f\t\4")
        buf.write("\2\2\u009f\u00a0\5\f\7\2\u00a0\u00a6\3\2\2\2\u00a1\u00a3")
        buf.write("\7*\2\2\u00a2\u00a1\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3")
        buf.write("\u00a4\3\2\2\2\u00a4\u00a6\5\16\b\2\u00a5\u009d\3\2\2")
        buf.write("\2\u00a5\u00a2\3\2\2\2\u00a6\r\3\2\2\2\u00a7\u00a9\7\34")
        buf.write("\2\2\u00a8\u00a7\3\2\2\2\u00a8\u00a9\3\2\2\2\u00a9\u00aa")
        buf.write("\3\2\2\2\u00aa\u00b2\7>\2\2\u00ab\u00b2\7<\2\2\u00ac\u00b2")
        buf.write("\5\64\33\2\u00ad\u00ae\7\60\2\2\u00ae\u00af\5\f\7\2\u00af")
        buf.write("\u00b0\7\61\2\2\u00b0\u00b2\3\2\2\2\u00b1\u00a8\3\2\2")
        buf.write("\2\u00b1\u00ab\3\2\2\2\u00b1\u00ac\3\2\2\2\u00b1\u00ad")
        buf.write("\3\2\2\2\u00b2\17\3\2\2\2\u00b3\u00b4\5\22\n\2\u00b4\u00b5")
        buf.write("\t\5\2\2\u00b5\u00b6\5\20\t\2\u00b6\u00b9\3\2\2\2\u00b7")
        buf.write("\u00b9\5\22\n\2\u00b8\u00b3\3\2\2\2\u00b8\u00b7\3\2\2")
        buf.write("\2\u00b9\21\3\2\2\2\u00ba\u00bc\7\34\2\2\u00bb\u00ba\3")
        buf.write("\2\2\2\u00bb\u00bc\3\2\2\2\u00bc\u00bd\3\2\2\2\u00bd\u00c5")
        buf.write("\7>\2\2\u00be\u00c5\7=\2\2\u00bf\u00c5\5\64\33\2\u00c0")
        buf.write("\u00c1\7\60\2\2\u00c1\u00c2\5\20\t\2\u00c2\u00c3\7\61")
        buf.write("\2\2\u00c3\u00c5\3\2\2\2\u00c4\u00bb\3\2\2\2\u00c4\u00be")
        buf.write("\3\2\2\2\u00c4\u00bf\3\2\2\2\u00c4\u00c0\3\2\2\2\u00c5")
        buf.write("\23\3\2\2\2\u00c6\u00c7\5\26\f\2\u00c7\u00c8\t\6\2\2\u00c8")
        buf.write("\u00c9\5\26\f\2\u00c9\25\3\2\2\2\u00ca\u00cb\7\60\2\2")
        buf.write("\u00cb\u00cc\5<\37\2\u00cc\u00cd\7\61\2\2\u00cd\u00d9")
        buf.write("\3\2\2\2\u00ce\u00d9\7:\2\2\u00cf\u00d9\7<\2\2\u00d0\u00d2")
        buf.write("\7\34\2\2\u00d1\u00d0\3\2\2\2\u00d1\u00d2\3\2\2\2\u00d2")
        buf.write("\u00d3\3\2\2\2\u00d3\u00d9\7>\2\2\u00d4\u00d5\7\60\2\2")
        buf.write("\u00d5\u00d6\5\24\13\2\u00d6\u00d7\7\61\2\2\u00d7\u00d9")
        buf.write("\3\2\2\2\u00d8\u00ca\3\2\2\2\u00d8\u00ce\3\2\2\2\u00d8")
        buf.write("\u00cf\3\2\2\2\u00d8\u00d1\3\2\2\2\u00d8\u00d4\3\2\2\2")
        buf.write("\u00d9\27\3\2\2\2\u00da\u00db\5\32\16\2\u00db\u00dc\t")
        buf.write("\7\2\2\u00dc\u00dd\5\32\16\2\u00dd\31\3\2\2\2\u00de\u00df")
        buf.write("\7\60\2\2\u00df\u00e0\5<\37\2\u00e0\u00e1\7\61\2\2\u00e1")
        buf.write("\u00e9\3\2\2\2\u00e2\u00e9\7:\2\2\u00e3\u00e9\7;\2\2\u00e4")
        buf.write("\u00e6\7\34\2\2\u00e5\u00e4\3\2\2\2\u00e5\u00e6\3\2\2")
        buf.write("\2\u00e6\u00e7\3\2\2\2\u00e7\u00e9\7>\2\2\u00e8\u00de")
        buf.write("\3\2\2\2\u00e8\u00e2\3\2\2\2\u00e8\u00e3\3\2\2\2\u00e8")
        buf.write("\u00e5\3\2\2\2\u00e9\33\3\2\2\2\u00ea\u00ed\5\24\13\2")
        buf.write("\u00eb\u00ed\5\30\r\2\u00ec\u00ea\3\2\2\2\u00ec\u00eb")
        buf.write("\3\2\2\2\u00ed\35\3\2\2\2\u00ee\u00f1\5:\36\2\u00ef\u00f1")
        buf.write("\7>\2\2\u00f0\u00ee\3\2\2\2\u00f0\u00ef\3\2\2\2\u00f1")
        buf.write("\u00f2\3\2\2\2\u00f2\u00f3\5 \21\2\u00f3\37\3\2\2\2\u00f4")
        buf.write("\u00f5\b\21\1\2\u00f5\u00f6\7\62\2\2\u00f6\u00f7\5\"\22")
        buf.write("\2\u00f7\u00f8\7\63\2\2\u00f8\u0105\3\2\2\2\u00f9\u00fa")
        buf.write("\f\4\2\2\u00fa\u00fb\7\62\2\2\u00fb\u00fc\5\"\22\2\u00fc")
        buf.write("\u00fd\7\63\2\2\u00fd\u0104\3\2\2\2\u00fe\u00ff\f\3\2")
        buf.write("\2\u00ff\u0100\7\62\2\2\u0100\u0101\5\36\20\2\u0101\u0102")
        buf.write("\7\63\2\2\u0102\u0104\3\2\2\2\u0103\u00f9\3\2\2\2\u0103")
        buf.write("\u00fe\3\2\2\2\u0104\u0107\3\2\2\2\u0105\u0103\3\2\2\2")
        buf.write("\u0105\u0106\3\2\2\2\u0106!\3\2\2\2\u0107\u0105\3\2\2")
        buf.write("\2\u0108\u010a\7\34\2\2\u0109\u0108\3\2\2\2\u0109\u010a")
        buf.write("\3\2\2\2\u010a\u010b\3\2\2\2\u010b\u0114\7>\2\2\u010c")
        buf.write("\u0114\7:\2\2\u010d\u0114\5<\37\2\u010e\u0114\5\36\20")
        buf.write("\2\u010f\u0110\7\60\2\2\u0110\u0111\5\36\20\2\u0111\u0112")
        buf.write("\7\61\2\2\u0112\u0114\3\2\2\2\u0113\u0109\3\2\2\2\u0113")
        buf.write("\u010c\3\2\2\2\u0113\u010d\3\2\2\2\u0113\u010e\3\2\2\2")
        buf.write("\u0113\u010f\3\2\2\2\u0114#\3\2\2\2\u0115\u0116\b\23\1")
        buf.write("\2\u0116\u0117\5&\24\2\u0117\u011d\3\2\2\2\u0118\u0119")
        buf.write("\f\4\2\2\u0119\u011a\78\2\2\u011a\u011c\7>\2\2\u011b\u0118")
        buf.write("\3\2\2\2\u011c\u011f\3\2\2\2\u011d\u011b\3\2\2\2\u011d")
        buf.write("\u011e\3\2\2\2\u011e%\3\2\2\2\u011f\u011d\3\2\2\2\u0120")
        buf.write("\u0121\7\60\2\2\u0121\u0122\58\35\2\u0122\u0123\7\61\2")
        buf.write("\2\u0123\u0129\3\2\2\2\u0124\u0129\7>\2\2\u0125\u0129")
        buf.write("\7\33\2\2\u0126\u0129\5(\25\2\u0127\u0129\5.\30\2\u0128")
        buf.write("\u0120\3\2\2\2\u0128\u0124\3\2\2\2\u0128\u0125\3\2\2\2")
        buf.write("\u0128\u0126\3\2\2\2\u0128\u0127\3\2\2\2\u0129\'\3\2\2")
        buf.write("\2\u012a\u012b\7>\2\2\u012b\u012c\7/\2\2\u012c\u012d\7")
        buf.write("\34\2\2\u012d\u012e\7>\2\2\u012e)\3\2\2\2\u012f\u0130")
        buf.write("\b\26\1\2\u0130\u0131\5,\27\2\u0131\u013b\3\2\2\2\u0132")
        buf.write("\u0133\f\4\2\2\u0133\u0134\78\2\2\u0134\u0135\7>\2\2\u0135")
        buf.write("\u0136\7\60\2\2\u0136\u0137\5> \2\u0137\u0138\7\61\2\2")
        buf.write("\u0138\u013a\3\2\2\2\u0139\u0132\3\2\2\2\u013a\u013d\3")
        buf.write("\2\2\2\u013b\u0139\3\2\2\2\u013b\u013c\3\2\2\2\u013c+")
        buf.write("\3\2\2\2\u013d\u013b\3\2\2\2\u013e\u013f\7\60\2\2\u013f")
        buf.write("\u0140\58\35\2\u0140\u0141\7\61\2\2\u0141\u0147\3\2\2")
        buf.write("\2\u0142\u0147\7>\2\2\u0143\u0147\7\33\2\2\u0144\u0147")
        buf.write("\5(\25\2\u0145\u0147\5.\30\2\u0146\u013e\3\2\2\2\u0146")
        buf.write("\u0142\3\2\2\2\u0146\u0143\3\2\2\2\u0146\u0144\3\2\2\2")
        buf.write("\u0146\u0145\3\2\2\2\u0147-\3\2\2\2\u0148\u0149\7>\2\2")
        buf.write("\u0149\u014a\7/\2\2\u014a\u014b\7\34\2\2\u014b\u014c\7")
        buf.write(">\2\2\u014c\u014d\7\60\2\2\u014d\u014e\5> \2\u014e\u014f")
        buf.write("\7\61\2\2\u014f/\3\2\2\2\u0150\u0151\b\31\1\2\u0151\u0152")
        buf.write("\5\62\32\2\u0152\u0160\3\2\2\2\u0153\u015c\f\4\2\2\u0154")
        buf.write("\u0155\78\2\2\u0155\u015d\7>\2\2\u0156\u0157\78\2\2\u0157")
        buf.write("\u0158\7>\2\2\u0158\u0159\7\60\2\2\u0159\u015a\5> \2\u015a")
        buf.write("\u015b\7\61\2\2\u015b\u015d\3\2\2\2\u015c\u0154\3\2\2")
        buf.write("\2\u015c\u0156\3\2\2\2\u015d\u015f\3\2\2\2\u015e\u0153")
        buf.write("\3\2\2\2\u015f\u0162\3\2\2\2\u0160\u015e\3\2\2\2\u0160")
        buf.write("\u0161\3\2\2\2\u0161\61\3\2\2\2\u0162\u0160\3\2\2\2\u0163")
        buf.write("\u0166\5$\23\2\u0164\u0166\5*\26\2\u0165\u0163\3\2\2\2")
        buf.write("\u0165\u0164\3\2\2\2\u0166\63\3\2\2\2\u0167\u016b\5\60")
        buf.write("\31\2\u0168\u016b\5(\25\2\u0169\u016b\5.\30\2\u016a\u0167")
        buf.write("\3\2\2\2\u016a\u0168\3\2\2\2\u016a\u0169\3\2\2\2\u016b")
        buf.write("\65\3\2\2\2\u016c\u016d\7\31\2\2\u016d\u016e\7>\2\2\u016e")
        buf.write("\u016f\7\60\2\2\u016f\u0170\5> \2\u0170\u0171\7\61\2\2")
        buf.write("\u0171\u0177\3\2\2\2\u0172\u0173\7\60\2\2\u0173\u0174")
        buf.write("\5\66\34\2\u0174\u0175\7\61\2\2\u0175\u0177\3\2\2\2\u0176")
        buf.write("\u016c\3\2\2\2\u0176\u0172\3\2\2\2\u0177\67\3\2\2\2\u0178")
        buf.write("\u017b\7>\2\2\u0179\u017b\5\66\34\2\u017a\u0178\3\2\2")
        buf.write("\2\u017a\u0179\3\2\2\2\u017b9\3\2\2\2\u017c\u017d\7>\2")
        buf.write("\2\u017d\u017e\7\60\2\2\u017e\u017f\5> \2\u017f\u0180")
        buf.write("\7\61\2\2\u0180;\3\2\2\2\u0181\u018a\5\66\34\2\u0182\u018a")
        buf.write("\5\64\33\2\u0183\u018a\5\4\3\2\u0184\u018a\5\f\7\2\u0185")
        buf.write("\u018a\5\20\t\2\u0186\u018a\5\36\20\2\u0187\u018a\5\34")
        buf.write("\17\2\u0188\u018a\5p9\2\u0189\u0181\3\2\2\2\u0189\u0182")
        buf.write("\3\2\2\2\u0189\u0183\3\2\2\2\u0189\u0184\3\2\2\2\u0189")
        buf.write("\u0185\3\2\2\2\u0189\u0186\3\2\2\2\u0189\u0187\3\2\2\2")
        buf.write("\u0189\u0188\3\2\2\2\u018a=\3\2\2\2\u018b\u0190\5<\37")
        buf.write("\2\u018c\u018d\7\67\2\2\u018d\u018f\5<\37\2\u018e\u018c")
        buf.write("\3\2\2\2\u018f\u0192\3\2\2\2\u0190\u018e\3\2\2\2\u0190")
        buf.write("\u0191\3\2\2\2\u0191\u0194\3\2\2\2\u0192\u0190\3\2\2\2")
        buf.write("\u0193\u018b\3\2\2\2\u0193\u0194\3\2\2\2\u0194?\3\2\2")
        buf.write("\2\u0195\u019b\7\16\2\2\u0196\u019b\7\17\2\2\u0197\u019b")
        buf.write("\7\20\2\2\u0198\u019b\7\21\2\2\u0199\u019b\5B\"\2\u019a")
        buf.write("\u0195\3\2\2\2\u019a\u0196\3\2\2\2\u019a\u0197\3\2\2\2")
        buf.write("\u019a\u0198\3\2\2\2\u019a\u0199\3\2\2\2\u019bA\3\2\2")
        buf.write("\2\u019c\u019d\7\f\2\2\u019d\u019e\7\62\2\2\u019e\u019f")
        buf.write("\5@!\2\u019f\u01a0\7\67\2\2\u01a0\u01a1\7:\2\2\u01a1\u01a2")
        buf.write("\7\63\2\2\u01a2C\3\2\2\2\u01a3\u01a5\7\34\2\2\u01a4\u01a3")
        buf.write("\3\2\2\2\u01a4\u01a5\3\2\2\2\u01a5\u01a6\3\2\2\2\u01a6")
        buf.write("\u01ae\7>\2\2\u01a7\u01a9\7\67\2\2\u01a8\u01aa\7\34\2")
        buf.write("\2\u01a9\u01a8\3\2\2\2\u01a9\u01aa\3\2\2\2\u01aa\u01ab")
        buf.write("\3\2\2\2\u01ab\u01ad\7>\2\2\u01ac\u01a7\3\2\2\2\u01ad")
        buf.write("\u01b0\3\2\2\2\u01ae\u01ac\3\2\2\2\u01ae\u01af\3\2\2\2")
        buf.write("\u01afE\3\2\2\2\u01b0\u01ae\3\2\2\2\u01b1\u01b3\t\b\2")
        buf.write("\2\u01b2\u01b1\3\2\2\2\u01b2\u01b3\3\2\2\2\u01b3\u01b4")
        buf.write("\3\2\2\2\u01b4\u01b5\5D#\2\u01b5\u01b6\7-\2\2\u01b6\u01b9")
        buf.write("\5@!\2\u01b7\u01b8\7.\2\2\u01b8\u01ba\5> \2\u01b9\u01b7")
        buf.write("\3\2\2\2\u01b9\u01ba\3\2\2\2\u01ba\u01bb\3\2\2\2\u01bb")
        buf.write("\u01bc\7\66\2\2\u01bcG\3\2\2\2\u01bd\u01c0\7>\2\2\u01be")
        buf.write("\u01c0\5<\37\2\u01bf\u01bd\3\2\2\2\u01bf\u01be\3\2\2\2")
        buf.write("\u01c0I\3\2\2\2\u01c1\u01c2\5H%\2\u01c2\u01c3\7.\2\2\u01c3")
        buf.write("\u01c4\5<\37\2\u01c4\u01c5\7\66\2\2\u01c5K\3\2\2\2\u01c6")
        buf.write("\u01c7\7\6\2\2\u01c7\u01c8\7\60\2\2\u01c8\u01c9\5<\37")
        buf.write("\2\u01c9\u01cd\7\61\2\2\u01ca\u01cc\5P)\2\u01cb\u01ca")
        buf.write("\3\2\2\2\u01cc\u01cf\3\2\2\2\u01cd\u01cb\3\2\2\2\u01cd")
        buf.write("\u01ce\3\2\2\2\u01ce\u01dc\3\2\2\2\u01cf\u01cd\3\2\2\2")
        buf.write("\u01d0\u01d1\7\7\2\2\u01d1\u01d2\7\60\2\2\u01d2\u01d3")
        buf.write("\5<\37\2\u01d3\u01d7\7\61\2\2\u01d4\u01d6\5P)\2\u01d5")
        buf.write("\u01d4\3\2\2\2\u01d6\u01d9\3\2\2\2\u01d7\u01d5\3\2\2\2")
        buf.write("\u01d7\u01d8\3\2\2\2\u01d8\u01db\3\2\2\2\u01d9\u01d7\3")
        buf.write("\2\2\2\u01da\u01d0\3\2\2\2\u01db\u01de\3\2\2\2\u01dc\u01da")
        buf.write("\3\2\2\2\u01dc\u01dd\3\2\2\2\u01dd\u01e6\3\2\2\2\u01de")
        buf.write("\u01dc\3\2\2\2\u01df\u01e3\7\b\2\2\u01e0\u01e2\5P)\2\u01e1")
        buf.write("\u01e0\3\2\2\2\u01e2\u01e5\3\2\2\2\u01e3\u01e1\3\2\2\2")
        buf.write("\u01e3\u01e4\3\2\2\2\u01e4\u01e7\3\2\2\2\u01e5\u01e3\3")
        buf.write("\2\2\2\u01e6\u01df\3\2\2\2\u01e6\u01e7\3\2\2\2\u01e7M")
        buf.write("\3\2\2\2\u01e8\u01e9\7\t\2\2\u01e9\u01ea\7\60\2\2\u01ea")
        buf.write("\u01eb\7>\2\2\u01eb\u01ec\7\r\2\2\u01ec\u01ed\5<\37\2")
        buf.write("\u01ed\u01ee\7\3\2\2\u01ee\u01f1\5<\37\2\u01ef\u01f0\7")
        buf.write("\32\2\2\u01f0\u01f2\5<\37\2\u01f1\u01ef\3\2\2\2\u01f1")
        buf.write("\u01f2\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3\u01f4\7\61\2")
        buf.write("\2\u01f4\u01f5\5P)\2\u01f5O\3\2\2\2\u01f6\u01f7\7\64\2")
        buf.write("\2\u01f7\u01f8\5\\/\2\u01f8\u01f9\7\65\2\2\u01f9Q\3\2")
        buf.write("\2\2\u01fa\u01fe\5*\26\2\u01fb\u01fe\5.\30\2\u01fc\u01fe")
        buf.write("\5:\36\2\u01fd\u01fa\3\2\2\2\u01fd\u01fb\3\2\2\2\u01fd")
        buf.write("\u01fc\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff\u0200\7\66\2")
        buf.write("\2\u0200S\3\2\2\2\u0201\u0202\7\5\2\2\u0202\u0203\7\66")
        buf.write("\2\2\u0203U\3\2\2\2\u0204\u0206\7\22\2\2\u0205\u0207\5")
        buf.write("<\37\2\u0206\u0205\3\2\2\2\u0206\u0207\3\2\2\2\u0207\u0208")
        buf.write("\3\2\2\2\u0208\u0209\7\66\2\2\u0209W\3\2\2\2\u020a\u020b")
        buf.write("\7\4\2\2\u020b\u020c\7\66\2\2\u020cY\3\2\2\2\u020d\u0219")
        buf.write("\5F$\2\u020e\u0219\5J&\2\u020f\u0219\5L\'\2\u0210\u0219")
        buf.write("\5N(\2\u0211\u0219\5P)\2\u0212\u0219\5R*\2\u0213\u0219")
        buf.write("\5T+\2\u0214\u0219\5V,\2\u0215\u0219\5X-\2\u0216\u0219")
        buf.write("\5b\62\2\u0217\u0219\5^\60\2\u0218\u020d\3\2\2\2\u0218")
        buf.write("\u020e\3\2\2\2\u0218\u020f\3\2\2\2\u0218\u0210\3\2\2\2")
        buf.write("\u0218\u0211\3\2\2\2\u0218\u0212\3\2\2\2\u0218\u0213\3")
        buf.write("\2\2\2\u0218\u0214\3\2\2\2\u0218\u0215\3\2\2\2\u0218\u0216")
        buf.write("\3\2\2\2\u0218\u0217\3\2\2\2\u0219[\3\2\2\2\u021a\u021c")
        buf.write("\5Z.\2\u021b\u021a\3\2\2\2\u021c\u021f\3\2\2\2\u021d\u021b")
        buf.write("\3\2\2\2\u021d\u021e\3\2\2\2\u021e]\3\2\2\2\u021f\u021d")
        buf.write("\3\2\2\2\u0220\u0224\5f\64\2\u0221\u0224\5h\65\2\u0222")
        buf.write("\u0224\5d\63\2\u0223\u0220\3\2\2\2\u0223\u0221\3\2\2\2")
        buf.write("\u0223\u0222\3\2\2\2\u0224_\3\2\2\2\u0225\u0226\7\24\2")
        buf.write("\2\u0226\u0227\5D#\2\u0227\u022c\7\64\2\2\u0228\u022b")
        buf.write("\5F$\2\u0229\u022b\5b\62\2\u022a\u0228\3\2\2\2\u022a\u0229")
        buf.write("\3\2\2\2\u022b\u022e\3\2\2\2\u022c\u022a\3\2\2\2\u022c")
        buf.write("\u022d\3\2\2\2\u022d\u022f\3\2\2\2\u022e\u022c\3\2\2\2")
        buf.write("\u022f\u0230\7\65\2\2\u0230a\3\2\2\2\u0231\u0233\7\34")
        buf.write("\2\2\u0232\u0231\3\2\2\2\u0232\u0233\3\2\2\2\u0233\u0234")
        buf.write("\3\2\2\2\u0234\u0235\7>\2\2\u0235\u0237\7\60\2\2\u0236")
        buf.write("\u0238\5j\66\2\u0237\u0236\3\2\2\2\u0237\u0238\3\2\2\2")
        buf.write("\u0238\u0239\3\2\2\2\u0239\u023a\7\61\2\2\u023a\u023b")
        buf.write("\5P)\2\u023bc\3\2\2\2\u023c\u023d\7\24\2\2\u023d\u0240")
        buf.write("\7>\2\2\u023e\u023f\7-\2\2\u023f\u0241\7>\2\2\u0240\u023e")
        buf.write("\3\2\2\2\u0240\u0241\3\2\2\2\u0241\u0242\3\2\2\2\u0242")
        buf.write("\u0243\7\64\2\2\u0243\u0244\5\\/\2\u0244\u0245\7\65\2")
        buf.write("\2\u0245e\3\2\2\2\u0246\u0247\7\27\2\2\u0247\u0249\7\60")
        buf.write("\2\2\u0248\u024a\5j\66\2\u0249\u0248\3\2\2\2\u0249\u024a")
        buf.write("\3\2\2\2\u024a\u024b\3\2\2\2\u024b\u024c\7\61\2\2\u024c")
        buf.write("\u024d\5P)\2\u024dg\3\2\2\2\u024e\u024f\7\30\2\2\u024f")
        buf.write("\u0250\7\61\2\2\u0250\u0251\7\60\2\2\u0251\u0252\5P)\2")
        buf.write("\u0252i\3\2\2\2\u0253\u0258\5l\67\2\u0254\u0255\7\66\2")
        buf.write("\2\u0255\u0257\5l\67\2\u0256\u0254\3\2\2\2\u0257\u025a")
        buf.write("\3\2\2\2\u0258\u0256\3\2\2\2\u0258\u0259\3\2\2\2\u0259")
        buf.write("k\3\2\2\2\u025a\u0258\3\2\2\2\u025b\u025c\5D#\2\u025c")
        buf.write("\u025d\7-\2\2\u025d\u025e\5@!\2\u025em\3\2\2\2\u025f\u0260")
        buf.write("\7\f\2\2\u0260\u0269\7\60\2\2\u0261\u0266\5p9\2\u0262")
        buf.write("\u0263\7\67\2\2\u0263\u0265\5p9\2\u0264\u0262\3\2\2\2")
        buf.write("\u0265\u0268\3\2\2\2\u0266\u0264\3\2\2\2\u0266\u0267\3")
        buf.write("\2\2\2\u0267\u026a\3\2\2\2\u0268\u0266\3\2\2\2\u0269\u0261")
        buf.write("\3\2\2\2\u0269\u026a\3\2\2\2\u026a\u026b\3\2\2\2\u026b")
        buf.write("\u026c\7\61\2\2\u026co\3\2\2\2\u026d\u0273\7:\2\2\u026e")
        buf.write("\u0273\7;\2\2\u026f\u0273\7<\2\2\u0270\u0273\7=\2\2\u0271")
        buf.write("\u0273\5n8\2\u0272\u026d\3\2\2\2\u0272\u026e\3\2\2\2\u0272")
        buf.write("\u026f\3\2\2\2\u0272\u0270\3\2\2\2\u0272\u0271\3\2\2\2")
        buf.write("\u0273q\3\2\2\2@u\u0083\u008e\u009b\u00a2\u00a5\u00a8")
        buf.write("\u00b1\u00b8\u00bb\u00c4\u00d1\u00d8\u00e5\u00e8\u00ec")
        buf.write("\u00f0\u0103\u0105\u0109\u0113\u011d\u0128\u013b\u0146")
        buf.write("\u015c\u0160\u0165\u016a\u0176\u017a\u0189\u0190\u0193")
        buf.write("\u019a\u01a4\u01a9\u01ae\u01b2\u01b9\u01bf\u01cd\u01d7")
        buf.write("\u01dc\u01e3\u01e6\u01f1\u01fd\u0206\u0218\u021d\u0223")
        buf.write("\u022a\u022c\u0232\u0237\u0240\u0249\u0258\u0266\u0269")
        buf.write("\u0272")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'..'", "'Break'", "'Continue'", "'If'", 
                     "'Elseif'", "'Else'", "'Foreach'", "'True'", "'False'", 
                     "'Array'", "'In'", "'Int'", "'Float'", "'Boolean'", 
                     "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
                     "'Var'", "'Constructor'", "'Destructor'", "'New'", 
                     "'By'", "'Self'", "'$'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'=='", "'!='", "'>'", "'>='", "'<'", "'<='", 
                     "'+.'", "'==.'", "'!'", "'&&'", "'||'", "':'", "'='", 
                     "'::'", "'('", "')'", "'['", "']'", "'{'", "'}'", "';'", 
                     "','", "'.'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "BREAK", "CONTINUE", "IF", 
                      "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", "ARRAY", 
                      "IN", "INT", "FLOAT", "BOOLEAN", "STRING", "RETURN", 
                      "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", "DESTRUCTOR", 
                      "NEW", "BY", "SELF", "STATIC", "ADD", "SUB", "MUL", 
                      "DIV", "MOD", "EQ", "NEQ", "GT", "GTE", "LT", "LTE", 
                      "SADD", "SEQ", "NOT", "AND", "OR", "COLON", "ASSIGN", 
                      "SCOPE", "LB", "RB", "LSB", "RSB", "LCB", "RCB", "SM", 
                      "CM", "DOT", "BLOCK_COMMENT", "INTLIT", "FLOATLIT", 
                      "BOOLLIT", "STRLIT", "ID", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE" ]

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
    RULE_lit_Array = 54
    RULE_lit_Data = 55

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
                   "lit_Array", "lit_Data" ]

    EOF = Token.EOF
    T__0=1
    BREAK=2
    CONTINUE=3
    IF=4
    ELSEIF=5
    ELSE=6
    FOREACH=7
    TRUE=8
    FALSE=9
    ARRAY=10
    IN=11
    INT=12
    FLOAT=13
    BOOLEAN=14
    STRING=15
    RETURN=16
    NULL=17
    CLASS=18
    VAL=19
    VAR=20
    CONSTRUCTOR=21
    DESTRUCTOR=22
    NEW=23
    BY=24
    SELF=25
    STATIC=26
    ADD=27
    SUB=28
    MUL=29
    DIV=30
    MOD=31
    EQ=32
    NEQ=33
    GT=34
    GTE=35
    LT=36
    LTE=37
    SADD=38
    SEQ=39
    NOT=40
    AND=41
    OR=42
    COLON=43
    ASSIGN=44
    SCOPE=45
    LB=46
    RB=47
    LSB=48
    RSB=49
    LCB=50
    RCB=51
    SM=52
    CM=53
    DOT=54
    BLOCK_COMMENT=55
    INTLIT=56
    FLOATLIT=57
    BOOLLIT=58
    STRLIT=59
    ID=60
    WS=61
    ERROR_CHAR=62
    UNCLOSE_STRING=63
    ILLEGAL_ESCAPE=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_0(self):
            return self.getTypedRuleContext(D96Parser.Exp_0Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp_IntFloat

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_IntFloat" ):
                return visitor.visitExp_IntFloat(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_0" ):
                return visitor.visitExp_0(self)
            else:
                return visitor.visitChildren(self)



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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_1" ):
                return visitor.visitExp_1(self)
            else:
                return visitor.visitChildren(self)



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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_2" ):
                return visitor.visitExp_2(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_Bool" ):
                return visitor.visitExp_Bool(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_TermBool" ):
                return visitor.visitExp_TermBool(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_Str" ):
                return visitor.visitExp_Str(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_TermStr" ):
                return visitor.visitExp_TermStr(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_EqualAndNotEqual" ):
                return visitor.visitExp_EqualAndNotEqual(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_TermEQANEQ" ):
                return visitor.visitExp_TermEQANEQ(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_LessLargeEqual" ):
                return visitor.visitExp_LessLargeEqual(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_TermLRE" ):
                return visitor.visitExp_TermLRE(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_EqualAndNotEqual(self):
            return self.getTypedRuleContext(D96Parser.Exp_EqualAndNotEqualContext,0)


        def exp_LessLargeEqual(self):
            return self.getTypedRuleContext(D96Parser.Exp_LessLargeEqualContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp_RelationalOperation

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_RelationalOperation" ):
                return visitor.visitExp_RelationalOperation(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_Idx" ):
                return visitor.visitExp_Idx(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_TermIdx" ):
                return visitor.visitExp_TermIdx(self)
            else:
                return visitor.visitChildren(self)



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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdx_Operators" ):
                return visitor.visitIdx_Operators(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_InstanceAttributeAccess" ):
                return visitor.visitExp_InstanceAttributeAccess(self)
            else:
                return visitor.visitChildren(self)



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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_InstanceAttributeAccessTerm" ):
                return visitor.visitExp_InstanceAttributeAccessTerm(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_StaticAttributeAccess" ):
                return visitor.visitExp_StaticAttributeAccess(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_InstanceMethodInvocation" ):
                return visitor.visitExp_InstanceMethodInvocation(self)
            else:
                return visitor.visitChildren(self)



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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_InstanceMethodInvocationTerm" ):
                return visitor.visitExp_InstanceMethodInvocationTerm(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_StaticMethodInvocation" ):
                return visitor.visitExp_StaticMethodInvocation(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_InstanceAttributeMethod" ):
                return visitor.visitExp_InstanceAttributeMethod(self)
            else:
                return visitor.visitChildren(self)



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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_InstanceAttributeAccess(self):
            return self.getTypedRuleContext(D96Parser.Exp_InstanceAttributeAccessContext,0)


        def exp_InstanceMethodInvocation(self):
            return self.getTypedRuleContext(D96Parser.Exp_InstanceMethodInvocationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp_InstanceAttributeMethodTerm

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_InstanceAttributeMethodTerm" ):
                return visitor.visitExp_InstanceAttributeMethodTerm(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_MemberAccess" ):
                return visitor.visitExp_MemberAccess(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_ObjCreation" ):
                return visitor.visitExp_ObjCreation(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def exp_ObjCreation(self):
            return self.getTypedRuleContext(D96Parser.Exp_ObjCreationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp_ClassObject

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_ClassObject" ):
                return visitor.visitExp_ClassObject(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp_Method" ):
                return visitor.visitExp_Method(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

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


        def lit_Data(self):
            return self.getTypedRuleContext(D96Parser.Lit_DataContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




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
                self.lit_Data()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_ExprContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_Expr" ):
                return visitor.visitList_Expr(self)
            else:
                return visitor.visitChildren(self)




    def list_Expr(self):

        localctx = D96Parser.List_ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_list_Expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.STATIC) | (1 << D96Parser.NOT) | (1 << D96Parser.LB) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLLIT) | (1 << D96Parser.STRLIT) | (1 << D96Parser.ID))) != 0):
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitType_Data" ):
                return visitor.visitType_Data(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArray_Type" ):
                return visitor.visitArray_Type(self)
            else:
                return visitor.visitChildren(self)




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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.ID)
            else:
                return self.getToken(D96Parser.ID, i)

        def STATIC(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.STATIC)
            else:
                return self.getToken(D96Parser.STATIC, i)

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_seq_ID

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeq_ID" ):
                return visitor.visitSeq_ID(self)
            else:
                return visitor.visitChildren(self)




    def seq_ID(self):

        localctx = D96Parser.Seq_IDContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_seq_ID)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 418
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.STATIC:
                self.state = 417
                self.match(D96Parser.STATIC)


            self.state = 420
            self.match(D96Parser.ID)
            self.state = 428
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 421
                self.match(D96Parser.CM)
                self.state = 423
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.STATIC:
                    self.state = 422
                    self.match(D96Parser.STATIC)


                self.state = 425
                self.match(D96Parser.ID)
                self.state = 430
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_VarDeclaration" ):
                return visitor.visitStmt_VarDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def stmt_VarDeclaration(self):

        localctx = D96Parser.Stmt_VarDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_stmt_VarDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 432
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.VAL or _la==D96Parser.VAR:
                self.state = 431
                _la = self._input.LA(1)
                if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 434
            self.seq_ID()
            self.state = 435
            self.match(D96Parser.COLON)
            self.state = 436
            self.type_Data()
            self.state = 439
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN:
                self.state = 437
                self.match(D96Parser.ASSIGN)
                self.state = 438
                self.list_Expr()


            self.state = 441
            self.match(D96Parser.SM)
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
            return self.getToken(D96Parser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = D96Parser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_lhs)
        try:
            self.state = 445
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 443
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 444
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_Assign" ):
                return visitor.visitStmt_Assign(self)
            else:
                return visitor.visitChildren(self)




    def stmt_Assign(self):

        localctx = D96Parser.Stmt_AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_stmt_Assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 447
            self.lhs()
            self.state = 448
            self.match(D96Parser.ASSIGN)
            self.state = 449
            self.expr()
            self.state = 450
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_IfContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_If" ):
                return visitor.visitStmt_If(self)
            else:
                return visitor.visitChildren(self)




    def stmt_If(self):

        localctx = D96Parser.Stmt_IfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_stmt_If)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 452
            self.match(D96Parser.IF)
            self.state = 453
            self.match(D96Parser.LB)
            self.state = 454
            self.expr()
            self.state = 455
            self.match(D96Parser.RB)
            self.state = 459
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 456
                    self.stmt_Block() 
                self.state = 461
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

            self.state = 474
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 462
                self.match(D96Parser.ELSEIF)
                self.state = 463
                self.match(D96Parser.LB)
                self.state = 464
                self.expr()
                self.state = 465
                self.match(D96Parser.RB)
                self.state = 469
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 466
                        self.stmt_Block() 
                    self.state = 471
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

                self.state = 476
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 484
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 477
                self.match(D96Parser.ELSE)
                self.state = 481
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 478
                        self.stmt_Block() 
                    self.state = 483
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,44,self._ctx)



        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_ForInContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_ForIn" ):
                return visitor.visitStmt_ForIn(self)
            else:
                return visitor.visitChildren(self)




    def stmt_ForIn(self):

        localctx = D96Parser.Stmt_ForInContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_stmt_ForIn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 486
            self.match(D96Parser.FOREACH)
            self.state = 487
            self.match(D96Parser.LB)
            self.state = 488
            self.match(D96Parser.ID)
            self.state = 489
            self.match(D96Parser.IN)
            self.state = 490
            self.expr()
            self.state = 491
            self.match(D96Parser.T__0)
            self.state = 492
            self.expr()
            self.state = 495
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 493
                self.match(D96Parser.BY)
                self.state = 494
                self.expr()


            self.state = 497
            self.match(D96Parser.RB)
            self.state = 498
            self.stmt_Block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_BlockContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_Block" ):
                return visitor.visitStmt_Block(self)
            else:
                return visitor.visitChildren(self)




    def stmt_Block(self):

        localctx = D96Parser.Stmt_BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_stmt_Block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 500
            self.match(D96Parser.LCB)

            self.state = 501
            self.list_Stmt()
            self.state = 502
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_MethodInvocationContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_MethodInvocation" ):
                return visitor.visitStmt_MethodInvocation(self)
            else:
                return visitor.visitChildren(self)




    def stmt_MethodInvocation(self):

        localctx = D96Parser.Stmt_MethodInvocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_stmt_MethodInvocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 507
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.state = 504
                self.exp_InstanceMethodInvocation(0)
                pass

            elif la_ == 2:
                self.state = 505
                self.exp_StaticMethodInvocation()
                pass

            elif la_ == 3:
                self.state = 506
                self.exp_Method()
                pass


            self.state = 509
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_ContinueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(D96Parser.CONTINUE, 0)

        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stmt_Continue

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_Continue" ):
                return visitor.visitStmt_Continue(self)
            else:
                return visitor.visitChildren(self)




    def stmt_Continue(self):

        localctx = D96Parser.Stmt_ContinueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_stmt_Continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 511
            self.match(D96Parser.CONTINUE)
            self.state = 512
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_ReturnContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_Return" ):
                return visitor.visitStmt_Return(self)
            else:
                return visitor.visitChildren(self)




    def stmt_Return(self):

        localctx = D96Parser.Stmt_ReturnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_stmt_Return)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 514
            self.match(D96Parser.RETURN)
            self.state = 516
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.STATIC) | (1 << D96Parser.NOT) | (1 << D96Parser.LB) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLLIT) | (1 << D96Parser.STRLIT) | (1 << D96Parser.ID))) != 0):
                self.state = 515
                self.expr()


            self.state = 518
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_BreakContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(D96Parser.BREAK, 0)

        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stmt_Break

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_Break" ):
                return visitor.visitStmt_Break(self)
            else:
                return visitor.visitChildren(self)




    def stmt_Break(self):

        localctx = D96Parser.Stmt_BreakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_stmt_Break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 520
            self.match(D96Parser.BREAK)
            self.state = 521
            self.match(D96Parser.SM)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt" ):
                return visitor.visitStmt(self)
            else:
                return visitor.visitChildren(self)




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_stmt)
        try:
            self.state = 534
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 523
                self.stmt_VarDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 524
                self.stmt_Assign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 525
                self.stmt_If()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 526
                self.stmt_ForIn()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 527
                self.stmt_Block()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 528
                self.stmt_MethodInvocation()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 529
                self.stmt_Continue()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 530
                self.stmt_Return()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 531
                self.stmt_Break()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 532
                self.stmt_MethodDeclaration()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 533
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_Stmt" ):
                return visitor.visitList_Stmt(self)
            else:
                return visitor.visitChildren(self)




    def list_Stmt(self):

        localctx = D96Parser.List_StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_list_Stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 539
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.ARRAY) | (1 << D96Parser.RETURN) | (1 << D96Parser.CLASS) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.STATIC) | (1 << D96Parser.NOT) | (1 << D96Parser.LB) | (1 << D96Parser.LCB) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLLIT) | (1 << D96Parser.STRLIT) | (1 << D96Parser.ID))) != 0):
                self.state = 536
                self.stmt()
                self.state = 541
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_Class" ):
                return visitor.visitStmt_Class(self)
            else:
                return visitor.visitChildren(self)




    def stmt_Class(self):

        localctx = D96Parser.Stmt_ClassContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_stmt_Class)
        try:
            self.state = 545
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 542
                self.class_Construction()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 543
                self.class_Destruction()
                pass
            elif token in [D96Parser.CLASS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 544
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
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASS(self):
            return self.getToken(D96Parser.CLASS, 0)

        def seq_ID(self):
            return self.getTypedRuleContext(D96Parser.Seq_IDContext,0)


        def LCB(self):
            return self.getToken(D96Parser.LCB, 0)

        def RCB(self):
            return self.getToken(D96Parser.RCB, 0)

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_ClassDeclaration" ):
                return visitor.visitStmt_ClassDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def stmt_ClassDeclaration(self):

        localctx = D96Parser.Stmt_ClassDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_stmt_ClassDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 547
            self.match(D96Parser.CLASS)
            self.state = 548
            self.seq_ID()
            self.state = 549
            self.match(D96Parser.LCB)
            self.state = 554
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.STATIC) | (1 << D96Parser.ID))) != 0):
                self.state = 552
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,52,self._ctx)
                if la_ == 1:
                    self.state = 550
                    self.stmt_VarDeclaration()
                    pass

                elif la_ == 2:
                    self.state = 551
                    self.stmt_MethodDeclaration()
                    pass


                self.state = 556
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 557
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_MethodDeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStmt_MethodDeclaration" ):
                return visitor.visitStmt_MethodDeclaration(self)
            else:
                return visitor.visitChildren(self)




    def stmt_MethodDeclaration(self):

        localctx = D96Parser.Stmt_MethodDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_stmt_MethodDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 560
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.STATIC:
                self.state = 559
                self.match(D96Parser.STATIC)


            self.state = 562
            self.match(D96Parser.ID)
            self.state = 563
            self.match(D96Parser.LB)
            self.state = 565
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.STATIC or _la==D96Parser.ID:
                self.state = 564
                self.list_Parameters()


            self.state = 567
            self.match(D96Parser.RB)
            self.state = 568
            self.stmt_Block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_DeclarationContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_Declaration" ):
                return visitor.visitClass_Declaration(self)
            else:
                return visitor.visitChildren(self)




    def class_Declaration(self):

        localctx = D96Parser.Class_DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_class_Declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 570
            self.match(D96Parser.CLASS)
            self.state = 571
            self.match(D96Parser.ID)
            self.state = 574
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 572
                self.match(D96Parser.COLON)
                self.state = 573
                self.match(D96Parser.ID)


            self.state = 576
            self.match(D96Parser.LCB)
            self.state = 577
            self.list_Stmt()
            self.state = 578
            self.match(D96Parser.RCB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_ConstructionContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_Construction" ):
                return visitor.visitClass_Construction(self)
            else:
                return visitor.visitChildren(self)




    def class_Construction(self):

        localctx = D96Parser.Class_ConstructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_class_Construction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 580
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 581
            self.match(D96Parser.LB)
            self.state = 583
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.STATIC or _la==D96Parser.ID:
                self.state = 582
                self.list_Parameters()


            self.state = 585
            self.match(D96Parser.RB)
            self.state = 586
            self.stmt_Block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Class_DestructionContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClass_Destruction" ):
                return visitor.visitClass_Destruction(self)
            else:
                return visitor.visitChildren(self)




    def class_Destruction(self):

        localctx = D96Parser.Class_DestructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 102, self.RULE_class_Destruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 588
            self.match(D96Parser.DESTRUCTOR)
            self.state = 589
            self.match(D96Parser.RB)
            self.state = 590
            self.match(D96Parser.LB)
            self.state = 591
            self.stmt_Block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_Parameters" ):
                return visitor.visitList_Parameters(self)
            else:
                return visitor.visitChildren(self)




    def list_Parameters(self):

        localctx = D96Parser.List_ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_list_Parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 593
            self.seq_Parameters()
            self.state = 598
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SM:
                self.state = 594
                self.match(D96Parser.SM)
                self.state = 595
                self.seq_Parameters()
                self.state = 600
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
        __slots__ = 'parser'

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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSeq_Parameters" ):
                return visitor.visitSeq_Parameters(self)
            else:
                return visitor.visitChildren(self)




    def seq_Parameters(self):

        localctx = D96Parser.Seq_ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_seq_Parameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 601
            self.seq_ID()
            self.state = 602
            self.match(D96Parser.COLON)
            self.state = 603
            self.type_Data()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lit_ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ARRAY(self):
            return self.getToken(D96Parser.ARRAY, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def lit_Data(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Lit_DataContext)
            else:
                return self.getTypedRuleContext(D96Parser.Lit_DataContext,i)


        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def getRuleIndex(self):
            return D96Parser.RULE_lit_Array

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLit_Array" ):
                return visitor.visitLit_Array(self)
            else:
                return visitor.visitChildren(self)




    def lit_Array(self):

        localctx = D96Parser.Lit_ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_lit_Array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 605
            self.match(D96Parser.ARRAY)
            self.state = 606
            self.match(D96Parser.LB)
            self.state = 615
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.ARRAY) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLLIT) | (1 << D96Parser.STRLIT))) != 0):
                self.state = 607
                self.lit_Data()
                self.state = 612
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.CM:
                    self.state = 608
                    self.match(D96Parser.CM)
                    self.state = 609
                    self.lit_Data()
                    self.state = 614
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 617
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lit_DataContext(ParserRuleContext):
        __slots__ = 'parser'

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

        def lit_Array(self):
            return self.getTypedRuleContext(D96Parser.Lit_ArrayContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_lit_Data

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLit_Data" ):
                return visitor.visitLit_Data(self)
            else:
                return visitor.visitChildren(self)




    def lit_Data(self):

        localctx = D96Parser.Lit_DataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 110, self.RULE_lit_Data)
        try:
            self.state = 624
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 619
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 620
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.BOOLLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 621
                self.match(D96Parser.BOOLLIT)
                pass
            elif token in [D96Parser.STRLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 622
                self.match(D96Parser.STRLIT)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 623
                self.lit_Array()
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
         




