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
        buf.write("\u0260\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\3\2\3\2\3\2\3\3\3")
        buf.write("\3\3\4\3\4\3\4\3\4\3\4\3\4\7\4|\n\4\f\4\16\4\177\13\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\7\5\u0087\n\5\f\5\16\5\u008a")
        buf.write("\13\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\5\6\u0096")
        buf.write("\n\6\3\7\3\7\3\7\3\7\3\7\5\7\u009d\n\7\3\7\5\7\u00a0\n")
        buf.write("\7\3\b\5\b\u00a3\n\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\5\b\u00ac")
        buf.write("\n\b\3\t\3\t\3\t\3\t\3\t\5\t\u00b3\n\t\3\n\5\n\u00b6\n")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n\u00bf\n\n\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\5\f\u00cc\n\f\3")
        buf.write("\f\3\f\3\f\3\f\3\f\5\f\u00d3\n\f\3\r\3\r\3\r\3\r\3\16")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\5\16\u00e0\n\16\3\16\5")
        buf.write("\16\u00e3\n\16\3\17\3\17\5\17\u00e7\n\17\3\20\3\20\5\20")
        buf.write("\u00eb\n\20\3\20\3\20\3\21\3\21\3\21\3\21\3\21\3\21\3")
        buf.write("\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\3\21\7\21\u00fe")
        buf.write("\n\21\f\21\16\21\u0101\13\21\3\22\5\22\u0104\n\22\3\22")
        buf.write("\3\22\3\22\3\22\3\22\3\22\3\22\3\22\5\22\u010e\n\22\3")
        buf.write("\23\3\23\3\23\3\23\3\23\3\23\7\23\u0116\n\23\f\23\16\23")
        buf.write("\u0119\13\23\3\24\3\24\3\24\3\24\3\24\3\24\3\24\3\24\5")
        buf.write("\24\u0123\n\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\7\26\u0134\n\26\f")
        buf.write("\26\16\26\u0137\13\26\3\27\3\27\3\27\3\27\3\27\3\27\3")
        buf.write("\27\3\27\5\27\u0141\n\27\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\5\31\u0157\n\31\7\31\u0159\n\31\f\31\16")
        buf.write("\31\u015c\13\31\3\32\3\32\5\32\u0160\n\32\3\33\3\33\3")
        buf.write("\33\5\33\u0165\n\33\3\34\3\34\3\34\3\34\3\34\3\34\3\34")
        buf.write("\3\34\3\34\3\34\5\34\u0171\n\34\3\35\3\35\5\35\u0175\n")
        buf.write("\35\3\36\3\36\3\36\3\36\3\36\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\3\37\3\37\5\37\u0184\n\37\3 \3 \3 \7 \u0189\n \f")
        buf.write(" \16 \u018c\13 \5 \u018e\n \3!\3!\3!\3!\3!\5!\u0195\n")
        buf.write("!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\7#\u01a1\n#\f#")
        buf.write("\16#\u01a4\13#\3$\5$\u01a7\n$\3$\5$\u01aa\n$\3$\3$\3$")
        buf.write("\3$\3$\5$\u01b1\n$\3$\3$\3%\3%\5%\u01b7\n%\3&\3&\3&\3")
        buf.write("&\3&\3\'\3\'\3\'\3\'\3\'\7\'\u01c3\n\'\f\'\16\'\u01c6")
        buf.write("\13\'\3\'\3\'\3\'\3\'\3\'\7\'\u01cd\n\'\f\'\16\'\u01d0")
        buf.write("\13\'\7\'\u01d2\n\'\f\'\16\'\u01d5\13\'\3\'\3\'\7\'\u01d9")
        buf.write("\n\'\f\'\16\'\u01dc\13\'\5\'\u01de\n\'\3(\3(\3(\3(\3(")
        buf.write("\3(\3(\3(\3(\5(\u01e9\n(\3(\3(\3(\3)\3)\3)\3)\3*\3*\3")
        buf.write("*\5*\u01f5\n*\3*\3*\3+\3+\3+\3,\3,\5,\u01fe\n,\3,\3,\3")
        buf.write("-\3-\3-\3.\5.\u0206\n.\3.\3.\3.\5.\u020b\n.\3.\3.\3.\3")
        buf.write("/\3/\3/\3/\3/\3/\3/\3/\3/\3/\3/\5/\u021b\n/\3\60\7\60")
        buf.write("\u021e\n\60\f\60\16\60\u0221\13\60\3\61\3\61\3\61\5\61")
        buf.write("\u0226\n\61\3\62\3\62\3\62\3\62\5\62\u022c\n\62\3\62\3")
        buf.write("\62\3\62\3\62\3\63\3\63\3\63\5\63\u0235\n\63\3\63\3\63")
        buf.write("\3\63\3\64\3\64\3\64\3\64\3\64\3\65\3\65\3\65\7\65\u0242")
        buf.write("\n\65\f\65\16\65\u0245\13\65\3\66\3\66\3\66\3\66\3\67")
        buf.write("\3\67\3\67\3\67\3\67\7\67\u0250\n\67\f\67\16\67\u0253")
        buf.write("\13\67\5\67\u0255\n\67\3\67\3\67\38\38\38\38\38\58\u025e")
        buf.write("\n8\38\2\b\6\b $*\609\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bdfh")
        buf.write("jln\2\t\3\2\"#\3\2$&\3\2\60\61\3\2-.\3\2\'(\3\2),\3\2")
        buf.write("\32\33\2\u0291\2p\3\2\2\2\4s\3\2\2\2\6u\3\2\2\2\b\u0080")
        buf.write("\3\2\2\2\n\u0095\3\2\2\2\f\u009f\3\2\2\2\16\u00ab\3\2")
        buf.write("\2\2\20\u00b2\3\2\2\2\22\u00be\3\2\2\2\24\u00c0\3\2\2")
        buf.write("\2\26\u00d2\3\2\2\2\30\u00d4\3\2\2\2\32\u00e2\3\2\2\2")
        buf.write("\34\u00e6\3\2\2\2\36\u00ea\3\2\2\2 \u00ee\3\2\2\2\"\u010d")
        buf.write("\3\2\2\2$\u010f\3\2\2\2&\u0122\3\2\2\2(\u0124\3\2\2\2")
        buf.write("*\u0129\3\2\2\2,\u0140\3\2\2\2.\u0142\3\2\2\2\60\u014a")
        buf.write("\3\2\2\2\62\u015f\3\2\2\2\64\u0164\3\2\2\2\66\u0170\3")
        buf.write("\2\2\28\u0174\3\2\2\2:\u0176\3\2\2\2<\u0183\3\2\2\2>\u018d")
        buf.write("\3\2\2\2@\u0194\3\2\2\2B\u0196\3\2\2\2D\u019d\3\2\2\2")
        buf.write("F\u01a6\3\2\2\2H\u01b6\3\2\2\2J\u01b8\3\2\2\2L\u01bd\3")
        buf.write("\2\2\2N\u01df\3\2\2\2P\u01ed\3\2\2\2R\u01f4\3\2\2\2T\u01f8")
        buf.write("\3\2\2\2V\u01fb\3\2\2\2X\u0201\3\2\2\2Z\u0205\3\2\2\2")
        buf.write("\\\u021a\3\2\2\2^\u021f\3\2\2\2`\u0225\3\2\2\2b\u0227")
        buf.write("\3\2\2\2d\u0231\3\2\2\2f\u0239\3\2\2\2h\u023e\3\2\2\2")
        buf.write("j\u0246\3\2\2\2l\u024a\3\2\2\2n\u025d\3\2\2\2pq\5^\60")
        buf.write("\2qr\7\2\2\3r\3\3\2\2\2st\5\6\4\2t\5\3\2\2\2uv\b\4\1\2")
        buf.write("vw\5\b\5\2w}\3\2\2\2xy\f\4\2\2yz\t\2\2\2z|\5\b\5\2{x\3")
        buf.write("\2\2\2|\177\3\2\2\2}{\3\2\2\2}~\3\2\2\2~\7\3\2\2\2\177")
        buf.write("}\3\2\2\2\u0080\u0081\b\5\1\2\u0081\u0082\5\n\6\2\u0082")
        buf.write("\u0088\3\2\2\2\u0083\u0084\f\4\2\2\u0084\u0085\t\3\2\2")
        buf.write("\u0085\u0087\5\n\6\2\u0086\u0083\3\2\2\2\u0087\u008a\3")
        buf.write("\2\2\2\u0088\u0086\3\2\2\2\u0088\u0089\3\2\2\2\u0089\t")
        buf.write("\3\2\2\2\u008a\u0088\3\2\2\2\u008b\u0096\7>\2\2\u008c")
        buf.write("\u0096\7\5\2\2\u008d\u0096\7\6\2\2\u008e\u0096\5\64\33")
        buf.write("\2\u008f\u0096\5:\36\2\u0090\u0096\5\36\20\2\u0091\u0092")
        buf.write("\7\65\2\2\u0092\u0093\5\6\4\2\u0093\u0094\7\66\2\2\u0094")
        buf.write("\u0096\3\2\2\2\u0095\u008b\3\2\2\2\u0095\u008c\3\2\2\2")
        buf.write("\u0095\u008d\3\2\2\2\u0095\u008e\3\2\2\2\u0095\u008f\3")
        buf.write("\2\2\2\u0095\u0090\3\2\2\2\u0095\u0091\3\2\2\2\u0096\13")
        buf.write("\3\2\2\2\u0097\u0098\5\16\b\2\u0098\u0099\t\4\2\2\u0099")
        buf.write("\u009a\5\f\7\2\u009a\u00a0\3\2\2\2\u009b\u009d\7/\2\2")
        buf.write("\u009c\u009b\3\2\2\2\u009c\u009d\3\2\2\2\u009d\u009e\3")
        buf.write("\2\2\2\u009e\u00a0\5\16\b\2\u009f\u0097\3\2\2\2\u009f")
        buf.write("\u009c\3\2\2\2\u00a0\r\3\2\2\2\u00a1\u00a3\7!\2\2\u00a2")
        buf.write("\u00a1\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4\3\2\2\2")
        buf.write("\u00a4\u00ac\7>\2\2\u00a5\u00ac\7\7\2\2\u00a6\u00ac\5")
        buf.write("\64\33\2\u00a7\u00a8\7\65\2\2\u00a8\u00a9\5\f\7\2\u00a9")
        buf.write("\u00aa\7\66\2\2\u00aa\u00ac\3\2\2\2\u00ab\u00a2\3\2\2")
        buf.write("\2\u00ab\u00a5\3\2\2\2\u00ab\u00a6\3\2\2\2\u00ab\u00a7")
        buf.write("\3\2\2\2\u00ac\17\3\2\2\2\u00ad\u00ae\5\22\n\2\u00ae\u00af")
        buf.write("\t\5\2\2\u00af\u00b0\5\20\t\2\u00b0\u00b3\3\2\2\2\u00b1")
        buf.write("\u00b3\5\22\n\2\u00b2\u00ad\3\2\2\2\u00b2\u00b1\3\2\2")
        buf.write("\2\u00b3\21\3\2\2\2\u00b4\u00b6\7!\2\2\u00b5\u00b4\3\2")
        buf.write("\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\u00bf")
        buf.write("\7>\2\2\u00b8\u00bf\7\b\2\2\u00b9\u00bf\5\64\33\2\u00ba")
        buf.write("\u00bb\7\65\2\2\u00bb\u00bc\5\20\t\2\u00bc\u00bd\7\66")
        buf.write("\2\2\u00bd\u00bf\3\2\2\2\u00be\u00b5\3\2\2\2\u00be\u00b8")
        buf.write("\3\2\2\2\u00be\u00b9\3\2\2\2\u00be\u00ba\3\2\2\2\u00bf")
        buf.write("\23\3\2\2\2\u00c0\u00c1\5\26\f\2\u00c1\u00c2\t\6\2\2\u00c2")
        buf.write("\u00c3\5\26\f\2\u00c3\25\3\2\2\2\u00c4\u00c5\7\65\2\2")
        buf.write("\u00c5\u00c6\5<\37\2\u00c6\u00c7\7\66\2\2\u00c7\u00d3")
        buf.write("\3\2\2\2\u00c8\u00d3\7\5\2\2\u00c9\u00d3\7\7\2\2\u00ca")
        buf.write("\u00cc\7!\2\2\u00cb\u00ca\3\2\2\2\u00cb\u00cc\3\2\2\2")
        buf.write("\u00cc\u00cd\3\2\2\2\u00cd\u00d3\7>\2\2\u00ce\u00cf\7")
        buf.write("\65\2\2\u00cf\u00d0\5\24\13\2\u00d0\u00d1\7\66\2\2\u00d1")
        buf.write("\u00d3\3\2\2\2\u00d2\u00c4\3\2\2\2\u00d2\u00c8\3\2\2\2")
        buf.write("\u00d2\u00c9\3\2\2\2\u00d2\u00cb\3\2\2\2\u00d2\u00ce\3")
        buf.write("\2\2\2\u00d3\27\3\2\2\2\u00d4\u00d5\5\32\16\2\u00d5\u00d6")
        buf.write("\t\7\2\2\u00d6\u00d7\5\32\16\2\u00d7\31\3\2\2\2\u00d8")
        buf.write("\u00d9\7\65\2\2\u00d9\u00da\5<\37\2\u00da\u00db\7\66\2")
        buf.write("\2\u00db\u00e3\3\2\2\2\u00dc\u00e3\7\5\2\2\u00dd\u00e3")
        buf.write("\7\6\2\2\u00de\u00e0\7!\2\2\u00df\u00de\3\2\2\2\u00df")
        buf.write("\u00e0\3\2\2\2\u00e0\u00e1\3\2\2\2\u00e1\u00e3\7>\2\2")
        buf.write("\u00e2\u00d8\3\2\2\2\u00e2\u00dc\3\2\2\2\u00e2\u00dd\3")
        buf.write("\2\2\2\u00e2\u00df\3\2\2\2\u00e3\33\3\2\2\2\u00e4\u00e7")
        buf.write("\5\24\13\2\u00e5\u00e7\5\30\r\2\u00e6\u00e4\3\2\2\2\u00e6")
        buf.write("\u00e5\3\2\2\2\u00e7\35\3\2\2\2\u00e8\u00eb\5:\36\2\u00e9")
        buf.write("\u00eb\7>\2\2\u00ea\u00e8\3\2\2\2\u00ea\u00e9\3\2\2\2")
        buf.write("\u00eb\u00ec\3\2\2\2\u00ec\u00ed\5 \21\2\u00ed\37\3\2")
        buf.write("\2\2\u00ee\u00ef\b\21\1\2\u00ef\u00f0\7\67\2\2\u00f0\u00f1")
        buf.write("\5\"\22\2\u00f1\u00f2\78\2\2\u00f2\u00ff\3\2\2\2\u00f3")
        buf.write("\u00f4\f\4\2\2\u00f4\u00f5\7\67\2\2\u00f5\u00f6\5\"\22")
        buf.write("\2\u00f6\u00f7\78\2\2\u00f7\u00fe\3\2\2\2\u00f8\u00f9")
        buf.write("\f\3\2\2\u00f9\u00fa\7\67\2\2\u00fa\u00fb\5\36\20\2\u00fb")
        buf.write("\u00fc\78\2\2\u00fc\u00fe\3\2\2\2\u00fd\u00f3\3\2\2\2")
        buf.write("\u00fd\u00f8\3\2\2\2\u00fe\u0101\3\2\2\2\u00ff\u00fd\3")
        buf.write("\2\2\2\u00ff\u0100\3\2\2\2\u0100!\3\2\2\2\u0101\u00ff")
        buf.write("\3\2\2\2\u0102\u0104\7!\2\2\u0103\u0102\3\2\2\2\u0103")
        buf.write("\u0104\3\2\2\2\u0104\u0105\3\2\2\2\u0105\u010e\7>\2\2")
        buf.write("\u0106\u010e\7\5\2\2\u0107\u010e\5<\37\2\u0108\u010e\5")
        buf.write("\36\20\2\u0109\u010a\7\65\2\2\u010a\u010b\5\36\20\2\u010b")
        buf.write("\u010c\7\66\2\2\u010c\u010e\3\2\2\2\u010d\u0103\3\2\2")
        buf.write("\2\u010d\u0106\3\2\2\2\u010d\u0107\3\2\2\2\u010d\u0108")
        buf.write("\3\2\2\2\u010d\u0109\3\2\2\2\u010e#\3\2\2\2\u010f\u0110")
        buf.write("\b\23\1\2\u0110\u0111\5&\24\2\u0111\u0117\3\2\2\2\u0112")
        buf.write("\u0113\f\4\2\2\u0113\u0114\7=\2\2\u0114\u0116\7>\2\2\u0115")
        buf.write("\u0112\3\2\2\2\u0116\u0119\3\2\2\2\u0117\u0115\3\2\2\2")
        buf.write("\u0117\u0118\3\2\2\2\u0118%\3\2\2\2\u0119\u0117\3\2\2")
        buf.write("\2\u011a\u011b\7\65\2\2\u011b\u011c\58\35\2\u011c\u011d")
        buf.write("\7\66\2\2\u011d\u0123\3\2\2\2\u011e\u0123\7>\2\2\u011f")
        buf.write("\u0123\7 \2\2\u0120\u0123\5(\25\2\u0121\u0123\5.\30\2")
        buf.write("\u0122\u011a\3\2\2\2\u0122\u011e\3\2\2\2\u0122\u011f\3")
        buf.write("\2\2\2\u0122\u0120\3\2\2\2\u0122\u0121\3\2\2\2\u0123\'")
        buf.write("\3\2\2\2\u0124\u0125\7>\2\2\u0125\u0126\7\64\2\2\u0126")
        buf.write("\u0127\7!\2\2\u0127\u0128\7>\2\2\u0128)\3\2\2\2\u0129")
        buf.write("\u012a\b\26\1\2\u012a\u012b\5,\27\2\u012b\u0135\3\2\2")
        buf.write("\2\u012c\u012d\f\4\2\2\u012d\u012e\7=\2\2\u012e\u012f")
        buf.write("\7>\2\2\u012f\u0130\7\65\2\2\u0130\u0131\5> \2\u0131\u0132")
        buf.write("\7\66\2\2\u0132\u0134\3\2\2\2\u0133\u012c\3\2\2\2\u0134")
        buf.write("\u0137\3\2\2\2\u0135\u0133\3\2\2\2\u0135\u0136\3\2\2\2")
        buf.write("\u0136+\3\2\2\2\u0137\u0135\3\2\2\2\u0138\u0139\7\65\2")
        buf.write("\2\u0139\u013a\58\35\2\u013a\u013b\7\66\2\2\u013b\u0141")
        buf.write("\3\2\2\2\u013c\u0141\7>\2\2\u013d\u0141\7 \2\2\u013e\u0141")
        buf.write("\5(\25\2\u013f\u0141\5.\30\2\u0140\u0138\3\2\2\2\u0140")
        buf.write("\u013c\3\2\2\2\u0140\u013d\3\2\2\2\u0140\u013e\3\2\2\2")
        buf.write("\u0140\u013f\3\2\2\2\u0141-\3\2\2\2\u0142\u0143\7>\2\2")
        buf.write("\u0143\u0144\7\64\2\2\u0144\u0145\7!\2\2\u0145\u0146\7")
        buf.write(">\2\2\u0146\u0147\7\65\2\2\u0147\u0148\5> \2\u0148\u0149")
        buf.write("\7\66\2\2\u0149/\3\2\2\2\u014a\u014b\b\31\1\2\u014b\u014c")
        buf.write("\5\62\32\2\u014c\u015a\3\2\2\2\u014d\u0156\f\4\2\2\u014e")
        buf.write("\u014f\7=\2\2\u014f\u0157\7>\2\2\u0150\u0151\7=\2\2\u0151")
        buf.write("\u0152\7>\2\2\u0152\u0153\7\65\2\2\u0153\u0154\5> \2\u0154")
        buf.write("\u0155\7\66\2\2\u0155\u0157\3\2\2\2\u0156\u014e\3\2\2")
        buf.write("\2\u0156\u0150\3\2\2\2\u0157\u0159\3\2\2\2\u0158\u014d")
        buf.write("\3\2\2\2\u0159\u015c\3\2\2\2\u015a\u0158\3\2\2\2\u015a")
        buf.write("\u015b\3\2\2\2\u015b\61\3\2\2\2\u015c\u015a\3\2\2\2\u015d")
        buf.write("\u0160\5$\23\2\u015e\u0160\5*\26\2\u015f\u015d\3\2\2\2")
        buf.write("\u015f\u015e\3\2\2\2\u0160\63\3\2\2\2\u0161\u0165\5\60")
        buf.write("\31\2\u0162\u0165\5(\25\2\u0163\u0165\5.\30\2\u0164\u0161")
        buf.write("\3\2\2\2\u0164\u0162\3\2\2\2\u0164\u0163\3\2\2\2\u0165")
        buf.write("\65\3\2\2\2\u0166\u0167\7\36\2\2\u0167\u0168\7>\2\2\u0168")
        buf.write("\u0169\7\65\2\2\u0169\u016a\5> \2\u016a\u016b\7\66\2\2")
        buf.write("\u016b\u0171\3\2\2\2\u016c\u016d\7\65\2\2\u016d\u016e")
        buf.write("\5\66\34\2\u016e\u016f\7\66\2\2\u016f\u0171\3\2\2\2\u0170")
        buf.write("\u0166\3\2\2\2\u0170\u016c\3\2\2\2\u0171\67\3\2\2\2\u0172")
        buf.write("\u0175\7>\2\2\u0173\u0175\5\66\34\2\u0174\u0172\3\2\2")
        buf.write("\2\u0174\u0173\3\2\2\2\u01759\3\2\2\2\u0176\u0177\7>\2")
        buf.write("\2\u0177\u0178\7\65\2\2\u0178\u0179\5> \2\u0179\u017a")
        buf.write("\7\66\2\2\u017a;\3\2\2\2\u017b\u0184\5\66\34\2\u017c\u0184")
        buf.write("\5\64\33\2\u017d\u0184\5\4\3\2\u017e\u0184\5\f\7\2\u017f")
        buf.write("\u0184\5\20\t\2\u0180\u0184\5\36\20\2\u0181\u0184\5\34")
        buf.write("\17\2\u0182\u0184\5n8\2\u0183\u017b\3\2\2\2\u0183\u017c")
        buf.write("\3\2\2\2\u0183\u017d\3\2\2\2\u0183\u017e\3\2\2\2\u0183")
        buf.write("\u017f\3\2\2\2\u0183\u0180\3\2\2\2\u0183\u0181\3\2\2\2")
        buf.write("\u0183\u0182\3\2\2\2\u0184=\3\2\2\2\u0185\u018a\5<\37")
        buf.write("\2\u0186\u0187\7<\2\2\u0187\u0189\5<\37\2\u0188\u0186")
        buf.write("\3\2\2\2\u0189\u018c\3\2\2\2\u018a\u0188\3\2\2\2\u018a")
        buf.write("\u018b\3\2\2\2\u018b\u018e\3\2\2\2\u018c\u018a\3\2\2\2")
        buf.write("\u018d\u0185\3\2\2\2\u018d\u018e\3\2\2\2\u018e?\3\2\2")
        buf.write("\2\u018f\u0195\7\23\2\2\u0190\u0195\7\24\2\2\u0191\u0195")
        buf.write("\7\25\2\2\u0192\u0195\7\26\2\2\u0193\u0195\5B\"\2\u0194")
        buf.write("\u018f\3\2\2\2\u0194\u0190\3\2\2\2\u0194\u0191\3\2\2\2")
        buf.write("\u0194\u0192\3\2\2\2\u0194\u0193\3\2\2\2\u0195A\3\2\2")
        buf.write("\2\u0196\u0197\7\21\2\2\u0197\u0198\7\67\2\2\u0198\u0199")
        buf.write("\5@!\2\u0199\u019a\7<\2\2\u019a\u019b\7\5\2\2\u019b\u019c")
        buf.write("\78\2\2\u019cC\3\2\2\2\u019d\u01a2\7>\2\2\u019e\u019f")
        buf.write("\7<\2\2\u019f\u01a1\7>\2\2\u01a0\u019e\3\2\2\2\u01a1\u01a4")
        buf.write("\3\2\2\2\u01a2\u01a0\3\2\2\2\u01a2\u01a3\3\2\2\2\u01a3")
        buf.write("E\3\2\2\2\u01a4\u01a2\3\2\2\2\u01a5\u01a7\t\b\2\2\u01a6")
        buf.write("\u01a5\3\2\2\2\u01a6\u01a7\3\2\2\2\u01a7\u01a9\3\2\2\2")
        buf.write("\u01a8\u01aa\7!\2\2\u01a9\u01a8\3\2\2\2\u01a9\u01aa\3")
        buf.write("\2\2\2\u01aa\u01ab\3\2\2\2\u01ab\u01ac\5D#\2\u01ac\u01ad")
        buf.write("\7\62\2\2\u01ad\u01b0\5@!\2\u01ae\u01af\7\63\2\2\u01af")
        buf.write("\u01b1\5> \2\u01b0\u01ae\3\2\2\2\u01b0\u01b1\3\2\2\2\u01b1")
        buf.write("\u01b2\3\2\2\2\u01b2\u01b3\7;\2\2\u01b3G\3\2\2\2\u01b4")
        buf.write("\u01b7\7>\2\2\u01b5\u01b7\5<\37\2\u01b6\u01b4\3\2\2\2")
        buf.write("\u01b6\u01b5\3\2\2\2\u01b7I\3\2\2\2\u01b8\u01b9\5H%\2")
        buf.write("\u01b9\u01ba\7\63\2\2\u01ba\u01bb\5<\37\2\u01bb\u01bc")
        buf.write("\7;\2\2\u01bcK\3\2\2\2\u01bd\u01be\7\13\2\2\u01be\u01bf")
        buf.write("\7\65\2\2\u01bf\u01c0\5<\37\2\u01c0\u01c4\7\66\2\2\u01c1")
        buf.write("\u01c3\5P)\2\u01c2\u01c1\3\2\2\2\u01c3\u01c6\3\2\2\2\u01c4")
        buf.write("\u01c2\3\2\2\2\u01c4\u01c5\3\2\2\2\u01c5\u01d3\3\2\2\2")
        buf.write("\u01c6\u01c4\3\2\2\2\u01c7\u01c8\7\f\2\2\u01c8\u01c9\7")
        buf.write("\65\2\2\u01c9\u01ca\5<\37\2\u01ca\u01ce\7\66\2\2\u01cb")
        buf.write("\u01cd\5P)\2\u01cc\u01cb\3\2\2\2\u01cd\u01d0\3\2\2\2\u01ce")
        buf.write("\u01cc\3\2\2\2\u01ce\u01cf\3\2\2\2\u01cf\u01d2\3\2\2\2")
        buf.write("\u01d0\u01ce\3\2\2\2\u01d1\u01c7\3\2\2\2\u01d2\u01d5\3")
        buf.write("\2\2\2\u01d3\u01d1\3\2\2\2\u01d3\u01d4\3\2\2\2\u01d4\u01dd")
        buf.write("\3\2\2\2\u01d5\u01d3\3\2\2\2\u01d6\u01da\7\r\2\2\u01d7")
        buf.write("\u01d9\5P)\2\u01d8\u01d7\3\2\2\2\u01d9\u01dc\3\2\2\2\u01da")
        buf.write("\u01d8\3\2\2\2\u01da\u01db\3\2\2\2\u01db\u01de\3\2\2\2")
        buf.write("\u01dc\u01da\3\2\2\2\u01dd\u01d6\3\2\2\2\u01dd\u01de\3")
        buf.write("\2\2\2\u01deM\3\2\2\2\u01df\u01e0\7\16\2\2\u01e0\u01e1")
        buf.write("\7\65\2\2\u01e1\u01e2\7>\2\2\u01e2\u01e3\7\22\2\2\u01e3")
        buf.write("\u01e4\5<\37\2\u01e4\u01e5\7\3\2\2\u01e5\u01e8\5<\37\2")
        buf.write("\u01e6\u01e7\7\37\2\2\u01e7\u01e9\5<\37\2\u01e8\u01e6")
        buf.write("\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01ea\3\2\2\2\u01ea")
        buf.write("\u01eb\7\66\2\2\u01eb\u01ec\5P)\2\u01ecO\3\2\2\2\u01ed")
        buf.write("\u01ee\79\2\2\u01ee\u01ef\5^\60\2\u01ef\u01f0\7:\2\2\u01f0")
        buf.write("Q\3\2\2\2\u01f1\u01f5\5*\26\2\u01f2\u01f5\5.\30\2\u01f3")
        buf.write("\u01f5\5:\36\2\u01f4\u01f1\3\2\2\2\u01f4\u01f2\3\2\2\2")
        buf.write("\u01f4\u01f3\3\2\2\2\u01f5\u01f6\3\2\2\2\u01f6\u01f7\7")
        buf.write(";\2\2\u01f7S\3\2\2\2\u01f8\u01f9\7\n\2\2\u01f9\u01fa\7")
        buf.write(";\2\2\u01faU\3\2\2\2\u01fb\u01fd\7\27\2\2\u01fc\u01fe")
        buf.write("\5<\37\2\u01fd\u01fc\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe")
        buf.write("\u01ff\3\2\2\2\u01ff\u0200\7;\2\2\u0200W\3\2\2\2\u0201")
        buf.write("\u0202\7\t\2\2\u0202\u0203\7;\2\2\u0203Y\3\2\2\2\u0204")
        buf.write("\u0206\7!\2\2\u0205\u0204\3\2\2\2\u0205\u0206\3\2\2\2")
        buf.write("\u0206\u0207\3\2\2\2\u0207\u0208\7>\2\2\u0208\u020a\7")
        buf.write("\65\2\2\u0209\u020b\5h\65\2\u020a\u0209\3\2\2\2\u020a")
        buf.write("\u020b\3\2\2\2\u020b\u020c\3\2\2\2\u020c\u020d\7\66\2")
        buf.write("\2\u020d\u020e\5P)\2\u020e[\3\2\2\2\u020f\u021b\5F$\2")
        buf.write("\u0210\u021b\5J&\2\u0211\u021b\5L\'\2\u0212\u021b\5N(")
        buf.write("\2\u0213\u021b\5P)\2\u0214\u021b\5R*\2\u0215\u021b\5T")
        buf.write("+\2\u0216\u021b\5V,\2\u0217\u021b\5X-\2\u0218\u021b\5")
        buf.write("Z.\2\u0219\u021b\5`\61\2\u021a\u020f\3\2\2\2\u021a\u0210")
        buf.write("\3\2\2\2\u021a\u0211\3\2\2\2\u021a\u0212\3\2\2\2\u021a")
        buf.write("\u0213\3\2\2\2\u021a\u0214\3\2\2\2\u021a\u0215\3\2\2\2")
        buf.write("\u021a\u0216\3\2\2\2\u021a\u0217\3\2\2\2\u021a\u0218\3")
        buf.write("\2\2\2\u021a\u0219\3\2\2\2\u021b]\3\2\2\2\u021c\u021e")
        buf.write("\5\\/\2\u021d\u021c\3\2\2\2\u021e\u0221\3\2\2\2\u021f")
        buf.write("\u021d\3\2\2\2\u021f\u0220\3\2\2\2\u0220_\3\2\2\2\u0221")
        buf.write("\u021f\3\2\2\2\u0222\u0226\5d\63\2\u0223\u0226\5f\64\2")
        buf.write("\u0224\u0226\5b\62\2\u0225\u0222\3\2\2\2\u0225\u0223\3")
        buf.write("\2\2\2\u0225\u0224\3\2\2\2\u0226a\3\2\2\2\u0227\u0228")
        buf.write("\7\31\2\2\u0228\u022b\7>\2\2\u0229\u022a\7\62\2\2\u022a")
        buf.write("\u022c\7>\2\2\u022b\u0229\3\2\2\2\u022b\u022c\3\2\2\2")
        buf.write("\u022c\u022d\3\2\2\2\u022d\u022e\79\2\2\u022e\u022f\5")
        buf.write("^\60\2\u022f\u0230\7:\2\2\u0230c\3\2\2\2\u0231\u0232\7")
        buf.write("\34\2\2\u0232\u0234\7\65\2\2\u0233\u0235\5h\65\2\u0234")
        buf.write("\u0233\3\2\2\2\u0234\u0235\3\2\2\2\u0235\u0236\3\2\2\2")
        buf.write("\u0236\u0237\7\66\2\2\u0237\u0238\5P)\2\u0238e\3\2\2\2")
        buf.write("\u0239\u023a\7\35\2\2\u023a\u023b\7\66\2\2\u023b\u023c")
        buf.write("\7\65\2\2\u023c\u023d\5P)\2\u023dg\3\2\2\2\u023e\u0243")
        buf.write("\5j\66\2\u023f\u0240\7;\2\2\u0240\u0242\5j\66\2\u0241")
        buf.write("\u023f\3\2\2\2\u0242\u0245\3\2\2\2\u0243\u0241\3\2\2\2")
        buf.write("\u0243\u0244\3\2\2\2\u0244i\3\2\2\2\u0245\u0243\3\2\2")
        buf.write("\2\u0246\u0247\5D#\2\u0247\u0248\7\62\2\2\u0248\u0249")
        buf.write("\5@!\2\u0249k\3\2\2\2\u024a\u024b\7\21\2\2\u024b\u0254")
        buf.write("\7\65\2\2\u024c\u0251\5n8\2\u024d\u024e\7<\2\2\u024e\u0250")
        buf.write("\5n8\2\u024f\u024d\3\2\2\2\u0250\u0253\3\2\2\2\u0251\u024f")
        buf.write("\3\2\2\2\u0251\u0252\3\2\2\2\u0252\u0255\3\2\2\2\u0253")
        buf.write("\u0251\3\2\2\2\u0254\u024c\3\2\2\2\u0254\u0255\3\2\2\2")
        buf.write("\u0255\u0256\3\2\2\2\u0256\u0257\7\66\2\2\u0257m\3\2\2")
        buf.write("\2\u0258\u025e\7\5\2\2\u0259\u025e\7\6\2\2\u025a\u025e")
        buf.write("\7\7\2\2\u025b\u025e\7\b\2\2\u025c\u025e\5l\67\2\u025d")
        buf.write("\u0258\3\2\2\2\u025d\u0259\3\2\2\2\u025d\u025a\3\2\2\2")
        buf.write("\u025d\u025b\3\2\2\2\u025d\u025c\3\2\2\2\u025eo\3\2\2")
        buf.write("\2<}\u0088\u0095\u009c\u009f\u00a2\u00ab\u00b2\u00b5\u00be")
        buf.write("\u00cb\u00d2\u00df\u00e2\u00e6\u00ea\u00fd\u00ff\u0103")
        buf.write("\u010d\u0117\u0122\u0135\u0140\u0156\u015a\u015f\u0164")
        buf.write("\u0170\u0174\u0183\u018a\u018d\u0194\u01a2\u01a6\u01a9")
        buf.write("\u01b0\u01b6\u01c4\u01ce\u01d3\u01da\u01dd\u01e8\u01f4")
        buf.write("\u01fd\u0205\u020a\u021a\u021f\u0225\u022b\u0234\u0243")
        buf.write("\u0251\u0254\u025d")
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
    RULE_var_Declaration = 34
    RULE_lhs = 35
    RULE_stmt_Assign = 36
    RULE_stmt_If = 37
    RULE_stmt_ForIn = 38
    RULE_stmt_Block = 39
    RULE_stmt_MethodInvocation = 40
    RULE_stmt_Continue = 41
    RULE_stmt_Return = 42
    RULE_stmt_Break = 43
    RULE_stmt_MethodDeclaration = 44
    RULE_stmt = 45
    RULE_list_Stmt = 46
    RULE_stmt_Class = 47
    RULE_class_Declaration = 48
    RULE_class_Construction = 49
    RULE_class_Destruction = 50
    RULE_list_Parameters = 51
    RULE_seq_Parameters = 52
    RULE_idx_arraylit = 53
    RULE_datalit = 54

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
                   "list_Expr", "type_Data", "array_Type", "seq_ID", "var_Declaration", 
                   "lhs", "stmt_Assign", "stmt_If", "stmt_ForIn", "stmt_Block", 
                   "stmt_MethodInvocation", "stmt_Continue", "stmt_Return", 
                   "stmt_Break", "stmt_MethodDeclaration", "stmt", "list_Stmt", 
                   "stmt_Class", "class_Declaration", "class_Construction", 
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
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_Stmt(self):
            return self.getTypedRuleContext(D96Parser.List_StmtContext,0)


        def EOF(self):
            return self.getToken(D96Parser.EOF, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.list_Stmt()
            self.state = 111
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
            self.state = 113
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
            self.state = 116
            self.exp_1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 123
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp_0Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_0)
                    self.state = 118
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 119
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 120
                    self.exp_1(0) 
                self.state = 125
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

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
            self.state = 127
            self.exp_2()
            self._ctx.stop = self._input.LT(-1)
            self.state = 134
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp_1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_1)
                    self.state = 129
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 130
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 131
                    self.exp_2() 
                self.state = 136
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

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
            self.state = 147
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 137
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 138
                self.match(D96Parser.INTLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 139
                self.match(D96Parser.FLOATLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 140
                self.exp_MemberAccess()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 141
                self.exp_Method()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 142
                self.exp_Idx()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 143
                self.match(D96Parser.LB)
                self.state = 144
                self.exp_0(0)
                self.state = 145
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
            self.state = 157
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 149
                self.exp_TermBool()
                self.state = 150
                _la = self._input.LA(1)
                if not(_la==D96Parser.AND or _la==D96Parser.OR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 151
                self.exp_Bool()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.NOT:
                    self.state = 153
                    self.match(D96Parser.NOT)


                self.state = 156
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
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.STATIC:
                    self.state = 159
                    self.match(D96Parser.STATIC)


                self.state = 162
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 163
                self.match(D96Parser.BOOLLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 164
                self.exp_MemberAccess()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 165
                self.match(D96Parser.LB)
                self.state = 166
                self.exp_Bool()
                self.state = 167
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
            self.state = 176
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 171
                self.exp_TermStr()
                self.state = 172
                _la = self._input.LA(1)
                if not(_la==D96Parser.SADD or _la==D96Parser.SEQ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 173
                self.exp_Str()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 175
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
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.STATIC:
                    self.state = 178
                    self.match(D96Parser.STATIC)


                self.state = 181
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 182
                self.match(D96Parser.STRLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 183
                self.exp_MemberAccess()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 184
                self.match(D96Parser.LB)
                self.state = 185
                self.exp_Str()
                self.state = 186
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
            self.state = 190
            self.exp_TermEQANEQ()
            self.state = 191
            _la = self._input.LA(1)
            if not(_la==D96Parser.EQ or _la==D96Parser.NEQ):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 192
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
            self.state = 208
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 194
                self.match(D96Parser.LB)
                self.state = 195
                self.expr()
                self.state = 196
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 198
                self.match(D96Parser.INTLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 199
                self.match(D96Parser.BOOLLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 201
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.STATIC:
                    self.state = 200
                    self.match(D96Parser.STATIC)


                self.state = 203
                self.match(D96Parser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 204
                self.match(D96Parser.LB)
                self.state = 205
                self.exp_EqualAndNotEqual()
                self.state = 206
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
            self.state = 210
            self.exp_TermLRE()
            self.state = 211
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.GT) | (1 << D96Parser.GTE) | (1 << D96Parser.LT) | (1 << D96Parser.LTE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 212
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
            self.state = 224
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.match(D96Parser.LB)
                self.state = 215
                self.expr()
                self.state = 216
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 219
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.STATIC, D96Parser.ID]:
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
            self.state = 228
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.exp_EqualAndNotEqual()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 227
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
            self.state = 232
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.state = 230
                self.exp_Method()
                pass

            elif la_ == 2:
                self.state = 231
                self.match(D96Parser.ID)
                pass


            self.state = 234
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
            self.state = 237
            self.match(D96Parser.LSB)
            self.state = 238
            self.idx_Operators()
            self.state = 239
            self.match(D96Parser.RSB)
            self._ctx.stop = self._input.LT(-1)
            self.state = 253
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,17,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 251
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp_TermIdxContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_TermIdx)
                        self.state = 241
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 242
                        self.match(D96Parser.LSB)
                        self.state = 243
                        self.idx_Operators()
                        self.state = 244
                        self.match(D96Parser.RSB)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp_TermIdxContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_TermIdx)
                        self.state = 246
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 247
                        self.match(D96Parser.LSB)
                        self.state = 248
                        self.exp_Idx()
                        self.state = 249
                        self.match(D96Parser.RSB)
                        pass

             
                self.state = 255
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,17,self._ctx)

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
            self.state = 267
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 257
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==D96Parser.STATIC:
                    self.state = 256
                    self.match(D96Parser.STATIC)


                self.state = 259
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 260
                self.match(D96Parser.INTLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 261
                self.expr()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 262
                self.exp_Idx()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 263
                self.match(D96Parser.LB)
                self.state = 264
                self.exp_Idx()
                self.state = 265
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
            self.state = 270
            self.exp_InstanceAttributeAccessTerm()
            self._ctx.stop = self._input.LT(-1)
            self.state = 277
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,20,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp_InstanceAttributeAccessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_InstanceAttributeAccess)
                    self.state = 272
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 273
                    self.match(D96Parser.DOT)
                    self.state = 274
                    self.match(D96Parser.ID) 
                self.state = 279
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

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
            self.state = 288
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 280
                self.match(D96Parser.LB)
                self.state = 281
                self.exp_ClassObject()
                self.state = 282
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.state = 284
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.state = 285
                self.match(D96Parser.SELF)
                pass

            elif la_ == 4:
                self.state = 286
                self.exp_StaticAttributeAccess()
                pass

            elif la_ == 5:
                self.state = 287
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
            self.state = 290
            self.match(D96Parser.ID)
            self.state = 291
            self.match(D96Parser.SCOPE)
            self.state = 292
            self.match(D96Parser.STATIC)
            self.state = 293
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
            self.state = 296
            self.exp_InstanceMethodInvocationTerm()
            self._ctx.stop = self._input.LT(-1)
            self.state = 307
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp_InstanceMethodInvocationContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_InstanceMethodInvocation)
                    self.state = 298
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 299
                    self.match(D96Parser.DOT)
                    self.state = 300
                    self.match(D96Parser.ID)
                    self.state = 301
                    self.match(D96Parser.LB)
                    self.state = 302
                    self.list_Expr()
                    self.state = 303
                    self.match(D96Parser.RB) 
                self.state = 309
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

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
            self.state = 318
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 310
                self.match(D96Parser.LB)
                self.state = 311
                self.exp_ClassObject()
                self.state = 312
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.state = 314
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.state = 315
                self.match(D96Parser.SELF)
                pass

            elif la_ == 4:
                self.state = 316
                self.exp_StaticAttributeAccess()
                pass

            elif la_ == 5:
                self.state = 317
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
            self.state = 320
            self.match(D96Parser.ID)
            self.state = 321
            self.match(D96Parser.SCOPE)
            self.state = 322
            self.match(D96Parser.STATIC)
            self.state = 323
            self.match(D96Parser.ID)
            self.state = 324
            self.match(D96Parser.LB)
            self.state = 325
            self.list_Expr()
            self.state = 326
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
            self.state = 329
            self.exp_InstanceAttributeMethodTerm()
            self._ctx.stop = self._input.LT(-1)
            self.state = 344
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,25,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp_InstanceAttributeMethodContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_InstanceAttributeMethod)
                    self.state = 331
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 340
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
                    if la_ == 1:
                        self.state = 332
                        self.match(D96Parser.DOT)
                        self.state = 333
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 2:
                        self.state = 334
                        self.match(D96Parser.DOT)
                        self.state = 335
                        self.match(D96Parser.ID)
                        self.state = 336
                        self.match(D96Parser.LB)
                        self.state = 337
                        self.list_Expr()
                        self.state = 338
                        self.match(D96Parser.RB)
                        pass

             
                self.state = 346
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,25,self._ctx)

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
            self.state = 349
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 347
                self.exp_InstanceAttributeAccess(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 348
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
            self.state = 354
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 351
                self.exp_InstanceAttributeMethod(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 352
                self.exp_StaticAttributeAccess()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 353
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
            self.state = 366
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 356
                self.match(D96Parser.NEW)
                self.state = 357
                self.match(D96Parser.ID)
                self.state = 358
                self.match(D96Parser.LB)
                self.state = 359
                self.list_Expr()
                self.state = 360
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 362
                self.match(D96Parser.LB)
                self.state = 363
                self.exp_ObjCreation()
                self.state = 364
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
            self.state = 370
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.NEW, D96Parser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 369
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
            self.state = 372
            self.match(D96Parser.ID)
            self.state = 373
            self.match(D96Parser.LB)

            self.state = 374
            self.list_Expr()
            self.state = 375
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


        def datalit(self):
            return self.getTypedRuleContext(D96Parser.DatalitContext,0)


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
            self.state = 385
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,30,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 377
                self.exp_ObjCreation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 378
                self.exp_MemberAccess()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 379
                self.exp_IntFloat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 380
                self.exp_Bool()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 381
                self.exp_Str()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 382
                self.exp_Idx()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 383
                self.exp_RelationalOperation()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 384
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
            self.state = 395
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLLIT) | (1 << D96Parser.STRLIT) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.STATIC) | (1 << D96Parser.NOT) | (1 << D96Parser.LB) | (1 << D96Parser.ID))) != 0):
                self.state = 387
                self.expr()
                self.state = 392
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.CM:
                    self.state = 388
                    self.match(D96Parser.CM)
                    self.state = 389
                    self.expr()
                    self.state = 394
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
            self.state = 402
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 397
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 398
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 399
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 400
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 401
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
            self.state = 404
            self.match(D96Parser.ARRAY)
            self.state = 405
            self.match(D96Parser.LSB)
            self.state = 406
            self.type_Data()
            self.state = 407
            self.match(D96Parser.CM)
            self.state = 408
            self.match(D96Parser.INTLIT)
            self.state = 409
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
            self.state = 411
            self.match(D96Parser.ID)
            self.state = 416
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 412
                self.match(D96Parser.CM)
                self.state = 413
                self.match(D96Parser.ID)
                self.state = 418
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_DeclarationContext(ParserRuleContext):
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
            return D96Parser.RULE_var_Declaration

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_Declaration" ):
                return visitor.visitVar_Declaration(self)
            else:
                return visitor.visitChildren(self)




    def var_Declaration(self):

        localctx = D96Parser.Var_DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_var_Declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.VAL or _la==D96Parser.VAR:
                self.state = 419
                _la = self._input.LA(1)
                if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 423
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.STATIC:
                self.state = 422
                self.match(D96Parser.STATIC)


            self.state = 425
            self.seq_ID()
            self.state = 426
            self.match(D96Parser.COLON)
            self.state = 427
            self.type_Data()
            self.state = 430
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ASSIGN:
                self.state = 428
                self.match(D96Parser.ASSIGN)
                self.state = 429
                self.list_Expr()


            self.state = 432
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
            self.state = 436
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,38,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 434
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 435
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
            self.state = 438
            self.lhs()
            self.state = 439
            self.match(D96Parser.ASSIGN)
            self.state = 440
            self.expr()
            self.state = 441
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
            self.state = 443
            self.match(D96Parser.IF)
            self.state = 444
            self.match(D96Parser.LB)
            self.state = 445
            self.expr()
            self.state = 446
            self.match(D96Parser.RB)
            self.state = 450
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,39,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 447
                    self.stmt_Block() 
                self.state = 452
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,39,self._ctx)

            self.state = 465
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 453
                self.match(D96Parser.ELSEIF)
                self.state = 454
                self.match(D96Parser.LB)
                self.state = 455
                self.expr()
                self.state = 456
                self.match(D96Parser.RB)
                self.state = 460
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,40,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 457
                        self.stmt_Block() 
                    self.state = 462
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,40,self._ctx)

                self.state = 467
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 475
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 468
                self.match(D96Parser.ELSE)
                self.state = 472
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 469
                        self.stmt_Block() 
                    self.state = 474
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,42,self._ctx)



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
            self.state = 477
            self.match(D96Parser.FOREACH)
            self.state = 478
            self.match(D96Parser.LB)
            self.state = 479
            self.match(D96Parser.ID)
            self.state = 480
            self.match(D96Parser.IN)
            self.state = 481
            self.expr()
            self.state = 482
            self.match(D96Parser.T__0)
            self.state = 483
            self.expr()
            self.state = 486
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 484
                self.match(D96Parser.BY)
                self.state = 485
                self.expr()


            self.state = 488
            self.match(D96Parser.RB)
            self.state = 489
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
            self.state = 491
            self.match(D96Parser.LCB)

            self.state = 492
            self.list_Stmt()
            self.state = 493
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
            self.state = 498
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,45,self._ctx)
            if la_ == 1:
                self.state = 495
                self.exp_InstanceMethodInvocation(0)
                pass

            elif la_ == 2:
                self.state = 496
                self.exp_StaticMethodInvocation()
                pass

            elif la_ == 3:
                self.state = 497
                self.exp_Method()
                pass


            self.state = 500
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
            self.state = 502
            self.match(D96Parser.CONTINUE)
            self.state = 503
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
            self.state = 505
            self.match(D96Parser.RETURN)
            self.state = 507
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLLIT) | (1 << D96Parser.STRLIT) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.STATIC) | (1 << D96Parser.NOT) | (1 << D96Parser.LB) | (1 << D96Parser.ID))) != 0):
                self.state = 506
                self.expr()


            self.state = 509
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
            self.state = 511
            self.match(D96Parser.BREAK)
            self.state = 512
            self.match(D96Parser.SM)
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
        self.enterRule(localctx, 88, self.RULE_stmt_MethodDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 515
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.STATIC:
                self.state = 514
                self.match(D96Parser.STATIC)


            self.state = 517
            self.match(D96Parser.ID)
            self.state = 518
            self.match(D96Parser.LB)
            self.state = 520
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 519
                self.list_Parameters()


            self.state = 522
            self.match(D96Parser.RB)
            self.state = 523
            self.stmt_Block()
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

        def var_Declaration(self):
            return self.getTypedRuleContext(D96Parser.Var_DeclarationContext,0)


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
        self.enterRule(localctx, 90, self.RULE_stmt)
        try:
            self.state = 536
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 525
                self.var_Declaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 526
                self.stmt_Assign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 527
                self.stmt_If()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 528
                self.stmt_ForIn()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 529
                self.stmt_Block()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 530
                self.stmt_MethodInvocation()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 531
                self.stmt_Continue()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 532
                self.stmt_Return()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 533
                self.stmt_Break()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 534
                self.stmt_MethodDeclaration()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 535
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
        self.enterRule(localctx, 92, self.RULE_list_Stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 541
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLLIT) | (1 << D96Parser.STRLIT) | (1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.ARRAY) | (1 << D96Parser.RETURN) | (1 << D96Parser.CLASS) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.STATIC) | (1 << D96Parser.NOT) | (1 << D96Parser.LB) | (1 << D96Parser.LCB) | (1 << D96Parser.ID))) != 0):
                self.state = 538
                self.stmt()
                self.state = 543
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
        self.enterRule(localctx, 94, self.RULE_stmt_Class)
        try:
            self.state = 547
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 544
                self.class_Construction()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 545
                self.class_Destruction()
                pass
            elif token in [D96Parser.CLASS]:
                self.enterOuterAlt(localctx, 3)
                self.state = 546
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
        self.enterRule(localctx, 96, self.RULE_class_Declaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 549
            self.match(D96Parser.CLASS)
            self.state = 550
            self.match(D96Parser.ID)
            self.state = 553
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 551
                self.match(D96Parser.COLON)
                self.state = 552
                self.match(D96Parser.ID)


            self.state = 555
            self.match(D96Parser.LCB)
            self.state = 556
            self.list_Stmt()
            self.state = 557
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
        self.enterRule(localctx, 98, self.RULE_class_Construction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 559
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 560
            self.match(D96Parser.LB)
            self.state = 562
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ID:
                self.state = 561
                self.list_Parameters()


            self.state = 564
            self.match(D96Parser.RB)
            self.state = 565
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
        self.enterRule(localctx, 100, self.RULE_class_Destruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 567
            self.match(D96Parser.DESTRUCTOR)
            self.state = 568
            self.match(D96Parser.RB)
            self.state = 569
            self.match(D96Parser.LB)
            self.state = 570
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
        self.enterRule(localctx, 102, self.RULE_list_Parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 572
            self.seq_Parameters()
            self.state = 577
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SM:
                self.state = 573
                self.match(D96Parser.SM)
                self.state = 574
                self.seq_Parameters()
                self.state = 579
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
        self.enterRule(localctx, 104, self.RULE_seq_Parameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 580
            self.seq_ID()
            self.state = 581
            self.match(D96Parser.COLON)
            self.state = 582
            self.type_Data()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Idx_arraylitContext(ParserRuleContext):
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdx_arraylit" ):
                return visitor.visitIdx_arraylit(self)
            else:
                return visitor.visitChildren(self)




    def idx_arraylit(self):

        localctx = D96Parser.Idx_arraylitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_idx_arraylit)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 584
            self.match(D96Parser.ARRAY)
            self.state = 585
            self.match(D96Parser.LB)
            self.state = 594
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.BOOLLIT) | (1 << D96Parser.STRLIT) | (1 << D96Parser.ARRAY))) != 0):
                self.state = 586
                self.datalit()
                self.state = 591
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.CM:
                    self.state = 587
                    self.match(D96Parser.CM)
                    self.state = 588
                    self.datalit()
                    self.state = 593
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 596
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DatalitContext(ParserRuleContext):
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

        def idx_arraylit(self):
            return self.getTypedRuleContext(D96Parser.Idx_arraylitContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_datalit

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDatalit" ):
                return visitor.visitDatalit(self)
            else:
                return visitor.visitChildren(self)




    def datalit(self):

        localctx = D96Parser.DatalitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_datalit)
        try:
            self.state = 603
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 598
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 599
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.BOOLLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 600
                self.match(D96Parser.BOOLLIT)
                pass
            elif token in [D96Parser.STRLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 601
                self.match(D96Parser.STRLIT)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 602
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
         



