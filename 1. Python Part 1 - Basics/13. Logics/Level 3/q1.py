n1 = int(input("n: "))
n2 = int(input("x: "))

r = [n for n in range(1, n1+1)]
pointers = {x:0 for x in range(1, n2+1)}


for value in pointers.keys():
    print(value)
