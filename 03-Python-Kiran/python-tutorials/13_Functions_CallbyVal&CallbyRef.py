#################################################################################################################
# Function is a  block of code to perform specific task. Write once and use multiple times.
# Function are two types 1. Builtin functions 2. User Defined Functions
# Large programs will be sub divided into smaller chunks of code henceforth the programs will be more readable.
# Function will have function name, arguments,indention,block of statements and return type.
# Function calling should be always after the function definition in programme execution.
# A function return statement can return more than one value and the return result is a tuple.
# help('modules') # run this help function - will list all the available modules in the library.
# dir() is a builtin function to get the list of attributes/functions used in the module. Ex: dir(math)
#################################################################################################################

# function with out parameters.

def first():                                           # Function definition start with keyword  "def" followed by "fun name" and indentation (:). Def not required in bash scripting.
    """This is first function with out return stmt"""  # This is a doc string which tells the functionality of the function.
    print( "Hello this is usage of function!!" )       # Here starts the function body followed by return statement and it is optional.


print("Calling & Checking return type:",first())       # I am calling function first() whose return type is none.
print(first.__doc__)                                   # Usage of doc string. ** doc string is only for functions but not for class methods.**

print("1 **********************")
#################################################################################################################
# functions with arguments are divided into 4 categories
# 1.Default arguments  2. Required arguments   3.Keyword arguments    4.Variable length Keyword arguments

def defarg(age, name='kiran',):                   # "Non default arguments" should be always placed first and followed by "Default arguments"
    """Default argument functionality"""
    x=name;y=age+10;
    print("Name and age:",x,y,sep=',')
    return y

print(defarg(28))                                 # Function not passing name argument the defined default will be taken
print(defarg(28,'Python'))                        # Calling function arguments should be in same order of function definition

print("2 **********************")
#################################################################################################################
# 2. Required Arguments
# Required arguments are the mandatory arguments of a function. These argument values must be passed in correct number and order during function call.
# def sum(name,age): --> Defining function
#   sum('Linux',20)  --> Calling function with mandatory arguments (2) and matching data types (string,int).
#################################################################################################################
# 3. Key word Arguments
# In key word arguments, arguments will be called with keyword and  the arguments can be in any order.
#  def sum(name,age,price):
# sum(name='Unix',age=27,price=230.45)             # Calling the arguments with names assigned with values.
# sum(price=230.45,name='Unix',age=27,)            # Order of the arguments is not same with function definition.
#################################################################################################################
# 4. Variable length Arguments
# If the no of arguments that will be passed to a function is not sure then the argument should be declared as Variable length argument.

def vararg(name,*arg):
    for x in arg:
        print('Printing arguments name is:{0} and variable argument:{1}'.format(name,x))


vararg('python',10,20,30)                          # First argument ('python') will assigned to 'name' rest will be variable arguments (10,20,30).
vararg(999999,12.34,'Hello',34)                    # Name=999999, *args=12.34,'Hello',34

# Variable length keyword Args **kwargs; kwargs is a dictionary object which takes key,value pair.

def funcargs(x,**y):
    """This function will test the **kwargs """
    x=10
    for i,j in y.items():
        print("Keys and value {0}:{1}".format(i,j))
    
funcargs(10,id=10,name='Kiran',City='Blr')  # **y is a dictionary object.

#################################################################################################################
# Call by Value (Immutable objects) and Call by reference (Mutable Objects).
# Call by value: Value of the object is passed as copy hence there wont be any affect to the global variable.
# Call by Reference: Address of the object is passed as reference hence what ever the value changed
# .. inside the function will reflect outside the function.

a=50
l1=[1,2,3]
print("Before func call: a={0},add={1},l1={2},add={3}".format(a,id(a),l1,id(l1)))

def callbyval(x,l2):
    x=10;
    l2[0]=9                    # Here a,s1 are call by value and l1 is call by reference.
    print("Inside func:      x={0},add={1},l2={2},add={3}".format(x,id(x),l2,id(l2)))

callbyval(a,l1) 
# (a,x) are different copies with diff address id's and l1,l2 refer to the same mem location with same address id's.
print("Before func call: a={0},add={1},l1={2},add={3}".format(a,id(a),l1,id(l1)))

#################################################################################################################
# Global Variable and Local Variable
# A variable that is declared "out side the function" is called Global Variable.
# A variable that is declared "in  side the function" is called Local Variable.

glob=100

def testglobal():
    loc=200
    print('In testglobal function',glob,loc,'\n')

testglobal()

#################################################################################################################
# Changing the global variable inside the function.
# To change the value of global variable inside the function the variable has to be declared as global.
# The global variable  which is overridden inside the function is applicable to outside the function as well.

g=99

print('Print global before function call=',g)
def testglobal1():
    global g        # g should be declared as a global variable, to overwrite its value with in the function and the same is applicable outside the function.
    g=100
    l=200
    print('Inside testglobal1 func local and global',g,l)

testglobal1()
print('Print global after function call=',g) # Prints the value which is overridden inside the function.

#################################################################################################################
# First class functions
# A function is an instance of the Object type.
# You can store the function in a variable.
# You can pass the function as a parameter to another function.
# You can return the function from a function.
# You can store them in data structures such as hash tables, lists,
# This type of functions are called first class functions.

def display(name):
    print("Upper case=",name.upper())

x=display
x('Kiran')
print(type(x))  # here x is the instance of display function class

# Returning multiple values and return type is tuple data type.

def display(name):
    print("Upper case=",name.upper())
    x=100
    return x,name.upper()


print(type(display('Kiran')))






