g = lambda: [*map(int, input().split())]
N, L = g()
ans = False
for i in range(L, min(101, 2 + int(((8 * N + 1) ** .5 - 1) // 2))):
    r, c = divmod(N, i)
    num = i >> 1
    if i&1:
        if c == 0:
            ans = [*range(r - num, r + num + 1)]
            break
    else:
        if c == num:
            ans = [*range(r - num + 1, r + num + 1)]
            break
if ans:
    print(*ans)
else:
    print(-1)