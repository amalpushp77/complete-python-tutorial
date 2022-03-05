class Rectangle:
    def __init__(self, width, height):
        self._width = None
        self._height = None
        # now we call our accessor methods to set the width and height
        self.width = width
        self.height = height

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