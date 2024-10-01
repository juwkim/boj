n, *a = map(int, open(0).read().split())
a.sort()
i, cur, ans = 0, 0, 1
while cur != n:
    while cur < n and a[cur] <= a[i] + 1:
        cur += 1
    ans = max(ans, cur - i)
    i += 1
print(ans)