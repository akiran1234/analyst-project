# modules
# json, csv, logging, datetime, os, sys,random,

# pickling is the process of writing the state of an object to file and writing back from file to object is un pickiling.
# import pickle;


print(format(12, "08b")) # creating whole number to binary, 08b leading zero and total length 8.
print(int('1111',2))     # creating binary number to whole number.
print(abs.__doc__)       # doc string used against a function to get the info.
########################################################################################
# n+nn+nnn
n=3 # int(input("enter the value of n\n"))

n1="{0}".format(n)
n2="{0}{0}".format(n)
n3="{0}{0}{0}".format(n)
print("{0}+{1}+{2}".format(n1,n2,n3))
########################################################################################
import calendar
print(calendar.month(2018,8))        # Displaying calander
########################################################################################
import datetime                      # Caliculate the no of days between two dates.
print(datetime.date(2018,1,31)-datetime.date(2018,12,31))
########################################################################################
def personal_details():
    name, age = "Simon", 19
    address = "Bangalore, Karnataka, India"
    print("Name: {}\nAge: {}\nAddress: {}".format(name, age, address))

personal_details()
########################################################################################
import os.path
open('abc.txt', 'w')
print(os.path.isfile('abc.txt'))
########################################################################################
import platform
import os
print(os.name)
print(platform.system())
print(platform.release())
########################################################################################
import os
os.system('ping 8.8.8.8')
########################################################################################
import os
print(os.environ)  # To print the environmental variables of os from python
########################################################################################
import getpass
print(getpass.getuser())
########################################################################################
