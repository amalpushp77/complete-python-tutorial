# List Comprehension

a = 7

l = []
for i in range(10):
    l.append(i)

l = [i for i in range(10)]
print(l)

num = 30
l = []
for i in range(1, num + 1):
    if num % i == 0:
        l.append(i)

l = [i for i in range(1, num + 1) if num % i == 0]
print(l)

l = [x ** 2 for x in range(11)]

print(l)

# Single line for loop with if statement
lst = [num for num in range(11) if num % 2 == 0]

print(lst)

# convert celsius to fahrenheit
# f = c*(9/5) + 32

celsius = [-50, 0, 10, 37, 50]

fahrenheit = [temp * (9 / 5) + 32 for temp in celsius]

print(fahrenheit)

v = [5, -6, 7]
w = [10 * i for i in v]

print(w)

# Cartesian Product
# A x B = {(a,b) | a belongs to set A, b belongs to set B}
# A = {1,3}
# B = {x,y}

# A x B = {(1,x), (1,y), (3,x), (3,y)}

a = [1, 3, 5, 7]
b = [2, 4, 6, 8]

cartesian_product = {(x, y) for x in a for y in b}

print(cartesian_product)

# Tuple comprehension- same as of list, except --> ()
celsius = [-50, 0, 10, 37, 50]
fahrenheit = (temp * (9 / 5) + 32 for temp in celsius)
print(fahrenheit)