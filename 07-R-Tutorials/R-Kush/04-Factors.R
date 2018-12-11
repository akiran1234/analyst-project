#factors ---- Used for categorical data

#Continuous variable and Categorical variable 
#YES/NO
#GENDER
#LOCATION
#BODY TYPE
#SIZE

gender_vector <- c("Male","Male","Female","Female","Female")

#Creating a factor
student.genders <- factor(gender_vector) # factor
student.genders                  #Here we see that there is a extra attribute levels
class(student.genders)  
str(student.genders)
levels(student.genders)
#By default the levels of a factor are set in an alphabetical order

#Defining the levels of a factor using the levels argument
student.genders <- factor(student.genders,
                          levels= c("Male", "Female")) # Character vector

#Let us see the Structure 
str(student.genders)
#We see that the levels of a factor  are not stored as names but as numeric values

#NOMINAL AND ORDINAL Categorical variables
#NOMINAL --- It is a categorical variable without any implied order, which means
#we cannot say one is more important than any other
#Example - Gender 
#ORDINAL --- It is a categorical variable with an implied order
#Example - Small Medium Large

Intensity <- c("Low", "Low","Medium","High","Medium")
Intensity_factor <- factor(Intensity)
Intensity_factor
str(Intensity_factor)
Intensity_factor <- factor(Intensity,order=T)
Intensity_factor <- factor(Intensity,order=T,
                           levels= c("Low","Medium","High"))
str(Intensity_factor)


#Summarizing a factor 
summary(Intensity_factor)
table(Intensity_factor)

summary(mtcars) #Mean,Min,Max,Ist Quartile,2nd Quartile,3rd Quartile
summary(iris)

#Apply table function onto cyl column of mtcars
table(mtcars$cyl)
table(mtcars[,2])


data.frame(stringsAsFactors = )