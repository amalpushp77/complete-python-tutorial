# Boolean
d = True
print(type(d))

# Empty datatype and 0 are considered as False

empty_string = ""
zero_integer = 0
zero_float = 0.0
zero_complex = 0 + 0j
empty_list = []
empty_tuple = ()
empty_dictionary = {}
empty_set = set()

# using comparison operator we are evaluating above datatype and data structure
# only numeric datatype equates to False condition
# there is no meaning in evaluating string, list, tuple, dictionary, set with equivalent operator, for both Ture and
# False it will evaluate to False
# print(empty_string == False)
print(zero_integer == False)
print(zero_float == False)
print(zero_complex == False)
# print(empty_list == False)
# print(empty_tuple == False)
# print(empty_dictionary == False)
# print(empty_set == False)


# using as a condition
if empty_list:
    print("List is not empty")
else:
    print("List is empty")

if empty_string:
    print("String is not empty")
else:
    print("String is empty")

if empty_tuple:
    print("Tuple is not empty")
else:
    print("Tuple is empty")

if empty_list:
    print("Set is not empty")
else:
    print("Set is empty")
