import sys
input = sys.stdin.readline
g = lambda: [*map(int, input().split())]
from bisect import bisect

W, H, K = g()
N, prv = int(input()), 0
nums = []
for y in g() + [H]:
    nums.append(y - prv)
    prv = y
nums.sort()
M, prv = int(input()), 0
ans = 0
for x in g() + [W]:
    ans += bisect(nums, K // (x - prv))
    prv = x
print(ans)