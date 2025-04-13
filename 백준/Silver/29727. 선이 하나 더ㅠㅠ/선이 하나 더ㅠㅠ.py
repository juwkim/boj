n, xa, ya, xb, yb = map(int, open(0).read().split())
ans = (n * (n + 1) >> 1)**2
if xa == xb:
    ya, yb = sorted((ya, yb))
    d = max(0, min(n, yb) - max(-1, ya))
    ans += d * (d - 1) * (n + 1) >> 1
elif ya == yb:
    xa, xb = sorted((xa, xb))
    d = max(0, min(n, xb) - max(-1, xa))
    ans += d * (d - 1) * (n + 1) >> 1
print(ans)