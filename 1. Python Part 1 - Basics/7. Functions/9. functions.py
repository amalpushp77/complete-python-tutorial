def func(a):
    print(id(a))
    a.append(9)


b = [1, 2, 3, 4, 5]
print(id(b))
func(b)
print(b)

# unpacking iterables
a, b, c = 'XYZ'
print(a)
print(b)
print(c)
# * can be used once in LHS
a, b, *c = 'XYZACK'
print(a)
print(b)
print(c)

a, b, *c, d = 'XYZACK'
print(a)
print(b)
print(c)

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]

l = [l1, l2]
print(l)

unpack = [*l1, *l2]
print(unpack)

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 6, 'f': 5}

# d = {d1, d2, d3}
# print(d)

# keys as set
d_s1 = {*d1, *d2, *d3}
print(d_s1)

# keys and values as dictionary
d_s2 = {**d1, **d2, **d3}
print(d_s2)

# keys and values as dictionary
d_ex = {'a': 5, **d1, **d2, **d3}  # default value if don't exist
print(d_ex)

# keys and values as dictionary
d_ex = {**d1, **d2, **d3, 'a': 5}  # default value overwrites everytime if exist
print(d_ex)

# nested unpacking

a, b, (c, d) = [1, 2, ['X', 'Y']]
print(a)
print(b)
print(c)
print(d)

a, *b, (c, d, *e) = [1, 2, 3, 'python']
print(a)
print(b)
print(c)
print(d)
print(e)

a, *b, (c, d, *e) = [1, 2, 3, 'python']
print(a)
print(b)
print(c)
print(d)
print(e)


def func1(a, b, *args):
    print(a)
    print(b)
    print(args)


def avg(*args):
    # count = len(args)
    # total = sum(args)
    # if count == 0:
    #     return 0
    # else:
    #     return total/count

    return len(args) and sum(args) / len(args)


print(avg())


def func1(a, b, c):
    print(a)
    print(b)
    print(c)


l = [10, 20, 30]

func1(*l)


def func1(a, b, *args, d):
    print(a, b, args, d)


func1(10, 20, 'a', 'b', 100)


def func1(*, a, b):
    print(a)
    print(b)


func1(a=10, b=20)
func1(10, 20)


def func1(a, *, b='hello', c):
    print(a, b, c)


func1(5, c='bye')

''' 
    def func(a, b)
    def func(a, b=10)
    def func(a, b, *args)
    def func(a, b, *args, kw1, kw2=100)
    def func(a, b, *, kw1, kw2=100)
    def func(a, b, *args, kw1, kw2=100, **kwargs)
    def func(a, b, *, kw1, kw2=100, **kwargs)  
    def func(*args)
    def func(**kwargs)
    def func(*args, **kwargs)
    
    *args -> tuple
    *kwargs -> dictionary
    '''


# Positionals Only: no extra positionals, no defaults (all positionals required)
def func(a, b):
    print(a, b)


func('hello', 'world')
func(b='world', a='hello')


# Positionals Only: no extra positionals, defaults (some positionals optional)
def func(a, b='world', c=10):
    print(a, b, c)


func('hello')
func('hello', c='!')


# Positionals Only: extra positionals, no defaults (all positionals required)
def func(a, b, *args):
    print(a, b, args)


func(1, 2, 'x', 'y', 'z')


# func(b=2, a=1, 'x', 'y', 'z')   # Note that we cannot call the function this way

# Keywords Only: no positionals, no defaults (all keyword args required)
def func(*, a, b):
    print(a, b)


func(a=1, b=2)


# Keywords Only: no positionals, some defaults (not all keyword args required)
def func(*, a=1, b):
    print(a, b)


func(a=10, b=20)
func(b=2)


# Keywords and Positionals: some positionals (no defaults), keywords (no defaults)
def func(a, b, *, c, d):
    print(a, b, c, d)


func(1, 2, c=3, d=4)
func(1, 2, d=4, c=3)
func(1, c=3, d=4, b=2)


# Keywords and Positionals: some positional defaults
def func(a, b=2, *, c, d=4):
    print(a, b, c, d)


func(1, c=3)
func(c=3, a=1)
func(1, 2, c=3, d=4)
func(c=3, a=1, b=2, d=4)


# Keywords and Positionals: extra positionals
def func(a, b=2, *args, c=3, d):
    print(a, b, args, c, d)


func(1, 2, 'x', 'y', 'z', c=3, d=4)
# Note that if we are going to use the extra arguments, then we cannot actually use a default value for b
func(1, 'x', 'y', 'z', c=3, d=4)


# Keywords and Positionals: no extra positionals, extra keywords
def func(a, b, *, c, d=4, **kwargs):
    print(a, b, c, d, kwargs)


func(1, 2, c=3, x=100, y=200, z=300)
func(x=100, y=200, z=300, c=3, b=2, a=1)


# Keywords and Positionals: extra positionals, extra keywords
def func(a, b, *args, c, d=4, **kwargs):
    print(a, b, args, c, d, kwargs)


func(1, 2, 'x', 'y', 'z', c=3, d=5, x=100, y=200, z=300)


# Keywords and Positionals: only extra positionals and extra keywords
def func(*args, **kwargs):
    print(args, kwargs)


func(1, 2, 3, x=100, y=200, z=300)

# https://realpython.com/defining-your-own-python-function/
# This is Python 3.8
# Any parameters to the left of the slash (/) must be specified positionally
# def f(x, y, /, z):
#     print(f'x: {x}')
#     print(f'y: {y}')
#     print(f'z: {z}')

f(1, 2, 3)
f(1, 2, z=3)


# f(x=1, y=2, z=3)


# x and y are positional-only
# a and b are keyword-only
# z and w may be specified positionally or by keyword
# def f(x, y, /, z, w, *, a, b):
#      print(x, y, z, w, a, b)
#
# f(1, 2, z=3, w=4, a=5, b=6)
# f(1, 2, 3, w=4, a=5, b=6)


# use case
def calc_hi_lo_avg(*args, log_to_console=False):
    hi = int(bool(args)) and max(args)
    lo = int(bool(args)) and min(args)
    avg = (hi + lo) / 2
    if log_to_console:
        print("high={0}, low={1}, avg={2}".format(hi, lo, avg))
    return avg


avg = calc_hi_lo_avg(1, 2, 3, 4, 5)
print(avg)

avg = calc_hi_lo_avg(1, 2, 3, 4, 5, log_to_console=True)
print(avg)

# a simple function timer
"""We'll call our function time_it, and it will need to have the following parameters:

the function we want to time
the positional arguments of the function we want to time (if any)
the keyword-only arguments of the function we want to time (if any)
the number of times we want to run this function"""

import time


# def time_it(fn, *args, rep=5, **kwargs):
#     print(args, rep, kwargs)

def time_it(fn, *args, rep=5, **kwargs):
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    return (end - start) / rep


def compute_powers_1(n, *, start=1, end):
    # using a for loop
    results = []
    for i in range(start, end):
        results.append(n ** i)
    return results


def compute_powers_2(n, *, start=1, end):
    # using a list comprehension
    return [n ** i for i in range(start, end)]


def compute_powers_3(n, *, start=1, end):
    # using a generator expression
    return (n ** i for i in range(start, end))


time_it(compute_powers_1, n=2, end=20000, rep=4)
time_it(compute_powers_2, n=2, end=20000, rep=4)
time_it(compute_powers_3, n=2, end=20000, rep=4)

# default values in parameter of a function - beware
from datetime import datetime


# 1
def log_prob(msg, *, dt=datetime.utcnow()):
    print('{0}: {1}'.format(dt, msg))


log_prob('message 1')
log_prob('message 2')
log_prob('message 3')


def log(msg, *, dt=None):
    dt = dt or datetime.utcnow()
    # above is equivalent to:
    # if not dt:
    #    dt = datetime.utcnow()
    print('{0}: {1}'.format(dt, msg))


log('message 1')
log('message 2')
log('message 3')


# 2
def add_item(name, quantity, unit, grocery_list):
    item_fmt = "{0} ({1} {2})".format(name, quantity, unit)
    grocery_list.append(item_fmt)
    return grocery_list


store_1 = []
store_2 = []

add_item('bananas', 2, 'units', store_1)
add_item('grapes', 1, 'bunch', store_1)
add_item('python', 1, 'medium-rare', store_2)

print(store_1)
print(store_2)


def add_item(name, quantity, unit, grocery_list=[]):
    item_fmt = "{0} ({1} {2})".format(name, quantity, unit)
    grocery_list.append(item_fmt)
    return grocery_list


store_1 = add_item('bananas', 2, 'units')
add_item('grapes', 1, 'bunch', store_1)
print(store_1)

store_2 = add_item('milk', 1, 'gallon')
print(store_2)


def add_item(name, quantity, unit, grocery_list=None):
    if not grocery_list:
        grocery_list = []
    item_fmt = "{0} ({1} {2})".format(name, quantity, unit)
    grocery_list.append(item_fmt)
    return grocery_list


store_1 = add_item('bananas', 2, 'units')
add_item('grapes', 1, 'bunch', store_1)

store_2 = add_item('milk', 1, 'gallon')
print(store_2)


# use case
def factorial(n):
    if n < 1:
        return 1
    else:
        print('calculating {0}!'.format(n))
        return n * factorial(n - 1)


factorial(3)
factorial(3)


def factorial(n, cache={}):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print('calculating {0}!'.format(n))
        result = n * factorial(n - 1)
        cache[n] = result
        return result


factorial(3)
factorial(3)
factorial(5)


# docstring and annotation
def my_func(a, b):
    return a * b


help(my_func)


def my_func(a, b):
    'Returns the product of a and b'
    return a * b


help(my_func)


def fact(n):
    '''Calculates n! (factorial function)

    Inputs:
        n: non-negative integer
    Returns:
        the factorial of n
    '''

    if n < 0:
        '''Note that this is not part of the docstring!'''
        return 1
    else:
        return n * fact(n - 1)


help(fact)
print(fact.__doc__)


def my_func(a: 'annotation for a',
            b: 'annotation for b') -> 'annotation for return':
    return a * b


help(my_func)

x = 3
y = 5


def my_func(a: str) -> 'a repeated ' + str(max(3, 5)) + ' times':
    return a * max(x, y)


help(my_func)

print(my_func.__annotations__)


def fact(n: 'int >= 0') -> int:
    '''Calculates n! (factorial function)

    Inputs:
        n: non-negative integer
    Returns:
        the factorial of n
    '''

    if n < 0:
        '''Note that this is not part of the docstring!'''
        return 1
    else:
        return n * fact(n - 1)

help(fact)

def my_func(a:str='a', b:int=1)->str:
    return a*b

help(my_func)

my_func()
my_func('abc', 3)

def my_func(a:int=0, *args:'additional args'):
    print(a, args)

print(my_func.__annotations__)

help(my_func)

# lambda
a = lambda x: x**2
print(a)
print(type(a))

print(func(3))

func_2 = lambda x, *args, y, **kwargs: (x, *args, y, {**kwargs})
func_2(1, 'a', 'b', y=100, a=10, b=20)

# Passing as an Argument
# Lambdas are functions, and can therefore be passed to any other function as an argument (or returned from another function)

def apply_func(x, fn):
    return fn(x)

apply_func(3, lambda x: x**2)

# Lambdas and Sorting

l = ['a', 'B', 'c', 'D']
sorted(l)

sorted(l, key=str.upper)

l = ['Cleese', 'Idle', 'Palin', 'Chapman', 'Gilliam', 'Jones']
sorted(l, key=lambda s: s[-1])

# Randomizing an Iterable using Sorted

import random
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sorted(l, key=lambda x: random.random())
sorted('abcdefg', key = lambda x: random.random())
''.join(sorted('abcdefg', key = lambda x: random.random()))