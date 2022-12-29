n, k, *coins = map(int, open(0).read().split())
dp = [1] + [0] * k
for coin in coins:
    for idx in range(coin, k + 1):
        dp[idx] += dp[idx - coin]    
print(dp[-1])