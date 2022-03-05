def address(var):
    print(hex(id(var)))
    return id(var)


a = 7000000000
b = 7000000000
address(a)
address(b)

l1 = [1,2,3]
l2 = [1,2,3]
l3 = l1
address(l1)
address(l2)
address(l3)


# the memory manager will always use a shared referencewhen assigning a variable to None