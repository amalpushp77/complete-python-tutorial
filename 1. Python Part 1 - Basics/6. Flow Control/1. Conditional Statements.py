# more on conditional statements https://www.geeksforgeeks.org/python-if-else/

# if statement

i = input("Enter your name: ")

if i == 'Aditya':  # test expression
    # if block
    print("Good Morning", i)  # if statements will get executed only when if condition is True

# if - else statement

age = int(input("Enter your age: "))

if age >= 18:  # Test Expression
    print("You are eligible to vote")
else:
    print("You are not 18 years old. You cannot vote.")

# nested if statements

i = int(input("Enter a number: "))
if i >= 10:
    #  First if statement
    if i < 15:
        print("i is smaller than 15")
    # Nested - if statement
    # Will only be executed if statement above
    # it is true
    if i < 12:
        print("i is smaller than 12 too")
    else:
        print("i is greater than 15")

# nested if - else
a = 12
b = 13
if a > 10:
    print('inside 1st if block')
    if b < 15:
        print('inside nested if')
    else:
        print('inside of nested else')
else:
    print('inside else block')

print('outside of nested if else')

# if-elif-else ladder

if a > 7:
    print('inside of if block')
elif a < 7:
    print('inside of elif block')
else:
    print('inside of else block')

print('outside of if elif else block')


marks = int(input("Enter your marks: "))
if 45 < marks <= 50:
    print("Your grade is A+")
elif 40 < marks <= 45:
    print("Your grade is A")
elif 30 < marks <= 40:
    print("Your grade is B")
elif 20 < marks <= 30:
    print("Your grade is C")
elif 15 < marks <= 20:
    print("Your grade is D")
else:
    print("You have Failed")

print("This is your next line")

