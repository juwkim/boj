N = int(input())
nums = [*map(int, input().split())]
dp = [nums[0]]

for i in range(1, len(nums)):
    temp = 0
    for j in range(i):
        if nums[j] < nums[i]:
            temp = max(temp, dp[j])
    dp.append(temp + nums[i])
print(max(dp))