import csv

with open("C:/Users/PBR/Desktop/Datasets/OfficeSupplies.csv",'r') as file: # Creating file object
    reader=csv.reader(file)   # using reader function to create reader object by passing file object as parameter.
    for line in reader:       # the out come is a list.
        print(line)



# writer code
import os
os.getcwd()

