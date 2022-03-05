# list is mutable nad tuple is immutable
# thus, values inside tuple object cannot be changed

t = (1,2,3,4,5,6)
print(t)
print(hex(id(t)))

t = (1,2,3,43,5, 6)
print(t)
print(hex(id(t)))

l1 = [1,2,3]
l2 = [4,5,6]

t = (l1, l2)
print(t)
print(hex(id(t)))

l2[1] = 56
print(t)
print(hex(id(t)))

# tuple is still immutable but we indirectly change the value inside tuple because it contains mutable datatype list
# note- while creating a function mutable objects modify the existing memory using methods (not by reassignment)
# immutable object creates a new memory because of reassignment
