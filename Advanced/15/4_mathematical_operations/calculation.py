from math import pow
def add(number1,number2):
    return number1+number2
def subtract(number1,number2):
    return number1-number2
def multiply(number1,number2):
    return number1*number2
def divide(number1,number2):
    return number1/number2
def power(number1,number2):
    return pow(number1,number2)
def figure_out(number1,number2, sign):
    if sign=="+":
        return add(number1,number2)
    elif sign=="-":
        return subtract(number1,number2)
    elif sign=="*":
        return multiply(number1,number2)
    elif sign=='/':
        return divide(number1,number2)
    elif sign=='^':
        return power(number1,number2)
