#Day 57

#Understanding the concept of Class and Object in OOP

class Person:
    name = "John"
    occupation = "Engineer"
    networth = "10L"
    
    def info(self): #Self is a reference to the current instance of the class
        print(f"{self.name} is a {self.occupation}")
        
a = Person()
a.info()