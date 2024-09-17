n, *p = map(int, open(0).read().split())
d = {num: i for i, num in enumerate(p)}
ans, prev = 0, -1
for i in range(1, n + 1):
    if d[i] < prev:
        ans += 1
    prev = d[i]
print(ans)