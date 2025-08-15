from math import gcd, lcm

def solve(p, q):
    g = gcd(p, q)
    return p // g, q // g

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    a, b = solve(a, b)
    c, d = solve(c, d)
    m, n = solve(gcd(a, c), lcm(b, d))
    x, y = solve(lcm(a, c), gcd(b, d))
    print(f"{m}/{n} {x}/{y}")