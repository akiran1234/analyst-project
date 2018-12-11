#Working Directory

getwd() # print the current working directory - cwd 
setwd("C:\\Users\\Richu's Lappy\\Desktop\\R Programming")
setwd("C:/Users/Richu's Lappy/Desktop/R Programming")
setwd(file.path("C:","Users", "Richu's Lappy","Desktop"))

# help in R
help(apply) # learn about available options
?mean
?apply/term  # exact term
help.search()
??apply/term #not sure of the exact term
??mean

#To see the examples for a given function
example(mean)

# work with your previous commands
history() # display all previous commands

#save your command history #
savehistory(file="myfile") # default is ".Rhistory" 

# recall your command history 
loadhistory() # default is ".Rhistory"

# save the workspace to the file .RData in the current working directory 
save.image()

q() # quit R. You will be prompted to save the workspace
