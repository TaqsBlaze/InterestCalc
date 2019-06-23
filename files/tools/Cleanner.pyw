import sys
import os
#
#
#This module is just a cleanner 
#it removes all the compiles files
#After exiting the programe
#Just keeping things clean

def Cleanner():

    os.chdir('files')
    os.system("del -y *.pyc ")
    os.chdir('UI')
    os.system("del -y *.pyc")
    os.chdir('../patchs')
    os.system('del -y *.pyc')
    os.chdir('../tools')
    os.system('del -y *.pyc')