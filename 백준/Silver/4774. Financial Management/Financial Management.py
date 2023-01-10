from decimal import *
avg = sum(Decimal(input()) for _ in range(12)) / 12
print("$%.2f" % avg.quantize(Decimal('.01'), rounding=ROUND_HALF_UP))