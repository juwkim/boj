import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

from math import inf
from itertools import combinations

def solve(idx, a, b, c, d):
    global ans
    if idx == 12:
        s, *_, S = sorted(map(sum, [a, b, c, d]))
        ans = min(ans, S - s)
        return
    if len(a) < 3:
        solve(idx + 1, a + [nums[idx]], b, c, d)
    if len(b) < 3:
        solve(idx + 1, a, b + [nums[idx]], c, d)
    if len(c) < 3:
        solve(idx + 1, a, b, c + [nums[idx]], d)
    if len(d) < 3:
        solve(idx + 1, a, b, c, d + [nums[idx]])
ans = inf
nums = [int(input()) for _ in range(12)]
solve(0, [], [], [], [])
print(ans)