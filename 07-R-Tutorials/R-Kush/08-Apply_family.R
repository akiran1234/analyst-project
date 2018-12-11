#Quick Revision
#Matrix ordering/Sorting
mtcars
#order the mtcars data on the basis on mpg column
length(mtcars$mpg)
mtcars[order(mtcars$mpg),]
mtcars[order(mtcars$mpg)]
mtcars[order(mtcars$mpg,mtcars$disp),]

#apply #applied on a array #Matrix or Dataframe 
mat1 <- matrix(1:16, 4, ncol = 4)
apply
apply(mat1, 1, sum)
apply(mat1, 1, mean)
apply(mat1, 2, sum)

#Quick revision 
rowSums(mat1)

X<-matrix(rnorm(30,10,1), nrow=5, ncol=6)
apply(X,1,sum)


#lapply #The output is a List #Any component of a list or element of a vector
cities<- list(c("Jaipur","ABCS"),"New Delhi","Pune","Bengaluru")
output<- lapply(cities, nchar)
unlist(output)

#Easier way
nchar(cities)

#Function to double the values in a list
oil_prices <- list(a=2.3, b=4.5,c=6.7, d=8.4)

double_value <- function(x) {
  2*(x)
}
double_value(oil_prices)             #Error 

#Using lapply function
output<- lapply(oil_prices,double_value)
output

#lapply function on dataframes
mtcars
lapply(mtcars,as.integer)


#Now make this as a generic function
multiply<- function(x, factor){
  x* factor
}
lapply(oil_prices, multiply,factor=4)

#Using lapply on dataframes
mat1 <- matrix(rep(seq(10:4), 4), ncol = 4)
mat1.df <- as.data.frame(mat1)
a<-lapply(mat1.df,mean)
class(a)
is.vector(mat1.df$V1)

#sapply $Similar to lapply but simplifies the output

#create a list with 2 elements
l <- list(a = 1:10, b = 11:20)
# mean of values using sapply
l.mean <- lapply(l, mean)

# what type of object was returned?
class(l.mean)
# it's a numeric vector, so we can get element "a" like this
l.mean[['a']]

#Using sapply
new_mean <- sapply(l, mean)

#vapply # To get the output in a predefined format
?fivenum
l <- list(a = 1:10, b = 11:20)
# fivenum of values using vapply
l.fivenum <- vapply(l, fivenum, c(Min.=0, "1st Qu."=0, Median=0, "3rd Qu."=0, Max.=0))
class(l.fivenum)


#replicate
replicate(5,sum(rnorm(10)))

set.seed(10)
print("a")
rnorm(20)


#How to get the same output all the time #Can use rnorm as well
#Method 1 
a <-function(x)
  {
  set.seed(1)
  rnorm(x)
  }
replicate(5,sum(a(x=20)))

#Method 2
abc<-function(){
  set.seed(1)
  sum(rnorm(10))
}
replicate(5,abc())


#mapply --Mulvariate
l1 <- list(a = 1:10, b =11:20)
l2 <- list(c = 21:30, d = 31:40)
l1$a+l2$c
b<-mapply(sum, l1, l2)

# sum the corresponding elements of l1 and l2
l1 <- list(a = 1:10, b =11:20)
l2 <- list(c = 21:25, d = 31:40)
mapply(sum,l1$a, l1$b, l2$c, l2$d)
mapply(sum,l1$b, l2$c)
mapply(mean, c(l1, l2))

#tapply
x1<- runif(16)
cat1 <- rep(1:4, (length(x1)/4))
cat2 <- c(rep(1, 8), rep(2, 8))
cat3 <- rep(1:4, (length(x1)/4))
cat4 <- rep(1:8, 2)


#Creating the dataframe
mat2.df <- data.frame(x1)
dim(mat2.df)
names(mat2.df) <- c("Data")

mat2.df=cbind(mat2.df,cat3)
#How to modify the dataframe. Adding 4 caloums 
#through different ways

#Adding 2nd column
mat2.df <- data.frame(mat2.df,cat1)

#Adding 3rd column
mat2.df[,3]<- cat2
#naming the 3rd column as cat2
names(mat2.df)[3]<- "cat2"

#Adding 4th column
mat2.df$cat3 <- cat3
#OR
mat2.df <- cbind(mat2.df,cat3)

#Using tapply to find the indexwise summation
#SYNTAX  #tapply(data,index,function)
tapply(mat2.df$Data,mat2.df$cat1,sum)
tapply(mat2.df$Data,mat2.df$cat2,sum)

tapply(mat2.df$Data,list(mat2.df$cat1,mat2.df$cat2), sum)
tapply(mat2.df$Data,list(mat2.df$cat1,mat2.df$cat2,mat2.df$cat3),sum)
tapply(mat2.df$Data,list(mat2.df$cat1,mat2.df$cat3,mat2.df$cat2),sum)
