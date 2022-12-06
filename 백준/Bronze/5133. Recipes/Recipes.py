g = lambda: [*map(int, input().split())]

import math
for i in range(1, 1 + int(input())):
    I, C = g()
    print(f'Data Set {i}:')
    for _ in range(I):
        a, l = input().split()
        b, c = l.split('/')
        a, b, c = map(int, [a, b, c])
        a *= C
        b *= C
        r, b = divmod(b, c)
        a += r
        gcdbc = math.gcd(b, c)
        b //= gcdbc
        c //= gcdbc
        if b:
            print(f'{a} {b}/{c}')
        else:
            print(a)
    print()