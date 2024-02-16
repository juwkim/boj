input()
r, g, b, y = 1, 0, 0, 0
for c in map(int, input().split()):
    match c:
        case 0: r, g, b, y = g, r, 0, b | y
        case 1: r, g, b, y = y, r, g | b, 0
        case -1: r, g, b, y = g | y, r, g | b, b | y
for c in r, g, b, y:
    print(("EI", "JAH")[c])