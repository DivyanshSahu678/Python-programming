#Day 19

#Break and Continue

#Break statement 

for i in range(11):
    print("5*" + str(i) + " =", 5 * i)
    if i == 10:
        break

#continue statement

for i in {1, 2, 3, 4, 5}:
    if i == 3:
        continue
    print(i)
