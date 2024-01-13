import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, K = g()
nums = sorted(g())
ans = 0
l, r = 0, N - 1
while l < r:
    s = nums[l] + nums[r]
    if s <= K:
        ans += 1
        l += 1
    r -= 1
print(ans)