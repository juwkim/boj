x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
x2, x3 = x2 - x1, x3 - x1
y2, y3 = y2 - y1, y3 - y1
a = x2 * y3 - x3 * y2
print((a > 0) - (a < 0))