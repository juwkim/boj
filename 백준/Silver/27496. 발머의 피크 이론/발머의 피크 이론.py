import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, L = g()
nums = [0] * L + g()
ans = 0
cur = 0
for i in range(L, N + L):
    cur += nums[i] - nums[i - L]
    ans += 129 <= cur <= 138
print(ans)