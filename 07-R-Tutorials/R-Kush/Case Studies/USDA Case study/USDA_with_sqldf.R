USDA<-read.csv("https://storage.googleapis.com/dimensionless/Analytics/USDA.csv")
View(USDA)
str(USDA)
summary(USDA)
library(sqldf)
sqldf("SELECT Description FROM USDA WHERE Sodium=38758")
which.max(USDA$Sodium)
USDA$Description[265]
HighSodium<-sqldf("SELECT * FROM USDA WHERE Sodium>10000")
HighSodium2<-subset(USDA,USDA$Sodium>10000)
sqldf("SELECT * FROM HighSodium WHERE Description='CAVIAR' ")
sqldf("SELECT * FROM USDA WHERE Description LIKE('%CAVI%')",row.names=T)
sqldf("SELECT STDEV(Sodium) FROM USDA")

mean(USDA$Sodium,na.rm = T)
summary(USDA$Sodium)
sd(USDA$Sodium,na.rm = T)
Sc<-scale(USDA$Sodium)
Sc[4154]

sqldf("SELECT scale(Sodium) FROM USDA")
sqldf("SELECT")
plot(USDA$Protein,USDA$TotalFat,main = "Protein Vs Fat",xlab = "Protein",ylab="TotalFat",col="Red")
qplot(USDA$Protein,USDA$TotalFat,main = "Protein Vs Fat",xlab = "Protein",ylab="TotalFat",col="Red")

hist(USDA$VitaminC,xlab = "Vitamin C",main = "Histogram of Vitamin C levels",breaks=100,xlim=c(0,100))
?hist
boxplot(USDA$Sugar,main= "Boxplot of Sugar Levels")
summary(USDA$Sugar)
quantile(USDA$Sugar,na.rm = T)
HighSodium<-sqldf("SELECT Sodium, CASE WHEN Sodium>AVG(Sodium) THEN 1 ELSE 0 END HighSodium FROM USDA")
sqldf("SELECT AVG(Sodium) FROM USDA")
USDA$HighSodium<-as.numeric(USDA$Sodium>mean(USDA$Sodium,na.rm = T))
USDA$Sodium>mean(USDA$Sodium,na.rm = T)
USDA$HighSodium<-ifelse(USDA$Sodium>mean(USDA$Sodium,na.rm = T),1,0)
sqldf("SELECT COUNT(Sodium) FROM USDA")
sqldf("SELECT Sodium,IF Sodium>AVG(Sodium) SET HighSodium=1;
                  ELSE SET HighSodium=0;
                  END IF; 
                  FROM USDA")
USDA$HighProtein<-ifelse(USDA$Protein>mean(USDA$Protein,na.rm = T),1,0)
USDA$HighCarbs<-ifelse(USDA$Carbohydrate>mean(USDA$Carbohydrate,na.rm = T),1,0)
USDA$HighFat<-ifelse(USDA$TotalFat>mean(USDA$TotalFat,na.rm = T),1,0)
str(USDA)
table(USDA$HighSodium)
table(USDA$HighSodium,USDA$HighFat)
