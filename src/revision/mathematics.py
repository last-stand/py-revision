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
    pass

def hcf(list):
    pass

