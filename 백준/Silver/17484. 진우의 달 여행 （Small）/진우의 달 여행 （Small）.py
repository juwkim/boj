import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

N, M = g()
dp = [[[float("inf")]*3, *[[0]*3 for _ in range(M)], [float("inf")]*3] for _ in range(2)]
for i in range(N):
    cur, nxt = i&1, (i+1)&1
    nums = g()
    for j in range(1, M + 1):
        dp[nxt][j][0] = min(dp[cur][j-1][1], dp[cur][j-1][2]) + nums[j - 1]
        dp[nxt][j][1] = min(dp[cur][j][0], dp[cur][j][2]) + nums[j - 1]
        dp[nxt][j][2] = min(dp[cur][j+1][0], dp[cur][j+1][1]) + nums[j - 1]
print(min(min(l) for l in dp[N&1]))