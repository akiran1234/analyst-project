import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

startup= pd.read_csv("https://raw.githubusercontent.com/akiran1234/superds-datasets/master/50_Startups.csv")
startup.columns
startup.head()

# Converting the categorical variables to dummy variables.
dummy_state=pd.get_dummies(startup['State'],drop_first=True)
startup=pd.concat([dummy_state,startup],axis=1)
startup.drop(columns=['State'],inplace=True) # Droping the State Categorical column after converting into dummy variables.

# Removing the special chars and spaces in the dataframe column names.
startup.rename(index=str, columns={"New York": "NewYork","R&D Spend": "RDSpend", "Marketing Spend": "MarketingSpend"},inplace=True)

#Divide into X, y variables as below.
X=startup[['Florida', 'NewYork', 'RDSpend', 'Administration', 'MarketingSpend']]
y=startup[['Profit']]

# Summary of the model and backward elimination to find the significant variables can be done by this stats model package.
import statsmodels.api as sm
X=sm.add_constant(X)
model=sm.OLS(y,X).fit()
#model1=sm.ols('Profit~Florida+NewYork+RDSpend+Administration+MarketingSpend',data=train)
#model1_fit=model1.fit()
model.summary()


# Divide the data set into train and test datasets.
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)

# Do the predictions from the sklearn linear model for test data set.
from sklearn.linear_model import LinearRegression
lr = LinearRegression()
lr.fit(X, y)
lr.score(X,y)  # R^2 value to cross check with the stats model R^2 value.
y_pred = lr.predict(X_test)
y_pred

sns.jointplot(y_test,y_pred,kind='reg')

