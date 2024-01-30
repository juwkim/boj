import sys
input = lambda: sys.stdin.readline().rstrip()
g = lambda: map(int, input().split())

n, x = g()
nums = sorted(g())
l, r = 0, n - 1
ans = 0
while l < r:
    Sum = nums[l] + nums[r]
    if Sum <= x:
        ans = max(ans, Sum)
    if Sum < x:
        l += 1
    else:
        r -= 1
print(ans)