#Day 58

#Understanding the concept of constructor in python

# def __init__(self): keyword used to create a construtor

class Person:
    
    def __init__ (self, n, o):
        print("This is a constructor")
        self.name = n
        self.occ = o
        
    def info(self):
        print(f"{self.name} is a {self.occ}")
        
a = Person("John", "Engineer")
b = Person("Mike", "Doctor")
a.info()
b.info()