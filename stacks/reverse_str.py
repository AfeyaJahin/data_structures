from stack import Stack

def rev_str(my_str):
    s1 = Stack()
    for ch in my_str:
        s1.push(ch)
    
    reversed_str = ''
    while not s1.is_empty():
        reversed_str = reversed_str + s1.pop()
    return reversed_str
        

print(rev_str("cat"))