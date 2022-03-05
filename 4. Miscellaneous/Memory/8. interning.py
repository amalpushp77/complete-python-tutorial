import time

def address(var):
    print(hex(id(var)))
    return id(var)


a = 1
b = int(True)
c = int('1')
d = int('0001', 2)

address(a)
address(b)
address(c)
address(d)


a = 'the quick brown fox'
b = 'the quick brown fox'

print(a is b)

# force string to interned -> sys.intern(string)


def compare_using_equals(n):
    a = 'a long string that is not interned' * 200
    b = 'a long string that is not interned' * 200
    for i in range(n):
        if a == b:
            pass


def compare_using_interning(n):
    a = 'a long string that is not interned' * 200
    b = 'a long string that is not interned' * 200
    for i in range(n):
        if a is b:
            pass


start = time.perf_counter()
compare_using_equals(10000000)
end = time.perf_counter()

print('equality: ', end-start)

start = time.perf_counter()
compare_using_interning(10000000)
end = time.perf_counter()

print('identity: ', end-start)