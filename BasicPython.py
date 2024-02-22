# Using variables to store values
# x = 10
# y = 20
# result = x + y
# print(result)  # Output: 30

# -----------------------------------------------------------------------------------

# Dynamic Typing

# Python variables don't require explicit type declarations.
# Their type is determined by the value assigned.
# This provides flexibility but can sometimes lead to errors if you're not careful.

# x = 5  # Integer
# x = "Hello"  # String
# x = 3.14  # Float
# x = [1, 2, 3]  # List
# x = {'name': 'Alice', 'age': 30}  # Dictionary

# -----------------------------------------------------------------------------------

# Python Math

# Basic arithmetic operators (+, -, *, /, **) and order of operations apply.
# The / operator performs floating-point division.

# Addition, subtraction, multiplication, division
# result = 5 + 3
# print(result)  # Output: 8

# result = 10 - 2
# print(result)  # Output: 8

# result = 4 * 5
# print(result)  # Output: 20

# result = 12 / 3
# print(result)  # Output: 4.0 (float)

# Exponentiation
# result = 2 ** 3
# print(result)  # Output: 8

# Order of operations
# result = 2 * (3 + 4)
# print(result)  # Output: 14

# -----------------------------------------------------------------------------------

# Sequences

# Sequences store collections of items in a specific order.
# Lists are mutable, meaning you can change their contents.
# Tuples and strings are immutable, meaning they cannot be changed after creation.
# Sets store unique elements and are unordered.

# Lists (ordered, mutable)
# my_list = [1, 2, 3, "apple", True]
# print(my_list[0])  # Output: 1 (accessing elements by index)
# my_list.append(4)  # Adding elements
# my_list.remove(2)  # Removing elements

# Tuples (ordered, immutable)
# my_tuple = (1, "two", 3.0)
# print(my_tuple[1])  # Output: "two"
# Tuples cannot be modified after creation

# Strings (ordered, immutable)
# my_string = "Hello, world!"
# print(my_string[0])  # Output: "H"
# Strings cannot be modified directly, but you can create new strings

# Sets (unordered, unique elements)
# my_set = {1, 2, 2, 3}  # Duplicates are automatically removed
# print(my_set)  # Output: {1, 2, 3}

# -----------------------------------------------------------------------------------

# Conditional Flow

# Used for making decisions based on conditions.

# age = 20
# if age > 18:
#     print("You are an adult.")
# elif age == 18:
#     print("You are 18.")
# else:
#     print("You are not an adult.")

# -----------------------------------------------------------------------------------

# Looping and Iterations

# for and while loops allow you to repeat code blocks multiple times.
# List comprehensions provide a compact way to create lists based on existing iterables.

# For loop iterating over a list
# my_list = ["Volvo", "Mercedes", "BMW"]
# for item in my_list:
#     print(item)

# Another for loop example to iterate over a list and access the index of each element
# len() -> Built-in function to find the length of an array
# range () -> Built-in function to create a sequence of numbers starting from 0
# my_other_list = ["Soccer", "Baseball", "Basketball"]
# for index in range(len(my_list)):
#     print(my_list[index])

# While loop iterating until a condition is met
# count = 0
# while count < 2:
#     print(count)
#     count += 1

# -----------------------------------------------------------------------------------

# Functions

# Functions are reusable blocks of code that perform specific tasks.
# They can take arguments and return values.

# def greet(name):
#     print("Hello, " + name + "!")
#
# greet("Alice")  # Output: Hello, Alice!

# -----------------------------------------------------------------------------------

# Importing Modules

# Modules provide additional functionality in Python.
# Use import to make them available in your code.
# Access module functions using dot notation (e.g., math.sqrt).

# import math
#
# result = math.sqrt(16)  # Using functions from the math module
# print(result)  # Output: 4.0

# -----------------------------------------------------------------------------------

# Exceptions

# The try block contains the code that might raise an exception.
# If an exception occurs within the try block, the execution jumps
# to the first matching except block that handles that type of exception.
# You can have multiple except blocks to handle different exception types.

# try:
#     # Code that might raise an exception
#     result = 10 / 0
# except ZeroDivisionError:
#     print("You cannot divide by zero!")
# finally:
#     print("I'll be always printed.")


