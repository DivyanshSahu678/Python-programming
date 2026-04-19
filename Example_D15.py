#Day 15 

# Example Question : 

#WAP for display greet msg according to the time which is taken as input from the user.

hour = int(input("Enter the hour : "))
minute = int(input("Enter the minute : "))

if hour < 0 or hour > 23 or minute < 0 or minute > 59:
    print("Invalid time")
else:
    if hour < 12:
        print("Good Morning")
    elif hour < 17:
        print("Good Afternoon")
    elif hour < 21:
        print("Good Evening")
    else:
        print("Good Night")
