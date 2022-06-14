from stack import Stack 
def base_converter(dec_num, base):
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTWXYZ"
    s = Stack()
    converted_num = ''
    if dec_num ==0:
        converted_num += "0"
    else:
        while dec_num > 0:
            rem = dec_num%base
            s.push(rem)
            dec_num = dec_num//base 
    while not s.is_empty():
        converted_num += digits[s.pop()]
        
    return converted_num

print(base_converter(233,8)) #351
print(base_converter(233,16)) #E9
    