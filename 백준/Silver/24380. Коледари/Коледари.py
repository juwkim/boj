k, n, *a = map(int, open(0).read().split())
px, idx = 0, [None] * k
idx[0] = -1
ans = "no kravaiche"
for i in range(n):
    px += a[i]
    mod = px % k
    if idx[mod] is not None:
        ans = " ".join(str(idx) for idx in range(idx[mod] + 2, i + 2))
        break
    idx[mod] = i
print(ans)