#day 51

#more func in python

#seek func() and tell() func() in python

with open("myfile.txt" , "r") as f:
    print(type(f))

    f.seek(5)
    
    print(f.tell())
    data = f.read(5)
    print(data)
