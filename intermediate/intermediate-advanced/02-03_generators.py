"""
Generators returns one value at a time, and also gives them as an iterable.
- Instead of 'return', they use 'yield'.
- They are so much lighter. Perfect for efficiency and algorithm speed. 
"""

def my_generator():
    yield 1 + 1
    yield 1 + 2
    yield 1 + 3
    yield 1 + 4
    yield 1 + 5
    
g = my_generator()
print(g) # prints an object
print(next(g)) # goes through the values one at a time
print(next(g))
print(next(g))

print(list(g)) # prints a list of the yielded values

#! comparison between a normal func and a generator
import sys

def my_func(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

a = my_func(1000000)

# as it returns the values as an iterator, we don't need a list anymore
def my_gen(n):
    num = 0
    while num < n:
        yield num
        num += 1
        
b = my_gen(1000000)

print(sys.getsizeof(a))
print(sys.getsizeof(b))