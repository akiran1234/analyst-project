# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

####### Encoding Categorical Data ###############

data=pd.read_csv("https://raw.githubusercontent.com/akiran1234/datasets/master/OfficeSupplies.csv")
data.columns
dummy=pd.get_dummies(data['Region'],drop_first=True)        # Droping first column to avoid dummy variable trap.
data=pd.concat([dummy,data],axis=1,verify_integrity=True)
data.drop(columns=['OrderDate', 'Region'],inplace=True)
data


