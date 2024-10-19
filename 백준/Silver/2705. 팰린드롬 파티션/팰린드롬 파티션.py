dp = [0] * 1001
dp[0] = 1
def solve(n):
    if dp[n]: return dp[n]
    dp[n] = sum(solve(i) for i in range(n // 2 + 1))
    return dp[n]

for _ in range(int(input())):
    print(solve(int(input())))