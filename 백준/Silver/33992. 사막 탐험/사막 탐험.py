from math import dist

ax, ay, bx, by, px, py, r = map(int, input().split())
print(min(dist((ax, ay), (bx, by)), max(0, dist((ax, ay), (px, py)) - r) + max(0, dist((bx, by), (px, py)) - r)))