# Numpy is the main building block used for math/scientific computation and used with rest of PyData Libraries.
# Numpy array is an n-dimensional object,1d array is called "vector" and 2d is "matrix" still matrix can have 1 row and 1 column.
# Numpy Arrays and Lists both are mutable
# List doesn't support range index assignment but Array will support Ex:  array1=[1,2,3,4,5,6]; array1=array1[0:3]=99
# We can perform math operations on each elements of Array and list will not support with out for loop.
# Array will consume very less amount of space and performance of computation on Array is higher than list.
# To perform arithmetic operations on two numpy arrays they should be of equal size.
# Numpy 1-d array are called vectors and a vector should have all the elements of same data type else elements will be type casted automatically to
# .. same data type elements.
import numpy as np

l1=[1,2,3,4]
print(type(np.array(l1)),np.array(l1))
l2=[[1,2,3],[4,5,6],[7,8,9]]
print(type(np.array(l2)),np.array(l2))

print("********************************")

# Creating an array using numpy array function.
a=np.array([10,20,30,40,50,60])
print("Type={} and a={}".format(type(a),a))

print("********************************")
# Applying Array with Array operations on array elements which is not allowed in list directly.
#

print("Addition=",a+a)
print("Multipy=",a*a) 
print("Minus=",a-a)
print("Divi=",a/a)
print("Modules=",a%a)
print("Floor=",a//a)
print(a)
print("********************************")

# Applying scalar(Arithmetic) operations with Arrays.

print("Addition with Array:",a+10)
print("Sub with Array:",     a-10)
print("Exponent with Array:",a**2)

print("********************************")
# using Numpy arange function which works like builtin range function.
a1=np.arange(10)
print("Generating random numbers={1} and type={0}".format(type(a1),a1))
print(np.arange(0,5,0.5))  # Incrementing by 0.5 which is not possible in range().
print("********************************")

# Usage of zeros and ones function to create sample data.
print("Vector of 5 zeros=",    np.zeros(5))       # 5 is the size and it will generate 5 zeros.
print("Two dimensional Array=",np.zeros((3,4)))   # pass tuple (3,4) to get 3 rows and 4 columns
print("********************************")

# Usage of zeros and ones function to create sample data.
print("Vector of 5 zeros=",    np.ones(5))        # 5 is the size and it will generate 5 zeros.
print("Two dimensional Array=",np.ones((3,2)))    # 2d Array, pass tuple (3,4) to get 3 rows and 4 columns.

print("********************************")

# Creating and dividing the sample data into equal spaces using linspace() function.
print("5 Equall spaces=",  np.linspace(0,20,5))   # Starts with 0 and ends with 20 which creates 5 equal spaces.
print("4 Equall spaces=",  np.linspace(0,20,4))   # Starts with 0 and ends with 20 which creates 4 equal spaces.

print("********************************")

# Identity Matrix - will have rows=columns and diagonal will have all ones.
print("Identity Matrix 4*4=",np.eye(3),sep='\n')  # Size = sum of ones in the diagonal.


print("********************************")
# Generate random numbers using random module of numpy library rand(), randint(), randn() functions.

print("4 Random Numbers=",              np.random.rand(4))           # Generate 4 random numbers and each item will be 0 and 1
print("5 Random Numbers between limit=",np.random.randint(10,50,5))  # Generate 5 random integers between 10 and 5.
print("3x3 Matrix with randn()",np.random.randn(3,3),sep='\n')       # Generate matrix

print("********************************")
# reshape method of array class used to create MxN matrix
re=np.arange(25)
print(re.reshape(5,5))        # this can be written as print(np.arange(25).reshape(5,5))

print("********************************")

# Numpy Array Indexing
#     c0 c1 c2
# --------------
# r0  00 01 02
# r1  10 11 12
# r2  20 21 22
# syntax array_1[row_index,col_index]    row_index and col_index can be range slicers.

arrayd=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
print("2-Array 3x4=",arrayd,sep='\n') 

print("0,1 element Method1=",arrayd[0,1],sep='\n')    # Method 1 and this is preferable;
print("0,1 element Method2=",arrayd[0][1],sep='\n')   # Method 2 Provided only row_index and col_index

print("Printng 2nd row=",arrayd[1],sep='\n')          # Printing only 2 row
print("Printng 3rd col=",arrayd[:,1],sep='\n')        # Printing only 2 column using slicer.
print("Printing 0-2 rown & 1-end column",arrayd[:2,1:],sep='\n')  # range slicer for rows and columns (Till 0-2nd row,1st column to end column)

print("********************************")

# Boolean Array

ar=np.array([1,2,3,4,5,6,7])
bol=ar>3              # bol=[False False False  True  True  True  True]
print(bol,ar[bol])    # a[bol]=[4 5 6 7]  we can simplify this to a[a>3]
print(ar[ar>3])       # This can be even applied to matrix as well

# Array Universal functions- np.sum(a),np.std(),np.min(a),np.max(a),np.argmin(a),np.argmax(a)
