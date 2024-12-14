n, *t = map(int, open(0).read().split())
t.sort()
ans = []
q, b = divmod(n, 2)
l = q - 1
if b:
    ans.append(t[q])
    r = q + 1
else:
    r = q
while l >= 0:
    ans.extend((t[l], t[r]))
    l -= 1
    r += 1
print(*ans)