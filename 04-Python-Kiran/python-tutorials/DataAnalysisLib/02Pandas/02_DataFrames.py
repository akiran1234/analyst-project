# A data frame is a bunch of series where each column represents one series with common label to all series.


import numpy as np
import pandas as pd
from numpy.random import randn

m=np.arange(16).reshape(4,4)    # Creating 4x4 matrix
ind=['a','b','c','d']
d1=pd.DataFrame(m,ind,['c1','c2','c3','c4'])
print(d1)

# Accessing rows and columns
# print(d1[['c1','c2']])             # displaying columns by passing col names in list [c1,c2]

# print(d1[['a','b','c']])           # Displaying rows using index values.

print(d1.loc[['a','b'],['c1','c2']]) # retrieving selected columns and rows

# Deriving new columns

# d1['sumc1c2']=d1['c1']+d1['c2']
# print(d1)

# Accessing rows using index of the rows and labels

# print(d1.iloc[2])       # display rows it will display 3 rows row start with 0.
# print(d1.loc['a'])      # display rows using index label column.


# Drop a column Note axis=0 refers to row axis=1 refers to column
# print(d1.drop('sumc1c2',axis=1))              # This will not permanently delete the column
# print(d1.drop('sumc1c2',axis=1,inplace=True)) # inplace=True will permanently will delete column.
# print(d1)

# Conditional Formatting
