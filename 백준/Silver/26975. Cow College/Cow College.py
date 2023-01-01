N = int(input())
nums = sorted(map(int, input().split()), reverse=True)
ans, cost = nums[-1], nums[-1] * N
for i in range(N - 1):
    if nums[i] > nums[i + 1] and nums[i] * (i + 1) >= cost:
        ans = nums[i]
        cost = nums[i] * (i + 1)
print(cost, ans)