import time

time_here = time.localtime()
print(time_here)

# to access any values from time_here
print("Year is:", time_here.tm_year)
print("Month is:", time_here.tm_mon)
print('Day of Month is:', time_here.tm_mday)
print('Time is =', time_here.tm_hour, ':', time_here.tm_min, ':', time_here.tm_sec )

# current time of system in seconds
time_in_seconds = time.time()
print(time_in_seconds)

# help(time.time)

