from math import dist

ax, ay, bx, by, px, py, r = map(int, input().split())
a, b, p = (ax, ay), (bx, by), (px, py)
print(min(dist(a, b), max(0, dist(a, p) - r) + max(0, dist(b, p) - r)))