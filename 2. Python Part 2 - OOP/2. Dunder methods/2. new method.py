# __new__()

class Object:
   def __new__(self):
       print('Object created with return type')

a = Object()
print(a)
print(type(a))