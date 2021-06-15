#Number System

##decimal = 78
##binary = 0b1010
##octal = 0o5432
##hexa = 0x000F
##
##print("Prints in decimal -> int format")
##print('Decimal: ',decimal)
##print('Binary: ', binary)
##print('Octal: ', octal)
##print('Hexa: ', hexa)

##decimal = 12
##
##binary_equivalent = bin(decimal)
##octal_equivalent = oct(decimal)
##hexa_equivalent = hex(decimal)
##
##print('Returns string format... check the type() of variables binary_equivalent, octal_equivalent, hexa_equivalent')
##print('Value of',decimal,'in binary is:',binary_equivalent)
##print('Value of',decimal,'in octal is:',octal_equivalent)
##print('Value of',decimal,'in hexa is:',hexa_equivalent)
##print(type(binary_equivalent))

#Shift operator
#  >> Right Shift           << Left shift

##a = 0b10100
##b = 0b00100
##
##l_shift =  a << 3  #Left shift adds the number of bits
##r_shift = b >> 2
##
##print(r_shift)
##print(l_shift)

#Convert string binary into decimal equivalent
##binary = '0b1010'
##
##dec = int(binary, base=2) #for hexa base=16, for octal base=8
##
##print(dec)

##a = 0b1010
##b = 0b1101
##
##print('And operation:',bin(a&b))
##print('OR opeartion:',bin(a|b))
##print('XOR operation:',bin(a^b))
##
##print("Add:", bin(a+b))
##print("SUB:", bin(a-b))
##print("Multiply:", bin(a*b))

#NOT GATE function
##def not_gate(decimal):
##    binary_equivalent = bin(decimal)
##    binary_ones = '0b' + (len(binary_equivalent) - 2) * '1'
##
##    decimal_not_equivalent = int(binary_ones, base=2) - decimal
##    binary_not_equivalent = bin(decimal_not_equivalent)
##
##    return binary_equivalent, decimal_not_equivalent, binary_not_equivalent
##
##a = int(input("Enter an interger: "))
##
##binary, dec_not, binary_not = not_gate(a)
##
##print('The binary equivalent of', a, 'is:', binary)
##print('NOT of', binary, 'is:', binary_not, '\n' + 'which is:', dec_not)


#NOT GATE for exact bits
##def not_gate_bits(decimal, number_of_bits = 8):
##
##    binary_equivalent = bin(decimal)
##
##    if (len(bin(decimal)) - 2) != number_of_bits:
##        binary_equivalent = '0b' + ('0' * (number_of_bits - (len(bin(decimal)) - 2))) + bin(decimal)[2:]
##
##    binary_ones = '0b' + (len(binary_equivalent) - 2) * '1'
##
##    decimal_not_equivalent = int(binary_ones, base=2) - decimal
##    binary_not_equivalent = bin(decimal_not_equivalent)
##
##    if len(binary_equivalent) != len(binary_not_equivalent):
##        binary_not_equivalent = '0b' + ('0' * (len(binary_equivalent) - len(binary_not_equivalent))) + binary_not_equivalent[2:]
##
##    return binary_equivalent, decimal_not_equivalent, binary_not_equivalent
##
##
##a = int(input("Enter an interger: "))
##
##binary, dec_not, binary_not = not_gate_bits(a)
##
##print('The binary equivalent of', a, 'is:', binary)
##print('NOT of', binary, 'is:', binary_not, '\n' + 'which is:', dec_not)




#CONVERSIONS

i = 17

b = bin(i)
print('Binary value of',i,'is',b)

o = oct(i)
print('Octal value of',i,'is',o)

h = hex(i)
print('Hexadecimal value of',i,'is',h)

print("\n"+'But observe this')
print('variable i =',i, 'is of', type(i))
print('AND')
print('variable b =',b, 'is of', type(b))

print('similar for variable o and h')
print('variable o =',o, 'is of', type(o))
print('variable h =',h, 'is of', type(h))

print('\n'+ 'Now, How will you convert the binary which is in string to its decimal equivalent?')

binary = '0b1011101'

#This will give error
#value = int(binary)
print('\n'+ 'variable binary =',binary, 'is of', type(binary))
print('BY passing the 2nd parameter to int() function that define base')
value = int(binary,2)
print('Integer value of',binary,'is',value)
print('variable value =',value, 'is of', type(value))

print('\n'+ 'You can give any value to base but make sure you pass the right value')
print("For ex- hexadecimal has 16 digits 012...F" + "\n"+ 'If I take base = LESS THAN the no. of digits reqiured to represent that no. system it will give ERROR')

no_system = '1257824'  #This no. system has 9 digits 012...8 OR it can be decimal (if use default base=10) OR hexadecimal (if base=16)

#This will give error
#equivalent = int(no_system,2)
#equivalent = int(no_system,3)
#equivalent = int(no_system,4)
#equivalent = int(no_system,5)
#equivalent = int(no_system,6)
#equivalent = int(no_system,7)
#equivalent = int(no_system,8)

equivalent = int(no_system,9)
print('For no. system with base =9',no_system, ' equivalent is', equivalent)

equivalent = int(no_system,10)
print('For no. system with base =10',no_system, 'equivalent is', equivalent)

equivalent = int(no_system,16)
print('For no. system with base =16',no_system, 'equivalent is', equivalent)