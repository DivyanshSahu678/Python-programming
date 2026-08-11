#Day 53

#Use of Map, filter and reduce

#map

def cube(x):
    return x*x*x

print(cube(2))

l = [1, 2, 4, 6, 8]

newl = list(map(cube, l))
print(newl)

# #filter

def filter_function(a):
    return a>4
newnewl = list(filter(filter_function, l))
print(newnewl)

#reduce

from functools import reduce

numbers = [1, 2, 3, 4, 5]

sum = reduce(lambda x, y : x+y, numbers)

print(sum)