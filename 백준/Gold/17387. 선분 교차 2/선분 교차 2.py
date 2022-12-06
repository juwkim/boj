def cross(x1, y1, x2, y2, x3, y3):
    x2 -= x1
    x3 -= x1
    y2 -= y1
    y3 -= y1
    return x2 * y3 - x3 * y2

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

a = cross(x1, y1, x2, y2, x3, y3) * cross(x1, y1, x2, y2, x4, y4)
b = cross(x3, y3, x4, y4, x1, y1) * cross(x3, y3, x4, y4, x2, y2)

if a + b:
    print(int(a <= 0 and b <= 0))
else:
    x1, x2 = sorted([x1, x2])
    x3, x4 = sorted([x3, x4])
    if x4 > x2:
        print(int(x3 <= x2))
    elif x4 < x2:
        print(int(x1 <= x4))
    else:
        y1, y2 = sorted([y1, y2])
        y3, y4 = sorted([y3, y4])
        if y4 > y2:
            print(int(y3 <= y2))
        elif y4 < y2:
            print(int(y1 <= y4))
        else:
            print(1)
