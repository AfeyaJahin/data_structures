# Given an array, find the average of all sub arrays of ‘K’ contiguous elements in it.

#inefficient O(N*k)
def sub_average(my_list, k):
    result = []
    
    for j in range(len(my_list)-k+1):
        sum = 0
        for i in range(j, j+k):
            sum = sum + my_list[i]
        result.append(sum/k)
    return result

#more efficient using brute force algorithm O(N)
def sub_average_2(arr,k):
    result = []
    sum = 0.0
    window_start = 0
    for element in range(len(arr)):
        sum += arr[element] #keep adding elements to sum
        if element >= k-1: #if we hit window size of k
            result.append(sum/k)
            sum -= arr[window_start] #subtract the element going out of window
            window_start += 1 
    return result
        
        
        
        
array = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
print(sub_average_2(array,k))

    
    