# We can implement abstract class using module abc
# abstract class must inherit ABC class
# any methods in abstract class must use @abstractmethod decorator

"""
    note -
    1. Objects can't be created from abstract class
    2. Any derived class from abstract class must fully provide the definition of abstractmethod before creating a
    object
"""

from abc import ABC, abstractmethod


class Institute(ABC):

    def __init__(self):
        print(type(self).__name__, " details: ")

    def coursesOffered(self):
        print("Course offered: C, C++, Java, .net")

    @abstractmethod
    def address(self):
        pass


class PythonAcademy(Institute):
    def coursesOffered(self):
        print("Courses offered: Python, Data Science, ML")

    def address(self):
        print("Nagpur")


class OnlineAcademy(Institute):
    def address(self):
        print("Online")

