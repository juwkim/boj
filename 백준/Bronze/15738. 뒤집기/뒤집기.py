g = lambda: [*map(int, input().split())]

N, K, M = g()
input()
for _ in range(M):
    op = int(input())
    if op >= K:
        K = 1 + op - K
    elif K >= N + op + 1:
        K = 1 + op - K + 2 * N
print(K)