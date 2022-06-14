def reverse_str(str):
    
    if len(str)==1:
        return str
    else:
        return reverse_str(str[1:]) + str[0]  
    
print(reverse_str("hello"))
