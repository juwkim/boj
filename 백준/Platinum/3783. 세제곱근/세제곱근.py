import decimal
decimal.getcontext().prec = 1000
pow_num = decimal.Decimal('1') / 3
for _ in range(int(input())):print(round(decimal.Decimal(decimal.Decimal(input()) ** pow_num), 500).quantize(decimal.Decimal('.0000000001'), rounding=decimal.ROUND_DOWN))