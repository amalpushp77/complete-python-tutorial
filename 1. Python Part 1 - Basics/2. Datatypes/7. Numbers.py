import sys
import time
from fractions import Fraction
import math
from math import trunc
from math import floor
from math import ceil


print(sys.getsizeof(0)) # overhead (in bytes)
print(sys.getsizeof(1)) # 28-24 = 4 bytes are used to create 1, i.e 32bits


def calc(a):
    for i in range(10000000):
        a * 2

start = time.perf_counter()
calc(10)
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
calc(2**100)
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
calc(2**10000)
end = time.perf_counter()
print(end - start)


def div_quo_rule(n, d):
    print(n == d*(n//d) + n%d)


div_quo_rule(8,3)
div_quo_rule(8,-3)
div_quo_rule(-8,3)
div_quo_rule(-8,-3)
div_quo_rule(3,8)
div_quo_rule(3,-8)
div_quo_rule(-3,8)
div_quo_rule(-3,-8)



def from_base10(n, b):
    if b < 2:
        raise ValueError('Base b must be >= 2')
    if n < 0:
        raise ValueError('Number n must be >= 0')
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        # m = n % b
        # n = n // b
        # which is the same as:
        n, m = divmod(n, b)
        digits.insert(0, m)
    return digits

print(from_base10(255, 16))


def encode(digits, digit_map):
    # we require that digit_map has at least as many
    # characters as the max number in digits
    if max(digits) >= len(digit_map):
        raise ValueError("digit_map is not long enough to encode digits")

    # we'll see this later, but the following would be better:
    encoding = ''.join([digit_map[d] for d in digits])
    return encoding

print(encode([1, 10, 11], '0123456789AB'))


def rebase_from10(number, base):
    digit_map = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if base < 2 or base > 36:
        raise ValueError('Invalid base: 2 <= base <= 36')
    # we store the sign of number and make it positive
    # we'll re-insert the sign at the end
    sign = -1 if number < 0 else 1
    number *= sign

    digits = from_base10(number, base)
    encoding = encode(digits, digit_map)
    if sign == -1:
        encoding = '-' + encoding
    return encoding

e = rebase_from10(10, 2)
print(e)
print(int(e, 2))

e = rebase_from10(-10, 2)
print(e)
print(int(e, 2))

rebase_from10(4095, 16)
rebase_from10(-4095, 16)


print(format(0.3,'.25f'))

x = Fraction(22, 7)
print(x.numerator)
print(x.denominator)


x = Fraction(math.pi)
print(x)
print(float(x))

delta = Fraction(0.3) - Fraction(3, 10)
print(delta == 0)
print(delta)
print(float(delta))


x = Fraction(math.pi)
print(x)
print(format(float(x), '.25f'))

y = x.limit_denominator(10)
print(y)
print(format(float(y), '.25f'))

y = x.limit_denominator(100)
print(y)
print(format(float(y), '.25f'))

y = x.limit_denominator(500)
print(y)
print(format(float(y), '.25f'))

print(format(0.1, '.25f'))  # approximate float representation in base 2
print(format(0.125, '.25f'))  # exact float representation in base 2

x = 0.1 + 0.1 + 0.1
y = 0.3
print(x == y)

print('0.1 --> {0:.25f}'.format(0.1))
print('x --> {0:.25f}'.format(x))
print('y --> {0:.25f}'.format(y))

x = 0.125 + 0.125 + 0.125
y = 0.375
print(x == y)

print('0.125 --> {0:.25f}'.format(0.125))
print('x --> {0:.25f}'.format(x))
print('y --> {0:.25f}'.format(y))


x = 0.1 + 0.1 + 0.1
y = 0.3
print(math.isclose(x, y))  # relative tolerance vs absolute tolerance

x = 0.1 + 0.1 + 0.1
y = 0.3
print(math.isclose(x, y))

print(math.isclose(0.01, 0.02, rel_tol=0.01))
# be careful with relative tolerances when working with values that are close to zero
# pep 485

x = 0.0000001
y = 0.0000002
print(math.isclose(x, y, rel_tol=0.01))


print(math.isclose(x, y, abs_tol=0.0001, rel_tol=0))

x = 0.0000001
y = 0.0000002

a = 123456789.01
b = 123456789.02

print('x = y:', math.isclose(x, y, abs_tol=0.0001, rel_tol=0.01))
print('a = b:', math.isclose(a, b, abs_tol=0.0001, rel_tol=0.01))


#  Coercing Floats to Integers - data lose
print(trunc(10.3), trunc(10.5), trunc(10.6))
print(trunc(-10.3), trunc(-10.5), trunc(-10.6))

print(int(10.3), int(10.5), int(10.6))
print(int(-10.3), int(-10.5), int(-10.6))

print(floor(10.4), floor(10.5), floor(10.6))
print(floor(-10.4), floor(-10.5), floor(-10.6))

print(ceil(10.4), ceil(10.5), ceil(10.6))
print(ceil(-10.4), ceil(-10.5), ceil(-10.6))

def _round(x):
    from math import copysign
    return int(x + 0.5 * copysign(1, x))

print(round(2.5), _round(2.5)) # rounding away from zero


# decimal

import decimal
from decimal import Decimal

g_ctx  = decimal.getcontext()
print(g_ctx.prec)
print(g_ctx.rounding)
g_ctx.prec = 6
g_ctx.rounding = decimal.ROUND_HALF_UP

print(decimal.getcontext().prec)
print(decimal.getcontext().rounding)


with decimal.localcontext() as ctx:
    print(ctx.prec)
    print(ctx.rounding)


with decimal.localcontext() as ctx:
    ctx.prec = 10
    print('local prec = {0}, global prec = {1}'.format(ctx.prec, g_ctx.prec))


print(decimal.getcontext().rounding)

x = Decimal('1.25')
y = Decimal('1.35')
print(round(x, 1))
print(round(y, 1))

decimal.getcontext().rounding = decimal.ROUND_HALF_UP

x = Decimal('1.25')
y = Decimal('1.35')
print(round(x, 1))
print(round(y, 1))

decimal.getcontext().rounding = decimal.ROUND_HALF_EVEN

x = Decimal('1.25')
y = Decimal('1.35')
print(round(x, 1), round(y, 1))
with decimal.localcontext() as ctx:
    ctx.rounding = decimal.ROUND_HALF_UP
    print(round(x, 1), round(y, 1))
print(round(x, 1), round(y, 1))


print(Decimal ((0, (3,1,4,1,5), -4)))
print(Decimal((1, (1,2,3,4), -3)))
print(Decimal((0, (1,2,3), 3)))
print(Decimal(0.1)) # dont use float

decimal.getcontext().prec = 2
a = Decimal('0.12345')
b = Decimal('0.12345')
print(a+b)


decimal.getcontext().prec = 6
print(decimal.getcontext().rounding)

a = Decimal('0.12345')
b = Decimal('0.12345')
print(a + b)
with decimal.localcontext() as ctx:
    ctx.prec = 2
    c = a + b
    print('c within local context: {0}'.format(c))
print('c within global context: {0}'.format(c))

"""Since c was created within the local context by adding a and b, and the local context had a precision of 2, c was rounded to 2 digits after the decimal point.

Once the local context is destroyed (after the with block), the variable c still exists, and its precision is still just 2 - it doesn't magically suddenly get the global context's precision of 6."""

x = 10
y = 3
print(x//y, x%y)
print(divmod(x, y))
print( x == y * (x//y) + x % y)

a = Decimal('10')
b = Decimal('3')
print(a//b, a%b)
print(divmod(a, b))
print( a == b * (a//b) + a % b)


x = -10
y = 3
print(x//y, x%y)
print(divmod(x, y))
print( x == y * (x//y) + x % y)


a = Decimal('-10')
b = Decimal('3')
print(a//b, a%b)
print(divmod(a, b))
print( a == b * (a//b) + a % b)

a = Decimal('1.5')
print(a.log10())  # base 10 logarithm
print(a.ln())     # natural logarithm (base e)
print(a.exp())    # e**a
print(a.sqrt())   # square root

x = 2
x_dec = Decimal(2)

root_float = math.sqrt(x)
root_mixed = math.sqrt(x_dec)
root_dec = x_dec.sqrt()

print(format(root_float, '1.27f'))
print(format(root_mixed, '1.27f'))
print(root_dec)

print(format(root_float * root_float, '1.27f'))
print(format(root_mixed * root_mixed, '1.27f'))
print(root_dec * root_dec)

x = 0.01
x_dec = Decimal('0.01')

root_float = math.sqrt(x)
root_mixed = math.sqrt(x_dec)
root_dec = x_dec.sqrt()

print(format(root_float, '1.27f'))
print(format(root_mixed, '1.27f'))
print(root_dec)

print(format(root_float * root_float, '1.27f'))
print(format(root_mixed * root_mixed, '1.27f'))
print(root_dec * root_dec)

# decimal performance consideration

a = 3.1415
b = Decimal('3.1415')

print(sys.getsizeof(a))
print(sys.getsizeof(b))


def run_float(n=1):
    for i in range(n):
        a = 3.1415


def run_decimal(n=1):
    for i in range(n):
        a = Decimal('3.1415')


n = 10000000

start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end-start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('decimal: ', end-start)


def run_float(n=1):
    a = 3.1415
    for i in range(n):
        a + a


def run_decimal(n=1):
    a = Decimal('3.1415')
    for i in range(n):
        a + a


start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end - start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('decimal: ', end - start)

n = 5000000

import math


def run_float(n=1):
    a = 3.1415
    for i in range(n):
        math.sqrt(a)


def run_decimal(n=1):
    a = Decimal('3.1415')
    for i in range(n):
        a.sqrt()


start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ', end - start)

start = time.perf_counter()
run_decimal(n)
end = time.perf_counter()
print('decimal: ', end - start)

# complex number

a = complex(1, 2)
b = 1 + 2j

print(a == b)

print(a.real, type(a.real))
print(a.imag, type(a.imag))
print(a.conjugate())

import cmath

a = 1 + 5j
print(cmath.sqrt(a))

a = 1 + 1j

r = abs(a)
phi = cmath.phase(a)
print('{0} = ({1},{2})'.format(a, r, phi))

r = math.sqrt(2)
phi = cmath.pi/4
print(cmath.rect(r, phi))

# Euler's Identity
RHS = cmath.exp(cmath.pi * 1j) + 1
print(RHS)

cmath.isclose(RHS, 0, abs_tol=0.00001)

cmath.isclose(RHS, 0)

# boolean

# every object has a True truth value except:
# None
# Flase
# 0 in numberic (0, 0.0, 0 +0j,...)
# empty sequence (list, tuple, string,..)
# empty mapping types (dictioannry, set, ...)
# custom classes that implements a __bool__ or __len__
# methods that returns False or 0

l = []
print(l.__len__().__bool__())

a = [1, 2, 3]
if a:
    print(a[0])
else:
    print('a is None, or a is empty')

a = []
if a:
    print(a[0])
else:
    print('a is None, or a is empty')

a = 'abc'
if a:
    print(a[0])
else:
    print('a is None, or a is empty')

a = ''
if a:
    print(a[0])
else:
    print('a is None, or a is empty')

# same thing but internally
a = 'abc'
if a is not None and len(a) > 0:
    print(a[0])
else:
    print('a is None, or a is empty')

# code can crash

a = 'abc'
if a is not None:
    print(a[0])

a = ''
if a is not None:
    print(a[0])

a = None
if len(a) > 0:
    print(a[0])

a = None
if a is not None and len(a) > 0:
    print(a[0])

a = None
if len(a) > 0 and a is not None:
    print(a[0])


# short circuiting
a = 10
b = 0

if b and a/b > 2:
    print('a is at least double b')

import string
name = ''
if name[0] in string.digits:
    print('Name cannot start with a digit!')

name = ''
if name and name[0] in string.digits:
    print('Name cannot start with a digit!')

name = None
if name and name[0] in string.digits:
    print('Name cannot start with a digit!')

name = 'Bob'
if name and name[0] in string.digits:
    print('Name cannot start with a digit!')

name = '1Bob'
if name and name[0] in string.digits:
    print('Name cannot start with a digit!')

print('' or 'abc')
print(0 or 100)
print([] or [1, 2, 3] )
print([1, 2] or [1, 2, 3])


def _or(x, y):
    if x:
        return x
    else:
        return y

print(_or(0, 100) == (0 or 100))
print(_or(None, 'n/a') == (None or 'n/a'))
print(_or('abc', 'n/a') == ('abc' or 'n/a'))

# _or(1, 1/0)

s = None
a = s or 'n/a'
print(a)

total = 0
n = 0
x = n and total/n
print(x)


a = s and s[0] or 'default'
print(a)