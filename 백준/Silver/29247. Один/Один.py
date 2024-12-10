d = 0
for c in input():
    if c == '(':
        match d:
            case 0: c = '{'
            case 1: c = '['
            case _: c = '('
        d += 1
    elif c == ')':
        d -= 1
        match d:
            case 0: c = '}'
            case 1: c = ']'
            case _: c = ')'
    print(c, end='')