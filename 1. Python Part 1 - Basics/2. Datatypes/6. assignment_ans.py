# 1. WAP to add 2 numbers by taking input from user
# int() built-in function is used to type cast the return type of input function from sting to integer
a = int(input("enter number 1: "))
print(a)

b = int(input("enter number 2: "))
print(b)

c = a+b
print(c)

# 2. WAP to concatenate first name with last name by taking input from user
first_name = input("Enter 1st name: ")
last_name = input("Enter last name: ")

print(first_name + last_name)   # concatenation
print(first_name, last_name)

# 3. Create user specific message using this template - string formatting
first_name = input("Enter 1st name: ")
last_name = input("Enter last name: ")
phone_number = input("Enter phone no: ")
email = input("Enter email: ")
string = f"Hi {first_name} {last_name}, please verify your phone number {phone_number} and email address {email} for " \
         f"smooth customer service. Regards Service Manager"
print(string)

# 4. Which of the following operator is used with list:
#     a) +    b) -    c) *    d) /    e) in
#   answer: a, c, e

# 5. Comment on the output
a = 5/3
print(round(a, 2))  # round the fraction up to 2 decimal digits

p = 4 * 5 ** 2
print(p)   # BIDMAS/BODMAS

n = ---5   # 3 times -ve is -ve
print(n)

# 6. Which of the following is not valid
abc = 745,000,475   # if you provide multiple values to a variable it behaves as tuple
# a b, c = 1245,0145,457   # b) variable can't have space in between
a, b, c = 1209,789,451
a_b_c = 1245
