"""
! Fibonacci challenge
Write a program that prints the first 50 numbers of the 
fibonacci succession starting from 0.
- Fibonacci sequence is a succession where the
next number is the sum of the last two numbers.
- 0 1 1 2 3 5 8 13 21...
"""

def fib() -> None:
    prev: int = 0
    next: int = 1
    for i in range(0, 50):
        fibo: int = prev + next
        prev = next
        next = fibo
        print(fibo)
        
fib()