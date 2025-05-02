''' CALCULATOR
Takes input like a calculator

Operators: +, -, *, /
Values: integer, float

(2 + 6 * 3)^2 - 10

'''

# Simple Version: takes only two inputs


import math

def solve(val1, val2, oper):
    if oper == '+':
        answer = val1 + val2
    elif oper == '-':
        answer = val1 - val2
    elif oper == '*':
        answer = val1 * val2
    elif oper == '/':
        answer = val1 / val2
    elif oper == '^':
        answer = math.pow(val1, val2)

    return answer


### MAIN FUNCTION ###
val1 = int(input("Enter first value: "))
oper = input("[+, -, *, /, ^]: ")
val2 = int(input("Enter second value: "))

print(solve(val1, val2, oper))