# Day 25 of 100

# operations on tuples

#conversion of list into tuple

countries = ['India', 'USA', 'UK', 'Australia', 'Canada']  # list of countries
temp =list(countries)  # converting list into tuple
temp.append('Germany')  # adding an element to the list 
temp.pop(3)  # removing an element from the list
temp[2] = 'France'  # changing an element in the list
countries = tuple(temp)  # converting list back into tuple

print(countries)  # Output: ('India', 'USA', 'France', 'Canada', 'Germany')

#methods of tuple

#count() method returns the number of occurrences of an element in the tuple
tup = (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)  # Tuple of integers
print(tup.count(3))  # Output: 2

#index() method returns the index of the first occurrence of an element in the tuple
print(tup.index(4))  # Output: 3

#len() method returns the number of elements in the tuple
print(len(tup))  # Output: 10



