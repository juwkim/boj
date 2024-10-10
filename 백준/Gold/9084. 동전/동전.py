import sys
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    coins = [*map(int, input().split())]
    M = int(input())
    dp = [1] + [0] * M
    for coin in coins:
        for j in range(coin, M + 1):
            dp[j] += dp[j - coin]
    print(dp[M])