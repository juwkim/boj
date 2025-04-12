from math import isqrt

X, Y, c = map(int, input().split())
d = X**2 + Y**2
if d == 0:
    print(0)
elif d < c**2:
    print(2)
else:
    i = isqrt(d)
    if i**2 == d:
        print((i + c - 1) // c)
    else:
        print(i // c + 1)