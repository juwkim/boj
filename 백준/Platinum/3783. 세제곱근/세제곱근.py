import decimal
decimal.getcontext().prec = 1000

for _ in range(int(input())):
    N = input()
    num = decimal.Decimal(N)
    pow_num = decimal.Decimal('1') / decimal.Decimal('3')
    
    cubic = decimal.Decimal(num ** pow_num)
    cubic = round(cubic, 500)
    # cubic = cubic.quantize(decimal.Decimal('.0000000000000000000001'), rounding=decimal.ROUND_HALF_UP)
    cubic = cubic.quantize(decimal.Decimal('.0000000001'), rounding=decimal.ROUND_DOWN)
    print(cubic)