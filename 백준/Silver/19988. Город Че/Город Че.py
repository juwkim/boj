n, r, *d = map(int, open(0).read().split())
ans, j = n * (n - 1) >> 1, 0
for i in range(n):
    while j + 1 < n and d[j + 1] - d[i] <= r:
        j += 1
    ans += i - j
print(ans)