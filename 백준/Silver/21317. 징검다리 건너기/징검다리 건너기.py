import sys
input = sys.stdin.readline

N = int(input())
nums = [[*map(int, input().split())] for _ in range(N - 1)]
K = int(input())
dp = [[1e9, 1e9] for _ in range(N + 2)]
dp[0] = [0, 0]
for i in range(N - 1):
    dp[i + 1][0] = min(dp[i + 1][0], dp[i][0] + nums[i][0])
    dp[i + 1][1] = min(dp[i + 1][1], dp[i][1] + nums[i][0])
    dp[i + 2][0] = min(dp[i + 2][0], dp[i][0] + nums[i][1])
    dp[i + 2][1] = min(dp[i + 2][1], dp[i][1] + nums[i][1])
    dp[i + 3][1] = min(dp[i + 3][1], dp[i][0] + K)
print(min(dp[N - 1]))