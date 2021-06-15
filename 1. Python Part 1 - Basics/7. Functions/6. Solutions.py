# 1. WAP for calculator using functions
def add(x,y):
    c = x+y
    return c

def sub(a,b):
    c = a-b
    return c

def multiply(a,b):
    c = a*b
    return c

def div(a,b):
    c = a/b
    return c

print("enter the operator")
print("1.Add")
print("2.sub")
print("3.multi")
print("4.div")

operator= (input("1/2/3/4"))

num1=int(input("enter 1st number"))
num2=int(input("enter 2nd number"))

if operator=="1":
    #print(add(num_1,num_2))
    print(num1,"+",num2,"=", add(num1,num2))

