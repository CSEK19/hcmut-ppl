import os
import shutil
os.system('python run.py gen')

try:
    os.mkdir("../submission")
    print("Create folder submission")
except:
    print("The folder submission already created")

try:
    CheckSuite = 'test/CheckerSuite.py'
    StaticCheck = 'main/d96/checker/StaticCheck.py'

    shutil.copy(CheckSuite, '../submission/CheckSuite.py')
    shutil.copy(StaticCheck, '../submission/StaticCheck.py')

    print("Gen 2 files successfully")
except:
    print("Gen failed")
