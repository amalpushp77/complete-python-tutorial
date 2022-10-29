# conditional compilation

import sys
from os import path

# zz = not __debug__
# if not zz:
#     input = sys.stdin.readline
# else:
#     sys.stdin = open('input.txt', 'r')
#     sys.stdout = open('output.txt', 'w')

if path.exists('input.txt'):
    sys.stdin = open("input.txt", "r")
    sys.stdout = open("output.txt", "w")
