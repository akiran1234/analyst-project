with open('C:/Users/PBR/Desktop/Datasets/fileops.txt','w') as f:
    f.write("This is first Line\n")
    f.write("This is second Line\n")
    f.write("This is third Line\n")
    f.write("This is fourth Line\n")
    f.write("This is 5th Line\n")
    f.write("This is 6th Line\n")

with open('C:/Users/PBR/Desktop/Datasets/fileops.txt','r') as f1:
    print(f1.read())           # Reading the whole file at a time.

with open('C:/Users/PBR/Desktop/Datasets/fileops.txt','r') as f1:
    count=0
    for line in f1:            # Reading the file using for loop.
        print(line,count)
        count+=1

print("Total no of lines in file",count)
