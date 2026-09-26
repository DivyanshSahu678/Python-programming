#Day 80

#understand the concept of multilevel inheritance in python

class Vehicle:
    def __init__(self, brand):
        self.brand = brand
        
    def general_info(self):
        return f"This is a transportation vehicle made by {self.brand}."

# Car inherits from Vehicle
class Car(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand) # Passes brand to Vehicle
        self.model = model
        
    def specific_info(self):
        return f"It is a {self.brand} {self.model}."

# ElectricCar inherits from Car
class ElectricCar(Car):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model) # Passes brand and model to Car
        self.battery_capacity = battery_capacity
        
    def battery_info(self):
        return f"It has a {self.battery_capacity} kWh battery."

# Creating an instance of the bottom-level class
my_ev = ElectricCar("Tesla", "Model 3", 75)

# Accessing methods across all three tiers
print(my_ev.general_info())   # Inherited from Grandparent (Vehicle)
print(my_ev.specific_info())  # Inherited from Parent (Car)
print(my_ev.battery_info())   # Defined in Child (ElectricCar)
