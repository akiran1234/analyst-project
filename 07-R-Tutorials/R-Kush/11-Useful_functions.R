#Don't edit these two lines#Quick Revision
vec1 <- c(a= 1.99, -2.5, 8.4, 3.5, 6.3)
vec1[vec1>0]


#Absolute
abs(vec1)
#convert vec1 to integer
vec1 <- as.integer(vec1)
vec1 <- round(vec1,2)

#Reverse the order of values
vec2 <- rev(vec1)
length(vec1)
vec3<- c(10,20,30)

#Sequence function
seq(from,to,by)  
seq(from,by,length.out )

seq(10,99,by=5)
seq(5,by=10,length.out = 30)

seq_along(vec2)

#Repeat function
rep(c(1,2),each=3,times=5)
length(rep(seq(1, 9,by = 2),each=4,times=5))
length(rep(1,each=4,times=7))

#Mean function
mean(c(10,20,NA),na.rm = T)
mean(c(10,50,90))
mean(c(10,1:10,500),trim = 0.1)


#grep() and grepl()
emails <- c("j@sundae.edu","edu@world.gov",
            "dalai.lama@peace.org", "invalid.edu", 
            "quant@bigdata.edu", 
            "hello@world.tv")

# Use grepl() to match for "edu"
edu_mail<- grepl("edu", emails)


# Use grep() to match for "edu", save result to hits
matched_email <- grep("edu", emails)

# Subset emails using match
subset(emails,edu_mail)
emails[matched_email]

emails <- c("john.doe@ivyleague.edu", "education@world.gov", "dalai.lama@peace.org", 
            "invalid.edu", "quant@bigdatacollege.edu", "cookie.monster@sesame.tv")

# Use grepl() to match for .edu addresses more robustly
email_match<- grepl("@.*\\.edu$", emails)
emails[email_match]


# Use grep() to match for .edu addresses more robustly, save result to hits
hits <- grep("@.*\\.edu$", emails)

# Subset emails using hits
emails[hits]

#sub and gsub functions
# The emails vector has already been defined for you
emails <- c("john.doe@ivyleague.edu", "education@world.gov", "dalai.lama@peace.org", 
            "invalid.edu", "quant@bigdatacollege.edu", "cookie.monster@sesame.tv")

# Use sub() to convert the email domains 
sub("@.*\\.edu$", "@dimensionless.in", emails)
gsub("@.*\\.edu$", "@dimensionless.in", emails)


emails <- c("john.doe@ivyleague.edu,education@world.gov", "dalai.lama@peace.org", 
            "invalid.edu", "quant@bigdatacollege.edu", "cookie.monster@sesame.tv")


#Another example
b<-"hellolll"
sub("l", "a",b)     #Only the first instance
gsub("l","a",b)   #All the  instances

#Playing around with DATE
today<- Sys.Date()
now <- Sys.time()
my.Date <- as.Date("2016-03-10")
class(my.Date)

my.Date <- as.Date("2016-15-10")
my.Date <- as.Date("2016-15-10", format = "%Y-%d-%m")
my.time <- as.POSIXct("2016-03-10 10:35:00")
class(my.time)


#arithmatic on dates
my.Date <- my.Date+2

#Assignment - month and year - in R

#format date
today <- Sys.Date()
today <- format(today,format = "%d-%m-%Y")
today<-as.Date(today,format = "%d-%m-%Y")
class(today)

format(Sys.Date()+1, format = "Today is a %A!")

#lubridate - read vignette on lubridate
