"""
! Prime number challenge
Make a program that prints if a given number is prime or not.
After, make a program that prints the prime numbers
from 1 to 100.
"""

def is_prime(n) -> bool:
    if n < 2:
        return False
    
    divisors = []
    for i in range(1, n+1):
        if n % i == 0:
            divisors.append(i)
    
    if len(divisors) <= 2:
        return True
        
    return False

print(is_prime(7)) # True
print(is_prime(10)) # False

def prime_numbers() -> None:
    for n in range(2, 101):
        
        if n > 2:
            for i in range(2, n):
                
                divisible = False
                
                if n % i == 0:
                    print(f"{n}   {i}")
                    divisible = True
                    break
                    
            if not divisible:
                print(f"{n} - Prime")

print(prime_numbers())