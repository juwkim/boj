g = lambda: [*map(int, input().split())]
from copy import deepcopy
from math import dist
N = int(input())
cows = [g() for _ in range(N)]
tmp = deepcopy(cows)
idx = 0
for _ in range(N-1):
    r_idx = min(range(len(cows)), key=lambda x: dist(cows[idx], cows[x]) + 1e10 * (x == idx))
    del cows[r_idx]
    idx += r_idx > idx
    idx %= len(cows)
print(tmp.index(cows[0])+1)