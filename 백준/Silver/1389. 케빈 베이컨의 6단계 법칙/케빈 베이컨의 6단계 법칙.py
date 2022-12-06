g = lambda: [*map(int, input().split())]

N, M = g()
d = [[1e9] * N for _ in range(N)]
for i in range(N):
    d[i][i] = 0
for _ in range(M):
    a, b = g()
    d[a - 1][b - 1] = 1
    d[b - 1][a - 1] = 1
    
for m in range(N):
    for s in range(N):
        for e in range(N):
            num = d[s][m] + d[m][e]
            if d[s][m] and d[m][e]:
                d[s][e] = min(d[s][e], num)

ans = min(range(N), key=lambda x: (sum(d[x]), x)) + 1
print(ans)