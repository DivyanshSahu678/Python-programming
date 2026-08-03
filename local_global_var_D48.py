#Day 48

#Global and local variable in python

x = 4       #global variable
print(x)

def hello():
    x = 5
    print(f"The local x is {x}") #local variable
    print(x)
print(f"The global x is {x}") 
hello()
print(f"the global x is {x}")