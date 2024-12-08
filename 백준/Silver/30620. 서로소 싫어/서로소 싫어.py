from math import gcd

x, y = map(int, input().split())
if x == y:
    print(0)
else:
    g = gcd(x, y - x)
    if g != 1:
        print(1)
        print(y - x)
    else:
        print(2)
        z = x
        while gcd(x + z, y - x - z) == 1:
            z += x
        print(z)
        print(y - x - z)