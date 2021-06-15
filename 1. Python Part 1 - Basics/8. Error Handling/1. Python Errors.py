#Errors in Python
# https://www.programiz.com/python-programming/exceptions
# https://www.tutorialsteacher.com/python/error-types-in-python

# 1. Syntax Error
# 2. Logical Error / Built-in Exceptions


# Indentation Error

a = 7


# Logical Errors

# Import Error - Raised when the imported module is not found. The ImportError is thrown when a specified function can not be found

#from math import cube

#print(sqrt(4))

# IndexError - Raised when the index of a sequence is out of range.

#a = 'hello world!'

#print(a[40])

# KeyError - Raised when a key is not found in a dictionary.

#d = {1: 'apple', 2: 'mango', 3:'orange'}
#print(d[4])


# KeyboardInterrupt - Raised when the user hits the interrupt key (Ctrl+C or Delete).

# while True:
#     print('infinite loop')

# NameError - Raised when a variable is not found in local or global scope.

# age = 18
# print(agee)

# TypeError - The TypeError is thrown when an operation or function is applied to an object of an inappropriate type.

# a = 5 + 'abcd'
# print(a)


# ValueError - Raised when a function gets an argument of correct type but improper value.

# age = int(input('Enter age:'))
# print(age)

# ZeroDivisionError - Raised when the second operand of division or modulo operation is zero.

# a = 5/0
# print(a)