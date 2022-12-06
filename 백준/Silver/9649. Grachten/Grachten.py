g = lambda: [*map(int, input().split())]

from math import gcd
while True:
    try:
        AB, AC, BD = g()
        
        a = AB * AC
        b = BD - AC
        GCD = gcd(a, b)
        a //= GCD
        b //= GCD
        print(f'{a}/{b}')
    except:
        break