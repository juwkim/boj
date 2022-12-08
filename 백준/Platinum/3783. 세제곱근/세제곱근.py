from decimal import *
getcontext().prec = 1000
pow_num = Decimal('1') / 3
for _ in range(int(input())):print(round(Decimal(Decimal(input()) ** pow_num), 500).quantize(Decimal('.0000000001'), rounding=ROUND_DOWN))