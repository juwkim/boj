def P4(x, y):
    if (x, y) == (0, 0):
        return '0.0'
    if (x, y) == (0, -1):
        return '0.2'
    if y & 1:
        y += 1
        l = ['.2']
    else:
        l = ['.0']
    i = 0
    while x or y:
        if i & 1:
            l.append(str(y % 8 >> 1))
            y = -((y - y % 8) // 4)
        else:
            l.append(str(x % 4))
            x = -(x // 4)
        i += 1
    return ''.join(reversed(l))