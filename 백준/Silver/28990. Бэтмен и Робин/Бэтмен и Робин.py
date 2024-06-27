n, *a = map(int, open(0).read().split())

a1, a2 = a[::2], a[1::2]
b1, b2 = min(a1), max(a2)
print(sum(a1) - sum(a2) + 2 * (b2 - b1) * (b2 > b1))