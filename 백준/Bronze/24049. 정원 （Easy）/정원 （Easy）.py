g = lambda: [*map(int, input().split())]
N, M = g()
left = g()
a = [[0] + g()] + [[0] * (M + 1) for _ in range(N)]
for i in range(N):
    a[i+1][0] = left[i]
for i in range(1, 1 + N):
    for j in range(1, 1 + M):
        a[i][j] = a[i][j-1] ^ a[i-1][j]
print(a[N][M])