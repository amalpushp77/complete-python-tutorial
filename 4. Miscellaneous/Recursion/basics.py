# recursion is a double edged sword, if not used properly it can cause stack overflow
# a function that calls itself
# let f(x) = x^2
# recursion is f(f(x)) = f(x^2) = x^4

# def func(n):
#     if n==0:
#         return
#
#     print(n)
#     func(n-1)

# func(5)

# def func_inc(n):
#     if n>=6 or n<1:
#         return
#
#     print(n)
#     func(n+1)

# def sum_n(n):
#     if n<1:
#         return 0
#     else:
#         return n+sum_n(n-1)

# print(sum_n(10))

# def factorial(n):
#     if n==1:
#         return 1
#     elif n==0:
#         return 1
#     else:
#         return n*factorial(n-1)

# print(factorial(5))

# palindrome logic
# def is_palindrome(string):
#     if len(string)==0 or len(string)==1:
#         return True
#
#     if string[0]==string[-1]:
#         return is_palindrome(string[1:-1])
#
#     return False
#
# print(is_palindrome("abccba"))

# def x_power_n(x, n):
#     if n==0:
#         return 1
#     elif x==0:
#         return 0
#     else:
#         return x*x_power_n(x,n-1)

# print(x_power_n(2,3))


# decimal_binary


# print reverse string
# def rev_s(s):
#     if s=="":
#         return ""
#
#     return rev_s(s[1:]) + s[0]
#
#
# print(rev_s("abcd"))

# find 1st and last occurrence of a char in sting
# def find_char(sting, char, index=0):
#     global first, last
#     if index==0:
#         first = -1
#         last = -1
#
#     if index==len(sting):
#         return first, last
#     elif sting[index]==char:
#         if first==-1:
#             first=index
#         else:
#             last=index
#         return find_char(sting, char, index + 1)
#     else:
#         return find_char(sting,char,index+1)
#
#
# print(find_char("abcdbcrfsasgsd","f"))


# return list of no. in decreasing order
# def nums(n, l=None):
#     if n == 0:
#         return 0
#     elif l is not None:
#         l.append(n)
#         return nums(n-1, l)
#     else:
#         l = []
#         l.append(n)
#         return l, nums(n-1,l)
#
#
#
# l1, _ = nums(5)
# print(f"l1: {l1}")
# print(f"_: {_}")


# return reversed string
# def rev_string(string, index, reverse=None):
#     if index < 0:
#         return reverse
#     elif reverse is not None:
#         reverse += string[index]
#         return rev_string(string, index - 1, reverse)
#     else:
#         reverse = ""
#         return rev_string(string, index - 1, reverse)
#
#
# s = "abcd"
# print(rev_string(s, len(s)))

# binary search
# def binary_search(array, left, right, x):
#     if left>right or right<left:
#         return -1
#
#     mid = (left+right)//2
#
#     if x==array[mid]:
#         return mid
#
#     if x<array[mid]:
#         return binary_search(array, left, mid-1, x)
#
#     return binary_search(array, mid+1, right, x)
#
#
# a = [-5,-2,0,4,5,6,7,8,11,15,20,25]
# print(binary_search(a,0, len(a), 7))


