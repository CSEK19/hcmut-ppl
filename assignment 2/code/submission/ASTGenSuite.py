import unittest
from TestUtils import TestAST
from AST import *


class ASTGenSuite(unittest.TestCase):
    def test_300(self):
        input = '''
        Class A {
        foo(){}
        }
        '''
        expect = 'Program([ClassDecl(Id(A),[])])'
        self.assertTrue(TestAST.test(input, expect, 300))

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
        expect = 'Program([ClassDecl(Id(C),[MethodDecl(Id("Constructor"),Instance,[param(Id(a),IntType)],Block([Block([]),Return(Id(D))]))])])'
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
        expect = 'Program([ClassDecl(Id(C),[MethodDecl(Id("Destructor"),Instance,[],Block([Return(Id(GG))]))])])'
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
        Class C{
            func(a : Int){
                Var x,y: Int = 1+1, 2+2;
            }
        }
        '''
        expect = ''
        self.assertTrue(TestAST.test(input, expect, 321))


