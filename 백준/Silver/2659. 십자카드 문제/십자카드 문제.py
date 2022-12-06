g = lambda: map(int, input().split())
from itertools import product

buf = set()
for a, b, c, d in product(range(1, 10), repeat=4):
    l = [a, b, c, d, a, b, c]
    p, q, r, s = min([l[i:i+4] for i in range(4)])
    num = p * 1000 + q * 100 + r * 10 + s
    buf.add(num)
buf = sorted(buf)

a, b, c, d = g()
l = [a, b, c, d, a, b, c]
p, q, r, s = min([l[i:i+4] for i in range(4)])
num = p * 1000 + q * 100 + r * 10 + s
ans = 1 + buf.index(num)
print(ans)