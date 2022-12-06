g = lambda: [*map(int, input().split())]

n, p = g()
nums = sorted(g())
ans = -1
for i in range(n):
    ans = max(ans, p * (i + 1) - nums[i])
print(ans + nums[0])