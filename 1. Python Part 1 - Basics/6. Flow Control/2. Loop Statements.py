# loops in python

# for loop
# while loop

# for i in range(100):
#     print('good morning')

# for i in range(10):
#     print(i)

# for i in range(1,10):
#     print(i)

# for i in range(1,10,2):
#     print(i)

#for loop with else statement
##for i in range(20):
##    print('i is now {}'.format(i))
##    if i == 25:  #try changing range(20) to range(30)
##        print('for loop break at i =',i)
##        break
##else:
##    print('else statement will only execute when for loop will run properly i.e without break')


# while loop
i=0
while i<11:
    print(i)
    i = i + 1   # update statement

#while loop with else statement
##i = 20
##while i>=0:
##    print('value of i is:',i)
##    if i == 7:
##        print('while loop break at i =',i)
##        break
##    i -= 1  #change i -= 2 to i -= 1 i = i-2
##else:
##    print('else statement will only execute when while loop will run properly i.e without break')


##count = 0
##for i in 'abc':
##    count+=1
##    print(count,'iteration value:',i)

# the variable 'i' will contain the value of last iteration

count = 1
for i in [1, 2, 3.4, 'abc', [1, 2, 3]]:
    print(count, 'iteration value:', i)
    count += 1

# range(value)

##count = 0
##for i in range(10):
##    count+=1
##    print("Value of i at iteration", count, 'is:', i)

# range(start,stop-1)

##count = 0
##for i in range(2,11):
##    count+=1
##    print("Value of i at iteration", count, 'is:', i)

# range(start,stop-1,range)

##count = 0
##for i in range(2,20,2):
##    count+=1
##    print("Value of i at iteration", count, 'is:', i)

# Reverse
##count = 0
##for i in range(20,0,-1):
##    count+=1
##    print("Value of i at iteration", count, 'is:', i)

# enumerate()

##count = 0
##for index,value in enumerate('abc'):
##    count+=1
##    print("Value at index",index, "of iteration", count, 'is:', value)


# ctrl+c Keyboard interept to stop infinte loop

##n=5
##while n>=1:
##    print("123")
##
##    #update statement
##    n-=1

###1,1,2,3,5,8,...
##a = 1
##b = 1
##
###Less than 1000
##while b<1000:
##    print(a,end=' ')
##
##    #update statement
##    a,b = b,a+b
##
##    #a = b
##    #b = a+b

# print 10th value

##
##for i in (1,2,3,4,5,6,7,8,9,10):
##    for j in (10,9,8,7,6,5,4,3,2,1):
##        print('{}*{} ='.format(i,j),i*j)

##for i in range(1,11):
##    n1 = i
##    n2 = 11 - i
##    #print('{}*{} ='.format(n1,n2),n1*n2)
##    print(n1,'*',n2,'=',n1*n2)

##i=[1,2,3,4,5,6,7,8,9,10]
##j=[10,9,8,7,6,5,4,3,2,1]
##
##for index in range(10):
##    print(i[index],'*',j[index],'=',i[index]*j[index])

##l = [1,2,3,4,5,6,7,8,9,10]
##
##for index in range(10):
##    n1 = l[index]
##    n2 = l[9-index]
##
##    print(n1*n2)


#range in ascending order
##for i in range(-5,6):
##    print('i is now {}'.format(i))

#range in reverse order
##for i in range(5,-6,-1):
##    print('i is now {}'.format(i))


# for loop

# string
##s = 'Hello World'
##count = 1
##
##for i in s:
##    print('At iteration',count,'value of i is:',i)
##    count +=1

# list
##l = ['a','b','65','78',[1,2,3],'Hello World']
##
##for i in l:
##    print('At iteration', count,'value of i is:',i)
##    count +=1

# convert string datatype into list
##print(list(s))

# create list using range fuction
##print(list(range(1,101)))

# enumerate function returns index with value
# string
##s = 'Hello World'
##for index,value in enumerate(s):
##    print("Index of",value,"is:", index)

# list
##l = ['a','b','65','78',[1,2,3],'Hello World']
##for index,value in enumerate(l):
##    print("Index of",value,"is:", index)

# Index of every element, even for nested index
##l = ['a', 'b', '65', 54, '78', 67.46788, [1,2,3], 'Hello World', 7-3.8j, (4,5,6,7,8)]
##
##for index, value in enumerate(l):
##
##    print("Index of",value,"is:", index)
##    if type(value) != int and type(value) != float and type(value) != complex:
##        if len(value) > 1:
##            print('*'*10)
##            for nested_index, nested_value in enumerate(value):
##                print("Index of",nested_value,"is:", nested_index)
##    print('='*30)
