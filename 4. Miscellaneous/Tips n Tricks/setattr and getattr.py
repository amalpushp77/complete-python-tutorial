class Person:
    pass


person = Person()
person_info = {"first_name": "Amal", "Last_name": "Pushp"}

for key, value in person_info.items():
    setattr(person, key, value)

for key in person_info.keys():
    print(getattr(person, key))