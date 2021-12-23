# methods are used with a dot '.' ex: 'strings'.count('s')

# 1. Numeric datatype

# a) Integer
i = 7
print(dir(i))

# b) Float
f = 4.6
print(dir(f))

# c) complex
c = 3 + 6j
print(dir(c))


# 2. Important string methods

s = 'Hello world, python!'
print(dir(s))

# 1. count() returns the number of any parameter (ex-alphabet or word)

print(s.count('o'))
print(s.count('world'))

# 2. join() to convert any datatype to string in a representable manner

l = ['hello', 'world', 'python']

print(str(l))
print(' '.join(l))

# 3. lower() returns a string in lower case

print(s.lower())

# 4. upper() returns a string in upper case

print(s.upper())

# 5. split()

txt = "welcome to the jungle"
x = txt.split()  # default argument is ' '
print(x)

# More string methods

# 1. endswith() return a boolean whether the string ends with given value

print(s.endswith('!'))

# 2. startswith() return a boolean whether the string starts with given value

print(s.startswith('!'))

# 3. find() | index() returns the starting index of given value, if not found it returns -1

print(s.find())

# 4. format() - instead of using format method on string use format modifier f"this is a string with length {value}"

name = input("Enter name: ")
age = int(input("Enter age: "))

print('Hello, My name is {}. I\'m {} years old.'.format(name,age))

# 5. islower() returns boolen True if all values is in lower case
# 6. isupper() returns booLen True if all values is in Upper case

# 7. replace()

txt = "I like bananas"
x = txt.replace("bananas", "apples")
print(x)

# 8. splitlines()

txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
print(x)


# 3. List Methods
l = []
print(dir(l))

# 1. append() add an element to the list

fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")

print(fruits)

# 2. clear() delete all elements from list

fruits.clear()
print(fruits)

# 3. copy() create different memory for same elements

another_fruits = fruits.copy()
another_fruits.append('mango')

print(another_fruits)
print(fruits)

# 4. count() Return the number of times the value appeared in list

x = fruits.count("cherry")
print(x)

# 5. extend()

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)
print(fruits)

# 6. index()

x = fruits.index("cherry")
print(x)

# 7. insert()

fruits.insert(1, "orange")

# 8. pop(index = -1)

fruits.pop(1)
print(fruits)

# 8. remove(value)
fruits.remove("banana")

# 9. reverse()
fruits.reverse()

# 10. sort()
fruits.sort()


# 4. Tuple methods
t = ()
print(dir(t))

# 1. count() Returns the number of times a specified value occurs in a tuple

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
print(x)

# 2. index() Searches the tuple for a specified value and returns the position of where it was found

thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.index(8)
print(x)


# 5. Dictionary
d = {}
print(dir(d))

# 1. fromkeys() Returns a dictionary with the specified keys and value

x = ('a', 'b', 'c')
y = 0

thisdict = dict.fromkeys(x, y)
print(thisdict)

# 2. get() Returns the value of the specified key

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
  }


x = car.get("model")
y = car['model']   # preferable way

print(x)
print(y)

# 3. items() Returns a list containing a tuple for each key value pair

x = list(car.items())
print(x)


# 4. keys() Returns a list containing the dictionary's keys

x = list(car.keys())
print(x)

# 5. values() Returns a list of all the values in the dictionary

y = list(car.values())
print(y)

# 5. setdefault() - Returns the value of the specified key.
# If the key does not exist: insert the key, with the specified value

x = car.setdefault("model", "Bronco")
print(x)

# 6. update() - Updates the dictionary with the specified key-value pairs

car.update({"color": "White"})
car['brand3'] = 'white'
print(car)
