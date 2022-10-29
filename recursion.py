# loop - for, while
# function - return keyword
# stack

# def func(a, b):
#     print(a+b)
#
# x = func(5,6)
# print(x)

# def fact(n):
#     if n==1:
#         return 1
#     else:
#         return n*fact(n-1)
#
# print(fact(5))


def nums(n, l=None):
    if n == 0:
        return 0
    elif l is not None:
        l.append(n)
        n = nums(n-1, l)
        print(n)
        return n
        # return nums(n-1, l)
    else:
        l = []
        l.append(n)
        return l, nums(n-1,l)


l1, _ = nums(5)
# print(f"l1: {l1}")
# print(f"_: {_}")

# print(f"l: {l}")





# def count_z(num):
#     if num==0:
#         return 0
#     elif num%10==0:
#         return 1+count_z(num//10)
#     else:
#         return count_z(num//10)
#
#
# n = 200000526803245002
# print(count_z(n))



