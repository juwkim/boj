g = lambda: map(int, input().split())

from math import dist
from itertools import combinations
for _ in range(int(input())):
    p = [tuple(g()) for _ in range(4)]
    if len(set((dist(p[i], p[j]) for i, j in combinations(range(4), 2)))) == 2:
        print(1)
    else:
        print(0)