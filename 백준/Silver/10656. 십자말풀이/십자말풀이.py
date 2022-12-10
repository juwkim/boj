N, M = map(int, input().split())
Map = [[*input()] for _ in range(N)]
buf = []
for i in range(N):
    for j in range(M):
        if (j == 0 or Map[i][j-1] == '#') and j < M - 2 and Map[i][j] + Map[i][j+1] + Map[i][j+2] == '...':
            buf.append((i+1, j+1))
        elif (i == 0 or Map[i-1][j] == '#') and i < N - 2 and Map[i][j] + Map[i+1][j] + Map[i+2][j] == '...':
            buf.append((i+1, j+1))
print(len(buf))
for line in buf:
    print(*line)