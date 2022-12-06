g = lambda: [*map(int, input().split())]


A, B, C, D, E = g()
ans = A + B + C
E -= min(B, E)

if D <= C:
    num = E - 2 * (C - D)
    if num > 0:
        ans += (num + 4) // 5
else:
    D -= C
    r, q = divmod(D, 2)
    ans += r
    E -= min(r, E)
    if q:
        ans += 1
        E -= min(3, E)
    ans += (E + 4) // 5
print(ans)    