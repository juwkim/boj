import sys
input = sys.stdin.readline

for tc in range(1, int(input()) + 1):
    M, N, P = map(int, input().split())
    idx = {name: i for i, name in enumerate(input().split())}
    dist = [[1e9] * M for _ in range(M)]
    for i in range(M):
        dist[i][i] = 0
    for _ in range(N):
        a, b = input().split()
        u, v = idx[a], idx[b]
        dist[u][v], dist[v][u] = 1, 1
    for m in range(M):
        for s in range(M):
            for e in range(M):
                dist[s][e] = min(dist[s][e], dist[s][m] + dist[m][e])
    print(f"DATA SET {tc}\n")
    for _ in range(P):
        size, a, b = input().split()
        src, dst = idx[a], idx[b]
        ans = "NO SHIPMENT POSSIBLE"
        if dist[src][dst] != 1e9:
            ans = f"${int(size) * dist[src][dst] * 100}"
        print(ans)
    print()