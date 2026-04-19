# Day 16

#match case statements

a = int(input("Enter a number: "))

match a:
    
    case 1:
        print("X is 1")
    
    case 2:
        print("X is 2")
    
    case 3:
        print("X is 3")
        
    case _ if a > 2:
        print(str(a) + " is greater than 2")
        