def check_anagram(s1,s2):
    still_ok = True
    if len(s1) != len(s2):
        still_ok = false 
    s2 = list(s2)
    for i in range(len(s1)):
        if s1[i] in s2 and still_ok:
            index_element = s2.index(s1[i]) 
            s2[index_element] = None
            still_ok = True 
            
    for k in s2:
        if k != None:
            still_ok = False
    
    return still_ok
            
       
print(check_anagram("apple", "pleap"))  # expected: True
print(check_anagram("abcd", "dcba"))  # expected: True
print(check_anagram("abcd", "dcda"))  # expected: False


""" Checking off O(n^2)"""
def anagram_solution_1(s1, s2):
    still_ok = True
    if len(s1) != len(s2):
        still_ok = False

    a_list = list(s2)
    pos_1 = 0

    while pos_1 < len(s1) and still_ok:
        pos_2 = 0
        found = False
        while pos_2 < len(a_list) and not found:
            if s1[pos_1] == a_list[pos_2]:
                found = True
            else:
                pos_2 = pos_2 + 1

        if found:
            a_list[pos_2] = None
        else:
            still_ok = False

        pos_1 = pos_1 + 1

    return still_ok


print(anagram_solution_1("apple", "pleap"))  # expected: True
print(anagram_solution_1("abcd", "dcba"))  # expected: True
print(anagram_solution_1("abcd", "dcda"))  # expected: False

"""Sort and Compare
The two calls to the Python sort method are not without their own cost. 
sorting is typically either 𝑂(𝑛2) or 𝑂(𝑛log𝑛),so the sorting operations dominate the iteration.
This algorithm will have the same order of magnitude as that of the sorting process.
"""
def anagram_solution_2(s1, s2):
    a_list_1 = list(s1)
    a_list_2 = list(s2)

    a_list_1.sort()
    a_list_2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if a_list_1[pos] == a_list_2[pos]:
            pos = pos + 1
        else:
            matches = False

    return matches


print(anagram_solution_2("apple", "pleap"))  # expected: True
print(anagram_solution_2("abcd", "dcba"))  # expected: True
print(anagram_solution_2("abcd", "dcda"))  # expected: False

"""Count and Compare O(n)"""
def anagram_solution_4(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        # find what letter and then increment number by 1
        # suppose 103 (g) - 97(a) tells us it is the 6th letter in the alphabet
        # increment element in list c1 by 1
        pos = ord(s1[i]) - ord("a")
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        # same thing just for second list
        pos = ord(s2[i]) - ord("a")
        c2[pos] = c2[pos] + 1

    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            still_ok = False

    return still_ok


print(anagram_solution_4("apple", "pleap"))  # expected: True
print(anagram_solution_4("abcd", "dcba"))  # expected: True
print(anagram_solution_4("abcd", "dcda"))  # expected: False

