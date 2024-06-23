N, K, *A = map(int, open(0).read().split())
ans = 1e9
l, r, cur = 0, 0, 0
while r < N:
    if cur < K:
        cur += A[r] == 1
        r += 1
    else:
        while A[l] == 2:
            l += 1
        ans = min(ans, r - l)
        cur -= 1
        l += 1
if cur == K:
    while A[l] == 2:
        l += 1
    ans = min(ans, r - l)
print(-1 if ans == 1e9 else ans)