#Components of a function
#function ( arglist )  {body}

formals(mean)

#Primitive functions dont have components #Part of only base package 
formals(sum)

#Mean function takes only 1 argument as input
mean(5,10)
mean(c(7,5,8,6))

#Creating a function #Function Definition
Total <- function(A,B) {
  Final_Score <- A + B
}
formals(Total)

score_test1 <- c(74,87,45,65)
score_test2 <- c(7,5,8,6)

#Calling a function with arguments
Total_marks <- Total(score_test1,score_test2)
Total_marks

#What happens when the argument value is not passed
Total_marks1 <- Total(score_test1)


#ARGUMENT WITH DEFAULT VALUE
Total <- function(A, B=c(10,4,5,6)) {
  Final_Score <- A + B
}

#Running with default value
Total_marks1 <- Total(score_test1)


#Lazy Evaluation 
#The function checks the value of the argument inside the body
#then in the global environment to find the value
Total <- function(A, B, C = new_marks) {  
  #new_marks <- mean(B)
  Final_score <- A+B+C
  Final_score
}
Total(A = c(70,75, 80, 85), B = c(7L, 5L, 8L, 6L))


#Multiple Return Values
Multiple_return <- function(A, B) {  
  Final_score <- A+B 
  Average_marks <- mean(Final_score)
  (c(Total=Final_score,Average = Average_marks))
}

Multiple_return(A = c(70L, 75L, 80L, 85L), B = c(7L, 5L, 8L, 6L))

#01 Look into them
Total #return the function itself
formals(Total) #Access arguments
body(Total) #Access body


#Example
a<-function(b,c){
  d<-b+c
  d
}
a(5,6)

#Complex function example
#Function definition
f <- function(y) {
    function(x){ y+x }
  }
f(10)(15)

lf <- vector("list",10)    #Calling function inside the or loop
for (i in 1:10) {
  lf[[i]] <- f(i)(10)
}