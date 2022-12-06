K, N = map(int, input().split())
print(-1 if N == 1 else (N * (K + 1) - 2) // (N - 1))