n, d, *p = map(int, open(0).read().split())
ans = 1
s, *p = sorted(p)
for a in p:
    if a - s > d:
        ans += 1
        s = a
print(ans)