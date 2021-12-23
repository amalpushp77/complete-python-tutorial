"""
    # https://www.informit.com/articles/article.aspx?p=453682&seqNum=6
    # https://dbader.org/blog/python-dunder-methods#:~:text=In%20Python%2C%20special%20methods%20are,__%20or%20__str__%20.
    # https://diveintopython3.net/special-method-names.html
    # https://www.tutorialsteacher.com/python/magic-methods-in-python
    # https://rszalski.github.io/magicmethods/"""


# Constructors are special methods which are used to initialise the members of a class at the time of instantiation
# 1. Parameterized Constructor
# 2. Non-parameterized Constructor

# if there are more than 1 constructor in a class, the last constructor will get executed

# __init__()

class Object:
    def __init__(self):
        print('Object created')


a = Object()
print(a)
print(type(a))


# copy constructor
class Point:
    def __init__(self, x, y=None, z=None):
        if isinstance(x, Point):
            self.x = x.x
            self.y = x.y
            self.z = x.z
        else:
            self.x = x
            self.y = y
            self.z = z

    def __str__(self):
        if self.z is None:
            return '({},{})'.format(self.x, self.y)
        else:
            return '({},{},{})'.format(self.x, self.y, self.z)


p1 = Point(1, 2)
print(p1)
p2 = Point(p1)
print(p2)
