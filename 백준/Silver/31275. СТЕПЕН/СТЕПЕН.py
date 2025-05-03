n, m, *a = map(int, open(0).read().split())
ans = 0
for i in range(n):
    ans = (ans + pow(a[i], i + 2, m)) % m
print(ans)