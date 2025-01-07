d = {}
for _ in range(int(input())):
    s, m = input().split()
    d[s] = float(m)
ans, prv, cnt = 0, None, 0
for c in input():
    if c.isdigit():
        cnt = cnt * 10 + int(c)
    elif c.isupper():
        if prv: ans += d[prv] * max(cnt, 1)
        prv, cnt = c, 0
    else:
        prv += c
if prv: ans += d[prv] * max(cnt, 1)
print(ans)