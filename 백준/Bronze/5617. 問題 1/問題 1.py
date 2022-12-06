a, b, c, d = 0, 0, 0, 0
while True:
    x, y, z = sorted(map(int, input().split()))
    
    if x + y <= z:
        print(a, b, c, d)
        break

    if x**2 + y**2 == z**2:
        b += 1
    elif x**2 + y**2 > z**2:
        c += 1
    else:
        d += 1
    a += 1