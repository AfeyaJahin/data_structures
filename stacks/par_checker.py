from stack import Stack

"""Explanation: This function, par_checker, returns a boolean result for balanced.
If the current symbol is (, then it is pushed on the stack.
If the stack becomes empty before we reach the end of the symbol_string,
then there are too many closing parentheses and the string is not balanced, 
so we immediately return False. At the end, the string represents a correctly balanced 
sequence of parentheses as long as the stack has been completely cleaned off."""
 
def better_par_checker(symbol_string):
    s = Stack()
    for symbol in symbol_string:
        if symbol == "(":
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            else:
                s.pop()

    return s.is_empty()

def par_checker(str):
    balanced = True
    s = Stack()
    for symbol in str:
        if symbol == "(":
            s.push(symbol)
        elif symbol == ")" and s.is_empty() == False:
            s.pop()
        else: 
            balanced = False
    if not s.is_empty():
        balanced = False
    return balanced 
        

print(par_checker("((()))"))  # expected True
print(par_checker("((()()))"))  # expected True
print(par_checker("(()"))  # expected False
print(par_checker(")("))  # expected False