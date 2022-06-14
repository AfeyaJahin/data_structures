"""Write two Python functions to find the minimum number in a list. 
The first function should compare each number to every other number on the list. 𝑂(𝑛2).
The second function should be linear 𝑂(𝑛)."""

def min_num(my_list):
    minimum = my_list[0]
    for i in range(1, len(my_list)):
        if minimum > my_list[i]:
            minimum = my_list[i]
    return minimum
my_list = [3, 2, 5, 9, 8, 10, 11, 13, 2, 3, 1]
print(min_num(my_list))   

    
    