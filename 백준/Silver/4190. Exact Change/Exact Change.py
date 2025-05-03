import sys
input = sys.stdin.readline

for _ in range(int(input())):
    price = int(input())
    MAX, INF = 10000, 101
    dp = [INF] * (MAX + 1)
    dp[0] = 0
    for _ in range(int(input())):
        coin = int(input())
        for total in range(MAX, coin - 1, -1):
            if dp[total - coin] != INF:
                dp[total] = min(dp[total], dp[total - coin] + 1)
    i = price
    while dp[i] == INF:
        i += 1
    print(i, dp[i])