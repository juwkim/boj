N, *A = map(int, open(0).read().split())
dp = [0] * N
for i in range(N):
    dp[i] = (sum(dp[j] for j in range(i) if A[j] < A[i]) + 1) % 998_244_353
print(*dp)