testCases = int(input())
for i in range(0, testCases):
    N = input()
    A = list(map(int,input().split()))
    K = int(input())
    result = A[K - 1]
    A = sorted(A)
    for i in range(0, len(A)):
        if (A[i]== result):
            print (i + 1)

# 3
# 4
# 1 3 4 2
# 2
# 5
# 1 2 3 9 4
# 5
# 5
# 1 2 3 9 4
# 1