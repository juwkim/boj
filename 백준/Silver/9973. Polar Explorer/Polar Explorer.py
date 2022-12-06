while (s:= input()) == 'START':
    x, y, z = map(int, input().split())
    dist = 12.56636 * x * min(z, 360 - z) / 360
    if dist > 5 * y:
        print('NO', 5 * y)
    else:
        print('YES', int(y - dist / 5))
    input()