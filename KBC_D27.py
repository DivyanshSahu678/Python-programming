print("===================================")
print("      WELCOME TO KBC GAME")
print("===================================")

questions = [
    ["Q1. What is the capital of India?",
     "A. Mumbai", "B. New Delhi", "C. Chennai", "D. Kolkata", "B", 1000],

    ["Q2. Which planet is known as the Red Planet?",
     "A. Earth", "B. Venus", "C. Mars", "D. Jupiter", "C", 5000],

    ["Q3. Who is known as the Father of Computer?",
     "A. Charles Babbage", "B. Newton", "C. Einstein", "D. Bill Gates", "A", 10000],

    ["Q4. Which is the largest ocean in the world?",
     "A. Indian Ocean", "B. Atlantic Ocean", "C. Pacific Ocean", "D. Arctic Ocean", "C", 50000],

    ["Q5. Which language is used for Artificial Intelligence and Data Science the most?",
     "A. Python", "B. Java", "C. C", "D. HTML", "A", 100000]
]

amount = 0

for q in questions:
    print("\n-----------------------------------")
    print(q[0])
    print(q[1])
    print(q[2])
    print(q[3])
    print(q[4])

    ans = input("Enter your answer (A/B/C/D): ").upper()

    if ans == q[5]:
        amount = q[6]
        print(" Correct Answer!")
        print("You have won ₹", amount)
    else:
        print(" Wrong Answer!")
        print("Correct Answer is:", q[5])
        break

print("\n===================================")
print("        GAME OVER")
print("===================================")
print("Total Amount Won = ₹", amount)
print("Thank You for Playing KBC!")