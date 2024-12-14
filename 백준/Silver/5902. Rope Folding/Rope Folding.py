N, L, *a = map(int, open(0).read().split())
a.sort()
ans = 0
for x in range(1, 2 * L):
    for i in range(N):
        if 0 < x - a[i] < L and x - a[i] not in a:
            break
    else:
        ans += 1
print(ans)