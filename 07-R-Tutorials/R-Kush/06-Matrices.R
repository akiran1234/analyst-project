#SYNTAX#matrix(data no.of rows,no.of col)
Mat1<-matrix(1:6,3,2)
Mat1

#Filling the matrix rowwise
Mat2<-matrix(1:6,3,2,byrow=T)
class(Mat2)


#class() will tell the data type for vectors and Data 
#structure for other data structures

#Structure function
str(Mat1)

#Dimensions of a Matrix
dimens <- dim(Mat1)
class(dimens)
class(dim(Mat1))
is.vector(dimens)

dim(Mat1)[1]
dimens[1]
dim(Mat1)[2]
dimens[2]

#checking the no. of rows and columns
nrow(Mat1)
ncol(Mat1)
    
#Problem 1 
#Create a Matrix "Cricket" with  Scores of Three batsmen
#Sachin(90,40), 
#Rahul(80,100), 
#Ganguly(92,79) for 2 innings

sachin <- c(90,40)
Rahul <- c(80,100)
Ganguly <- c(92,79)
#method1
Score_Mat <- matrix(c(sachin,Rahul,Ganguly),3,2,byrow = T)

#method2
a<-matrix(c(90,80,92,40,100,79),nrow=3,ncol=2)

rownames(Score_Mat) <- c("Sachin","Rahul","Ganguly")
colnames(Score_Mat) <- c("Inning1","Inning2")

#method3
Cricket<-matrix(c(90,40,80,100,92,79),nrow=3,ncol=2,
                byrow = TRUE,list(c("Sachin","Rahul","Ganguly"),c("Inning1","Inning2")))

#method4
#rbind()   - row bind 
Cric_Mat_bindr <- rbind(sachin,Rahul,Ganguly)
class(Cric_Mat_bindr)

#append another player's score into the existing matrix
kohli <- c(45,60)
Cric_Mat_bindr <- rbind(Cric_Mat_bindr,kohli)

#cbind()   - column bind
Cric_Mat_bindc <- cbind(sachin,Rahul,Ganguly)
class(Cric_Mat_bindr) 

Score3 <- c(90,80,90,70)
Cric_Mat_bindr2 <-cbind(Cric_Mat_bindr,Score3)

#Example 2
phy_marks <- c( 84,75,80,85)
chem_marks <- c(60,70,85,70)

student_marks <-cbind(phy_marks, chem_marks)
student_marks_r <-rbind(phy_marks, chem_marks)

rownames(student_marks) <- c("Anil","Sudeep","Krishna","Pallavi")
student_marks

dimnames(student_marks)

#Subsetting: Extract element(s) from matrix
student_marks#row number,column number
student_marks[,]
student_marks[2,2]
student_marks[1,]
student_marks[,2]

str(student_marks[,2])
is.vector(student_marks[,2])

student_marks[1:3]

hindi_marks<- c(80,50,54,72)
science_marks<- c(45,89,95,82)

student_marks <-cbind(student_marks,hindi_marks,science_marks)
dim(student_marks)

#SYNTAX#matrix_name[row,col]
student_marks[c(2,3),c(1,2)]    
student_marks[(1:3),c(1,2)]
student_marks[,c(T,F)]              
student_marks[,-c(2,3)]


#summary
student_marks
rowSums(student_marks) #Row wise sum
colSums(student_marks) #Column wise sum
rowMeans(student_marks) #Row wise Mean
colMeans(student_marks) #Column wise mean)



#Problem - 
#Find all the details of students who have scored > 75 in chemistry
  

student_marks[,(student_marks[,2]>75)] === Incorrect output
student_marks[student_marks[,2]>75,]




#Find the name of the students for the previous question
(which(student_marks[,2]>75))
rownames(student_marks)[which(student_marks[,2]>75)]

#Using Subset function
subset(student_marks,student_marks[,2]>75,)

#Problems
#Find all students who have scored more than 75% marks on average

#Method 1
total<- rowMeans(student_marks)
student_marks_new <- cbind(student_marks,total)
subset(student_marks_new,student_marks_new[,5]>75,1:5)

#Method2
student_marks[(rowMeans(student_marks)>75),]

#Method3
subset(student_marks,rowMeans(student_marks)>75,)


#Find only names of students whose avg marks is >75%
rownames(student_marks)[rowMeans(student_marks)>75]
rownames(student_marks)[which(rowMeans(student_marks)>75)]


#Naming the dimensions of a matrix
N<- matrix(1:12,4,3,dimnames= list(c("A","B","C","D"),c("L","N","O")))
N<- matrix(1:12,4,3,dimnames= list(c(paste("row",1:nrow(N), sep="-")),c("L","N","O")))

#How paste function works
paste("abcde",c("efghi","jklmn"), sep="-")
X<-paste(30,"April",2017,sep="-")
class(X)
