#Day 71

#Dict, dir methods in python

# x=[1,2,3]
# print(dir(x))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
a = Person("Aman", 20)
print(a.__dict__)
    