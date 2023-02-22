"""
! Fizzbuzz challenge
In a range of 100 (including 1 and itself)
make a program that prints the following:
- Multiple of 3 - print Fizz.
- Multiple of 5 - print Buzz.
- Multuple of both - print FizzBuzz.
"""

def fibu():
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


"""
! Anagram challenge
Define a function that takes two arguments (strings) and 
returns a boolean.
- It's not needed to check if both words exist.
- Two identical words are not an anagram.
"""

# * Verbose solution
def is_anagram(word_one, word_two) -> bool:
    word_one_list = {i for i in word_one}
    word_two_list = {i for i in word_two}
    diff = word_one_list.difference(word_two_list)
    
    if word_one.lower() == word_two.lower():
        return False
    elif not diff:
        print("Is_anagram")
        return True
        
    return word_one == word_two

is_anagram("amor", "roma")

# * Direct solution
def is_anagram_2(first_word, second_word) -> bool:
    if first_word.lower() == second_word.lower():
        return False
    
    return sorted(first_word.lower()) == sorted(second_word.lower())

print(is_anagram_2("pato", "topa"))


"""
! Fibonacci challenge
Write a program that prints the first 50 numbers of the 
fibonacci succession starting from 0.
- Fibonacci sequence is a succession where the
next number is the sum of the last two numbers.
- 0 1 1 2 3 5 8 13 21...
"""

def fib():
    prev = 0
    next = 1
    for i in range(0, 50):
        fibo = prev + next
        prev = next
        next = fibo
        print(fibo)
        
fib()