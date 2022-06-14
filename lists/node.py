class Node():
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        
    def getData(self):
        return self.data
        
    def setData(self, node_data):
        self.data = node_data
        
    def getNext(self):
        return self.next
    
    def setNext(self, node_next):
        self.next = node_next 
         
    def __str__(self):
        return str(self.data)
        
   