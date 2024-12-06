import sys
input = sys.stdin.readline
MIS = lambda: [*map(int, input().split())]
from itertools import combinations

N = int(input())
nums = [MIS() for _ in range(N)]
r1, g1, b1 = MIS()
ans = 1e9
for i in range(2, min(N, 7) + 1):
    for colors in combinations(nums, i):
        r2, g2, b2 = 0, 0, 0
        for r, g, b in colors:
            r2 += r
            g2 += g
            b2 += b
        r2, g2, b2 = r2 // i, g2 // i, b2 // i
        ans = min(ans, abs(r1 - r2) + abs(g1 - g2) + abs(b1 - b2))
print(ans)