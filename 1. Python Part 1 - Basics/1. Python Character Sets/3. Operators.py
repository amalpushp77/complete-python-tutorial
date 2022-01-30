# Operators in python visit this link - https://www.w3schools.com/python/python_operators.asp

""" 1. Arithmetic operators
    2. Assignment operators
    3. Comparison operators
    4. Logical operators
    5. Identity operators
    6. Membership operators
    7. Bitwise operators"""

# 1. Arithmetic operators - used with numeric datatypes
print(5+6)
print(5-9)
print(9*6)
print(8/2)
print(17 % 5)  # modulus - gives remainder
print(8//3)  # floor division - gives integer value i.e quotient
print(2**3)  # power

# Modulus in detail
''' 1. 8%3 = 2
    2. 3%8 = 3 (Numerator is less than Denominator, i.e Numerator is the remainder)
    3. -8%3 = 1 (Negative Remainder, 9-8=1)
    4. -3%8 = 5 (simple subtract, 8-3=5)
    5. 0%6 = 0 (0/6 = 0)
    6. 6%0 = Error (ZeroDivisionError: integer division or modulo by zero)'''

# 2. Assignment operator
value = 7
value += 5  # same as value = value + 5

# 3. Comparison operator - returns True or False after comparing 2 values
print(5 == 7)
print(3 > 3)
print(3 >= 3)

# 4. Logical operator - condition based multiple comparison
print(5 == 7 and 6 >= 5)
print(5 == 7 or 6 >= 5)
print(not 5 == 5)

# 5. Identity operator - to compare objects with the same memory location
""" is / is not"""
c = 5
d = 7
print(c is d)

a = 5
# b = a
b = 5
print(a is b)

# 6. Membership operator - checks if a sequence is present in an object
""" in / not in"""
print('app' in 'apple')
