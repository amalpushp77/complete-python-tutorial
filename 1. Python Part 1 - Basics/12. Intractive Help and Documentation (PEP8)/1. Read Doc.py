import math
import os
import requests


# (...)
#  =   (optional argument/default value)
# -->  function returns value
# *iterables

#dir()
#help()

#print(dir(math))
#print(help(math.acos))


#print(dir(os))

#print(os.getenv('PROCESSOR_ARCHITECTURE'))


print(dir(requests))


#Interactive Help
#dir()   #shows all the availabe modules with their fucntions and methods
#dir(__builtins__) #__builtins__ module contains in built functions like print() input() int() round() and many more
#help(__builtins__.print) # view the documentation on in built function print

##print(help('modules'))   #view the name of all libraries that you can use in python


##l = []
##print(l)
##print(type(l))   #type of variable l is list
##print(dir())     #notice l is added to the list
##print(dir(l))    #you wil find append method inside 'l'