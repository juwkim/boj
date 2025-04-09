N, K, *A = map(int, open(0).read().split())
off = max(0, max(A[i] - A[0] - i * K for i in range(N)))
print(sum(A[0] + i * K + off - A[i] for i in range(N)))