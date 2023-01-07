from decimal import Decimal, getcontext
 
getcontext().prec = 1024
base = (3 + Decimal(5).sqrt())
for t in range(1, int(input()) + 1):
    exp = int(input())
    if exp >= 103:
        exp = (exp - 3) % 100 + 3

    ans = int(base ** exp) % 1000
    print(f"Case #{t}: {ans:#03d}")