from itertools import permutations
from math import gcd

for _ in range(int(input())):
    n = int(input())
    edges = [[*map(int, input().split())] for _ in range(n - 1)]
    for p in permutations(range(1, n + 1)):
        if all(gcd(p[u - 1], p[v - 1]) == 1 for u, v in edges):
            print(*p)
            break