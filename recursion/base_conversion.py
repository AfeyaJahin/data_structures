
def convert(an_int,base):
    convert_str = "0123456789ABCDEFGHIJKLMNOPQRSTWXYZ"  
    if an_int < base:
        return convert_str[an_int]
    else:
        return convert(an_int//base, base) + convert_str[an_int%base] 
    
print(convert(10, 2))
    
