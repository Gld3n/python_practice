import time

l = [i for i in range(1, 13_000_000)]

start1 = time.perf_counter()
pows = [i**2 for i in l if i**2 > 30]
end1 = time.perf_counter()
result = f'elapsed: {end1 - start1:.1f} seconds'
print(result)

start2 = time.perf_counter()
pows_walrus = [val for i in l if (val := i**2) > 30]
end2 = time.perf_counter()
result2 = f'elapsed: {end2 - start2:.1f} seconds'
print(result2)