from math import isqrt
while N:= int(input()):
    r = isqrt(N)
    while N % r:
        r -= 1
    c = N // r
    print(f'Minimum perimeter is {r + c << 1} with dimensions {r} x {c}')