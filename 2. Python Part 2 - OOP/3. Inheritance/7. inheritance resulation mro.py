class A:
    x=10


class B(A):
    pass


class C(A):
    pass


class D(C):
    x = 5


class E(B, D):
    pass


e = E()
print(e.x)
print(E.__mro__)

""" If the same class appears in mro (method resolution order) the earlier occurrence get removed
    E-B-A-D-C-A -> E-B-D-C-A. Still in DFS"""