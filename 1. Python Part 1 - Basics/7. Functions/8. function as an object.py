def add(a,b):
    return a+b


def mul(a,b):
    return a*b


def power(a,b):
    return a**b


def sub(a,b):
    return a-b


def cal(func):
    if func == 1:
        return add
    elif func == 2:
        return sub
    elif func == 3:
        return mul
    elif func == 4:
        return power


def exec_func(f, *n):
    return f(*n)


f = cal(4)
print(f(5,3))

print(exec_func(f,5,3))