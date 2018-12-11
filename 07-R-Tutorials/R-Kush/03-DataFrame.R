#Various datasets already loaded in your R 
data()

#Lets check the class of a few of them
class(mtcars)
class(Titanic)

#Dataframe Properties
#similar to matrix.... but heterogenous

names <- c("Ritesh","Anil","Krishna","Pallavi")
weights <- c( 72, 75 , 82,  51)
genders <- c("Male","Male","Male","Female")
phy_marks <- c(70,70,80,85)
chem_marks <- c(60,70,80,70)

#Creating a Dataframe
students <- data.frame(names,weights,genders,phy_marks,chem_marks)
str(students)

#Making sure strings are not converted to factors 
students1 <- data.frame(names,weights,genders,phy_marks, chem_marks, stringsAsFactors = F)
students1
str(students1)
summary(students1)

#converting gender to factors
students$genders <- factor(students$genders)

#Accessing variable names and dimension names 
names(students)
rownames(students)
colnames(students)

#Assigning dimension names
rownames(students) <- c("AA","BB", "CC","DD")

#similarly can be done for columns thru colnames and names functions as well

#finding the dimensions of a dataframe
dim(students)
dim(students)[1]
dim(students)[2]

nrow(students)
ncol(students)

#viewing a dataframe
students
mtcars

head(students)  #By default only 6 rows are seen
tail(students)

dim(mtcars)

head(mtcars)
tail(mtcars)

#To see a particular no. of rows
head(mtcars,n=8)
tail(mtcars,n=8)


#Subsetting: Extract element(s) in data frame
mtcars[1:3]
students[1]
class(students[1])

students[[1]]
class(students[[1]])

students[[1]][1]
str(students)

#Single brackets [] return element of same type
typeof(students[1])
typeof(students[c(1,4)])
class(students[c(1,4)])


students["names"]
students[["names"]] #double brackets [[]] return the object in its own type
typeof(students[["names"]])
students$names #$ return the object in its own type

students$names[1]
students[,1:3]

students[c("phy_marks","chem_marks")]
students
students[1,2]  #Row number, Column number
students[1:3,1:2]
students[c(1,2),c(1,3)]
students[1,]
class(students[1,])

students[c(T,F),]
students[c(T,F,T,F),]


#Problem
#Students who have scored >70 in physics


students[[4]]>70
students[students[[4]]>70,]
subset(students,students[[4]]>70,4)
students[(students[,4]>70),]
students[(students[4]>70),]
students[phy_marks>70,]
subset(students,phy_marks>70)

#Find all the cars from mtcars which have cyl>4 and gears<4

mtcars[mtcars$cyl>4 & mtcars$gear<4,]
mtcars[c(mtcars$cyl>4,mtcars$gear<4),]

mtcars[["cyl"]]>4
mtcars[["gear"]]<4
mtcars[mtcars["cyl"]>4 & mtcars["gear"]<4,]

mtcars[[2]]>4
mtcars[[10]]<4
mtcars[mtcars[2]>4 & mtcars[10]<4,]

mtcars[mtcars$cyl>4 & mtcars$gear<4,]
subset(mtcars,cyl>4 & gear<4)

#Students who have chemistry >75 OR weight > 70
subset(students,students$chem_marks>75 | students$weights>70)


#Deleting rows and columns
students$phy_marks<- NULL                 #Delete physics marks
students <- students[c(1,3,4)]            #Delete weights
students <- students[c(-2,-3)]            #Delete multiple variables  
students <- students[,-2]                 #Delete a variable
students <- students[c(-1,-3),]           #Delete rows
students <- students[c(-1,-3),c(-2,-4)]   #Delete rows as well as columns

students<- students[!(students$phy_marks<75),]
students$names <- NULL


#Appending a dataframe(Columns)
level <- c("A", "B","C","F")
level <-factor(level)
students1 <- cbind(students,level,stringsAsFactors=F)   #appending columns
str(students1)

#Appending a dataframe(Row)
new_row <- c("Krishna", 82,"Male",80,60,"B")
students_updated <- rbind(students1, new_row,stringsAsFactors=F)

#Sorting the dataframe based on a particular column
students[order(students$weights),]
students[order(students$weights,decreasing = T),]
students[order(-students$weights),]
students[order(students$chem_marks, students$weights),]

#If the chem marks has to be arranged in ascending but names in Descending order
students[order(-students$chem_marks,students$names,decreasing = T),]

#Problem
# Sort mtcars on the below mentioned basis
# cyl - ascending order
# gear - decreasing order

#Sorting on the mtcars dataframe
mtcars
mtcars[order(mtcars$cyl,-mtcars$gear),]
mtcars[order(mtcars$gear,mtcars$mpg),]
mtcars[order(mtcars$cyl,-mtcars$gear),]


# Merging two data frames #
Died.At <- c(22,40,72,41)
Writer.At <- c(16, 18, 36, 36)
First.Name <- c("John", "Edgar", "Walt", "Jane")
Second.Name <- c("Doe", "Poe", "Whitman", "Austen")
Sex <- c("MALE", "MALE", "MALE", "FEMALE")
Date.Of.Death <- c("2015-05-10", "1849-10-07", "1892-03-26","1817-07-18")

#if the values are common
writers_df <- data.frame(Died.At, Writer.At, First.Name, Second.Name, Sex, Date.Of.Death,stringsAsFactors = FALSE)
str(writers_df)
data2 <- data.frame(Died.At=c(22,41,72,40), Location=5:8)
Output <-merge(writers_df,data2)


#if the value is different
data3 <- data.frame(Died.At=c(22,41,7,4), Location=5:8)
Output<-merge(writers_df,data3)

#if you wanted to have all rows from first dataset
Output<-merge(writers_df,data3,all.y = T)

#if column names are different
data4 <- data.frame(a.Died.At=c(22,30), Location=5:8)
X<-merge(writers_df,data4, by.x = "Died.At", by.y = "a.Died.At")

#if column names are different and you dont mention anything
data4 <- data.frame(a.Died.At=c(80,30), Location=5:8)
X<-merge(writers_df,data4)


#merging multiple columns
x <- data.frame(k1 = c(1,1,3,4,5), k2 = c(1,1,1,4,5), data = 1:5)
y <- data.frame(k1 = c(1,1,1,4,5), k2 = c(1,1,3,4,5), data = 1:5)
merge(x, y, by = c("k1","k2"))
