import sys
g = lambda: [*map(int, sys.stdin.readline().split())]
from itertools import pairwise

N, M = g()
s = [[0] * (M + 1)] + [[0] + g() for _ in range(N)]
print(2 * (N * M + sum(sum(b - a for a, b in pairwise(l) if a < b) for l in s) + sum(sum(b - a for a, b in pairwise(l) if a < b) for l in zip(*s))))