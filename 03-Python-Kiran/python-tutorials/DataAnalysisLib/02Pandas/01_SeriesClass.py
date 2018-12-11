# Pandas mainly deal with three data structures (Series[1-d], DataFrame[2-d] and Panel[3-d])
# Series is sub set of DataFrame and it is subset of Panel
# A series can be created from various sources ndarray, list, dictionary, scalar/constant value
import numpy as np
import pandas as pd


# Syntax = pandas.Series( data, index, dtype, copy)

l=[10,20,30,40,50]
d={'name':'Kiran','id':100,'sal':1000.50}              # When dict is passed as data key values will be taken as index.

s1=pd.Series(l,index=['a','b','c','d','e'])            # Creating Series from a list.
print(s1.iloc[[0]])

s2=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])  # Passing data and index directly
#print(s2)

s3= pd.Series(5,['a','b','c','d','e'])                 # Passing constant value with index values.
#print(s3)

s4=pd.Series(d)   # When dict is passed as data, keys will be taken as index and values will be data.
#print(s4)

# Accessing series data obj[row_index]

print(s2[0:3])    # To retrieve first 3 rows

# # Panda Series will take two args data and label(Index) as inputs and displayed at the output.
#
# l1=[10,20,30,40,50]
# ind=['a','b','c','d','e']
#
#
# # print(pd.Series(l1,ind))   # Here l1 is data and ind items will be displayed as index.
# # print(pd.Series(l1))       # Always index is displayed as first column. If index column is not provided it will display default index.
# # print(pd.Series(data=ind)) # Data field is assigned with ind then it displayed default index.
#
# a1=np.array([1,2,3,4,5])
# a2=np.array([6,7,8,9,10])
# loc1=['hyd','blr','del','pune','chn']
# loc2=['rjy','vjw','hyd','blr','del']
#
# s1=pd.Series(a1,loc1)
# s2=pd.Series(a2,loc2)
#
# print("Series1=",s1,sep='\n')
# print("Series2=",s2,sep='\n')
#
# # Operations on Series; s1+s2, s1-s2, s3*s4 so on and so forth ..
#
# print(s1+s2) # It will check for the matching labels and it will do sum and for non matching it will result Null(NaN)

