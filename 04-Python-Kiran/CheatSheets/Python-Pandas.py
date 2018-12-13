# Python Points Pandas # Reference- https://pandas.pydata.org/pandas-docs/stable/tutorials.html --> Lessons for new pandas users

axis=0 means rows and axis=1 means columns.
import pandas as pd
df=pd.read_csv("C:\\DataSets\\emp.csv")                                                                                                                   # Creating data frame from CSV file.
df=pd.read_csv("https://raw.githubusercontent.com/akiran1234/datasets/master/emp.csv")[1:-5]         # To filter the records based on indexing and slicing
df.to_csv('hello.csv',index=False,header=False)                                                                                                          # Writing to CSV file.

################# Extracting the rows and columns ####################################
df.columns                                      # Dispaly the column names of the dataframe.
df['empno']                                     # Supply the column name in single quotes in square brackets followed by dataframe. column names are case sensitive.
df['empno'].values                        # To convert datframe to numpy array since it has one column it will become 1d- Numpy Array. print(type(df['empno'].values))
df[['empno','job','deptno']]        # Supply List to extract  multiple columns from the dataframe. print(type(df[['empno','job','deptno']].values))
df[['empno','job','deptno']].values # This will convert to 2x2 numpy array. Single bracket 1d, Double bracket 2D.
df.iloc[:,1:2]                                    # First : represents all rows second : represents columns. df.iloc[:,1:2] = df.iloc[:,[1,2]]       
df.iloc[:,1:2].values                       # This will convert again into 2x2 Numpy array.
df.iloc[:3,:]                                       # Displays first 3 rows and all the columns.
df['deptno'].value_counts()        # It will display the deptno and it's counts;   select depnto,count() from emp group by depnto.



############### Data Frame Info ####################################################
df.shape                                                                  # Display the no of rows and columns in the data frame
df.columns                                                             # Display the columns of data frame
df.index                                                                  # Display the index information
df.info()                                                                  # Index info, rows and columns info, display the columns, memory size of the data frame.
df.dtypes                                                                # display the data types of all columns; df[['empno','ename']].dtype- This will display data type of supplied columns.
df.corr()                                                                  # This will show the co relation b/w all the numerical variables of the data frame.
obj_df = df.select_dtypes(include=['object']).copy()  # extract only varchar fields
df.values                                                                # This will display the data frame in 2x2 Array format by avoiding the index return type numpy array object. type(df.values) np.shape(after)

############### Data Frame limiting the records like rownum and limit in SQL ######################
df.head()                                                                # Will display the first 5 records of the data frame by default.  df.head(10)- Display first 10 records.
df.tail()                                                                   # Will display the last 5 records of the data frame by default.    df.tail(10)   - Display last 10 records.

################ Find Null Values in data frame ###################################################
df.isnull().sum()                                                    # It will sum the null values across all the columns of the data frame
df['comm'].isnull().sum()                                   # It will sum the null values of comm column. function calling other function

df[df['comm'].isnull()]                                        # Display the records which are null
df[df['comm'].notnull()]                                    # Display records which are not null

############### Reading data from data frame ##############################################
df[['empno','sal','comm']]                                  # selecting the required columns from the data frame by passing the list.
df[['empno','sal','comm']][:6]                           # selecting the required columns and reading the first 6 records from the data frame.
df[['empno','sal','comm']].head(6)                  # Listing the first 6 records with selected columns.
df['job'].value_counts()                                      # list the count of grouped values in a column; Similarly in  SQL -  select count(*) from emp group by job 
df.values                                                                 # Print the values of data frame as 2-d nested list.
df.sample(n=5)                                                      # sample the records randomly from the data frame.
############ Indexing using iloc[] and loc[] methods ############################################
df.iloc[:,:]                                                                # Will display all the rows and columns on index basis. Works like rownum to display the N records.
df.iloc[:3,:4]                                                           # Will display rows(0,1,2) and columns(0,1,2,3).
df[:6]                                                                       # We can retrivew only rows from this method using index slicing

emp.loc[:,'ename']                                               # extract all the rows and ename column only.
df.index = list("abcdefghijklmn")                      # Assigning the index with new values.
df.loc[['g','k']]                                                        # extract records based on index labels using loc[] method.
df[:'g']                                                                     # start from 'a' index row and print till 'g' index row by excluding it.
df['c':]                                                                     # Start from 'c' row and print till end of the row.

############ sorting ############################################################################
df.sort_values(by='deptno')                             # Sort the data frame with single values
df.sort_values(by='sal',ascending=False).head(5)        # To pick top 5 salaries
df.sort_values(by=['deptno','sal'])                  # Sort with multiple values.
df[(df['deptno']==10) | (df['deptno']==20)].sort_values(by=['deptno','sal'])  # Filter DF and sort with columns.

############# unique values in a column ##################
df['deptno'].unique()                                        # unique() method belongs to series object hence it cannot be applied on data frame object. This will give the unique values.
df['deptno'].nunique()                                      # it will give the no of unique values from the column.

########## Boolean Data Frame (Where clause) #################################################
df[sal]>5                                                                  # Will display boolean table.
df[df[sal]>1500]                                                    # Works like where class. The dataframe records with matched condition will be displayed with all the columns.
df[df['deptno']==10]                                            # Usage of equality operator.

df[(df['sal']>1500) & (df['deptno']==20)]        # Conditional formating i.e where clause with multiple conditions (Usage of and(&) operator)
df[(df['deptno']==10) | (df['deptno']==20)]   # or operator(|), conditional formating.

############ group by ##################################
# when ever grouping is done a groupby object is created and statistical functions/grouping functions will be applied on each of this objects. (gd=dt.groupby('deptno'); type(gd))
# groupby task in pandas will work like this Split(Grouping column), Apply(grouping function), combine(Result will be combined from all groups and displayed). Refer Diagram
# The data is splitted into groups and each group is a key value pair, key will be groupby column and value will be entire data. 
# df=pd.read_csv("https://raw.githubusercontent.com/akiran1234/datasets/master/OfficeSupplies.csv")
# https://pandas.pydata.org/pandas-docs/stable/groupby.html

gd=df.groupby('deptno')  # grouping on deptno and creating groupby object gd. Here each group will have key

# To view the group by data method 1
for i,j in gd:                         
    print(i)                                         # key value (10,20,30)
	print(j)                                         # data for each group 
	
# To view the group by data method 2 using get_group() method.
gd.get_group(10)                         # Reding on deptno=10 group; If groupby is done on varchar field pass groupby value is Quotes.
# Apply stat functions on grouped data
gd.min()                                          # min() function is applied on each of the column of data frame and display the min value from each of the columns.
gd.max()                                         # max() function is applied on each of the column of data frame and display the max value from each of the columns.
gd.describe()                                 # It will show statistics for all the numeric columns and exclude varchar fields.
gd.size()/gd.count()                    # Will show the count of all groups.
gd['sal'].max()                               # This will show max sal from each deptno; select max(sal) from emp group by deptno
df.groupby('Region').sum()        # In one shot creating grouping object and applying statistical function.
df.groupby('Region').describe()

df['deptno'].value_counts()       # It will display the deptno and it's counts;   select depnto,count() from emp group by depnto.

############ merge() - Joins #########################
# merge() method will perform the join operations same as data base joins
# syntax -->                                      left_df.merge(right_df,on=[keys],how='inner/left/right/outer')
# If join key names is different ;  left_df.merge(right_df,left_on='lkey', right_on='rkey',how='inner/left/right/outer')
df_emp[['empno','ename','deptno']].merge(df_dept[['deptno','dname']],on='deptno',how='right')

############ pd.concat() - Union #########################
# In data base to combine(Union/Union ALL/minus/Intersect) tow tables should have same structure.
# In Pandas data frames it is not necessary that tow data frames should be of same structure
# The data frames can be joined vertically or horizontally 
pd.concat([df_emp[['empno','ename']],df_dept[['dname','location']]],axis=0)    # axis=0 combines vertically(column wise) axis=1 joins horizontally (row wise).

########## apply() method #########################################################
# String functions- https://pandas.pydata.org/pandas-docs/stable/text.html
Explore more on apply() function.

########### pivot tables ######################################################################

########### read & writing from different files (csv,tsv,excel,xml,html,json,data base) ######################################################################

########### Imp functions######################################################################
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df.describe()

########### Find outliers in dataframe ###################
from scipy import stats
import numpy as np
z = np.abs(stats.zscore(boston_df))
print(z)

q1=df.quantile(0.25)
q3=df.quantile(0.75)
iqr=q3-q1
lower_bound= q1-1.5*IQR
upper_bound= q3+1.5*IQR
df[(df['col']<lower_bound) | (df['col']>upper_bound)]   # display outlier records
df[~(df['col']<lower_bound) | (df['col']>upper_bound)] # display non-outlier records ; create a function and call the function from df.apply()
df['outlier']=df[(df['col']<lower_bound) | (df['col']>upper_bound)]

############ Do descriptive statistics & plotting with Python #######################################

How to read multiple files in pandas.
path =r'C:\DRO\DCL_rawdata_files' # use your path
allFiles = glob.glob(path + "/*.csv")
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0)
    list_.append(df)
frame = pd.concat(list_)
