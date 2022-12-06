n, m = map(int, input().split())
dp = [[0 for i in range(m+1)] for j in range(n+1)]

def solve(n, m):
    if dp[n][m]:
        return dp[n][m]
    elif m == n or m == 0:
        return 1
    else:
        s = solve(n-1, m) + solve(n-1, m-1)
        dp[n][m] = s
        return dp[n][m]
print(solve(n, m))