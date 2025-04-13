n, xa, ya, xb, yb = map(int, open(0).read().split())
d = 0
if xa == xb:
    ya, yb = sorted((ya, yb))
    d = max(0, min(n, yb) - max(-1, ya))
elif ya == yb:
    xa, xb = sorted((xa, xb))
    d = max(0, min(n, xb) - max(-1, xa))
print((n * (n + 1) >> 1)**2 + d * (d - 1) * (n + 1) // 2)