from math import gcd

for l in open(0):
    n, *p = map(int, l.split())
    a, b, *k = [int(x) - 2 for x in p]
    g = gcd(a, b)
    for num in k:
        g = gcd(g, num)
    ans = sum([a, b, *k]) // g
    print(g, ans)