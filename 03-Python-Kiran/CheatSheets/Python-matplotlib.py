##################### matplotlib ########################
# plotting can be done in two ways 1.Functional Approch 2. Object Oriented Approch.
# The below is a functional approch calling the functions directly from pyplot module.
import matplotlib.pyplot as plt          # matplotlib is a package/library and pyplot is a module and plt() is a function for plotting the graphs.

days=[1,2,3,4,5,6,7]                              # days of the week
max_t=[50,51,52,48,47,49,46]          #  max temp
min_t=[43,42,40,44,33,35,37]           #  min  temp
avg_t=[45,48,48,46,40,42,41]            # avg temp

plt.plot(days,max_t)                               # plot() is a function belongs to pyplot module. pass x,y values for plotting; x = independent variable and y= dependent variable.
plt.plot()                                                   # is a plotting function which will draw a lines meeting all the data points or given pattern symbols . This will not draw regression line for that use sns.lm()
# plotting with more options linestyle, linewidth, color  and search for plot function in matplot lib website it will show all the available arguments that plot functions uses.
plt.plot(days,max_t,linestyle='--',linewidth=2,color='g',alpha=0.5)   # alpha is the thickness of the color ranges from (0.1 to 1.0)
plt.plot(days,max_t,'g--')                      # This is a shortcut for linestyle and line color

                                                                 # To see the difference draw the plot by taking data set with small points and many points.
x=[1,2,3,4,5,6,7]                                 # days of the week
max_t=[50,51,52,48,47,49,46]         # reading for each day.
iris=sns.load_dataset("iris")
plt.plot(iris['sepal_length'], iris['sepal_width'])      # drawing with more datapoints to see the difference. by default it will draw line if we don't supply any markers.

# giving Label and Title to the plot
plt.xlabel("Time")                                   # Draw label to x-axis
plt.ylabel("Distance")                            # Draw lable to y-axis
plt.title("Graph Drawing")                   # Draw title to graph  this is not working check.
plt.plot(days,temp)                               # now plot and a line will be drawn meeting all the data points.

# plotting multiple lines on the same graphs (x is same with different y values)
plt.plot(days,max_t,label='max')       # This label property will be shown in the legend giving the name to line.
plt.plot(days,min_t,label='min')     
plt.plot(days,avg_t,label='avg')          
plt.legend()
plt.grid()                                                  # enable grid in the plotting canvas

######################  Bar Chart, Side by Side Bar Chart, Stacked Bar Chart ######################################
plt.bar(df['Region'],df['Unit Price'],width=0.4,color='blue')            # width ranges from (0.1 To 1.0)

Try Side by Side Bar Chart check in seaborn.
####################### Histogram #########################################################
# Histogram plots frequency of continious variable of each bucket. bins/buckets will have always equal size and each bin tells the frequency of values in a bucket.
his=np.random.randint(0,80,size=30)                # It will generate 30 random numbers b/w 10-90.
plt.hist(his,bins=4,color='w',edgecolor='r')       # It will divide the random numbers into 4 buckets and plot the frequency of each bucket on graph.

###################### Box Plot ########################################
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
df.plot.box(grid=True)

##################### Scatter Plot #####################################
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
df.plot.scatter(x='a', y='b')

######### drawing dual/ multi axis chart  ########################
days=[1,2,3,4,5,6,7]                              # days of the week
max_t=[50,51,52,48,47,49,46]          #  max temp
min_t=[43,42,40,44,33,35,37]           #  min  temp
avg_t=[45,48,48,46,40,42,41]            # avg temp

# executing plot commands one after the other will result in dual axis / multi axis charts.
plt.plot(days,min_t,label='min')           # drawing plot with 1st-Axis; label property will enable legend.
plt.plot(days,max_t,label='max')         # drawing plot with 2nd-Axis
plt.plot(days,avg_t,label='avg')            # drawing plot with 3rd-Axis

# setting properties to plotting
plt.xlabel('X-Axis')
plt.ylabel('Y-Label')
plt.title('Test Title')

# Drawing subplots in functional style 
x=[1,2,3,4,5,6,7]                                    # days of the week
max_t=[50,51,52,48,47,49,46]          #  max temp
min_t=[43,42,40,44,33,35,37]           #  min  temp
avg_t=[45,48,48,46,40,42,41]            # avg temp

plt.subplot(2,1,1)                                   # First Arg=2 means 2 rows, Second Arg=1 means one column and Third Arg=1 means first diagram.
plt.plot(x,max_t)                                     # This is the plot function of 1st diagram which should be followed by subplot() function.
plt.subplot(2,1,2)
plt.plot(x,max_t)

############################### seaborn ############################
# we can load seaborn datasets from the following github link - https://github.com/mwaskom/seaborn-data
# seaborn is more versatile which is build on top of matplotlib and has more control of plotting than matplotlib.
# Using seaborn we can write one line of code for plotting unlike writing multiple lines of code in matplotlib.
# Refer --> https://seaborn.pydata.org/api.html
############ distribution plots (univariate & bi variate plots) ##############
sns.distplot()   # univariate analysis one variable
sns.jointplot() # bivariate analysis  two variables kind=reg, hex will highlight the densed data points and rest in fadded manner. kind=kde 
sns.pairplot()
sns.rugplot()
sns.kdeplot()

########### categorical plots  ##############
barplot() # estimator is mean , hue for stacked bar chart
countplot() 
boxplot() # x,y can be passed compare with plt.box() 
violinplot()
stripplot()
swarmplot()

######### Matrix Plots ###############
load flights data.
check pivot_table()
# for matrix plots the data frame should have index with column name and header with column name so pivot_table is used.
heatmap()
clustermap()
######### Regression Plots ########
lmplot()

import seaborn as sns
tips=sns.load_dataset('tips')     # using this function we can load built in seaborn data sets. Data set name has to be passed with out extension and a data frame object will be created.
########### Categorical Plotting ################
########### bar graph ###############
sns.barplot(x='sex',y='total_bill',data=tips)   # x is the independent variable and y is the dependent variable by default it will show the mean value in plotting.
sns.barplot(x='sex',y='total_bill',data=tips,estimator=np.sum) # To see the sum of values for each category pass the estimator parameter as np.sum function.

######### sort the data set before plotting to see the plotting in sorted order ################
tips=sns.load_dataset('tips').sort_values('tip',ascending=True)
sns.barplot(x='day',y='tip',data=tips,rug=True)

# Creating labels for the plot
p=sns.barplot(x='day',y='tip',data=tips,estimator=sum,hue='sex')  # creating plot object.
p.set_title("Day wise Tips")
p.set_xlabel("Week of the Day")
p.set_ylabel("Sum of Tips")

########## side by side bar graph using hue parameter #########
sns.barplot(x='day',y='total_bill',data=tips,estimator=np.sum,hue='sex')           # by using hue parameter we can compare side by side.
sns.barplot(x='day',y='tip',data=tips,estimator=sum,hue='sex',palette='cool')  # by passing palette parameter color can be set.

########## ploting horizontal bar graph  #####################
sns.barplot(x='tip',y='day',data=tips)    # To plot horizontal bar graph take independent variable on y-axis and dependent variable on x-axis.

########### rugplot ######################################
sns.rugplot(tips['total_bill'],height=0.5)      # rugplot takes only one variable and tells where the most of the data point lies from min to max scale. height= line height.

########## boxplot #######################################
# most of the properties will be same for all the plot methods.
sns.boxplot(x='day',y='tip',data=tips,hue='sex',order=['Sun','Fri','Sat','Thur'],hue_order=['Female','Male']) # We can order the x variable by passing order parameter and we can control the hue_order by passing hue_order parameter.
sns.boxplot(x='tip',y='day',data=tips,orient='horizontal')   # plotting horizontal.
sns.boxplot(data=tips,orient='horizontal')                              # pass the whole data set and set orient=horizontal for horizontal plotting.

########## countplot #####################################
# count plot will count the no of occurances in each category of a categorical variable.
sns.countplot(tips['sex'])           # draw the plot how many male and female in sex variable.    select count(*),sex from table tips by sex

########### strip plot #####################################
sns.stripplot(x='time',y='tip',data=tips)
sns.stripplot(x='time',y='tip',data=tips,hue='sex',jitter=0.1,dodge=True)  #  pass jitter and dodge parameter for more insights.

############# violin plot ###################################
sns.violinplot(x='day',y='tip',data=tips,hue='sex',split=True)
sns.violinplot(x='day',y='tip',data=tips,hue='sex',split=True,inner='quartile')  # will display quartile

##########  Distribution plots ###############################
# distplot()                   # This is a univariate function i.e it will show the distribution only for a single variable.
sns.distplot(tips['total_bill'],bins=10,rug=True)             # This will plot the distribution by drawing the histogram.

# jointplot() is a bivariate function i.e it will use two variables for plotting.
sns.jointplot(x='total_bill',y='tip',data=tips)                     # by default it will plot scatter plot
sns.jointplot(x='total_bill',y='tip',data=tips,kind='reg')  # passing argument kind='reg', it will draw a regression line. other values for kind=('reg','hex','kde')

# pairplot() will draws the relations between all the numeric variables of the datasets and correlation can be identified.
sns.pairplot(tips,hue='sex',kind='scatter')                        # This will plot the relation b/w all the numeric variables. Diagonal above and below are exact mirror images.
# If no of variable n is huge, like n=500 then dimensionality reduction and PCA (principal component analysis) will help in identifing the relationship b/w variables.

########## linear model plot ###############################
sns.lmplot(x='total_bill',y='tip',data=tips)
sns.lmplot(x='total_bill',y='tip',data=tips,hue='sex')

######### Matrix Plot ####################################
# get familarity with pivot() and pivot_table() in pandas
flight_pivot=pd.pivot_table(flights,index='month',columns='year',values='passengers') # using pivot_table we are creating index so that it will become matrix i.e row and column has identifiers.

# To display heatmap the dataframe should be converted to matrix meaning every cell can referenced from row label and column label.
sns.heatmap(flight_pivot,linecolor='white',linewidths=1)  # linecolor will seperate the boxes with white color and linewidth is the width b/w boxes.

# cluster map will plot the graph based on rows and columns of similar values.
sns.clustermap(flight_pivot)
sns.clustermap(flight_pivot,cmap='coolwarm')

######## Grid Plot  ##########################################
PairGrid
FacetGrid
######## drawing sub plots in sea born ##########################
f, axes = plt.subplots(1, 2)
sns.boxplot(  y="b", x= "a", data=df,  orient='v' , ax=axes[0])
sns.boxplot(  y="c", x= "a", data=df,  orient='v' , ax=axes[1])
plt.tight_layout() # avoid the overlapping of sub plots.



