import timeit
from functools import lru_cache


# print(help(timeit.timeit))
# print(help(timeit.default_timer))

def fibonacci_explicit(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    elif n > 2:
        value = fibonacci_explicit(n - 1) + fibonacci_explicit(n - 2)

    fibonacci_cache[n] = value

    return value


def fibonacci_re(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci_re(n - 1) + fibonacci_re(n - 2)


@lru_cache(maxsize=1000)
def fibonacci(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fibonacci(n - 1) + fibonacci(n - 2)


##start = timeit.default_timer()
##
##a = 100
##b = 100
##c = a**b
##
##stop = timeit.default_timer()
##
##print(stop - start)


##start_2 = timeit.default_timer()
##
##print()
##
##stop_2 = timeit.default_timer()
##
##print(stop_2 - start_2)


# Explicit Time

start_explicit = timeit.default_timer()

fibonacci_cache = {}

for n in range(1, 1000):
    fibonacci_explicit(n)

end_explicit = timeit.default_timer()

print()
print('Explicit:', end_explicit - start_explicit)
print()
print('-' * 100)

# Recursive Time

##start_re = timeit.default_timer()
##
##for n in range(1,35):
##    fibonacci_re(n)
##
##end_re = timeit.default_timer()
##
##print()
##print('REcursive:', end_re - start_re)
##print()
##print('-'*100)


# LRU Time

start_lru = timeit.default_timer()

for n in range(1, 1000):
    fibonacci(n)

end_lru = timeit.default_timer()

print()
print('LRU:', end_lru - start_lru)
print()
print('-' * 100)
