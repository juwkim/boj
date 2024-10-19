N, *A = map(int, open(0).read().split())
dp = [0] + [1e9] * (N - 1)
for i in range(N - 1):
    for j in range(i + 1, N):
        if dp[j] > dp[i]:
            dp[j] = min(dp[j], max(dp[i], (j - i) * (1 + abs(A[j] - A[i]))))
print(dp[-1])