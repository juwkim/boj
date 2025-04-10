from itertools import permutations
from math import comb

N, F = map(int, input().split())
c = [comb(N - 1, i) for i in range(N)]
for p in permutations(range(1, N + 1)):
    if sum(a * b for a, b in zip(p, c)) == F:
        print(*p)
        break