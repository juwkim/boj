import sys
input = sys.stdin.readline
from itertools import combinations

P = []
N = int(input())
for _ in range(N):
    name, x, y = input().split()
    P.append((name, int(x), int(y)))
printed = False
for (name1, x1, y1), (name2, x2, y2), (name3, x3, y3) in combinations(P, 3):
    if (x2 - x1) * (y3 - y1) != (x3 - x1) * (y2 - y1):
        print(name1, name2, name3)
        printed = True
if not printed:
    print("No triangles.")