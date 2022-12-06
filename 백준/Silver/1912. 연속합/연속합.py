g = lambda: [*map(int, input().split())]


N = int(input())
nums = g()
ans = nums[0]
cur = nums[0]
for i in range(1, N):
    cur = max(nums[i], cur + nums[i])
    ans = max(ans, cur)
print(ans)