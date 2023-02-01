from math import gcd
def g(): return [*map(int, input().split())]

n, b = g()
p, q = 0, 0
for _ in range(n):
    x, y = g()
    p += y - b
    q += x

if n == 1 or q == 0:
    print('EZPZ')
else:
    GCD = gcd(p, q)
    p, q  = p // GCD, q // GCD
    if q < 0:
        p = -p
        q = -q
    if q == 1:
        print(p)
    else:
        print(f'{p}/{q}')