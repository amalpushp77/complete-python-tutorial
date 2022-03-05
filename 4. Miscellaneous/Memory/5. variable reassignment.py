def address(var):
    print(hex(id(var)))

a = 10
address(a)

a = a + 4
address(a)


a += 5
address(a)