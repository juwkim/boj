N, K, *d = map(int, open(0).read().split())
d = [1e9] + d + [1e9]
l, r = K - 1, K
dl, dr = d[l], d[r]
ans = 0
while l or r < N:
    if dr < dl:
        ans += dr
        dl += dr
        r += 1
        dr = d[r]
    else:
        ans += dl
        dr += dl
        l -= 1
        dl = d[l]
print(ans)