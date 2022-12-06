e, f, c = map(int, input().split())
s, total = e + f, 0
while s >= c:
    a = s // c
    total += a
    s -= a*(c-1)
print(total)