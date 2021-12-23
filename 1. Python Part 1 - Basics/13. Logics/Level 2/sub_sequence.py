s = "abcdefg"

# 1 length sub string
# 1 pointer
p = 0
while p < len(s):
    print(s[p])

    p += 1

# 2 pointers
p1 = 0
p2 = 1

while p2<=len(s):
    print(s[p1:p2])

    p1 += 1
    p2 += 1

# 2 length sub string
p1 = 0
p2 = 2

while p2<=len(s):
    print(s[p1:p2])

    p1 += 1
    p2 += 1

# 3 length sub string
p1 = 0
p2 = 3

while p2<=len(s):
    print(s[p1:p2])

    p1 += 1
    p2 += 1

# 4 length sub string
p1 = 0
p2 = 4

while p2<=len(s):
    print(s[p1:p2])

    p1 += 1
    p2 += 1

# 5 length sub string
p1 = 0
p2 = 5

while p2<=len(s):
    print(s[p1:p2])

    p1 += 1
    p2 += 1

# 6 length sub string
p1 = 0
p2 = 6

while p2<=len(s):
    print(s[p1:p2])

    p1 += 1
    p2 += 1


# n length sub-string
p1 = 0
gap = 1

while gap <= len(s):
    p1 = 0
    p2 = gap
    while p2 <= len(s):
        print(s[p1:p2])

        p1 += 1
        p2 += 1

    gap += 1