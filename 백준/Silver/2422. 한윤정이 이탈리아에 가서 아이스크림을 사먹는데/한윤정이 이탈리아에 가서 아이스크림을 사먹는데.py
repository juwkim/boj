g = lambda: [*map(int, input().split())]

N, M = g()
buf = [bytearray(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = sorted(g())
    buf[a][b] = 1

ans = 0
for i in range(1, N-1):
    for j in range(i+1, N):
        if buf[i][j] == 0:
            for k in range(j+1, N+1):
                ans += buf[i][k] == 0 and buf[j][k] == 0
print(ans)