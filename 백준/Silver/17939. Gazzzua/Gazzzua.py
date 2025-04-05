N, *nums = map(int, open(0).read().split())
ans, m = 0, 0
for num in reversed(nums):
    m = max(m, num)
    ans += m - num
print(ans)