# Day 22 of 100

#Introduction to Lists

l = [1, 2, 3, 4, 5, "harry"]  #List of integers can store any type of data
print(l)            #basic list

print(l[0])
print(l[1])
print(l[2])
print(l[3])
print(l[4])

#convert of negative index to positive index #this all shows same element
print(l[-1])  #last element
print(l[len(l)-1])  #last element
print(l[6-1])  #last element

if 5 in l:  #check if element is present in list
    print("Yes 5 is present in list")
else:
    print("No 5 is not present in list")

#list comprehension

li = [i for i in range(5)]  #list of integers from 0 to 4
print(li)