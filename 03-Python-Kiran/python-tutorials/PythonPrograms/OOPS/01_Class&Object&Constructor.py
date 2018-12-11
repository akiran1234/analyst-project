# A class is a blue print or a template which is logical in memory.
# Class Names start with Upper Word case.
# An object is instance of the class which is actual and occupies memory.
# A class is defined with key word class and object is created by calling the class name with parenthesis.
# In python object it self is passed as an argument to the class hence self is used as the first argument
# .. in constructor and all the methods of the class.
# Variables inside class are called fields and functions inside class are called methods.
# In OOP's two type of variables Class Variables, Instance Variables.

class Student:           # Creating class student with class keyword.
    def hello(self):     # Defining a method inside class
        print("I'm in student class")

s1 = Student()           # Creating an object by simply calling the class the same as function.
s1.hello()               # Calling the method with instance s1 and s1 itself is passed as an argument.
print(type(s1))          # Checking the type of object s1
print(type(s1.hello))    # Checking the type of method


# Constructor in python
# constructor is a special method in python with name __init__(self) and gets executed when ever instance is created.
# It is used to initialize the instance variables and this variables are visible to all the methods of a class.
# constructor vs method
# 1. Constructor will start with name __init__				 1. method can have any name
# 2. It is used to initialize the instance variables.        2. It is used to write business logic inside.
# 3. It is executed implicitly when ever object is created.  3. It is executed explicitly from an object.

class College:

    def __init__(self):
        print("I am a constructor,I will be executed for every instance created")

c1=College()          # constructor invoked implicitly for object creation c1 with out args.
c2=College()          # constructor invoked implicitly for object creation c2

# Invoking constructor with arguments if args not match it will throw error.

class College:

    def __init__(self,a,b):
        self.z=a+b    # This will represent c1.z=a+b for c2 object c2.z=a+b
        print("Printing sum of Instance Variables",self.z)

c1=College(10,20)     # While creating the instance itself constructor will be executed with this arguments.
print("Instance Variable",c1.z) # Accessing Instance variable outside the class



