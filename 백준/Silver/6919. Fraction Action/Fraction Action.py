from math import gcd
a, b = int(input()), int(input())
GCD = gcd(a, b)
a, b = a // GCD, b // GCD
q, r = divmod(a, b)
if q and r:
    print(q, f'{r}/{b}')
elif q:
    print(q)
elif r:
    print(f'{r}/{b}')
else:
    print(0)