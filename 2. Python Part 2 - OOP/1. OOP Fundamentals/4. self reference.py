# understanding the use of self(reference/instance)
# The self-parameter refers to the current instance of the class and accesses the class variables.

class A:

    def get_A(self):
        print('calling get_A method')


a = A()
a.get_A()

print('Another way of doing it')

b = A()
A.get_A(b)
