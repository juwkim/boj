d = 0
closed = False
s = ''.join(open(0).read().split())
for i, c in enumerate(s):
    match c:
        case '{':
            if d:
                print(" ", end='')
            d += 4
            print('{')
            print(' ' * d, end='')
        case ';':
            print(';')
            if i + 1 < len(s) and s[i + 1] == '}':
                d -= 4
            print(' ' * d, end='')
        case ',':
            print(", ", end='')
        case _:
            print(c, end='')