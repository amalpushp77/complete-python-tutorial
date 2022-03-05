class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def to_str(self):
        return 'Rectangle (width={0}, height={1})'.format(self.width, self.height)

    # def __str__(self):
    #     return 'Rectangle (width={0}, height={1})'.format(self.width, self.height)

    # def __repr__(self):
    #     return 'Rectangle({0}, {1})'.format(self.width, self.height)

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return (self.width, self.height) == (other.width, other.height)
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented


r1 = Rectangle(10, 20)
print(r1.area())
print(r1.perimeter())


str(10)
str(r1)

# r1.to_str()

print(r1)


r1 = Rectangle(100, 200)
r2 = Rectangle(10, 20)
print(r1 < r2)
print(r1 > r2)
print(r1 <= r2)