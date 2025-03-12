N, *A = map(int, open(0).read().split())
ans, cur = 2, 2
for i in range(0, N - 2, 2):
    if abs(A[i + 2] - A[i]) in (0, 2):
        cur += 2
    else:
        ans = max(ans, cur)
        cur = 3
print(max(ans, cur - (N & 1)))