import math
#matematicka kniznica

##
# @file mathlib.py
# @brief mathematical library for basic operations
#
# consists of addition, substraction, multiplication
# division, power, root, sinus, cosinus and
# factiorial
#
# @author Marek Buch (xbuchm02)
# @author David Jokay (xjokay02)
# @author Matus Snopek (xsnope04)
# @author Jan Spacek (xspace39)
#

#error message when division by zero occures
error_message_1 = "ERROR - division by zero"

#error message when root of negative number with even number
error_message_root = "ERROR - root laws were not obeyed"

#error message for using factorial function on negative or decimal number
error_message_fact = "ERROR - factorial laws were not obeyed"

##
# @brief function that calculates factorial
#
# @param n number of which we calculate the factorial
#
# @return fact number equal to the factorial on n
#

def factorial(n):
    fact = 1
    if n< 0:
        return error_message_fact
    if n % 1 > 0:
        return error_message_fact
    for i in range(1, n + 1):
        fact = fact * i
    return fact

##
# @brief function that calculates the sinus value of a number
#
# @param n number of which we calculate sinus
#
# @return math.sin(n) sinus of n calculated with the help of math library
#

def sin(n):
    return math.sin(n)

##
# @brief function that calculates the cosinus value of a number
#
# @param n number of which we calculate cosinus
#
# @return math.cos(n) cosinus of n calculated with the help of math library
#

def cos(n):
    return math.cos(n)

##
# @brief function that adds two numbers
#
# @param op1 the first number of the addition
# @param op2 the second number of the addition
#
# @return the sum of two numbers
#
def add(op1,op2):
    return op1 + op2

##
# @brief function that substracts two numbers
#
# @param op1 the first number of the substraction
# @param op2 the second number of the substraction
#
# @return the substraction of two numbers
#

#sub
def sub(op1,op2):
    return op1 - op2

##
# @brief function that multiplies two numbers
#
# @param op1 the first number of the multiplication
# @param op2 the second number of the multiplication
#
# @return the multiplication of two numbers
#

def mul(op1,op2):
    return op1 * op2

##
# @brief function that divides two numbers
#
# @param op1 dividend, the first number of the division
# @param op2 divisor, the second number of the division
#
# @return the division of two numbers
#
def div(op1,op2):
    if op2 != 0:
        return op1 / op2
    return error_message_1

##
# @brief function that calculates a number raised to a power
#
# @param op1 the base
# @param op2 the power
#
# @return the number raised to a power
#

def pow(op1,op2):
    if op1 <0:
        if not isinstance(op2, int):
            return error_message_root
    return op1**op2

##
# @brief function calculates the nth root of a nuber
#
# @param op1 the number of which we want root
# @param op2 the digree of the root
#
# @exception if second operand is an even number, first operand must be from interval <0
# @return nth root of a number
#

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



