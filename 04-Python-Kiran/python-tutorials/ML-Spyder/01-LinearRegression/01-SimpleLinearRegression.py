import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm

#%matplotlib inline
data=pd.read_csv("https://raw.githubusercontent.com/akiran1234/superds-datasets/master/Salary_Data.csv")
data.columns

X=data[['YearsExperience']]  # Always ensure to X in double bracket so it will be dataframe else it will become series. and fit() function always expect 2d array or data frame.
y=data[['Salary']]
print(type(X),type(y))

sns.jointplot('YearsExperience','Salary',data=data,kind='reg')

############ Linear Regression using statsmodels to identify significant variables #####################

import statsmodels.api as sm
lm=sm.OLS(y,sm.add_constant(X))                 # creating ols object by giving trainning data
model=lm.fit()                                  # Fitting the model; print(type(model))
model.summary()                                 # printing the summary of the model.
#y_pred_sm = model.predict(X_test_sm)           # predicting the y variable.

############ Linear Regression using sklearn package #####################
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)


from sklearn.linear_model import LinearRegression
sklm=LinearRegression()
sklm.fit(X_train,y_train)                             # fit function always takes 2d array; converting series to numpy array.
y_pred_sk=sklm.predict(X_test)                  
sklm.intercept_                                       # constant for intercept will be taken care by sklearn
sklm.coef_
sklm.score(X_train,y_train)                           # R^2 value will be printed.



############ Linear Regression using statsmodels package R style syntax #####################

''' import statsmodels.formula.api as sm
model=sm.ols('Salary~YearsExperience',data=data)
print(model)
model_fit=model.fit()
model.predict()
model_fit.summary() '''


