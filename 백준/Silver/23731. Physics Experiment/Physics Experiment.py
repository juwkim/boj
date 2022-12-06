from decimal import *
getcontext().rounding = ROUND_HALF_UP
S = input()
num = Decimal(S)
for i in range(1, 1 + len(S)):
    tmp = round(num, -i)
    if tmp > num:
        num = tmp
print(int(num))