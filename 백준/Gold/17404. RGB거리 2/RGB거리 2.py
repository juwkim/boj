N = int(input())
nums = [[*map(int, input().split())] for _ in range(N)]
dp = [[[1000000, 1000000, 1000000] for _ in range(3)] for _ in range(N)]

dp[1][0][1], dp[1][0][2] = nums[1][1] + nums[0][0], nums[1][2] + nums[0][0]
dp[1][1][0], dp[1][1][2] = nums[1][0] + nums[0][1], nums[1][2] + nums[0][1]
dp[1][2][0], dp[1][2][1] = nums[1][0] + nums[0][2], nums[1][1] + nums[0][2]

for i in range(2, N):
    for j in range(3):
        dp[i][j][0] = nums[i][0] + min(dp[i-1][j][1], dp[i-1][j][2])
        dp[i][j][1] = nums[i][1] + min(dp[i-1][j][0], dp[i-1][j][2])
        dp[i][j][2] = nums[i][2] + min(dp[i-1][j][0], dp[i-1][j][1])

a = min(dp[N-1][0][1:])
b = min(dp[N-1][1][::2])
c = min(dp[N-1][2][:2])
print(min(a, b, c))