N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
total = 0
for coin in reversed(coins):
    r, change = divmod(K, coin)
    total += r
    K = change
print(total)