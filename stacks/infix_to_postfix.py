from stack import Stack

def infix_to_postfix(my_str):
    op_stack = Stack()
    output_list = []
    my_list = my_str.split()
    op = "+-*/"
    operand = "ABCDEFGHIJKLMNOPQRST0123456789"
    prec = {"+":2, "-":2, "*": 3, "/": 3, "(": 1, ")":1, "**": 4}
    for element in my_list:
        if element in operand:
            output_list.append(element)
        elif element == "(":
            op_stack.push(element)
        #pop last two stack items, append only the operator
        elif element == ")":
            output_list.append((op_stack.pop()))
            op_stack.pop()
        # if empty or higher precedence
        elif op_stack.is_empty() or (prec[element] > prec[op_stack.peek()]):
            op_stack.push(element)
        else:
            #if lower precedence, pop the previous higher precedence operator, then add to stack
            if (element in op) and (prec[element] <= prec [op_stack.peek()]):
                output_list.append((op_stack.pop()))
                op_stack.push(element)
    
    # append leftover operators from the stack       
    while not op_stack.is_empty():
        output_list.append(op_stack.pop())  
    
    #list to string
    return " ".join(output_list)       
    
        
print(infix_to_postfix("A * B + C * D")) #A B + C * D E - F G + * -
print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )")) #A B + C * D E - F G + * -  
print(infix_to_postfix("( A + B ) * ( C + D )")) #A B + C D + *
print(infix_to_postfix("( A + B ) * C")) #A B + C *
print(infix_to_postfix("A + B * C")) #A B C * +
print(infix_to_postfix("5 * 3 ** ( 4 - 2 )"))