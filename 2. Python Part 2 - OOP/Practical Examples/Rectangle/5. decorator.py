class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self.width, self.height)

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive.')
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height <= 0:
            raise ValueError('Height must be positive.')
        self._height = height


r1 = Rectangle(100, 20)
r1.width = 10
print(r1.width)