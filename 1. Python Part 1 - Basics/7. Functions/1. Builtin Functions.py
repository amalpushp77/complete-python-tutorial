# https://www.w3schools.com/python/python_ref_functions.asp

""" A funtion is a block of code which only runs when it is called.
        Types of Functions
        1) Built in functions
        2) User define fuction
        3) Methods (fuctions which is a part of a class)
        4) Anonymous function  """


a = 'abcd'
print(len(a))

#Built-in Functions

#Important function

#dir() returns an object's attribute

#range()
#enumerate() returns index,value pair of itreable objects

#help() return the documentation
#print(help(print))

#input() returns a string

#len() returns the length of object

#print(len('abcd'))


# print()
#print("hello","world") #concatinate two strings, two parameter to function print
#print(sep=' ')
#print('amal'+'pushp','hello')

#print(end='\n')
##print('hello', end=' ')
##print('world')
##print('abc')


#all type casting functions
'''
int()
str()
float()
complex()
list()
tuple()
set()
dict()
'''

#filter()

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = list(filter(myFunc, ages))

print(adults)


#map()

ages = [5, 12, 17, 18, 24, 32]

def myFunc(x):
  if x < 18:
    return False
  else:
    return True

adults = list(map(myFunc, ages))

print(adults)

#zip()

name = ['abc','def','ije']
age = [23,34,24]
marks = (45,55,56)

sheet = list(zip(name,age,marks))   # tips n trick with for loop
print(sheet)
#========================================================================================
#Functions

#ascii() returns a value to non ascii character
#print(type(ascii('ș')))

#chr() returns the character
#print(chr(67))

#max() returns maximum value
#min() returns minimum value

#open()

#ord() returns an integer that represents Unicode

#sorted() returns a sorted object

#iter()
#next()

#==========================================================================================
# other functions

# round()
#print(round(758.12856,3)) #example of round

#==========================================================================================
#Related to class

#classmethod()
#delattr()
#getattr()
#hasattr()
#setattr()
#hash()
#property()
#id()
#isinstance()
#issubclass()
#object()
#staticmethod()
#super()
