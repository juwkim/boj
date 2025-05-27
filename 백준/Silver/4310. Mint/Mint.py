import sys
from math import lcm
from itertools import combinations
input = sys.stdin.readline

while (l:=[*map(int, input().split())])[0]:
    n, t = l
    coins = [int(input()) for _ in range(n)]
    for _ in range(t):
        h = int(input())
        lo, hi = 0, 1e9
        for c4 in combinations(coins, 4):
            num = lcm(*c4)
            lo = max(lo, h // num * num)
            hi = min(hi, (h + num - 1) // num * num)
        print(lo, hi)