class MyException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message

    # or

    # def __init__(self, msg):
    #     Exception.__init__(msg)
