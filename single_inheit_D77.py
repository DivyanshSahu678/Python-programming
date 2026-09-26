#Day 77

#understand the concept of inheritance in python

class Parent:
    def __init__(self,name):
        self.name= name
        
    def show(self):
        print(f"name: {self.name}")
        
class Child(Parent):
    def __init__(self,age):
        self.age = age
        
    def show(self):
        print(f"age: {self.age}")
        
a = Parent("Aman")
b = Child(20)
a.show()
b.show()


 
    