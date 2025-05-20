N, *A = map(int, open(0).read().split())
ans, Min = 0, 1e9
for i in range(N - 1, -1, -1):
    Min = min(Min, A[i])
    ans += Min
print(ans)