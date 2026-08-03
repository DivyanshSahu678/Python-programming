#day 37

#Finally Keyword:- always executes the code block, whether an exception is raised or not.

try:
    l = [1, 5, 3, 6]
    i = int(input("enter the index : "))
    print(l[i])
except :
    print("Invalid Input, Please enter a valid index")
    
finally:
    print("Program completed successfully")