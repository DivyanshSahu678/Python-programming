#Day 76

#understand the concept of operator overloading in python

class Vector:
    def __init__(self, i, j ,k):
        self.i = i
        self.j = j
        self.k = k
        
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
v= Vector(1,2,3)
print(v)
v2 = Vector(4,5,6)
print(v+v2)