vars = ['a','b','c']
val = 5
for var in vars:
    exec(f"{var} = {val}")

print(a)
print(b)
print(c)