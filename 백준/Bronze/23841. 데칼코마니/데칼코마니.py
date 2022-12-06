N, M = map(int, input().split())
p = [[*input()] for _ in range(N)]
for i in range(N):
    for j in range(M):
        p[i][j] = max(p[i][j], p[i][M-1-j])
for i in range(N):
    print(*p[i], sep='')