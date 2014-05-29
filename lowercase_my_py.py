# lower case all my py files
import os, sys

def lwr_py():

    python = os.getcwd()

    python_files = os.chdir("/home/ptrickg/python/python_files")
    python_files = os.getcwd()
    print(python)
    print(python_files)
        
    opn = '/home/ptrickg/python/python_files/animal_hangman.py'
    opnf= open(opn,'r')
    rd = opnf.read()

    # print dir path
    print(opn)
    # print contents 
    print("""


    Following is the Program


"""
          , rd)


        

    
lwr_py()
