from itertools import combinations
g = lambda: [*map(int, input().split())]

N, M = g()
city = [g() for _ in range(N)]
homes, chickens = [], []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            homes.append((i, j))
        elif city[i][j] == 2:
            chickens.append((i, j))

dist = {home: {} for home in homes}
for home in homes:
    for chicken in chickens:
        d = abs(home[0] - chicken[0]) + abs(home[1] - chicken[1])
        dist[home][chicken] = d

ans = 1e9
for alive in combinations(chickens, M):
    num = sum(min(dist[home][store] for store in alive) for home in homes)
    ans = min(ans, num)
print(ans)