p = 15

myDiction = {}

for i in range(0, p):
    char = 'abcd'[i%4]

    if char not in myDiction:
        myDiction[char] = 0

    myDiction[char] += 1

print(myDiction)
