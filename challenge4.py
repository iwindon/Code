from cmath import sqrt
from unittest import result

def squarenumber(num):
    """
    Takes a number and runs the square root function agianst it
    """
    return sqrt(num)
    
print(squarenumber(5))

def sqrtnum(num):
    """
    Takes a number and returns the sqare of the number.
    """
    return num ** 2

print(sqrtnum(5))

def letters(x):
    """
    Takes a string of characters and prints them out.
    """
    print(x)

letters("hello")

def options(req1, req2, req3, op1=5, op2=2):
    """
    Function that takes 3 required values, with two optional.
    """
    return req1 + req2 + req3 + op1 + op2

print(options(5,2,3))
print(options(5,3,2,8,3))

def firstfunc(num1):
    """
    Takes a number and divides it by 2
    """
    return num1 / 2

def secondfunc(num1):
    """
    Takes a number and multiples it by 4
    """
    return num1 * 4

result1 = firstfunc(5)
print(result1)
print(secondfunc(result1))

def converter(string):
    """
    Takes a string and if it is a number converts it to a float, otherwise it prints an error.
    """
    try:
        return float(string)
    except ValueError:
        print("Could not conver the string to a float")

print(converter("10.2"))
