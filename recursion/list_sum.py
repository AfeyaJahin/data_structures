
def recursive_sum(a_list):
    if len(a_list) == 1:
        return a_list[0]
    else:
        return a_list[0]+recursive_sum(a_list[1:])
    
print(recursive_sum([1,2,3,4,5,6]))