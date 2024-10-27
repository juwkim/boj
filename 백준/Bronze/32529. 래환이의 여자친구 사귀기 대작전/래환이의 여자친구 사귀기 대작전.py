N, M, *A = map(int, open(0).read().split())
ans, cur = -1, 0
for i in range(N - 1, -1, -1):
    cur += A[i]
    if cur >= M:
        ans = i + 1
        break
print(ans)