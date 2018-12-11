#Quick revision
ls(pos = "package:dplyr")
search()

#install and load the dplyr and hflights package
install.packages("dplyr")
install.packages("hflights")

library(dplyr)
library(hflights)

help(hflights)

#Viewing the data
head(hflights)
summary(hflights)
glimpse(hflights)


#Convert the hflights data.frame into a hflights tbl
hflights_1 <- tbl_df(hflights)

# Display the hflights tbl
hflights_1

#MANIPULATE THE D(ATA
#Unique function example
mtcars
unique(mtcars$cyl)

#Find the total no. of unique carriers in the given dataset
unique(hflights_1$UniqueCarrier)

#function to check exactly how long this is
length(unique(hflights_1$UniqueCarrier))


#Example for understanding
Data <- c("AA", "AS","AA","AA","AS")
Reference <- c("AA" = "American", 
               "AS" = "Alaska")
week<- c(a="Mon",b="Tue",c="wed")
Data<- c(a,b,c)
week[c("a","b","a")]

Reference["AS"]
Data <- Reference[Data]
  

#Organising the Unique carrier data 

Reference_Data <- c("AA" = "American", "AS" = "Alaska", "B6" = "JetBlue", "CO" = "Continental", 
         "DL" = "Delta", "OO" = "SkyWest", "UA" = "United", "US" = "US_Airways", 
         "WN" = "Southwest", "EV" = "Atlantic_Southeast", "F9" = "Frontier", 
         "FL" = "AirTran", "MQ" = "American_Eagle", "XE" = "ExpressJet", "YV" = "Mesa")

hflights_1$UniqueCarrier <- Reference_Data[hflights_1$UniqueCarrier]
unique(hflights_1$UniqueCarrier)

#Perform similar operation on Cancellation code for reasons
unique(hflights_1$CancellationCode)


# The Reference variable       #Error encountered
Ref_reason<- c("A" = "carrier", "B" = "weather", "C" = "FFA", "D" = "security", "" = "not cancelled")

#Method 1
table(hflights_1$CancellationCode)
Ref_reason<- c("A" = "carrier", "B" = "weather", "C" = "FFA", "D" = "security", " " = "not cancelled")
hflights_1$CancellationCode<-Ref_reason[hflights_1$CancellationCode] 
hflights_1$CancellationCode[is.na(hflights_1$CancellationCode)]<- "not cancelled"
table(hflights_1$CancellationCode)

#Method 2
# Convert the blanks to some value
hflights_1$CancellationCode[hflights_1$CancellationCode == ""]<- "E"
unique(hflights_1$CancellationCode)

#Updated reference variable
Ref_reason<- c("A" = "carrier", "B" = "weather", "C" = "FFA", "D" = "security", "E" = "not cancelled")

#Convert cancellation code to reasons
hflights_1$CancellationCode<- Ref_reason[hflights_1$CancellationCode]
unique(hflights_1$CancellationCode)

length(which(hflights_1$CancellationCode !="not cancelled"))
table(hflights$Cancelled)

#Find the total no. of cancelled flights
length(hflights_1$CancellationCode[hflights_1$CancellationCode == "not cancelled"])

#SELECT VERB
hflights_1
#See if the changes that we made earlier are in place
select(hflights_1,UniqueCarrier,CancellationCode)

# Print out a tbl with the four columns of hflights related to delay
select(hflights_1, ArrDelay, DepDelay, ActualElapsedTime,AirTime)

#Use head for better viewing of the result
head(select(hflights_1, ArrDelay, DepDelay, ActualElapsedTime,AirTime))

# Print out the columns Origin up to Cancelled of hflights
head(select(hflights_1, Origin:Cancelled))

# Print out a tbl containing just ArrDelay and DepDelay
head(select(hflights, contains("Delay")))

# Print out the columns that contains "time" or ends with "num"
head(select(hflights,contains("time"),ends_with("num")))

#Predict the output of the below mentioned code
head(select(hflights, UniqueCarrier, contains("Cancell"), ends_with("Num")))


#MUTATE
# Add the new variable ActualGroundTime= (ActualElapsedTime - AirTime)
g1 <- mutate(hflights_1,ActualGroundTime= ActualElapsedTime - AirTime)
str(g1)

# Add the new variable TotalTaxiingtime to g1. Save the result as g2.
hflights_1 <- mutate(hflights_1, TotalTaxiingtime = TaxiIn+TaxiOut)
str(hflights_1)

# Add the new variable AverageSpeed to g2. Save the result as g3.
hflights_1 <- mutate(hflights_1, AverageSpeed = (Distance/AirTime)*60)

#Combine Year,Month & DayofMonth variables to create Date column
hflights_1<-mutate(hflights_1,Date=as.Date(paste(DayofMonth,Month,Year,sep = "-"),format="%d-%m-%Y"))
head(select(hflights_1,Date_1))
str(hflights_1)


#FILTER
#Find total no. of flights that travelled 3000 miles or more
nrow(filter(hflights_1,Distance> 3000))

unique(filter(hflights_1,Distance>3900)$Dest)
distinct(select(filter(hflights_1,Distance>3900),Dest))



#Total no. of flights that travelled > 3300,3500 and 3900  miles
nrow(filter(hflights_1, Distance >= 3300))
nrow(filter(hflights_1, Distance >= 3500))
nrow(filter(hflights_1, Distance >= 3900))


#Find the unique destination for flights that travelled >3300 miles or more
unique(select(filter(hflights_1,Distance>3900),Dest))
unique(filter(hflights_1,Distance>3900)$Dest)
unique(filter(hflights_1,Distance>3900)[,"Dest"])

#Find total no. of aircrafts that American airlines has
length(unique(filter(hflights_1,UniqueCarrier == "Alaska")$TailNum))

#Find total no. of flights that a particular carrier has
length(filter(hflights_1,UniqueCarrier =="American")$FlightNum)

#WHAT DOES TAILNUM and FLIGHTNUMBER SIGNIFY
unique(filter(hflights,UniqueCarrier == "American")$TailNum) 
unique(filter(hflights,UniqueCarrier == "American")$FlightNum) 

# All flights flown by one of JetBlue, Southwest, or Delta

#Incorrect way
filter(hflights,UniqueCarrier == c("Southwest","Delta","JetBlue"))
filter(hflights_1, UniqueCarrier == "Delta" |UniqueCarrier == "Southwest"|UniqueCarrier == "JetBlue")

nrow(filter(hflights_1, UniqueCarrier == "Delta"))
nrow(filter(hflights_1, UniqueCarrier == "Southwest"))
nrow(filter(hflights_1, UniqueCarrier == "JetBlue"))


# All flights where taxiing took longer than flying
nrow(filter(hflights,AirTime<(TaxiIn + TaxiOut)))

# All flights where taxiing took longer than flying using Mutate
nrow(filter(mutate(hflights,Taxitime=TaxiIn + TaxiOut),AirTime<Taxitime))

# All flights that departed late but arrived ahead of schedule
select(filter(hflights, DepDelay > 0 & ArrDelay < 0), DepDelay, ArrDelay)

# Select the flights that had JFK as their destination
filter(hflights, Dest == "JFK")


#ARRANGE
#Arrange the data based on DepDelay
head(select(arrange(hflights_1,DepDelay),Year:ArrTime,DepDelay))
head(select(arrange(hflights,desc(DepDelay)),Year:ArrTime,DepDelay))

# Find all flights which have been cancelled and 
#whose DepDelay is present/DepDelay is not NA

N=filter(hflights_1,Cancelled== 1, !is.na(DepDelay))

# Arrange N so that cancellation reasons are grouped
select(arrange(N, CancellationCode), Year, Month, CancellationCode)

#Sort the data in descending order of Departure delay 
arrange(N,desc(DepDelay),ArrTime)$DepDelay

# Arrange according to carrier and decreasing departure delays
arrange(hflights, UniqueCarrier, desc(DepDelay))

#Arrange hflights by departure delays such that the shortest departure delay is at top 
arrange(hflights,desc(Cancelled), DepDelay,desc(FlightNum))

# Arrange flights by total delay (normal order).
arrange(mutate(hflights, Delay = (ArrDelay + DepDelay)), Delay)

#Find all the flights that have been delayed by more than 70 mins 
#and sort by taxiing time
arrange(mutate(filter(hflights,DepDelay >70), TaxiTime = TaxiIn + TaxiOut),TaxiTime, desc(DepDelay))

#SUMMARISE
#Print out a summary with variables min_dist and max_dist for shortest and longest distaance flown
summarise(hflights, min_dist = min(Distance), max_dist = max(Distance), mean_dst = mean(Distance))

#Find the maximum distance for all diverted flights
summarise(filter(hflights,Diverted==1),max(Distance))


#Find the maximum AirTime for all flights whose Departure delay is not NA
summarise(filter(hflights,!is.na(DepDelay),!is.na(AirTime)),max(AirTime))

#Remove rows that have NA ArrDelay and find the summary of Arrival Delay
summarise(filter(hflights, !is.na(ArrDelay)), earliest= min(ArrDelay), average = mean(ArrDelay), latest= max(ArrDelay), sd=sd(ArrDelay))


#PIPE SYMBOL

# Write the 'piped' version of the English sentences.
hflights %>%
  mutate(diff = TaxiOut - TaxiIn) %>%
  filter(!is.na(diff)) %>%
  summarise(avg = mean(diff))
summarise(filter(mutate(hflights,diff = TaxiOut - TaxiIn),!is.na(diff)),avg = mean(diff))

# Chain together mutate(), filter() and summarise()
#Should you drive or fly ----- Consider waiting time at airport is 
#100 mins and it is not workthwhile if the average speed of flight 
#is less than that of car# Average speed is 60 mph

hflights %>%
  mutate(RealTime = ActualElapsedTime + 100, mph = Distance / RealTime * 60) %>%
  filter( mph < 60) %>%
  summarise(n_less = n(), 
            n_dest = length(unique(Dest)), 
            min_dist = min(Distance), 
            max_dist = max(Distance))

#Ideally you end up paying more for flight so its better that 
#average speed is 1.5 times that of car and also we should not be 
#choosing diverted or cancelled flights
hflights %>%
  mutate(RealTime = ActualElapsedTime + 100, mph = Distance / RealTime * 60) %>%
  filter(!is.na(mph), mph < 90 | Cancelled == 1 |Diverted == 1) %>%
  summarise(n_less = n(), 
            n_dest = length(unique(Dest)), 
            min_dist = min(Distance), 
            max_dist = max(Distance))

#Using n_distinct() function 
hflights %>%
  mutate(RealTime = ActualElapsedTime + 100, mph = Distance / RealTime * 60) %>%
  filter(mph < 90 & Cancelled != 1 & Diverted != 1) %>%
  summarise(n_non = n(), 
            n_dest = n_distinct(Dest), 
            min_dist = min(Distance), 
            max_dist = max(Distance))


# Count the number of overnight flights
#logic-1
# All flights that departed before 5am or arrived after 10pm
filter(hflights, ArrTime > 2200 | DepTime < 0500)
unique(hflights$Cancelled)


#More refinement
select(filter(hflights,DepTime > ArrTime & ArrTime > 500 & DepTime < 2300),ActualElapsedTime,Month:FlightNum)


#GROUP_BY
# Make an ordered per-carrier summary of hflights
hflights %>%
  group_by(UniqueCarrier) %>%
  summarise(avg_delay = mean(ArrDelay, na.rm=TRUE)) %>%
  arrange(avg_delay)

summarise(group_by(hflights,UniqueCarrier, Cancelled),avg_delay = mean(ArrDelay,na.rm =TRUE)) 

#Group by two variables ... UniqueCarrier and Cancelled
A<-hflights %>%
  group_by(UniqueCarrier,Cancelled) %>%
  summarise(avg_delay = mean(ArrDelay, na.rm = TRUE)) %>%
  arrange(avg_delay)

class(unique(hflights$UniqueCarrier))

#Ordered overview of average arrival delays per carrier
hflights %>%
  group_by(UniqueCarrier) %>%
  filter(!is.na(ArrDelay), ArrDelay > 0) %>%
  summarise(avg = mean(ArrDelay)) %>%
  mutate(rank = rank(avg)) %>%
  arrange(rank)

# How many airplanes only flew to one destination from Houston?
hflights %>%
  group_by(TailNum) %>%
  summarise(ndest = n_distinct(Dest)) %>%
  filter(ndest > 365) %>%
  summarise(nplanes = n())

# Find the most visited destination for each carrier
hflights %>% 
  group_by(UniqueCarrier, Dest) %>%
  summarise(n = n()) %>%
  mutate(rank = rank(desc(n))) %>%
  filter(rank == 1)
