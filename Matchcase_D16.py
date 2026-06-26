# Day 16

#match case statements

b = int(input("Enter a number below 10: "))

match b:
    
    case 1:
        print("X is 1")
        
    case 2:
        print("X is 2")
    
    case 3:
        print("X is 3")
        
    case _ if b > 2:
        print(str(b) + " is greater than 2")
        