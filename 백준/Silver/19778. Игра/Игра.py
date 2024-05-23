g = lambda: [*map(int, input().split())]

n, m = g()
l1, r1 = g()
l2, r2 = g()
a, b, c = 0, 0, 0
for h in g():
    if l1 <= h <= r1 and l2 <= h <= r2: c += 1
    elif l1 <= h <= r1: a += 1
    elif l2 <= h <= r2: b += 1
p, q = 0, 0
for i in range(m):
    if i & 1:
        if c: c -= 1; q += 1
        elif b: b -= 1; q += 1
    else:
        if c: c -= 1; p += 1
        elif a: a -= 1; p += 1
print(("Draw", "Petya", "Vasya")[(p > q) - (p < q)])