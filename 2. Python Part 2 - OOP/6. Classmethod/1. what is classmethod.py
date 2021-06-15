# classmethod
# use as alternative constructors
# class methods can't use instance level data
# @classmethod decorator is used

"""     class Employee:
            def __init__(self, name, salary = 30000):
                ....

            @classmethod
            def from_file(cls , filename);
                with open(filename, "r") as f:
                    name = f.readline()
                return cls(name)
                """
