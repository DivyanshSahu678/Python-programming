#Day 20 

#Functions in python

def calculate_Gmean(a, b): #Function that can be used many times when we needed
    mean = (a*b)/(a+b)
    print(mean)
    
def isgreater(a, b):
    if(a > b):
        print("c is greater than d")
    else:
        print("d is greater than or equal to c")

a = 9
b = 8
calculate_Gmean(a, b)

c = 10
d = 4
isgreater(c, d)
