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

current_salary = 67293.23
is_employed = True

print(type(name))
print(type(age))
print(type(current_salary))
print(type(is_employed))

age_and_salary = age + current_salary
print(age_and_salary)
print(type(age_and_salary))

print(float(age))
print(int(current_salary))

# Strings
original_string = "hello, world!"
print(original_string)
original_string = original_string.capitalize()
print(original_string)

width = 20
fill_char = '-'
centered_string = original_string.center(width, fill_char)
print(centered_string)

uppercase = original_string.upper() 
print(uppercase)

# Standard Operators
# +
result = 5 + 5
print(result)

# -
result = 5 - 5
print(result)

# *
result = 5 * 5
print(result)

# / division
result = 5 / 5
print(result)

# // florr division or integer division
result = 42 / 4
print(result)

# % modulus - remainder
result = 100 % 5
print(result)

# ** power
result = 2 ** 4

age = 25
age = age + 1
print (age)

age += 1
print(age)

result = ( (10 + 5) * 2) / 3 - 1
print(result) = 9.0