handle = open("test.txt","r") #open the file in read only mode

data = handle.read()  #read the file 
print(data)

handle.close #close the file

#Reading only a single line
handle = open("test.txt","r")

data = handle.readline() #readline method for reading only a single line
print(data)

handle.close()

#Reading multiplelines
handle = open("test.txt","r")

data = handle.readlines() #readlines method for reading many lines
print(data)

handle.close()

#Looping through a file
#Finding how many times the word Python has been used in the file
handle = open("test.txt","r")

data = handle.read()
counter = 0
for word in data.split(): #split method transforms the data into a list of words
    if word == "Python":
        counter +=1

print(counter)

with open("test.txt","r") as handle:
    data = handle.read()
    print(data)
    
