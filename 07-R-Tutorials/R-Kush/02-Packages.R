#Install a package in R
install.packages("plyr")

#Load a package
library("plyr")

#Check installed packages
installed.packages()

#Update a package 
update.packages()


#Uninstall a package
remove.packages("dplyr")

#Unload a package 
detach("package:tidyr", unload=TRUE)

#Loaded packages and also the order in which R searches 
search()


#Datasets 
data()                  #all the installed 
data(package = "stats")  #In a particular package


AirPassengers

help(nasa)              #to search which package does a dataset belong to
help("AirPassengers")
help("Titanic")
help("mtcars")
mtcars

example(mean)
ls()  #Display the components of global environment

#Functions in a package
ls(pos="package:dplyr")
ls(pos="package:base")     

#To increase the maximum lines printed on the console
options(max.print=100000)


#Vignette is a help document/usage doc for a particular function   
vignette(all= T) #gives the list of vignettes present in the installed packages 
vignette("ggplot2-specs") #see a particular vignette
