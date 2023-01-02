change = 100 - int(input())
coins = (25, 10, 5, 1)
for coin in coins:
    q, change = divmod(change, coin)
    print(q, end=' ')