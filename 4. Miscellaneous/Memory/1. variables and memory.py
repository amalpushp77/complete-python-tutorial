import sys
import ctypes

a = 3
b = 5
c = 3
d = b

print(a, ':', hex(id(a)))
print(b, ':', hex(id(b)))
print(c, ':', hex(id(c)))
print(d, ':', hex(id(d)))


print(sys.getrefcount(a)) # to get actual reference count decrement by 1
print(ctypes.c_long.from_address(id(a)).value)
