from math import gcd
for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    p = abs(a * d - b * c)
    q = b * d
    GCD = gcd(p, q)
    p //= GCD
    q //= GCD
    if p == 1:
        print(f'{p}/{q}')
    else:
        print('NOT NEIGHBORS')