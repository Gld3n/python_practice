from datetime import datetime

now = datetime.now()
timestamp = datetime.timestamp(now)

date: dict = {
    "year": now.year,
    "month": now.month,
    "day": now.day,
    "hour": now.hour,
    "minute": now.minute
}

def formated_date(date) -> datetime:
    year = date["year"] 
    month = datetime.strptime(str(date["month"]), "%m").strftime("%B")
    day = date["day"]
    hour = date["hour"]
    minute = date["minute"]
    return f"Today is {month} {day}, {year}. It's {hour} hours with {minute} minutes."

f_date = formated_date(date)
print(f_date)


print("\n====================================================================\n")


sqrts = [i * i for i in range(40 + 1)] 
print(sqrts)
if 1024 in sqrts:
    print(1024 // 32)
        
        
print("\n====================================================================\n")


capy_printer = lambda capys_name: f"{capys_name} is an amazing capybara!"
print(capy_printer("Gort"))


print("\n====================================================================\n")


def f_sum(value: int) -> int:
    return value + 10

def f_mult(value: int) -> int:
    return value * 10

def higher_order(first, second: int, func) -> int:
    return func(first + second)

print(higher_order(5, 5, f_sum))
print(higher_order(5, 5, f_mult))


print("\n====================================================================\n")


#? Closures concept from Programiz
"""
* The nested function now acts as a closure that closes the outer scope 
* variable within its scope even after the outer function is executed.
* This makes posible operating over the same value (num) again and again.
"""
def calculate():
    num = 1
    def inner_func():
        nonlocal num 
        num += 2
        return num
    return inner_func

# call the outer function
odd = calculate() #! inner_func is now given to odd as a closure

# call the inner function
print(odd())
print(odd())
print(odd())

# call the outer function again
odd2 = calculate() #! Resets the value
print(odd2())


print("\n====================================================================\n")


#? Decorator: an elegant way to apply a function to a function

def reversed_printer(func):
    def inner_func(t):
        reversed_tc = ""
        for i in t[::-1]:
            reversed_tc += i
            
        return func(reversed_tc)
    return inner_func

@reversed_printer
def boring_printer(text):
    print(text)
    
boring_printer("Hello")
boring_printer("Love")
boring_printer("Dog")
boring_printer("Square")
boring_printer("Infinitely")


print("\n====================================================================\n")

#? -- map --

names = ["Robert", "Jose", "Chiqui"]

def greets(name):
    return f"Hello, {name}!" 

greetings = list(map(greets, names))
greetings2 = list(map(lambda name: f"Hello, {name}!", names)) # the same as above

for g in greetings:
    print(g)

print()    

for g in greetings2:
    print(g)
    
#? -- filter --

numbers = [4, 2, 10, 90, 324, 3, 8, 7, 56437]
filtered = list(filter(lambda n: n % 2 == 0, numbers))

print(f"\n{filtered}")
print(list(filter(lambda n: n % 3 == 0, numbers)))