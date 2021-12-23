# Scope of variable

def func():
    x = 20  # local variable

    print('Value of x inside fuction: ', x)


func()
x = 10
print("Outside of function, value of x: ", x)


print('Value of x after calling function: ', x)


def func():
    print('Value of x inside fuction: ', x)


x = 10  # global variable
print("Outside of function, value of x: ", x)
func()

print('Value of x after calling function: ', x)


def func():
    global x  # global variable
    x = 20

    print('Value of x inside fuction: ', x)


x = 10
print("Outside of function, value of x: ", x)
func()

print('Value of x after calling function: ', x)
