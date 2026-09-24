#Day 61 
# Understand the concept of inheritance

class Parent:
    def __init__(self,name):
        self.name = name
        
    def showDetails(self):
        print("Father's Name:",self.name)
        
class Son(Parent):
    def sonname(self,name):
        print("Son's Name:",name)
e1 = Parent('John')
e1.showDetails()
e2 = Son('Mike')
e2.sonname('Mike')