import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    # def test_300(self):
    #     input = '''
    #             Class iPhone:Apple{
    #             Val $os: String = "iOS";
    #             Var IMEI: String;
    #             Var $phone_number: Int;
    #             Var $phone: Array[Boolean, 100];
    #             insertSIM(sim: SIM){
    #                 Self.phone_number = SIM.number;
    #             }
    #             detachSIM(){
    #                 Self.phone_number = Null;
    #             }
    #     }
    #     '''
    #     expect = 'Program([ClassDecl(Id(A),[])])'
    #     self.assertTrue(TestAST.test(input, expect, 300))

    def test_301(self):
        input = '''
        Class A {}
        '''
        expect = 'Program([ClassDecl(Id(A),[])])'
        self.assertTrue(TestAST.test(input, expect, 301))

    def test_302(self):
        input = '''
        Class A:B {}
        '''
        expect = 'Program([ClassDecl(Id(A),Id(B),[])])'
        self.assertTrue(TestAST.test(input, expect, 302))

    def test_303(self):
        input = '''
        Class A:B {}
        Class C {}
        '''
        expect = 'Program([ClassDecl(Id(A),Id(B),[]),ClassDecl(Id(C),[])])'
        self.assertTrue(TestAST.test(input, expect, 303))

    def test_304(self):
        input = '''
        Class A:B {}
        Class C:D {}
        '''
        expect = 'Program([ClassDecl(Id(A),Id(B),[]),ClassDecl(Id(C),Id(D),[])])'
        self.assertTrue(TestAST.test(input, expect, 304))

    def test_305(self):
        input = '''
        Class A:B {}
        Class C:D {}
        Class E {}
        '''
        expect = 'Program([ClassDecl(Id(A),Id(B),[]),ClassDecl(Id(C),Id(D),[]),ClassDecl(Id(E),[])])'
        self.assertTrue(TestAST.test(input, expect, 305))

    def test_306(self):
        input = '''
        Class A{
            Var N : Int;
        }
        '''
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(N),IntType))])])'
        self.assertTrue(TestAST.test(input, expect, 306))

    def test_307(self):
        input = '''
        Class A{
            Var x,y,$z : Int;
        }
        '''
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Instance,VarDecl(Id(x),IntType)),AttributeDecl(Instance,VarDecl(Id(y),IntType)),AttributeDecl(Static,VarDecl(Id($z),IntType))])])'
        self.assertTrue(TestAST.test(input, expect, 307))

    def test_308(self):
        input = '''
        Class A{
            Val $x,$z,y : String;
        }
        '''
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Static,ConstDecl(Id($x),StringType,None)),AttributeDecl(Static,ConstDecl(Id($z),StringType,None)),AttributeDecl(Instance,ConstDecl(Id(y),StringType,None))])])'
        self.assertTrue(TestAST.test(input, expect, 308))

    def test_309(self):
        input = '''
        Class A{
            Val $x :Int = 1;
        }
        '''
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Static,ConstDecl(Id($x),IntType,IntLit(1)))])])'
        self.assertTrue(TestAST.test(input, expect, 309))

    def test_310(self):
        input = '''
         Class A{
            Val $x, $y : Int = 1, 2+2;
        }
        '''
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Static,ConstDecl(Id($x),IntType,IntLit(1))),AttributeDecl(Static,ConstDecl(Id($y),IntType,BinaryOp(+,IntLit(2),IntLit(2))))])])'
        self.assertTrue(TestAST.test(input, expect, 310))

    def test_311(self):
        input = '''
         Class A{
            Val $x, $y : Int = 1, 2+2;
            Var p,$q : Boolean = True, False;
        }
        '''
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Static,ConstDecl(Id($x),IntType,IntLit(1))),AttributeDecl(Static,ConstDecl(Id($y),IntType,BinaryOp(+,IntLit(2),IntLit(2)))),AttributeDecl(Instance,VarDecl(Id(p),BoolType,BooleanLit(True))),AttributeDecl(Static,VarDecl(Id($q),BoolType,BooleanLit(False)))])])'
        self.assertTrue(TestAST.test(input, expect, 311))

    def test_312(self):
        input = '''
        Class A{
           Var $x, $y : Int = 0, 0;
           Val a, $b : Int = 0x0, 0B0;
        }
        '''
        expect = 'Program([ClassDecl(Id(A),[AttributeDecl(Static,VarDecl(Id($x),IntType,IntLit(0))),AttributeDecl(Static,VarDecl(Id($y),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(a),IntType,IntLit(0))),AttributeDecl(Static,ConstDecl(Id($b),IntType,IntLit(0)))])])'
        self.assertTrue(TestAST.test(input, expect, 312))

    def test_313(self):
        input = '''
        Class A{
            func(){}
        }
        '''
        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(func),Instance,[],Block([]))])])'
        self.assertTrue(TestAST.test(input, expect, 313))

    def test_314(self):
        input = '''
        Class C{
            func(a : Int){}
        }
        '''
        expect = 'Program([ClassDecl(Id(C),[MethodDecl(Id(func),Instance,[param(Id(a),IntType)],Block([]))])])'
        self.assertTrue(TestAST.test(input, expect, 314))

    def test_315(self):
        input = '''
        Class C{
            func(a : Int){
                Var x,y: Int = 1+1, 2+2;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(C),[MethodDecl(Id(func),Instance,[param(Id(a),IntType)],Block([VarDecl(Id(x),IntType,BinaryOp(+,IntLit(1),IntLit(1))),VarDecl(Id(y),IntType,BinaryOp(+,IntLit(2),IntLit(2)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 315))

    def test_316(self):
        input = '''
        Class C{
            func(){
                Return;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(C),[MethodDecl(Id(func),Instance,[],Block([Return()]))])])'
        self.assertTrue(TestAST.test(input, expect, 316))

    def test_317(self):
        input = '''
        Class C{
            func(){
                Return True;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(C),[MethodDecl(Id(func),Instance,[],Block([Return(BooleanLit(True))]))])])'
        self.assertTrue(TestAST.test(input, expect, 317))

    def test_318(self):
        input = '''
        Class C{
            Constructor(a : Int){
                {}
                Return D;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(C),[MethodDecl(Id(Constructor),Instance,[param(Id(a),IntType)],Block([Block([]),Return(Id(D))]))])])'
        self.assertTrue(TestAST.test(input, expect, 318))

    def test_319(self):
        input = '''
        Class C{
            Destructor(){ 
                ## Nothing ##
                Return GG;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(C),[MethodDecl(Id(Destructor),Instance,[],Block([Return(Id(GG))]))])])'
        self.assertTrue(TestAST.test(input, expect, 319))

    def test_320(self):
        input = '''
        Class C{
            func(a : Int){
                a = True;
                Return 2+3*4/5; 
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(C),[MethodDecl(Id(func),Instance,[param(Id(a),IntType)],Block([AssignStmt(Id(a),BooleanLit(True)),Return(BinaryOp(+,IntLit(2),BinaryOp(/,BinaryOp(*,IntLit(3),IntLit(4)),IntLit(5))))]))])])'
        self.assertTrue(TestAST.test(input, expect, 320))

    def test_321(self):
        input = '''
        Class Program{
            main(){
                Var x,y: Int = 1+1, 2+2;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(x),IntType,BinaryOp(+,IntLit(1),IntLit(1))),VarDecl(Id(y),IntType,BinaryOp(+,IntLit(2),IntLit(2)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 321))

    def test_322(self):
        input = '''
        Class Program{
            main(a : Int){
                a = "String";
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([AssignStmt(Id(a),StringLit(String))]))])])'
        self.assertTrue(TestAST.test(input, expect, 322))

    def test_323(self):
        input = '''
        Class Programming{
            Val $x: Int = 10_3;
            main(){
                Val y: Int = 11.23123;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Programming),[AttributeDecl(Static,ConstDecl(Id($x),IntType,IntLit(103))),MethodDecl(Id(main),Instance,[],Block([ConstDecl(Id(y),IntType,FloatLit(11.23123))]))])])'
        self.assertTrue(TestAST.test(input, expect, 323))

    def test_324(self):
        input = '''
        Class Programming{
            main(){
                If(1){
                Love = 0;
                }
                Elseif(2){
                Love = 1;}
                Else{
                Friendzone = True;
                }
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Programming),[MethodDecl(Id(main),Instance,[],Block([If(IntLit(1),Block([AssignStmt(Id(Love),IntLit(0))]),If(IntLit(2),Block([AssignStmt(Id(Love),IntLit(1))]),Block([AssignStmt(Id(Friendzone),BooleanLit(True))])))]))])])'
        self.assertTrue(TestAST.test(input, expect, 324))

    def test_325(self):
        input = '''
        Class Programming{
            main(){
                If( (a < 2) && (b > 3)){
                    d = "OK";
                }
                Else{
                    e = "FAIL";
                }
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Programming),[MethodDecl(Id(main),Instance,[],Block([If(BinaryOp(&&,BinaryOp(<,Id(a),IntLit(2)),BinaryOp(>,Id(b),IntLit(3))),Block([AssignStmt(Id(d),StringLit(OK))]),Block([AssignStmt(Id(e),StringLit(FAIL))]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 325))

    def test_326(self):
        input = '''
        Class Program{
            main(){
                If( number % 2 == 0){
                    System.printInt(Integer::$HEX);
                }
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(==,BinaryOp(%,Id(number),IntLit(2)),IntLit(0)),Block([Call(Id(System),Id(printInt),[FieldAccess(Id(Integer),Id($HEX))])]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 326))

    def test_327(self):
        input = '''
        Class Program{
            main(a : Int){
                Foreach (i In 1 .. 100 By 2) {
                Out.printInt(i);
                }
                Foreach (x In 5 .. 2) {
                Out.printInt(arr[x]);
                }
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([For(Id(i),IntLit(1),IntLit(100),IntLit(2),Block([Call(Id(Out),Id(printInt),[Id(i)])])]),For(Id(x),IntLit(5),IntLit(2),IntLit(1),Block([Call(Id(Out),Id(printInt),[ArrayCell(Id(arr),[Id(x)])])])])]))])])'
        self.assertTrue(TestAST.test(input, expect, 327))

    def test_328(self):
        input = '''
        Class Program{
            main(){
                Var r, s: Int;
                r = 2.0;
                Var a, b: Array[Int, 5];
                s = r * r * Self.myPI;
                a[0] = s;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([VarDecl(Id(r),IntType),VarDecl(Id(s),IntType),AssignStmt(Id(r),FloatLit(2.0)),VarDecl(Id(a),ArrayType(5,IntType)),VarDecl(Id(b),ArrayType(5,IntType)),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Self(),Id(myPI)))),AssignStmt(ArrayCell(Id(a),[IntLit(0)]),Id(s))]))])])'
        self.assertTrue(TestAST.test(input, expect, 328))

    def test_329(self):
        input = '''
        Class Program{
            main(a : Int){
                a = "String";
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([AssignStmt(Id(a),StringLit(String))]))])])'
        self.assertTrue(TestAST.test(input, expect, 329))

    def test_330(self):
        input = '''
        Class Program{
            main(a : Int){
            If (1 + 2 == 0) {
                OutScreen.println(3 * 2);
            }
            Elseif (1 + 2 == "3") {
                Sys32.terminate(41241211 - "4124124124");
            }
            Else {
                Break;
                Return;
            }
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Instance,[param(Id(a),IntType)],Block([If(BinaryOp(==,BinaryOp(+,IntLit(1),IntLit(2)),IntLit(0)),Block([Call(Id(OutScreen),Id(println),[BinaryOp(*,IntLit(3),IntLit(2))])]),If(BinaryOp(==,BinaryOp(+,IntLit(1),IntLit(2)),StringLit(3)),Block([Call(Id(Sys32),Id(terminate),[BinaryOp(-,IntLit(41241211),StringLit(4124124124))])]),Block([Break,Return()])))]))])])'
        self.assertTrue(TestAST.test(input, expect, 330))

    def test_331(self):
        input = '''
        Class C{
                function(){
                    a = b%c + Self.foo();
                    a = b*c*d + Self.foo();
                    Self.foo();
                    Return True;
                }
        }
        '''
        expect = 'Program([ClassDecl(Id(C),[MethodDecl(Id(function),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+,BinaryOp(%,Id(b),Id(c)),CallExpr(Self(),Id(foo),[]))),AssignStmt(Id(a),BinaryOp(+,BinaryOp(*,BinaryOp(*,Id(b),Id(c)),Id(d)),CallExpr(Self(),Id(foo),[]))),Call(Self(),Id(foo),[]),Return(BooleanLit(True))]))])])'
        self.assertTrue(TestAST.test(input, expect, 331))

    def test_332(self):
        input = '''
        Class B{
                main(){
                }
                foo(){
                    a = b%c + Self.foo();
                    Self.foo2(param1, param2);
                    a1 = Self.foo3(param1, param2);
                    b = 1 >= 3;
                    val1 = True == False;
                    b = ! val1;
                }
        }
        '''
        expect = 'Program([ClassDecl(Id(B),[MethodDecl(Id(main),Instance,[],Block([])),MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+,BinaryOp(%,Id(b),Id(c)),CallExpr(Self(),Id(foo),[]))),Call(Self(),Id(foo2),[Id(param1),Id(param2)]),AssignStmt(Id(a1),CallExpr(Self(),Id(foo3),[Id(param1),Id(param2)])),AssignStmt(Id(b),BinaryOp(>=,IntLit(1),IntLit(3))),AssignStmt(Id(val1),BinaryOp(==,BooleanLit(True),BooleanLit(False))),AssignStmt(Id(b),UnaryOp(!,Id(val1)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 332))

    def test_333(self):
        input = '''
        Class Vehicle{
                run(){
                    Self.running = True;
                }
                stop(){
                    Self.running = False;
                }
        }
        '''
        expect = 'Program([ClassDecl(Id(Vehicle),[MethodDecl(Id(run),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(running)),BooleanLit(True))])),MethodDecl(Id(stop),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(running)),BooleanLit(False))]))])])'
        self.assertTrue(TestAST.test(input, expect, 333))

    def test_334(self):
        input = '''
        Class Vinfast{
            Var running: Boolean = True;
            Val speed: Int;
            Constructor(){
                Self.speed = 10000000;
            }
            Constructor(speed: Int){
                Self.speed = speed;
            }
            run(){
                Self.running = True;
            }
            stop(){
                Self.running = False;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Vinfast),[AttributeDecl(Instance,VarDecl(Id(running),BoolType,BooleanLit(True))),AttributeDecl(Instance,ConstDecl(Id(speed),IntType,None)),MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(speed)),IntLit(10000000))])),MethodDecl(Id(Constructor),Instance,[param(Id(speed),IntType)],Block([AssignStmt(FieldAccess(Self(),Id(speed)),Id(speed))])),MethodDecl(Id(run),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(running)),BooleanLit(True))])),MethodDecl(Id(stop),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(running)),BooleanLit(False))]))])])'
        self.assertTrue(TestAST.test(input, expect, 334))

    def test_335(self):
        input = '''
        Class Car:Vehicle{
            Val sunScreen: Boolean = False;
            open(){
                ## Open hood ##
                If (Hood==False){
                    Hood = True;
                    Return True;
                }
                Else{
                    Return False;
                }
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Car),Id(Vehicle),[AttributeDecl(Instance,ConstDecl(Id(sunScreen),BoolType,BooleanLit(False))),MethodDecl(Id(open),Instance,[],Block([If(BinaryOp(==,Id(Hood),BooleanLit(False)),Block([AssignStmt(Id(Hood),BooleanLit(True)),Return(BooleanLit(True))]),Block([Return(BooleanLit(False))]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 335))

    def test_336(self):
        input = '''
        Class Eval{
            getSpeedfromKm(a, b, c: Int; e, f: String){
                Outscreen.get("The speed = " +.  "1000km/h");
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Eval),[MethodDecl(Id(getSpeedfromKm),Instance,[param(Id(a),IntType),param(Id(b),IntType),param(Id(c),IntType),param(Id(e),StringType),param(Id(f),StringType)],Block([Call(Id(Outscreen),Id(get),[BinaryOp(+.,StringLit(The speed = ),StringLit(1000km/h))])]))])])'
        self.assertTrue(TestAST.test(input, expect, 336))

    def test_337(self):
        input = '''
        Class Shape {
            foo(){
                a = ("a"+."b")+."b";
            } 
        }
        '''
        expect = 'Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(a),BinaryOp(+.,BinaryOp(+.,StringLit(a),StringLit(b)),StringLit(b)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 337))

    def test_338(self):
        input = '''
        Class Shape {
            foo(){
                c = ("a"==."a")==True;
            } 
        }
        '''
        expect = 'Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(c),BinaryOp(==,BinaryOp(==.,StringLit(a),StringLit(a)),BooleanLit(True)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 338))

    def test_339(self):
        input = '''
        Class Loop {
            function(){
                i=-1;
             } 
        }
        '''
        expect = 'Program([ClassDecl(Id(Loop),[MethodDecl(Id(function),Instance,[],Block([AssignStmt(Id(i),UnaryOp(-,IntLit(1)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 339))

    def test_340(self):
        input = '''
        Class Sharp{
            foo(){
                _ID = New X().Y().Z();
                Var C : Array[Int, 0B1010];
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Sharp),[MethodDecl(Id(foo),Instance,[],Block([AssignStmt(Id(_ID),CallExpr(CallExpr(NewExpr(Id(X),[]),Id(Y),[]),Id(Z),[])),VarDecl(Id(C),ArrayType(10,IntType))]))])])'
        self.assertTrue(TestAST.test(input, expect, 340))

    def test_341(self):
        input = '''
        Class Mine:Arr{
            func(){
                Var a: Array[Int, 01];
                Var a: Array[Int, 0x1];
                Var a: Array[Int, 0X1];
                Var a: Array[Int, 0b1];
                Var a: Array[Int, 0B1];
                Var a: Array[Int, 1];
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Mine),Id(Arr),[MethodDecl(Id(func),Instance,[],Block([VarDecl(Id(a),ArrayType(1,IntType)),VarDecl(Id(a),ArrayType(1,IntType)),VarDecl(Id(a),ArrayType(1,IntType)),VarDecl(Id(a),ArrayType(1,IntType)),VarDecl(Id(a),ArrayType(1,IntType)),VarDecl(Id(a),ArrayType(1,IntType))]))])])'
        self.assertTrue(TestAST.test(input, expect, 341))

    def test_342(self):
        input = '''
        Class Mine:Arr{
            func(){
                Var a: Array[Int, 1] = 1_23.456e+7990;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Mine),Id(Arr),[MethodDecl(Id(func),Instance,[],Block([VarDecl(Id(a),ArrayType(1,IntType),FloatLit(inf))]))])])'
        self.assertTrue(TestAST.test(input, expect, 342))

    def test_343(self):
        input = '''
        Class Program{
            main(){
                Return Arr[1][2][3][3+1][4];
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Return(ArrayCell(Id(Arr),[IntLit(1),IntLit(2),IntLit(3),BinaryOp(+,IntLit(3),IntLit(1)),IntLit(4)]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 343))

    def test_344(self):
        input = '''
        Class Program {
            main() {
                (abc[123]).funct();
                a[123] = "1";
                Out.println(f.a[1]);
                ((((efh[32][1]).a[21]).funct()[0]).a[21]).funct();
                Return;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(ArrayCell(Id(abc),[IntLit(123)]),Id(funct),[]),AssignStmt(ArrayCell(Id(a),[IntLit(123)]),StringLit(1)),Call(Id(Out),Id(println),[ArrayCell(FieldAccess(Id(f),Id(a)),[IntLit(1)])]),Call(ArrayCell(FieldAccess(ArrayCell(CallExpr(ArrayCell(FieldAccess(ArrayCell(Id(efh),[IntLit(32),IntLit(1)]),Id(a)),[IntLit(21)]),Id(funct),[]),[IntLit(0)]),Id(a)),[IntLit(21)]),Id(funct),[]),Return()]))])])'
        self.assertTrue(TestAST.test(input, expect, 344))

    def test_345(self):
        input = '''
        Class Shape{
            func_tion(){
                Return A::$B * C::$DD--F::$H;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Shape),[MethodDecl(Id(func_tion),Instance,[],Block([Return(BinaryOp(-,BinaryOp(*,FieldAccess(Id(A),Id($B)),FieldAccess(Id(C),Id($DD))),UnaryOp(-,FieldAccess(Id(F),Id($H)))))]))])])'
        self.assertTrue(TestAST.test(input, expect, 345))

    def test_346(self):
        input = '''
        Class Shape{
            func_tion(){
                Foreach (Step In 1+1 .. 100+100 By D.func_tion()){}
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Shape),[MethodDecl(Id(func_tion),Instance,[],Block([For(Id(Step),BinaryOp(+,IntLit(1),IntLit(1)),BinaryOp(+,IntLit(100),IntLit(100)),CallExpr(Id(D),Id(func_tion),[]),Block([])])]))])])'
        self.assertTrue(TestAST.test(input, expect, 346))

    def test_347(self):
        input = '''
        Class Shape{
            func_tion(){
               A[b[c[d[e[f::$g]]]]][h::$i][j.k()][F::$DDD()]=0;
            }
        }   
        '''
        expect = 'Program([ClassDecl(Id(Shape),[MethodDecl(Id(func_tion),Instance,[],Block([AssignStmt(ArrayCell(Id(A),[ArrayCell(Id(b),[ArrayCell(Id(c),[ArrayCell(Id(d),[ArrayCell(Id(e),[FieldAccess(Id(f),Id($g))])])])]),FieldAccess(Id(h),Id($i)),CallExpr(Id(j),Id(k),[]),CallExpr(Id(F),Id($DDD),[])]),IntLit(0))]))])])'
        self.assertTrue(TestAST.test(input, expect, 347))

    def test_348(self):
        input = '''
        Class Shape{
            func_tion(){
                If (a == -1--1){
                    If(b == "c"+."c"){}
                    Elseif(SHAPE == b ==. c){}
                }
            }
        }   
        '''
        expect = 'Program([ClassDecl(Id(Shape),[MethodDecl(Id(func_tion),Instance,[],Block([If(BinaryOp(==,Id(a),BinaryOp(-,UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(1)))),Block([If(BinaryOp(+.,BinaryOp(==,Id(b),StringLit(c)),StringLit(c)),Block([]),If(BinaryOp(==.,BinaryOp(==,Id(SHAPE),Id(b)),Id(c)),Block([])))]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 348))

    def test_349(self):
        input = '''
        Class Shape{
            $a(){
                Break;
                Continue;
                Return;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Shape),[MethodDecl(Id($a),Static,[],Block([Break,Continue,Return()]))])])'
        self.assertTrue(TestAST.test(input, expect, 349))

    def test_350(self):
        input = '''
        Class League_of_Legend{
            Destructor(){
                Status = 0x123;
                Return;
                Run::$Client.start();
            } 
        }

        Class Master:Rank{}
        '''
        expect = 'Program([ClassDecl(Id(League_of_Legend),[MethodDecl(Id(Destructor),Instance,[],Block([AssignStmt(Id(Status),IntLit(291)),Return(),Call(FieldAccess(Id(Run),Id($Client)),Id(start),[])]))]),ClassDecl(Id(Master),Id(Rank),[])])'
        self.assertTrue(TestAST.test(input, expect, 350))

    def test_351(self):
        input = '''
        Class Process{
            main(){
                If(a == True){
                    Data = True;
                    Foreach(idx In 1+1 .. 1*2+3 By CPU.nVidia("RTX 3090")){}
                }
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Process),[MethodDecl(Id(main),Instance,[],Block([If(BinaryOp(==,Id(a),BooleanLit(True)),Block([AssignStmt(Id(Data),BooleanLit(True)),For(Id(idx),BinaryOp(+,IntLit(1),IntLit(1)),BinaryOp(+,BinaryOp(*,IntLit(1),IntLit(2)),IntLit(3)),CallExpr(Id(CPU),Id(nVidia),[StringLit(RTX 3090)]),Block([])])]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 351))

    def test_352(self):
        input = '''
        Class Program{
            main(){
                If(FFF == True){
                    Foreach(idx In 1+1 .. 1*2+3 By CPU.nVidia("RTX 3090")){
                        Foreach (x In E::$F() .. a.b.c.d By H::$XYZ){}
                    }
                }
            }
        }                
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(==,Id(FFF),BooleanLit(True)),Block([For(Id(idx),BinaryOp(+,IntLit(1),IntLit(1)),BinaryOp(+,BinaryOp(*,IntLit(1),IntLit(2)),IntLit(3)),CallExpr(Id(CPU),Id(nVidia),[StringLit(RTX 3090)]),Block([For(Id(x),CallExpr(Id(E),Id($F),[]),FieldAccess(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(d)),FieldAccess(Id(H),Id($XYZ)),Block([])])])])]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 352))

    def test_353(self):
        input = '''
        Class Program : PPL {
            Val a, b : Int = "Hello", "World";
            Var c : String = (x ==. y) && (a +. b);
            Var d : Boolean = (True == False) && (True == True) || True && False;
            Var e : Boolean = ("Hello" ==. "World") || (a == b);
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),Id(PPL),[AttributeDecl(Instance,ConstDecl(Id(a),IntType,StringLit(Hello))),AttributeDecl(Instance,ConstDecl(Id(b),IntType,StringLit(World))),AttributeDecl(Instance,VarDecl(Id(c),StringType,BinaryOp(&&,BinaryOp(==.,Id(x),Id(y)),BinaryOp(+.,Id(a),Id(b))))),AttributeDecl(Instance,VarDecl(Id(d),BoolType,BinaryOp(&&,BinaryOp(||,BinaryOp(&&,BinaryOp(==,BooleanLit(True),BooleanLit(False)),BinaryOp(==,BooleanLit(True),BooleanLit(True))),BooleanLit(True)),BooleanLit(False)))),AttributeDecl(Instance,VarDecl(Id(e),BoolType,BinaryOp(||,BinaryOp(==.,StringLit(Hello),StringLit(World)),BinaryOp(==,Id(a),Id(b)))))])])'
        self.assertTrue(TestAST.test(input, expect, 353))

    def test_354(self):
        input = '''
        Class Program : PPL {
            Val a : Array[Int, 3] = Array("A","B","C");
            Val $b : Int = a[Arr[0]];
        }        
        '''
        expect = 'Program([ClassDecl(Id(Program),Id(PPL),[AttributeDecl(Instance,ConstDecl(Id(a),ArrayType(3,IntType),[StringLit(A),StringLit(B),StringLit(C)])),AttributeDecl(Static,ConstDecl(Id($b),IntType,ArrayCell(Id(a),[ArrayCell(Id(Arr),[IntLit(0)])])))])])'
        self.assertTrue(TestAST.test(input, expect, 354))

    def test_355(self):
        input = '''
        Class Program{
            Constructor() {}
            Constructor(str  : String) {}
            Constructor(arr : Array[Int, 10]) {}
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(str),StringType)],Block([])),MethodDecl(Id(Constructor),Instance,[param(Id(arr),ArrayType(10,IntType))],Block([]))])])'
        self.assertTrue(TestAST.test(input, expect, 355))

    def test_356(self):
        input = '''
        Class A{
            Destructor(){}
        }
        Class B:A{
            Destructor(){Return;}
        }
        '''
        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(Destructor),Instance,[],Block([]))]),ClassDecl(Id(B),Id(A),[MethodDecl(Id(Destructor),Instance,[],Block([Return()]))])])'
        self.assertTrue(TestAST.test(input, expect, 356))

    def test_357(self):
        input = '''
        Class Program{
            main(){
                ABC.function();
                ABC::$func();
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(ABC),Id(function),[]),Call(Id(ABC),Id($func),[])]))])])'
        self.assertTrue(TestAST.test(input, expect, 357))

    def test_358(self):
        input = '''
        Class Program{
            main(){
                (a::$func().arr[1][2]).test();
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(ArrayCell(FieldAccess(CallExpr(Id(a),Id($func),[]),Id(arr)),[IntLit(1),IntLit(2)]),Id(test),[])]))])])'
        self.assertTrue(TestAST.test(input, expect, 358))

    def test_359(self):
        input = '''
        Class Brand{
            func(){
                New Brand().function();
                a.b.c.d.e.f().g().h.j();
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Brand),[MethodDecl(Id(func),Instance,[],Block([Call(NewExpr(Id(Brand),[]),Id(function),[]),Call(FieldAccess(CallExpr(CallExpr(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(d)),Id(e)),Id(f),[]),Id(g),[]),Id(h)),Id(j),[])]))])])'
        self.assertTrue(TestAST.test(input, expect, 359))

    def test_360(self):
        input = '''
        Class Circle : Shape {
            Val height : Int = New Obj(1).a[1];
            Var $width : Float = 0x123456789;
        }
        '''
        expect = 'Program([ClassDecl(Id(Circle),Id(Shape),[AttributeDecl(Instance,ConstDecl(Id(height),IntType,ArrayCell(FieldAccess(NewExpr(Id(Obj),[IntLit(1)]),Id(a)),[IntLit(1)]))),AttributeDecl(Static,VarDecl(Id($width),FloatType,IntLit(4886718345)))])])'
        self.assertTrue(TestAST.test(input, expect, 360))

    def test_361(self):
        input = '''
        Class Shape {
            foo() {
                Obj.doSth();
                Return New X(123, 124, 10 * 20 + 30);
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([Call(Id(Obj),Id(doSth),[]),Return(NewExpr(Id(X),[IntLit(123),IntLit(124),BinaryOp(+,BinaryOp(*,IntLit(10),IntLit(20)),IntLit(30))]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 361))

    def test_362(self):
        input = '''
        Class Shape {
            foo() {
                Val a : Int = ABC::$a.b.c.d[1][2][3][4][(0 + 012 + 0xA5 + 0XA3 + 0b10101 + 0B1010)];
                Var b : Int = 0x0 + 0X0 + 0b0 + 0B0 + 00 + 0;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([ConstDecl(Id(a),IntType,ArrayCell(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(ABC),Id($a)),Id(b)),Id(c)),Id(d)),[IntLit(1),IntLit(2),IntLit(3),IntLit(4),BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(0),IntLit(10)),IntLit(165)),IntLit(163)),IntLit(21)),IntLit(10))])),VarDecl(Id(b),IntType,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(+,IntLit(0),IntLit(0)),IntLit(0)),IntLit(0)),IntLit(0)),IntLit(0)))]))])])'
        self.assertTrue(TestAST.test(input, expect, 362))

    def test_363(self):
        input = '''
        Class Shape {
            foo() {
                Val c, d : Float = .e123 , 1e-101;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([ConstDecl(Id(c),FloatType,FloatLit(0.0)),ConstDecl(Id(d),FloatType,FloatLit(1e-101))]))])])'
        self.assertTrue(TestAST.test(input, expect, 363))

    def test_364(self):
        input = '''
        Class Swap{
            func(){
                temp = p1;
                p1 = p2;
                p2 = temp;
                Return True;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Swap),[MethodDecl(Id(func),Instance,[],Block([AssignStmt(Id(temp),Id(p1)),AssignStmt(Id(p1),Id(p2)),AssignStmt(Id(p2),Id(temp)),Return(BooleanLit(True))]))])])'
        self.assertTrue(TestAST.test(input, expect, 364))

    def test_365(self):
        input = '''
        Class Swap{
            func(){
                If (1 == -1--1){
                    If(b == "f"+."h"){}
                    Elseif(a == b ==. c){}
                }
            }
        }   
        '''
        expect = 'Program([ClassDecl(Id(Swap),[MethodDecl(Id(func),Instance,[],Block([If(BinaryOp(==,IntLit(1),BinaryOp(-,UnaryOp(-,IntLit(1)),UnaryOp(-,IntLit(1)))),Block([If(BinaryOp(+.,BinaryOp(==,Id(b),StringLit(f)),StringLit(h)),Block([]),If(BinaryOp(==.,BinaryOp(==,Id(a),Id(b)),Id(c)),Block([])))]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 365))

    def test_366(self):
        input = '''
        Class Shape{
            Var $a : Int;
            Var b : int;
            Val c : Int;
            Val $d : Int;
        }   
        '''
        expect = 'Program([ClassDecl(Id(Shape),[AttributeDecl(Static,VarDecl(Id($a),IntType)),AttributeDecl(Instance,VarDecl(Id(b),ClassType(Id(int)),NullLiteral())),AttributeDecl(Instance,ConstDecl(Id(c),IntType,None)),AttributeDecl(Static,ConstDecl(Id($d),IntType,None))])])'
        self.assertTrue(TestAST.test(input, expect, 366))

    def test_367(self):
        input = '''
            Class Shape {
                foo(){
                    Var a : Int = ((b < c) < (e < f)) < (True < False);
                } 
            }
        '''
        expect = 'Program([ClassDecl(Id(Shape),[MethodDecl(Id(foo),Instance,[],Block([VarDecl(Id(a),IntType,BinaryOp(<,BinaryOp(<,BinaryOp(<,Id(b),Id(c)),BinaryOp(<,Id(e),Id(f))),BinaryOp(<,BooleanLit(True),BooleanLit(False))))]))])])'
        self.assertTrue(TestAST.test(input, expect, 367))

    def test_368(self):
        input = '''
        Class Shape {
            $func() {
                a.b().c[1][2] = d.foo() +. Self.foo();
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Shape),[MethodDecl(Id($func),Static,[],Block([AssignStmt(ArrayCell(FieldAccess(CallExpr(Id(a),Id(b),[]),Id(c)),[IntLit(1),IntLit(2)]),BinaryOp(+.,CallExpr(Id(d),Id(foo),[]),CallExpr(Self(),Id(foo),[])))]))])])'
        self.assertTrue(TestAST.test(input, expect, 368))

    def test_369(self):
        input = '''
        Class Car {
            run() {
                Foreach (hp In New Engine("Start") .. Self.wheel().A.bar() By BKC) {
                    Self.display(speed);
                }
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Car),[MethodDecl(Id(run),Instance,[],Block([For(Id(hp),NewExpr(Id(Engine),[StringLit(Start)]),CallExpr(FieldAccess(CallExpr(Self(),Id(wheel),[]),Id(A)),Id(bar),[]),Id(BKC),Block([Call(Self(),Id(display),[Id(speed)])])])]))])])'
        self.assertTrue(TestAST.test(input, expect, 369))

    def test_370(self):
        input = '''
        Class Program {
            a() {
                Val a : ABC = Null;
                a = New XYZ(1 + 2, a - 4 * b, 10 / 7 + d, "Hello World");
                Self.display(a.b.c.d);
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([ConstDecl(Id(a),ClassType(Id(ABC)),NullLiteral()),AssignStmt(Id(a),NewExpr(Id(XYZ),[BinaryOp(+,IntLit(1),IntLit(2)),BinaryOp(-,Id(a),BinaryOp(*,IntLit(4),Id(b))),BinaryOp(+,BinaryOp(/,IntLit(10),IntLit(7)),Id(d)),StringLit(Hello World)])),Call(Self(),Id(display),[FieldAccess(FieldAccess(FieldAccess(Id(a),Id(b)),Id(c)),Id(d))])]))])])'
        self.assertTrue(TestAST.test(input, expect, 370))

    def test_371(self):
        input = '''
        Class Program {
            a() {
                Val a : ABC = Null;
                Val b : BCD = New X();
                a = New XYZ(0x123 + 00, a - 0B1 * b, 0231 / 7.1230 + d, "Hello World");
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(a),Instance,[],Block([ConstDecl(Id(a),ClassType(Id(ABC)),NullLiteral()),ConstDecl(Id(b),ClassType(Id(BCD)),NewExpr(Id(X),[])),AssignStmt(Id(a),NewExpr(Id(XYZ),[BinaryOp(+,IntLit(291),IntLit(0)),BinaryOp(-,Id(a),BinaryOp(*,IntLit(1),Id(b))),BinaryOp(+,BinaryOp(/,IntLit(153),FloatLit(7.123)),Id(d)),StringLit(Hello World)]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 371))

    def test_372(self):
        input = '''
        Class iPhone:Apple{
            Var $Battery : Int;
            foo( i : Array [Boolean , 073]){
                a = 01050203;
                b.c(Null, Self, Null, Array(1)).f = 0xABC12DEF;
                g[l][w[x]]=0B101011;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(iPhone),Id(Apple),[AttributeDecl(Static,VarDecl(Id($Battery),IntType)),MethodDecl(Id(foo),Instance,[param(Id(i),ArrayType(59,BoolType))],Block([AssignStmt(Id(a),IntLit(282755)),AssignStmt(FieldAccess(CallExpr(Id(b),Id(c),[NullLiteral(),Self(),NullLiteral(),[IntLit(1)]]),Id(f)),IntLit(2881564143)),AssignStmt(ArrayCell(Id(g),[Id(l),ArrayCell(Id(w),[Id(x)])]),IntLit(43))]))])])'
        self.assertTrue(TestAST.test(input, expect, 372))

    def test_373(self):
        input = '''
        Class Person{
            Val is_Student : Boolean = True;
            learn(status : String){
                If (is_Student == True){
                    Self.is_learning = True;
                }
                Else{
                    Self.is_learning = False;
                    Self.working = True;
                }
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Person),[AttributeDecl(Instance,ConstDecl(Id(is_Student),BoolType,BooleanLit(True))),MethodDecl(Id(learn),Instance,[param(Id(status),StringType)],Block([If(BinaryOp(==,Id(is_Student),BooleanLit(True)),Block([AssignStmt(FieldAccess(Self(),Id(is_learning)),BooleanLit(True))]),Block([AssignStmt(FieldAccess(Self(),Id(is_learning)),BooleanLit(False)),AssignStmt(FieldAccess(Self(),Id(working)),BooleanLit(True))]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 373))

    def test_374(self):
        input = '''
        Class Home{
                Constructor(){
                    Home::$people = Home::$people + 1;
                }
                Destructor(){
                    Home::$people = Null;
                    Return True;
                }
        }
        '''
        expect = 'Program([ClassDecl(Id(Home),[MethodDecl(Id(Constructor),Instance,[],Block([AssignStmt(FieldAccess(Id(Home),Id($people)),BinaryOp(+,FieldAccess(Id(Home),Id($people)),IntLit(1)))])),MethodDecl(Id(Destructor),Instance,[],Block([AssignStmt(FieldAccess(Id(Home),Id($people)),NullLiteral()),Return(BooleanLit(True))]))])])'
        self.assertTrue(TestAST.test(input, expect, 374))

    def test_375(self):
        input = '''
        Class Vehicle{
            run(){
                Self.running = True;
            }
            stop(){
                Self.running = False;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Vehicle),[MethodDecl(Id(run),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(running)),BooleanLit(True))])),MethodDecl(Id(stop),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(running)),BooleanLit(False))]))])])'
        self.assertTrue(TestAST.test(input, expect, 375))

    def test_376(self):
        input = '''
        Class Car : Vehicle{
                Val speed: Float = 0.000;
                Val $model, tire_um: Int = 1 * 3 + 4 + 5 + 4 - 4 / 100_000_0000, Self.tire_num(this.car);
        }
        '''
        expect = 'Program([ClassDecl(Id(Car),Id(Vehicle),[AttributeDecl(Instance,ConstDecl(Id(speed),FloatType,FloatLit(0.0))),AttributeDecl(Static,ConstDecl(Id($model),IntType,BinaryOp(-,BinaryOp(+,BinaryOp(+,BinaryOp(+,BinaryOp(*,IntLit(1),IntLit(3)),IntLit(4)),IntLit(5)),IntLit(4)),BinaryOp(/,IntLit(4),IntLit(1000000000))))),AttributeDecl(Instance,ConstDecl(Id(tire_um),IntType,CallExpr(Self(),Id(tire_num),[FieldAccess(Id(this),Id(car))])))])])'
        self.assertTrue(TestAST.test(input, expect, 376))

    def test_377(self):
        input = '''
        Class A{}

        Class B{
            Val $_ : Float;
            }

        Class F6_{
            Val $P_X_, $_, $91 : String;
        }
        '''
        expect = 'Program([ClassDecl(Id(A),[]),ClassDecl(Id(B),[AttributeDecl(Static,ConstDecl(Id($_),FloatType,None))]),ClassDecl(Id(F6_),[AttributeDecl(Static,ConstDecl(Id($P_X_),StringType,None)),AttributeDecl(Static,ConstDecl(Id($_),StringType,None)),AttributeDecl(Static,ConstDecl(Id($91),StringType,None))])])'
        self.assertTrue(TestAST.test(input, expect, 377))

    def test_378(self):
        input = '''
        Class A{
            $func(a_a, b_b, c_c : Int){
                Return;
                Return !!!!!! New _().B52();
                {}
                Continue;
            }
        }    
        '''
        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id($func),Static,[param(Id(a_a),IntType),param(Id(b_b),IntType),param(Id(c_c),IntType)],Block([Return(),Return(UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,UnaryOp(!,CallExpr(NewExpr(Id(_),[]),Id(B52),[])))))))),Block([]),Continue]))])])'
        self.assertTrue(TestAST.test(input, expect, 378))

    def test_379(self):
        input = '''
        Class Shape{
            Var $Circle : Array[Array[Array[Boolean, 023],50],0XE_62];
        }
        '''
        expect = 'Program([ClassDecl(Id(Shape),[AttributeDecl(Static,VarDecl(Id($Circle),ArrayType(3682,ArrayType(50,ArrayType(19,BoolType)))))])])'
        self.assertTrue(TestAST.test(input, expect, 379))

    def test_380(self):
        input = '''
        Class Book{
            Val $Page: Array[String, 0X34122];
            Constructor(){}
            addBook(book: Array[String, 01231_2]){
                Book::$arr[0] = "Hello World";
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Book),[AttributeDecl(Static,ConstDecl(Id($Page),ArrayType(213282,StringType),None)),MethodDecl(Id(Constructor),Instance,[],Block([])),MethodDecl(Id(addBook),Instance,[param(Id(book),ArrayType(5322,StringType))],Block([AssignStmt(ArrayCell(FieldAccess(Id(Book),Id($arr)),[IntLit(0)]),StringLit(Hello World))]))])])'
        self.assertTrue(TestAST.test(input, expect, 380))

    def test_381(self):
        input = '''
        Class Device{
                Var weight: Float = 0.0;
                Var smart: Boolean = False;
        }
        '''
        expect = 'Program([ClassDecl(Id(Device),[AttributeDecl(Instance,VarDecl(Id(weight),FloatType,FloatLit(0.0))),AttributeDecl(Instance,VarDecl(Id(smart),BoolType,BooleanLit(False)))])])'
        self.assertTrue(TestAST.test(input, expect, 381))

    def test_382(self):
        input = '''
        Class Device{
            Var weight: Float = 0.0;
            Var smart: Boolean = False;
        }

        Class Router:Device{
            start(){
                    Return Self.status();
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Device),[AttributeDecl(Instance,VarDecl(Id(weight),FloatType,FloatLit(0.0))),AttributeDecl(Instance,VarDecl(Id(smart),BoolType,BooleanLit(False)))]),ClassDecl(Id(Router),Id(Device),[MethodDecl(Id(start),Instance,[],Block([Return(CallExpr(Self(),Id(status),[]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 382))

    def test_383(self):
        input = '''
        Class Router:Device{
            start(){
                    Return Self.status();
            }

            status(){
                Continue;
            }

             $Refresh(){
                Foreach(i In _::$quantity .. 0 By -1){}
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Router),Id(Device),[MethodDecl(Id(start),Instance,[],Block([Return(CallExpr(Self(),Id(status),[]))])),MethodDecl(Id(status),Instance,[],Block([Continue])),MethodDecl(Id($Refresh),Static,[],Block([For(Id(i),FieldAccess(Id(_),Id($quantity)),IntLit(0),UnaryOp(-,IntLit(1)),Block([])])]))])])'
        self.assertTrue(TestAST.test(input, expect, 383))

    def test_384(self):
        input = '''
        Class Computer{
            display(){
                Self.print();
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Computer),[MethodDecl(Id(display),Instance,[],Block([Call(Self(),Id(print),[])]))])])'
        self.assertTrue(TestAST.test(input, expect, 384))

    def test_385(self):
        input = '''
        Class Sound:Computer{
            startMusic(link : String){
                Self.start = True;
                Break;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Sound),Id(Computer),[MethodDecl(Id(startMusic),Instance,[param(Id(link),StringType)],Block([AssignStmt(FieldAccess(Self(),Id(start)),BooleanLit(True)),Break]))])])'
        self.assertTrue(TestAST.test(input, expect, 385))

    def test_386(self):
        input = '''
        Class Clock:Computer{
            func(){
                Foreach(i In real_time .. 0 By 1){
                    ABC::$DoSth();
                    Continue;
                }
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Clock),Id(Computer),[MethodDecl(Id(func),Instance,[],Block([For(Id(i),Id(real_time),IntLit(0),IntLit(1),Block([Call(Id(ABC),Id($DoSth),[]),Continue])])]))])])'
        self.assertTrue(TestAST.test(input, expect, 386))

    def test_387(self):
        input = '''
        Class Example{
            run(){
                Var r, s: Int;
                r = 2.0;
                Var a, b: Array[Int, 5];
                s = r * r * Self.myPI;
                a[0] = s;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Example),[MethodDecl(Id(run),Instance,[],Block([VarDecl(Id(r),IntType),VarDecl(Id(s),IntType),AssignStmt(Id(r),FloatLit(2.0)),VarDecl(Id(a),ArrayType(5,IntType)),VarDecl(Id(b),ArrayType(5,IntType)),AssignStmt(Id(s),BinaryOp(*,BinaryOp(*,Id(r),Id(r)),FieldAccess(Self(),Id(myPI)))),AssignStmt(ArrayCell(Id(a),[IntLit(0)]),Id(s))]))])])'
        self.assertTrue(TestAST.test(input, expect, 387))

    def test_388(self):
        input = '''
        Class AI{
            CNN(){
                Foreach (row In 1 .. 256 By 1){
                        Foreach (col In 256 .. 1 By -1){
                            Foreach (channel In 1 .. 3 By 1){
                                Self.addMatrix[row][col][channel] = Self.matrix[row][col][channel];
                                Self.addMatrix[row + 256][col][channel] = Self.matrix[row][col][channel];
                            } 
                        }
                }
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(AI),[MethodDecl(Id(CNN),Instance,[],Block([For(Id(row),IntLit(1),IntLit(256),IntLit(1),Block([For(Id(col),IntLit(256),IntLit(1),UnaryOp(-,IntLit(1)),Block([For(Id(channel),IntLit(1),IntLit(3),IntLit(1),Block([AssignStmt(ArrayCell(FieldAccess(Self(),Id(addMatrix)),[Id(row),Id(col),Id(channel)]),ArrayCell(FieldAccess(Self(),Id(matrix)),[Id(row),Id(col),Id(channel)])),AssignStmt(ArrayCell(FieldAccess(Self(),Id(addMatrix)),[BinaryOp(+,Id(row),IntLit(256)),Id(col),Id(channel)]),ArrayCell(FieldAccess(Self(),Id(matrix)),[Id(row),Id(col),Id(channel)]))])])])])])])]))])])'
        self.assertTrue(TestAST.test(input, expect, 388))

    def test_389(self):
        input = '''
        Class Program {
            main() {
                Foreach (i In 0 .. 1000 By 1) {
                    If (i == 100) {
                        Continue;
                        Break;
                        Return;
                    } 
                    Else {
                        i = i +. 1;
                    }
                }
                Self.print(a.b.func());
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(i),IntLit(0),IntLit(1000),IntLit(1),Block([If(BinaryOp(==,Id(i),IntLit(100)),Block([Continue,Break,Return()]),Block([AssignStmt(Id(i),BinaryOp(+.,Id(i),IntLit(1)))]))])]),Call(Self(),Id(print),[CallExpr(FieldAccess(Id(a),Id(b)),Id(func),[])])]))])])'
        self.assertTrue(TestAST.test(input, expect, 389))

    def test_390(self):
        input = '''
        Class Program{
            main(){
                    Foreach(i In 0 .. i < R1 By i + 1){
                        Foreach(j In 0 .. j < C2 By j + 1){
                            rslt[i][j] = 0;
                            Foreach(k In 0 .. j < R2 By k + 1){
                                rslt[i][j] = rslt[i][j] + mat1[i][k] * mat2[k][j];
                            }
                            System.print(rslt);
                        }
                    }
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([For(Id(i),IntLit(0),BinaryOp(<,Id(i),Id(R1)),BinaryOp(+,Id(i),IntLit(1)),Block([For(Id(j),IntLit(0),BinaryOp(<,Id(j),Id(C2)),BinaryOp(+,Id(j),IntLit(1)),Block([AssignStmt(ArrayCell(Id(rslt),[Id(i),Id(j)]),IntLit(0)),For(Id(k),IntLit(0),BinaryOp(<,Id(j),Id(R2)),BinaryOp(+,Id(k),IntLit(1)),Block([AssignStmt(ArrayCell(Id(rslt),[Id(i),Id(j)]),BinaryOp(+,ArrayCell(Id(rslt),[Id(i),Id(j)]),BinaryOp(*,ArrayCell(Id(mat1),[Id(i),Id(k)]),ArrayCell(Id(mat2),[Id(k),Id(j)]))))])]),Call(Id(System),Id(print),[Id(rslt)])])])])])]))])])'
        self.assertTrue(TestAST.test(input, expect, 390))

    def test_391(self):
        input = '''
        Class Program{
            main(){
                If(C1 != C2){
                    Break;
                    Self.Exit(EXIT_FAILURE);
                    Return;
                }
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([If(BinaryOp(!=,Id(C1),Id(C2)),Block([Break,Call(Self(),Id(Exit),[Id(EXIT_FAILURE)]),Return()]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 391))

    def test_392(self):
        input = '''
        Class Program {
            main() {
                (Self[0]).func();
                Self[1] = "Hello World";
                Out.println(Self.arr[1]);
                ((((a[1][2][3]).a[4][5]).func()[arr[0]]).a[1]).func();
                Return;
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(ArrayCell(Self(),[IntLit(0)]),Id(func),[]),AssignStmt(ArrayCell(Self(),[IntLit(1)]),StringLit(Hello World)),Call(Id(Out),Id(println),[ArrayCell(FieldAccess(Self(),Id(arr)),[IntLit(1)])]),Call(ArrayCell(FieldAccess(ArrayCell(CallExpr(ArrayCell(FieldAccess(ArrayCell(Id(a),[IntLit(1),IntLit(2),IntLit(3)]),Id(a)),[IntLit(4),IntLit(5)]),Id(func),[]),[ArrayCell(Id(arr),[IntLit(0)])]),Id(a)),[IntLit(1)]),Id(func),[]),Return()]))])])'
        self.assertTrue(TestAST.test(input, expect, 392))

    def test_393(self):
        input = '''
        Class Program {
            main()
            {
                Val list : LinkedList = New LinkedList();
                list.head = New Node(1);
                list.head.next = New Node(0x12F3);
                list.head.next.next = New Node(0B101);
                list.head.next.next.next = New Node(0312412);
                System.out.println("Given Linked list");
                list.printList(head);
                head = list.reverse(head);
                System.out.println("Newline");
                System.out.println("Reversed linked list ");
                list.printList(tail);
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([ConstDecl(Id(list),ClassType(Id(LinkedList)),NewExpr(Id(LinkedList),[])),AssignStmt(FieldAccess(Id(list),Id(head)),NewExpr(Id(Node),[IntLit(1)])),AssignStmt(FieldAccess(FieldAccess(Id(list),Id(head)),Id(next)),NewExpr(Id(Node),[IntLit(4851)])),AssignStmt(FieldAccess(FieldAccess(FieldAccess(Id(list),Id(head)),Id(next)),Id(next)),NewExpr(Id(Node),[IntLit(5)])),AssignStmt(FieldAccess(FieldAccess(FieldAccess(FieldAccess(Id(list),Id(head)),Id(next)),Id(next)),Id(next)),NewExpr(Id(Node),[IntLit(103690)])),Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Given Linked list)]),Call(Id(list),Id(printList),[Id(head)]),AssignStmt(Id(head),CallExpr(Id(list),Id(reverse),[Id(head)])),Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Newline)]),Call(FieldAccess(Id(System),Id(out)),Id(println),[StringLit(Reversed linked list )]),Call(Id(list),Id(printList),[Id(tail)])]))])])'
        self.assertTrue(TestAST.test(input, expect, 393))

    def test_394(self):
        input = '''
        Class Program {
            $foo() {
                Self.A = Array(1, 02312 + a, a * b);
                a[1.3412e-3][(i - j)][0x10] = c[i][k] + b[1][(j+1)][(k - 1412)][123];

                Self.System.Out(a.a);
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Program),[MethodDecl(Id($foo),Static,[],Block([AssignStmt(FieldAccess(Self(),Id(A)),[IntLit(1),BinaryOp(+,IntLit(1226),Id(a)),BinaryOp(*,Id(a),Id(b))]),AssignStmt(ArrayCell(Id(a),[FloatLit(0.0013412),BinaryOp(-,Id(i),Id(j)),IntLit(16)]),BinaryOp(+,ArrayCell(Id(c),[Id(i),Id(k)]),ArrayCell(Id(b),[IntLit(1),BinaryOp(+,Id(j),IntLit(1)),BinaryOp(-,Id(k),IntLit(1412)),IntLit(123)]))),Call(FieldAccess(Self(),Id(System)),Id(Out),[FieldAccess(Id(a),Id(a))])]))])])'
        self.assertTrue(TestAST.test(input, expect, 394))

    def test_395(self):
        input = '''
        Class iPhone:Apple{
                Val $os: String = "iOS";
                Var IMEI: String; 
                Var $phone_number: Int;
                Var $phone: Array[Boolean, 100];
                insertSIM(sim: SIM){
                    Self.phone_number = SIM.number;
                }
                detachSIM(){
                    Self.phone_number = Null;
                }
        }
        '''
        expect = 'Program([ClassDecl(Id(iPhone),Id(Apple),[AttributeDecl(Static,ConstDecl(Id($os),StringType,StringLit(iOS))),AttributeDecl(Instance,VarDecl(Id(IMEI),StringType)),AttributeDecl(Static,VarDecl(Id($phone_number),IntType)),AttributeDecl(Static,VarDecl(Id($phone),ArrayType(100,BoolType))),MethodDecl(Id(insertSIM),Instance,[param(Id(sim),ClassType(Id(SIM)))],Block([AssignStmt(FieldAccess(Self(),Id(phone_number)),FieldAccess(Id(SIM),Id(number)))])),MethodDecl(Id(detachSIM),Instance,[],Block([AssignStmt(FieldAccess(Self(),Id(phone_number)),NullLiteral())]))])])'
        self.assertTrue(TestAST.test(input, expect, 395))

    def test_396(self):
        input = '''
        Class Smart:Home{
            Val $Camera : Module;
            detect(Camera : Module){
                If(Self.detect() == True){
                    Return True;
                }
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Smart),Id(Home),[AttributeDecl(Static,ConstDecl(Id($Camera),ClassType(Id(Module)),None)),MethodDecl(Id(detect),Instance,[param(Id(Camera),ClassType(Id(Module)))],Block([If(BinaryOp(==,CallExpr(Self(),Id(detect),[]),BooleanLit(True)),Block([Return(BooleanLit(True))]))]))])])'
        self.assertTrue(TestAST.test(input, expect, 396))

    def test_397(self):
        input = '''
        Class Smart:Home{
            Val $Camera : Module;
            detect(Camera : Module){
                If(Self.detect() == True){
                    Return True;
                }
                Else{
                    Return False;
                }
                Break;
            }
            func(){
                Self.DoSth();
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Smart),Id(Home),[AttributeDecl(Static,ConstDecl(Id($Camera),ClassType(Id(Module)),None)),MethodDecl(Id(detect),Instance,[param(Id(Camera),ClassType(Id(Module)))],Block([If(BinaryOp(==,CallExpr(Self(),Id(detect),[]),BooleanLit(True)),Block([Return(BooleanLit(True))]),Block([Return(BooleanLit(False))])),Break])),MethodDecl(Id(func),Instance,[],Block([Call(Self(),Id(DoSth),[])]))])])'
        self.assertTrue(TestAST.test(input, expect, 397))

    def test_398(self):
        input = '''
        Class Smart:Home{
            Val $Camera : Module;
            detect(Camera : Module){
                If(Self.detect() == True){
                    Return True;
                }
                Else{
                    Return False;
                }
                Break;
            }
            func(){
                Self.DoSth();
                Foreach(i In Device .. 0 By 0x123){}
                Foreach(i In Device.ABC() .. 0){}
                If(1){}
                Elseif(2){}
                Else{}
                lhs = "Hello World";
                {{{{{{{{{{}}}}}}}}}}
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Smart),Id(Home),[AttributeDecl(Static,ConstDecl(Id($Camera),ClassType(Id(Module)),None)),MethodDecl(Id(detect),Instance,[param(Id(Camera),ClassType(Id(Module)))],Block([If(BinaryOp(==,CallExpr(Self(),Id(detect),[]),BooleanLit(True)),Block([Return(BooleanLit(True))]),Block([Return(BooleanLit(False))])),Break])),MethodDecl(Id(func),Instance,[],Block([Call(Self(),Id(DoSth),[]),For(Id(i),Id(Device),IntLit(0),IntLit(291),Block([])]),For(Id(i),CallExpr(Id(Device),Id(ABC),[]),IntLit(0),IntLit(1),Block([])]),If(IntLit(1),Block([]),If(IntLit(2),Block([]),Block([]))),AssignStmt(Id(lhs),StringLit(Hello World)),Block([Block([Block([Block([Block([Block([Block([Block([Block([Block([])])])])])])])])])])]))])])'
        self.assertTrue(TestAST.test(input, expect, 398))

    def test_399(self):
        input = '''
        Class Shape {
            Val $numOfShape: Int = 0;
            Val immutableAttribute: Int = 0;
            Var length, width: Int;
            $getNumOfShape() {
                Return numOfShape.func();
            }
        }

        Class Rectangle: Shape {
            getArea() {
                Return Self.length * Self.width;
            }
        }

        Class Program {
            main() {
            Out.printInt(Shape::$numOfShape);
            }
        }
        '''
        expect = 'Program([ClassDecl(Id(Shape),[AttributeDecl(Static,ConstDecl(Id($numOfShape),IntType,IntLit(0))),AttributeDecl(Instance,ConstDecl(Id(immutableAttribute),IntType,IntLit(0))),AttributeDecl(Instance,VarDecl(Id(length),IntType)),AttributeDecl(Instance,VarDecl(Id(width),IntType)),MethodDecl(Id($getNumOfShape),Static,[],Block([Return(CallExpr(Id(numOfShape),Id(func),[]))]))]),ClassDecl(Id(Rectangle),Id(Shape),[MethodDecl(Id(getArea),Instance,[],Block([Return(BinaryOp(*,FieldAccess(Self(),Id(length)),FieldAccess(Self(),Id(width))))]))]),ClassDecl(Id(Program),[MethodDecl(Id(main),Static,[],Block([Call(Id(Out),Id(printInt),[FieldAccess(Id(Shape),Id($numOfShape))])]))])])'
        self.assertTrue(TestAST.test(input, expect, 399))

    def test_400(self):
        input = '''
        Class A{
            Destructor(){
            Return;_9::$g3k.m();
            } 
        }

        Class A1:A{}

        Class A2:A{
           func_1(){
                Name = "BKU";
           }
           func_2(){
                Slogan = "vjp pro no 1";
           }
        } 
        '''
        expect = 'Program([ClassDecl(Id(A),[MethodDecl(Id(Destructor),Instance,[],Block([Return(),Call(FieldAccess(Id(_9),Id($g3k)),Id(m),[])]))]),ClassDecl(Id(A1),Id(A),[]),ClassDecl(Id(A2),Id(A),[MethodDecl(Id(func_1),Instance,[],Block([AssignStmt(Id(Name),StringLit(BKU))])),MethodDecl(Id(func_2),Instance,[],Block([AssignStmt(Id(Slogan),StringLit(vjp pro no 1))]))])])'
        self.assertTrue(TestAST.test(input, expect, 400))




def printComparison(number: int, expected: str):
    solution_path = "C:/Users/Admin/Desktop/P/BK/212/Principles of Programming Languages/Assignment/ppl/assignment 2/code/src/test/solutions/" + str(number) + ".txt"
    print(solution_path)
    f = open(solution_path, "r")
    solution = f.read()
    f.close()
    print(44 * '-' + ' COMPARASION RESULT: ' + str(solution == expected).upper() + ' ' + 44 * '-')
    if (solution != expected):
        length = len(solution) if len(solution) < len(expected) else len(expected)
        position = 0
        for idx in range(length):
            if solution[idx] == expected[idx]:
                position += 1
            else:
                break
        print('* * * * * CHARACTER ' + str(position) + ' ' + solution[position] + ' * * * * *')
        print(50 * '-' + ' SOLUTION: ' + str(len(solution)) + ' ' + 50 * '-')
        print(solution[:position + 1])
        print(50 * '-' + ' EXPECTED: ' + str(len(expected)) + ' ' + 50 * '-')
        print(expected[:position + 1])
    return
