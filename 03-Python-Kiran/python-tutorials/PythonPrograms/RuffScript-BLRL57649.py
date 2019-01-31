import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
nba=pd.read_csv("https://storage.googleapis.com/dimensionless/Analytics/NBA_train.csv")

nba.columns

X=nba[['SeasonEnd', 'Team', 'Playoffs', 'W','oppPTS', 'FG', 'FGA',
       '2P', '2PA', '3P', '3PA', 'FT', 'FTA', 'ORB', 'DRB', 'AST', 'STL',
       'BLK', 'TOV']]
y=nba[['PTS']]

from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
X_train.shape, X_test.shape, y_train.shape, y_test.shape

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score,mean_squared_error
lr1=LinearRegression()
lres1=lr1.fit(X_train[['FG','2P','3P','FT']],y_train)
lres1.score(X_train[['FG','2P','3P','FT']],y_train)
lres1.intercept_
y_pred=lres1.predict(X_test[['FG','2P','3P','FT']])
mean_squared_error(y_test,y_pred)
r2_score(y_test,y_pred)

sum(y_test.values - y_pred)
type(y_pred)
