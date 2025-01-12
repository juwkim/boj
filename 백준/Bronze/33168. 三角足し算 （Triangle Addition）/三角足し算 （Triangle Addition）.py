N, *A = map(int, open(0).read().split())
for _ in range(N - 1):
    A = [a + b for a, b in zip(A, A[1:])]
    print(*A)