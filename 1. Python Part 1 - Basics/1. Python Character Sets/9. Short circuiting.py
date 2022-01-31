# concept of short circuiting
# Evaluate: True or False and True
# note: AND has higher precedence thus, True or (False and True)
# note: print() returns None
# note: bool(None) is False
# there is no meaning in using logical operator on other than boolean datatype

# Evaluate
print(True and bool(print(4)))
print(False and bool(print(4)))
print(bool(print(4)) and True)
print(bool(print(4)) and False)

print(True or bool(print(4)))
print(False or bool(print(4)))
print(bool(print(4)) or True)
print(bool(print(4)) or False)

# Try
print(False or False or False)  # False
print(False or False or True)  # True
print(False or True or False)  # True
print(False or True or True)  # True
print(True or False or False)  # True
print(True or False or True)  # True
print(True or True or False)  # True
print(True or True or True)  # True

print(False and False and False)  # False
print(False and False and True)  # False
print(False and True and False)  # False
print(False and True and True)  # False
print(True and False and False)  # False
print(True and False and True)  # False
print(True and True and False)  # False
print(True and True and True)  # True

print(False or False and False)  # False # print(bool(print(4)) or bool(print(4)) and bool(print(4)))
print(False or False and True)  # False
print(False or True and False)  # False
print(False or True and True)  # True
print(True or False and False)  # True
print(True or False and True)  # True
print(True or True and False)  # True
print(True or True and True)  # True

print(False and False or False)  # False # print(bool(print(4)) and bool(print(4)) or bool(print(4)))
print(False and False or True)  # True
print(False and True or False)  # False
print(False and True or True)  # True
print(True and False or False)  # False
print(True and False or True)  # True
print(True and True or False)  # True
print(True and True or True)  # True # print(bool(print(4)) and True or True)

print(True and False and True or False)  # False
print(not True or False and True or False)  # False # (not True) or (False and True) or False
print(True or False and True or False)  # True

# note: place the most critical condition first
