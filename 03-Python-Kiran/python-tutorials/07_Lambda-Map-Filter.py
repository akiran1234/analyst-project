# Syntax: lambda var1,var2,..var(n):expression
# In traditional function we will define function with def as below and call the function by passing arguments.
# def fun_name(x,y):
#     return(x**2+y**2)
# The same functionality is simplified in to one line by reducing the code using lambda function.
# A function which doesn't have function name is called lambda/Anonymous Function.
# From the below x,y are arguments and (x**2+y**2) is an expression evaluated and returned.
# Lambda functions are used in combination with map(),filter() and reduce() builtin functions.


result = lambda x, y, z: x ** 2 + y ** 2
print(result(2, 2, 2))

x=lambda i:i*i
print(x(5))


print("**********************")
#########################################################################################
# map function will have two arguments 1. function 2.sequence/iterator (list,tuple ..)
# Syntax: map(function,iterator)
# The map(aFunction, aSequence) function applies a passed-in function to each item
# .. in an iterable object and returns a list containing all the function call results.

def sqrt(x):return(x*x)
# print("Square root value={}".format(sqrt(4)))

# Applying this function with map()
l=[1,2,3,4]
l=list(map(sqrt,l))      # Here map function maps each element to sqrt function and each element will be returned as a list of elements.
print("Map example1=",l)


# The above example will be applied with lambda function.

l1=[2,4,6,8,9]
l2=list(map(lambda x:x*x,l1))
print("Map example2=",l2)

#########################################################################################
# filter function will have two arguments 1. function 2.sequence/iterator (list,tuple ..)
# Syntax: filter(function,iterator)
# The filter(aFunction, aSequence) function applies a passed-in function to each item
# Filter works on True/False return value of function which is passed as an argument.
# .. in an iterable object and returns a list containing all the function call results.
# filter () also works the same way as map but it filters the elements based on condition.
# Syntax: filter(function,iterator)
# filter is similar to list comprehension where we can apply filter in list comprehension as well.

l3=list(filter(lambda x:x*x<30,l1))   # Filter works on True/False values of function argument.
l4=list(filter(lambda x:x%2==0,l1))
print("Filter applied",l3,l4)


l11=[1,2,3,4,5,6,7,8,9]
exp=lambda x:x>2 and x<8
print(list(map(exp,l11)))
print(list(filter(exp,l11)))

# List comprehension

l10=[1,2,3,4]
print([x*x for x in l if x*x>4])

# Reduce function is available in functools module.
# This will take two arguments 1. Function and 2. Iterable

import functools as f
r=[1,2,3,4,5,6]

print(f.reduce(lambda x,y:x+y,r)) # Here x,y values taken from list, here first two elements will be summed and then it will be summed with next element.



