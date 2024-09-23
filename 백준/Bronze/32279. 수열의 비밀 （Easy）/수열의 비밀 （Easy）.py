n, p, q, r, s, a1 = map(int, open(0).read().split())
a = [0, a1] + [0] * (n - 1)
ans = a1
for i in range(2, n + 1):
    if i & 1:
        a[i] = r * a[i // 2] + s
    else:
        a[i] = p * a[i // 2] + q
    ans += a[i]
print(ans)