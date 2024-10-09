import sys
input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 1)
for i in range(1, N + 1):
    T, P = map(int, input().split())
    dp[i] = max(dp[i], dp[i - 1])
    if i + T - 1 <= N:
        dp[i + T - 1] = max(dp[i + T - 1], dp[i - 1] + P)
print(dp[N])