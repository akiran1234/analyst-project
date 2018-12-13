# LEGB Rule <Local, Enclosed, Global, Builtin> Variables.
# Order of execution of variable will be first it checks locally then enclosed function then globally then builtin variables.
# There is a concept of Namespace where each module and it's functions and nested functions will have it's own
# .. namespace and isolated to each other.
# Here x='Global' is a global variable with in the scope of this it's module and visible to to it's
# .. functions and nested functions.
# View builtin variables import builtins; print(dir(builtins))
# "global" keyword defined in enclosed function and inner function to change the global variables values.
# "nonlocal" keyword defined in local/inner function to change enclosed variable value.


x='Global'

def outer():
    x='Outer Function Variable'   # Comment and try to print, it refers to global variable.
    print(x)   # This x is local to outer() function if x is commented it refers to enclosed and then global.
               # Since there is no enclosed function it will refer to global variable x.
outer()

print("**********************")

#######################################################################################
# Changing the value of global variable inside the function by using key word "global".

y=10

def valchange():
    global y
    y=30
    print("Printing y value in Valchange function y=",y)
print("Printing the global variable value before change y=",y)
valchange()
print("Printing the global variable value after change y=",y)

print("**********************")

#######################################################################################
# Changing the value of variable in enclosed function by using key word "nonlocal".

z=100

def outer():
    z=200                                           # Comment and try to print, it refers to global variable.
    print("Enclosed function z before change =",z)  # This x is local to outer() function if x is commented it refers to enclosed and then global.
                                                    # Since there is no enclosed function it will refer to global variable z.
    def inner():
        nonlocal z
        z = 300
        print("Inner function z=",z)

    inner()
    print("Enclosed function z after change =", z)

outer()
print("Printing global variable z=",z)


print("**********************")