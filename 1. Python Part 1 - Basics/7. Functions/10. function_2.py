# function introspection
def fact(n: "some non-negative integer") -> "n! or 0 if n < 0":
    """Calculates the factorial of a non-negative integer n

    If n is negative, returns 0.
    """
    if n < 0:
        return 0
    elif n <= 1:
        return 1
    else:
        return n * fact(n - 1)


# Since functions are objects, we can add attributes to a function:
fact.short_description = "factorial function"
print(fact.short_description)

print(dir(fact))

print(fact.__doc__)
print(fact.__annotations__)

def my_func(a, b=2, c=3, *, kw1, kw2=2, **kwargs):
    pass

f = my_func
print(f.__name__)
print(my_func.__defaults__)
print(my_func.__kwdefaults__)


def my_func(a, b=1, *args, **kwargs):
    i = 10
    b = min(i, b)
    return a * b


print(my_func('a', 100))
print(my_func.__code__)
print(dir(my_func.__code__))
print(my_func.__code__.co_varnames)
print(my_func.__code__.co_argcount) # number of argument


# inspect module
import inspect

# A method is a function that is bound to some object
print(inspect.isfunction(my_func))
print(inspect.ismethod(my_func))


# Instance methods are bound to the instance of a class (not the class itself)
# Class methods are bound to the class, not instances
# Static methods are no bound either to the class or its instances
class MyClass:
    def f_instance(self):
        pass

    @classmethod
    def f_class(cls):
        pass

    @staticmethod
    def f_static():
        pass


print(inspect.isfunction(MyClass.f_instance), inspect.ismethod(MyClass.f_instance))
print(inspect.isfunction(MyClass.f_class), inspect.ismethod(MyClass.f_class))
print(inspect.isfunction(MyClass.f_static), inspect.ismethod(MyClass.f_static))

my_obj = MyClass()

print(inspect.isfunction(my_obj.f_instance), inspect.ismethod(my_obj.f_instance))
print(inspect.isfunction(my_obj.f_class), inspect.ismethod(my_obj.f_class))
print(inspect.isfunction(my_obj.f_static), inspect.ismethod(my_obj.f_static))

# for function or a method
print(inspect.isroutine(my_func))
print(inspect.isroutine(MyClass.f_instance))
print(inspect.isroutine(my_obj.f_class))
print(inspect.isroutine(my_obj.f_static))


# Introspecting Callable Code
print(inspect.getsource(fact))
print(inspect.getsource(fact))
print(inspect.getsource(MyClass.f_instance))
print(inspect.getsource(my_obj.f_instance))
print(inspect.getmodule(fact))
print(inspect.getmodule(print))


import math

print(inspect.getmodule(math.sin))

# setting up variable
i = 10

# comment line 1
# comment line 2
def my_func(a, b=1):
    # comment inside my_func
    pass

print(inspect.getcomments(my_func))
print(inspect.getcomments(my_func))

# Introspecting Callable Signatures

# TODO: Provide implementation
def my_func(a: 'a string',
            b: int = 1,
            *args: 'additional positional args',
            kw1: 'first keyword-only arg',
            kw2: 'second keyword-only arg' = 10,
            **kwargs: 'additional keyword-only args') -> str:
    """does something
       or other"""
    pass

print(inspect.signature(my_func))
print(type(inspect.signature(my_func)))
sig = inspect.signature(my_func)
print(dir(sig))

for param_name, param in sig.parameters.items():
    print(param_name, param)


def print_info(f: "callable") -> None:
    print(f.__name__)
    print('=' * len(f.__name__), end='\n\n')

    print('{0}\n{1}\n'.format(inspect.getcomments(f),
                              inspect.cleandoc(f.__doc__)))

    print('{0}\n{1}'.format('Inputs', '-' * len('Inputs')))

    sig = inspect.signature(f)
    for param in sig.parameters.values():
        print('Name:', param.name)
        print('Default:', param.default)
        print('Annotation:', param.annotation)
        print('Kind:', param.kind)
        print('--------------------------\n')

    print('{0}\n{1}'.format('\n\nOutput', '-' * len('Output')))
    print(sig.return_annotation)

print_info(my_func)

# positional argument

print(help(divmod))
divmod(10, 3)
divmod(x=10, y=3)

help(str.replace)
'abcdefg'.replace('abc', 'xyz')
'abcdefg'.replace(old='abc', new='xyz')


# callables - A callable is an object that can be called (using the () operator), and always returns a value.

callable(print)
callable(len)
l = [1, 2, 3]
callable(l.append)

s = 'abc'
callable(s.upper)

result = print('hello')
print(result)


l = [1, 2, 3]
result = l.append(4)
print(result)
print(l)


s = 'abc'
result = s.upper()
print(result)


from decimal import Decimal

callable(Decimal)
result = Decimal('10.5')
print(result)


class MyClass:
    def __init__(self):
        print('initializing...')
        self.counter = 0

    def __call__(self, x=1):
        self.counter += x
        print(self.counter)


my_obj = MyClass()
callable(my_obj.__init__)
callable(my_obj.__call__)

my_obj()
my_obj()
my_obj(10)

# map and filter
l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30, 40, 50]

f = lambda x, y: x+y

m = map(f, l1, l2)
list(m)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = filter(lambda x: x % 2 == 0, l)
print(list(result))

# Alternatives to map and filter using Comprehensions
# map using list comprehension
l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30, 40, 50]
result = [i + j for i,j in zip(l1,l2)]
print(result)

# fiter using list comprehension
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

result = [i for i in l if i % 2 == 0]
print(result)

# list(filter(lambda y: y < 25, map(lambda x: x**2, range(10))))
# [x**2 for x in range(10) if x**2 < 25]