N, K = map(int, input().split())
dp = {}
def solve(i):
    if i in dp:
        return dp[i]
    if i < K + 2 or (i - K) & 1:
        return 1
    dp[i] = solve((i - K) // 2) + solve((i + K) // 2)
    return dp[i]
print(solve(N))