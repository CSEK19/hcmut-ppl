import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
    def test_0(self):
        input = '''Class m:Z{Val _,$8,__,$5,y:g;}Class _{Var $c_:Array[Array[Float,3],9_84_0_5];}Class _:z7m{}Class _:H5{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 0))

    def test_1(self):
        input = '''Class __{Constructor(l:Array[Array[Int,0X8],06_7]){ {} }}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 1))

    def test_2(self):
        input = '''Class J{Val $8:Array[Array[Int,016],0x83];Constructor(_,Q,_:Array[String,0b10100];_:Dt9_896){Break;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 2))

    def test_3(self):
        input = '''Class L__:_q{Constructor(){}_6(N:Array[Array[Array[Array[Int,0xC],0x12_0],95],0x60]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 3))

    def test_4(self):
        input = '''Class Z{}Class s{}Class _a1M:zDd{Constructor(){Continue;}Val $_1K_:Array[Float,1];}Class l{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 4))

    def test_5(self):
        input = '''Class Ri{Var $m_,R,_:Int;Constructor(){}Destructor(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 5))

    def test_6(self):
        input = '''Class w:wp_{Var $__:String;$__L(){} }Class _v_{}Class _:_f_a{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 6))

    def test_7(self):
        input = '''Class NUU7_h:O{}Class I8__:__{}Class y_{Constructor(){} }Class W{Destructor(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 7))

    def test_8(self):
        input = '''Class E:_{Val $m,$T,_,$_:Array[Array[Array[Array[Array[Boolean,0132],0132],03553_2_7_4],8],0132];Destructor(){Val __:Array[Boolean,016];} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 8))

    def test_9(self):
        input = '''Class __:P{Constructor(a:_;_,_s,y,F,_,_a36,_:Array[Int,81]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 9))

    def test_10(self):
        input = '''Class H:__{}Class _{Destructor(){Var _9v_8,X,__,_,_4_:Array[Array[Array[String,0B1011],0XE_3],1];}$f(){} }Class v:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 10))

    def test_11(self):
        input = '''Class _V{Constructor(){}Constructor(w:Boolean;S,__:Array[Array[Array[Array[String,0B1_0],0X7],17],8];P_,L3:Int;qK_,_,__5_,n,V,hV,__8:X;_,p:Array[Array[Array[Array[String,0B100],0B100],54],0B1]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 11))

    def test_12(self):
        input = '''Class x{Val $_:Array[Array[Boolean,06],0130];Destructor(){} }Class _{Destructor(){}Constructor(xQ,a_:pM_1;_T,__,_E,_h_c,_,t:Array[Array[Array[Boolean,82],0xA],7];JgO:Array[Float,82]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 12))

    def test_13(self):
        input = '''Class U:_{}Class z{}Class _:U{}Class _88__9tY{Var g:Array[Array[Array[Boolean,0x8_342],0B11100],0122];}Class _:n2{}Class __d:___{}Class _:x4{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 13))

    def test_14(self):
        input = '''Class _{_(_:t;_:Array[String,034_5];l,sa,o_:YZP_){ {} }_(){Return;}R(){}Destructor(){}Var $4:__;}Class __Xq{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 14))

    def test_15(self):
        input = '''Class g{Constructor(x:Array[Int,5_5_99]){} }Class __o4{}Class _5__:o{_c__(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 15))

    def test_16(self):
        input = '''Class _7{Val C:Float;}Class tE5:_{$_m1(){Return;Continue;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 16))

    def test_17(self):
        input = '''Class A:w{}Class __{Destructor(){}Var ze4:_0;}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 17))

    def test_18(self):
        input = '''Class _3:__GT{}Class P_{}Class gk_:_7Q_T{Var P_zVE2___15,$V___:Array[Array[Array[Array[Boolean,43],84],0x5],030];}Class u{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 18))

    def test_19(self):
        input = '''Class f:__W{}Class O:_{}Class _c2:W{Constructor(_2_J1F:Float;_,_,_:Array[Array[Float,0X1D],0x4]){}Val $0_TY8x,$_7A_,$d_,$4d_c,LOo__,$0W_,$19Up_:Float;Var $S4:Boolean;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 19))

    def test_20(self):
        input = '''Class _{Constructor(){Break;} }Class __{}Class _{Var $W,$__d_K:_e;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 20))

    def test_21(self):
        input = '''Class kc_:mu_{}Class m:F{Var _5:_7_;}Class _{}Class C:gI{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 21))

    def test_22(self):
        input = '''Class _:_{Var C:Int;Var d:Array[String,01];Constructor(V2:Array[Int,0X23];a8:Int;_A:_j;G,T:_4;hd,_:t_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 22))

    def test_23(self):
        input = '''Class B_5:T3{Var L:_A;m(z:Array[Array[String,0B100010],054]){} }Class R{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 23))

    def test_24(self):
        input = '''Class _58o_W{}Class _2:Q_{Destructor(){} }Class _3__Fq_8q:T{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 24))

    def test_25(self):
        input = '''Class _:H{_(){} }Class l{Constructor(B1,_:Int;t,Q:Array[Float,0b1011000]){} }Class B{Destructor(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 25))

    def test_26(self):
        input = '''Class _:On1K9{Constructor(){} }Class E_9O1{$6(){}Constructor(){}_(){Continue;} }Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 26))

    def test_27(self):
        input = '''Class u3{}Class s{Val B7,$_,_,$__,b,_6,_b,$_:_p5__;Var _,_A,$33,$B:_;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 27))

    def test_28(self):
        input = '''Class s:P{Constructor(i:Array[Array[Boolean,05],0x17];u:Array[Array[Array[Array[Array[Array[Array[Array[String,073],0b100_0],8],7],0x17],78],0X2_F],05_2_53];g,H:Array[String,3_0]){}Val E:Array[Boolean,0X35];Destructor(){Var H,_,f:o;} }Class _:_w{Var _3fK:O9_;Destructor(){}Var _,$V,$Fd:O81;}Class j__:q9{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 28))

    def test_29(self):
        input = '''Class C{$_45(hQ___2T5,_C0,_,__,_:_0_9_;V3s,fwU:Array[Array[String,0b1001],01]){Break;}$__(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 29))

    def test_30(self):
        input = '''Class z{Constructor(_:Array[String,4];_:Array[String,0B10_11]){} }Class e:_h{Constructor(_2_k_J,__:Boolean;_:M){}Destructor(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 30))

    def test_31(self):
        input = '''Class K8:t{}Class _7k8{Val $S,b_:o5BYD;}Class v9_Z:Lr{Var $9:s;}Class uG{}Class w{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 31))

    def test_32(self):
        input = '''Class n{}Class _{}Class q{}Class _B:T1_K{Val __k:Array[String,0B1_1];}Class _c{Constructor(){ {}{} }Constructor(_:String){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 32))

    def test_33(self):
        input = '''Class _u_v{}Class B_:q_9{}Class _:_{Constructor(_1,n416:A){}_(){} }Class _Y0{Var $w:Int;$niG(u:Float;q:Array[String,0x11]){}Val $Q9qe_P6_3:Array[Array[Array[String,0b1],42],0x1];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 33))

    def test_34(self):
        input = '''Class TK:_{Constructor(){Continue;Continue;Return;Continue;}Var _:__;Val _I,$t3Z,$7o,$_4_u:Array[Array[Array[Float,0B1_11],06],0x1];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 34))

    def test_35(self):
        input = '''Class B:_6_x{Var N:Array[Array[Int,03],06];Val $_C8A_:Array[Array[String,67],03];Val $W_V:Array[String,66_5];}Class Um{Destructor(){Break;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 35))

    def test_36(self):
        input = '''Class _{}Class W{}Class rK_{Destructor(){} }Class _P:___{_(_,f,Rw:String;_:g){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 36))

    def test_37(self):
        input = '''Class Hr:a{}Class W:c{}Class _a2T_j__:Mzt{}Class _{}Class _7_{Val _,_:String;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 37))

    def test_38(self):
        input = '''Class R_4H:__{Val ___:Array[Array[Float,9],0B1010110];}Class _7{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 38))

    def test_39(self):
        input = '''Class _{$_W_(B___6,_,__y,P,_P,__,_,J1,_,Ep3_,B:Array[Array[Array[Boolean,78],0b1010101],836]){Return;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 39))

    def test_40(self):
        input = '''Class Iqi_5:__9{Var _,$W:Array[Array[String,02],0b100001];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 40))

    def test_41(self):
        input = '''Class _{Val $JH,$Xd:Array[String,050];}Class Y1_{Val $4,_020J_:String;}Class xN:Hb___6{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 41))

    def test_42(self):
        input = '''Class _t{Destructor(){} }Class _{}Class T_i:__F{Val bi4_87,$_5,__:Array[Array[Array[String,04],0B110011],0B110011];}Class _:_____0_{}Class _{}Class _:a_{}Class _:_{Destructor(){ {} }}Class _S{I(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 42))

    def test_43(self):
        input = '''Class q_234{Var _:_A0_i_;Constructor(T3:Array[Int,06]){} }Class M{Val _,$_:Array[Array[Array[String,89],0X4D],030];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 43))

    def test_44(self):
        input = '''Class K_9:___{}Class _p2{_(_:Array[Array[Array[String,0X5D],0X5D],0B1110];ET:Array[Array[Array[Float,0x29],0b100011],0b100011];Wb45:Array[Array[Array[Array[Array[Float,0X5D],07],0b1],0x29],045];I:String){Break;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 44))

    def test_45(self):
        input = '''Class _DN{$_(){Continue;} }Class w{Destructor(){}Val $0,$O,$544_8:g;Var _:Boolean;Var _:String;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 45))

    def test_46(self):
        input = '''Class _:__{Var _,$b_,$PO8,W,N,_8e,$_2,$J:String;}Class D{}Class L_{}Class kw__{Destructor(){Break;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 46))

    def test_47(self):
        input = '''Class ___:d{O(_6,__,_:String){ {N3::$_()._().l();}Break;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 47))

    def test_48(self):
        input = '''Class J_{}Class qm5Ng7Ng:_M{Constructor(__t:Boolean){_::$1().w_U();} }Class xD{Var $6x8,s_D9,e__0z2,_12,N_,$W0H_:Array[Array[Array[Int,0X1D],07_7],057];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 48))

    def test_49(self):
        input = '''Class _{Var $_T:Array[Float,80];}Class ___:a84_{}Class _{}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 49))

    def test_50(self):
        input = '''Class _p:_{}Class _m1u_:_{Destructor(){} }Class F{}Class _6:_I62{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 50))

    def test_51(self):
        input = '''Class _1:wb7{Var IcP:Array[Array[Float,10],0x1C];Var $4,_88:Array[String,0XC];}Class X{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 51))

    def test_52(self):
        input = '''Class Q{}Class _:_05_{Var J:Array[Array[Array[String,0X61],0x9C],0X61];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 52))

    def test_53(self):
        input = '''Class _1:w5U1WB{Var $4,$q,_7,b_u_:Int;Val $__:Array[Array[Boolean,0144],070];}Class t4z:_{}Class _:F3{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 53))

    def test_54(self):
        input = '''Class __:_8{}Class V{}Class x___{Destructor(){} }Class _n_4_{$N(){} }Class _5_{_6(){}Var _8i7_:Boolean;$_(H__2:gd4;_:Int;_n_,X:_){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 54))

    def test_55(self):
        input = '''Class _{Val $9,$J,L_,$4__0:Array[Array[String,7_8_5],6];Val $_K,$A__,_,_9:Array[Array[Float,0b1011001],0x39];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 55))

    def test_56(self):
        input = '''Class H{Constructor(_,V6_:Array[Array[Array[String,0X3],0x3],0b1]){Continue;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 56))

    def test_57(self):
        input = '''Class sn4n{}Class _{Destructor(){Val h:Array[Float,0B10];} }Class _5q_:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 57))

    def test_58(self):
        input = '''Class j__3t{$5_(_,J_,_6_:_x;__u:Array[Boolean,0X47]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 58))

    def test_59(self):
        input = '''Class _{Val n_,$_:Array[Boolean,0xDF_8_2_0_1_EA_AC];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 59))

    def test_60(self):
        input = '''Class _st{}Class I{}Class _f:fr{Destructor(){Break;Return;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 60))

    def test_61(self):
        input = '''Class Q_{Constructor(T:String){}Val _3,$m,$D3,$s:I;}Class __L:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 61))

    def test_62(self):
        input = '''Class E:z8x3_8y{}Class i{_(R,Z:Array[Float,0XD]){Return;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 62))

    def test_63(self):
        input = '''Class __{$U(){}Destructor(){Break;} }Class _b9:_{}Class ___{}Class __:x_{Constructor(e:Array[Array[Float,0XF],0X3A]){} }Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 63))

    def test_64(self):
        input = '''Class _:_T{}Class __:_{Var k_d_,$3h,$8,q:Array[Array[Boolean,0X3],03];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 64))

    def test_65(self):
        input = '''Class q:x{Constructor(W_354,y,X,_0:Array[Array[Float,79],8];C:Array[Int,0B1];D,_:Array[Array[Array[Int,0X10],0x4_4_8],0X4_B_BA_0];_:String;_V7,__:Boolean){Return;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 65))

    def test_66(self):
        input = '''Class s:_{Val $w_:Array[Array[Array[Array[Boolean,0X5],0xA_F],4_9],47];Var $4,$_:js;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 66))

    def test_67(self):
        input = '''Class A5{Constructor(){} }Class _:_y_{Var _1F,_:String;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 67))

    def test_68(self):
        input = '''Class _{}Class __F:_b{Var $L,$7_78:Int;Constructor(_4_:Array[String,05];_1:Int){}$_(_,_L:K;e:Array[Boolean,6];_86:Float){} }Class _{$_(){} }Class _l{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 68))

    def test_69(self):
        input = '''Class I{$2(_Gs3l:Array[String,011];_,_:Array[String,0B100101]){ {}{} }}Class _:cZ_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 69))

    def test_70(self):
        input = '''Class _{Destructor(){Continue;}Var $V_LV:Array[Float,0B111100];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 70))

    def test_71(self):
        input = '''Class U_:R{Var _,_0I_,$Yv,KN,$9_,$1,$1:Array[Float,0B1];Destructor(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 71))

    def test_72(self):
        input = '''Class V_6N1d{Constructor(){}Constructor(){}Destructor(){}Constructor(){} }Class O_98{$1O5(Qz0_6_1,_9_3,_,_:Float){Continue;Break;} }Class _J3:E{V__(){}Val w,$_:Array[Array[Array[Int,0B1110],1],075];Destructor(){}Destructor(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 72))

    def test_73(self):
        input = '''Class _{Var rp56,_m_t,c,_3,yi_3:t2;Var $h:Array[Array[Array[Array[Array[Int,0X17],0xC],3_7],0B1],0b1];}Class L:n_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 73))

    def test_74(self):
        input = '''Class _:Z54_2{}Class J:n8_{n(nx:j){} }Class p{}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 74))

    def test_75(self):
        input = '''Class _9_{}Class __{Destructor(){Return;Val _Q,B:Array[String,0X3F];} }Class o288_:V{}Class Ep{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 75))

    def test_76(self):
        input = '''Class __{}Class _w{}Class cr:L_{}Class L_{Val _,S:Array[Array[Array[Float,07],054],15];}Class _{Val $z:R0;}Class P{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 76))

    def test_77(self):
        input = '''Class d4{Destructor(){Return;} }Class _3k_b5{Constructor(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 77))

    def test_78(self):
        input = '''Class K:g{Val _:Array[Array[Int,0B10],0B100110];}Class _3{Constructor(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 78))

    def test_79(self):
        input = '''Class __36:_4aa_7{}Class _:_{}Class v{Val _,$1:Array[Int,0X548];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 79))

    def test_80(self):
        input = '''Class Z_:___{Val $5:String;Var __I9,_M:Array[Array[Array[String,0B1],0XBB_F],99];Var $8,$9:Boolean;}Class __1{}Class O{g6(){}Constructor(){}Var $2_4_86_:Float;}Class _:raf{Constructor(){}Destructor(){} }Class __1:_{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 80))

    def test_81(self):
        input = '''Class _:r{}Class _:R{Var _,__0,j_:Array[Array[Array[Float,04],2],0B1];}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 81))

    def test_82(self):
        input = '''Class d:q{}Class G{}Class _{}Class _:G{}Class _{Destructor(){} }Class N8_40IWV:B__{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 82))

    def test_83(self):
        input = '''Class c:_{Destructor(){} }Class __:y_161{Destructor(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 83))

    def test_84(self):
        input = '''Class a:tW_{$_8(){}Var $_:Float;_(){} }Class D:_{}Class _3M:o_8__l{Constructor(_:W8){Break;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 84))

    def test_85(self):
        input = '''Class ATE2:__0{}Class A5:_u1gP{}Class _{Val _,$5_,$__R_3v,Q,_,$_H,$9zV_4s_,J_,A6,_:String;}Class __:_v42{}Class F{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 85))

    def test_86(self):
        input = '''Class __:___b_{}Class e{Var $H6:Float;Val $e_,$_9_:Boolean;Var $_,G,$0143:__1W_;}Class s:_{t(l8:Array[Array[Array[Int,0114],4],0X45];P_:Boolean){} }Class U{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 86))

    def test_87(self):
        input = '''Class _60{}Class __:_{}Class _4B:_{}Class z:jA{}Class _1{}Class x{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 87))

    def test_88(self):
        input = '''Class _{$2_1(){} }Class _t:_0{}Class A_:gO6{$S(_:_;X,_3,_,_:Int){Return;Return!!!!!!New _().X61();{}Continue;} }Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 88))

    def test_89(self):
        input = '''Class _{Constructor(){}Constructor(_O_,b_,i:_;LB,H,_j,___:String;_x10__,O1:Float;X,H:_T;T:Array[Array[Array[Boolean,0b1_0],0126],06]){} }Class q95{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 89))

    def test_90(self):
        input = '''Class _:N_L{Destructor(){Break;}y8(o_d_8,_,w,_1:J6){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 90))

    def test_91(self):
        input = '''Class _{}Class l__5{Val $_:Float;}Class F6_{Val $P_X_,$_,$91:String;}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 91))

    def test_92(self):
        input = '''Class _{Constructor(U0d,W2,__mMlKE,_Jl11:String;b_C,E:String){} }Class _:Pm4{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 92))

    def test_93(self):
        input = '''Class _{}Class ot{$_(){} }Class g__1mU{Constructor(){Var __12:String;} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 93))

    def test_94(self):
        input = '''Class b{}Class _445{Constructor(_:String;K:Array[String,0b1];r_4N:k3h;_,Y_48g__:_;_,_:e_;b:B_;O:_3){}Var $7_:Array[Array[Array[Boolean,03],50],0XE_62];}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 94))

    def test_95(self):
        input = '''Class _:__uDj{Constructor(_5:Array[Boolean,0b1001110];_,_,_v,_,T:Array[Array[Float,0X8_9_D],070];_,_9:Array[Int,0B100101];v,nu:Array[Boolean,05_2]){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 95))

    def test_96(self):
        input = '''Class _:y{}Class s:S{Val $3,_,_x_c3_93k,C1:V;}Class _:n7{}Class __1:_{}Class _{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 96))

    def test_97(self):
        input = '''Class dp:_{Constructor(_8v_,M:Int;_,_N_:Array[Array[Int,0x50],45];B4cl38,_:_8){}Destructor(){}$0(T:Float){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 97))

    def test_98(self):
        input = '''Class p:_o{Constructor(u,_90,V:J__;_4:c){}Constructor(){} }'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 98))

    def test_99(self):
        input = '''Class L{Destructor(){Return;_9::$g3k.m();} }Class a0:z{}'''
        expect = 'successful'
        self.assertTrue(TestParser.test(input, expect, 99))

