g = lambda: [*map(int, input().split())]

N, M = g()
space = [[[0] * (N + 2) for _ in range(N + 2)] for _ in range(N + 2)]
for _ in range(M):
    i, j, k = g()
    space[i][j][k] = 1

ans = 0
for i in range(1, N + 1):
    for j in range(1, N + 1):
        for k in range(1, N + 1):
            ans += all(space[a][b][c] for a, b, c in ((i, j, k), (i-1, j, k), (i+1, j, k), (i, j-1, k), (i, j+1, k), (i, j, k-1), (i, j, k+1)))
print(ans)