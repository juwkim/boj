N, M, *A = map(int, open(0).read().split())
ans, i = 0, 1
while i < N:
    if abs(A[i] - A[i - 1]) < M:
        ans += 1
        i += 2
    else:
        i += 1
print(ans)