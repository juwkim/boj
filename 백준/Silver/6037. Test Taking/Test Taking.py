N, K, *A = map(int, open(0).read().split())
A.sort()
ans = max(N - A[-1], A[0])
for i in range(K - 1):
    ans = max(ans, A[i+1] - A[i] >> 1)
print(ans)