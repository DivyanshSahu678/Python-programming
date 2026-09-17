#Day 60

#Understanding the concept of getter and setter in python

class MyClass:
    def __init__(self, value):
        self._value = value
        
    def show(self):
        print(f"The value is: {self._value}")

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
        
obj = MyClass(10)
obj.show()  # Output: The value is: 10
print(obj.value)  # Output: 10
obj.value = 20
obj.show()  # Output: The value is: 20