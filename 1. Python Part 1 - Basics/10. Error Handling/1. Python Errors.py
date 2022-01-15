# Errors in Python
# https://www.programiz.com/python-programming/exceptions
# https://www.tutorialsteacher.com/python/error-types-in-python

# To troubleshoot you should ask these questions to yourself
# 1. What does this error mean?
# 2. Where this error happened?
# 3. How to fix this error?


# 1. Syntax Error
# 2. Logical Error / Built-in Exceptions


# Indentation Error

 # a = 7


# Logical Errors

# ImportError - Raised when the imported module is not found.
# The ImportError is thrown when a specified function can not be found

# from math import cube
# print(cube(4))

# IndexError - Raised when the index of a sequence is out of range.

# a = 'hello world!'
# print(a[40])

# KeyError - Raised when a key is not found in a dictionary.

# d = {1: 'apple', 2: 'mango', 3:'orange'}
# print(d[4])

# NameError - Raised when a variable is not found in local or global scope.

# age = 18
# print(agee)

# TypeError - The TypeError is thrown when an operation or function is applied to an object of an inappropriate type.

# a = 5 + 'abcd'
# print(a)


# ValueError - Raised when a function gets an argument of correct type but improper value.

# age = int(input('Enter age:'), base=16)
# print(age)

# ZeroDivisionError - Raised when the second operand of division or modulo operation is zero.

# a = 5/0
# print(a)