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
    for ex - on line 13 with_space is a parameter to print() function
"""
a1 = "hello"
a2 = "world"
print(a1, a2)  # adding parameters to print function adds a space in between them
# you can use infinite number of parameters in print() function

#print("hello "*3) #for printing same word three times
#print ("hello"+3) #it will give error because we can add only two string data types we cannot add one integer and one string datatype


#Escape Sequence
t = 'what\'s your name'
print(t)

string = 'what is \n your name?'
print(string)

#c = "he said,\"what's there?\""  #use of escape sequence \' \" \n
#print(c)

#d = 'he said,"what\'s there?"'
#print(d)

#Supress Escape sequence

# notice \n is escape sequence , try removing r before string and run the program
link = r'C:\asd\sdfsd\cvaswfvs\new folder\python'
print(link)

#Input

#a = input("enter your name:") #take input from user, by default datatype of input is string
#print(a)

##i = input("Enter your name: ")
##print("User entered: " + i)
##
##num = int(input("Enter your age: "))
##print("Your age at present is" , num, "asdasdas", i)
##
##print(type(num))
###num += 10
##num = num +10
##print("Your age after 10 years will be " , num)

# format method
print('hello {a} {s} . welcome to {c}'.format(a='jay',s='d',c='rcoem')) #format method
first_name = input("enter the first name: ")
last_name = input("enter the surname: ")
college_name=input("enter the university: ")
print('hello {} {}welcome to {}'.format(first_name,last_name,college_name))