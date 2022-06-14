""" Write a function that takes a string as a parameter 
    and returns True if the string is a palindrome, False otherwise.
    Remember that a string is a palindrome if it is spelled the same
    both forward and backward.Check for punctuations and space
"""

import re
def palindrome_checker(str):
    str = (str.replace(" ",'')).lower()
    str = re.sub(r'[^\w\s]','', str)
    
    if len(str) <=1:
        return True
    if str[0]!=str[-1]:
        return False
    return palindrome_checker(str[1:-1])
        
    
#test       
print(palindrome_checker("cat")) #False 
print(palindrome_checker("Kayak")) #True
print(palindrome_checker("Madam I'm Adam")) #True
print(palindrome_checker("Go hang a salami; I’m a lasagna hog.")) #True
print(palindrome_checker("Reviled did I live, said I, as evil I did deliver")) #True
print(palindrome_checker("hello this is not a palindrome")) #False
