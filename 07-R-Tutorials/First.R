wine = read.csv("https://storage.googleapis.com/dimensionless/Analytics/wine.csv")
#View(wine)
#summary(wine)

#plot(Price~AGST,data=wine)
linear=lm(Price~AGST,data=wine)
abline(linear)
