"""
! Inverted string challenge
Write a program that prints a reversed given string without
using any built-in function that does it automatically.
- 'Hello world' ==> 'dlrow olleH' 
"""

#* Old version. More expensive and slower to execute
def reversed_text(text: str) -> str:
    
    if type(text) != str:
        return "That's not a string I can reverse."
    
    reversed_tc: str = ""
    for i in text[::-1]:
        reversed_tc += i #! This will create a whole new string
        
    return reversed_tc

print(reversed_text("Hello world!"))


#* Faster and more efficient way to do it
def new_reversed(text: str) -> str:
    
    if type(text) != str:
        return "That's not a string I can reverse."
    
    reversed_tc: list = [i for i in text[::-1]]
        
    #* Join method will add each element of the list into a string
    return "".join(reversed_tc)

print(new_reversed("Hello world!"))