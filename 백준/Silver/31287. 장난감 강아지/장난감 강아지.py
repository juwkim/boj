import sys
input = lambda: sys.stdin.readline().rstrip()

N, K = map(int, input().split())
buf = []
x, y = 0, 0
for c in input():
    match c:
        case 'R': x += 1
        case 'L': x -= 1
        case 'U': y += 1
        case 'D': y -= 1
    buf.append((x, y))
ans = "NO"
xoff, yoff = buf[-1]
if xoff and yoff:
    for x, y in buf:
        k1, r1 = divmod(-x, xoff)
        k2, r2 = divmod(-y, yoff)
        if r1 or r2:
            continue
        if k1 == k2 and 0 <= k1 < K:
            ans = "YES"
            break
elif xoff:
    for x, y in buf:
        if y:
            continue
        k, r = divmod(-x, xoff)
        if r == 0 and 0 <= k < K:
            ans = "YES"
            break
elif yoff:
    for x, y in buf:
        if x:
            continue
        k, r = divmod(-y, yoff)
        if r == 0 and 0 <= k < K:
            ans = "YES"
            break
else:
    ans = "YES"
print(ans)

"""
x + (0 ~ K - 1) * xoff = 0
y + (0 ~ K - 1) * yoff = 0
"""
