# Slicing [start:stop]
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Forward index slicing
print(lst[0:4])
print(lst[6:9])

# Backward Index Slicing
print(lst[-10:-6])

# Stepwise Slicing [start:stop:step]
print(lst[0::2])

print(lst[0:6:3])

# Reverse
print(lst[-1:-11:-1])
print(lst[::-1])


# Reverse a string
string = "Hello World!"

print('To reverse complete string:', string + ' to', string[::-1])
print('To reverse only:', string[0:5], 'to', string[4::-1])
print('Similarly reverse', string[6:], 'to', string[10:5:-1])
