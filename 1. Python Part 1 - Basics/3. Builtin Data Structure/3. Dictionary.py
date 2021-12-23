# Dictionary {key:value}
# this datatype is called dictionary, key must be immutable datatype and value can be of any datatype
# dictionary don't support indexing and slicing
# d={} # empty dictionary

d = {1: 'abc', 2: 2.34, 3: True}
print(d)
print(type(d))

d = {'username': 'amal', 'location': 'nagpur,In', 'time': '12:00', 'Date': '19-11-2020'}
print(d)

print(d['username'])

fb_post = {'user_name': 'amal pushp',
           'user_id': 1234456,
           'message': 'your post',
           'timestamp': 'D11202018T1125',
           'language': 'English',
           'location': (44.4820234, -103.234543)}

print('Before changing language: ', fb_post)
fb_post['language'] = 'Hindi'
print('After changing language: ', fb_post)

# add new item in dictionary,a key and value pair
fb_post['tag'] = 'best friend'
print(fb_post)
