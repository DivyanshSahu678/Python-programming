#day 38

#raise custom error:- we can raise our own error using raise keyword.

x = int(input("Enter a number between 5 and 9 : "))
if x < 5 or x > 9:
    raise ValueError("Number should be between 5 and 9")