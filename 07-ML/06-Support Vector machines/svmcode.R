set.seed(1)
x= matrix(rnorm(20*2),ncol = 2)
x
plot(x)
y = c(rep(-1,10),rep(1,10))
y
plot(x,col=as.factor(y),pch=19)

x[y==1,] <- x[y==1,]+1
plot(x,col=as.factor(y),pch =19)
# They are not linearly seperable

dat = data.frame(x=x,y=as.factor(y))
library(e1071)
svmfit = svm(y~.,data = dat,kernel="linear",cost = 10,scale = F)
plot(svmfit,dat)
make.grid = function(x, n = 75) {
  grange = apply(x, 2, range)
  x1 = seq(from = grange[1, 1], to = grange[2, 1], length = n)
  x2 = seq(from = grange[1, 2], to = grange[2, 2], length = n)
  expand.grid(x.1 = x1, x.2 = x2)
}
xgrid = make.grid(x)
xgrid
ygrid = predict(svmfit, xgrid)
plot(xgrid, col = c("red", "blue")[as.numeric(ygrid)], pch = 20, cex = 0.2)
points(x, col = y + 3, pch = 19)
points(x[svmfit$index, ], pch = 5, cex = 2)

svmfit$index

summary(svmfit)

# What if we instead used a smaller value of the cost parameter?
svmfit = svm(y~.,data = dat,kernel="linear",cost = 0.1,scale = F,probability=T)
plot(svmfit,dat)
svmfit$index
svmfit$probA
svmfit$probB
svmfit$SV
# Cross Validation 

set.seed(1)
tune.out = tune(svm,y~.,data=dat,kernel="linear",ranges=list(cost=c(0.001,0.01,0.1,1,5,10,100)))
summary(tune.out)
plot(tune.out)

bestmod = tune.out$best.model
summary(bestmod)

# generating a testdata set 
set.seed(42)
xtest = matrix(rnorm(20*2),ncol = 2)
ytest = sample(c(-1,1),20,rep=T)
ytest
plot(xtest,col=as.factor(ytest),pch=19)
xtest[ytest==1,]=xtest[ytest==1,]+1
plot(xtest,col=as.factor(ytest),pch=19)
testdat = data.frame(x=xtest,y=as.factor(ytest))

ypred = predict(bestmod,newdata = testdat)
table(testdat$y,ypred)
# Checking with cost = 0.01
svmfit = svm(y~.,data = dat,kernel="linear",cost=0.01,scale=F)
plot(svmfit,dat)

ypred = predict (svmfit , testdat )
table(testdat$y,ypred)

# Linearly seperable data 

x[y==1 ,]= x[y ==1 ,]+0.5
plot(x, col =as.factor(y), pch =19)
# Fitting svm 
dat = data.frame(x=x,y=as.factor(y))
svmfit =svm(y???., data=dat , kernel ="linear", cost =1e5)
plot(svmfit,dat)
summary(svmfit)
# No training errors are made , only 3 support vectors used 

# Decreasing the cost 
svmfit =svm(y~., data=dat , kernel ="linear", cost =1)
plot(svmfit,dat)
summary(svmfit)


## Support Vector machines 

# We first generate some data with a non-linear class boundary

set.seed(1)
x = matrix(rnorm(200*2),ncol=2)
plot(x)
x[1:100,]=x[1:100,]+2
x[100:150,]=x[100:150,]-2

plot(x)
y = c(rep(1,150),rep(2,50))
plot(x,col=as.factor(y),pch=19)
dat = data.frame(x=x,y=as.factor(y))
# Splitting into train and test 
train = sample(200,100)
dat[train,]
svmfit= svm(y~.,data = dat[train,],kernel="radial",gamma=1,cost=1)
plot(svmfit,dat[train,])
summary(svmfit)

# Using a higher cost value 

svmfit= svm(y~.,data = dat[train,],kernel="radial",gamma=1,cost=1e5)

plot(svmfit,dat[train,])
summary(svmfit)
# Perform cross validation to select gamma and cost 

set.seed(1)
tune.out<-tune(svm,y~.,data=dat[train,],kernel="radial",ranges=(list(cost=c(0.1,1,10,100,1000),gamma=c(0,0.25,0.5,1,2,3,4))))

summary(tune.out)

tune.out$best.model
plot(tune.out)

pred_test<-predict(object = tune.out$best.model,newdata=dat[-train,])

table(dat[-train,]$y,pred_test)

set.seed(1)
tune.out<-tune(svm,y~.,data=dat[train,],kernel="poly",ranges=(list(cost=c(0.1,1,10,100,1000),degree=c(1,2,3,4))))

tune.out$best.model

pred_test<-predict(object = tune.out$best.model,newdata=dat[-train,])

table(dat[-train,]$y,pred_test)

svmfit <-svm(y~.,data=dat[train,],kernel="poly",cost=10,degree=4)
plot(svmfit,dat[train,])

pred<-predict(svmfit,newdata = dat[-train,])
pred
table(dat[-train,]$y,pred)
