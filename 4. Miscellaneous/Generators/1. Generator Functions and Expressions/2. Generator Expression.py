# list comprehension
newlist = [item.upper() for item in collection]

# generator expression
(item.upper() for item in collection)


#list of mixed format numbers
numbers = [7, 22, 4.5, 99.7, '3', '5']

#convert numbers to integers using expression
integers = (int(n) for n in numbers)

names_list = ['Adam','Anne','Barry','Brianne','Charlie','Cassandra','David','Dana']

#Converts names to uppercase
uppercase_names = (name.upper() for name in names_list)


# even integer expression
even_integers = (n for n in range(10) if n%2==0)

# list of names
names_list = ['Adam','Anne','Barry','Brianne','Charlie','Cassandra','David','Dana']

# too long
# reverse_uppercase = (name[::-1] for name in (name.upper() for name in names_list))

# breaking it up
uppercase = (name.upper() for name in names_list)
reverse_uppercase = (name[::-1] for name in upper_case)

