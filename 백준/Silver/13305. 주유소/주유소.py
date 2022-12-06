g = lambda: [*map(int, input().split())]

N = int(input())
dist = g()
cost = g()

ans = cost[0] * dist[0]
Min = cost[0]
for i in range(1, N-1):
    Min = min(Min, cost[i])
    ans += Min * dist[i]
print(ans)