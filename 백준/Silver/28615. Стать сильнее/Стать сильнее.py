n, *a = map(int, open(0).read().split())
a.sort()
cur, ans = 0, 1
for i in range(n):
    while cur < n and a[cur] <= a[i] + 1:
        cur += 1
    ans = max(ans, cur - i)
print(ans)