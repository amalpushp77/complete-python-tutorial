
# Function overriding - same function with different functionality
# https://www.geeksforgeeks.org/method-overriding-in-python/


class Base_Class:
   def __init__(self):
       print('Base class created')

   def override(self):
       print('Base class override')

class Derived_Class(Base_Class):
   def __init__(self):
       super().__init__()
       print('Derived class created')

   def override(self):
       #super().override()
       print('Derived class override')

print('MRO', Derived_Class.__mro__, sep='\n')

d = Derived_Class()
d.override()


# Polymorphism

class India():
    def capital(self):
        print("New Delhi is the capital of India.")

    def language(self):
        print("Hindi the primary language of India.")

    def type(self, value):
        print("India is a developing country.", value)


class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA.")

    def language(self):
        print("English is the primary language of USA.")

    def type(self, value):
        print("USA is a developed country.", value)


def common_method(obj):
    obj.capital()
    obj.language()
    obj.type(4)


i = India()
u = USA()

common_method(i)
common_method(u)
