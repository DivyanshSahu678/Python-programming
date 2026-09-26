#Day 69

#understand the concept of class methods in python

class Employee:
    company = "Google"
        
    def show(self):
        print(f"Name: {self.name}, Salary: {self.salary}, Company: {self.company}")
        
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company
        
e1 = Employee()
e1.name="Aman"
e1.salary= 10000
e1.show()
e1.change_company("Microsoft")
e1.show()
print(Employee.company)

