#Day 49

#file I/O in python

#open method used to open a file
#r- read mode w- write mode a- append mode
#r mode is default mode

f = open("myfile.txt", "r")
text = f.read()
print(text)
f.close()

#using w mode we can create file also
f = open("myfile.txt", "w")
f.write("Hello, World!")
f.close()

#using a mode we can append text to a file
f = open("myfile.txt", "a")
f.write("Hello, World!")
f.close()

with open ("myfile.txt", "a") as f:
    f.write("Hello, World!")