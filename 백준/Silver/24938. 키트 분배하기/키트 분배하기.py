N, *A = map(int, open(0).read().split())
ans, cnt = 0, sum(A) // N
for i in range(N - 1):
    ans += abs(A[i] - cnt)
    A[i + 1] += A[i] - cnt
print(ans)