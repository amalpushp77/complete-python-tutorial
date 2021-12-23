from MyException import MyException

try:
    raise MyException("some error")
except Exception as e:
    print(e)
