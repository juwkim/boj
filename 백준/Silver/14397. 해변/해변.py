g = lambda: [*map(int, input().split())]

N, M = g()
Map = [input() for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(M-1):
        ans += Map[i][j] != Map[i][j+1]

for i in range(1, N, 2):
    if i != N - 1:
        for j in range(M-1):
            ans += Map[i][j] != Map[i-1][j]
            ans += Map[i][j] != Map[i-1][j+1]
            ans += Map[i][j] != Map[i+1][j]
            ans += Map[i][j] != Map[i+1][j+1]
        ans += Map[i][M-1] != Map[i-1][M-1]
        ans += Map[i][M-1] != Map[i+1][M-1]
    else:
        for j in range(M-1):
            ans += Map[i][j] != Map[i-1][j]
            ans += Map[i][j] != Map[i-1][j+1]
        ans += Map[i][M-1] != Map[i-1][M-1]
print(ans)