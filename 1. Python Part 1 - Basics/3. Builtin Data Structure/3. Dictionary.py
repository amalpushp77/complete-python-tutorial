# Dictionary {key:value}
#d={} #it is not empty set it has datatype dictionary i.e empty dictionary
#this datatype is called dictionary, key must be immutable datatype and value can be of any datatype
d = {1: 'abc', 2: 2.34, 3: True}
print(d)
print(type(d))

# Dictionary
d = {'username': 'amal', 'location': 'nagpur,In', 'time': '12:00', 'Date': '19-11-2020'}

print(d)

print(d['username'])


#dictionary don't support indexing and slicing

##fb_post = {'user_name' : 'amal pushp',
##           'user_id' : 1234456,
##           'message' : 'your post',
##           'datetime' : 'D11202018T1125',
##           'language' : 'English',
##           'location' : (44.4820234, -103.234543)}
##
##print('Before changing language: ',fb_post)
##fb_post['language'] = 'Hindi'
##print('After changing language: ',fb_post)

#add element in dictionary,key and value
##fb_post['tag'] = 'best friend'
##print(fb_post)