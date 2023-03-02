# Decorators

#! noob decorator
def respectfully(func) -> any:
    def wrapper():
        func()
        print("How has your day been going?")
    return wrapper

def greet(name:str):
    print(f"Hello, {name}!")
    
# greet_respectfully = respectfully(greet("Robert"))
# print((greet_respectfully))

#! well implemented decorator
def respectfully2(func) -> any:
    def wrapper2():
        func()
        print("How has your day been going?")
    return wrapper2

@respectfully2
def greet(name:str):
    print(f"Hello {name}!")
    
greetings = greet("")