import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=pd.read_csv("https://raw.githubusercontent.com/akiran1234/superds-datasets/master/Salary_Data.csv")
data.columns
#sns.pairplot(data)

X=data[['YearsExperience']].values   # df.values will give 2x2 array, this will avoid the index.
y=data[['Salary']].values

# Dividing the data set to train and test splits.
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

lm=LinearRegression()
lm.fit(X_train,y_train)       # Train the model with train datsets
y_predict=lm.predict(X_test)  # Predict with test dataset
y_p=lm.predict(15) 
plt.scatter(X_train,y_train,color='red')
plt.plot(X_train,lm.predict(X_train),color='b')
plt.xlabel("Experiance")
plt.ylabel("Salary")
plt.title("Exp vs Salary")

plt.scatter(X_test,y_test,color='green')
plt.plot(X_test,lm.predict(X_test),color='r')
plt.xlabel("Experiance")
plt.ylabel("Salary")
plt.title("Exp vs Salary")
# To derive the R^2 and Adj R^2 and tune the model using below code.
import statsmodels.formula.api as sm
model = sm.ols(formula="y_train ~ X_train", data=data)
result=model.fit()
y_pred_sm=model.predict(X_test)
result.summary()
#print result.summary()


# Visualising the Training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, lm.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# Visualising the Test set results
plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, lm.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()






