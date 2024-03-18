import sys
input = sys.stdin.readline
from bisect import bisect

nums = [[*map(int, input().split())] for _ in range(int(input()))]
h = [int(input()) for _ in range(int(input()))]
ans = 0
for s, t in nums:
    a, b = bisect(h, s), bisect(h, t)
    ans += h[a - 1] == s or a != b
print(ans)