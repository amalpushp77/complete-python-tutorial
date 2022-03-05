import string
import time


# python pre-calculate constant expression like
# numeric calculation
# short sequence with length less than 20

# membership test - mutables are replaced by immutables
# list to tuple
# set to frozen set

# fastest is set

def my_func():
    a = 24 * 60
    b = (1, 2) * 5
    c = 'abc' * 3
    d = 'ab' * 11
    e = 'the quick brown fox' * 1000000
    f = [1, 2] * 5

print(my_func.__code__.co_consts)


def my_func2():
    if 3 in [1, 2, 3]:
        pass

print(my_func2.__code__.co_consts)

def my_func3():
    if 1 in {1, 2, 3}:
        pass

print(my_func3.__code__.co_consts)




char_list = list(string.ascii_letters)
char_tuple = tuple(string.ascii_letters)
char_set = set(string.ascii_letters)

def membership_test(n, container):
    for i in range(n):
        if 'p' in container:
            pass

start = time.perf_counter()
membership_test(10000000, char_list)
end = time.perf_counter()
print('list membership: ', end-start)

start = time.perf_counter()
membership_test(10000000, char_tuple)
end = time.perf_counter()
print('tuple membership: ', end-start)

start = time.perf_counter()
membership_test(10000000, char_set)
end = time.perf_counter()
print('set membership: ', end-start)