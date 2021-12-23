# with statement automatically close the file when done working on it

with open('example.txt', 'a') as file:
    file.write('\n' + 'Hello World')
