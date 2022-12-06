money = int(input())
prices = [*map(int, input().split())]
BNP_money, Timing_money = money, money
BNP_stock, Timing_stock = 0, 0
plus, minus, yester_price = -1, 0, 0
for price in prices:
    if BNP_money >= price:
        plus_stock = BNP_money // price
        BNP_stock += plus_stock
        BNP_money -= plus_stock * price
    if price > yester_price:
        plus += 1
        minus = 0
    elif price < yester_price:
        plus = 0
        minus -= 1
    else:
        plus, minus = 0, 0

    if plus >= 3:
        Timing_money += Timing_stock * price
        Timing_stock = 0
    elif minus <= -3:
        plus_stock = Timing_money // price
        Timing_stock += plus_stock
        Timing_money -= plus_stock * price
    yester_price = price
        
BNP = BNP_money + BNP_stock * prices[-1]
TIMING = Timing_money + Timing_stock * prices[-1]
print(['SAMESAME', 'BNP', 'TIMING'][(BNP > TIMING) - (BNP < TIMING)])