#more on conditional statements https://www.geeksforgeeks.org/python-if-else/

# # if statement
#
# i = input("Enter your name: ")
#
# if i == 'Aditya':     # test expression
#     # if block
#     print("Good Morning", i)   # if statements will get executed only when if condition is True

a = 73
b = 121

##if a>8:
##    print('inside of if statement')
##
##print('outside of if statement')


# if - else statement
#
age = int(input("Enter your age: "))

if age >= 18:  # Test Expression
    print("You are eligible to vote")
else:
    print("You are not 18 years old. You cannot vote.")


##if a>8:
##    print('inside of if block')
##else:
##    print('inside of else block')
##
##print('outside of if else statement')


# nested if statements

i = 10
if (i == 10):
    #  First if statement
    if (i < 15):
        print ("i is smaller than 15")
    # Nested - if statement
    # Will only be executed if statement above
    # it is true
    if (i < 12):
        print ("i is smaller than 12 too")
    else:
        print ("i is greater than 15")

if a>10:
    print('inside 1st if block')
    if b<15:
        print('inside nested if')
    else:
        print('inside of nested else')
else:
    print('inside else block')

print('outside of nested if else')

# if-elif-else ladder

i = 20
if (i == 10):
    print ("i is 10")
elif (i == 15):
    print ("i is 15")
elif (i == 20):
    print ("i is 20")
else:
    print ("i is not present")


##if a>7:
##    print('inside of if block')
##elif a<7:
##    print('inside of elif block')
##else:
##    print('inside of else block')
##
##print('outside of if elif else block')


# Short Hand if statement

i = 10
if i < 15: print("i is less than 15")

# Short Hand if-else statement / comprehensive if-else

i = 10
print(True) if i < 15 else print(False)