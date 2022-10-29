# def A(n):
#     if n>0:
#         print(n)
#         A(n-1)
#         print(n)

# total of n invocation/function call
# TC: O(n)
# SC: Height of tree, O(n)
# A(3)


# def A(n):
#     if n>0:
#         A(n-1)
#         print(n)
#         A(n-1)
#
# # TC: O(2^n)
# # SC: Height of tree, O(n)
# A(3)

# tower of hanoi
# def hanoi_tower(n, source, destination, helper):
#     if n>=1:
#         hanoi_tower(n-1, source, helper, destination)
#         print(f"Move disk {n} from {source} to {destination}")
#         hanoi_tower(n-1, helper, destination, source)
#
#
# hanoi_tower(3, "S", "D", "H")



# def fibonacci(n):
#     if n<=1:
#         return n
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)

# print(fibonacci(10))


# sub-sequences
# def sub_seq(sting, index=0, sub=''):
#     if index==len(sting):
#         print(sub)
#         return
#
#     char = sting[index]
#
#     sub_seq(sting, index+1, sub+char)
#     sub_seq(sting, index+1, sub)
#
#
# sub_seq("abc")


# unique sub-sequences
# def sub_seq(sting, index=0, sub=''):
#     global s
#     if index==len(sting):
#         s.add(sub)
#         return
#
#     if index==0:
#         s = set()
#
#     char = sting[index]
#
#     sub_seq(sting, index+1, sub+char)
#     sub_seq(sting, index+1, sub)
#
#
# sub_seq("aba")
# print(s)
#
#
# def countSubstring(str1, str2):
#     n1 = len(str1)
#     n2 = len(str2)
#
#     if n1 == 0 or n1 < n2:
#         return 0
#
#     if str1[0: n2] == str2:
#         return countSubstring(str1[1:], str2) + 1
#
#     return countSubstring(str1[1:], str2)
#
#
# string = "aba"
# l = []
# for i in s:
#     if i=="":
#         continue
#
#     if countSubstring(string, i):
#         l.append(i)
#
# print(l)


# # no. of ways in which you can invite n people to your party, single or in pair
# def invite(n):
#     if n<1:
#         return 0
#
#     if n==1:
#         return 1
#
#     return invite(n-1) + (n-1)*invite(n-2)
#
# print(invite(7))


# how many ways to reach the top of stairs if you can only take 1,2 or 3 steps
def stair_top(n):
    if n<0:
        return 0

    if n==0:
        return 1

    return stair_top(n-1)+stair_top(n-2)+stair_top(n-3)

print(stair_top(5))



