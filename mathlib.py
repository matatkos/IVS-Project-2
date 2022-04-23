import math
#matematicka kniznica

#error message when division by zero occures
error_message_1 = "ERROR - division by zero"

#error message when root of negative number with even number
error_message_root = "ERROR - root laws were not obeyed"

#error message for using factorial function on negative or decimal number
error_message_fact = "ERROR - factorial laws were not obeyed"

#factorial function
def factorial(n):
    fact = 1
    if n< 0:
        return error_message_fact
    if n % 1 > 0:
        return error_message_fact
    for i in range(1, n + 1):
        fact = fact * i
    return fact

#sinus function
def sin(n):
    return math.sin(n)

#cosinus
def cos(n):
    return math.cos(n)

#add
def add(op1,op2):
    return op1 + op2

#sub
def sub(op1,op2):
    return op1 - op2

#mul
def mul(op1,op2):
    return op1 * op2

#diviosion
def div(op1,op2):
    if op2 != 0:
        return op1 / op2
    return error_message_1

#power
def pow(op1,op2):
    if op1 <0:
        if not isinstance(op2, int):
            return error_message_root
    return op1**op2

#root
#1.operand (odmocnina z coho)
#2. operand (kolkata odmocnina)
def root(op1,op2):
    #if second operand is even number, first operand must be fron interval <0,inf)
    if op2%2 == 0:
        if op1 >=0:
            return op1 ** (1 / op2)
        else:
            return error_message_root
    else:
        if op1 < 0:
            op1 = abs(op1)
            return -abs(op1 ** (1 / op2))
        else:
            return op1 ** (1 / op2)



