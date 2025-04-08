import math
for l in map(str.rstrip, open(0)):
    i, j, k = l.index('.'), l.index('('), l.index(')')    
    a = int("".join(c for c in l if c.isdigit())) - int(float(l[:j]) * 10 ** (j - i - 1))
    b = 10 ** (k - i - 2) - 10 ** (j - i - 1)
    g = math.gcd(a, b)
    print(f"{l} = {a // g} / {b // g}")