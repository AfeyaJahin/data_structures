from stack import Stack
def dec_to_binary(dec_num):
    s = Stack()
    binary = ''
    if dec_num == 0:
        binary = binary + "0"    
    else:
        while dec_num > 0:
            rem = dec_num % 2 
            s.push(rem)
            dec_num = dec_num//2
            
    while not s.is_empty():
        binary = binary + str(s.pop())
    return binary
    
            
print(dec_to_binary(0)) #0
print(dec_to_binary(11)) # 1011
print(dec_to_binary(233)) #11101001
