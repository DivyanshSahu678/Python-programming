#Day 23 of 100

#List Methods

l=[1, 2, 3, 4, 5]  #List of integers can store any type of data

#append() method adds an element at the end of the list
l.append(6)  #append 6 at the end of the list

#sort() method sorts the list in ascending order
l.sort()  #sort the list in ascending order

#sort(reverse=True) method sorts the list in descending order
l.sort(reverse=True)  #sort the list in descending order

#reverse() method reverses the list
l.reverse()  #reverse the list

#index() method returns the index of the first occurrence of an element in the list
print(l.index(3))  #returns the index of the first occurrence of 3 in the list

#count() method returns the number of occurrences of an element in the list
print(l.count(3))  #returns the number of occurrences of 3 in the list

#copy() method returns a shallow copy of the list
l2 = l.copy()  #returns a shallow copy of the list

#insert() method inserts an element at a specified index in the list
l.insert(2, 10)  #inserts 10 at index 2 in the list

#extend() method adds all the elements of an iterable (list, tuple, set, etc.) to the end of the list
l.extend([7, 8, 9])  #adds all the elements of the iterable [7, 8, 9] to the end of the list

