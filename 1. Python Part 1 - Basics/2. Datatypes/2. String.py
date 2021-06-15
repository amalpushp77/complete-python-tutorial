# String
# String can have double inverted commas "abc" or single inverted comma 'abc'
# + operator is used to concatenate strings
# * operator is used to repeat whole string

s = "Hello World"
print(type(s))

a = "hello "+"world"  # concatenate two strings, single parameter to function print
print(a)

#print("hello"+" "+"world") #concatinate three strings, single parameter to function print

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