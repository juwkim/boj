N, *A = map(int, open(0).read().split())
root = A[0]
p = [-1] * (max(A) + 1)
for i in range(1, N):
    if A[i] != root and p[A[i]] == -1:
        p[A[i]] = A[i - 1]
print(len(p))
print(*p)