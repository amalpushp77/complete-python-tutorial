# 1. WAP to find the remainder without using modulus operator
num1 = 8
num2 = 3

# Calculator method
division = num1/num2
quotient = num1//num2
remainder = num2*(division-quotient)
print(remainder)
print(round(remainder))

# Alternate/Pythonic method
quotient = num1//num2
remainder = num1 - (quotient*num2)
print(remainder)

# 2. comment on the output of following statements

# comparison operator
print(True == 1)     # True is equivalent to 1
print(False == 0)    # False is equivalent to 0
print(True == -5)
print(True > False)  # 1 > 0

# membership operator
print("5" in "1458632")   # here 5 is a string
print(5 in "1458672")     # TypeError: 'in <string>' requires string as left operand, not int
print(5 in 145872)        # TypeError: argument of type 'int' is not iterable

# 3. Try short circuit evaluation with logical operators. Pre-requisite - AND/OR boolean table
# video reference
# https://www.youtube.com/watch?v=oV1JOkjCw5E&ab_channel=Finxter-CreateYourCodingBusiness
