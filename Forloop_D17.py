#Day 17 

#loops 

#For loops 

name = "John"
for letter in name:
    print(letter)
    
colors = ["red", "green", "blue"]

for color in colors:
    print(color)

    for i in color:
        print(i)

    if(color == "blue"):
        print("Found the color blue!") 

#range(stop)
        
for a in range(6):
    print(a)

# range(start, stop)

for b in range(2, 6):
    print(b)

# range(start, stop, step)
    
for c in range(2, 10, 2):
    print(c)
    
for d in range(3, 30, 3):
    print(d)