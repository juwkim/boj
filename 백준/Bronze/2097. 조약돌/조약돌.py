from math import isqrt
N = int(input())
if N <= 4:
    print(4)
else:
    d = isqrt(N)
    if d * d == N:
        print(4 * d - 4)
    elif d * (d + 1) >= N:
        print(4 * d - 2)
    else:
        print(4 * d)