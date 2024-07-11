import sys
g = lambda: map(int, sys.stdin.readline().split())

N, M = g()
dp = [0] * (N + 1)
for _ in range(M):
    a, b = g()
    for i in range(N, a - 1, -1):
        dp[i] = max(dp[i], dp[i - a] + b)
print(dp[N])