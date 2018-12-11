# Vector is the basic datastructure to hold multiple same values in a single variable.
# Vector is homogenous and it will have allways same datatype elements.
# Vector uses a function c() which combines multiple values to form one single vector.
# If a vector is assigned with different datatype elements it is automatically typecasted to single data type elements.
# A vector can hold another variables aswell
# A vector are 1-d array.
# Vectors of same size/diff size can be also applied with arthematic operatons.

v1=c(1,2,3)            # Creating a vector and it has all the same datatype elements.
v1;typeof(v1)          # Multiple statments executed in single stament like python
v2=200               
v3=c(10,20,30,v2)      # Vector holding another variable v2
v4=c(hello,10,20)      # This will check for variable hello and not found throws error.
v5=c("hello",20,30)    # Vector with string and numbers automatically tycasted to string
v5                     # All the values have been typcasted to string automatically.
v6=c(10,20,TRUE,1.5)   # Binary value and rest of the elements typecasted to decimals.
v6                     # Numeric and Binary value have become decimals.
v7=c(FALSE,1,"ab",2.0) # Typecasted to String
v7
v8=c(1:5)              # Creating a vector of sequence of elements.
v8
v9=c(6:10)
v9
v8+v9

is.vector(v9)          # Checking for a vector returns TRUE/FALSE.


# Vector arithematic Operations of un equal lengths

v14=c(1,2,3,4,5,6,7)
v15=c(1,2)            
v16=v14+v15           # Vectors are of not equal length, warning will be thrown
v16                   # Shorter vector will be recursively added to long vector.

rep(1,3)              # repeat function which repeates n times here n=3
v10=rep(1:3,4)        # here 1:3 elements repeated 4 times.
v10
v10[1]
v11=c(1:10)


# Retrivew the elements of vectors using indexing

v11[-1]               # This will ignore the first element and give all numbers not like python
v11[-1:-5]            # ignoring range of values and display rest of elements.
v11[v11>3]            # Displaying vector of elements whose values are greater than 3
v12=c(1,23,v10,v11)   # Vector holding another vector
v13=rep(1,4)
v14=rep(2,4)
v13+v14
head(v11,3)           # Display the first n elements(n=3)
tail(v11,1)           # Display the last n elements (n=1)

# Retrivew vector with labels

v17=c(a=10,b=20,c=30) # Creating a vector with labels
v17
v17["a"]              # Reading vector with labels
v17[c("a","b")]

# Retrivew vectors with binary/Logical values.
v18=c(1:10)
v18
v18[c(T,F,T,F,T,T)]   # Trues will be displayed and Flase will not displayed position starts from beginning.

# Updating & appending the Vector
v19=seq(1,5)
v19
v19[1]=200            # updating the vector
v19
v19=c(v19,100)        # Appending the vector
v19
