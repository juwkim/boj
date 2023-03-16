g = lambda: [*map(int, input().split())]

N, M = g()
Map = [[0] * (M + 1)] + [[0] + g() for _ in range(N)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        Map[i][j] += max(Map[i][j-1], Map[i-1][j])
ans = [Map[i][M] for i in range(1, N + 1)]
print(*ans)