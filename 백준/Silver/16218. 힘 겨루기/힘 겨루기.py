g = lambda: [*map(int, input().split())]

N, K = g()
a, b = 0, 0
ans = 0
for _ in range(N):
    s, t = g()
    a += s
    b += t
    if a >= K or a + s // 2 - b >= 50:
        ans = 1
        break
        
    if a + s // 2 >= K:
        if b >= K:
            ans = -1
        else:
            ans = 1
        break
    if b >= K:
        ans = -1
        break
print(ans)