flower=read.csv("https://storage.googleapis.com/dimensionless/Analytics/flower.csv",header=FALSE)
flowerMatrix=as.matrix(flower)
class(flowerMatrix)
str(flowerMatrix)
flowerVector=as.vector(flowerMatrix)
class(flowerVector)
distance<-dist(flowerVector,method = "euclidean")
str(distance)
clusterIntensity<-hclust(distance,method="ward.D")
clusterIntensity$merge


plot(clusterIntensity)
rect.hclust(clusterIntensity,3)

flowerClusters<-cutree(clusterIntensity,k=3)
str(flowerClusters)
tapply(flowerVector,flowerClusters,mean)
table(flowerClusters)
#matrix(flowerClusters,50,50)
dim(flowerClusters)= c(50,50)
mat<-matrix(flowerClusters,nrow = 50,ncol = 50,byrow = F)
flowerClusters
class(flowerClusters)
image(flowerClusters,axes=F)
image(flowerMatrix,axes=FALSE,col = grey(seq(0,1,length=256)))
image(flowerClusters,axes=FALSE,col = grey(seq(0,1,length=3)))
par(mfrow=c(1,1))
image(flowerMatrix)
# MRI Image segmentation
# Let's try this with an MRI image of the brain

healthy = read.csv("C:/Users/himanshu arora/Documents/Data Science/Analytics Edge/Unit 6/Case 2 - Image segmentation/healthy.csv", header=FALSE)
healthyMatrix = as.matrix(healthy)
str(healthyMatrix)
image(healthyMatrix)
image(healthyMatrix,col=grey(seq(0,1,length=256)),axes=F)
# Hierarchial clustering
healthyVector = as.vector(healthyMatrix)
distance = dist(healthyVector, method = "euclidean")

# We have an error - why?
str(healthyVector)



# Plot image
image(healthyMatrix,axes=FALSE,col=grey(seq(0,1,length=256)))

# K means clustering
# Specify number of clusters
k = 5

# Run k-means
set.seed(1)
KMC = kmeans(healthyVector, centers = k, iter.max = 1000)
kmeans(healthyVector,centers = 5,iter.max = 50)
str(KMC)
KMC$betweenss

healthyClusters<-KMC$cluster

# Extract clusters
healthyClusters = KMC$cluster
KMC$centers[2]
KMC$withinss
KMC$tot.withinss
KMC$size
# Plot the image with the clusters
dim(healthyClusters) = c(nrow(healthyMatrix), ncol(healthyMatrix))
dim(healthyClusters) = c(566, 646)
#Image 
image(healthyClusters,axes=FALSE,col = rainbow(k))
image(healthyClusters,axes=FALSE,col = grey(seq(0,1,length=256)))
par(mfrow=c(1,2))
# Scree Plots
set.seed(1)
KMC2 = kmeans(healthyVector, centers =2, iter.max = 1000)
KMC2$withinss
KMC2$tot.withinss
SumWithinss = sapply(2:10, function(x) {sum(kmeans(healthyVector, centers=x, iter.max=1000)$withinss)})

SumWithinss = sapply(2:10, function(x) {kmeans(healthyVector, centers=x, iter.max=1000)$tot.withinss})
totwithinss = NULL
for (k in 2:10){
  set.seed(1)
  totwithinss[k-1] = (kmeans(healthyVector, centers =k, iter.max = 1000))$tot.withinss
}
totwithinss
NumClusters = seq(2,10,1)
plot(NumClusters,SumWithinss,type="b")

# Tumor 

tumor<-read.csv("https://storage.googleapis.com/dimensionless/Analytics/tumor.csv",header=FALSE)
str(tumor)
tumorMatrix<-as.matrix(tumor)
tumorVector<-as.vector(tumorMatrix)
image(tumorMatrix,axes=FALSE,col=grey(seq(0,1,length=256)))
library(flexclust)
KMC.kcca = as.kcca(KMC, healthyVector)
KMC.kcca@family
KMC.kcca@centers
KMC.kcca@clusinfo
KMC.kcca@xcent
KMC.kcca@totaldist
KMC.kcca@clsim
KMC.kcca@family
summary(KMC.kcca)
tumorClusters <-predict(KMC.kcca, newdata=tumorVector)
head(tumorClusters,50)
summary(tumorClusters)
str(tumorClusters)
table(tumorClusters)

# Segmented Image

dim(tumorClusters)<-c(nrow(tumorMatrix),ncol(tumorMatrix))
dim(tumorMatrix)

image(tumorClusters,axes=FALSE,col=rainbow(k))
dim(tumorVector)<-c(571,512)
image(tumorMatrix,axes=F)
image.default(tumorMatrix)
image(t(tumorVector))
tumortrans<-t(tumorVector)
image(t(t(tumortrans)))
image()