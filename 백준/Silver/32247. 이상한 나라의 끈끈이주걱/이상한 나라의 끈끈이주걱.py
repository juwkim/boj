import sys
g = lambda: [*map(int, sys.stdin.readline().split())]

N, M = g()
curx, cury = 0, 0
for c, x, h in sorted([g() for _ in range(M)], key=lambda i: i[1]):
    if c:
        cury += curx - x
        if h <= cury:
            idx = 1
            break
    else:
        cury = max(cury + curx - x, h + 1)
    curx = x
else:
    idx = curx + cury > N
print(("stay", "adios")[idx])