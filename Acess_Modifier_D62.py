#day 62

#understading access modifiers in python

#public

class A:
    def __init__(self):
        self.name = "A"

a = A()   
print(a.name)

#Private use __ to make it private

#how to access :- print(obj name._class name__private variable name)

class B:
    def __init__(self):
        self.__name = "B"
        
a = B()
print(a._B__name)


# Protected use _ to make it protected

class c:
    def __init__(self):
        self._name = "C"
        
a = c()
print(a._name)
