# Set { }
# set it only store unique value i.e. a={1,2,2,3} after execution a={1,2,3}
# sets don't support indexing and slicing
# s = set() # empty set

s = {1, 1, 1, 1, 1, 1, 2, 3, 4, 5, 6}
print(s)
print(type(s))

# Operations on Set
A = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
B = {2, 3, 5, 7, 11, 13, 17, 19}

# Difference
print(A-B)

# Union
print(A | B)

# Intersection
print(A & B)

# Complement of A&B
print(A ^ B)
