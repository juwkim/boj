n, *a = map(int, open(0).read().split())
dp = [0] * n
for i in range(n):
    dp[i] = a[i] + max([dp[j] for j in range(i) if a[j] < a[i]], default=0)
print(max(dp))