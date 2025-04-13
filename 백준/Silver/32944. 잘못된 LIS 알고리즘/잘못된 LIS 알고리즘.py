N, M, K = map(int, input().split())
if M == N:
    print(-1)
else:
    print(*range(1, K), N, *range(N - 1, M, -1), *range(K, M + 1))