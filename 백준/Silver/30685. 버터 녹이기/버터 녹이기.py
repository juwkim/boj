import sys
input = sys.stdin.readline
from itertools import pairwise

ans = 1e9
for (x1, h1), (x2, h2) in pairwise(sorted([*map(int, input().split())] for _ in range(int(input())))):
    gap = x2 - x1 - 1
    if gap >= h1 // 2 + h2 // 2:
        continue
    ans = min(ans, max(gap - h1 // 2, gap - h2 // 2, gap // 2))
print((ans, "forever")[ans == 1e9])