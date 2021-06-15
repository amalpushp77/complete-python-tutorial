# generators - produces values
# coroutines - consume values, not for iterations

""" Coroutine is used for
        1. Repeatedly receives input
        2. Processes input
        3. stops at yield statement"""

# function - it's the same function each time it is called
# coroutine - persistent properties can be changed and altered

# send() method

""" yield in coroutine
        1. Pauses flow
        2. captures sent values"""


def coroutine_example():
    while True:
        x = yield
        #do something with x
        print(x)


c = coroutine_example()
next(c)
c.send(10)

def counter(string):
    count = 0
    try:
        while True:
            item = yield
            if isinstance(item, str):
                if item in string:
                    count += 1
                    print(item)
                else:
                    print('No Match')
            else:
                print('Not a string')
    except GeneratorExit:
        print(count)

c = counter("Maharashtra")
next(c)
c.send("Mah")
c.send("tra")
c.send("nag")
c.close()

