#We are using timeit module to find time required to create 9999999 list and tuple with same elements
import timeit


##help(timeit.timeit)

list_time = timeit.timeit(stmt = "[1,2,3,4,5]", number = 9999999)

tuple_time = timeit.timeit(stmt = "(1,2,3,4,5)", number = 9999999)

print('List time in seconds:', list_time)
print('Tuple time in seconds:', tuple_time)
print()
print('Thus, Creating of datatype list takes more time than tuple')