# __del__
import sys


class Object:
    def __init__(self):
        print('object is created')

    def __del__(self):
        print('object is deleted')


a = Object()

print(sys.getrefcount(a))

del a
