import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

social=pd.read_csv("https://raw.githubusercontent.com/akiran1234/superds-datasets/master/Social_Network_Ads-Logistic.csv")
social.head()
social.shape
social.columns

# Dividing independent and dependent variables
X=social[['Age','EstimatedSalary']].values
y=social['Purchased'].values

# Feature Scaling using StandardScaler
from sklearn import preprocessing
ss=preprocessing.StandardScaler()
X=ss.fit_transform(X)

# Split the dataset into train and test data sets
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.25, random_state=0)

# Create Logistic Model, fit & predict the data.
from sklearn.linear_model import LogisticRegression
model=LogisticRegression(random_state = 0)
model.fit(X_train,y_train)
y_pred=model.predict(X_test)

# Check the model perfomance by calling confusion matrix
from sklearn.metrics import confusion_matrix
confusion_matrix(y_test,y_pred)


