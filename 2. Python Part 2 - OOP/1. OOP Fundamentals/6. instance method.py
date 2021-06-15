# instance method, using class and instance variable inside of class

class Circle:
    pi = 3.14

    def set_radius(self, radius=1):
        self.radius = radius

    def circum(self):
        return 2 * Circle.pi * self.radius

    def area(self):
        return Circle.pi * (self.radius ** 2)


c1 = Circle()
c1.set_radius(10)
print('Circumference:', c1.circum())
print('Area:', c1.area())

# print(Circle.pi)
Circle.pi = 3.1415926535
c1.radius = 100
# print(Circle.pi)
print()
print('Circumference:', c1.circum())
print('Area:', c1.area())
