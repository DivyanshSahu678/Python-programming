#Day 91

#understand the concept of generators in python

def my_generator():
    for i in range(50):
        yield i
        
gen = my_generator()
# print(next(gen))

for j in gen:
    print(j)