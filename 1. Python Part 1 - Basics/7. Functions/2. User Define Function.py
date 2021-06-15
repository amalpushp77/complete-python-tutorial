def add():
    a = int(input("Enter a number: "))
    b = int(input("Enter a number: "))

    c = a + b
    print(c)


#calling a function add
add()


# for num in range(2, 100):
#     for i in range(2, num):
#         if num%i==0:
#             break
#     else:
#         print(num)

n = 8
sq = ((2*8+1)*(n)*(n+1))/6
print(sq)


# without parameter and without return type

##def add():
##
##    c = a+b
##    print(c)
##
##
##a = int(input("Enter a number: "))
##b = int(input("Enter a number: "))
##
##
###calling a function add
##add()


# with parameter and without return

##def sub(m,n):  #dummy variables m,n
##
##    s = m-n
##    print(s)
##
##a = int(input("Enter a number: "))
##b = int(input("Enter a number: "))
##
##x = sub(a,b)
##print(x)
##print(type(x))

# with parameter and with return

##def mul(m,n):
##
##    s = m*n
##    return s
##
##a = int(input("Enter a number: "))
##b = int(input("Enter a number: "))
##
##x = mul(a,b)
##print(x)
##print(type(x))

# without parameter and with return

##def div():
##
##    s = m/n
##    return s
##
##m = int(input("Enter a number: "))
##n = int(input("Enter a number: "))
##
##x = div()
##print(x)
##print(type(x))

##WAF to return a list of odd numbers between 1 and 100

##def odd_list():
##
##    l = []
##    #index = 0
##    for i in range(1,101):
##        if i%2==1:
##            #i%2!=0
##            #i%2
##            #range(1,101,2)
##
##            l.append(i)
##
##            #l.insert(index,i)
##            #index+=1
##
##    return l
##
##print(odd_list())


##WAF to return a list of even numbers by user defined range

##def even_list():
##    start = int(input("Initial value: "))
##    stop = int(input('Last exclusive value: '))
##    l = []
##    #index = 0
##    for i in range(start,stop):
##        if i%2==0:
##            #i%2!=1
##
##            l.append(i)
##
##            #l.insert(index,i)
##            #index+=1
##
##    return l
##
##print(even_list())

# WAF to return even and odd list of numbers by user define range

def even_odd_number():
    '''
    returns a list of even and odd numbers within a range.'''

    even_list = []
    odd_list = []

    initial = int(input("enter initial range: "))
    final = int(input("enter finanl range: "))

    for i in range(initial, final + 1):
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)

    return even_list, odd_list


a, b = even_odd_number()
print(a)
print(b)

print(dir())
print(help(even_odd_number))

# WAF that checks whether a number is in a given range

##def isrange(value):
##    print('function is called')
##    i = 10
##    f = 100
##
##    if i<value<f:
##        #print(True)
##        return True
##    else:
##        #print(False)
##        return False
##
##print("1st line that executed")
##x = int(input("Enter a number to check whether in range or not: "))
##print('before function call')
##result = isrange(x)
##print(result)

# WAF that accepts a string and calculate the number of uppercase letters and lowercase letters

##def count_case(string):
##    u_count = 0
##    l_count = 0
##    for i in string:
##        if i.isupper():
##            u_count+=1
##        else:
##            l_count+=1
##
##    return u_count,l_count
##
##s = input("Enter a string: ")
##u,l = count_case(s)
##print(u)
##print(l)


# User Define Parameterized functions

#Compulsory parameter

##def make_list(a,b,c,d):  #dummy variables (arguments)
##    l = []
##    l.append(a)
##    l.append(b)
##    l.append(c)
##    l.append(d)
##
##    return l
##
##m = 32
##n = 43
##o = 123
##p = 445
##q = 123
##r = 4321
##s = 12345
##t = 192387
##
##x = make_list(m,n,o,p) #actual values (parameter)
##print(x)
##
##y = make_list(p,q,r,s)
##print(y)
##
##z = make_list(t,s,r,q)
##print(z)

##Default (optional) parameter
##def make_list(a,b,c=0,d=0):
##    l = []
##    l.append(a)
##    l.append(b)
##    l.append(c)
##    l.append(d)
##
##    return l
##
##m = 32
##n = 43
##o = 123
##p = 445
##q = 123
##r = 4321
##s = 12345
##t = 192387
##
##x = make_list(m,n,o)
##print(x)
##
##y = make_list(p,q,r,s)
##print(y)
##
##z = make_list(t,s,r,q)
##print(z)

#unknown number of arguments

##def create_list(*arg):
##    return [*arg]
##
##l = create_list(1,2,3,4,5,6,4)
##print(l)
##
##def add(*arg):
##    return sum(arg)
##
##a = add(1,2,3,4,5,6,4)
##print(a)

#unknown number of arguments with default values

##def pair(**k):
##    print(k)
##
##pair(a=3,b=4,asdf=1234)
##
