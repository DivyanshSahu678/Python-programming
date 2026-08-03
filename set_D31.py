# day 31 

#set in python 

s = {2, 4, 6 ,2}
print(s) # {2, 4, 6} - duplicates are removed

#unordered collection of unique elements

info = {"aman", 19 , False , 9.8 , 19}
print(info)

abc = {}
print(type(abc)) # <class 'dict'> - empty dictionary 

abcd = set()
print(type(abcd)) # <class 'set'> - empty set

for value in info:
    print(value)