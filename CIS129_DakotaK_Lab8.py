# CIS129_DakotaK_Lab8.py 
# Dakota K
# CIS129 Prog & Problem Solv I
# The is_palindrome function will check if a string is a palindrome using a stack, ignoring case, spaces, and punctuation, and returns True or False.

import string

def is_palindrome(input_string):
    # Process the data by removing spaces, punctuation, and by making lowercase
    proccessed = ''.join(char.lower() for char in input_string if char.isalnum())
    
    # Create an empty list to simulate a stack
    stack = []
    
    # Push the first half of the characters onto the stack
    for char in proccessed[:len(proccessed) // 2]:
        stack.append(char)
    
    # Start checking from the middle of the string
    mid_index = len(proccessed) // 2
    
    # If the length of the string has odd character count, skip the middle character
    if len(proccessed) % 2 != 0:
        mid_index += 1
    
    # Compare the characters in the second half to the stack
    for char in proccessed[mid_index:]:
        if stack.pop() != char:
            return False  # Palindrome = False
    
    return True  # Palindrome = True

# Deitel and Deitel test cases
print(is_palindrome("A man, a plan, a canal, Panama"))  # Palindrome = True
print(is_palindrome("racecar"))                         # Palindrome = True
print(is_palindrome("hello"))                           # Palindrome = False

# My test cases
print(is_palindrome("kayak"))
print(is_palindrome("wow")) 
print(is_palindrome("dakota")) 
print(is_palindrome("saippuakivikauppias")) 
print(is_palindrome("malayalam ")) 
                         
