g = lambda: [*map(int, input().split())]
N = int(input())
Map = [g() for _ in range(N)]
cnt = [[0] * N for _ in range(N)]
cnt[0][0] = 1
for i in range(N):
    for j in range(N):
        if i + Map[i][j] < N:
            cnt[i + Map[i][j]][j] += cnt[i][j]
        if j + Map[i][j] < N:
            cnt[i][j + Map[i][j]] += cnt[i][j]
print(cnt[N-1][N-1] >> 2)