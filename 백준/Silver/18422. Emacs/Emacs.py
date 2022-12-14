g = lambda: [*map(int, input().split())]

N, M = g()
Map = [input() for _ in range(N)]
ans = (Map[0][0] == '*') + Map[0].count('.*')
for i in range(N-1):
    ans += Map[i][0] + Map[i+1][0] == '.*'
for i in range(1, N):
    for j in range(1, M):
        ans += Map[i][j] + Map[i-1][j] + Map[i][j-1] == '*..'
print(ans)