# String
# String can have double inverted commas "abc" or single inverted comma 'abc'
# + operator is used to concatenate strings
# * operator is used to repeat whole string

s = "Hello World"
print("Datatype stored in variable s is ", type(s))

# concatenate two strings, single parameter to function print
without_space = "hello" + "world"
with_space = "hello" + " " + "world"
print(without_space)
print(with_space)

""" understanding print function
    earlier we used one parameter to print function, now we are using two parameters
    what is a parameter? -> any value given to the function is a parameter
    for ex - in above statement with_space is a parameter to print() function
"""

a1 = "hello"
a2 = "world"

print(a1, a2)  # adding parameters to print function adds a space in between them
# you can use infinite number of parameters in print() function

print("hello " * 3)  # for printing same word three times
# print("aditya" * "patro") # TypeError: can't multiply sequence by non-int of type 'str'
print("aditya" + "patro")  # concatenation of string datatype
# print("hello"+3) # TypeError: can only concatenate str (not "int") to str


# Escape Sequence
t = 'what\'s your name?'
print(t)

string = 'what is \n your name?'  # \n -> for next line
print(string)

# double quote string
c = "he said,\"what's there?\""  # use of escape sequence \' \" \n
print(c)

# single quote string
d = 'he said,"what\'s there?"'
print(d)

# Suppress Escape sequence
# notice \n is escape sequence , try removing r before string and run the program
link = r'C:\asd\sdfsd\cvaswfvs\new folder\python'
print(link)


# String formatting
age = int(input("Enter your age: "))
sentence = f"My age is {age}"
print(sentence)


# Input function return type
a = input("enter your name: ")  # take input from user, return type of input function is string
print(type(a))

# concatenation of strings using +
name = input("Enter your name: ")
# print("User entered: " + name)
print("User entered: ", name)

# when you want to form a sentence using different datatype avoid using +, instead of this you can use string
# formatting (recommended) or use datatype as print parameters
age = int(input("Enter your age: "))
print(type(age))

# using print function with parameters
print("Hi", name, ",are you", age, "years old?")

# using string formatting
print(f"Hi {name}, are you {age} years old?")

# age += 10   #
age = age + 10
print("Your age after 10 years will be ", age)
