n, m = map(int, input().split())
a = [input().split() for _ in range(n)]
idxs = []
for i in range(n):
    for j in range(m):
        if a[i][j] == '1':
            idxs.append((i, j))
            if len(idxs) == 2:
                break
    if len(idxs) == 2:
        break
(i1, j1), (i2, j2) = idxs
ans = 0
if i1 < i2:
    ans = max(i2, n - i1 - 1) * m
j1, j2 = sorted((j1, j2))
if j1 < j2:
    ans = max(ans, j2 * n, (m - j1 - 1) * n)
print(ans)