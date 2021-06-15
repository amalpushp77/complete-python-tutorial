# Encapsulation / Data abstraction is acheived using access moodifiers
# https://www.javatpoint.com/abstraction-in-python

class Encapsulate:
   a = 10   #public
   _a = 20  #protected
   __a = 30 #private

e = Encapsulate()
print(e.a)
print(e._a)
#print(e.__a)

class Encapsulate:
   def __init__(self,a,_a,__a):
       self.a = a
       self._a = _a
       self.__a = __a

   def get_value(self):
       return self.__a

   def set_value(self,val):
       self.__a = val

e = Encapsulate(1,2,3)
print(e.a)
print(e._a)
#print(e.__a)
print()
print('Accessing __a using method')
print(e.get_value())
print()
print('Setting value of __a using method i.e inside the class')
e.set_value(7)
print(e.get_value())
print()
print('Setting value of __a outside of class \ni.e e.__a = 10')
e.__a = 10
print(e.get_value())
print('Unchanged')

class Encapsulate:
   def __init__(self):
       self.__func()
       self.func()

   def func(self):
       print('func is called')

   def __func(self):
       print('__func is called')

e = Encapsulate()
print()
print('Outside of class')
e.func()
#e.__func()