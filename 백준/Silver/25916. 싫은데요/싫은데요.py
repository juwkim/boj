N, M, *A = map(int, open(0).read().split())

ans = 0
l, r, cur = 0, 0, 0
while r < N:
    if cur + A[r] <= M:
        cur += A[r]
        r += 1
        ans = max(ans, cur)
    else:
        cur -= A[l]
        l += 1
print(ans)