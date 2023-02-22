"""
! Fizzbuzz challenge
In a range of 100 (including 1 and itself)
make a program that prints the following:
- Multiple of 3 - print Fizz.
- Multiple of 5 - print Buzz.
- Multuple of both - print FizzBuzz.
"""

def fibu() -> None:
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0:
            print(f"{i} - FizzBuzz!")
        elif i % 3 == 0:
            print(f"{i} - Fizz!")
        elif i % 5 == 0:
            print(f"{i} - Buzz!")
        else:
            print(i)
                
fibu()