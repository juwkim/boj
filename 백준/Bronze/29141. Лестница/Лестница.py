g = lambda: [*map(int, input().split())]

xa, ya = g()
xb, yb = g()
a, b = g()
x, y = abs(xa - xb), abs(ya - yb)
if x // a >= (y + b - 1) // b:
    p = x // a
    print(x, p)
    print(y, p)
else:
    print(-1)