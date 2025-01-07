import sys
input = lambda: sys.stdin.readline().rstrip()

d = {}
for _ in range(int(input())):
    s, m = input().split()
    d[s] = float(m)
ans, prv, cnt = 0, None, 0
for c in input():
    if c.isdigit():
        cnt = cnt * 10 + int(c)
    elif c.isupper():
        if prv:
            if cnt:
                ans += d[prv] * cnt
            else:
                ans += d[prv]
        prv, cnt = c, 0
    else:
        prv += c
if prv:
    if cnt:
        ans += d[prv] * cnt
    else:
        ans += d[prv]
print(f"{ans:.2f}")