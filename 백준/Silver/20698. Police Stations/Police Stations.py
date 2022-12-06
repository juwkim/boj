g = lambda: [*map(int, input().split())]

xmin, xmax = 1e9, -1e9
ymin, ymax = 1e9, -1e9
for _ in range(int(input())):
    x, y = g()
    xmin = min(xmin, x)
    xmax = max(xmax, x)
    ymin = min(ymin, y)
    ymax = max(ymax, y)
a = (xmax - xmin + 1) // 2
b = (ymax - ymin + 1) // 2
print(a, b)