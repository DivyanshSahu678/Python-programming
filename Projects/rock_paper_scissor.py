import random 

item = ["rock", "paper", "scissors"]

computer = random.choice(item)
user = input("Enter your choice (rock, paper, scissors): ")
print("Computer chose: ", computer)

if user == computer:
    print("It's a tie!")
elif user == "rock":
    if computer == "scissors":
        print("you win!")
    else:
        print("you lose!")
elif user == "paper":
    if computer == "rock":
        print("you win!")
    else:
        print("you lose!")
elif user == "scissors":
    if computer == "paper":
        print("you win!")
    else :
        print("you lose!")