import sys
input = sys.stdin.readline
from bisect import bisect

nums = [[*map(int, input().split())] for _ in range(int(input()))]
h = [int(input()) for _ in range(int(input()))]
ans = 0
for s, t in nums:
    if t < h[0] or s > h[-1]:
        continue
    a = bisect(h, s)
    b = bisect(h, t)
    if h[a - 1] == s or a != b:
        ans += 1
print(ans)