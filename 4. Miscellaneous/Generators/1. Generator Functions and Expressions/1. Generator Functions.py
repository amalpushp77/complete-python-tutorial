""" Userful for
    1. Large Data sets
    2. Memeory Intensive Operations"""

# Generator Function - Returns a generator object
# Generator Object - Uses lazy evaluation to yield sequence (yields the value)
"""     1. cannot be reused
        2. calling next() on an exhausted generators raises StopIteration
        3. for loop handles StopIteration error"""
# Keyword yield

# function solution
def even_integers_function(n):
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(i)
    return result

# generator solution
def even_integers_generator(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

intergers = even_integers_generator(10)
print(next(intergers))
print(next(intergers))