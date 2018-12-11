#Test for independence
mat<-matrix(c(7,16,6,43,34,44),nrow = 2,ncol = 3,byrow = T)
mat
chisq.test(mat)

#Goodness of fit
chisq.test(c(41,59),p = c(0.33,0.67))
chisq.test(x = c(41,59),p = c(0.33,0.67))

#One Sample t-test
# Beak Width of finches
library(readxl)
finches<-read_excel("Finches - Lesson 10.xlsx")
finches<-finches[1]
finches<-na.omit(finches)
t.test(x = finches,mu = 6.07,alternative ="greater",conf.level = 0.95)

#t.test(x = Data,mu = "tocompare",alternative=two.sided,conf.level = 0.95)

# Dependent Sample t-test
# Keyboard example
keyboards<-read.csv("C://Users/himanshu arora/Documents/Inferential Statistics/Lesson 10/Keyboards - Lesson 10 - Sheet1.csv")
library(readr)
keyboards<-read_csv("C://Users/himanshu arora/Documents/Inferential Statistics/Lesson 10/Keyboards - Lesson 10 - Sheet1.csv")
t.test(keyboards$`QWERTY errors`,keyboards$`Alphabetical errors`,alternative = "two.sided",mu = 0,paired = T,conf.level = 0.95)

# Two sample independent t-test
# Food Prices Gettysburg and Wilma
library(readxl)
food_prices<-read_excel("C:/Users/himanshu arora/Documents/Inferential Statistics/Lesson 11/Food Prices - Lesson 11.xlsx")
t.test(x=food_prices$`Average meal prices at restaurants in Gettysburg ($)`,y=food_prices$`Average meal prices at restaurants in Wilma ($)`,alternative = "two.sided",mu = 0,paired = F,var.equal = F,conf.level = 0.95)

#Acne Example
x<-c(40,36,20,32,45,28)
y<-c(41,39,18,23,35)
t.test(x,y,alternative ="two.sided",mu = 0,paired = F,var.equal = F,conf.level = 0.95)

# Anova
prices<-c(15,12,14,11,39,45,48,60,65,45,32,38)
brands<-c(rep("Snapzi",4),rep("Irisa",4),rep("Lolamoon",4))
brands

anova_output<-aov(formula = prices~brands)
summary(anova_output)

#HSD
TukeyHSD(anova_output)


prices<-c(15,12,14,11,39,45,48,60)
brands<-c(rep("Snapzi",4),rep("Irisa",4))
ttest<-t.test(prices~brands)
ttest