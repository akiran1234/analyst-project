import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

fiber=pd.read_csv("https://raw.githubusercontent.com/akiran1234/superds-datasets/master/statinfer/Logisic%20Regression/Fiberbits/Fiberbits.csv")
fiber.shape
list(fiber.columns)
fiber['Num_complaints'].value_counts()

import statsmodels.formula.api as sm
x_vars=fiber.drop(['active_cust'], axis=1)
xvar_names=x_vars.columns
xvar_names.shape[0]

def vif_cal(input_data, dependent_col):
    x_vars=input_data.drop([dependent_col], axis=1)
    xvar_names=x_vars.columns
    for i in range(0,xvar_names.shape[0]):
        y=x_vars[xvar_names[i]] 
        x=x_vars[xvar_names.drop(xvar_names[i])]
        rsq=sm.ols(formula="y~x", data=x_vars).fit().rsquared  
        vif=round(1/(1-rsq),2)
        print (xvar_names[i], " VIF = " , vif)
 
#Calculating VIF values using that function
vif_cal(input_data=fiber, dependent_col="active_cust")
 