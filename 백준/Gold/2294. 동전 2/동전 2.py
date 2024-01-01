import sys

input = lambda: sys.stdin.readline().rstrip()
g = lambda: [*map(int, input().split())]

n, k = g()
coins = [int(input()) for _ in range(n)]
dp = [0] + [10**9] * k
for coin in coins:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)
print(dp[k] if dp[k] != 10**9 else -1)