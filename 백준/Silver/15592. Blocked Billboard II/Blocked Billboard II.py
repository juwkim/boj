x1, y1, x2, y2 = map(int, input().split())
m1, n1, m2, n2 = map(int, input().split())

if m1 <= x1 <= x2 <= m2:
    if n1 <= y1 <= y2 <= n2:
        print(0)
    elif n1 <= y1 <= n2 <= y2:
        y1 = n2
        print((x2 - x1) * (y2 - y1))
    elif y1 <= n1 <= y2 <= n2:
        y2 = n1
        print((x2 - x1) * (y2 - y1))
    else:
        print((x2 - x1) * (y2 - y1))
else:
    x1, y1, x2, y2 = y1, x1, y2, x2
    m1, n1, m2, n2 = n1, m1, n2, m2
    if m1 <= x1 <= x2 <= m2:
        if n1 <= y1 <= y2 <= n2:
            print(0)
        elif n1 <= y1 <= n2 <= y2:
            y1 = n2
            print((x2 - x1) * (y2 - y1))
        elif y1 <= n1 <= y2 <= n2:
            y2 = n1
            print((x2 - x1) * (y2 - y1))
        else:
            print((x2 - x1) * (y2 - y1))
    else:
        print((x2 - x1) * (y2 - y1))       