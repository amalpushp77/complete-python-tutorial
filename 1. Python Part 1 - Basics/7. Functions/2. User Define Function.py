# 1. Parameters and return type

# a) without parameter and without return type

def add():
    c = a + b
    print(c)


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

# calling a function add
add()


# b) with parameter and without return

def sub(m, n):  # dummy variables m,n

    s = m - n
    print(s)


# a and bare called the arguments of function sub(). a&b are passed by reference, i.e memory address of a&b are passed.
# m and n are called parameters. m,n & s are local variables of sub()
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

#sub(a, b)
x = sub(a, b)
print(x)
print(type(x))


# c) with parameter and with return

def mul(m, n):
    s = m * n
    return s


a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

x = mul(a, b)
print(x)
print(type(x))


# d) without parameter and with return

def div():
    s = m / n
    return s


m = int(input("Enter a number: "))
n = int(input("Enter a number: "))

x = div()
print(x)
print(type(x))


# 2. More on user define parameterized functions

# a) Compulsory parameter

def make_list(a, b, c, d):  # dummy variables (arguments)
    l = []
    l.append(a)
    l.append(b)
    l.append(c)
    l.append(d)

    return l


m = 32
n = 43
o = 123
p = 445
q = 123
r = 4321
s = 12345
t = 192387

x = make_list(m, n, o, p)  # actual values (parameter)
print(x)

y = make_list(p, q, r, s)
print(y)

z = make_list(t, s, r, q)
print(z)


# b) Default (optional) parameter - must be at the end

def make_list(a, b, c=0, d=0):
    l = []
    l.append(a)
    l.append(b)
    l.append(c)
    l.append(d)

    return l


m = 32
n = 43
o = 123
p = 445
q = 123
r = 4321
s = 12345
t = 192387

x = make_list(m, n, o)
print(x)

y = make_list(p, q, r, s)
print(y)

z = make_list(t, s, r, q)
print(z)


# c) unknown number of arguments

def create_list(*arg):
    return [*arg]


l = create_list(1, 2, 3, 4, 5, 6, 4)
print(l)


def add(*args):
    return sum(args)


a = add(1, 2, 3, 4, 5, 6, 4)
print(a)


# d) unknown number of arguments with default values

def pair(**kwargs):
    print(kwargs)


pair(a=3, b=4, asdf=1234)
