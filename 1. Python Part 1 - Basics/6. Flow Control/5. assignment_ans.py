# 1. WAP to find the largest of 2 numbers taken from user

num1 = input("enter number A")
num2 = input("enter number B")

if num1 > num2:
    print("Largest number is: ", num1)
else:
    print("Largest number is: ", num2)

# 2. WAP to find the largest and smallest of 3 numbers taken from user

num1 = int(input('Enter First number : '))
num2 = int(input('Enter Second number : '))
num3 = int(input('Enter Third number : '))

a = int(input('enter a: '))
b = int(input('enter b: '))
c = int(input('enter c: '))

# a) the largest of 3 numbers taken from user
if a > b > c or a > c > b:
    print("Largest number is ", a)
elif b > a > c or b > c > a:
    print('Largest number is ', b)
else:
    print('Largest number is ', c)

# b) the largest and the smallest of 3 numbers taken from user
if num1 > num2 > num3 or num1 > num3 > num2:
    print("Largest number is:", num1)
    if num2 > num3:
        print("Smallest number is:", num3)
    else:
        print("Smallest number is:", num2)
elif num2 > num1 > num3 or num2 > num3 > num1:
    print("Largest number is:", num2)
    if num1 > num3:
        print("Smallest number is:", num3)
    else:
        print("Smallest number is:", num3)
else:
    print("Largest number is:", num3)
    print("Smallest number is:", num1)

# 3. Create a multiplication table form 1*1 up to 10*10.
for i in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
    for j in (10, 9, 8, 7, 6, 5, 4, 3, 2, 1):
        print('{}*{} ='.format(i, j), i * j)

# 3. Print multiplication table of 14 from a list in which multiplication table of 12 is stored.
l = [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]
count = 1
for i in l:
    print(i + 2 * count)
    count += 1

# 4. Using range(1,101), print all numbers which are divisible bt 5
for i in range(1, 101):
    if i % 5 == 0:
        print(i)

# 5. WAP to print all the consonants by taking input from user
string = "combining the best experiences in tile manufacture and latest technology, " \
         "artile become a highest achievement in lifestyle."

for char in string:
    if char not in "aeiou":
        print(char, end="")


# 6. Display only number(without comma)

number = '9,452,798,132,546,500'
# print(number.replace(",", ""))
for i in range(0, len(number)):
    if number[i] in '0123456789':
        print(number[i])

# 7. WAP tp find the index of every element (included nested once) for

l = ['a', 'b', '65', 54, '78', 67.46788, [1, 2, 3], 'Hello World', 7 - 3.8j, (4, 5, 6, 7, 8)]

for index, value in enumerate(l):
    print("Index of", value, "is:", index)
    if type(value) != int and type(value) != float and type(value) != complex:
        if len(value) > 1:
            print('*' * 30)
            for nested_index, nested_value in enumerate(value):
                print("Index of", nested_value, "is:", nested_index)
    print('=' * 30)
