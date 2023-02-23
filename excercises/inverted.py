"""
! Inverted string challenge
Write a program that prints a reversed given string without
using any built-in function that does it automatically.
- 'Hello world' ==> 'dlrow olleH' 
"""

def reversed_text(text: str) -> str:
    
    if type(text) != str:
        return "That's not a string I can reverse."
    
    reversed_tc: str = ""
    for i in text[::-1]:
        reversed_tc += i
        
    return reversed_tc

print(reversed_text("Hello world!"))