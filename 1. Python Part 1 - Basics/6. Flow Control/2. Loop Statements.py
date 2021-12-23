# loops in python

# for loop
# while loop

for i in range(10):
    print('good morning')

for i in range(10):
    print(i)

for i in range(1, 10):
    print(i)

for i in range(1, 10, 2):
    print(i)

# for loop with else statement
for i in range(30):
    print(f'i is now {i}')
    if i == 30:  # try changing range(20) to range(30)
        print('for loop break at i =', i)
        break
else:
    print('else statement will only execute when for loop will run properly i.e without break')

print("Outside for loop")

# while loop
i = 0
while i < 11:
    print(i)
    i = i + 1  # update statement


# while loop with else statement
i = 20
while i >= 0:
    print('value of i is:', i)
    if i == 7:
        print('while loop break at i =', i)
        break
    i -= 2  # change i -= 2 to i -= 1
else:
    print('else statement will only execute when while loop will run properly i.e without break')

# using iterable data types
# string
count = 0
for i in 'abc':
    count += 1
    # the variable 'i' contains the value of last iteration
    print(count, 'iteration value:', i)
    # print(i)
# list
count = 1
for i in [1, 2, 3.4, 'abc', [1, 2, 3]]:
    print(count, 'iteration value:', i)
    count += 1


# range(value)
count = 0
for i in range(10):
    count += 1
    print("Value of i at iteration", count, 'is:', i)

# range(start,stop)
count = 0
for i in range(2, 11):
    count += 1
    print("Value of i at iteration", count, 'is:', i)

# range(start,stop,range)
count = 0
for i in range(2, 20, 2):
    count += 1
    print("Value of i at iteration", count, 'is:', i)

# create list using range function
print(list(range(1, 101)))

# Reverse
count = 0
for i in range(20, 0, -1):
    count += 1
    print("Value of i at iteration", count, 'is:', i)

# enumerate()
count = 0
for index, value in enumerate('abc'):
    count += 1
    print("Value at index", index, "of iteration", count, 'is:', value)

# ctrl+c Keyboard interrupt to stop infinite loop
n = 5
while n >= 1:
    print("123")

    # update statement
    n += 1  # n -= 1 for infinite loop

# fibonacci series - 0,1,1,2,3,5,8,...
a = 0
b = 1

while b < 100:
    print(a, end=' ')

    # update statement
    a, b = b, a + b

    # a = b
    # b = a+b
