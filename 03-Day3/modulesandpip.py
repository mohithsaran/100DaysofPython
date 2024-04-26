# Module is like a code library which can be used to borrow code written by somebody else in our python program. There are two types of modules in python:

# Built in Modules - These modules are ready to import and use and ships with the python interpreter. there is no need to install such modules explicitly.
# External Modules - These modules are imported from a third party file or can be installed using a package manager like pip or conda. Since this code is written by someone else, we can install different versions of a same module with time.
# The pip command
# It can be used as a package manager pip to install a python module. Lets install a module called pandas using the following command

# pip install pandas
#import the module
#import pandas
#and use the pandas module

import pandas  # This is an example of external module
import hashlib  # This is an example of built in module hashlib is used to hash a string

print("Hi")

# Dont worry about how to use these modules just yet!
pandas.read_csv("one.csv")
m = hashlib.sha256()
