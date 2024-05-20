N, M, *A = map(int, open(0).read().split())
A.sort(reverse=True)
ans = 0
for i in range(min((N + 1) // 2, M)):
    if A[i] < 0:
        break
    ans += A[i]
print(ans)