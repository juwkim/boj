g = lambda: [*map(int, input().split())]

N, M = g()
Map = [g() for _ in range(N)]

ans = 1e9
for i in range(N):
    for j in range(M):
        cost = 0
        for s in range(N):
            for t in range(M):
                cost += Map[s][t] * (abs(s - i) + abs(t - j))
        ans = min(ans, cost)
print(ans)