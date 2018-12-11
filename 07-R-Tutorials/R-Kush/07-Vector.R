5+4
15%%5

#Assignment Operator and Assign function
x<-10
x
y="AnKush"
50->m


assign(n,20)
assign('p',70)

rm(n)  #Remove a value
rm(xm)

m

assign("x","A")                                                      #assigns the value 20 to the value in x
assign(x,40)


#print the value of any variable
x
A
print("Hello World")

#Data types and its class
a<-6L
class(a)

b<- 5+3
class(b)

d<-3<5
class(d)

e<- "abc" 
class(e)

#Special Numbers 
1/0  #Inf
-1/0 #-Inf
0/0 #NaN
NA
NULL

#Workspace - revisited
ls()                        # Display the objects in the current workspace

#Combine function --- how to multiple values in the same vector
B <- c(10,20,30,40)
D <- c(10,20,a,40)
C <- c(10,20,mn,40)
print(B)

#Arithmetic operation in R 
A <- 10
B <- 20
A+B

search()

#Vector is a homogeneous data structure... has to be of same data type 
B<-"28" 
class(B)
A<-40
A+B

#Coercion  -- What happens if we put 2 different datatypes in a vector
C <- c(10,20,"mn",40)
C
class(C)

D<- c(10,FALSE)                                  #converted to numeric  
D
class(D)

#FALSE is considered as 0 and TRUE as 1  
D<- c(10,"TRUE",NA,TRUE)          # Converted to character

#checking the class 
class(D)

#Checking for a vector
is.vector(D)


#abc<- vector(mode="numeric",x= c(40,50))
M<-1:1000 
M
class(M)
length(M)

#Creating a vector using ":" operator for range of values
#Integer vs Numeric #Why are values incremented by 1 only when we use : operator
Vector1 <- (0:6)
Vector2 <- c(0.2,-1,-2)
class(Vector1)
class(Vector2)

#VECTOR--1D --that can contain data of only 1 type
#Recursiveness#corresponding value adds up
M<- c(10,20,30,40)
N<- c(20,20,40,50)

Result<-M+N

#recursiveness along with warning
M <- c(10,20,30,40,50,60,120)
N <- c(20,30,40)

Result1<-M+N

#recursiveness with no warning
M<- c(10,20,30,40)
N<- c(20,20)
Result2<- M+N

#Creating a named vector 
#Method 1
A <- c(a=10,b=20)
A

#Method 2
B <- c(12,240)
names(B) <- c("c","b")

#Method 1#Not assigning names to every element
A<- c(a=10,b=20,b=30)

#Method 2#Not assigning names to every element
A <- c(10,20,30)
names(A) <- c("a","b")


#Finding the no. of elements
length(A)

z<- c("Asd","fda","dfa","hind")
length(z)
nchar(z)

#Subsetting a vector using square brackets []
week<- c(a="Sun",b="Mon",c="Tue",d="Thur",e="Sat")

#By Position
week[2]
week[c(3,5)]
week[2:5]

#By Name
week["a"]
week[c("b","d")]

#By Logical vector
week[c(T,F,F,T,F)]
week[c(T,F)]

#Dropping values 
week[-2]
week[c(-1,-2)]
week[c(T,T,F)]

#PROBLEM
#In a gambling game,my win/loss at two location(A & B)
#You need to create two named vectors A and B 
#Mon = Location A won 100   #Location B = lost 50
#Tue = Location A won 70    #Location B = won 60
#Wed = Location A lost 50   #Location B = won 80
#Thurs = Location  A won 20  #Location B = Lost 30


#Method 1
A<- c(Mon=100,Tue=70,Wed=-50,Thurs=20)
B<-c(Mon=-50,Tue=60,Wed=80,Thurs=-30)

#Method 2
A<- c(100,70,-50,20)
names(A)<- c("Mon","Tue","Wed","Thurs")


B<- c(-50,60,80,-30)
names(B)<- c("Mon","Tue","Wed","Thurs")

#Get only the winning amount from A #and Losing amount from B
A[A>0]
B[B<0]



#Find the Net win/loss on Monday
A["Mon"]+B["Mon"]

#Total amount won at location A
sum(A[A>0])

#Total amount lost at location A
sum(A[A<0])    

#Highest winning amount at location A
max(A)        

#Highest losing amount at location A
min(A) 

#What happens when we use [[]] in a named vector
A[2]
A[[2]]

class(A)

#Explicit Coercion
A<-as.character(A)
class(as.character(A))
A<-as.numeric(A)

#Explicit Coercion
Vector1<- 1:6
Vector1<- as.numeric(Vector1)
class(Vector1)
is.numeric(Vector1)
is.logical(Vector1)

Vector2 <- c(0.9999,-1,-2)
Vector2<- as.integer(Vector2)
class(Vector2)

z<- c("10","20","30") 
class(z)
as.numeric(z)
as.integer(z)

z<- c("do","20","30")      
Z<-as.numeric(z)   
as.character(Z)
as.logical(z)


Logical_vector <- c(T,F,T,F)
Logical_vector<- as.numeric(Logical_vector)
class(Logical_vector)

#Manipulating the vector 
#add a new value to the vector
A[5]<- 100
length(A)
A[8]<- -20
A[1]<-600

names(A) <- "wed"
names(A)<- letters[1:length(A)]


B<- c(10,20,20,40)
names(B)<- c("a","b")

B<- c(a=10,b=20,20,40)
names(B)[2] <- "red"


c(A[1:3],55,A[4:length(A)])
append(A,45, after=3)

#append 10 to vector1 at the end
A<-c(10,A)
A[(length(A))+1] <- 200

#append a value 20 at position 5 in the vector "Vector1"
A<-c(A[1:4],20,A[5:length(A)])

#using append function
append(A,90,length(A))
append(A,c(1000,100,200,30),6)
