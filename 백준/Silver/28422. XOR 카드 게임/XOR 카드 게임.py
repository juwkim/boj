N, *A = map(int, open(0).read().split())
dp = [0] + [-1] * N
for i in range(N - 1):
    if dp[i] == -1:
        continue
    if i + 3 <= N:
        dp[i + 3] = dp[i] + (A[i] ^ A[i + 1] ^ A[i + 2]).bit_count()
    if i + 2 <= N:
        dp[i + 2] = max(dp[i + 2], dp[i] + (A[i] ^ A[i + 1]).bit_count())
print(max(0, dp[N]))