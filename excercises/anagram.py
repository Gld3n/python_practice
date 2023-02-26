"""
! Anagram challenge
Define a function that takes two arguments (strings) and 
returns a boolean.
- It's not needed to check if both words exist.
- Two identical words are not an anagram.
"""

# * Verbose solution
def is_anagram(word_one: str, word_two: str) -> bool:
    word_one_list: set = {i for i in word_one}
    word_two_list: set = {i for i in word_two}
    diff: set = word_one_list.difference(word_two_list)
    
    if word_one.lower() == word_two.lower():
        return False
    elif not diff:
        print("Is_anagram")
        return True
        
    return word_one == word_two

"""
! After some research, I noticed this function doesn't work properly
! if words with repeated letters are given (e.g: Alabama).
"""
is_anagram("amor", "roma")


# * Direct solution
def is_anagram_2(first_word, second_word) -> bool:
    if first_word.lower() == second_word.lower():
        return False
    
    return sorted(first_word.lower()) == sorted(second_word.lower())

#! This function would be a correct solution
print(is_anagram_2("pato", "topa"))