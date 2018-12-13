import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

fiber=pd.read_csv("https://raw.githubusercontent.com/akiran1234/superds-datasets/master/statinfer/Logisic%20Regression/Fiberbits/Fiberbits.csv")
fiber.shape
list(fiber.columns)
fiber['Num_complaints'].value_counts()
y=fiber[['active_cust']]
X=fiber[['income', 'months_on_network', 'Num_complaints', 'number_plan_changes', 'relocated', 'monthly_bill', 'technical_issues_per_month', 'Speed_test_result']]

# Find the significant variables using statsmodel package.
# Disadvantage is, always add constant to X variable we cannot print confusion matrix and other few metrics.
# Then use sklearn package for spliting the data into train and test and predict the y variable on train and test datasets.

import statsmodels.api as sm               # endog= y variable	and exog= x variables.
logit=sm.Logit(y,sm.add_constant(X)).fit() # ensure, using stats model package requires adding constant to X variable.
logit.summary2()                           # summary2() will show AIC & BIC but summary() will not show AIC & BIC.

# Split the dataset into train and test data sets.
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

# sklearn will not have summary() function hence we take the help of statsmodel.api 
from sklearn.linear_model import LogisticRegression
model=LogisticRegression().fit(X_train,y_train)
y_pred=model.predict(X_test)
model.score(X_train,y_train) # Printing Accurancy from model

from sklearn.metrics import confusion_matrix
confusion_matrix(y_test,y_pred)
from sklearn.metrics import accuracy_score, classification_report, f1_score
accuracy_score(y_test,y_pred)  
classification_report(y_test,y_pred)
f1_score(y_test,y_pred)


