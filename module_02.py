""""
Description: Module02 demostration
Author: jasleen Kaur 
Date: 2024-01-22
Usage: To demonstrate conent for module 02 
"""""

#This is single line comment

"""

This would be a multi line comment.
it can spam multiple lines.
"""

# Basic Function
absolute_value = abs(-12)
print('absolute value:', absolute_value)

print('absolute value:', abs(-99))

# Print Function
print("I am" , absolute_value, "years old.")
print("I m 20 years old.")

print("apples","oranges","bananas",sep=",")

# Print using f-string
name = "john"
age = 25
print(f"My name is {name} and I am {age} years old.")

value = 3.14159
print(f"The value is {value: .3f}.")

number = 123
print(f"The value is {number:05}.")

print(f"hello, {name:>10}.")

print("Hello\tworld.\n\nHello \'World.\'")