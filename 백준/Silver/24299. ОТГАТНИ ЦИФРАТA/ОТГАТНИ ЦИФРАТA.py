import re

def is_valid_number(num_str):
    if num_str in ('0', '-0'):
        return True
    if num_str.startswith('-'):
        num_str = num_str[1:]
    return not (num_str.startswith('0') and len(num_str) > 1)

def solve(equation):
    match = re.match(r'([-?0-9]+)([+\-*])([-?0-9]+)=(\-?[0-9?]+)', equation)
    # if not match:
    #     return "mistake"
    
    num1, op, num2, result = match.groups()
    existing_digits = {*equation} - {'?-+*='}
    
    for digit in range(10):
        digit = str(digit)
        if digit in existing_digits:
            continue
        replaced_expr = equation.replace('?', digit)
        match_replaced = re.match(r'([-0-9]+)([+\-*])([-0-9]+)=([-0-9]+)', replaced_expr)
        if not match_replaced:
            continue
        num1_r, op_r, num2_r, result_r = match_replaced.groups()
        if not (is_valid_number(num1_r) and is_valid_number(num2_r) and is_valid_number(result_r)):
            continue
        expression = f"{num1_r} {op_r} {num2_r}"
        try:
            if eval(expression) == int(result_r):
                return digit
        except:
            pass
    return "mistake"

print(solve(input()))