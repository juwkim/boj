for l in open(0):
    a, b, c, d, m, t = map(float, l.split())
    lo, hi = 0, 1e9
    while hi - lo > 1e-8:
        v = (lo + hi) / 2
        if m * (a * v**3 + b * v**2 + c * v + d) < t:
            lo = v
        else:
            hi = v
    print(f"{int(lo * 100)/100:.2f}")