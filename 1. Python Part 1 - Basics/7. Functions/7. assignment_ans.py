# 1. WAP create a simple calculator using functions

def add(x, y):
    c = x + y
    return c


def sub(a, b):
    c = a - b
    return c


def multiply(a, b):
    c = a * b
    return c


def div(a, b):
    c = a / b
    return c


print("enter the operator")
print("1.Add")
print("2.sub")
print("3.multi")
print("4.div")

operator = input("1/2/3/4")

num1 = int(input("enter 1st number"))
num2 = int(input("enter 2nd number"))

if operator == "1":
    # print(add(num_1,num_2))
    print(num1, "+", num2, "=", add(num1, num2))


# 2. WAF to return a list of odd numbers between 1 and 100

def odd_list():
    l = []
    # index = 0
    for i in range(1, 101):
        if i % 2 == 1:
            # i%2!=0
            # i%2
            # range(1,101,2)

            l.append(i)

            # l.insert(index,i)
            # index+=1

    return l


print(odd_list())


# 3. WAF to return a list of even numbers by user defined range

def even_list():
    start = int(input("Initial value: "))
    stop = int(input('Last exclusive value: '))
    l = []
    # index = 0
    for i in range(start, stop):
        if i % 2 == 0:
            # i%2!=1

            l.append(i)

            # l.insert(index,i)
            # index+=1

    return l


print(even_list())


# 4. WAF to return even and odd list of numbers by user define range

def even_odd_number():
    """
    returns a list of even and odd numbers within a range."""

    even_list = []
    odd_list = []

    initial = int(input("enter initial range: "))
    final = int(input("enter final range: "))

    for i in range(initial, final + 1):
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    return even_list, odd_list


a, b = even_odd_number()
print(a)
print(b)

print(dir())
print(help(even_odd_number))


# 5. WAF that checks whether a number is present in a given range (between 10 and 100)

def isrange(value):
    print('function is called')
    i = 10
    f = 100

    if i < value < f:
        # print(True)
        return True
    else:
        # print(False)
        return False


print("1st line that executed")
x = int(input("Enter a number to check whether in range or not: "))
print('before function call')
result = isrange(x)
print(result)


# 6. WAF that accepts a string and calculate the number of uppercase letters and lowercase letters

def count_case(string):
    u_count = 0
    l_count = 0
    for i in string:
        if i.isupper():
            u_count += 1
        else:
            l_count += 1

    return u_count, l_count


s = input("Enter a string: ")
u, l = count_case(s)
print(u)
print(l)


# 7. WAP to implement list index method

def lst_index(l):
    index = 0
    for i in l:
        if i == 'cherry':
            break
        index += 1
    return index


l = [2, 67, 5, 2, 426, 23, "asd", [4, 5, 6, 7]]
print(lst_index(l))
