import math
from collections import Counter

def v_factor(n, p):
    c = 0
    while n % p == 0:
        n //= p
        c += 1
    return n, c

def factorize(n):
    f, d = Counter(), 2
    while d * d <= n:
        while n % d == 0:
            f[d] += 1
            n //= d
        d += 1
    if n > 1:
        f[n] += 1
    return f

def euler_phi(n):
    if n == 1:
        return 1
    d = 2
    res, x = n, n
    while d * d <= x:
        if x % d == 0:
            while x % d == 0:
                x //= d
            res -= res // d
        d += 1
    if x > 1:
        res -= res // x
    return res

def multiplicative_order_10(m):
    phi = euler_phi(m)
    d = phi
    for p in factorize(phi):
        while d % p == 0 and pow(10, d // p, m) == 1:
            d //= p
    return d

for line in [*open(0)][:-1]:
    x, y = map(int, line.split())
    tmp, a = v_factor(y // math.gcd(x, y), 2)
    m, b = v_factor(tmp, 5)
    if m == 1:
        cycle = 0
    else:
        cycle = multiplicative_order_10(m)
    print(max(a, b), cycle)