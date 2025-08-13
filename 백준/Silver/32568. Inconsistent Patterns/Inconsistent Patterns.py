N, M = map(int, input().split())
for _ in range(N - 2):
    print(1, 1, 1, 2)
print(1, 1, M - 2 * N + 1, M - 2 * N + 2)
print(M - 2 * N, M - N + 1, 1, 2)