from math import gcd

a0, b0, c0, d, a1, b1, c1, d = map(int, open(0).read().split())
for x, y, z in ((a0 * a1, b0 * a1 + b1 * a0, c0 * a1 + c1 * a0), (a0 * a1, b0 * a1 - b1 * a0, c0 * a1 - c1 * a0), (a0 * a1, b0 * b1 + c0 * c1 * d, b0 * c1 + b1 * c0)):
    g = gcd(x, y, z)
    if z and d:
        print(x // g, y // g, z // g, d)
    else:
        print(x // g, y // g, 0, 0)

x, y, z = a0 * (b1**2 - d * c1**2), a1 * (b0 * b1 - c0 * c1 * d), a1 * (b1 * c0 - b0 * c1)
if x < 0: x, y, z = -x, -y, -z
g = gcd(x, y, z)
if z and d:
    print(x // g, y // g, z // g, d)
else:
    print(x // g, y // g, 0, 0)