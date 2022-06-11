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
    pass

def lcm(list):
    pass

def hcf(list):
    pass

