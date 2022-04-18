import math
#matematicka kniznica

error_message_1 = "ERROR - division by zero"

#factorial function
def factorial(n):
    fact = 1
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
            return
    else:
        return op1 ** (1 / op2)




