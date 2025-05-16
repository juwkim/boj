from math import dist

for tc in range(1, int(input()) + 1):
    x1, y1, x2, y2, x3, y3 = map(int, input().split())
    p = [(x1, y1), (x2, y2), (x3, y3)]
    cx, cy, cr = None, None, 1e9
    for i, j, k in (0, 1, 2), (0, 2, 1), (1, 2, 0):
        tx, ty = (p[i][0] + p[j][0]) / 2, (p[i][1] + p[j][1]) / 2
        tr = dist(p[i], (tx, ty))
        if dist(p[k], (tx, ty)) <= tr < cr:
            cx, cy, cr = tx, ty, tr
    if cx is None:
        D = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
        cx = ((x1**2 + y1**2) * (y2 - y3) + (x2**2 + y2**2) * (y3 - y1) + (x3**2 + y3**2) * (y1 - y2)) / D
        cy = ((x1**2 + y1**2) * (x3 - x2) + (x2**2 + y2**2) * (x1 - x3) + (x3**2 + y3**2) * (x2 - x1)) / D
    print(f"Case #{tc}: {cx:.2f} {cy:.2f}")