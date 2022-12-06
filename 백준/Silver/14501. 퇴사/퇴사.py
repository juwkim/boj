g = lambda: [*map(int, input().split())]

N = int(input())
dp = [0] * (N + 1)
for i in range(N):
    dp[i+1] = max(dp[:i+2])
    T, P = g()
    idx = i + T
    if idx <= N:
        dp[idx] = max(dp[idx], dp[i] + P)
print(dp[N])