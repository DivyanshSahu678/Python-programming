#Day 55

# Snake Water Gun Game

import random

item = ["Snake", "Water","Gun"]

computer = random.choice(item)
user = input ("Enter your choice (Snake, Water and Gun) : ")
print("Computer choice : ", computer)

if user == computer:
    print("Match Tied")
elif user == "snake":
    if computer == "Water":
        print("You win")
    else:
        print("You lose")
        
elif user == "Gun":
    if computer =="snake":
        print("You win")
    else:
        print("You lose")
    
elif user == "Water":
    if computer == "gun":
        print("You win")
    else:
        print("You lose")
