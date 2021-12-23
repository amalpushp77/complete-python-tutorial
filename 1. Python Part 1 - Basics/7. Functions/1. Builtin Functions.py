# https://www.w3schools.com/python/python_ref_functions.asp

""" 1. Sequential Programming
    2. Procedural Programming
    3. Object Oriented Programming"""

""" A function is a block of code which only runs when it is called.
        Types of Functions
        1) Built in functions
        2) User define function
        3) Methods (functions which is a part of a class)
        4) Anonymous function  """

# Built-in Functions
# more on built-in functions https://www.w3schools.com/python/python_ref_functions.asp

# Important function
# 1. dir() returns an object's attribute

# 2. range()

# 3. enumerate() returns index,value pair of itreable objects

# 4. help() return the documentation
# print(help(print))

# 5. input() take input from user and returns a string

# 6. len() returns the length of object
# print(len('abcd'))

# 7. print()

# all type casting functions
'''
int()
str()
float()
complex()
list()
tuple()
set()
dict()
'''

# 8. filter()

ages = [5, 12, 17, 18, 24, 32]


def myFunc(x):
    if x < 18:
        return False
    else:
        return True


adults = list(filter(myFunc, ages))

print(adults)

# 9. map()

ages = [5, 12, 17, 18, 24, 32]


def myFunc(x):
    if x < 18:
        return False
    else:
        return True


adults = list(map(myFunc, ages))

print(adults)

# 10. zip()

name = ['abc', 'def', 'ije']
age = [23, 34, 24]
marks = (45, 55, 56)

sheet = list(zip(name, age, marks))  # tips n trick with for loop
print(sheet)


# ========================================================================================
# Functions

# ascii() returns a value to non ascii character
# print(type(ascii('ș')))

# chr() returns the character
# print(chr(67))

# max() returns maximum value
# min() returns minimum value

# open()

# ord() returns an integer that represents Unicode

# sorted() returns a sorted object

# iter()
# next()

# ==========================================================================================
# other functions

# round()
# print(round(758.12856,3)) #example of round

# ==========================================================================================
# Functions related to class

# classmethod()
# delattr()
# getattr()
# hasattr()
# setattr()
# hash()
# property()
# id()
# isinstance()
# issubclass()
# object()
# staticmethod()
# super()
