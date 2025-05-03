l = open(0).read().splitlines()
tc, idx = 1, 0
while idx < len(l):
    dist = [[float('inf')] * 21 for _ in range(21)]
    for i in range(1, 21):
        dist[i][i] = 0
    for i in range(1, 20):
        cnt, *nums = list(map(int, l[idx].split()))
        for j in nums:
            dist[i][j], dist[j][i] = 1, 1
        idx += 1
    for k in range(1, 21):
        for i in range(1, 21):
            for j in range(1, 21):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    q = int(l[idx])
    idx += 1
    print(f'Test Set #{tc}')
    for _ in range(q):
        a, b = map(int, l[idx].split())
        print(f'{a:2d} to {b:2d}: {dist[a][b]}')
        idx += 1
    print()
    tc += 1