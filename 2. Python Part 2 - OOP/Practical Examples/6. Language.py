class English:
    def greet(self, name):
        print("Good Morning", name)


class French:
    def greet(self, name):
        print("Bonjour", name)


# common interface
def greetings(language, name):
    language.greet(name)


eng = English()
fre = French()

for language in [eng, fre]:
    greetings(language, "Amal")
