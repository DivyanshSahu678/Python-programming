#day 30 of 100

#Recursion in python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Enter a number to find its factorial: "))
print(factorial(n))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter a number to find its Fibonacci: "))
print(fibonacci(n))
