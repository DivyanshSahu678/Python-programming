#day 14

#if else statement  

a = int(input("Enter a number: "))
print("The number is " + str(a))
if a > 5:
    print("a is greater than 5")
else:
    print("a is not greater than 5")
 
# example 
    
b = int(input("enter no : "))
print("the no is : " + str(b))

if b > 18:
    print("You can vote ")
else:
    print("You cannot vote")  

#Conditional operators

c = int(input(" C = "))
print(c>18)
print(c<=18)
print(c!=18)
print(c==18) 

#if else ladder elif statement

num = int(input("Enter a number: "))    
if (num < 0):
    print("Negative number")
elif (num == 0):
    print("Zero")
elif(num == 999):
    print("three digit greater no ")

else:    
    print("Positive number")
    
#nested if else statement

num = int(input("Enter a number: "))

if (num<0):
    print("Negative number")

elif(num >0):

    if(num <= 10):
        print("The number is between 1 to 10")

    elif(num > 10 and num <= 20):
        print("The number is between 11 to 20")

    else:
        print("The number is greater than 20")

else:
    print("The number is zero")


    
      