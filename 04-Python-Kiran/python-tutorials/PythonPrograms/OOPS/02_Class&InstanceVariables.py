# A class variable is a static variable because no instance creation is required and it is bound to class.
# Instance Variables
# A variable that is defined inside a method and belongs only to the current instance of a class.
# For each object that is been created a separate copy will be created in memory.
# The scope of the instance variables that's been passed as arguments will be available to all the methods of the class.
# Instance variable will be prefixed with key word "self" and then only it can be available to all the methods and out side of the class.
# Instance Variable are independent of each object and change in once instance variable will not affect other instance variable.
# Instance variable from a method can only be accessible only when that method is called.

class Student:
    def __init__(self,name,rollno,marks): # Implicit Initialization of instance Variables no explicit method call required.
        self.n=name
        self.rollno=rollno
        self.marks=marks
        temp=name

    def display(self):
        print("Displaying from method",self.n,self.rollno,self.marks)
        # print("temp variable",temp)  # temp is not instance variable hence not able to print.

s1=Student('Kiran',501,600)
s1.display()
print("Printing the Instance Var out of the class=",s1.n,s1.rollno,s1.marks,sep=',')
print(s1.__dict__)

# Instance Variable initialization explicitly via method call.
# Here comes constructor method to initialize instance variables with out explicit method call.

class Student:
    def record(self,name,rollno,marks):
        self.n=name
        self.rollno=rollno
        self.marks=marks
        temp=name

    def display(self):
        print("Displaying from method",self.n,self.rollno,self.marks)
        # print("temp variable",temp)  # temp is not instance variable hence not able to print.

s1=Student()                # No initialisation of instance variables.
s1.record("Kiran",501,600)  # Initialisation by calling the method explicitly
print("Printing the Instance Var out of the class=",s1.n,s1.rollno,s1.marks,sep=',')


# Instance Variable are independent of each object and change in once instance variable will not affect other instance variable.

class test:
    def __init__(self):
        self.x=100

t1=test()
t2=test()
print("Before Change:",t1.x,t2.x)
t1.x=200
print("After Change: ",t1.x,t2.x)

# Class variables share the same value across all the instances of the class.
# Change of value in the class variable will reflect across all the instances.
# A class variable is a static variable because no instance creation is required to access those variables.

class test:
    v1=10
    def __init__(self):
        print("Hello i'm in constructor")

print(test.v1)  # Class variable can be directly accessed with class name with out instance creation.
t1=test()
t2=test()

print("class variable before change from object t1=",t1.v1)

print("class variable before change from object t2=",t2.v1)
test.v1=20      # Changing the class variable value.

print("class variable After change from object t1=",t1.v1)
print("class variable After change from object t2=",t2.v1)


