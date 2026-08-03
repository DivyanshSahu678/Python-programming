#Day 32 

#Set methods in python 

s1 = {1, 2, 3, 4, 5}
s2 = {3, 6 ,7}
print(s1.union(s2))

s3 = s1.intersection(s2)
print(s3)

s4 = s1.symmetric_difference(s2)
print(s4)

s5 = s1.difference(s2)
print(s5)

#set methods

cities = { "tokyo", "delhi", "london", "paris"}
cities2 = { "new york", "bombay", "sydney", "rome"}
print(cities.isdisjoint(cities2)) # True - no common elements

cities = { "tokyo", "delhi", "london", "paris"}
cities2 = { "new york", "bombay", "sydney", "rome"}
print(cities.issuperset(cities2))

cities = { "tokyo", "delhi", "london", "paris"}
cities2 = { "new york", "bombay", "sydney", "rome"}
print(cities.issubset(cities2))

cities.add("berlin") # add one item in set
print(cities)

cities.update(["mumbai", "chicago", "beijing"]) # add multiple items in set
print(cities)

cities.remove("delhi") # remove an item from set
print(cities)

cities.discard("mumbai") 
print(cities)

cities.pop() # remove a random item from set
print(cities)

del cities2 # delete the set
# print(cities2) # NameError: name 'cities2' is not defined

if "tokyo" in cities:
    print("Tokyo is present in the set")
else:
    print("Tokyo is not present in the set")