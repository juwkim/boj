import sys
g = lambda: [*map(int, sys.stdin.readline().split())]
from itertools import combinations

N, K = g()
C = [g() for _ in range(N)]
print(max(sum(C[a][b] for a, b in combinations(G, 2)) for G in combinations(range(N), K)))