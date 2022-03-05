# An object is mutable when its internal state can be changed

import ctypes


def address(var):
    print(hex(id(var)))
    return id(var)


def get_value(add):
    print(ctypes.cast(add, ctypes.py_object).value)


def ref_count(address):
    print(ctypes.c_long.from_address(address).value)
    return ctypes.c_long.from_address(address).value


# list is mutable
l = [1,2,34,4,4]
l1 = address(l)

l[2] = 55
address(l)

l.append(234)
address(l)

l = l + [77]  # reassignment creates a new memory location
address(l)
ref_count(l1)
get_value(l1)


s = 'abcd'
address(s)
s = 'abcde'
address(s)