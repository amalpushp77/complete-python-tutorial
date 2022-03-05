import ctypes


def ref_count(address):
    return ctypes.c_long.from_address(address).value


class A:
    def __init__(self):
        self.b = B(self)
        print('A: self: {0}, b:{1}'.format(hex(id(self)), hex(id(self.b))))


class B:
    def __init__(self, a):
        self.a = a
        # print(a)
        print('B: self: {0}, a: {1}'.format(hex(id(self)), hex(id(self.a))))


my_var = A()
print(hex(id(my_var)))


a_id = id(my_var)
b_id = id(my_var.b)

print('refcount(a) = {0}'.format(ref_count(a_id)))
print('refcount(b) = {0}'.format(ref_count(b_id)))