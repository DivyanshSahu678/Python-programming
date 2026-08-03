#Day 42

# Enumrate function in python

marks = [12, 56, 45, 53, 98 , 43, 53]
index = 0
for mark in marks:
    print(mark)
    if (index == 4):
        print("Awesome")
    index = index +1

# Using enumerate function
marks = [12, 56, 45, 53, 98 , 43, 53]
for index, mark in enumerate(marks, start = 1):
    print(mark)
    if (index == 4):
        print("Awesome")