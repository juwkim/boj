h, k, u, s = map(int, input().split())

dist = 0
while h:
    u += s
    u -= max(1, u // 10)
    if u >= k:
        h += 1
    elif u > 0:
        h -= 1
        if h == 0:
            u = 0
    else:
        h = 0
        u = 0
    dist += u
    if s > 0:
        s -= 1
print(dist)