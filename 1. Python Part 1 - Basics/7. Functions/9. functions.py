def func(a):
    print(id(a))
    a.append(9)

b = [1,2,3,4,5]
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

l1 = [1,2,3,4]
l2 = [5,6,7,8]

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

    return len(args) and sum(args)/len(args)

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