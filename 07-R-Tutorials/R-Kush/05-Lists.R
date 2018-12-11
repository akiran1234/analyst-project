names <- c("Ritesh","Anil","Krishna","Pallavi")
weights <- c( 72, 75 , 82,  51)
genders <- c("Male","Male","Male","Female")
phy_marks <- c(70,70,80,85)
chem_marks <- c(60,70,80,70)

#Creating a List #Lists can contain different kinds of data types
student_list <- list(names,weights,genders,phy_marks,chem_marks)

#Checking the structure of the list
str(student_list)

#Use length() to get number of elements
length(student_list)

#Naming different components of a list using the names function
names(student_list) <- c("NAMES","WEIGHTS","GENDERS","PHYSICS","CHEM")
student_list          #Check the output

#What-if the length of the vector is less than the no. of components of the list
names(student_list) <- c("NAMES","WEIGHTS","GENDERS","PHYSICS")
student_list         #Check the output


#Lists can contain different kinds of components i.e. it can be a list as well as dataframe
students_df<- data.frame(names,weights,genders,phy_marks,chem_marks)

#creating a list with dataframe as a component
student_list1 <- list(students_df,weights,student_marks,student_list)
str(student_list1)


#Recursiveness---Different components of a list are also a list
p<- list(b=c(12,13,15),c=14,d=16,18)      #Creating a list
l <- p[4]                                #Extracting the first element of a list 
l
class(l)                                 #Class of this component is also a List

m <-p[[1]] 
m
class(m)                                #Class of this component is a Vector


#SUBSETTING a List
student_list[1:4]                 #Subsetting through a "[" single bracket #Get components           


#SUBSETTING CONTD....
student_list[c(1,3)]         #Subsetting through a "[" single bracket #Get multiple components           
class(student_list[1])
names(student_list)         #Extracting names of components

#Extracting the values of a given component
student_list[[2]][3]

a<-student_list[[2]]
a[3]                      #Subsetting through "[[" double bracket     

#Extracting the values through names
student_list$WEIGHTS      #Access element using element name or label

#Access multiple elements using label names
student_list[c("NAMES","GENDERS")]

#Accessing particular values of a component
student_list$NAMES[c(2,4)]
student_list[[1]][2]



#MANIPULATING A LIST
#Adding a new component to the list
student_list$location <- c("A","B","C","D")
str(student_list)

student_list$1 <- c(2,4)

student_list$"1" <- c(2,4)               #only string can be used as name
      
#Deleting a component
student_list[7] <- NULL
student_list <- student_list[-6]
student_list[c(1,3)] <- NULL

c(student_list$NAMES,student_list$GENDERS) <- NULL
student_list[c("NAMES","GENDERS")] <- NULL
student_list$WEIGHTS <- NULL           #Deleting a component using $ operator

is.vector(student_list)


#Difference between Atomic Vector and List
vector(mode="numeric",length=4)
Y<-vector(mode="list",length=4)

is.vector(student_list)
is.vector(names)

is.atomic(names) 
is.atomic(student_list)

#Difference between NULL and NA 
length(NULL)
length(NA)

a<- c(10,20,NA,40) 
a[4]  -
a[3]  
length(a) 

b<- c(10,20,NULL,40)
b[4]     
b[3]     
length(b) 

#NA TAKES a space in the memory while NULL does not

#Unlist function : to convert a list into a vector 
stu<- unlist(student_list)
class(stu)
stu[8]
