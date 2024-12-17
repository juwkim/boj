n, m, *x = map(int, open(0).read().split())
dp, mx = [0] * m, 0
for i in range(m, n):
    cur = mx + x[i]
    dp.append(cur)
    mx = max(mx, dp[i - m + 1])
print(max(dp))