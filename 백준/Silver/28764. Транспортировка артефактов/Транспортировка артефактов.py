from itertools import product

a1, b1, a2, b2, a3, b3 = map(int, open(0))
ans = 1e9
for l in product(((a1, b1), (b1, a1)), ((a2, b2), (b2, a2)), ((a3, b3), (b3, a3))):
    s, t = map(sorted, zip(*l))
    ans = min(ans, sum(s) * t[2], (s[1] + s[2]) * max(t[0] + t[1], t[2]))
print(ans)