N, M, *A = map(int, open(0).read().split())
A.sort()
l, r = 0, N - 1
ans = 0
while l < r:
    if A[l] + A[r] >= M:
        ans += 1
        l += 1
        r -= 1
    else:
        l += 1
print(ans)