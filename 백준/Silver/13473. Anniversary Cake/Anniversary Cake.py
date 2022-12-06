g = lambda: [*map(int, input().split())]

w, h, ax, ay, bx, by = g()
if ax == bx:
    print(0, ay, w, by)
else:
    print(ax, 0, bx, h)