n = int(input())
triangles = sorted(map(int, input().split()))
circles = sorted(map(int, input().split()))

dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
dp[0] = [0] * (n + 1)
for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = dp[i][j-1]
        if triangles[i-1] < circles[j-1]:
            dp[i][j] = min(dp[i][j], dp[i-1][j-1] + abs(triangles[i-1] - circles[j-1]))
print(dp[n][n])