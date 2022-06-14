from node import Node

class unorderedList:
    def __init__(self):
        self.head = None
        
    def is_empty(self):
        return self.head == None
        
    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found and current is not None:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()          
        if self.is_empty():
            print("empty list")
        if current is None:
            print("item not in list")
            return 
        if previous is None:
            print("Removed the only node in list")
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
        return
           
    def remove_at_index(self,pos):
        current = self.head
        previous = None
        index = 0
            
        if self.is_empty():
            print("list is empty")
            return
        if pos<0:
            pos = self.size() + pos
        while index < pos and current != None:
            previous = current
            current = current.getNext()
            index +=1
        if previous is None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
               
    
    def search(self,item):
        current = self.head
        while Node != None:
            if current.data == item:
                return True 
            current = current.getNext()
        return False
        
    
    def size(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNext() 
        return count
               
    def __len__(self):
        return self.size() 
    
    def append(self,item):
        current = self.head
        if self.is_empty():
            self.head = Node(item)
            return
        while current.getNext() is not None:
            current = current.getNext()
        current.setNext(Node(item))
        
        
    def index(self,item):
        count = 0
        current = self.head
        while current.getData() != item:
            current = current.getNext()
            count += 1
        return count
        
    def insert(self,pos,item):
        current = self.head
        previous = None
        index = 0
        if self.is_empty():
            self.head = (Node(item))
        if pos<0:
            pos = self.size() + pos     
        while index < pos and current != None:
            previous = current 
            current = current.getNext()
            index+=1
        if previous == None:
            self.add(item)
        else:
            temp = Node(item)
            temp.setNext(current)
            previous.setNext(temp)
    
    def pop(self):
        current = self.head
        previous = None
        while current.getNext() is not None:
            previous = current
            current = current.getNext()
        if self.is_empty():
            print("List empty")
            return
        if previous is None:
            self.head = None
            return current.getData()
        else:
            previous.setNext(current.getNext())
            return current.getData()
        
    def __str__(self):
        result = "["
        current = self.head
        while current:
            result+= ('' if result == '[' else ", ") + str(current.data)
            current = current.getNext()
        result+="]"
        return result


def main():
    
    l = unorderedList()
    
    l.add(2)
    l.add(1)
    l.append(3)
    l.append(4)
    l.append(5)
    l.append(6)
    l.insert(0,0)
    print(l)
    l.insert(3,4)
    print(l)
    l.insert(5,9)
    print(l)
   

main()            
            