import re

def is_valid(str):
    if str in ('0', '-0'):
        return True
    if str[0] == '-':
        str = str[1:]
    return str[0] != '0' or len(str) == 1

def solve(equation):    
    num1, op, num2, res = re.match(r'([-?0-9]+)([+\-*])([-?0-9]+)=(\-?[0-9?]+)', equation).groups()
    for digit in map(str, range(10)):
        if digit in equation: continue
        num1, op, num2, res = re.match(r'([-0-9]+)([+\-*])([-0-9]+)=([-0-9]+)', equation.replace('?', digit)).groups()
        if any(not is_valid(x) for x in (num1, num2, res)):
            continue
        try:
            if eval(f"{num1} {op} {num2}") == int(res):
                return digit
        except:
            pass
    return "mistake"

print(solve(input()))