g = lambda: [*map(int, input().split())]

from math import gcd
while sum(s:= g()):
    n, m = s
    buf = [g()[-1] for _ in range(n)]
    Sum = sum(buf)
    for i in range(n):
        if buf[i] == 0:
            print('0 / 1')
        else:
            Gcd = gcd(buf[i], Sum)
            buf[i] //= Gcd
            print(f'{buf[i]} / {Sum // Gcd}')