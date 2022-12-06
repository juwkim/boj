g = lambda: [*map(int, input().split())]
N, K = g()
A = g()
A += A
cur = sum(A[:K])
ans = cur
for i in range(N - 1):
    cur += A[i + K] - A[i]
    ans = max(ans, cur)
print(ans)