m, n, k = map(int, input().split())
prices = [float(input()) for _ in range(k)]
buy, sell = 1, 1
for i in range(n, k+1):
    a, b = sum(prices[i-m:i]) / m, sum(prices[i-n:i]) / n
    if buy and a > b:
        print('BUY ON DAY', i)
        buy, sell = 0, 1
    elif sell and a < b:
        print('SELL ON DAY', i)
        buy, sell = 1, 0