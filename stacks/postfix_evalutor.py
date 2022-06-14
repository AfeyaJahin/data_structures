from stack import Stack

def postfix_evaluator(my_str):
    my_list = my_str.split()
    num_stack = Stack()
    numbers = "0123456789"
    
    for element in my_list:
        if element in numbers:
            num_stack.push(int(element))
        else:
            sec_operand = num_stack.pop()
            first_operand = num_stack.pop()
            new_number = int(do_math(element,first_operand,sec_operand))
            num_stack.push(new_number)
    return new_number

def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    elif op == "**":
        return op1 ** op2     
    else:
        return op1 - op2

    

print(postfix_evaluator("5 9 *")) #45
print(postfix_evaluator("7 8 + 3 2 + /")) #3


  