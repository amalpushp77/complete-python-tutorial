# class variable vs instance variable, accessing outside of class
# note - data member of class variable will be same for all object by default

class Variable:
    class_variable = 40

    def func(self, instance_variable):
        self.instance_variable = instance_variable
        self.class_variable = self.instance_variable


v1 = Variable()
v2 = Variable()

print('before calling method func()')

print('class_variable of v1:', v1.class_variable)
# print('instance_variable v1:', v1.instance_variable)

print('class_variable of v2:', v2.class_variable)
# print('instance_variable v2:', v2.instance_variable)

v1.func(10)
v2.func(20)

print('after calling method func()')

print('class_variable of v1:', v1.class_variable)
print('instance_variable v1:', v1.instance_variable)

print('class_variable of v2:', v2.class_variable)
print('instance_variable v2:', v2.instance_variable)
