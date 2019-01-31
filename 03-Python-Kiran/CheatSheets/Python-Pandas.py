# Python Points Pandas # Reference- https://pandas.pydata.org/pandas-docs/stable/tutorials.html --> Lessons for new pandas users
# pandas functions are basically divided into Series methods and Dataframe methods.
# df.seriesname.method
# %timeit
# https://github.com/justmarkham/pandas-videos/blob/master/pandas.ipynb  -- Dataschool kevin notebook
*************************************************************************************************************************************
axis=0 means rows and axis=1 means columns.
import pandas as pd
df=pd.read_csv("C:\\DataSets\\emp.csv")                                                                                                                   # Creating data frame from CSV file.
df=pd.read_csv("https://raw.githubusercontent.com/akiran1234/datasets/master/emp.csv")[1:-5]                  # To filter the records based on indexing and slicing
df.to_csv('hello.csv',index=False,header=False)                                                                                                          # Writing to CSV file.
pd.read_csv('filename.txt',columns=[col1,col2,col3])                                                                                                # reading the csv file with required columns
*************************************************************************************************************************************
# Data Frame Info #
df.shape                                                                  # Display the no of rows and columns in the data frame
df.columns                                                             # Display the columns of data frame
df.index                                                                  # Display the index information
df.info()                                                                  # Index info, rows and columns info, display the columns, memory size of the data frame.
df.dtypes                                                                # display the data types of all columns; df[['empno','ename']].dtype- This will display data type of supplied columns.
df.corr()                                                                  # This will show the co relation b/w all the numerical variables of the data frame.
obj_df = df.select_dtypes(include=['object']).copy()  # extract only varchar fields
df.values                                                                # This will display the data frame in 2x2 Array format by avoiding the index return type numpy array object. type(df.values) np.shape(after)
*************************************************************************************************************************************
# Data Frame limiting the records like rownum and limit in SQL 
df.head()                                                                # Will display the first 5 records of the data frame by default.  df.head(10)- Display first 10 records.
df.tail()                                                                   # Will display the last 5 records of the data frame by default.    df.tail(10)   - Display last 10 records.
*************************************************************************************************************************************
# Extracting the rows and columns 
df.columns                                                            # Dispaly the column names of the dataframe.
df['empno']                                                           # Supply the column name in single quotes in square brackets followed by dataframe. column names are case sensitive.
df['empno'].values                                               # To convert datframe to numpy array since it has one column it will become 1d- Numpy Array. print(type(df['empno'].values))
df[['empno','job','deptno']]                                # Supply List to extract  multiple columns from the dataframe. print(type(df[['empno','job','deptno']].values))
df[['empno','job','deptno']].values                    # This will convert to 2x2 numpy array. Single bracket 1d, Double bracket 2D.
df.iloc[:,1:2]                                                         # First : represents all rows second : represents columns. df.iloc[:,1:2] = df.iloc[:,[1,2]]       
df.iloc[:,1:2].values                                             # This will convert again into 2x2 Numpy array.
df.iloc[:3,:]                                                           # Displays first 3 rows and all the columns.
df['deptno'].value_counts()                               # It will display the deptno and it's counts;   select depnto,count() from emp group by depnto.
emp['comm'].value_counts(dropna=False)     # by default pandas methods drop null values so supplying dropna=False we can see the null values as well.
emp['comm'].value_counts(dropna=False,normalize=True) # normalize=True will give us the relative frequency.

emp['Flag'].value_counts() # This is extremely usefull in taking the counts of categorical/ Binary columns. This is a series method hence we cannot use with multiple columns. Data Frame method can be used for data frame and series as well.
caliculate the percentage in each group for it's grouped values.
*************************************************************************************************************************************
# diff b/w loc[], iloc[]  
df.loc[0:5,['R&D Spend', 'Administration', 'Marketing Spend']]    # in loc[] rows=0:5, 5 is inclusive and columns = 'Marketing Spend' is also inclusive.
start.iloc[0:5,0:3]                                                                                # in iloc[] rows=0:5 , 5 is exclusive and columns=0:3, 3 is exclusive.

# Find Null Values in data frame 
df.isnull().sum()                                                    # It will sum the null values across all the columns of the data frame
df['comm'].isnull().sum()                                    # It will sum the null values of comm column. function calling other function
df[df['comm'].isnull()]                                         # Display the records which are null
df[df['comm'].notnull()]                                      # Display records which are not null
df.count()                                                              # Pandas methods by default it will ignore NaN values in count
df.sum()                                                                # un like in DB's this sum function will work for all data types. For binary values(True/False) it will sum only True values i.e sum of 1's.
*************************************************************************************************************************************
# Reading data from data frame 
df[['empno','sal','comm']]                                  # selecting the required columns from the data frame by passing the list.
df[['empno','sal','comm']][:6]                            # selecting the required columns and reading the first 6 records from the data frame.
df[['empno','sal','comm']].head(6)                   # Listing the first 6 records with selected columns.
df['job'].value_counts()                                      # list the count of grouped values in a column; Similarly in  SQL -  select count(*) from emp group by job 
df.values                                                               # Print the values of data frame as 2-d nested list.
df.sample(n=5)                                                    # sample the records randomly from the data frame.
*************************************************************************************************************************************
# Indexing using iloc[] and loc[] methods 
df.iloc[:,:]                                                                # Will display all the rows and columns on index basis. Works like rownum to display the N records.
df.iloc[:3,:4]                                                           # Will display rows(0,1,2) and columns(0,1,2,3).
df[:6]                                                                       # We can retrivew only rows from this method using index slicing
emp.loc[:,'ename']                                               # extract all the rows and ename column only.
df.index = list("abcdefghijklmn")                         # Assigning the index with new values.
df.loc[['g','k']]                                                        # extract records based on index labels using loc[] method.
df[:'g']                                                                     # start from 'a' index row and print till 'g' index row by excluding it.
df['c':]                                                                     # Start from 'c' row and print till end of the row.
*************************************************************************************************************************************
#sorting 
df.sort_values(by='deptno')                                            # Sort the data frame with single values
df.sort_values(by='sal',ascending=False).head(5)        # To pick top 5 salaries
df.sort_values(by=['deptno','sal'])                                 # Sort with multiple values.
df[(df['deptno']==10) | (df['deptno']==20)].sort_values(by=['deptno','sal'])  # Filter DF and sort with columns.
*************************************************************************************************************************************
#unique values in a column 
df['deptno'].unique()                                           # unique() method belongs to series object hence it cannot be applied on data frame object. This will give the unique values like distinct in sql.
df['deptno'].nunique()                                         # it will give the no of unique values from the column.
*************************************************************************************************************************************
#Boolean Data Frame (Where clause) 
df[sal]>5                                                                # Will display boolean table.
df[df[sal]>1500]                                                   # Works like where class. The dataframe records with matched condition will be displayed with all the columns.
df[df['deptno']==10]                                            # Usage of equality operator.
df[(df['sal']>1500) & (df['deptno']==20)]          # Conditional formating i.e where clause with multiple conditions (Usage of and(&) operator)
df[(df['deptno']==10) | (df['deptno']==20)]     # or operator(|), conditional formating.
*************************************************************************************************************************************
# filter dataframe
emp[(emp['deptno']==20) & (emp['sal']>2000)]                                      # Filter the data frame
emp[['empno','ename']][(emp['deptno']==20) & (emp['sal']>2000)]    # Filter the data frame and select the required columns.
emp.loc[(emp.deptno==20) & (emp.sal>1000), : ]                                   # loc[conditon for rows, list of columns] is the best practise columns is empy it will display all the columns
emp.loc[(emp.deptno==20) & (emp.sal>1000),['empno','ename']]       # will display columns empno & ename only.
emp[emp.deptno.isin([10,20])]                                                                  # It will work like in operator in db.
*************************************************************************************************************************************
# finding duplicates 
ufo.City.duplicated().sum()                                                                         # will give the no of duplicated values.
ufo.City.nunique().sum()                                                                             # will give the no of unique values; sum of both will give total record count.
emp[~emp.deptno.duplicated()].head()                                                    # duplicated() method returns unique value as false and duplicate as true, so true will display duplicate values so we take inverse
*************************************************************************************************************************************
# Rename of data fram columns.
emp.rename(columns={'empno':'EMPNO','ename':'ENAME'},inplace=True)  # pass the dictionary 1 way.
emp.columns=emp.columns.str.upper()                                                              # 2nd way of passing values directly to columns attribute or take a list and assign.
*************************************************************************************************************************************
# droping the columns.
ufo.drop(columns=['City','State'],axis=1,inplace=True)
*************************************************************************************************************************************
# delete/ drop the rows
ufo.drop(labels=[0,1,2,3],axis=0)                                                                          # labels refer to row index.
*************************************************************************************************************************************
# conditional update of data frame columns (update statement like sql)
df = pd.DataFrame({'AAA' : [4,5,6,7], 'BBB' : [10,20,30,40],'CCC' : [100,50,-30,-50]}); df
df.loc[df.AAA >= 5,'BBB'] = -1; df                                                       # Condition check on 'AAA' column and apply change on other column 'BBB'
df.loc[df.AAA >= 5,['BBB','CCC']] = 555; df                                       # Condition check on 'AAA' column  and apply changes on BBB and CCC columns.
df.loc[(df['AAA']==4) & (df['BBB']==10),['AAA','BBB','CCC']]=40   # Checking condition on two columns and assign change to three columns.
# df.loc[] will work like "if then" but not "if then else" hence np.where() will work for "if then else" functionality.
nba=np.where(nba.PTS==8573,100,99)                                          # works like decode if true then 100 will be assigned else 99. (If then else)
*************************************************************************************************************************************
# group by 
# when ever grouping is done a groupby object is created and statistical functions/grouping functions will be applied on each of this objects. (gd=dt.groupby('deptno'); type(gd))
# groupby task in pandas will work like this Split(Grouping column), Apply(grouping function), combine(Result will be combined from all groups and displayed). Refer Diagram
# The data is splitted into groups and each group is a key value pair, key will be groupby column and value will be entire data. 
# df=pd.read_csv("https://raw.githubusercontent.com/akiran1234/datasets/master/OfficeSupplies.csv")
# https://pandas.pydata.org/pandas-docs/stable/groupby.html

gd=df.groupby('deptno')                     # grouping on deptno and creating groupby object gd. Here each group will have key

# To view the group by data method 1
for i,j in gd:                         
    print(i)                                               # key value (10,20,30)
	print(j)                                               # data for each group 
	
# To view the group by data method 2 using get_group() method.
gd.get_group(10)                                 # Reding on deptno=10 group; If groupby is done on varchar field pass groupby value is Quotes.
# Apply stat functions on grouped data
gd.min()                                                # min() function is applied on each of the column of data frame and display the min value from each of the columns.
gd.max()                                               # max() function is applied on each of the column of data frame and display the max value from each of the columns.
gd.describe()                                        # It will show statistics for all the numeric columns and exclude varchar fields.
gd.size()/gd.count()                            # Will show the count of all groups.
gd['sal'].max()                                     # This will show max sal from each deptno; select max(sal) from emp group by deptno
df.groupby('Region').sum()               # In one shot creating grouping object and applying statistical function.
df.groupby('Region').describe()

df['deptno'].value_counts()               # It will display the deptno and it's counts;   select depnto,count() from emp group by depnto.

# when group by is applied a groupby object is created with key,value pair. key=groupby key values, value= block of unit of group value.
emp.groupby(by='deptno').max()                                                                #  This will group by deptno and takes the max value from all the columns of data frame.
emp.groupby(by='deptno').sal.max()                                                          # grouping by deptno and finding the max value on only sal column.
emp.groupby(by='deptno').sal.agg(['min','max','mean','std'])                 # agg() method is applied on groupby object to pass the required group functions.
*************************************************************************************************************************************
# merge() - Joins 
# merge() method will perform the join operations same as data base joins
# syntax -->                                      left_df.merge(right_df,on=[keys],how='inner/left/right/outer')
# If join key names is different ;  left_df.merge(right_df,left_on='lkey', right_on='rkey',how='inner/left/right/outer')
df_emp[['empno','ename','deptno']].merge(df_dept[['deptno','dname']],on='deptno',how='right')
*************************************************************************************************************************************
# pd.concat() - Union 
# In data base to combine(Union/Union ALL/minus/Intersect) tow tables should have same structure.
# In Pandas data frames it is not necessary that tow data frames should be of same structure
# The data frames can be joined vertically or horizontally 
pd.concat([df_emp[['empno','ename']],df_dept[['dname','location']]],axis=0)    # axis=0 combines vertically(column wise) axis=1 joins horizontally (row wise).
*************************************************************************************************************************************
# apply() method 
# String functions- https://pandas.pydata.org/pandas-docs/stable/text.html
Explore more on apply() function.
df.Email.apply(lambda x: str(x).split('@')[-1])       # converting into string and apply string function 
*************************************************************************************************************************************
# string functions 
emp[emp.job.str.isdecimal()]                                                                     # filter using str method internally it will return True/False and typecasting to data frame.
emp['newcol']=emp.job.str.join('|')                                                          # applying string method and appending/updating to actual data frame.
*************************************************************************************************************************************
# data type conversion 
emp['mgr']=emp.mgr.astype(dtype='int64')                                            # converting float to int64 data type
*************************************************************************************************************************************
# pivot tables 
*************************************************************************************************************************************
# read & writing from different files (csv,tsv,excel,xml,html,json,data base) 
*************************************************************************************************************************************
# Imp functions 
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
df.describe()
ufo.dropna(how='any').shape                                                                # if 'any' values are missing in a row, then drop that row
ufo.dropna(how='all').shape                                                                  # if 'all' values are missing in a row, then drop that row (none are dropped in this case) inplace=False.
ufo.dropna(subset=['City', 'Shape Reported'], how='any').shape      # drop only if NaN in available in supplied columns.
emp.comm.fillna(value=emp.comm.mean())                                      # imputation
data.fillna({'C5':data.C5.mean(),'C6':data.C6.mean()},inplace=True)
*************************************************************************************************************************************
# pickle & un pickle 
df.to_pickle('path/filename.pkl')                                                   # it will create a pickle object which is stored on disk with filenam.pkl and copy it into pen drive/flash drive
df.read_pickle('path/filename.pkl')                                               # copy the pickle object from flash drive to other machine this stored pickle object can be read.
*************************************************************************************************************************************
# create dummy variables 
pd.get_dummies(df,columns=['State'],drop_first=True)             # pass the list of categorical variables to list of columns and enable drop_first=True to handle dummy variable trap.
*************************************************************************************************************************************
# convert string object to datetime datatype 
ufo['Time']=pd.to_datetime(ufo.Time)                                         # ensure this is pandas function, this will convert string to datetime datatype.
ufo.Time.dt.year                                                                              # applying dt attributes on ; Series.dt can be used to access the values of the series as datetimelike and return several properties.
df['timeStamp'].apply(lambda x: x.year)
*************************************************************************************************************************************
# map(), apply(), applymap() 
ufo.state.map({'blr':'bangalore','hyd':'hyderabad','male':'m'}) # map() is series function 
apply()                                                                                              # this is applied either to row or column of every element.
applymap()                                                                                      # this is applied to every element of dataframe row wise and column wise.
emp['lambda']=emp.deptno.apply(lambda x:'Ten' if x==10 else ('Twenty' if x==20 else 'Thirty')) # if elif else in lambda function
emp['deptno']=emp.deptno.apply(lambda x:'Ten' if x==10 else ('Twenty' if x==20 else 'Thirty'))  # assign to same column
*************************************************************************************************************************************
# plotting in pandas 
iris.plot.line('petal_width','petal_length')                                   # This will just draw the lines joining the data points but won't draw regression line. This is used in timeseries plotting.
iris.plot.bar('species','petal_length')                                            #  plt.bar(iris['species'], iris['petal_length'])
iris.plot.box()                                                                                  # drawing box plot, all the numeric fields will be plotted automatically and categorical will be ignored.
iris.sepal_length.plot.box()                                                           # drawing on single columns; In box plots we dont slice the data we give the whole column.
iris.plot.hist('petal_width',alpha=0.4)                                          # drawing histrogram from pandas df.
iris.plot.scatter('petal_width','petal_length')                              # Drawing scatter plot.
iris.plot.area('species','petal_length')                                          # Area plot by giving x=independent and y=dependent. 
iris.plot.density()                                                                            # kde plotting for all numeric variables.
iris.boxplot(column='sepal_length',by='species')                       # bar will tell the sum of values for the categorical variable, box will tell the percentile of the categories.
ax=iris.plot.box()                                                                            # Creating plot object 
ax.set_xlabel("X-Axis")                                                                   # Set the x-axis label
ax.set_ylabel("Y-Axis")                                                                   # Set the y-axis label
*************************************************************************************************************************************
# numpy 
np.reshape(3,3) # This will create 2d matrix from 1d array.
np.ravel()             # flatten the 2d array to 1d.
*************************************************************************************************************************************
# connecting to database from python

import pymysql
import pandas as pd
import sqlalchemy
conn=sqlalchemy.create_engine('mysql+pymysql://root:mysql@localhost:3306/sakila')
df=pd.read_sql_table('actor',conn)
print(df.head(5))

# connecting to oracle database from python.
# https://www.boureliou.com/technoblog/blog/2009/connecting-to-oracle-with-sqlachemy-and-plone-integration ; connecting to oracle.
import cx_Oracle
conn = cx_Oracle.connect('username/password@localhost/orcl')
ver = con.version.split(".")
print ver
*************************************************************************************************************************************
# Find outliers in dataframe 
from scipy import stats
import numpy as np
z = np.abs(stats.zscore(boston_df))
print(z)

def outlierDetect(df,col):
    q1=df.quantile(0.25)
    q3=df.quantile(0.75)
    iqr=q3-q1
    lbound= q1-1.5*IQR
    ubound= q3+1.5*IQR
  
df[(df['col']<lbound) | (df['col']>ubound)]   # display outlier records
df[~(df['col']<lbound) | (df['col']>ubound)] # display non-outlier records ; create a function and call the function from df.apply()
df['outlier']=df[(df['col']<lbound) | (df['col']>ubound)]
*************************************************************************************************************************************
# Do descriptive statistics & plotting with Python 

How to read multiple files in pandas.
path =r'C:\DRO\DCL_rawdata_files' # use your path
allFiles = glob.glob(path + "/*.csv")
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None, header=0)
    list_.append(df)
frame = pd.concat(list_)


















