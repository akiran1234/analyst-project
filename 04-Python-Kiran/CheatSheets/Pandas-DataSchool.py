
########### pandas ############################## Reference -> https://github.com/justmarkham/pandas-videos/blob/master/pandas.ipynb
pandas functions are basically divided into Series methods and Dataframe methods.
df.seriesname.method

df.count()       # Pandas methods by default it will ignore NaN values in count
df.sum()          # un like in DB's this sum function will work for all data types. For binary values(True/False) it will sum only True values i.e sum of 1's.

df.dropna()    # by default it check row wise if any null across the values of row that row is dropped. if axis=1 then it checks any NaN value column wise.
emp['comm'].value_counts(dropna=False) # by default pandas methods drop null values so supplying dropna=False we can see the null values as well.
emp['comm'].value_counts(dropna=False,normalize=True) # normalize=True will give us the relative frequency.

emp['Flag'].value_counts() # This is extremely usefull in taking the counts of categorical/ Binary columns. This is a series method hence we cannot use with multiple columns. Data Frame method can be used for data frame and series as well.
caliculate the percentage in each group for it's grouped values.




############ Data Cleansing in Python ####################################
1. grab the dataset and check for any column which has all the values as nulls.      # df.isnull().sum() ;       df.dropna()
2. Now handle missing values.
############## Data School Tutorials ###############
shift+tab; once, twice, third
# Rename of data fram columns.
emp.rename(columns={'empno':'EMPNO','ename':'ENAME'},inplace=True)  # pass the dictionary 1 way.
emp.columns=emp.columns.str.upper()    # 2nd way of passing values directly to columns attribute or take a list and assign.
# droping the columns.
ufo.drop(columns=['City','State'],axis=1,inplace=True)
# delete/ drop the rows
ufo.drop(labels=[0,1,2,3],axis=0)                                                                  # labels refer to row index.
# sorting of data frame
emp.sort_values(by=['DEPTNO','SAL'],ascending=True)                          # ascending= False will sort in descending order.
# filter dataframe
emp[(emp['deptno']==20) & (emp['sal']>2000)]                                        # Filter the data frame
emp[['empno','ename']][(emp['deptno']==20) & (emp['sal']>2000)]    # Filter the data frame and select the required columns.
emp.loc[(emp.deptno==20) & (emp.sal>1000), : ]                                    # loc[conditon for rows, list of columns] is the best practise columns is empy it will display all the columns
emp.loc[(emp.deptno==20) & (emp.sal>1000),['empno','ename']]      # will display columns empno & ename only.
emp[emp.deptno.isin([10,20])]                                                                      # It will work like in operator in db.
######## read the file with specific columsns #########
pd.read_csv('filename.txt',columns=[col1,col2,col3])                              # reading the csv file with required columns
####### string functions ##########
emp[emp.job.str.isdecimal()]                                                                         # filter using str method internally it will return True/False and typecasting to data frame.
emp['newcol']=emp.job.str.join('|')                                                              # applying string method and appending/updating to actual data frame.

####### data type conversion ###############
emp['mgr']=emp.mgr.astype(dtype='int64')                                               # converting float to int64 data type

####### group by ######################
# when group by is applied a groupby object is created with key,value pair. key=groupby key values, value= block of unit of group value.
emp.groupby(by='deptno').max()                                                                #  This will group by deptno and takes the max value from all the columns of data frame.
emp.groupby(by='deptno').sal.max()                                                          # grouping by deptno and finding the max value on only sal column.
emp.groupby(by='deptno').sal.agg(['min','max','mean','std'])              # agg() method is applied on groupby object to pass the required group functions.

###### plot with pandas #############
start.State.value_counts().plot(kind='bar') 

######### missing values ##############
ufo.dropna(how='any').shape                                                                     # if 'any' values are missing in a row, then drop that row
ufo.dropna(how='all').shape                                                                       # if 'all' values are missing in a row, then drop that row (none are dropped in this case) inplace=False.
ufo.dropna(subset=['City', 'Shape Reported'], how='any').shape      # drop only if NaN in available in supplied columns.

emp.comm.fillna(value=emp.comm.mean())

######### diff b/w loc[], iloc[]  ############
df.loc[0:5,['R&D Spend', 'Administration', 'Marketing Spend']]         # in loc[] rows=0:5, 5 is inclusive and columns = 'Marketing Spend' is also inclusive.
start.iloc[0:5,0:3]                                                                                           # in iloc[] rows=0:5, 5 is is exclusive and columns=0:3, 3 is exclusive

####### pickle & un pickle ##############
df.to_pickle('path/filename.pkl')                                                       # it will create a pickle object which is stored on disk with filenam.pkl and copy it into pen drive/flash drive
df.read_pickle('path/filename.pkl')                                                   # copy the pickle object from flash drive to other machine this stored pickle object can be read.

###### create dummy variables #########
pd.get_dummies(df,columns=['State'],drop_first=True)             # pass the list of categorical variables to list of columns and enable drop_first=True to handle dummy variable trap.

##### convert string object to datetime datatype ################
ufo['Time']=pd.to_datetime(ufo.Time)                                           # ensure this is pandas function, this will convert string to datetime datatype.
ufo.Time.dt.year                                                                                  # applying dt attributes on ; Series.dt can be used to access the values of the series as datetimelike and return several properties.

######### finding duplicates ##############################
ufo.City.duplicated().sum()                                                             # will give the no of duplicated values.
ufo.City.nunique().sum()                                                                 # will give the no of unique values; sum of both will give total record count.
emp[~emp.deptno.duplicated()].head()                                     # duplicated() method returns unique value as false and duplicate as true, so true will display duplicate values so we take inverse

######### map(), apply(), applymap() #########################
ufo.state.map({'blr':'bangalore','hyd':'hyderabad','male':'m'}) # map() is series function 
apply()                                                                                                  # this is applied either to row or column of every element.
applymap()                                                                                          # this is applied to every element of dataframe row wise and column wise.
%timeit
########## plotting in pandas ###############################
iris.plot.line('petal_width','petal_length')                                   # This will just draw the lines joining the data points but won't draw regression line. This is used in timeseries plotting.
iris.plot.bar('species','petal_length')                                             #  plt.bar(iris['species'], iris['petal_length'])
iris.plot.box()                                                                                      # drawing box plot, all the numeric fields will be plotted automatically and categorical will be ignored.
iris.sepal_length.plot.box()                                                             # drawing on single columns; In box plots we dont slice the data we give the whole column.
iris.plot.hist('petal_width',alpha=0.4)                                          # drawing histrogram from pandas df.
iris.plot.scatter('petal_width','petal_length')                             # Drawing scatter plot.
iris.plot.area('species','petal_length')                                           # Area plot by giving x=independent and y=dependent. 
iris.plot.density()                                                                                # kde plotting for all numeric variables.
iris.boxplot(column='sepal_length',by='species')                       # bar will tell the sum of values for the categorical variable, box will tell the percentile of the categories.
ax=iris.plot.box()                                                                                # Creating plot object 
ax.set_xlabel("X-Axis")                                                                      # Set the x-axis label
ax.set_ylabel("Y-Axis")                                                                      # Set the y-axis label

############ numpy #####################
np.reshape(3,3) # This will create 2d matrix from 1d array.
np.ravel()             # flatten the 2d array to 1d.



