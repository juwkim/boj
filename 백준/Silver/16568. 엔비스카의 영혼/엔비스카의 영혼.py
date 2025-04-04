N, a, b = map(int, input().split())
dp = [0] + [1e9] * N
for i in range(N):
    for k in (0, a, b):
        if i + k + 1 <= N:
            dp[i + k + 1] = min(dp[i + k + 1], dp[i] + 1)
print(dp[N])