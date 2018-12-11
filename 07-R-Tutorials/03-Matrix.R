# Matrix Datatype is a 2-d data type.
# Matrix will have homogenous data type elements
# Matrix is created using matrix() function
# Arithematic operations b/w two matrix should be of same dimensions.
# Indexing in R starts with row and columns with 1 and in python 0.

m1= matrix(c(1:12),nrow=4,ncol=3,byrow=TRUE)    # byrow=TRUE no wil be printed in row wise.
m1
m2= matrix(c(1:12),nrow=4,ncol=3,byrow=FALSE)   # byrow=FALSE, no will be printed in col wise.
m2

m3=matrix(list(1,2,"hello",3,4.5,"abc"),nrow=3) # Passing a list of elements
m3
length(m4)
class(m4[1,1])

# Indexing the matrix 

m1[1,3]        # First row 3rd column
m1[3,]         # Third row only

# Arithematic operations on un equal Matrix dimensions.

m4=matrix(c(1:6),  nrow=3,ncol=2);  m4
m5=matrix(c(10:12),nrow=4,ncol=3);  m5

m4*m5

# Arithematic operations on equal Matrix dimensions.

m6=matrix(c(1:6),  nrow=3,ncol=2);  m6
m7=matrix(c(6:12), nrow=3,ncol=2);  m7
m6*m7

# Updating Matrix

m8=matrix(c(1:12),nrow = 4); m8
m8[1,1]=100; m8    # updating the matrix element
m8[1,]=1;    m8    # updating 1st row with ones

# Summary of Matrix

str(m8)
nrow(m8)
ncol(m8)
