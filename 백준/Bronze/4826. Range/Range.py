while True:
    n, m = map(float, input().split())
    if (n, m) == (-1.0, -1.0):
        break
    dist, fuel = [n], [m]
    while True:
        n, m = map(float, input().split())
        if (n, m) == (0.0, 0.0):
            break
        dist.append(n)
        fuel.append(m)
    move = sum(dist[i+1] - dist[i] for i in range(len(dist)-1) if fuel[i] > fuel[i+1])
    cons = sum(fuel[i] - fuel[i+1] for i in range(len(fuel)-1) if fuel[i] > fuel[i+1])
    print(round(move*fuel[-1]/cons))