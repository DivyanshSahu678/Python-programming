#Day 34

#methods in dictionary
#dict is in ordered form

#update method

ep1 = {122 : 45 , 123 : 67 , 124 : 89 , 125 : 90}
ep2 = {126 : 78 , 127 : 56 , 128 : 34 , 129 : 12}

ep1.update(ep2)
print(ep1)

#clear method

ep2.clear()
print(ep2)

#pop method

ep1.pop(122) #popitem used to delete last item in dictionary
print(ep1)

#del method :-  delete whole dictionary

