# Decorators

#! noob decorator
""" def respectfully(func) -> any:
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        print("How has your day been going?")
    return wrapper

def greet(name:str):
    print(f"Hello, {name}!") """
    
# greet_respectfully = respectfully(greet("Robert"))
# print(greet_respectfully)

import functools

#! well implemented decorator
def respectfully2(func):
    @functools.wraps(func)
    def wrapper2(*args, **kwargs):
        result = func(*args, **kwargs)
        print("How has your day been going?")
        return result   
    return wrapper2

@respectfully2
def greet2(n):
    return f"Hello, {n}!"
    
a = greet2("Roberto")
print(a)

"""
Example of a practical use of the decorators.
The timer function returns the time it took the
function to execute.
"""
import time

def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"\nFinished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        suma = sum([i**2 for i in range(10000)])
    
# waste_some_time(10)


#! decorators with arguments
def repeat(num_times):
    """Will repeat the decorated function an arbitrary number of times."""
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper_repeat(*args, **kwargs):
            for _ in range(num_times):
                value = func(*args, **kwargs)
            return value
        return wrapper_repeat
    return decorator_repeat

@repeat(num_times=4)
def add(a):
    print(f"\n{a + 5}")

add(100)