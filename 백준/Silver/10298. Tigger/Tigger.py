import sys
input = sys.stdin.readline

for _ in range(int(input())):
    R, C, K, P = map(int, input().split())
    dp = [[[0 < i <= R and 0 < j <= C for j in range(C + 2)] for i in range(R + 2)] for _ in range(2)]
    for p in range(K - 1):
        for i in range(1, R + 1):
            for j in range(1, C + 1):
                dp[~p&1][i][j] = (dp[p&1][i - 1][j] + dp[p&1][i + 1][j] + dp[p&1][i][j - 1] + dp[p&1][i][j + 1] + dp[p&1][i][j]) % P
    ans = 0
    for row in dp[~K&1]:
        ans = (ans + sum(row)) % P
    print(ans)