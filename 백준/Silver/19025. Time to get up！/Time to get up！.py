def check(a, b, c, d, e, f, g):
    if a:
        if b:
            if c:
                if d:
                    if f:
                        return '8'
                    elif g:
                        return '9'
                    else:
                        return '3'
                else:
                    return '2'
            elif e:
                return '0'
            else:
                return '7'
        elif f:
            return '6'
        else:
            return '5'
    elif c:
        return '4'
    else:
        return '1'


for _ in range(int(input())):
    Map = [[i == 'X' for i in input()] for _ in range(7)]
    buf = []
    b = 1
    for i in range(4):
        buf.append(check(Map[0][b], Map[1][b+2], Map[3][b], Map[4][b+2], Map[6][b], Map[4][b-1], Map[1][b-1]))
        b += [5, 7, 5, 0][i]
    print(buf[0] + buf[1] + ':' + buf[2] + buf[3])