from queue import Queue

def hot_potato(names_list, num):
    q = Queue()
    for element in names_list:
        q.enqueue(element)
    while q.size()>1:
        for i in range(num):
            q.enqueue(q.dequeue())
        q.dequeue()
    
    return q.dequeue()

print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 7)) #susan
        
         
    