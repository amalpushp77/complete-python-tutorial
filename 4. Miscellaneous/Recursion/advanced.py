# keypad combination
# def keypad_combination(string, index=0, combination=""):
#     if index==len(string):
#         l.append(combination)
#     else:
#         n = keypad[string[index]]
#         for i in n:
#             keypad_combination(string, index+1, combination+i)
#
#
# keypad = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
# l=[]
# keypad_combination("26")
# print(l)


# all permutation of a string - n!
# def permutation(string, per=""):
#     if len(string)==0:
#         print(per)
#         return
#
#     for i in range(len(string)):
#         char = string[i]
#         newStr = string[0:i]+string[i+1:]
#         permutation(newStr, per+char)
#
#
# permutation("abc")

# total number of path to reach from matrix 0,0 to m,n (no diagonal/cross movement)
# every step taken should reach closure to m,n
# def count_path(i=0,j=0,*,m,n):
#     if i==m or j==n:
#         return 0
#
#     if i==m-1 and j==n-1:
#         return 1
#
#     down = count_path(i+1, j, m=m, n=n)
#     right = count_path(i, j+1, m=m, n=n)
#
#     return down+right
#
# print(count_path(m=3, n=3))

# place tiles of size 1xm in a floor of size nxm


# merge sort
