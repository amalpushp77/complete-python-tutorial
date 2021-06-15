#Explicit conversion/Type casting

#int()

n = '7'
n2 = int(n)

print(type(n))
print(n2)
print(type(n2))

#float()

f = 4
f2 = float(f)

print(f2)
print(type(f2))

#complex()

r = 5
r2 = complex(r)
print(r2)
print(type(r2))

#bool()
#Integer 0 --> False   except 0 --> True
#Other datatypes  if empty -->  False  if contain value --> True

w = bool("asdf")  # "", [] , () , {} , set()
print(w)
print(type(w))

#list()

l = 'asdfg'
l2 = list(l)

print(l2)
print(type(l2))

#tuple()

t = 'asdfg'
t2 = tuple(l)

print(t2)
print(type(t2))

#dict()

y = dict(a=1,b=2)
print(y)
print(type(y))

#set()

p = set([1,2,3,4])
print(p)
print(type(p))