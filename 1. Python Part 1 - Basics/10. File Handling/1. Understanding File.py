#File Handling
#For more info on in built function open() read documentation -> help(open)

#Opening and reading file
##file = open('example.txt', 'r')

##print(type(file))

#Available methods on file
##print(dir(file))

#Read the contents of the file that you open
##content = file.read()             #read() method reads the complete content of file and move the cursor to the end
##print(content)

#move the cursor to the beginning of file
##file.seek(0)

#readlines() method returns a list containing each line as an element
##line = file.readlines()
##file.close()              #always close the file when done working on it
##print(line)
##
##line = [i.rstrip('\n') for i in line]     #rstrip() is a string method used to remove trailing spaces or characters
##
##print(line)


#Opening and writing on file
#'w' parameter can create that file if not exist
##file = open('example_1.txt', 'w')
##
##file.write('Hello')       #'w' on existing file can overwrite the pre-contents
##
##file.close()             #always close the file when done working on it


#Opening and writing on file using append 'a' parameter
##file = open('example.txt', 'a')
##
##file.write('\nLine 4')
##
##file.close()             #always close the file when done working on it



#Pythonic way to open a file using with statement
#with statement automatically close the file when done working on it

##with open('example.txt', 'a') as file:
##    file.write('\n'+'Hello World')


#WAF writer() using with statement that takes list of temperature as input and creates a text file 'temps.txt'. Store the temperature in Fahrenheit
##def writer(temp_list):
##
##    with open('temps.txt', 'w') as file:
##        for celcius in temp_list:
##            f = celcius * (9/5) + 32
##            file.write(str(f) + '\n')
##
##
##cel = [-50, 0, 10, 20, 37, 50]
##
##writer(cel)






















