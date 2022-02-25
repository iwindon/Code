# Python Chapter 3 Challenges
# Author: Ivan Windon
# Date: 02/25/2022

# Print three different strings

print("This is challenge #1")
print("Hello World!")
print("My name is Ivan")
print("I'm learning programming")

# Write a program that prints a message if a variable is less tha n10, and different message if 
# the variable is greater than or equal to 10

print("\nThis is challenge #2")
x = 8

if x < 10:
    print("This message prints because the value is less than 10")
else:
    print("This message prints because the value is greater than 10")

# Write a program that prints a message if a varable is less than or equal to 10, another message if the 
# variable is greater than 10 but less than or equal to 25, and another message if the variable is 
# greater than 25.

print("\nThis is challenge #3")
y = 9

if y <= 10:
    print("This message prints because the value y is less or equal to 10")
elif y > 10 and y <= 25:
    print("This line prints if y is greater than 10 and equal or less than 25")
else:
    print("This line prints if y is greater than 25")

# Create a program that divides two varaibles and prints the remainder.

print("\nThis is challenge #4")
num1 = 23
num2 = 456
print(num1 % num2)

# Create a program that takes two variables, divides them, and prints the quatient.

print("\nThis is challenge #5")
print(num1 // num2)

# Write a program with a variable age assigned to an integer that prints different strings depending on
# what integer age is.

print("\nThis is challenge #6")
age = 49
if age <= 19:
    print("You are young.")
elif age > 20 and age <= 40:
    print("You are in the prime of life now, enjoy it!")
else:
    print("You are wise, be sure to teach others what you have learned.")