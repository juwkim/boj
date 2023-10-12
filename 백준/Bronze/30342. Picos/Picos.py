N, M, T, K = map(int, input().split())
n = (K + T - 1) // T
q, r = divmod(N, M)
print(M * min(q, n) * (2 * K - T * (min(q, n) - 1)) // 2 + (q < n) * (K - T * q) * r)