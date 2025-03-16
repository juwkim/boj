N, *L = map(int, open(0).read().split())
L.sort()
l, r = 0, N - 1
ans = 0
while l <= r:
    if l == r:
        ans += 1
        break
    l += L[r]
    r -= 1
    ans += 2
print(ans)