#day 79

#understand the concept of multiple inheritance in python

class Employee:
    def __init__(self, name):
        self.name = name

class Dancer:
    def __init__(self, dance):
        self.dance = dance

class DancerEmployee(Employee, Dancer):
    def __init__(self,name, dance):
        self.dance = dance
        self.name = name
        
a= DancerEmployee("Aman", "Hip Hop")
print(a.name)
print(a.dance)
    