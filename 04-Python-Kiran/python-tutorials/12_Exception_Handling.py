# Exception Handling.
# An exception is an event, which occurs during the execution of a program that disrupts
# .. the normal flow of the program's instructions.
# Handling those un expected exception/errors in the program is called Exception Handling.
# In python by using "try" and "except" block we can handle those exceptions with out interrupting the execution.
# try block:    Contains statements that may throw different types of exceptions hence multiple except blocks is required.
# except block: Will have a block of code that will be executed when that particular exception has raised.
# else block:   If there is not exception then else block will be executed. It means try block is executed successfully .
# finally:      This finally block will be executed regardless of exception has been raised or not. This block is used for clean up activities likes- closing the opened files
# .. disconnecting the db servers or remote servers.
# except Exception: block should be the last block of multiple except blocks since this will handle any sort of exceptions.
# All the exceptions are inherited from parent class (Exception Class) either directly or indirectly.
# All the exceptions in python are classes (ZeroDivisionError, ImportError,IOError, IndexError,AttributeError) and the super class/base class is Exception class.
# ZeroDivisionError --> This exception is raised when divided by Zero.
# ImportError       --> This is raised when the module that is getting imported is not found.
# IOError           --> This is raised when the file we are trying to open is not found.
# IndexError        --> When trying to access the index which is out of size.
# AttributeError    --> If the attribute is not found.

############## Syntax ###########################
# try:
# 	execute the suspected code
# except Exception1:
# 	execute this block
# except Exception2:
# 	execute this block
# except Exception:        # This is a generic exception or base class of all Exception which can handle any sort of exceptions.
# 	execute this block
# else:
# 	execute this block if no exception. # If there is no exception then else block will be executed. It means try block is executed sucessfully .
# finally:                              # This finally block will be executed regardless of exception has been raised or not.
# 	execute this block


try:
    with open("C:/Users/PBR/Desktop/Datasets/hello1.txt",'r') as f:
        print(f.read())

except IOError:
    print("File Not available")
finally:
    print("Finally block will be executed regardless of exceptions.")


a=10
try:
    n=int(input("Please enter Numeric Input\n"))
    quotent=a/n
    print("Quotent value ={0}".format(quotent))

except ValueError:
    print("Please enter Numeric value only")
except ArithmeticError:
    print("N value is zero plz enter non zero value")
except Exception:
    print("Something went wrong!!")
else:
    print("The try block executed successfully") # If try block executed successfully then else will execute
finally:
    print("Finally block will be executed regardless of exceptions.")


print(" **********************\n")
# Raising exceptions explicitly by using raise statement.

try:
    print("Hey, I'm raising exception explicitly using raise statement")
    raise IndexError    # Raising explicitly using raise statement.

except IndexError:
    print("Index Error is caught.")