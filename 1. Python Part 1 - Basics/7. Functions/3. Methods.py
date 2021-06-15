#Important string methods

#Method: methods can be used on any datatpe
#methods are used with a dot '.' ex: 'strings'.count('s')

s = 'Hello world, python!'

#count() returns the number of any parameter (ex-alphabet or word)

##print(s.count('o'))
##print(s.count('world'))

#join() to convert any datatype to string in a representable manner

##l = ['hello','world','python']
##
####print(str(l))
##
##print(' '.join(l))

#lower() returns a string in lower case

##print(s.lower())

#upper() returns a string in upper case

##print(s.upper())

#split()

##txt = "welcome to the jungle"
##
##x = txt.split() #default value is ' '
##
##print(x)

#=======================================================================

#endswith() return a boolen whether the string ends with given value

##print(s.endswith('!'))

#startswith() return a boolen wheter the string starts with given value

##print(s.startswith('!'))

#find() | index() returns the starting index of given value, if not found it returns -1

##print(s.find())

#format()

##name = input("Enter name: ")
##age = int(input("Enter age: "))
##
##print('Hello, My name is {}. I\'m {} years old.'.format(name,age))

#islower() returns boolen True if all values is in lower case
#isupper() returns booLen True if all values is in Upper case

#replace()

##txt = "I like bananas"
##
##x = txt.replace("bananas", "apples")
##
##print(x)

#splitlines()

##txt = "Thank you for the music\nWelcome to the jungle"
##
##x = txt.splitlines()
##
##print(x)




#append() add an element to the list

fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")

print(fruits)


#clear() delete all elements from list

##fruits.clear()
##print(fruits)

#copy() create different memory for same elements

##another_fruits = fruits.copy()
##
##another_fruits.append('mango')
##
##print(another_fruits)
##print(fruits)

#count() Return the number of times the value appeared in list

##x = fruits.count("cherry")
##print(x)

#extend()

##cars = ['Ford', 'BMW', 'Volvo']
##
##fruits.extend(cars)
##
##print(fruits)

#index()

##x = fruits.index("cherry")
##print(x)

##index = 0
##for i in fruits:
##    if i=='cherry':
##        break
##    index+=1
##print(index)

#insert()

#fruits.insert(1, "orange")

#pop(index = -1)

##fruits.pop(1)
##print(fruits)

#remove(value)
##fruits.remove("banana")

#reverse()
#fruits.reverse()

#sort()
##fruits.sort()





#count() Returns the number of times a specified value occurs in a tuple

##thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
##
##x = thistuple.count(5)
##
##print(x)


#index() Searches the tuple for a specified value and returns the position of where it was found

##thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
##
##x = thistuple.index(8)
##
##print(x)




#fromkeys() Returns a dictionary with the specified keys and value

##x = ('a', 'b', 'c')
##y = 0
##
##thisdict = dict.fromkeys(x, y)
##
##print(thisdict)

#get() Returns the value of the specified key

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
  }


##x = car.get("model")
##y = car['model']
##
##print(x)
##print(y)

#items() Returns a list containing a tuple for each key value pair

##x = list(car.items())
##
##print(x)


#keys() Returns a list containing the dictionary's keys

x = list(car.keys())

print(x)


#values() Returns a list of all the values in the dictionary

y = list(car.values())

print(y)

#setdefault()Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
x = car.setdefault("model", "Bronco")

print(x)

#update() Updates the dictionary with the specified key-value pairs

#car.update({"color": "White"})
car['brand3'] = 'white'
print(car)
