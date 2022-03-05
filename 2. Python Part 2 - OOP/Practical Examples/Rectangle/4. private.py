class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)


r1 = Rectangle(100, 20)
print(r1._width)
print(r1._height)
