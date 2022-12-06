from decimal import Decimal, getcontext
getcontext().prec = 50

for _ in range(int(input())):
    a = 0
    while (s := input().rstrip()) != '0':
        a += Decimal(s)
    print(str(a).rstrip('0').rstrip('.'))