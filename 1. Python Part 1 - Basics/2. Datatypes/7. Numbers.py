import sys
import time
from fractions import Fraction
import math

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
