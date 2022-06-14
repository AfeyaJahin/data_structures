class Queue():
    def __init__(self):
        self.items = []
        
    def enqueue(self,item):
        self.items.insert(0, item)
        
    def dequeue(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def __str__(self):
        return str(self.items)
    
    def size(self):
        return len(self.items)
    


""" 
q = Queue()
q.enqueue(4)
print(q)
q.enqueue("dog")
print(q)
q.enqueue(True)
print(q)
print(q.dequeue())
print(q)
q.dequeue()
q.dequeue()
print(q.is_empty()) """


