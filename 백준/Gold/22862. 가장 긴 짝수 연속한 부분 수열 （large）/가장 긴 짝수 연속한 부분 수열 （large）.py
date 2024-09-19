N, K, *A = map(int, open(0).read().split())
ans, l, r, cnt = 0, 0, 0, 0
while r < N:
    if A[r] & 1:
        if cnt == K:
            cnt -= A[l] & 1
            l += 1
        else:
            cnt += 1
            r += 1
    else:
        r += 1
        ans = max(ans, r - l - cnt)
print(ans)