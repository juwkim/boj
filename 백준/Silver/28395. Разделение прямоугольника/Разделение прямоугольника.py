import math

def solve(a, b, k, m):
    S = k + 2
    D = S * S - 4 * m
    if D < 0:
        return -1,
    r = math.isqrt(D)
    if r * r != D or S + r & 1:
        return -1,
    x, y = S - r >> 1, S + r >> 1
    if x <= 0 or y <= 0:
        return -1,
    return min([(p - 1, q - 1) for p, q in ((x, y), (y, x)) if p <= a and q <= b], default=(-1,))

for _ in range(int(input())):
    a, b, k, m = map(int, input().split())
    print(*solve(a, b, k, m))