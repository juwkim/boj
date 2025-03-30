from statistics import median

n, R, *a = map(int, open(0).read().split())
b, prv = [0] * n, -1e10
for i in sorted(range(n), key=lambda i: a[i]):
    b[i] = a[i] + median((-R, prv + 1 - a[i], R))
    prv = b[i]
print(len({*b}))
print(*b)