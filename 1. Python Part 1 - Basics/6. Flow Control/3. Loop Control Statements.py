# break keyword - break the loop

##email_list = ['google','whatsapp','rcoem','spam','facebook','flipkart']
##
##for i in email_list:
##    if i == 'spam':
##        print('Spam is deleted')
##        break
##    print('Read Email: ',i)
##
##print('outside of for loop')


# continue keyword

##email_list = ['google','whatsapp','rcoem','spam','facebook','flipkart']
##
##for i in email_list:
##    if i == 'spam':
##        print('Spam is deleted')
##        continue
##    print('Read Email: ',i)
##
##print('outside of for loop')

# pass keyword

##email_list = ['google','whatsapp','rcoem','spam','facebook','flipkart']
##
##for i in email_list:
##    if i == 'spam':
##        pass
##    print('Read Email: ',i)
##
##print('outside of for loop')


############################
b = 7

for i in range(12):
    for j in range(20):
        if i == 7:
            break
        print('value of j =', j)
    print('value of i =', i)
    print('=' * 100)

##################################

##b = 7
##
##for i in range(12):
##    print('inside for loop, iteration no.: ', i+1)
##    for j in range(20):
##        print('inside nested for loop iteration no.', j+1)
##        if i==7:
##            continue
##        print('value of j =',j)
##    print('value of i =',i)
##    print('='*100)


#####################################

# b = 7
#
# for i in range(12):
#     print('inside for loop, iteration no.: ', i + 1)
#     for j in range(20):
#         print('inside nested for loop iteration no.', j + 1)
#         if j == 7:
#             continue
#         print('value of j =', j)
#     print('value of i =', i)
#     print('=' * 100)

# continue and break keyword
##email_list = ['google','whatsapp','rcoem','spam','facebook','flipkart']
##
##for i in email_list:
##    if i == 'spam':
##        print('Spam is deleted')
##        continue
##    print('Read Email: ',i)
##
##print('outside of for loop')
