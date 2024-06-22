n, x, y, *a = map(int, open(0).read().split())
p, q = min(range(n), key=lambda i: a[i]), 0
for j in range(n):
    if a[p] + a[j] <= x and a[j] - a[p] >= y:
        q = j + 1
        break
if q: print(p + 1, q)
else: print(0)