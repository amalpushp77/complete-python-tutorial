users = {"user1": "password",
         "user2": "qwerty123"}

"""
def temp(*args, **kwargs):
    print(args)
    print(kwargs)
    
a = (1,2,3)

temp(a)
temp(*a)
"""


def login_required(func):
    def wrapper(username, password, *args, **kwargs):
        if username in users and users[username]==password:
            func(*args, **kwargs)
        else:
            print("Invalid user")

    return wrapper


def add(a, b):
    print(a+b)


add = login_required(add)
add("user1","password", 5, 6)


# using decorator
@login_required
def sub(a, b):
    print(a-b)


sub("user2", "qwerty123", 123, 12)
print(dir())

