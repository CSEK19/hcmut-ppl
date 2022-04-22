import os
import shutil
os.system('python run.py gen')

try:
    os.mkdir("../submission")
    print("Create folder submission")
except:
    print("The folder submission already created")

try:
    D96 = 'main/d96/parser/D96.g4'
    D96_interp = '../target/D96.interp'
    D96_tokens = '../target/D96.tokens'
    D96Lexer_interp = '../target/D96Lexer.interp'
    D96Lexer_tokens = '../target/D96Lexer.tokens'
    ASTGeneration = 'main/d96/astgen/ASTGeneration.py'
    ASTGenSuite = 'test/ASTGenSuite.py'
    Lexer = '../target/D96Lexer.py'
    Parser = '../target/D96Parser.py'
    Visitor = '../target/D96Visitor.py'

    shutil.copy(D96, '../submission/D96.g4')
    shutil.copy(ASTGeneration, '../submission/ASTGeneration.py')
    shutil.copy(ASTGenSuite, '../submission/ASTGenSuite.py')
    shutil.copy(Lexer, '../submission/D96Lexer.py')
    shutil.copy(Parser, '../submission/D96Parser.py')
    shutil.copy(Visitor, '../submission/D96Visitor.py')
    shutil.copy(D96_interp, '../submission/D96.interp')
    shutil.copy(D96_tokens, '../submission/D96.tokens')
    shutil.copy(D96Lexer_interp, '../submission/D96Lexer.interp')
    shutil.copy(D96Lexer_tokens, '../submission/D96Lexer.tokens')

    print("Gen 10 files successfully")
except:
    print("Gen failed")
