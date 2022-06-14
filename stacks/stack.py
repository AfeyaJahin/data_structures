class Stack():
    def __init__(self):
        """Create new stack"""
        self.items = []
        
    def push(self,item):
        """add item on top of stack"""
        self.items.append(item)
        
    def pop(self):
        """remove item from the top of stack"""
        return self.items.pop()
        
    def is_empty(self):
        """check if stack is empty"""
        return not bool(self.items)
    
    def peek(self):
        """return value of item at the top of stack"""
        return self.items[-1]
    
    def __str__(self):
        """string representation of the stack"""
        return str(self.items)
    
#Alternate implementation using the beginning of list as the top
class Stak():
    def __init__(self):
        """Create new stack"""
        self.items = []
        
    def push(self,item):
        """add item on top of stack"""
        self.items.insert(0, item)
        
    def pop(self):
        """remove item from the top of stack"""
        self.items.pop(0)
        
    def is_empty(self):
        """check if stack is empty"""
        return self.items == []
    
    def peek(self):
        """return value of item at the top of stack"""
        return self.items[0]
    
    def __str__(self):
        """string representation of the stack"""
        return str(self.items)

"""s = Stack()
s.push(4)
print(s)
s.push(True)
s.push("cat")
print(s)
s.pop()
print(s)
print(s.peek())
print(s.is_empty())"""
