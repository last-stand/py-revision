import math
def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total

def factorial(num):
    if num == 0:
        return 1
    else:
        for i in range(num + 1):
            result = num * factorial(num - 1)
            
        return result


def convert_temperature(value, unit):
    if unit == 'C':
        return round((value * (9 / 5)) + 32, 2)
    return round((value - 32) * (5/9), 2)


def lcm(list):
    lcm = list[0]
    n = len(list)
    for i in range(1, n):
        lcm = lcmOfTwoNumbers(lcm, list[i])

    return lcm
  
def hcf(list):
    hcf = list[0]
    n = len(list)
    for i in range(1, n):
        hcf = hcfOfTwoNumbers(hcf, list[i])

    return hcf
    
def hcfOfTwoNumbers(num1,num2):
    if num2 == 0:
        return num1
    return hcfOfTwoNumbers(num2, num1%num2)

def lcmOfTwoNumbers(num1,num2):
    return (num1 * num2) // hcfOfTwoNumbers(num1,num2)

def fibonacci(n):
    if n <= 1:
        return n
    return (fibonacci(n - 1) + fibonacci(n - 2))