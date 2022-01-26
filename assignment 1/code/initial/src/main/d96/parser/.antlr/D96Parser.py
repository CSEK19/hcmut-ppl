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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3D")
        buf.write("\u0284\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64\t\64")
        buf.write("\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:\4;\t")
        buf.write(";\4<\t<\4=\t=\4>\t>\3\2\6\2~\n\2\r\2\16\2\177\3\2\3\2")
        buf.write("\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\7\4\u008c\n\4\f\4\16")
        buf.write("\4\u008f\13\4\3\5\3\5\3\5\3\5\3\5\3\5\7\5\u0097\n\5\f")
        buf.write("\5\16\5\u009a\13\5\3\6\3\6\3\6\5\6\u009f\n\6\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7\u00ac\n\7\3\b\3")
        buf.write("\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\t\u00b9\n\t\3")
        buf.write("\n\3\n\3\n\5\n\u00be\n\n\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\5\13\u00c7\n\13\3\f\3\f\5\f\u00cb\n\f\3\r\3\r\3")
        buf.write("\r\3\r\3\r\5\r\u00d2\n\r\3\16\3\16\3\16\3\16\3\16\3\16")
        buf.write("\3\16\5\16\u00db\n\16\3\17\3\17\3\17\3\17\3\20\3\20\3")
        buf.write("\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\5\20")
        buf.write("\u00ed\n\20\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3")
        buf.write("\22\3\22\3\22\3\22\5\22\u00fb\n\22\3\23\3\23\5\23\u00ff")
        buf.write("\n\23\3\24\3\24\5\24\u0103\n\24\3\24\3\24\3\25\3\25\3")
        buf.write("\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25\3\25")
        buf.write("\3\25\3\25\7\25\u0116\n\25\f\25\16\25\u0119\13\25\3\26")
        buf.write("\3\26\3\26\3\26\3\26\3\26\3\26\3\26\3\26\5\26\u0124\n")
        buf.write("\26\3\27\3\27\3\27\3\27\3\27\3\27\7\27\u012c\n\27\f\27")
        buf.write("\16\27\u012f\13\27\3\30\3\30\3\30\3\30\3\30\5\30\u0136")
        buf.write("\n\30\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\5\32\u0144\n\32\3\32\7\32\u0147\n\32\f\32\16")
        buf.write("\32\u014a\13\32\3\33\3\33\3\33\3\33\3\33\5\33\u0151\n")
        buf.write("\33\3\34\3\34\3\34\3\34\3\34\5\34\u0158\n\34\3\34\3\34")
        buf.write("\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\3\35\5\35")
        buf.write("\u0166\n\35\3\35\5\35\u0169\n\35\7\35\u016b\n\35\f\35")
        buf.write("\16\35\u016e\13\35\3\36\3\36\5\36\u0172\n\36\3\37\3\37")
        buf.write("\3\37\5\37\u0177\n\37\3 \3 \3 \3 \5 \u017d\n \3 \3 \3")
        buf.write(" \3 \3 \5 \u0184\n \3!\3!\5!\u0188\n!\3\"\3\"\3\"\5\"")
        buf.write("\u018d\n\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3#\3#\5#\u0199\n")
        buf.write("#\3$\3$\3$\7$\u019e\n$\f$\16$\u01a1\13$\3%\3%\3%\3%\3")
        buf.write("%\5%\u01a8\n%\3&\3&\3&\3&\3&\3&\3&\3\'\3\'\3\'\7\'\u01b4")
        buf.write("\n\'\f\'\16\'\u01b7\13\'\3(\3(\3(\3(\3(\3(\3(\3(\5(\u01c1")
        buf.write("\n(\3)\3)\3)\3)\3)\3)\3)\3)\3)\3)\5)\u01cd\n)\3*\5*\u01d0")
        buf.write("\n*\3*\3*\3*\3+\3+\5+\u01d7\n+\3,\3,\3,\3,\3,\3-\3-\3")
        buf.write("-\3-\3-\7-\u01e3\n-\f-\16-\u01e6\13-\3-\3-\3-\3-\3-\7")
        buf.write("-\u01ed\n-\f-\16-\u01f0\13-\7-\u01f2\n-\f-\16-\u01f5\13")
        buf.write("-\3-\3-\7-\u01f9\n-\f-\16-\u01fc\13-\5-\u01fe\n-\3.\3")
        buf.write(".\3.\3.\3.\3.\3.\3.\3.\5.\u0209\n.\3.\3.\3.\3/\3/\3/\3")
        buf.write("/\3\60\3\60\3\60\5\60\u0215\n\60\3\60\3\60\3\61\3\61\3")
        buf.write("\61\3\62\3\62\5\62\u021e\n\62\3\62\3\62\3\63\3\63\3\63")
        buf.write("\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64\3\64")
        buf.write("\5\64\u0230\n\64\3\65\7\65\u0233\n\65\f\65\16\65\u0236")
        buf.write("\13\65\3\66\3\66\5\66\u023a\n\66\3\67\3\67\3\67\3\67\5")
        buf.write("\67\u0240\n\67\3\67\3\67\3\67\3\67\7\67\u0246\n\67\f\67")
        buf.write("\16\67\u0249\13\67\3\67\3\67\38\38\38\58\u0250\n8\38\3")
        buf.write("8\38\39\39\39\59\u0258\n9\39\39\39\3:\3:\3:\3:\3:\3;\3")
        buf.write(";\3;\7;\u0265\n;\f;\16;\u0268\13;\3<\3<\3<\3<\3=\3=\3")
        buf.write("=\3=\3=\7=\u0273\n=\f=\16=\u0276\13=\5=\u0278\n=\3=\3")
        buf.write("=\3>\3>\3>\3>\3>\3>\5>\u0282\n>\3>\2\b\6\b(,\628?\2\4")
        buf.write("\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64")
        buf.write("\668:<>@BDFHJLNPRTVXZ\\^`bdfhjlnprtvxz\2\n\3\2\35\36\3")
        buf.write("\2\37!\3\2+,\3\2?@\3\2()\3\2\"#\3\2$\'\3\2\26\27\2\u02b9")
        buf.write("\2}\3\2\2\2\4\u0083\3\2\2\2\6\u0085\3\2\2\2\b\u0090\3")
        buf.write("\2\2\2\n\u009e\3\2\2\2\f\u00ab\3\2\2\2\16\u00ad\3\2\2")
        buf.write("\2\20\u00b8\3\2\2\2\22\u00bd\3\2\2\2\24\u00c6\3\2\2\2")
        buf.write("\26\u00ca\3\2\2\2\30\u00d1\3\2\2\2\32\u00da\3\2\2\2\34")
        buf.write("\u00dc\3\2\2\2\36\u00ec\3\2\2\2 \u00ee\3\2\2\2\"\u00fa")
        buf.write("\3\2\2\2$\u00fe\3\2\2\2&\u0102\3\2\2\2(\u0106\3\2\2\2")
        buf.write("*\u0123\3\2\2\2,\u0125\3\2\2\2.\u0135\3\2\2\2\60\u0137")
        buf.write("\3\2\2\2\62\u013b\3\2\2\2\64\u0150\3\2\2\2\66\u0152\3")
        buf.write("\2\2\28\u015b\3\2\2\2:\u0171\3\2\2\2<\u0176\3\2\2\2>\u0183")
        buf.write("\3\2\2\2@\u0187\3\2\2\2B\u0189\3\2\2\2D\u0198\3\2\2\2")
        buf.write("F\u019a\3\2\2\2H\u01a7\3\2\2\2J\u01a9\3\2\2\2L\u01b0\3")
        buf.write("\2\2\2N\u01c0\3\2\2\2P\u01cc\3\2\2\2R\u01cf\3\2\2\2T\u01d6")
        buf.write("\3\2\2\2V\u01d8\3\2\2\2X\u01dd\3\2\2\2Z\u01ff\3\2\2\2")
        buf.write("\\\u020d\3\2\2\2^\u0214\3\2\2\2`\u0218\3\2\2\2b\u021b")
        buf.write("\3\2\2\2d\u0221\3\2\2\2f\u022f\3\2\2\2h\u0234\3\2\2\2")
        buf.write("j\u0239\3\2\2\2l\u023b\3\2\2\2n\u024c\3\2\2\2p\u0254\3")
        buf.write("\2\2\2r\u025c\3\2\2\2t\u0261\3\2\2\2v\u0269\3\2\2\2x\u026d")
        buf.write("\3\2\2\2z\u0281\3\2\2\2|~\5l\67\2}|\3\2\2\2~\177\3\2\2")
        buf.write("\2\177}\3\2\2\2\177\u0080\3\2\2\2\u0080\u0081\3\2\2\2")
        buf.write("\u0081\u0082\7\2\2\3\u0082\3\3\2\2\2\u0083\u0084\5\6\4")
        buf.write("\2\u0084\5\3\2\2\2\u0085\u0086\b\4\1\2\u0086\u0087\5\b")
        buf.write("\5\2\u0087\u008d\3\2\2\2\u0088\u0089\f\4\2\2\u0089\u008a")
        buf.write("\t\2\2\2\u008a\u008c\5\b\5\2\u008b\u0088\3\2\2\2\u008c")
        buf.write("\u008f\3\2\2\2\u008d\u008b\3\2\2\2\u008d\u008e\3\2\2\2")
        buf.write("\u008e\7\3\2\2\2\u008f\u008d\3\2\2\2\u0090\u0091\b\5\1")
        buf.write("\2\u0091\u0092\5\n\6\2\u0092\u0098\3\2\2\2\u0093\u0094")
        buf.write("\f\4\2\2\u0094\u0095\t\3\2\2\u0095\u0097\5\n\6\2\u0096")
        buf.write("\u0093\3\2\2\2\u0097\u009a\3\2\2\2\u0098\u0096\3\2\2\2")
        buf.write("\u0098\u0099\3\2\2\2\u0099\t\3\2\2\2\u009a\u0098\3\2\2")
        buf.write("\2\u009b\u009c\7\36\2\2\u009c\u009f\5\n\6\2\u009d\u009f")
        buf.write("\5\f\7\2\u009e\u009b\3\2\2\2\u009e\u009d\3\2\2\2\u009f")
        buf.write("\13\3\2\2\2\u00a0\u00ac\7@\2\2\u00a1\u00ac\7>\2\2\u00a2")
        buf.write("\u00ac\7;\2\2\u00a3\u00ac\7<\2\2\u00a4\u00ac\5<\37\2\u00a5")
        buf.write("\u00ac\5B\"\2\u00a6\u00ac\5&\24\2\u00a7\u00a8\7\60\2\2")
        buf.write("\u00a8\u00a9\5\6\4\2\u00a9\u00aa\7\61\2\2\u00aa\u00ac")
        buf.write("\3\2\2\2\u00ab\u00a0\3\2\2\2\u00ab\u00a1\3\2\2\2\u00ab")
        buf.write("\u00a2\3\2\2\2\u00ab\u00a3\3\2\2\2\u00ab\u00a4\3\2\2\2")
        buf.write("\u00ab\u00a5\3\2\2\2\u00ab\u00a6\3\2\2\2\u00ab\u00a7\3")
        buf.write("\2\2\2\u00ac\r\3\2\2\2\u00ad\u00ae\5\20\t\2\u00ae\u00af")
        buf.write("\t\4\2\2\u00af\u00b0\5\16\b\2\u00b0\17\3\2\2\2\u00b1\u00b9")
        buf.write("\t\5\2\2\u00b2\u00b9\7\4\2\2\u00b3\u00b9\5<\37\2\u00b4")
        buf.write("\u00b5\7\60\2\2\u00b5\u00b6\5\20\t\2\u00b6\u00b7\7\61")
        buf.write("\2\2\u00b7\u00b9\3\2\2\2\u00b8\u00b1\3\2\2\2\u00b8\u00b2")
        buf.write("\3\2\2\2\u00b8\u00b3\3\2\2\2\u00b8\u00b4\3\2\2\2\u00b9")
        buf.write("\21\3\2\2\2\u00ba\u00bb\7*\2\2\u00bb\u00be\5\22\n\2\u00bc")
        buf.write("\u00be\5\24\13\2\u00bd\u00ba\3\2\2\2\u00bd\u00bc\3\2\2")
        buf.write("\2\u00be\23\3\2\2\2\u00bf\u00c7\t\5\2\2\u00c0\u00c7\7")
        buf.write("\4\2\2\u00c1\u00c7\5<\37\2\u00c2\u00c3\7\60\2\2\u00c3")
        buf.write("\u00c4\5\24\13\2\u00c4\u00c5\7\61\2\2\u00c5\u00c7\3\2")
        buf.write("\2\2\u00c6\u00bf\3\2\2\2\u00c6\u00c0\3\2\2\2\u00c6\u00c1")
        buf.write("\3\2\2\2\u00c6\u00c2\3\2\2\2\u00c7\25\3\2\2\2\u00c8\u00cb")
        buf.write("\5\16\b\2\u00c9\u00cb\5\22\n\2\u00ca\u00c8\3\2\2\2\u00ca")
        buf.write("\u00c9\3\2\2\2\u00cb\27\3\2\2\2\u00cc\u00cd\5\32\16\2")
        buf.write("\u00cd\u00ce\t\6\2\2\u00ce\u00cf\5\30\r\2\u00cf\u00d2")
        buf.write("\3\2\2\2\u00d0\u00d2\5\32\16\2\u00d1\u00cc\3\2\2\2\u00d1")
        buf.write("\u00d0\3\2\2\2\u00d2\31\3\2\2\2\u00d3\u00db\t\5\2\2\u00d4")
        buf.write("\u00db\7=\2\2\u00d5\u00db\5<\37\2\u00d6\u00d7\7\60\2\2")
        buf.write("\u00d7\u00d8\5\30\r\2\u00d8\u00d9\7\61\2\2\u00d9\u00db")
        buf.write("\3\2\2\2\u00da\u00d3\3\2\2\2\u00da\u00d4\3\2\2\2\u00da")
        buf.write("\u00d5\3\2\2\2\u00da\u00d6\3\2\2\2\u00db\33\3\2\2\2\u00dc")
        buf.write("\u00dd\5\36\20\2\u00dd\u00de\t\7\2\2\u00de\u00df\5\36")
        buf.write("\20\2\u00df\35\3\2\2\2\u00e0\u00e1\7\60\2\2\u00e1\u00e2")
        buf.write("\5D#\2\u00e2\u00e3\7\61\2\2\u00e3\u00ed\3\2\2\2\u00e4")
        buf.write("\u00ed\7>\2\2\u00e5\u00ed\7;\2\2\u00e6\u00ed\7\4\2\2\u00e7")
        buf.write("\u00ed\t\5\2\2\u00e8\u00e9\7\60\2\2\u00e9\u00ea\5\34\17")
        buf.write("\2\u00ea\u00eb\7\61\2\2\u00eb\u00ed\3\2\2\2\u00ec\u00e0")
        buf.write("\3\2\2\2\u00ec\u00e4\3\2\2\2\u00ec\u00e5\3\2\2\2\u00ec")
        buf.write("\u00e6\3\2\2\2\u00ec\u00e7\3\2\2\2\u00ec\u00e8\3\2\2\2")
        buf.write("\u00ed\37\3\2\2\2\u00ee\u00ef\5\"\22\2\u00ef\u00f0\t\b")
        buf.write("\2\2\u00f0\u00f1\5\"\22\2\u00f1!\3\2\2\2\u00f2\u00f3\7")
        buf.write("\60\2\2\u00f3\u00f4\5D#\2\u00f4\u00f5\7\61\2\2\u00f5\u00fb")
        buf.write("\3\2\2\2\u00f6\u00fb\7>\2\2\u00f7\u00fb\7;\2\2\u00f8\u00fb")
        buf.write("\7<\2\2\u00f9\u00fb\t\5\2\2\u00fa\u00f2\3\2\2\2\u00fa")
        buf.write("\u00f6\3\2\2\2\u00fa\u00f7\3\2\2\2\u00fa\u00f8\3\2\2\2")
        buf.write("\u00fa\u00f9\3\2\2\2\u00fb#\3\2\2\2\u00fc\u00ff\5\34\17")
        buf.write("\2\u00fd\u00ff\5 \21\2\u00fe\u00fc\3\2\2\2\u00fe\u00fd")
        buf.write("\3\2\2\2\u00ff%\3\2\2\2\u0100\u0103\5B\"\2\u0101\u0103")
        buf.write("\7@\2\2\u0102\u0100\3\2\2\2\u0102\u0101\3\2\2\2\u0103")
        buf.write("\u0104\3\2\2\2\u0104\u0105\5(\25\2\u0105\'\3\2\2\2\u0106")
        buf.write("\u0107\b\25\1\2\u0107\u0108\7\62\2\2\u0108\u0109\5*\26")
        buf.write("\2\u0109\u010a\7\63\2\2\u010a\u0117\3\2\2\2\u010b\u010c")
        buf.write("\f\4\2\2\u010c\u010d\7\62\2\2\u010d\u010e\5*\26\2\u010e")
        buf.write("\u010f\7\63\2\2\u010f\u0116\3\2\2\2\u0110\u0111\f\3\2")
        buf.write("\2\u0111\u0112\7\62\2\2\u0112\u0113\5&\24\2\u0113\u0114")
        buf.write("\7\63\2\2\u0114\u0116\3\2\2\2\u0115\u010b\3\2\2\2\u0115")
        buf.write("\u0110\3\2\2\2\u0116\u0119\3\2\2\2\u0117\u0115\3\2\2\2")
        buf.write("\u0117\u0118\3\2\2\2\u0118)\3\2\2\2\u0119\u0117\3\2\2")
        buf.write("\2\u011a\u0124\t\5\2\2\u011b\u0124\7>\2\2\u011c\u0124")
        buf.write("\7;\2\2\u011d\u0124\5D#\2\u011e\u0124\5&\24\2\u011f\u0120")
        buf.write("\7\60\2\2\u0120\u0121\5&\24\2\u0121\u0122\7\61\2\2\u0122")
        buf.write("\u0124\3\2\2\2\u0123\u011a\3\2\2\2\u0123\u011b\3\2\2\2")
        buf.write("\u0123\u011c\3\2\2\2\u0123\u011d\3\2\2\2\u0123\u011e\3")
        buf.write("\2\2\2\u0123\u011f\3\2\2\2\u0124+\3\2\2\2\u0125\u0126")
        buf.write("\b\27\1\2\u0126\u0127\5.\30\2\u0127\u012d\3\2\2\2\u0128")
        buf.write("\u0129\f\4\2\2\u0129\u012a\78\2\2\u012a\u012c\7@\2\2\u012b")
        buf.write("\u0128\3\2\2\2\u012c\u012f\3\2\2\2\u012d\u012b\3\2\2\2")
        buf.write("\u012d\u012e\3\2\2\2\u012e-\3\2\2\2\u012f\u012d\3\2\2")
        buf.write("\2\u0130\u0136\5@!\2\u0131\u0136\7@\2\2\u0132\u0136\7")
        buf.write("\34\2\2\u0133\u0136\5\60\31\2\u0134\u0136\5\66\34\2\u0135")
        buf.write("\u0130\3\2\2\2\u0135\u0131\3\2\2\2\u0135\u0132\3\2\2\2")
        buf.write("\u0135\u0133\3\2\2\2\u0135\u0134\3\2\2\2\u0136/\3\2\2")
        buf.write("\2\u0137\u0138\7@\2\2\u0138\u0139\7/\2\2\u0139\u013a\7")
        buf.write("?\2\2\u013a\61\3\2\2\2\u013b\u013c\b\32\1\2\u013c\u013d")
        buf.write("\5\64\33\2\u013d\u0148\3\2\2\2\u013e\u013f\f\4\2\2\u013f")
        buf.write("\u0140\78\2\2\u0140\u0141\7@\2\2\u0141\u0143\7\60\2\2")
        buf.write("\u0142\u0144\5F$\2\u0143\u0142\3\2\2\2\u0143\u0144\3\2")
        buf.write("\2\2\u0144\u0145\3\2\2\2\u0145\u0147\7\61\2\2\u0146\u013e")
        buf.write("\3\2\2\2\u0147\u014a\3\2\2\2\u0148\u0146\3\2\2\2\u0148")
        buf.write("\u0149\3\2\2\2\u0149\63\3\2\2\2\u014a\u0148\3\2\2\2\u014b")
        buf.write("\u0151\5@!\2\u014c\u0151\7@\2\2\u014d\u0151\7\34\2\2\u014e")
        buf.write("\u0151\5\60\31\2\u014f\u0151\5\66\34\2\u0150\u014b\3\2")
        buf.write("\2\2\u0150\u014c\3\2\2\2\u0150\u014d\3\2\2\2\u0150\u014e")
        buf.write("\3\2\2\2\u0150\u014f\3\2\2\2\u0151\65\3\2\2\2\u0152\u0153")
        buf.write("\7@\2\2\u0153\u0154\7/\2\2\u0154\u0155\7?\2\2\u0155\u0157")
        buf.write("\7\60\2\2\u0156\u0158\5F$\2\u0157\u0156\3\2\2\2\u0157")
        buf.write("\u0158\3\2\2\2\u0158\u0159\3\2\2\2\u0159\u015a\7\61\2")
        buf.write("\2\u015a\67\3\2\2\2\u015b\u015c\b\35\1\2\u015c\u015d\5")
        buf.write(":\36\2\u015d\u016c\3\2\2\2\u015e\u0168\f\4\2\2\u015f\u0160")
        buf.write("\78\2\2\u0160\u0169\7@\2\2\u0161\u0162\78\2\2\u0162\u0163")
        buf.write("\7@\2\2\u0163\u0165\7\60\2\2\u0164\u0166\5F$\2\u0165\u0164")
        buf.write("\3\2\2\2\u0165\u0166\3\2\2\2\u0166\u0167\3\2\2\2\u0167")
        buf.write("\u0169\7\61\2\2\u0168\u015f\3\2\2\2\u0168\u0161\3\2\2")
        buf.write("\2\u0169\u016b\3\2\2\2\u016a\u015e\3\2\2\2\u016b\u016e")
        buf.write("\3\2\2\2\u016c\u016a\3\2\2\2\u016c\u016d\3\2\2\2\u016d")
        buf.write("9\3\2\2\2\u016e\u016c\3\2\2\2\u016f\u0172\5,\27\2\u0170")
        buf.write("\u0172\5\62\32\2\u0171\u016f\3\2\2\2\u0171\u0170\3\2\2")
        buf.write("\2\u0172;\3\2\2\2\u0173\u0177\5\66\34\2\u0174\u0177\5")
        buf.write("\60\31\2\u0175\u0177\58\35\2\u0176\u0173\3\2\2\2\u0176")
        buf.write("\u0174\3\2\2\2\u0176\u0175\3\2\2\2\u0177=\3\2\2\2\u0178")
        buf.write("\u0179\7\32\2\2\u0179\u017a\7@\2\2\u017a\u017c\7\60\2")
        buf.write("\2\u017b\u017d\5F$\2\u017c\u017b\3\2\2\2\u017c\u017d\3")
        buf.write("\2\2\2\u017d\u017e\3\2\2\2\u017e\u0184\7\61\2\2\u017f")
        buf.write("\u0180\7\60\2\2\u0180\u0181\5> \2\u0181\u0182\7\61\2\2")
        buf.write("\u0182\u0184\3\2\2\2\u0183\u0178\3\2\2\2\u0183\u017f\3")
        buf.write("\2\2\2\u0184?\3\2\2\2\u0185\u0188\7@\2\2\u0186\u0188\5")
        buf.write("> \2\u0187\u0185\3\2\2\2\u0187\u0186\3\2\2\2\u0188A\3")
        buf.write("\2\2\2\u0189\u018a\7@\2\2\u018a\u018c\7\60\2\2\u018b\u018d")
        buf.write("\5F$\2\u018c\u018b\3\2\2\2\u018c\u018d\3\2\2\2\u018d\u018e")
        buf.write("\3\2\2\2\u018e\u018f\7\61\2\2\u018fC\3\2\2\2\u0190\u0199")
        buf.write("\5> \2\u0191\u0199\5<\37\2\u0192\u0199\5\4\3\2\u0193\u0199")
        buf.write("\5\26\f\2\u0194\u0199\5\30\r\2\u0195\u0199\5&\24\2\u0196")
        buf.write("\u0199\5$\23\2\u0197\u0199\5z>\2\u0198\u0190\3\2\2\2\u0198")
        buf.write("\u0191\3\2\2\2\u0198\u0192\3\2\2\2\u0198\u0193\3\2\2\2")
        buf.write("\u0198\u0194\3\2\2\2\u0198\u0195\3\2\2\2\u0198\u0196\3")
        buf.write("\2\2\2\u0198\u0197\3\2\2\2\u0199E\3\2\2\2\u019a\u019f")
        buf.write("\5D#\2\u019b\u019c\7\67\2\2\u019c\u019e\5D#\2\u019d\u019b")
        buf.write("\3\2\2\2\u019e\u01a1\3\2\2\2\u019f\u019d\3\2\2\2\u019f")
        buf.write("\u01a0\3\2\2\2\u01a0G\3\2\2\2\u01a1\u019f\3\2\2\2\u01a2")
        buf.write("\u01a8\7\17\2\2\u01a3\u01a8\7\20\2\2\u01a4\u01a8\7\21")
        buf.write("\2\2\u01a5\u01a8\7\22\2\2\u01a6\u01a8\5J&\2\u01a7\u01a2")
        buf.write("\3\2\2\2\u01a7\u01a3\3\2\2\2\u01a7\u01a4\3\2\2\2\u01a7")
        buf.write("\u01a5\3\2\2\2\u01a7\u01a6\3\2\2\2\u01a8I\3\2\2\2\u01a9")
        buf.write("\u01aa\7\r\2\2\u01aa\u01ab\7\62\2\2\u01ab\u01ac\5H%\2")
        buf.write("\u01ac\u01ad\7\67\2\2\u01ad\u01ae\7;\2\2\u01ae\u01af\7")
        buf.write("\63\2\2\u01afK\3\2\2\2\u01b0\u01b5\t\5\2\2\u01b1\u01b2")
        buf.write("\7\67\2\2\u01b2\u01b4\t\5\2\2\u01b3\u01b1\3\2\2\2\u01b4")
        buf.write("\u01b7\3\2\2\2\u01b5\u01b3\3\2\2\2\u01b5\u01b6\3\2\2\2")
        buf.write("\u01b6M\3\2\2\2\u01b7\u01b5\3\2\2\2\u01b8\u01b9\t\5\2")
        buf.write("\2\u01b9\u01ba\5P)\2\u01ba\u01bb\5D#\2\u01bb\u01c1\3\2")
        buf.write("\2\2\u01bc\u01bd\5L\'\2\u01bd\u01be\7-\2\2\u01be\u01bf")
        buf.write("\5H%\2\u01bf\u01c1\3\2\2\2\u01c0\u01b8\3\2\2\2\u01c0\u01bc")
        buf.write("\3\2\2\2\u01c1O\3\2\2\2\u01c2\u01c3\7\67\2\2\u01c3\u01c4")
        buf.write("\t\5\2\2\u01c4\u01c5\5P)\2\u01c5\u01c6\5D#\2\u01c6\u01c7")
        buf.write("\7\67\2\2\u01c7\u01cd\3\2\2\2\u01c8\u01c9\7-\2\2\u01c9")
        buf.write("\u01ca\5H%\2\u01ca\u01cb\7.\2\2\u01cb\u01cd\3\2\2\2\u01cc")
        buf.write("\u01c2\3\2\2\2\u01cc\u01c8\3\2\2\2\u01cdQ\3\2\2\2\u01ce")
        buf.write("\u01d0\t\t\2\2\u01cf\u01ce\3\2\2\2\u01cf\u01d0\3\2\2\2")
        buf.write("\u01d0\u01d1\3\2\2\2\u01d1\u01d2\5N(\2\u01d2\u01d3\7\66")
        buf.write("\2\2\u01d3S\3\2\2\2\u01d4\u01d7\7@\2\2\u01d5\u01d7\5D")
        buf.write("#\2\u01d6\u01d4\3\2\2\2\u01d6\u01d5\3\2\2\2\u01d7U\3\2")
        buf.write("\2\2\u01d8\u01d9\5T+\2\u01d9\u01da\7.\2\2\u01da\u01db")
        buf.write("\5D#\2\u01db\u01dc\7\66\2\2\u01dcW\3\2\2\2\u01dd\u01de")
        buf.write("\7\7\2\2\u01de\u01df\7\60\2\2\u01df\u01e0\5D#\2\u01e0")
        buf.write("\u01e4\7\61\2\2\u01e1\u01e3\5\\/\2\u01e2\u01e1\3\2\2\2")
        buf.write("\u01e3\u01e6\3\2\2\2\u01e4\u01e2\3\2\2\2\u01e4\u01e5\3")
        buf.write("\2\2\2\u01e5\u01f3\3\2\2\2\u01e6\u01e4\3\2\2\2\u01e7\u01e8")
        buf.write("\7\b\2\2\u01e8\u01e9\7\60\2\2\u01e9\u01ea\5D#\2\u01ea")
        buf.write("\u01ee\7\61\2\2\u01eb\u01ed\5\\/\2\u01ec\u01eb\3\2\2\2")
        buf.write("\u01ed\u01f0\3\2\2\2\u01ee\u01ec\3\2\2\2\u01ee\u01ef\3")
        buf.write("\2\2\2\u01ef\u01f2\3\2\2\2\u01f0\u01ee\3\2\2\2\u01f1\u01e7")
        buf.write("\3\2\2\2\u01f2\u01f5\3\2\2\2\u01f3\u01f1\3\2\2\2\u01f3")
        buf.write("\u01f4\3\2\2\2\u01f4\u01fd\3\2\2\2\u01f5\u01f3\3\2\2\2")
        buf.write("\u01f6\u01fa\7\t\2\2\u01f7\u01f9\5\\/\2\u01f8\u01f7\3")
        buf.write("\2\2\2\u01f9\u01fc\3\2\2\2\u01fa\u01f8\3\2\2\2\u01fa\u01fb")
        buf.write("\3\2\2\2\u01fb\u01fe\3\2\2\2\u01fc\u01fa\3\2\2\2\u01fd")
        buf.write("\u01f6\3\2\2\2\u01fd\u01fe\3\2\2\2\u01feY\3\2\2\2\u01ff")
        buf.write("\u0200\7\n\2\2\u0200\u0201\7\60\2\2\u0201\u0202\7@\2\2")
        buf.write("\u0202\u0203\7\16\2\2\u0203\u0204\5D#\2\u0204\u0205\7")
        buf.write("\3\2\2\u0205\u0208\5D#\2\u0206\u0207\7\33\2\2\u0207\u0209")
        buf.write("\5D#\2\u0208\u0206\3\2\2\2\u0208\u0209\3\2\2\2\u0209\u020a")
        buf.write("\3\2\2\2\u020a\u020b\7\61\2\2\u020b\u020c\5\\/\2\u020c")
        buf.write("[\3\2\2\2\u020d\u020e\7\64\2\2\u020e\u020f\5h\65\2\u020f")
        buf.write("\u0210\7\65\2\2\u0210]\3\2\2\2\u0211\u0215\5\62\32\2\u0212")
        buf.write("\u0215\5\66\34\2\u0213\u0215\5B\"\2\u0214\u0211\3\2\2")
        buf.write("\2\u0214\u0212\3\2\2\2\u0214\u0213\3\2\2\2\u0215\u0216")
        buf.write("\3\2\2\2\u0216\u0217\7\66\2\2\u0217_\3\2\2\2\u0218\u0219")
        buf.write("\7\6\2\2\u0219\u021a\7\66\2\2\u021aa\3\2\2\2\u021b\u021d")
        buf.write("\7\23\2\2\u021c\u021e\5D#\2\u021d\u021c\3\2\2\2\u021d")
        buf.write("\u021e\3\2\2\2\u021e\u021f\3\2\2\2\u021f\u0220\7\66\2")
        buf.write("\2\u0220c\3\2\2\2\u0221\u0222\7\5\2\2\u0222\u0223\7\66")
        buf.write("\2\2\u0223e\3\2\2\2\u0224\u0230\5R*\2\u0225\u0230\5V,")
        buf.write("\2\u0226\u0230\5X-\2\u0227\u0230\5Z.\2\u0228\u0230\5\\")
        buf.write("/\2\u0229\u0230\5^\60\2\u022a\u0230\5`\61\2\u022b\u0230")
        buf.write("\5b\62\2\u022c\u0230\5d\63\2\u022d\u0230\5n8\2\u022e\u0230")
        buf.write("\5j\66\2\u022f\u0224\3\2\2\2\u022f\u0225\3\2\2\2\u022f")
        buf.write("\u0226\3\2\2\2\u022f\u0227\3\2\2\2\u022f\u0228\3\2\2\2")
        buf.write("\u022f\u0229\3\2\2\2\u022f\u022a\3\2\2\2\u022f\u022b\3")
        buf.write("\2\2\2\u022f\u022c\3\2\2\2\u022f\u022d\3\2\2\2\u022f\u022e")
        buf.write("\3\2\2\2\u0230g\3\2\2\2\u0231\u0233\5f\64\2\u0232\u0231")
        buf.write("\3\2\2\2\u0233\u0236\3\2\2\2\u0234\u0232\3\2\2\2\u0234")
        buf.write("\u0235\3\2\2\2\u0235i\3\2\2\2\u0236\u0234\3\2\2\2\u0237")
        buf.write("\u023a\5p9\2\u0238\u023a\5r:\2\u0239\u0237\3\2\2\2\u0239")
        buf.write("\u0238\3\2\2\2\u023ak\3\2\2\2\u023b\u023c\7\25\2\2\u023c")
        buf.write("\u023f\7@\2\2\u023d\u023e\7-\2\2\u023e\u0240\7@\2\2\u023f")
        buf.write("\u023d\3\2\2\2\u023f\u0240\3\2\2\2\u0240\u0241\3\2\2\2")
        buf.write("\u0241\u0247\7\64\2\2\u0242\u0246\5R*\2\u0243\u0246\5")
        buf.write("n8\2\u0244\u0246\5j\66\2\u0245\u0242\3\2\2\2\u0245\u0243")
        buf.write("\3\2\2\2\u0245\u0244\3\2\2\2\u0246\u0249\3\2\2\2\u0247")
        buf.write("\u0245\3\2\2\2\u0247\u0248\3\2\2\2\u0248\u024a\3\2\2\2")
        buf.write("\u0249\u0247\3\2\2\2\u024a\u024b\7\65\2\2\u024bm\3\2\2")
        buf.write("\2\u024c\u024d\t\5\2\2\u024d\u024f\7\60\2\2\u024e\u0250")
        buf.write("\5t;\2\u024f\u024e\3\2\2\2\u024f\u0250\3\2\2\2\u0250\u0251")
        buf.write("\3\2\2\2\u0251\u0252\7\61\2\2\u0252\u0253\5\\/\2\u0253")
        buf.write("o\3\2\2\2\u0254\u0255\7\30\2\2\u0255\u0257\7\60\2\2\u0256")
        buf.write("\u0258\5t;\2\u0257\u0256\3\2\2\2\u0257\u0258\3\2\2\2\u0258")
        buf.write("\u0259\3\2\2\2\u0259\u025a\7\61\2\2\u025a\u025b\5\\/\2")
        buf.write("\u025bq\3\2\2\2\u025c\u025d\7\31\2\2\u025d\u025e\7\60")
        buf.write("\2\2\u025e\u025f\7\61\2\2\u025f\u0260\5\\/\2\u0260s\3")
        buf.write("\2\2\2\u0261\u0266\5v<\2\u0262\u0263\7\66\2\2\u0263\u0265")
        buf.write("\5v<\2\u0264\u0262\3\2\2\2\u0265\u0268\3\2\2\2\u0266\u0264")
        buf.write("\3\2\2\2\u0266\u0267\3\2\2\2\u0267u\3\2\2\2\u0268\u0266")
        buf.write("\3\2\2\2\u0269\u026a\5L\'\2\u026a\u026b\7-\2\2\u026b\u026c")
        buf.write("\5H%\2\u026cw\3\2\2\2\u026d\u026e\7\r\2\2\u026e\u0277")
        buf.write("\7\60\2\2\u026f\u0274\5z>\2\u0270\u0271\7\67\2\2\u0271")
        buf.write("\u0273\5z>\2\u0272\u0270\3\2\2\2\u0273\u0276\3\2\2\2\u0274")
        buf.write("\u0272\3\2\2\2\u0274\u0275\3\2\2\2\u0275\u0278\3\2\2\2")
        buf.write("\u0276\u0274\3\2\2\2\u0277\u026f\3\2\2\2\u0277\u0278\3")
        buf.write("\2\2\2\u0278\u0279\3\2\2\2\u0279\u027a\7\61\2\2\u027a")
        buf.write("y\3\2\2\2\u027b\u0282\7>\2\2\u027c\u0282\7;\2\2\u027d")
        buf.write("\u0282\7<\2\2\u027e\u0282\7\4\2\2\u027f\u0282\7=\2\2\u0280")
        buf.write("\u0282\5x=\2\u0281\u027b\3\2\2\2\u0281\u027c\3\2\2\2\u0281")
        buf.write("\u027d\3\2\2\2\u0281\u027e\3\2\2\2\u0281\u027f\3\2\2\2")
        buf.write("\u0281\u0280\3\2\2\2\u0282{\3\2\2\2?\177\u008d\u0098\u009e")
        buf.write("\u00ab\u00b8\u00bd\u00c6\u00ca\u00d1\u00da\u00ec\u00fa")
        buf.write("\u00fe\u0102\u0115\u0117\u0123\u012d\u0135\u0143\u0148")
        buf.write("\u0150\u0157\u0165\u0168\u016c\u0171\u0176\u017c\u0183")
        buf.write("\u0187\u018c\u0198\u019f\u01a7\u01b5\u01c0\u01cc\u01cf")
        buf.write("\u01d6\u01e4\u01ee\u01f3\u01fa\u01fd\u0208\u0214\u021d")
        buf.write("\u022f\u0234\u0239\u023f\u0245\u0247\u024f\u0257\u0266")
        buf.write("\u0274\u0277\u0281")
        return buf.getvalue()


class D96Parser ( Parser ):

    grammarFileName = "D96.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'..'", "<INVALID>", "'Break'", "'Continue'", 
                     "'If'", "'Elseif'", "'Else'", "'Foreach'", "'True'", 
                     "'False'", "'Array'", "'In'", "'Int'", "'Float'", "'Boolean'", 
                     "'String'", "'Return'", "'Null'", "'Class'", "'Val'", 
                     "'Var'", "'Constructor'", "'Destructor'", "'New'", 
                     "'By'", "'Self'", "'+'", "'-'", "'*'", "'/'", "'%'", 
                     "'=='", "'!='", "'>'", "'>='", "'<'", "'<='", "'+.'", 
                     "'==.'", "'!'", "'&&'", "'||'", "':'", "'='", "'::'", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'", "';'", "','", 
                     "'.'", "'\"'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "BOOLLIT", "BREAK", "CONTINUE", 
                      "IF", "ELSEIF", "ELSE", "FOREACH", "TRUE", "FALSE", 
                      "ARRAY", "IN", "INT", "FLOAT", "BOOLEAN", "STRING", 
                      "RETURN", "NULL", "CLASS", "VAL", "VAR", "CONSTRUCTOR", 
                      "DESTRUCTOR", "NEW", "BY", "SELF", "ADD", "SUB", "MUL", 
                      "DIV", "MOD", "EQ", "NEQ", "GT", "GTE", "LT", "LTE", 
                      "SADD", "SEQ", "NOT", "AND", "OR", "COLON", "ASSIGN", 
                      "SCOPE", "LB", "RB", "LSB", "RSB", "LCB", "RCB", "SM", 
                      "CM", "DOT", "DOUBLE_QUOTE", "BLOCK_COMMENT", "INTLIT", 
                      "FLOATLIT", "STRLIT", "ZERO", "STATIC_ID", "ID", "WS", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE" ]

    RULE_program = 0
    RULE_exp_IntFloat = 1
    RULE_exp_0 = 2
    RULE_exp_1 = 3
    RULE_exp_2 = 4
    RULE_exp_3 = 5
    RULE_exp_Logical = 6
    RULE_exp_LogicalTerm = 7
    RULE_exp_LogicalNot = 8
    RULE_exp_LogicalNotTerm = 9
    RULE_exp_Bool = 10
    RULE_exp_Str = 11
    RULE_exp_TermStr = 12
    RULE_exp_EqualAndNotEqual = 13
    RULE_exp_TermEQANEQ = 14
    RULE_exp_LessLargeEqual = 15
    RULE_exp_TermLRE = 16
    RULE_exp_RelationalOperation = 17
    RULE_exp_Idx = 18
    RULE_exp_TermIdx = 19
    RULE_idx_Operators = 20
    RULE_exp_InstanceAttributeAccess = 21
    RULE_exp_InstanceAttributeAccessTerm = 22
    RULE_exp_StaticAttributeAccess = 23
    RULE_exp_InstanceMethodInvocation = 24
    RULE_exp_InstanceMethodInvocationTerm = 25
    RULE_exp_StaticMethodInvocation = 26
    RULE_exp_InstanceAttributeMethod = 27
    RULE_exp_InstanceAttributeMethodTerm = 28
    RULE_exp_MemberAccess = 29
    RULE_exp_ObjCreation = 30
    RULE_exp_ClassObject = 31
    RULE_exp_Method = 32
    RULE_expr = 33
    RULE_list_Expr = 34
    RULE_type_Data = 35
    RULE_array_Type = 36
    RULE_seq_ID = 37
    RULE_list_Attribute = 38
    RULE_list_AttributeTerm = 39
    RULE_stmt_AttributeDeclaration = 40
    RULE_lhs = 41
    RULE_stmt_Assign = 42
    RULE_stmt_If = 43
    RULE_stmt_ForIn = 44
    RULE_stmt_Block = 45
    RULE_stmt_MethodInvocation = 46
    RULE_stmt_Continue = 47
    RULE_stmt_Return = 48
    RULE_stmt_Break = 49
    RULE_stmt = 50
    RULE_list_Stmt = 51
    RULE_stmt_ClassMethod = 52
    RULE_stmt_ClassDeclaration = 53
    RULE_stmt_MethodDeclaration = 54
    RULE_class_Construction = 55
    RULE_class_Destruction = 56
    RULE_list_Parameters = 57
    RULE_seq_Parameters = 58
    RULE_lit_Array = 59
    RULE_lit_Data = 60

    ruleNames =  [ "program", "exp_IntFloat", "exp_0", "exp_1", "exp_2", 
                   "exp_3", "exp_Logical", "exp_LogicalTerm", "exp_LogicalNot", 
                   "exp_LogicalNotTerm", "exp_Bool", "exp_Str", "exp_TermStr", 
                   "exp_EqualAndNotEqual", "exp_TermEQANEQ", "exp_LessLargeEqual", 
                   "exp_TermLRE", "exp_RelationalOperation", "exp_Idx", 
                   "exp_TermIdx", "idx_Operators", "exp_InstanceAttributeAccess", 
                   "exp_InstanceAttributeAccessTerm", "exp_StaticAttributeAccess", 
                   "exp_InstanceMethodInvocation", "exp_InstanceMethodInvocationTerm", 
                   "exp_StaticMethodInvocation", "exp_InstanceAttributeMethod", 
                   "exp_InstanceAttributeMethodTerm", "exp_MemberAccess", 
                   "exp_ObjCreation", "exp_ClassObject", "exp_Method", "expr", 
                   "list_Expr", "type_Data", "array_Type", "seq_ID", "list_Attribute", 
                   "list_AttributeTerm", "stmt_AttributeDeclaration", "lhs", 
                   "stmt_Assign", "stmt_If", "stmt_ForIn", "stmt_Block", 
                   "stmt_MethodInvocation", "stmt_Continue", "stmt_Return", 
                   "stmt_Break", "stmt", "list_Stmt", "stmt_ClassMethod", 
                   "stmt_ClassDeclaration", "stmt_MethodDeclaration", "class_Construction", 
                   "class_Destruction", "list_Parameters", "seq_Parameters", 
                   "lit_Array", "lit_Data" ]

    EOF = Token.EOF
    T__0=1
    BOOLLIT=2
    BREAK=3
    CONTINUE=4
    IF=5
    ELSEIF=6
    ELSE=7
    FOREACH=8
    TRUE=9
    FALSE=10
    ARRAY=11
    IN=12
    INT=13
    FLOAT=14
    BOOLEAN=15
    STRING=16
    RETURN=17
    NULL=18
    CLASS=19
    VAL=20
    VAR=21
    CONSTRUCTOR=22
    DESTRUCTOR=23
    NEW=24
    BY=25
    SELF=26
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
    DOUBLE_QUOTE=55
    BLOCK_COMMENT=56
    INTLIT=57
    FLOATLIT=58
    STRLIT=59
    ZERO=60
    STATIC_ID=61
    ID=62
    WS=63
    ERROR_CHAR=64
    UNCLOSE_STRING=65
    ILLEGAL_ESCAPE=66

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
            self.state = 123 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 122
                self.stmt_ClassDeclaration()
                self.state = 125 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==D96Parser.CLASS):
                    break

            self.state = 127
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
            self.state = 129
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
            self.state = 132
            self.exp_1(0)
            self._ctx.stop = self._input.LT(-1)
            self.state = 139
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,1,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp_0Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_0)
                    self.state = 134
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 135
                    _la = self._input.LA(1)
                    if not(_la==D96Parser.ADD or _la==D96Parser.SUB):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 136
                    self.exp_1(0) 
                self.state = 141
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
            self.state = 143
            self.exp_2()
            self._ctx.stop = self._input.LT(-1)
            self.state = 150
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp_1Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_1)
                    self.state = 145
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 146
                    _la = self._input.LA(1)
                    if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.MUL) | (1 << D96Parser.DIV) | (1 << D96Parser.MOD))) != 0)):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 147
                    self.exp_2() 
                self.state = 152
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

        def SUB(self):
            return self.getToken(D96Parser.SUB, 0)

        def exp_2(self):
            return self.getTypedRuleContext(D96Parser.Exp_2Context,0)


        def exp_3(self):
            return self.getTypedRuleContext(D96Parser.Exp_3Context,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp_2




    def exp_2(self):

        localctx = D96Parser.Exp_2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_exp_2)
        try:
            self.state = 156
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.SUB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 153
                self.match(D96Parser.SUB)
                self.state = 154
                self.exp_2()
                pass
            elif token in [D96Parser.NEW, D96Parser.SELF, D96Parser.LB, D96Parser.INTLIT, D96Parser.FLOATLIT, D96Parser.ZERO, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 155
                self.exp_3()
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


    class Exp_3Context(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def ZERO(self):
            return self.getToken(D96Parser.ZERO, 0)

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
            return D96Parser.RULE_exp_3




    def exp_3(self):

        localctx = D96Parser.Exp_3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_exp_3)
        try:
            self.state = 169
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 158
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 159
                self.match(D96Parser.ZERO)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 160
                self.match(D96Parser.INTLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 161
                self.match(D96Parser.FLOATLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 162
                self.exp_MemberAccess()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 163
                self.exp_Method()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 164
                self.exp_Idx()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 165
                self.match(D96Parser.LB)
                self.state = 166
                self.exp_0(0)
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


    class Exp_LogicalContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_LogicalTerm(self):
            return self.getTypedRuleContext(D96Parser.Exp_LogicalTermContext,0)


        def exp_Logical(self):
            return self.getTypedRuleContext(D96Parser.Exp_LogicalContext,0)


        def AND(self):
            return self.getToken(D96Parser.AND, 0)

        def OR(self):
            return self.getToken(D96Parser.OR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp_Logical




    def exp_Logical(self):

        localctx = D96Parser.Exp_LogicalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_exp_Logical)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.exp_LogicalTerm()
            self.state = 172
            _la = self._input.LA(1)
            if not(_la==D96Parser.AND or _la==D96Parser.OR):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 173
            self.exp_Logical()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_LogicalTermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC_ID(self):
            return self.getToken(D96Parser.STATIC_ID, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def BOOLLIT(self):
            return self.getToken(D96Parser.BOOLLIT, 0)

        def exp_MemberAccess(self):
            return self.getTypedRuleContext(D96Parser.Exp_MemberAccessContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp_LogicalTerm(self):
            return self.getTypedRuleContext(D96Parser.Exp_LogicalTermContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp_LogicalTerm




    def exp_LogicalTerm(self):

        localctx = D96Parser.Exp_LogicalTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_exp_LogicalTerm)
        self._la = 0 # Token type
        try:
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 175
                _la = self._input.LA(1)
                if not(_la==D96Parser.STATIC_ID or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 176
                self.match(D96Parser.BOOLLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 177
                self.exp_MemberAccess()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 178
                self.match(D96Parser.LB)
                self.state = 179
                self.exp_LogicalTerm()
                self.state = 180
                self.match(D96Parser.RB)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Exp_LogicalNotContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(D96Parser.NOT, 0)

        def exp_LogicalNot(self):
            return self.getTypedRuleContext(D96Parser.Exp_LogicalNotContext,0)


        def exp_LogicalNotTerm(self):
            return self.getTypedRuleContext(D96Parser.Exp_LogicalNotTermContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp_LogicalNot




    def exp_LogicalNot(self):

        localctx = D96Parser.Exp_LogicalNotContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_exp_LogicalNot)
        try:
            self.state = 187
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NOT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 184
                self.match(D96Parser.NOT)
                self.state = 185
                self.exp_LogicalNot()
                pass
            elif token in [D96Parser.BOOLLIT, D96Parser.NEW, D96Parser.SELF, D96Parser.LB, D96Parser.STATIC_ID, D96Parser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 186
                self.exp_LogicalNotTerm()
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


    class Exp_LogicalNotTermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STATIC_ID(self):
            return self.getToken(D96Parser.STATIC_ID, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def BOOLLIT(self):
            return self.getToken(D96Parser.BOOLLIT, 0)

        def exp_MemberAccess(self):
            return self.getTypedRuleContext(D96Parser.Exp_MemberAccessContext,0)


        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def exp_LogicalNotTerm(self):
            return self.getTypedRuleContext(D96Parser.Exp_LogicalNotTermContext,0)


        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp_LogicalNotTerm




    def exp_LogicalNotTerm(self):

        localctx = D96Parser.Exp_LogicalNotTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_exp_LogicalNotTerm)
        self._la = 0 # Token type
        try:
            self.state = 196
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                _la = self._input.LA(1)
                if not(_la==D96Parser.STATIC_ID or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.match(D96Parser.BOOLLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 191
                self.exp_MemberAccess()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 192
                self.match(D96Parser.LB)
                self.state = 193
                self.exp_LogicalNotTerm()
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


    class Exp_BoolContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp_Logical(self):
            return self.getTypedRuleContext(D96Parser.Exp_LogicalContext,0)


        def exp_LogicalNot(self):
            return self.getTypedRuleContext(D96Parser.Exp_LogicalNotContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp_Bool




    def exp_Bool(self):

        localctx = D96Parser.Exp_BoolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_exp_Bool)
        try:
            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 198
                self.exp_Logical()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.exp_LogicalNot()
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
        self.enterRule(localctx, 22, self.RULE_exp_Str)
        self._la = 0 # Token type
        try:
            self.state = 207
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 202
                self.exp_TermStr()
                self.state = 203
                _la = self._input.LA(1)
                if not(_la==D96Parser.SADD or _la==D96Parser.SEQ):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 204
                self.exp_Str()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 206
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

        def STATIC_ID(self):
            return self.getToken(D96Parser.STATIC_ID, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

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
        self.enterRule(localctx, 24, self.RULE_exp_TermStr)
        self._la = 0 # Token type
        try:
            self.state = 216
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 209
                _la = self._input.LA(1)
                if not(_la==D96Parser.STATIC_ID or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 210
                self.match(D96Parser.STRLIT)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 211
                self.exp_MemberAccess()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 212
                self.match(D96Parser.LB)
                self.state = 213
                self.exp_Str()
                self.state = 214
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
        self.enterRule(localctx, 26, self.RULE_exp_EqualAndNotEqual)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 218
            self.exp_TermEQANEQ()
            self.state = 219
            _la = self._input.LA(1)
            if not(_la==D96Parser.EQ or _la==D96Parser.NEQ):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 220
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

        def ZERO(self):
            return self.getToken(D96Parser.ZERO, 0)

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def BOOLLIT(self):
            return self.getToken(D96Parser.BOOLLIT, 0)

        def STATIC_ID(self):
            return self.getToken(D96Parser.STATIC_ID, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def exp_EqualAndNotEqual(self):
            return self.getTypedRuleContext(D96Parser.Exp_EqualAndNotEqualContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp_TermEQANEQ




    def exp_TermEQANEQ(self):

        localctx = D96Parser.Exp_TermEQANEQContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_exp_TermEQANEQ)
        self._la = 0 # Token type
        try:
            self.state = 234
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 222
                self.match(D96Parser.LB)
                self.state = 223
                self.expr()
                self.state = 224
                self.match(D96Parser.RB)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 226
                self.match(D96Parser.ZERO)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 227
                self.match(D96Parser.INTLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 228
                self.match(D96Parser.BOOLLIT)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 229
                _la = self._input.LA(1)
                if not(_la==D96Parser.STATIC_ID or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 230
                self.match(D96Parser.LB)
                self.state = 231
                self.exp_EqualAndNotEqual()
                self.state = 232
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
        self.enterRule(localctx, 30, self.RULE_exp_LessLargeEqual)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.exp_TermLRE()
            self.state = 237
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.GT) | (1 << D96Parser.GTE) | (1 << D96Parser.LT) | (1 << D96Parser.LTE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 238
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

        def ZERO(self):
            return self.getToken(D96Parser.ZERO, 0)

        def INTLIT(self):
            return self.getToken(D96Parser.INTLIT, 0)

        def FLOATLIT(self):
            return self.getToken(D96Parser.FLOATLIT, 0)

        def STATIC_ID(self):
            return self.getToken(D96Parser.STATIC_ID, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp_TermLRE




    def exp_TermLRE(self):

        localctx = D96Parser.Exp_TermLREContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_exp_TermLRE)
        self._la = 0 # Token type
        try:
            self.state = 248
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 1)
                self.state = 240
                self.match(D96Parser.LB)
                self.state = 241
                self.expr()
                self.state = 242
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.ZERO]:
                self.enterOuterAlt(localctx, 2)
                self.state = 244
                self.match(D96Parser.ZERO)
                pass
            elif token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 245
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 246
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.STATIC_ID, D96Parser.ID]:
                self.enterOuterAlt(localctx, 5)
                self.state = 247
                _la = self._input.LA(1)
                if not(_la==D96Parser.STATIC_ID or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
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
        self.enterRule(localctx, 34, self.RULE_exp_RelationalOperation)
        try:
            self.state = 252
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self.exp_EqualAndNotEqual()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 251
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
        self.enterRule(localctx, 36, self.RULE_exp_Idx)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 254
                self.exp_Method()
                pass

            elif la_ == 2:
                self.state = 255
                self.match(D96Parser.ID)
                pass


            self.state = 258
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
        _startState = 38
        self.enterRecursionRule(localctx, 38, self.RULE_exp_TermIdx, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(D96Parser.LSB)
            self.state = 262
            self.idx_Operators()
            self.state = 263
            self.match(D96Parser.RSB)
            self._ctx.stop = self._input.LT(-1)
            self.state = 277
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,16,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 275
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        localctx = D96Parser.Exp_TermIdxContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_TermIdx)
                        self.state = 265
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 266
                        self.match(D96Parser.LSB)
                        self.state = 267
                        self.idx_Operators()
                        self.state = 268
                        self.match(D96Parser.RSB)
                        pass

                    elif la_ == 2:
                        localctx = D96Parser.Exp_TermIdxContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_TermIdx)
                        self.state = 270
                        if not self.precpred(self._ctx, 1):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                        self.state = 271
                        self.match(D96Parser.LSB)
                        self.state = 272
                        self.exp_Idx()
                        self.state = 273
                        self.match(D96Parser.RSB)
                        pass

             
                self.state = 279
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,16,self._ctx)

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

        def STATIC_ID(self):
            return self.getToken(D96Parser.STATIC_ID, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def ZERO(self):
            return self.getToken(D96Parser.ZERO, 0)

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
        self.enterRule(localctx, 40, self.RULE_idx_Operators)
        self._la = 0 # Token type
        try:
            self.state = 289
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                _la = self._input.LA(1)
                if not(_la==D96Parser.STATIC_ID or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.match(D96Parser.ZERO)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 282
                self.match(D96Parser.INTLIT)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 283
                self.expr()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 284
                self.exp_Idx()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 285
                self.match(D96Parser.LB)
                self.state = 286
                self.exp_Idx()
                self.state = 287
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
        _startState = 42
        self.enterRecursionRule(localctx, 42, self.RULE_exp_InstanceAttributeAccess, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 292
            self.exp_InstanceAttributeAccessTerm()
            self._ctx.stop = self._input.LT(-1)
            self.state = 299
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp_InstanceAttributeAccessContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_InstanceAttributeAccess)
                    self.state = 294
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 295
                    self.match(D96Parser.DOT)
                    self.state = 296
                    self.match(D96Parser.ID) 
                self.state = 301
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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

        def exp_ClassObject(self):
            return self.getTypedRuleContext(D96Parser.Exp_ClassObjectContext,0)


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
        self.enterRule(localctx, 44, self.RULE_exp_InstanceAttributeAccessTerm)
        try:
            self.state = 307
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 302
                self.exp_ClassObject()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 304
                self.match(D96Parser.SELF)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 305
                self.exp_StaticAttributeAccess()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 306
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

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def SCOPE(self):
            return self.getToken(D96Parser.SCOPE, 0)

        def STATIC_ID(self):
            return self.getToken(D96Parser.STATIC_ID, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_exp_StaticAttributeAccess




    def exp_StaticAttributeAccess(self):

        localctx = D96Parser.Exp_StaticAttributeAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_exp_StaticAttributeAccess)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 309
            self.match(D96Parser.ID)
            self.state = 310
            self.match(D96Parser.SCOPE)
            self.state = 311
            self.match(D96Parser.STATIC_ID)
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

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def list_Expr(self):
            return self.getTypedRuleContext(D96Parser.List_ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp_InstanceMethodInvocation



    def exp_InstanceMethodInvocation(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp_InstanceMethodInvocationContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_exp_InstanceMethodInvocation, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 314
            self.exp_InstanceMethodInvocationTerm()
            self._ctx.stop = self._input.LT(-1)
            self.state = 326
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,21,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp_InstanceMethodInvocationContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_InstanceMethodInvocation)
                    self.state = 316
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 317
                    self.match(D96Parser.DOT)
                    self.state = 318
                    self.match(D96Parser.ID)
                    self.state = 319
                    self.match(D96Parser.LB)
                    self.state = 321
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLLIT) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LB) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRLIT) | (1 << D96Parser.ZERO) | (1 << D96Parser.STATIC_ID) | (1 << D96Parser.ID))) != 0):
                        self.state = 320
                        self.list_Expr()


                    self.state = 323
                    self.match(D96Parser.RB) 
                self.state = 328
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

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

        def exp_ClassObject(self):
            return self.getTypedRuleContext(D96Parser.Exp_ClassObjectContext,0)


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
        self.enterRule(localctx, 50, self.RULE_exp_InstanceMethodInvocationTerm)
        try:
            self.state = 334
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 329
                self.exp_ClassObject()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 330
                self.match(D96Parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 331
                self.match(D96Parser.SELF)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 332
                self.exp_StaticAttributeAccess()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 333
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

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def SCOPE(self):
            return self.getToken(D96Parser.SCOPE, 0)

        def STATIC_ID(self):
            return self.getToken(D96Parser.STATIC_ID, 0)

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def list_Expr(self):
            return self.getTypedRuleContext(D96Parser.List_ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp_StaticMethodInvocation




    def exp_StaticMethodInvocation(self):

        localctx = D96Parser.Exp_StaticMethodInvocationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_exp_StaticMethodInvocation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 336
            self.match(D96Parser.ID)
            self.state = 337
            self.match(D96Parser.SCOPE)
            self.state = 338
            self.match(D96Parser.STATIC_ID)
            self.state = 339
            self.match(D96Parser.LB)
            self.state = 341
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLLIT) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LB) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRLIT) | (1 << D96Parser.ZERO) | (1 << D96Parser.STATIC_ID) | (1 << D96Parser.ID))) != 0):
                self.state = 340
                self.list_Expr()


            self.state = 343
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

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def list_Expr(self):
            return self.getTypedRuleContext(D96Parser.List_ExprContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp_InstanceAttributeMethod



    def exp_InstanceAttributeMethod(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = D96Parser.Exp_InstanceAttributeMethodContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 54
        self.enterRecursionRule(localctx, 54, self.RULE_exp_InstanceAttributeMethod, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 346
            self.exp_InstanceAttributeMethodTerm()
            self._ctx.stop = self._input.LT(-1)
            self.state = 362
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = D96Parser.Exp_InstanceAttributeMethodContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_exp_InstanceAttributeMethod)
                    self.state = 348
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 358
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
                    if la_ == 1:
                        self.state = 349
                        self.match(D96Parser.DOT)
                        self.state = 350
                        self.match(D96Parser.ID)
                        pass

                    elif la_ == 2:
                        self.state = 351
                        self.match(D96Parser.DOT)
                        self.state = 352
                        self.match(D96Parser.ID)
                        self.state = 353
                        self.match(D96Parser.LB)
                        self.state = 355
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLLIT) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LB) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRLIT) | (1 << D96Parser.ZERO) | (1 << D96Parser.STATIC_ID) | (1 << D96Parser.ID))) != 0):
                            self.state = 354
                            self.list_Expr()


                        self.state = 357
                        self.match(D96Parser.RB)
                        pass

             
                self.state = 364
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
        self.enterRule(localctx, 56, self.RULE_exp_InstanceAttributeMethodTerm)
        try:
            self.state = 367
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 365
                self.exp_InstanceAttributeAccess(0)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 366
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

        def exp_StaticMethodInvocation(self):
            return self.getTypedRuleContext(D96Parser.Exp_StaticMethodInvocationContext,0)


        def exp_StaticAttributeAccess(self):
            return self.getTypedRuleContext(D96Parser.Exp_StaticAttributeAccessContext,0)


        def exp_InstanceAttributeMethod(self):
            return self.getTypedRuleContext(D96Parser.Exp_InstanceAttributeMethodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp_MemberAccess




    def exp_MemberAccess(self):

        localctx = D96Parser.Exp_MemberAccessContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_exp_MemberAccess)
        try:
            self.state = 372
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 369
                self.exp_StaticMethodInvocation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 370
                self.exp_StaticAttributeAccess()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 371
                self.exp_InstanceAttributeMethod(0)
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

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def list_Expr(self):
            return self.getTypedRuleContext(D96Parser.List_ExprContext,0)


        def exp_ObjCreation(self):
            return self.getTypedRuleContext(D96Parser.Exp_ObjCreationContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_exp_ObjCreation




    def exp_ObjCreation(self):

        localctx = D96Parser.Exp_ObjCreationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_exp_ObjCreation)
        self._la = 0 # Token type
        try:
            self.state = 385
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.NEW]:
                self.enterOuterAlt(localctx, 1)
                self.state = 374
                self.match(D96Parser.NEW)
                self.state = 375
                self.match(D96Parser.ID)
                self.state = 376
                self.match(D96Parser.LB)
                self.state = 378
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLLIT) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LB) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRLIT) | (1 << D96Parser.ZERO) | (1 << D96Parser.STATIC_ID) | (1 << D96Parser.ID))) != 0):
                    self.state = 377
                    self.list_Expr()


                self.state = 380
                self.match(D96Parser.RB)
                pass
            elif token in [D96Parser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 381
                self.match(D96Parser.LB)
                self.state = 382
                self.exp_ObjCreation()
                self.state = 383
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
        self.enterRule(localctx, 62, self.RULE_exp_ClassObject)
        try:
            self.state = 389
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 387
                self.match(D96Parser.ID)
                pass
            elif token in [D96Parser.NEW, D96Parser.LB]:
                self.enterOuterAlt(localctx, 2)
                self.state = 388
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
        self.enterRule(localctx, 64, self.RULE_exp_Method)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(D96Parser.ID)
            self.state = 392
            self.match(D96Parser.LB)
            self.state = 394
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLLIT) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LB) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRLIT) | (1 << D96Parser.ZERO) | (1 << D96Parser.STATIC_ID) | (1 << D96Parser.ID))) != 0):
                self.state = 393
                self.list_Expr()


            self.state = 396
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


        def lit_Data(self):
            return self.getTypedRuleContext(D96Parser.Lit_DataContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_expr




    def expr(self):

        localctx = D96Parser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_expr)
        try:
            self.state = 406
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 398
                self.exp_ObjCreation()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 399
                self.exp_MemberAccess()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 400
                self.exp_IntFloat()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 401
                self.exp_Bool()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 402
                self.exp_Str()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 403
                self.exp_Idx()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 404
                self.exp_RelationalOperation()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 405
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
        self.enterRule(localctx, 68, self.RULE_list_Expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 408
            self.expr()
            self.state = 413
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 409
                self.match(D96Parser.CM)
                self.state = 410
                self.expr()
                self.state = 415
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
        self.enterRule(localctx, 70, self.RULE_type_Data)
        try:
            self.state = 421
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.INT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 416
                self.match(D96Parser.INT)
                pass
            elif token in [D96Parser.FLOAT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 417
                self.match(D96Parser.FLOAT)
                pass
            elif token in [D96Parser.BOOLEAN]:
                self.enterOuterAlt(localctx, 3)
                self.state = 418
                self.match(D96Parser.BOOLEAN)
                pass
            elif token in [D96Parser.STRING]:
                self.enterOuterAlt(localctx, 4)
                self.state = 419
                self.match(D96Parser.STRING)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 5)
                self.state = 420
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
        self.enterRule(localctx, 72, self.RULE_array_Type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 423
            self.match(D96Parser.ARRAY)
            self.state = 424
            self.match(D96Parser.LSB)
            self.state = 425
            self.type_Data()
            self.state = 426
            self.match(D96Parser.CM)
            self.state = 427
            self.match(D96Parser.INTLIT)
            self.state = 428
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

        def STATIC_ID(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.STATIC_ID)
            else:
                return self.getToken(D96Parser.STATIC_ID, i)

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
        self.enterRule(localctx, 74, self.RULE_seq_ID)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 430
            _la = self._input.LA(1)
            if not(_la==D96Parser.STATIC_ID or _la==D96Parser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 435
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.CM:
                self.state = 431
                self.match(D96Parser.CM)
                self.state = 432
                _la = self._input.LA(1)
                if not(_la==D96Parser.STATIC_ID or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 437
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_AttributeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_AttributeTerm(self):
            return self.getTypedRuleContext(D96Parser.List_AttributeTermContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def STATIC_ID(self):
            return self.getToken(D96Parser.STATIC_ID, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def seq_ID(self):
            return self.getTypedRuleContext(D96Parser.Seq_IDContext,0)


        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def type_Data(self):
            return self.getTypedRuleContext(D96Parser.Type_DataContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_list_Attribute




    def list_Attribute(self):

        localctx = D96Parser.List_AttributeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_list_Attribute)
        self._la = 0 # Token type
        try:
            self.state = 446
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 438
                _la = self._input.LA(1)
                if not(_la==D96Parser.STATIC_ID or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 439
                self.list_AttributeTerm()
                self.state = 440
                self.expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 442
                self.seq_ID()
                self.state = 443
                self.match(D96Parser.COLON)
                self.state = 444
                self.type_Data()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_AttributeTermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CM(self, i:int=None):
            if i is None:
                return self.getTokens(D96Parser.CM)
            else:
                return self.getToken(D96Parser.CM, i)

        def list_AttributeTerm(self):
            return self.getTypedRuleContext(D96Parser.List_AttributeTermContext,0)


        def expr(self):
            return self.getTypedRuleContext(D96Parser.ExprContext,0)


        def STATIC_ID(self):
            return self.getToken(D96Parser.STATIC_ID, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def COLON(self):
            return self.getToken(D96Parser.COLON, 0)

        def type_Data(self):
            return self.getTypedRuleContext(D96Parser.Type_DataContext,0)


        def ASSIGN(self):
            return self.getToken(D96Parser.ASSIGN, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_list_AttributeTerm




    def list_AttributeTerm(self):

        localctx = D96Parser.List_AttributeTermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_list_AttributeTerm)
        self._la = 0 # Token type
        try:
            self.state = 458
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CM]:
                self.enterOuterAlt(localctx, 1)
                self.state = 448
                self.match(D96Parser.CM)
                self.state = 449
                _la = self._input.LA(1)
                if not(_la==D96Parser.STATIC_ID or _la==D96Parser.ID):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 450
                self.list_AttributeTerm()
                self.state = 451
                self.expr()
                self.state = 452
                self.match(D96Parser.CM)
                pass
            elif token in [D96Parser.COLON]:
                self.enterOuterAlt(localctx, 2)
                self.state = 454
                self.match(D96Parser.COLON)
                self.state = 455
                self.type_Data()
                self.state = 456
                self.match(D96Parser.ASSIGN)
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


    class Stmt_AttributeDeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def list_Attribute(self):
            return self.getTypedRuleContext(D96Parser.List_AttributeContext,0)


        def SM(self):
            return self.getToken(D96Parser.SM, 0)

        def VAL(self):
            return self.getToken(D96Parser.VAL, 0)

        def VAR(self):
            return self.getToken(D96Parser.VAR, 0)

        def getRuleIndex(self):
            return D96Parser.RULE_stmt_AttributeDeclaration




    def stmt_AttributeDeclaration(self):

        localctx = D96Parser.Stmt_AttributeDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_stmt_AttributeDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 461
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.VAL or _la==D96Parser.VAR:
                self.state = 460
                _la = self._input.LA(1)
                if not(_la==D96Parser.VAL or _la==D96Parser.VAR):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


            self.state = 463
            self.list_Attribute()
            self.state = 464
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
        self.enterRule(localctx, 82, self.RULE_lhs)
        try:
            self.state = 468
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,40,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 466
                self.match(D96Parser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 467
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
        self.enterRule(localctx, 84, self.RULE_stmt_Assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 470
            self.lhs()
            self.state = 471
            self.match(D96Parser.ASSIGN)
            self.state = 472
            self.expr()
            self.state = 473
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
        self.enterRule(localctx, 86, self.RULE_stmt_If)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 475
            self.match(D96Parser.IF)
            self.state = 476
            self.match(D96Parser.LB)
            self.state = 477
            self.expr()
            self.state = 478
            self.match(D96Parser.RB)
            self.state = 482
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,41,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 479
                    self.stmt_Block() 
                self.state = 484
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,41,self._ctx)

            self.state = 497
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.ELSEIF:
                self.state = 485
                self.match(D96Parser.ELSEIF)
                self.state = 486
                self.match(D96Parser.LB)
                self.state = 487
                self.expr()
                self.state = 488
                self.match(D96Parser.RB)
                self.state = 492
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,42,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 489
                        self.stmt_Block() 
                    self.state = 494
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,42,self._ctx)

                self.state = 499
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 507
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.ELSE:
                self.state = 500
                self.match(D96Parser.ELSE)
                self.state = 504
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,44,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 501
                        self.stmt_Block() 
                    self.state = 506
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
        self.enterRule(localctx, 88, self.RULE_stmt_ForIn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 509
            self.match(D96Parser.FOREACH)
            self.state = 510
            self.match(D96Parser.LB)
            self.state = 511
            self.match(D96Parser.ID)
            self.state = 512
            self.match(D96Parser.IN)
            self.state = 513
            self.expr()
            self.state = 514
            self.match(D96Parser.T__0)
            self.state = 515
            self.expr()
            self.state = 518
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.BY:
                self.state = 516
                self.match(D96Parser.BY)
                self.state = 517
                self.expr()


            self.state = 520
            self.match(D96Parser.RB)
            self.state = 521
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
        self.enterRule(localctx, 90, self.RULE_stmt_Block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 523
            self.match(D96Parser.LCB)

            self.state = 524
            self.list_Stmt()
            self.state = 525
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
        self.enterRule(localctx, 92, self.RULE_stmt_MethodInvocation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 530
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,47,self._ctx)
            if la_ == 1:
                self.state = 527
                self.exp_InstanceMethodInvocation(0)
                pass

            elif la_ == 2:
                self.state = 528
                self.exp_StaticMethodInvocation()
                pass

            elif la_ == 3:
                self.state = 529
                self.exp_Method()
                pass


            self.state = 532
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
        self.enterRule(localctx, 94, self.RULE_stmt_Continue)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 534
            self.match(D96Parser.CONTINUE)
            self.state = 535
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
        self.enterRule(localctx, 96, self.RULE_stmt_Return)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 537
            self.match(D96Parser.RETURN)
            self.state = 539
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLLIT) | (1 << D96Parser.ARRAY) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LB) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRLIT) | (1 << D96Parser.ZERO) | (1 << D96Parser.STATIC_ID) | (1 << D96Parser.ID))) != 0):
                self.state = 538
                self.expr()


            self.state = 541
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
        self.enterRule(localctx, 98, self.RULE_stmt_Break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 543
            self.match(D96Parser.BREAK)
            self.state = 544
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

        def stmt_AttributeDeclaration(self):
            return self.getTypedRuleContext(D96Parser.Stmt_AttributeDeclarationContext,0)


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


        def stmt_ClassMethod(self):
            return self.getTypedRuleContext(D96Parser.Stmt_ClassMethodContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt




    def stmt(self):

        localctx = D96Parser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 100, self.RULE_stmt)
        try:
            self.state = 557
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,49,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 546
                self.stmt_AttributeDeclaration()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 547
                self.stmt_Assign()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 548
                self.stmt_If()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 549
                self.stmt_ForIn()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 550
                self.stmt_Block()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 551
                self.stmt_MethodInvocation()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 552
                self.stmt_Continue()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 553
                self.stmt_Return()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 554
                self.stmt_Break()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 555
                self.stmt_MethodDeclaration()
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 556
                self.stmt_ClassMethod()
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
        self.enterRule(localctx, 102, self.RULE_list_Stmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 562
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLLIT) | (1 << D96Parser.BREAK) | (1 << D96Parser.CONTINUE) | (1 << D96Parser.IF) | (1 << D96Parser.FOREACH) | (1 << D96Parser.ARRAY) | (1 << D96Parser.RETURN) | (1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.NEW) | (1 << D96Parser.SELF) | (1 << D96Parser.SUB) | (1 << D96Parser.NOT) | (1 << D96Parser.LB) | (1 << D96Parser.LCB) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRLIT) | (1 << D96Parser.ZERO) | (1 << D96Parser.STATIC_ID) | (1 << D96Parser.ID))) != 0):
                self.state = 559
                self.stmt()
                self.state = 564
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stmt_ClassMethodContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def class_Construction(self):
            return self.getTypedRuleContext(D96Parser.Class_ConstructionContext,0)


        def class_Destruction(self):
            return self.getTypedRuleContext(D96Parser.Class_DestructionContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt_ClassMethod




    def stmt_ClassMethod(self):

        localctx = D96Parser.Stmt_ClassMethodContext(self, self._ctx, self.state)
        self.enterRule(localctx, 104, self.RULE_stmt_ClassMethod)
        try:
            self.state = 567
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.CONSTRUCTOR]:
                self.enterOuterAlt(localctx, 1)
                self.state = 565
                self.class_Construction()
                pass
            elif token in [D96Parser.DESTRUCTOR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 566
                self.class_Destruction()
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

        def stmt_AttributeDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Stmt_AttributeDeclarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.Stmt_AttributeDeclarationContext,i)


        def stmt_MethodDeclaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Stmt_MethodDeclarationContext)
            else:
                return self.getTypedRuleContext(D96Parser.Stmt_MethodDeclarationContext,i)


        def stmt_ClassMethod(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(D96Parser.Stmt_ClassMethodContext)
            else:
                return self.getTypedRuleContext(D96Parser.Stmt_ClassMethodContext,i)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt_ClassDeclaration




    def stmt_ClassDeclaration(self):

        localctx = D96Parser.Stmt_ClassDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 106, self.RULE_stmt_ClassDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 569
            self.match(D96Parser.CLASS)
            self.state = 570
            self.match(D96Parser.ID)
            self.state = 573
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.COLON:
                self.state = 571
                self.match(D96Parser.COLON)
                self.state = 572
                self.match(D96Parser.ID)


            self.state = 575
            self.match(D96Parser.LCB)
            self.state = 581
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.VAL) | (1 << D96Parser.VAR) | (1 << D96Parser.CONSTRUCTOR) | (1 << D96Parser.DESTRUCTOR) | (1 << D96Parser.STATIC_ID) | (1 << D96Parser.ID))) != 0):
                self.state = 579
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,53,self._ctx)
                if la_ == 1:
                    self.state = 576
                    self.stmt_AttributeDeclaration()
                    pass

                elif la_ == 2:
                    self.state = 577
                    self.stmt_MethodDeclaration()
                    pass

                elif la_ == 3:
                    self.state = 578
                    self.stmt_ClassMethod()
                    pass


                self.state = 583
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 584
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

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def stmt_Block(self):
            return self.getTypedRuleContext(D96Parser.Stmt_BlockContext,0)


        def STATIC_ID(self):
            return self.getToken(D96Parser.STATIC_ID, 0)

        def ID(self):
            return self.getToken(D96Parser.ID, 0)

        def list_Parameters(self):
            return self.getTypedRuleContext(D96Parser.List_ParametersContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_stmt_MethodDeclaration




    def stmt_MethodDeclaration(self):

        localctx = D96Parser.Stmt_MethodDeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 108, self.RULE_stmt_MethodDeclaration)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 586
            _la = self._input.LA(1)
            if not(_la==D96Parser.STATIC_ID or _la==D96Parser.ID):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 587
            self.match(D96Parser.LB)
            self.state = 589
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.STATIC_ID or _la==D96Parser.ID:
                self.state = 588
                self.list_Parameters()


            self.state = 591
            self.match(D96Parser.RB)
            self.state = 592
            self.stmt_Block()
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
        self.enterRule(localctx, 110, self.RULE_class_Construction)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 594
            self.match(D96Parser.CONSTRUCTOR)
            self.state = 595
            self.match(D96Parser.LB)
            self.state = 597
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==D96Parser.STATIC_ID or _la==D96Parser.ID:
                self.state = 596
                self.list_Parameters()


            self.state = 599
            self.match(D96Parser.RB)
            self.state = 600
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

        def LB(self):
            return self.getToken(D96Parser.LB, 0)

        def RB(self):
            return self.getToken(D96Parser.RB, 0)

        def stmt_Block(self):
            return self.getTypedRuleContext(D96Parser.Stmt_BlockContext,0)


        def getRuleIndex(self):
            return D96Parser.RULE_class_Destruction




    def class_Destruction(self):

        localctx = D96Parser.Class_DestructionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 112, self.RULE_class_Destruction)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 602
            self.match(D96Parser.DESTRUCTOR)
            self.state = 603
            self.match(D96Parser.LB)
            self.state = 604
            self.match(D96Parser.RB)
            self.state = 605
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
        self.enterRule(localctx, 114, self.RULE_list_Parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 607
            self.seq_Parameters()
            self.state = 612
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==D96Parser.SM:
                self.state = 608
                self.match(D96Parser.SM)
                self.state = 609
                self.seq_Parameters()
                self.state = 614
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
        self.enterRule(localctx, 116, self.RULE_seq_Parameters)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 615
            self.seq_ID()
            self.state = 616
            self.match(D96Parser.COLON)
            self.state = 617
            self.type_Data()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lit_ArrayContext(ParserRuleContext):

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




    def lit_Array(self):

        localctx = D96Parser.Lit_ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 118, self.RULE_lit_Array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 619
            self.match(D96Parser.ARRAY)
            self.state = 620
            self.match(D96Parser.LB)
            self.state = 629
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << D96Parser.BOOLLIT) | (1 << D96Parser.ARRAY) | (1 << D96Parser.INTLIT) | (1 << D96Parser.FLOATLIT) | (1 << D96Parser.STRLIT) | (1 << D96Parser.ZERO))) != 0):
                self.state = 621
                self.lit_Data()
                self.state = 626
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==D96Parser.CM:
                    self.state = 622
                    self.match(D96Parser.CM)
                    self.state = 623
                    self.lit_Data()
                    self.state = 628
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 631
            self.match(D96Parser.RB)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Lit_DataContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ZERO(self):
            return self.getToken(D96Parser.ZERO, 0)

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




    def lit_Data(self):

        localctx = D96Parser.Lit_DataContext(self, self._ctx, self.state)
        self.enterRule(localctx, 120, self.RULE_lit_Data)
        try:
            self.state = 639
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [D96Parser.ZERO]:
                self.enterOuterAlt(localctx, 1)
                self.state = 633
                self.match(D96Parser.ZERO)
                pass
            elif token in [D96Parser.INTLIT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 634
                self.match(D96Parser.INTLIT)
                pass
            elif token in [D96Parser.FLOATLIT]:
                self.enterOuterAlt(localctx, 3)
                self.state = 635
                self.match(D96Parser.FLOATLIT)
                pass
            elif token in [D96Parser.BOOLLIT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 636
                self.match(D96Parser.BOOLLIT)
                pass
            elif token in [D96Parser.STRLIT]:
                self.enterOuterAlt(localctx, 5)
                self.state = 637
                self.match(D96Parser.STRLIT)
                pass
            elif token in [D96Parser.ARRAY]:
                self.enterOuterAlt(localctx, 6)
                self.state = 638
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
        self._predicates[19] = self.exp_TermIdx_sempred
        self._predicates[21] = self.exp_InstanceAttributeAccess_sempred
        self._predicates[24] = self.exp_InstanceMethodInvocation_sempred
        self._predicates[27] = self.exp_InstanceAttributeMethod_sempred
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
         




