a, b, c, d = map(int, input().split())
a &= 1
c &= 1
k = min(b, d)
b -= k
d -= k

ans = 0
if a:
    if b:
        b -= 1
        ans += 1
    elif d:
        d -= 1
        ans += 1
    elif c:
        c -= 1
        ans += 2
if c:
    if b:
        b -= 1
        ans += 1
    elif d:
        d -= 1
        ans += 1
ans += b + d
print(ans)