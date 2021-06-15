# def add_emp(emp, emp_lst=[]):
#     emp_lst.append(emp)
#     print(emp_lst)


def add_emp(emp, emp_lst=None):
    if emp_lst is None:
        emp_lst = []
    emp_lst.append(emp)
    print(emp_lst)


lst = ['amal', 'laskh', 'rishabh']
add_emp('aditya', lst)

add_emp('amal')
add_emp('laksh')
add_emp('rishabh')

import time
from datetime import datetime


# def display_time(time=datetime.now()):
#     print(time.strftime("%B %d, %Y %H:%M:%S"))

def display_time(time=None):
    if time is None:
        time = datetime.now()
    print(time.strftime("%B %d, %Y %H:%M:%S"))


display_time()
time.sleep(1)
display_time()
time.sleep(1)
display_time()
