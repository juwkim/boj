g = lambda: [*map(int, input().split())]

N, M = g()
a = [0] + g()
cnt = sum(a)
ans = -1
for i, b in enumerate(g()):
    if cnt <= i:
        ans = i
        break
    if a[b]: cnt -= 1
    else:    cnt += 1
    a[b] ^= 1
if ans == -1:
    ans = max(cnt, M)
print(ans)