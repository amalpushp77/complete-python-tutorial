
# Inheritance
# note - base/parent/super class should be define first
# https://www.geeksforgeeks.org/inheritance-in-python/
# https://www.javatpoint.com/inheritance-in-python

class Parent:
   def __init__(self):
       print('object of class Parent is initialized')

   def baap(self):
       print('rishte me hum tumhare baap lgte h')

class Child(Parent):
   def __init__(self):
       #super().__init__()
       print('object of class Child is initialized')

   def friends(self):
       print('friends of Child class')


c = Child()
c.baap()

#multiple inheritance

class A:
   def __init__(self):
       print('A created')

class B:
   def __init__(self):
       print('B created')

class C(B,A):
   def __init__(self):
       #super().__init__()
       A.__init__(self)
       B.__init__(self)
       print('C created')

c = C()
print('*'*20)
print('Method Resolution Order')
print(C.__mro__)

#multi-level inheritance

class A:
   def __init__(self):
       print('A created')

   def grandpa(self):
       print('baapo ke baap')

class B(A):
   def __init__(self):
       super().__init__()
       print('B created')

   def baap(self):
       print('bosss')

class C(B):
   def __init__(self):
       super().__init__()
       #A.__init__(self)
       #B.__init__(self)
       print('C created')

c = C()
c.baap()
c.grandpa()
print('*'*20)
print('isinstance(c,A)? ', isinstance(c,A))
print('isinstance(c,B)? ', isinstance(c,B))
print('isinstance(c,C)? ', isinstance(c,C))
print()
print('issubclass(A,A)? ', issubclass(A,A))
print('issubclass(A,B)? ', issubclass(A,B))
print('issubclass(A,C)? ', issubclass(A,C))
print('issubclass(B,A)? ', issubclass(B,A))
print('issubclass(C,A)? ', issubclass(C,A))
print('issubclass(C,B)? ', issubclass(C,B))

print('*'*20)
print('Method Resolution Order')
print(C.__mro__)