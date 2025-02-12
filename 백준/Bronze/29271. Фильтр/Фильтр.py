n, r, x, *a = map(int, open(0).read().split())
ans, cur = 0, 0
for num in a:
    p = min(r, cur + num)
    ans += min(x, p)
    cur = max(0, p - x)
print(ans)