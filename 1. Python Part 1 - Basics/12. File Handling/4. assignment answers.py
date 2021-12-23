# 1. WAF writer() using with statement that takes list of temperature as input and creates a text file 'temps.txt'.
# Store the temperature in Fahrenheit


def writer(temp_list):
    with open('temps.txt', 'w') as file:
        for Celsius in temp_list:
            f = Celsius * (9 / 5) + 32
            file.write(str(f) + '\n')


cel = [-50, 0, 10, 20, 37, 50]

writer(cel)


# 2.Repeat the above question without using context manager but should behave like one. Hint: use error handling

def writer2(temp_list):

    try:
        file = open('temps.txt', 'w')
        for Celsius in temp_list:
            f = Celsius * (9 / 5) + 32
            file.write(str(f) + '\n')
    except Exception as e:
        print("File not found")
    finally:
        file.close()


cel = [-50, 0, 10, 20, 37, 50]

writer2(cel)
