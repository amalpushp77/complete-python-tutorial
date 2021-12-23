# Dictionary

square_dict = dict()
for num in range(1, 11):
    square_dict[num] = num * num
print(square_dict)

square_dict = {num: num*num for num in range(1, 11)}
print(square_dict)

d = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
print(d)
