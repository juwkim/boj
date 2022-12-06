from math import pi
def solve(i, j):
    if dp[i][j]:
        return dp[i][j]
    if 0 <= i - j * pi <= pi:
        dp[i][j] = 1
        return 1
    dp[i][j] = (solve(i - 1, j) + solve(i, j + 1)) % mod
    return dp[i][j]
    
    
mod = 10**18
n = int(input())
dp = [[0] * (n + 1) for _ in range(n + 1)]
print(solve(n, 0))