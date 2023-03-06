# Types and syntax of function arguments

#! Positional args
def foo(a, b):
    print(a, b)
    
foo(1, 2)
print()

#! Keyword args
def bar(a, b, c):
    print(a, b, c)
    
bar(c=3, b=2, a=1)
bar(1, 2, 3)
print()

#! Default args
def kw(a, b, capy="cute"):
    print(a, b, f"capy is {capy}")
    
kw(1, 2)
kw(2, 3, "wholesome")
print()

#! Variable lenght args

# *args
def fizz(a, b, *args):
    print(a, b, args)
    # this is a tuple
    for arg in args:
        print(arg)
        
fizz(1, 2, 3, 4)
fizz(2, 6, "hello", True, 200, 3.14)
print()

# **kwargs
def buzz(a, b, *args, **kwargs):
    print(a, b, args, kwargs)
    # this is a dict
    for k in kwargs:
        print(k, kwargs[k])
        
buzz(1, 2, 3, 4, 5, two=2, true=True, capy="cool")
print()

#* **kwargs can also be defined this way, but the arg must match the param name
#* and won't be a dict
def greet(*, person1, person2):
    print(person1, person2)
        
greet(person1="Mario", person2="Robert")
print()

#! Unpacking args
def print_unpckd(a, b, c, d):
    print(a, b, c, d)
    
#* the ammount of args must match the ammount of params
#* and the unpacking is made by putting "*"
liste = [1, 2, 3, 4]

print_unpckd(*liste)

#* it can also be done with dicts using "**"
dicte = {"a": 1, "b": 2, "c": 3, "d": 4}

print_unpckd(**dicte)
print()

