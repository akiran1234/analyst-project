#####################################################################################################################
# Python Features
# Interpreted, OOPS,  Readability (Indentation), Portable, Easy to Learn, Open Source, Vast Libraries
# Dynamically Typed - No data type declaration (Data type is decided by the interpreter at run time)
#####################################################################################################################
# Identifiers are the names given to entities like  Variables, functions and classes ..
# Identifiers can be a combination of letters in lowercase (a to z) or uppercase (A to Z) or digits (0 to 9) or an underscore (_).
# Names like myClass, var_1 and print_this_to_screen, all are valid example.
# An identifier cannot start with a digit. 1variable is invalid, but variable1 is perfectly fine.
# Keywords cannot be used as identifiers.
# We cannot use special symbols like !, @, #, $, % etc. in our identifier.
# https://www.programiz.com/python-programming/keywords-identifier -- Reference
# Python Naming Convention --- http://visualgit.readthedocs.io/en/latest/pages/naming_convention.html#general
# https://data-flair.training/blogs/python-tutorial/ -- Refer for python
# Python is a pure OOPS Language- modules,variables,functions,classes. type(object) will return the object class.
# https://www.jetbrains.com/help/pycharm/symbols.html  -- pycharm symbol reference
# By default python is executed in  Cpython i.e it will compile the code to C based byte code and this byte code is converted into binary code which machine can be understood.
# https://www.toptal.com/python/why-are-there-so-many-pythons
import platform; 
print(platform.python_implementation())  # To check if it is Cpython or Jython or other compilers.
# Python private heap space - All Python objects and data structures are located in a private heap. The programmer does not have access to this private heap. The python interpreter takes care of this instead.
# Python also has an inbuilt garbage collector, which recycles all the unused memory and so that it can be made available to the heap space.

count = 10
print("Printing the value of count", count)

# Literal can be defined as data that is given in a variable/constant. Here 10 is the literal to variable count.

#####################################################################################################################
# Commenting a line in a Python can be done by placing "#" before the statement; This is single line comment.
''' This is a multi line
comment is python '''
# Indentation represents no braces {} to indicate block of code
# Quotations in Python
# Python accepts single ('), double (") and triple (''' or """) quotes
# If quote starts with single/double/triple it should end with single/double/triple.

print('This quote starts and ends with single quote')
print("This quote starts and ends with double quote")
print('''This quote starts and ends with triple quotes''')

#####################################################################################################################
# A statement can be divided into multi line statements by placing back slash \

print("This is multi line \
statement")

print(1+2+\
      3)

#####################################################################################################################
print("Semicolon (;) at the end of the statement in Python is optional");
print("Multiple statements can be executed in a single line by separating with ;")
print(1+2); print(5+6);print("Printing multiple statements in a single line by placing ;")

#####################################################################################################################
# Reading data from standard input (keyboard) and display on standard output using print() function.
# print() is a function belongs to builtins module.
# Reading data using input() function, by default it will read as string.
# input(): If an integer input is passed as command line Arg it has to be typed casted as a= int(input("Enter the value"))
# In python 3 input() will read as string.
# Even an integer value of 10 is entered or a list is entered its type will be of string only.

str1=input()                                                        # Execute in a separate script for better understanding; input= read in linux.
print("Printing from the standard input function:",type(str1),str1) # Printing standard output on screen



#####################################################################################################################
# Command line arguments pending

########### Python Architecture ############################
# Python is an interpreted language it will read each line and execute.
# Each script in python is a module.
# Module will have variables, functions and classes.
# Modules can be imported from the library path and it's attributes like variables, functions and classes can be utilized.

dir()              	   # is a function to get the list of hidden attributes/functions used in the module.
print(dir(object))     # s='string' s is object of string class. To list the methods of class string: dir(s).

abs.__doc__            # This will print the doc string for the abs function.
id(object)             # This will return the address of object. a=10; type(a)- This will return the address of object a.

# this help function we dont use much.
help('modules')        # run this help function - will list all the available modules in the library.
help('modulename')     # Ex: help('re')--> will give the list of functions available in the module.

# modules path         # C:\Program Files\Python36\Lib in windows.
# module index         # https://docs.python.org/3/py-modindex.html

print("Linux","Python","AWS",sep="|",end=':') # sep= out put separator and end=\n or some indicator.

# Python Standards

# Python packages & modules should have small names. (module_name, package_name)
# Class Names should be Capwords. (ClassName)
# method names should start with small case. (method_name)
# function names should start with small case. (function_name)
# GLOBAL_CONSTANT_NAME, global_var_name, instance_var_name,  function_parameter_name,  local_var_name.
# Maximum line length should be 79 chars
# Indentation should have 4 spaces.
# importing modules should be on separate lines.



