#Day 54

#is vs ==

#is compares at exact location of value
#== compares the value

a = 4
b = "4"

print(a is b) #exact location of object in memory out - false
print(a == b)#value  out- false

a = [1, 2, 43]
b = [1, 2 ,43]

print( a is b) #false becuz not at same loc
print (a == b) # true becuz same value

a = 3
b = 3

print(a is b) # true becuz at same loc
print(a == b) #true becuz same value