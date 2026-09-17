#Day 59

#Understanding the concept of decorators in python

#Decorators are a very powerful and useful tool in Python since it allows programmers to modify the behavior of function or class.

def greet(fx):
    def mfx():
        print("Good morning")
        fx()
    return mfx

@greet
def hello():
    print("Hello World")
    
hello()