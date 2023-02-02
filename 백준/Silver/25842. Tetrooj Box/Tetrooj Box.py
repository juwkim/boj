def g(): return [*map(int, input().split())]

b, r = g()
ans = [0] * (b + 1)
for _ in range(r):
    w, h, c = g()
    l = max(ans[c:c+w])
    for i in range(c, c + w):
        ans[i] = l + h
print(max(ans))