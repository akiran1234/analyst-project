#IF STATEMENT

# Variables related to you
Color <- "Blue"
fb_friends <- 55

# Examine the if statement for Color
if (Color == "Blue") {
  print("The color is Blue")
}
  
# Write the if statement for fb_friends
if (fb_friends > 100) {
  print("You're popular!")
}



Color <- "Blue"
fb_friends <- 55

# Control structure for Color
if (Color == "Blue") {
  print("The Sky is Blue")
} else {
  print("Color not known")
}

# Control structure for fb_friends
if(fb_friends > 100){
  print("You're popular!")
} else {
  print("Add more friends!")
}

seq

#Vectorized IF
x <- seq(1,by=5,length.out = 10)
y <- ifelse(x<5,x,2)

# Variables related to your last day of recordings
Color <- "Red"
fb_friends <- 55

# Control structure for Color
if (Color == "Blue") {
  print("The Sky is Blue")
} else if (Color == "Red") {
  print("The book is Red")
} else {
  print("Color not known")
}

# Control structure for fb_friends
if (fb_friends > 100) {
  print("You're popular!")
} else if (fb_friends <= 100 & fb_friends > 50) {
  print("You are getting there !!!")  
} else {
  print("Add more friends!")
}

#FOR LOOP
#Understanding that i takes the values that you provide 
#in this case it is vector x
asq1 <- 0
x<- c(20,90,100,400)
for(i in x)
{
  asq1<- asq1+i
  print(asq1)
}


#Squaring the values of a randomly generated vector
a <- rnorm(20,10,1)       #random number generation of 20 values with Mean=10 and SD=1

#Squaring the vector a using the loop
asq1 <- NULL
x<- seq(1,20,1)
for(i in x) 
{
  asq1[i]<- a[i]*a[i]
}


#Print the values
asq1

#Another way to do the same thing
asq1 <- NULL
for(i in seq(1,length(a),1))
{
  asq1 <- c(asq1,a[i]*a[i])
}
print(asq1)

#Easiest way to do it
a<- a*a
a<- a^2

#Quick revision
#Matrix multiplication in R
mymat1= matrix(c(1,2,3,4), nrow=2, ncol=2, byrow=TRUE)
mymat2= matrix(c(5,6,7,8), nrow=2, ncol=2, byrow=TRUE)
compo_wise_result <- mymat1*mymat2
Mat_mul_result <- mymat1%*%mymat2

#NESTED FOR LOOP
mymat= matrix(nrow=3, ncol=3)
class(dim(mymat)[1])
dim(mymat)[2]

#Problem
#How to create a 3x3 matrix whose each component is the 
#multiplication of its row number and column number
my_mat<-matrix(0,nrow=4,ncol=4)

for(i in 1:nrow(my_mat))
{
 for(j in 1:ncol(my_mat))
 {
  my_mat[i,j] = i*j 
 }
}


#WHILE LOOP
# Initialize the speed variable
speed <- 100

# Code the while loop
while (speed > 60) {
  print("Slow down!")
  speed <- speed - 10
}

# Print out the speed variable
speed


# Initialize the speed variable
speed <- 100

# Extend/adapt the while loop
while (speed > 60) {
  print(paste("Your speed is",speed))
  if (speed > 80) {
    print("Slow down big time!")
    speed <- speed - 10
  } else {
    print("Slow down!")
    speed <- speed - 5
  }
}


# Initialize the speed variable
speed <- 61
while (speed > 60) {
  print(paste("Your speed is", speed))
  # Break the while loop when speed exceeds 80
  if (speed > 80) {
  break
  }
  if (speed > 60) {
    print("Slow down big time!")
    speed <- speed - 10
  } else {
    print("Slow down!")
    speed <- speed - 5
  }
}


#REPEAT
z <- function()
{
  readline(prompt="Please, enter  a numeric value >40: ")
}
repeat
{
  response<-as.integer(z());
  if (response > 40)
  {
    print("Well done!");
    break
  } else print("Sorry, the value MUST be greater than 40");
}

#Break
# make a lower triangular matrix (zeroes in upper right corner)
m=4; n=4;
mymat = matrix(NA,m,n) # create a 4 x 4 matrix with zeroes
for(i in 1:m) {
  for(j in 1:n)
  {
    if(i<=j)
    {
     mymat[i,j]<- 0
     break
    } else
    {
      mymat[i,j] = 1   # we assign the values only when i<>j
    }
  }
}
print(mymat)


#NEXT
m=20;
for (k in 1:m)
{
  if (!(k%%2))
    next
  print(k)
}

