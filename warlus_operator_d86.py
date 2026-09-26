#Day 86

#understand the concept of walrus operator in python

# no = [1,2,3,4,5]

# while( n := len(no)) > 0:
#     print(no.pop()) 
    
happy = False
print(happy)

print(happy := True)

foods= list()

# while True:
#     food = input("Enter the food name: ")
#     if food == "quit":
#         break
#     foods.append(food)

# print(foods)

while(food := input("Enter the food name: ")) != "quit":
    foods.append(food)