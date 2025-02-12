N, *A = map(int, open(0).read().split())
A.sort()
ans = 0
for i in range(N - 1):
    ans += (A[i + 1] - A[i]) * (i + 1) * (N - i - 1)
print(ans)