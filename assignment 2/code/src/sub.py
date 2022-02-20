import os
import shutil
os.system('python run.py gen')
try:
    os.mkdir("../submission")
except:
    print("The folder submission already created")

try:
    d96_path = 'main/d96/parser/D96.g4'
    AST_path = 'main/d96/astgen/ASTGeneration.py'
    ASTSuite_path = 'test/ASTGenSuite.py'

    shutil.copy(d96_path, '../submission/D96.g4')
    shutil.copy(AST_path, '../submission/ASTGenerator.py')
    shutil.copy(ASTSuite_path, '../submission/ASTGenSuite.py')

    print("Gen successfully")
except:
    print("Gen failed")
