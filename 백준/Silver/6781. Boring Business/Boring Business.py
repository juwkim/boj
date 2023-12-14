import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

check = {(0, -1), (0, -2), (0, -3), (1, -3), (2, -3), (3, -3), (3, -4), (3, -5),
         (4, -5), (5, -5), (5, -4), (5, -3), (6, -3), (7, -3), (7, -4), (7, -5),
         (7, -6), (7, -7), (6, -7), (5, -7), (4, -7), (3, -7), (2, -7), (1, -7),
         (0, -7), (-1, -7), (-1, -6), (-1, -5)}

x, y = -1, -5
while True:
    d, num = input().split()
    if d == 'q':
        break
    if d == 'l':
        dx, dy = -1, 0
    elif d == 'r':
        dx, dy = 1, 0
    elif d == 'u':
        dx, dy = 0, 1
    else:
        dx, dy = 0, -1
    danger = False
    for i in range(int(num)):
        x += dx
        y += dy
        if (x, y) in check:
            danger = True
        check.add((x, y))
    if danger:
        print(x, y, "DANGER")
        break
    else:
        print(x, y, "safe")