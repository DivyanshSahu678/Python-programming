#Day 72

#understand the use of super keyword

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
class Programmer(Employee):
    def __init__(self,name, id,lang):
        super().__init__(name, id)
        self.lang = lang
        
a = Employee("Aman", "101")
b = Programmer("Ram", "101", "Python")
print(a.name)
print(b.name)
print(b.id)
print(b.lang)