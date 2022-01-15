# Rules for Identifiers visit this link - https://www.programiz.com/python-programming/keywords-identifier

# where identifier is used
""" 1) variable name  ex- num = 7
    2) user define function name ex- def func():
    3) user define class name ex - class Student:
    4) module/package name
    """

# rules for identifiers
""" 1) It can only contain (a-z), (A-Z), (0-9) and underscore (_), special characters are not allowed
    2) It can't start with digit
    3) Keywords can't be used as identifier
    4) An identifier can be of any length
    """

# types of casing
""" 1) snake casing ex- my_variable
    2) camel casing ex - myVariable
    """

# always use a meaningful identifier
num = 50
age = 18
math_marks = 50

# should be a single variable
number1 = 13
number2 = 15

# SyntaxError occurs when you break the syntax(i.e the rules of writing your code)
# number 1 = 17  # SyntaxError: invalid syntax
# 1number = 17        # SyntaxError: invalid syntax

# Both _a and __a are different variables
_a = 'Hello World'
__a = 2
# print() function is used to display output
# print(_a)
# print(__a)

# _ is normally used as garbage collector variable
_ = 7
# print(_)

# note - avoid using function names as variable
# print = 27  # this will overwrite the built-in function print with a variable name print
# print(print)
