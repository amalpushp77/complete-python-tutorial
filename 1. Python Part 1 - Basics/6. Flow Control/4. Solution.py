# 1. WAP to find the largest of 2 numbers taken from user
##num1=input("enter number A")
##num2=input("enter number B")

##if num1>num2:
##    print("Largest number is: ", num1)
##else:
##    print("Largest number is: ", num2)


##if num1>num2:
##    print("Largest number is: ", num1)
##
##if num2>num1:
##    print("Largest number is: ", num2)
##else:
##    print("Largest number is:", num1)

# 2. WAP to find the largest and smallest of 3 numbers taken from user
num1 = int(input('Enter First number : '))
num2 = int(input('Enter Second number : '))
num3 = int(input('Enter Third number : '))

# to find the largest number
##if (num1 > num2) and (num1 > num3):
##    print ("The largest of the 3 numbers is : ", num1)
##elif (num2 > num1) and (num2 > num3):
##    print ("The largest of the 3 numbers is : ", num2)
##else:
##    print ("The largest of the 3 numbers is : ", num3)
##
### to find the smallest number
##if (num1 < num2) and (num1 < num3):
##    print ("The smallest of the 3 numbers is : ", num1)
##elif (num2 < num1) and (num2 < num3):
##    print ("The smallest of the 3 numbers is : ", num2)
##else:
##    print ("The smallest of the 3 numbers is : ", num3)

##a = int(input('enter a: '))
##b = int(input('enter b: '))
##c = int(input('enter c: '))
##
##if a>b>c or a>c>b:
##    print("Largest number is ",a)
##elif b>a>c or b>c>a:
##    print('Largest number is ', b)
##else:
##    print('Largest number is ', c)


# to find the largest and smallest number
if num1 > num2 > num3 or num1 > num3 > num2:
    print("Largest number is:", num1)
    if num2 > num3:
        print("Smallest number is:", num3)
    else:
        print("Smallest number is:", num2)
elif num2 > num1 > num3 or num2 > num3 > num1:
    print("Largest number is:", num2)
    if num1 > num3:
        print("Smallest number is:", num3)
    else:
        print("Smallest number is:", num3)
else:
    print("Largest number is:", num3)
    print("Smallest number is:", num1)

### 3. Print multiplication table of 14 from a list in which multiplication table of 12 is stored.
##count = 1
##for i in [12,24,36,48,60,72,84,96,108,120]:
##    print(i+2*count)
##    count+=1

# 4. Using range(1,101), print all numbers which are divisible bt 5
##for i in range(1,101):
##    if(i%5==0):
##        print(i)

# display only numbers

##number = '9,452,798,132,546,500'
##
##for i in range(0,len(number)):
##    if number[i] in '0123456789':
##        print(number[i])