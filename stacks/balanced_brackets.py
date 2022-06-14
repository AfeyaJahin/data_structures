from stack import Stack 
def balanced_checker(my_str):
    s = Stack()
    for brac in my_str:
        if brac in "([{":
            s.push(brac)
        else:
            if s.is_empty():
                return False
            elif brac == "]" and s.peek() == "["\
                or brac == "}" and s.peek()== "{"\
                or brac == ")" and s.peek()== "(":
                s.pop()
            #else:
                #if not matches(s.pop(), brac):
                    #return False       
    return s.is_empty()

#def matches(l_symbol, r_symbol):
    #left = "([{"
    #right =")]}" 
    #return left.index(l_symbol) == right.index(r_symbol)


print(balanced_checker('{({([][])}())}')) #True
print(balanced_checker('[{()]')) #False