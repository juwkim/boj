N, M = map(int, input().split())
graph = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


cnt = N * (N - 1) - 2 * M
ans = []
while cnt:
    buf = set()
    for m in range(1, N + 1):
        for s in range(1, N + 1):
            for e in range(1, N + 1):
                if s != e and (s, e) not in buf and graph[s][e] == 0 and graph[s][m] and graph[m][e]:
                    buf.add((s, e))
    cnt -= len(buf)
    ans.append(len(buf) // 2)
    for s, e in buf:
        graph[s][e] = 1

print(len(ans))
for num in ans:
    print(num)