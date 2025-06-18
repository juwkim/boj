n, a, b, w, h = map(int, input().split())
lo, hi = 0, 10**18
f = lambda p, q: w >= p + d2 and h >= q + d2 and (w // (p + d2)) * (h // (q + d2)) >= n
while hi > lo + 1:
    d2 = (d := lo + hi >> 1) << 1
    if f(a, b) or f(b, a):
        lo = d
    else:
        hi = d
print(lo)