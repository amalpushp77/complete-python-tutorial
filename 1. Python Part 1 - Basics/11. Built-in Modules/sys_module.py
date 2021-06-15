#We are using sys module to find size of list and tuple with same elements
import sys

##list_eg = [1,2,3,4,5]
##
##tuple_eg = (1,2,3,4,5)
##
####help(sys.getsizeof)
##
##list_eg_size = sys.getsizeof(list_eg)
##tuple_eg_size = sys.getsizeof(tuple_eg)
##
##print('List size in bytes =', list_eg_size)
##print('Tuple size in bytes =', tuple_eg_size)
##print()
##print('Tuple takes less memory than List')

print(sys.argv[0])


if __name__ == '__main__':
    print(sys.argv)