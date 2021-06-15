#Slicing [start:end+1]
lst = [1,2,3,4,5,6,7,8,9,0]

#Forward index slicing
print(lst[0:4])
print(lst[6:9])

#Backward Index Slicing
print(lst[-10:-6])

#Stepwise Slicing [start:end+1:step]
print(lst[0::2])

print(lst[0:6:3])

#Reverse
print(lst[-1:-11:-1])
print(lst[::-1])


#Reverse a string
string = "Hello World!"
print(string[::-1])


##a = "Hello World"
##print('To reverse complete string:',a + ' to', a[::-1])
##print('To reverse only:', a[0:5],'to', a[4::-1])
##print('Similarly reverse', a[6:],'to', a[10:5:-1])