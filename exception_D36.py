#Day 36 

#exception handling in python

a = input("Enter the num :")
print(f"Multiplication table of {a} is :")

try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except :
    print("Invalid Input, Please enter a valid number")
    
print("Program completed successfully")

try :
    num = int(input("Enter a number : "))
    a = [6, 3]
    print(a[num])
    
except ValueError:
    print("Invalid Input, Please enter a valid number")
except IndexError:
    print("Index out of range, Please enter a valid index")