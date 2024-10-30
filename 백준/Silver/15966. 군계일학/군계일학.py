N, *a = map(int, open(0).read().split())
dp = [0] * 1000000
for num in a:
    dp[num] = dp[num - 1] + 1
print(max(dp))