g = lambda: [*map(int, input().split())]

n, p = g()
d = g()
l, r = 0, 0
ans = 0
while r < n:
    vacant = d[r] - d[l] - (r - l)
    if vacant <= p:
        ans = max(ans, d[r] - d[l] + 1 + p - vacant)
        r += 1
    else:
        l += 1
print(ans)