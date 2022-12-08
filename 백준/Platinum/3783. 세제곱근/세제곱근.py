import decimal
decimal.getcontext().prec = 1000
pow_num = decimal.Decimal('1') / 3
for _ in range(int(input())):
    num = decimal.Decimal(input())
    cubic = round(decimal.Decimal(num ** pow_num), 500)
    cubic = cubic.quantize(decimal.Decimal('.0000000001'), rounding=decimal.ROUND_DOWN)
    print(cubic)