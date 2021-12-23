# keywork - lambda
# uses of lambda - https://towardsdatascience.com/lambda-functions-with-practical-examples-in-python-45934f3653a8

def add(a, b):
    c = a + b
    return c


l = add(5, 136)
print(l)

x = lambda a, b: a + b

s = x(3, 133)
print(s)

f = lambda x: 3 * x + 1
eq = f(3)
print(eq)

full_name = lambda fn, ln: fn.strip().title() + " " + ln.strip().title()
print(full_name('    amal    ', ' pushp          '))


# Quadratic function f(x) = ax**2 + bx + c

def quad(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


q = quad(1, 2, 3)

print(q)
print(q(3))
print("Type of q: ", type(q))
print("Type of q(3): ", type(q(3)))
