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

print(int(a < 0 and b < 0))