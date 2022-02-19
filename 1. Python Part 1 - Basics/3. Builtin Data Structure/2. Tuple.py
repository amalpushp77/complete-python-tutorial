# Tuple is denoted by ( )

# t = () # empty tuple

t = (1, 'abc', 2.34, 3+4j, True)
print(t)
print(type(t))

# how to write one element in tuple -> (4,)
int_datatype = (4)
tuple_data_structure = (4,)
print(type(int_datatype))
print(type(tuple_data_structure))

t = (1,2,3,'hello') + (4,)  # concatenation
# t = (1,2,3,'hello') + (4) # TypeError: can only concatenate tuple (not "int") to tuple
print(t)
# print(1 not in t)  # membership operator is used to check whether 1 is present in tuple or not
