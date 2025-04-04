import sys
g = lambda: map(int, sys.stdin.readline().split())

N, M, A, B = g()
dp = [0, *[1e9] * N]
for _ in range(M):
    L, R = g()
    for i in range(L, R + 1):
        dp[i] = -1
for i in range(N):
    if dp[i] == -1:
        continue
    if i + A <= N and dp[i + A] != -1:
        dp[i + A] = min(dp[i + A], dp[i] + 1)
    if i + B <= N and dp[i + B] != -1:
        dp[i + B] = min(dp[i + B], dp[i] + 1)
print((dp[N], -1)[dp[N] == 1e9])