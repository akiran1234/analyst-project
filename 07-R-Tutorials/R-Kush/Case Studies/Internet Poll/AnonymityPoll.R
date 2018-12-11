getwd()
#Problem 1.1 - Loading and Summarizing the Dataset
poll=read.csv("https://storage.googleapis.com/dimensionless/Analytics/AnonymityPoll.csv")
str(poll)
summary(poll)
#How many people participated in the poll?
#Ans:- 1002
# Problem 1.2 - Loading and Summarizing the Dataset
#How many interviewees responded that they use a smartphone?
table(poll$Smartphone)
#Ans:- 487
#How many interviewees responded that they don't use a smartphone?
# Ans:- 472
#How many interviewees responded that they don't use a smartphone?
# Ans:- 43
#Problem 1.3 - Loading and Summarizing the Dataset 
#Which of the following are states in the Midwest census region?
table(poll$State,poll$Region)
#or 
MidwestInterviewees = subset(poll, Region=="Midwest")
table(MidwestInterviewees$State)
#Ans: Kansas, Missourri, Ohio
#To find the number of interviewees from each South region state we could have used:
SouthInterviewees = subset(poll, Region=="South")
table(SouthInterviewees$State)
# Ans:- Texas
# Problem 2.1 - Internet and Smartphone Users
#How many interviewees reported not having used the Internet and not having used a smartphone?
table(poll$Internet.Use,poll$Smartphone)
#Ans:- 186
#How many interviewees reported having used the Internet and having used a smartphone?
#Ans:-470
#How many interviewees reported having used the Internet but not having used a smartphone?
#Ans :- 285
#How many interviewees reported having used a smartphone but not having used the Internet?
# Ans :- 17
#Problem 2.2 - Internet and Smartphone Users
#How many interviewees have a missing value for their Internet use?
summary(poll$Internet.Use)
#Ans :- 1
#How many interviewees have a missing value for their smartphone use?
summary(poll$Smartphone)
# Ans:- 43
#Problem 2.3 - Internet and Smartphone Users
#How many interviewees are in the new data frame?
limited<-subset(poll,poll$Internet.Use==1|poll$Smartphone==1)
nrow(limited)
#Ans:- 792
#Problem 3.1 - Summarizing Opinions about Internet Privacy
#Which variables have missing values in the limited data frame?
summary(limited)
# Ans:- Smartphone, Age, Conservativeness, Worry.About.Info, Privacy.Importance,
#Anonymity.Possible, Tried.Masking.Identity , Privacy.Laws.Effective 
# Problem 3.2 - Summarizing Opinions about Internet Privacy
#What is the average number of pieces of personal information on the Internet, according to the Info.On.Internet variable?
mean(poll$Info.On.Internet,na.rm = TRUE)
#Ans:-3.795
#Problem 3.3 - Summarizing Opinions about Internet Privacy
#How many interviewees reported a value of 0 for Info.On.Internet?
table(poll$Info.On.Internet)
#Ans:-105
#How many interviewees reported the maximum value of 11 for Info.On.Internet?
#Ans:-8
#Problem 3.4 - Summarizing Opinions about Internet Privacy
#What proportion of interviewees who answered the Worry.About.Info question worry about how much information is available about them on the Internet?
table(limited$Worry.About.Info)
#Ans:- 0.4886
#Problem 3.5 - Summarizing Opinions about Internet Privacy
#What proportion of interviewees who answered the Anonymity.Possible question think it is possible to be completely anonymous on the Internet?
table(limited$Anonymity.Possible)
#Ans:- 0.3692
#Problem 3.6 - Summarizing Opinions about Internet Privacy
#What proportion of interviewees who answered the Tried.Masking.Identity question have tried masking their identity on the Internet?
table(limited$Tried.Masking.Identity)
#Ans:- 0.163
#Problem 3.7 - Summarizing Opinions about Internet Privacy

#What proportion of interviewees who answered the Privacy.Laws.Effective question find United States privacy laws effective?
table(limited$Privacy.Laws.Effective)
#Ans:- 0.256
#Problem 4.1 - Relating Demographics to Polling Results
#Build a histogram of the age of interviewees. What is the best represented age group in the population?
hist(poll$Age)
#Ans:- People aged about 60 years old 
#Problem 4.2 - Relating Demographics to Polling Results
#What is the largest number of interviewees that have exactly the same value in their Age variable AND the same value in their Info.On.Internet variable?
table(poll$Age,poll$Info.On.Internet)
max(table(limited$Age, limited$Info.On.Internet))
plot(limited$Age, limited$Info.On.Internet)
#Ans 6
#Problem 4.3 - Relating Demographics to Polling Results

#To avoid points covering each other up, we can use the jitter() function on the values we pass to the plot function. Experimenting with the command jitter(c(1, 2, 3)), what appears to be the functionality of the jitter command?
jitter(c(1,2,3))
#Ans:- D
#Problem 4.4 - Relating Demographics to Polling Results
#Now, plot Age against Info.On.Internet with plot(jitter(limited$Age), jitter(limited$Info.On.Internet)). What relationship to you observe between Age and Info.On.Internet?
plot(jitter(limited$Age), jitter(limited$Info.On.Internet),type="h",xlim=c(20,25,30,35,40,45))

#Ans C
#Problem 4.5 - Relating Demographics to Polling Results
#Use the tapply() function to obtain the summary of the Info.On.Internet value, broken down by whether an interviewee is a smartphone user.
#What is the average Info.On.Internet value for smartphone users?
tapply(limited$Info.On.Internet, limited$Smartphone, summary)
#Ans 4.368
#What is the average Info.On.Internet value for non-smartphone users?
# Ans :- 2.923
#Problem 4.6 - Relating Demographics to Polling Results

#Similarly use tapply to break down the Tried.Masking.Identity variable for smartphone and non-smartphone users.

#What proportion of smartphone users who answered the Tried.Masking.Identity question have tried masking their identity when using the Internet?
tapply(limited$Tried.Masking.Identity, limited$Smartphone, table)
#Ans:- 0.1925
#What proportion of non-smartphone users who answered the Tried.Masking.Identity question have tried masking their identity when using the Internet?
#Ans:- 0.1174