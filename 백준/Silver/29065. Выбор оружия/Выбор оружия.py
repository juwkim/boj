n, m = map(int, input().split())
a, b = zip(*[map(int, input().split()) for _ in range(n)])
p = sorted(range(n), key=lambda i: b[i] - a[i])
part = n - m + 1 >> 1

ans = sum(a)
l = [0] * n
for i in range(n - 1, n - part - 1, -1):
    l[p[i]] = 1
    ans += b[p[i]] - a[p[i]]

for i in range(n - part - 1, part - 1, -1):
    if b[p[i]] - a[p[i]] < 0:
        continue
    ans += b[p[i]] - a[p[i]]
    l[p[i]] = 1

print(ans)
print(*l)