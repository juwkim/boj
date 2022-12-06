N = int(input())
nums = [[*map(int, input().split())] for _ in range(N)]
dp = [nums[0]] + [[0, 0, 0] for _ in range(N-1)]
for i in range(1, N):
    dp[i][0] = nums[i][0] + min(dp[i-1][1], dp[i-1][2])
    dp[i][1] = nums[i][1] + min(dp[i-1][0], dp[i-1][2])
    dp[i][2] = nums[i][2] + min(dp[i-1][0], dp[i-1][1])
print(min(dp[N-1]))