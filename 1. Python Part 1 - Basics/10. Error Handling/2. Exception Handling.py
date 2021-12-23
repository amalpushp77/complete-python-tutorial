# Exception Handling

"""
Exception Handling is important so that the program won't crash even if something unexpected happens.

Python has total of 4 blocks to handle exception
1) try: any part of program that has potential to cause error is placed inside try block
2) except: except block will run only if try block gets any error.
3) else: (Optional) else block will run only if there isn't any error while interpreting try block
4) finally: (Optional) finally block will execute every time error or not in try block
"""
#
# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")
#
# print("Now we can use integer value in our program")


# def division(a, b):
#     return a / b
#
#
# d = division(2, 0)
# print(d)
#
# print("Program is working only when there isn't any ERROR!")


def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Why are you dividing by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")


divide(2, 0)

print('Program is still running')
