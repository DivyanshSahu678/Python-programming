#Day 50

#File handling methods in python

#readline() method:- it will read the first line of the file and return it as a string.

f = open ("myfile.txt" , "r")
while True:
    line = f.readline()
    print(line)
    if not line:
        print(line, type(line))
        break
    
    