xs, ys, xe, ye, dx, dy = map(int, open(0).read().split())
if dx == 0 and dy == 0:
    print(xe, ye)
elif dx == 0:
    if (ys - ye) * dy > 0:
        print(xe, ys)
    else:
        print(xe, ye)
elif dy == 0:
    if (xs - xe) * dx > 0:
        print(xs, ye)
    else:
        print(xe, ye)
else:
    if (xs - xe) * dx > 0:
        x = (dx**2 * xs + dy**2 * xe + dx * dy * (ys - ye)) // (dx**2 + dy**2)
        y = dy * (x - xe) // dx + ye
        print(x, y)
    else:
        print(xe, ye)