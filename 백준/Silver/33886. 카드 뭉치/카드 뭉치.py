N, *A = map(int, open(0).read().split())
dp = [0] + [1e9] * N
for i in range(N):
    for j in range(i + 1, min(i + A[i], N) + 1):
        dp[j] = min(dp[j], dp[i] + 1)
print(dp[N])