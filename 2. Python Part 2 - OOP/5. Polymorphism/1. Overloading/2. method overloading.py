# Method Overloading - same function with different parameters

class Point:
    def set_coordinate(self, x=None, y=None, z=None):
        if x is None and y is None and z is None:
            self.x = 0
            self.y = 0
            self.z = 0
        else:
            self.x = x
            self.y = y
            self.z = z

    def __str__(self):
        if self.z is None:
            return '({},{})'.format(self.x, self.y)
        else:
            return '({},{},{})'.format(self.x, self.y, self.z)


xyz_origin = Point()
xyz_origin.set_coordinate()
print(xyz_origin)

xy_origin = Point()
xy_origin.set_coordinate(0,0)
print(xy_origin)

xy_point = Point()
xy_point.set_coordinate(1,2)
print(xy_point)

xyz_point = Point()
xyz_point.set_coordinate(1,2,3)
print(xyz_point)
