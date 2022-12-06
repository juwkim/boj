n, m = map(int, input().split())
nums = [*map(int, input().split())]

cur = sum(nums[i] for i in range(m))
ans = cur
for i in range(m, n):
    cur += nums[i] - nums[i-m]
    ans = max(ans, cur)
print(ans)