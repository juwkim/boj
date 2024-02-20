from math import sqrt, acos
pi = 3.14159265358979
for _ in range(int(input())):
    s, r = map(int, input().split())
    if s >= 2 * r:
        ans = pi * r * r
    elif r * sqrt(2) >= s:
        ans = s * s
    else:
        ans = 2 * s * sqrt(r * r - s * s / 4) + r * r * (pi - 4 * acos(0.5 * s / r))
    print(f"{ans:.2f}")