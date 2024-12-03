N, L, R, *A = map(int, open(0).read().split())
P = A[:L-1] + sorted(A[L-1:R]) + A[R:]
print(+(P == sorted(P)))