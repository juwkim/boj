k, *p = map(int, open(0).read().split())
cur = 1
for i in range(k + 1):
    weight = 1 << i
    if cur < weight:
        break
    cur += weight * p[i]
print(cur)