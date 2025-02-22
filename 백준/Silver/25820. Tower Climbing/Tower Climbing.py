n, k, *x = map(int, open(0).read().split())
dp = [0] * n
for i in range(1, n):
    dp[i] = min(dp[j] + (i - j) ** 2 + abs(x[i] - x[j]) for j in range(max(0, i - k), i))
print(dp[-1])