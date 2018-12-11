Corelation 
correlation does not imply causation example. (Corelation is w.r.t some casual relationship)
Corelation Vs Regression
R2 = Goodness of Fit (R^2 Value will be inbetween 0 and 1 model is said to be good if the R2 value is in between 0.7 to 0.9)

we always check how the model fits the data but not vice versa.
The regression we use is Least Square regression method which is powerfull and infact there are many other regression models as well.
R^2 ( it penalizes the use of variables that are meaningless for the regression.)
Adj R2 is always< R2 

How to find the two variables are linear and non-linear.
Plot the dependent and independent variables (x,y) as scatter plot and if there a straight line then the variables are linear in nature and if the line is not linear i.e other than straight line
i.e polynomial, hyperbolic.
Non-Linear data can be brought into linear by applying exponential function/Log function/Sqrt/cuberoot
No Multicolinearity - This can be found by applying correlation by taking two pair of variables.
Convert Categorical Variables to Dummy variables (n variables=n-1 dummy variables)
Interpretation of Linear Regression Model summary tables.
#######################################################################################################
Variable in Machine Learning
for any machine learning model or function there will be two type of variables 1. dependent variable & 2. Independent Variable.
1. Dependent Variable / Outcome Var/ Explained Variable / Response Var / Label  - Which has to be predicted from the function/machine learning equation.
2. Independent Variable/ Feature / Explanatory Variable /  Predictor Variable/ Regressor/ - 

Confusion Matrix is a performance measurement for any machine learning classification. 
Caliculate Accuracy from confusion matrix (Accuracy will be in between 0-100% i.e is (0-1)).
What is Accuracy Paradox, Accuracy is not only the best metrics to evaluate model. Then check for 
AIC & BIC
ROC & AUC 

Refer for formulaes- https://www.geeksforgeeks.org/confusion-matrix-machine-learning/ 

# Feature Scaling (Independent Variable Scaling)
# Feature scaling is a method used to standardize the range of independent variables.  In data processing, it is also known as data normalization and is generally performed during the data preprocessing step.
# 

1. Loading Data Set
2. Handle Missing Data set
3. Handle Outliers is done after handling the missing data     # https://www.analyticsvidhya.com/blog/2016/01/guide-data-exploration/
3. Encoding Categorical Data Independent Variables
4. Encoding Categorical Data Dependent Variables
5. Do the Feature Scaling for the independent Variables.
6. Find the significant variables to build the optimum model using statsmodel.api package
7. Then check for multi colenearity of one independent variable aganist the other independent variables using VIF function
8.  Split the data into train_and_test 
9. Goodness of fit in Logistic model is measured based on p values as well as AIC value of the model always choose the lowest AIC value model for better results.
10. individual impact of the variables in logistic regression is measured with p value and good ness of fit is measured with confusion matrix.


Column Normalization vs Column Standardisation
Col Norm: All the values of the features will be scaled in between 0-1. Just to avoid the different magnitudes b/w the variables.
Col Std:  (xi-xbar)/std  (for each data point) like x-mu/std. This is most widely used.



#################### Logistic Regression ##############################################################################

#################### Decision Trees ###########################
root node, decision node, leaf node.
How is the best splitting criteria variable decided in Decision Tree. by default= gini index(entropy caliculation)
 Bagging (k-fold cross validation check?)
 
 ######## Feature Selection in Python ###########
 https://machinelearningmastery.com/feature-selection-machine-learning-python/
 1. Filter Methods (Single Factor Analysis)  --- best variable selection
		correlation with target variable
		Information Value
		ChiSquare Test
 2. Wrapper Methods (Best variable combination)
      - Predictive power of the variables is evaluated jointely.
	  - set of variables that performs best (Subset Selection, Forward Selection, Backward Selection)
 3. Embedded Methods
      - Inbuilt variable selection methods taken care by algoritham automatically (With out manual selection or rejection of feature)
	  - Lasso & Ridge Regression
	  - This method is also called shrinkage method.

In forward step wise selection  and backward sted wise elemination why we take only one variable at a time in step wise.

Choosing the best model from - Analytics University
Cross Validation - K-Fold Cross Validation
Use - Adj R-Square, AIC & BIC, RMSE



