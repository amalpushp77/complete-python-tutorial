string = "hello world"
print(string[1:1])
print(string[-1:])
print(string[:-1])
print(string[:-1:-1])
print(string[-1::-1])
print(string[:-2:-1])

# 2. Comment on output
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a[1:1] = a[-2::-1]     # insertion at a given index
# a[1:3] = a[-2::-1]
a[::-2] = "ZYXWV"
print(a)
