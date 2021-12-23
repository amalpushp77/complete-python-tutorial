import time

start = time.perf_counter()

# l = [x for x in range(99999)]

t = (x for x in range(99999))


stop = time.perf_counter()
print(stop - start)
