g = lambda: [*map(int, input().split())]
N, M = g()
bus = g()
cost = [g() for _ in range(N)]
print(sum(cost[a-1][b-1] for a, b in zip(bus, bus[1:])))