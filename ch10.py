# Modules

""" https://docs.python.org/library - Python Library Reference, which describes all of the modules in the standard library."""

import math
print(math.sin(9))

def hello():
    print("Comment allez vous? - study more french, you bastard.")

#CMD : cd C:\Users\username\OneDrive\Desktop\Work\Python 

#python
#import ch10
#ch10.hello()

#git status
#git pull
#git add 
#git commit -m ""
#git push

#import sys
#sys.path.append("path") - look for modules inside this directory

#import sys, pprint
#pprint.pprint(sys.path) - save modules on the "site-packages" directory : "As long as your module is located in a place like site-packages, all your programs will be able to import it"

print(range.__doc__) #shows the documentation of a module to help in its usage

import copy
print(copy.__doc__)
print(copy.__file__) #path of the module .py file

""" 
sys: A module that gives you access to several variables and
functions that are tightly linked with the Python interpreter.

os: A module that gives you access to several variables and
functions that are tightly linked with the operating system. 

"""







