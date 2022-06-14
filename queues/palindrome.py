from turtle import back
from deque import Deque

#using deque
def palindrome_checker(str):
    d = Deque()
    str = str.lower()
    for element in str:
        d.add_front(element)
    while d.size() > 1:
        return d.remove_front()==d.remove_rear()
    return True   

#using str method
def pal_checker(str):
    str = str.lower()
    front_index = 0
    back_index = -1
    for i in range(len(str)//2):
        if str[front_index] != str[back_index]:
            return False
        front_index += 1
        back_index -= 1
    return True

def pal_checker_2(str):
    str = str.lower()
    front_index = 0
    back_index = len(str)-1
    while front_index < back_index:
        if str[front_index] != str[back_index]:
            return False 
        front_index += 1
        back_index -= 1
    return True

def palindrome_check(str):
    str = str.lower().replace(" ",'')
    return str == str[::-1]

print(palindrome_checker("helo"))
print(palindrome_checker("Radar"))
print(palindrome_checker("lsdkjfskf"))
print(palindrome_checker("tot"))
print(palindrome_checker("t"))
print("\n")

print(pal_checker_2("helo"))
print(pal_checker_2("Radar"))
print(pal_checker_2("lsdkjfskf"))
print(pal_checker_2("tot"))
print(pal_checker_2("t"))
print("\n")

print(palindrome_check("helo"))
print(palindrome_check("Radar"))
print(palindrome_check("lsdkjfskf"))
print(palindrome_check("tot"))
print(palindrome_check("t"))
print("\n")



    
        